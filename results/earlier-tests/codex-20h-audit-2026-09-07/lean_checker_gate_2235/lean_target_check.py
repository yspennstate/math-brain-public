"""Experimental named-target Lean checking; compilation is not certification.

All writes are owned by this campaign. Source review is an investigator assertion
bound to exact input bytes. This is not a sandbox for untrusted Lean metaprograms.
"""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import time
import uuid

from formal_receipt_v2 import classify
from run_component_pilot import guard, ROOT
from solver_probe import pressure_check
from windowless_job_v2 import run

PROJECT = Path.home() / 'phase_retrieval_omega/lean/omega_comb'
TOOLCHAIN = Path.home() / '.elan/toolchains/leanprover--lean4---v4.29.1'
LEAN = TOOLCHAIN / 'bin/lean.exe'
IMPORTS = ('import Mathlib.Tactic\nimport Mathlib.Analysis.SpecialFunctions.Exp\n'
           'import Mathlib.Analysis.SpecialFunctions.Log.Basic\n'
           'import Mathlib.Probability.Independence.Basic\n'
           'import Mathlib.MeasureTheory.Integral.Bochner.Basic\n')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def compiler_environment(project=PROJECT):
    project = Path(project).resolve(strict=True)
    manifest_path = project / 'lake-manifest.json'
    manifest_raw = manifest_path.read_bytes()
    manifest = json.loads(manifest_raw)
    # Restrict manifest path interpretation to the known built layout.
    if manifest.get('packagesDir') != '.lake/packages':
        raise ValueError('Unsupported package directory; review the environment first')
    paths = [project / '.lake/build/lib/lean']
    revisions = {}
    unbuilt = []
    for package in manifest['packages']:
        name = package['name']
        if not re.fullmatch(r'[A-Za-z0-9_-]+', name):
            raise ValueError('Unsafe or unsupported package name')
        path = project / '.lake/packages' / name / '.lake/build/lib/lean'
        if not path.is_dir():
            unbuilt.append(name)
        else:
            paths.append(path)
        revisions[name] = package.get('rev')
    if 'mathlib' in unbuilt or 'mathlib' not in revisions:
        raise FileNotFoundError('Built Mathlib package is missing')
    env = dict(os.environ)
    env['LEAN_PATH'] = os.pathsep.join(str(p) for p in paths if p.is_dir())
    # Prevent an unrelated library prefix from overriding the pinned compiler.
    env.pop('LEAN_SYSROOT', None)
    return env, {'manifest_sha256': sha(manifest_raw), 'package_revisions_declared': revisions,
                 'search_paths': env['LEAN_PATH'].split(os.pathsep),
                 'unbuilt_manifest_packages': unbuilt,
                 'missing_import_policy': 'Compiler failure; no builds or fallbacks',
                 'dependency_bytes_independently_verified': False}


def target_commands(target):
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)*", target):
        raise ValueError('An explicit simple, fully qualified declaration name is required')
    # Name lookup uses Lean's environment, not a textual declaration search.
    return ('\nopen Lean Elab Command in\nrun_cmd do\n'
            f'  let ci \u2190 getConstInfo ``{target}\n'
            '  let isTheorem : Bool := match ci with | .thmInfo _ => true | _ => false\n'
            f'  logInfo m!"TARGET_KIND {target}: theorem={{toString isTheorem}}"\n'
            f'#print axioms {target}\n')


def check_source(source, *, target=None, reviewed_sha256=None, translation_reviewed=False,
                 timeout=900, use_mathlib=False, output_root=None):
    if not isinstance(source, bytes):
        raise TypeError('Source must be exact UTF-8 bytes')
    text = source.decode('utf-8')
    if type(translation_reviewed) is not bool:
        raise ValueError('Translation review must be an explicit boolean')
    if type(timeout) not in (int, float) or not 0 < timeout <= 900:
        raise ValueError('Timeout must be positive and at most 900 seconds')
    source_hash = sha(source)
    if reviewed_sha256 is not None and reviewed_sha256 != source_hash:
        raise ValueError('Reviewed source hash differs from input; no process launched')
    reviewed = reviewed_sha256 is not None
    if target:
        suffix = target_commands(target)
    else:
        suffix = ''
    generated = ('import Lean\n' + text + suffix).encode('utf-8')
    folder = Path(output_root or ROOT / 'lean_helper_runs') / uuid.uuid4().hex
    guard(str(folder), 'topic:math-brain-20h-processes-20260907')
    if not LEAN.is_file():
        raise FileNotFoundError('Pinned Lean compiler is missing')
    env, environment = compiler_environment() if use_mathlib else (dict(os.environ), {})
    if not use_mathlib:
        env.pop('LEAN_PATH', None)
        env.pop('LEAN_SYSROOT', None)
    pressure_check()
    folder.mkdir(parents=True, exist_ok=False)
    original_path, path = folder / 'INPUT.lean', folder / 'Check.lean'
    guard(str(original_path), str(path))
    original_path.write_bytes(source)
    path.write_bytes(generated)
    compiler_hash = sha(LEAN.read_bytes())
    started = time.monotonic()

    def progress(event):
        if event['phase'] == 'waiting':
            pressure_check()

    try:
        guard(str(folder), 'topic:math-brain-20h-processes-20260907')
        completed = run([str(LEAN), str(path)], cwd=folder, env=env,
                        timeout=timeout, progress=progress)
        code, output, timed_out = completed.returncode, completed.stdout + completed.stderr, False
    except subprocess.TimeoutExpired as exc:
        code, output, timed_out = None, (exc.output or '') + (exc.stderr or ''), True
    if target:
        result = classify(code, output, target=target, timed_out=timed_out,
                          source_reviewed=reviewed, translation_reviewed=translation_reviewed)
    else:
        result = {'status': 'RUNTIME_UNVERIFIED' if timed_out else
                  ('COMPILE_FAILED' if code != 0 else 'COMPILED_NO_NAMED_TARGET'),
                  'formal_target_verified': False, 'translation_reviewed': translation_reviewed,
                  'mathematical_falsity_established': False}
    # Hold the result if evidence or compiler changed during execution.
    integrity = (path.read_bytes() == generated and original_path.read_bytes() == source
                 and sha(LEAN.read_bytes()) == compiler_hash)
    if not integrity:
        result.update(status='EVIDENCE_DRIFT', formal_target_verified=False)
    receipt = {'as_of': dt.datetime.now(dt.timezone.utc).isoformat(),
               'source_sha256': source_hash, 'generated_sha256': sha(generated),
               'compiler_sha256': compiler_hash, 'compiler_path': str(LEAN),
               'compiler_exit_code': code, 'compiler_output': output,
               'seconds': round(time.monotonic() - started, 3), 'result': result,
               'environment': environment, 'evidence_integrity': integrity,
               'source_review_assertion_sha256': reviewed_sha256,
               'production_deployed': False, 'receipt_directory': str(folder)}
    guard(str(folder / 'RECEIPT.json'))
    (folder / 'RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--file', type=Path)
    source.add_argument('--stmt')
    parser.add_argument('--target')
    parser.add_argument('--reviewed-sha256')
    parser.add_argument('--translation-reviewed', action='store_true')
    parser.add_argument('--mathlib', action='store_true')
    parser.add_argument('--timeout', type=float, default=900)
    args = parser.parse_args()
    raw = args.file.read_bytes() if args.file else (
        (IMPORTS if args.mathlib else '') + args.stmt.strip() + '\n').encode('utf-8')
    receipt = check_source(raw, target=args.target, reviewed_sha256=args.reviewed_sha256,
                           translation_reviewed=args.translation_reviewed,
                           use_mathlib=args.mathlib, timeout=args.timeout)
    print(json.dumps(receipt, indent=2))
    return 0 if receipt['result']['formal_target_verified'] else 3


if __name__ == '__main__':
    raise SystemExit(main())
