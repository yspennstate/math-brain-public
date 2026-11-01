"""No compiler processes: exercise CLI wiring and filesystem evidence boundaries."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch
import uuid

import lean_check
from proof_receipt import digest

ROOT = Path(__file__).resolve().parent
RAW = b'theorem Target : True := True.intro\n'
GOOD = "TARGET_KIND Target: theorem=true\n'Target' does not depend on any axioms\n"


def guard(*paths):
    """Refuse to write fixtures outside this folder's mock_controls directory."""
    base = (ROOT / 'mock_controls').resolve()
    for p in paths:
        Path(p).resolve().relative_to(base)


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.folder = ROOT / 'mock_controls' / uuid.uuid4().hex
        self.compiler = self.folder / 'compiler_fixture.bin'
        self.source = self.folder / 'Source.lean'
        guard(self.folder, self.compiler, self.source)
        self.folder.mkdir(parents=True)
        self.compiler.write_bytes(b'not an executable; mocked compiler only')
        self.source.write_bytes(RAW)
        self.stack = contextlib.ExitStack()
        self.stack.enter_context(patch.object(lean_check, 'LEAN', self.compiler))
        self.admission = self.stack.enter_context(patch.object(lean_check, 'admission'))
        self.runner = self.stack.enter_context(patch.object(lean_check, 'run', return_value=subprocess.CompletedProcess([], 0, GOOD, '')))
        self.addCleanup(self.stack.close)

    def call(self, **overrides):
        args = dict(target='Target', reviewed_sha256=digest(RAW),
                    source_path=self.source, output_root=self.folder, use_mathlib=False)
        args.update(overrides)
        guard(self.folder)
        return lean_check.check_source(RAW, **args)

    def test_file_check_generates_actual_target_queries(self):
        r = self.call()
        self.assertTrue(r['result']['formal_target_verified'])
        checked = Path(self.runner.call_args.args[0][1])
        body = checked.read_text(encoding='utf-8')
        self.assertIn('getConstInfo ``Target', body)
        self.assertIn('#print axioms Target', body)
        self.assertEqual(self.source.read_bytes(), RAW)

    def test_cli_file_propagates_target_and_review(self):
        fake = dict(result=dict(status='FORMAL_TARGET_VERIFIED', formal_target_verified=True,
                                source_sha256=digest(RAW)), compiler_output='', seconds=0)
        with patch.object(lean_check, 'check_source', return_value=fake) as check, contextlib.redirect_stdout(io.StringIO()):
            rc = lean_check.main(['--file', str(self.source), '--target', 'Target', '--reviewed-sha256', digest(RAW), '--core'])
        self.assertEqual(rc, 0)
        self.assertEqual(check.call_args.kwargs['target'], 'Target')
        self.assertEqual(check.call_args.kwargs['reviewed_sha256'], digest(RAW))
        self.assertEqual(check.call_args.args[0], RAW)

    def test_source_deleted_during_compile(self):
        def fake_run(*args, **kwargs):
            guard(self.source)
            self.source.unlink()
            return subprocess.CompletedProcess([], 0, GOOD, '')
        self.runner.side_effect = fake_run
        self.assertEqual(self.call()['result']['status'], 'EVIDENCE_DRIFT_OR_MISSING')

    def test_source_changed_during_compile(self):
        def fake_run(*args, **kwargs):
            guard(self.source)
            self.source.write_bytes(RAW + b'-- changed\n')
            return subprocess.CompletedProcess([], 0, GOOD, '')
        self.runner.side_effect = fake_run
        self.assertFalse(self.call()['result']['formal_target_verified'])

    def test_generated_source_changed_during_compile(self):
        def fake_run(argv, **kwargs):
            guard(argv[1])
            Path(argv[1]).write_bytes(b'theorem Different : True := True.intro\n')
            return subprocess.CompletedProcess([], 0, GOOD, '')
        self.runner.side_effect = fake_run
        self.assertFalse(self.call()['result']['formal_target_verified'])

    def test_compiler_changed_during_compile(self):
        def fake_run(*args, **kwargs):
            guard(self.compiler)
            self.compiler.write_bytes(b'different mock compiler')
            return subprocess.CompletedProcess([], 0, GOOD, '')
        self.runner.side_effect = fake_run
        self.assertFalse(self.call()['result']['formal_target_verified'])

    def test_review_mismatch_launches_nothing(self):
        with self.assertRaises(ValueError):
            self.call(reviewed_sha256='0' * 64)
        self.runner.assert_not_called()

    def test_injected_target_launches_nothing(self):
        with self.assertRaises(ValueError):
            self.call(target='Target\n#eval 1')
        self.runner.assert_not_called()

    def test_admission_hold_launches_nothing(self):
        self.admission.side_effect = RuntimeError('pressure')
        with self.assertRaises(RuntimeError):
            self.call()
        self.runner.assert_not_called()

    def test_timeout_reports_unverified(self):
        self.runner.side_effect = subprocess.TimeoutExpired([], 1, output=GOOD)
        self.assertEqual(self.call()['result']['status'], 'RUNTIME_UNVERIFIED')

    def test_process_ownership_failure_reports_unverified(self):
        self.runner.side_effect = RuntimeError('Job assignment failed')
        self.assertEqual(self.call()['result']['status'], 'RUNTIME_UNVERIFIED')

    def test_no_target_still_reports_useful_compilation(self):
        self.assertEqual(self.call(target=None)['result']['status'], 'COMPILED_NO_NAMED_TARGET')

    def test_missing_source_before_cli_is_setup_failure(self):
        with contextlib.redirect_stdout(io.StringIO()):
            rc = lean_check.main(['--file', str(self.folder / 'Absent.lean'), '--target', 'Target'])
        self.assertEqual(rc, 2)
        self.runner.assert_not_called()

    def test_baseline_missing_source_was_pass(self):
        spec = importlib.util.spec_from_file_location('baseline_probe', ROOT / 'BASELINE_lean_check.py')
        baseline = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(baseline)
        self.assertEqual(baseline.classify(0, '', self.folder / 'Absent.lean'), 0)

    def test_baseline_definition_was_pass(self):
        spec = importlib.util.spec_from_file_location('baseline_probe', ROOT / 'BASELINE_lean_check.py')
        baseline = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(baseline)
        guard(self.source)
        self.source.write_bytes(b'def value : Nat := 1\n')
        self.assertEqual(baseline.classify(0, '', self.source), 0)

    def test_baseline_file_target_ignored(self):
        spec = importlib.util.spec_from_file_location('baseline_probe', ROOT / 'BASELINE_lean_check.py')
        baseline = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(baseline)
        with patch.object(sys, 'argv', ['lean_check.py', '--file', str(self.source), '--target', 'Absent']), \
             patch.object(baseline, 'run_file', return_value=(0, '', 0)) as run_file, \
             contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as stop:
            baseline.main()
        self.assertEqual(stop.exception.code, 0)
        run_file.assert_called_once_with(str(self.source))


if __name__ == '__main__':
    unittest.main()
