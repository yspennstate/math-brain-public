"""Synthetic acceptance tests for per-file/hunk verify_ops extraction.

Usage: python test_verify_ops_patch.py --source SOURCE/verify_ops.py
The selected module is loaded as code; inspect it first. No session discovery or
real proof files are used. State/logs are redirected to a fresh TemporaryDirectory
for every test before decide/main is called. Only the Python standard library is
required. Exit nonzero on any failed acceptance test.
"""
import argparse
import hashlib
import importlib.util
import io
import itertools
import json
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch as mock_patch

sys.dont_write_bytecode = True
SOURCE = None
RISK = 'Dividing both sides by $x-1$ gives $y=2$.'
JUST = 'Since $z$ is nonzero, its reciprocal exists.'
LOCAL_JUST = 'Since $x-1$ is nonzero, ' + RISK
EXCHANGE = 'We interchange the limit and the integral to obtain $y=0$.'
FINITE = r'We checked for $n \le 1000$ that the bound holds for all $n$.'
OLD = 'For every $n$ there exists $m$ with $m > n$.'
NEW = 'There exists $m$ such that for every $n$ we have $m > n$.'
SORRY = 'theorem example_bound : True := by sorry'
CLEAN_LEAN = 'theorem example_bound : True := by trivial'


def block(path, new, old='', kind='Update'):
    body = ''.join('-' + line + '\n' for line in old.splitlines())
    body += ''.join('+' + line + '\n' for line in new.splitlines())
    header = '@@\n' if kind == 'Update' else ''
    return f'*** {kind} File: {path}\n{header}{body}'


def patch_text(*blocks):
    return '*** Begin Patch\n' + ''.join(blocks) + '*** End Patch\n'


class OpsAcceptance(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location('ops_acceptance', SOURCE)
        self.ops = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.ops)
        self.tmp = tempfile.TemporaryDirectory(prefix='verify_ops_acceptance_')
        self.addCleanup(self.tmp.cleanup)
        self.ops.STATE = os.path.join(self.tmp.name, 'state.json')
        self.ops.LOG = os.path.join(self.tmp.name, 'log.jsonl')

    def decide(self, tool, inp, session='synthetic-session'):
        return self.ops.decide({'tool_name': tool, 'tool_input': inp, 'session_id': session})

    def apply(self, *blocks, session='synthetic-session'):
        return self.decide('apply_patch', {'input': patch_text(*blocks)}, session)

    def write(self, path, text, session='synthetic-session'):
        return self.decide('Write', {'file_path': path, 'content': text}, session)

    def ops_in(self, out):
        return re.findall(r'\[verify-op ([a-z]+)\]', out)

    def rows(self):
        path = Path(self.ops.LOG)
        return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []

    def attribution(self):
        return [(file['file'], op) for row in self.rows()
                for file in row.get('files', [row]) for op in file['ops']]

    def assert_patch(self, blocks, expected):
        out = self.apply(*blocks)
        self.assertEqual(self.ops_in(out), [op for _, op in expected])
        self.assertEqual(self.attribution(), expected)

    def test_write_unsafe(self):
        self.assertEqual(self.ops_in(self.write('proof.tex', RISK)), ['divide'])

    def test_write_justified_quiet(self):
        self.assertEqual(self.write('proof.tex', LOCAL_JUST), '')
        self.assertFalse(Path(self.ops.STATE).exists())
        self.assertEqual(self.rows(), [])

    def test_edit_swap(self):
        out = self.decide('Edit', {'file_path': 'proof.tex', 'old_string': OLD, 'new_string': NEW})
        self.assertEqual(self.ops_in(out), ['witness'])

    def test_write_quantifier_is_not_edit(self):
        self.assertEqual(self.write('proof.tex', NEW), '')

    def test_write_two_operation_limit(self):
        self.assertEqual(self.ops_in(self.write('proof.tex', RISK + '\n' + EXCHANGE + '\n' + FINITE)),
                         ['divide', 'exchange'])
        self.assertEqual(self.rows()[0]['ops'], ['divide', 'exchange'])

    def test_patch_same_hunk_justified_quiet(self):
        self.assertEqual(self.apply(block('proof.tex', LOCAL_JUST)), '')

    def test_patch_same_hunk_swap(self):
        self.assert_patch([block('proof.tex', NEW, OLD)], [('proof.tex', 'witness')])

    def test_patch_add(self):
        self.assert_patch([block('proof.tex', RISK, kind='Add')], [('proof.tex', 'divide')])

    def test_patch_delete_quiet(self):
        self.assertEqual(self.apply('*** Delete File: proof.tex\n'), '')

    def test_patch_delete_does_not_take_identity(self):
        self.assert_patch([block('proof.tex', RISK), '*** Delete File: helper.py\n'], [('proof.tex', 'divide')])

    def test_patch_removed_text_not_new_justification(self):
        self.assert_patch([block('proof.tex', RISK, JUST)], [('proof.tex', 'divide')])

    def test_patch_move_uses_destination_identity_and_extension(self):
        out = self.apply('*** Update File: old.py\n*** Move to: proof.tex\n@@\n+' + RISK + '\n')
        self.assertEqual(self.ops_in(out), ['divide'])
        self.assertEqual(self.attribution(), [('proof.tex', 'divide')])
        self.assertEqual(self.write('proof.tex', RISK), '')
        self.assertEqual(self.ops_in(self.write('old.tex', RISK)), ['divide'])

    def test_patch_move_to_python_quiet(self):
        self.assertEqual(self.apply('*** Update File: proof.tex\n*** Move to: helper.py\n@@\n+' + RISK + '\n'), '')

    def test_patch_literal_plus_prefix_not_diff_header(self):
        self.assert_patch([block('proof.tex', '++' + RISK)], [('proof.tex', 'divide')])

    def test_patch_literal_minus_prefix_keeps_old_pair(self):
        self.assert_patch([block('proof.tex', NEW, '--' + OLD)], [('proof.tex', 'witness')])

    def test_patch_context_not_a_new_operation(self):
        self.assertEqual(self.apply('*** Update File: proof.tex\n@@\n ' + RISK + '\n+Let $a=1$.\n'), '')

    def test_patch_context_not_a_new_justification(self):
        self.assert_patch(['*** Update File: proof.tex\n@@\n ' + JUST + '\n+' + RISK + '\n'],
                          [('proof.tex', 'divide')])

    def test_patch_far_context_does_not_create_old_quantifier_pair(self):
        self.assertEqual(self.apply('*** Update File: proof.tex\n@@\n-For every $n$\n ' + 'x' * 1300 +
                                    '\n-there exists $m$.\n+' + NEW + '\n'), '')

    def test_patch_far_context_does_not_create_new_quantifier_pair(self):
        self.assertEqual(self.apply('*** Update File: proof.tex\n@@\n-' + OLD + '\n+There exists $m$\n ' +
                                    'x' * 1300 + '\n+such that for every $n$ we have $m > n$.\n'), '')

    def test_patch_short_context_cannot_join_quantifier_words(self):
        self.assertEqual(self.apply('*** Update File: proof.tex\n@@\n-' + OLD + '\n+There exists $m$\n ' +
                                    'a different thought' + '\n+such that for every $n$ we have $m > n$.\n'), '')

    def test_patch_context_cannot_join_symbolic_exchange(self):
        self.assertEqual(self.apply('*** Update File: proof.tex\n@@\n+\\lim \\int f\n unchanged prose\n' +
                                    '+= \\int \\lim f\n'), '')

    def test_patch_text_outside_envelope_cannot_justify(self):
        inp = '+' + JUST + '\n' + patch_text(block('proof.tex', RISK)) + '+' + JUST + '\n'
        out = self.decide('apply_patch', inp)
        self.assertEqual(self.ops_in(out), ['divide'])

    def test_patch_no_file_is_quiet(self):
        self.assertEqual(self.decide('apply_patch', {'input': patch_text('@@\n+' + RISK + '\n')}), '')

    def test_patch_no_envelope_is_quiet(self):
        self.assertEqual(self.decide('apply_patch', {'input': block('proof.tex', RISK)}), '')

    def test_multiedit_true_swap(self):
        out = self.decide('MultiEdit', {'file_path': 'proof.tex', 'edits': [
            {'old_string': OLD, 'new_string': NEW}, {'old_string': 'a', 'new_string': 'b'}]})
        self.assertEqual(self.ops_in(out), ['witness'])

    def test_multiedit_other_new_forall_does_not_hide_swap(self):
        out = self.decide('MultiEdit', {'file_path': 'proof.tex', 'edits': [
            {'old_string': OLD, 'new_string': NEW}, {'old_string': 'a', 'new_string': OLD}]})
        self.assertEqual(self.ops_in(out), ['witness'])

    def test_multiedit_each_locally_justified_quiet(self):
        out = self.decide('MultiEdit', {'file_path': 'proof.tex', 'edits': [
            {'new_string': LOCAL_JUST}, {'new_string': 'By dominated convergence, ' + EXCHANGE}]})
        self.assertEqual(out, '')

    def test_multiedit_invalid_entries_ignored(self):
        out = self.decide('MultiEdit', {'file_path': 'proof.tex', 'edits': [None, 42, {'new_string': RISK}]})
        self.assertEqual(self.ops_in(out), ['divide'])

    def test_multiedit_repeated_operation_deduplicated(self):
        out = self.decide('MultiEdit', {'file_path': 'proof.tex', 'edits': [
            {'new_string': RISK}, {'new_string': RISK}, {'new_string': RISK}]})
        self.assertEqual(self.ops_in(out), ['divide'])
        self.assertEqual(self.attribution(), [('proof.tex', 'divide')])

    def test_cooldown_uses_actual_file(self):
        out = self.apply(block('proof.tex', RISK), block('other.tex', 'Let $z=1$.'))
        self.assertEqual(self.ops_in(out), ['divide'])
        self.assertEqual(self.attribution(), [('proof.tex', 'divide')])
        seen = json.loads(Path(self.ops.STATE).read_text())['synthetic-session']
        key = hashlib.sha1((os.path.normcase('proof.tex') + '|divide').encode()).hexdigest()[:16]
        self.assertEqual(set(seen), {key})
        self.assertEqual(self.write('proof.tex', RISK), '')
        self.assertEqual(self.ops_in(self.write('other.tex', RISK)), ['divide'])
        self.assertEqual(self.attribution(), [('proof.tex', 'divide'), ('other.tex', 'divide')])

    def test_cooldown_keeps_same_basename_directories_distinct(self):
        self.assertEqual(self.ops_in(self.write('first/proof.tex', RISK)), ['divide'])
        self.assertEqual(self.ops_in(self.write('second/proof.tex', RISK)), ['divide'])
        self.assertEqual(self.write('first/proof.tex', RISK), '')
        seen = json.loads(Path(self.ops.STATE).read_text())['synthetic-session']
        self.assertEqual(len(seen), 2)

    def test_cooldown_is_session_local(self):
        self.assertEqual(self.ops_in(self.write('proof.tex', RISK, 'session-a')), ['divide'])
        self.assertEqual(self.ops_in(self.write('proof.tex', RISK, 'session-b')), ['divide'])

    def test_cooldown_in_first_file_does_not_hide_second(self):
        self.write('first.tex', RISK)
        out = self.apply(block('first.tex', RISK), block('second.tex', RISK))
        self.assertEqual(self.ops_in(out), ['divide'])
        self.assertEqual(self.attribution(), [('first.tex', 'divide'), ('second.tex', 'divide')])

    def test_patch_call_limit_does_not_consume_omitted_cooldown(self):
        out = self.apply(*(block(path, RISK) for path in ['first.tex', 'second.tex', 'third.tex']))
        self.assertEqual(self.ops_in(out), ['divide', 'divide'])
        self.assertEqual(self.attribution(), [('first.tex', 'divide'), ('second.tex', 'divide')])
        self.assertEqual(self.ops_in(self.write('third.tex', RISK)), ['divide'])
        self.assertEqual(self.write('first.tex', RISK), '')
        self.assertEqual(self.write('second.tex', RISK), '')

    def test_multifile_logging_counts_one_call(self):
        self.apply(block('proof.tex', RISK), block('B.lean', SORRY))
        rows = self.rows()
        self.assertEqual(len(rows), 1)
        self.assertIsNone(rows[0]['file'])
        self.assertEqual(rows[0]['ops'], ['divide', 'sorry'])
        self.assertEqual(rows[0]['files'], [
            {'file': 'proof.tex', 'ops': ['divide']}, {'file': 'B.lean', 'ops': ['sorry']}])

    def test_single_file_log_schema_unchanged(self):
        self.write('proof.tex', RISK)
        row = self.rows()[0]
        self.assertEqual(set(row), {'ts', 'session', 'tool', 'file', 'ops'})
        self.assertEqual(row['file'], 'proof.tex')
        self.assertEqual(row['ops'], ['divide'])

    def test_repeated_hunks_same_file_deduplicate(self):
        out = self.apply(block('proof.tex', RISK) + '@@ later\n+' + RISK + '\n')
        self.assertEqual(self.ops_in(out), ['divide'])
        self.assertEqual(self.attribution(), [('proof.tex', 'divide')])

    def test_hunk_limit_and_log_grouping(self):
        out = self.apply(block('proof.tex', RISK) + '@@ later\n+' + EXCHANGE + '\n@@ later still\n+' + FINITE + '\n')
        self.assertEqual(self.ops_in(out), ['divide', 'exchange'])
        self.assertEqual(len(self.rows()), 1)
        self.assertEqual(self.rows()[0]['ops'], ['divide', 'exchange'])
        self.assertEqual(self.ops_in(self.write('proof.tex', FINITE)), ['finite'])

    def test_stdout_posttooluse_envelope(self):
        data = {'tool_name': 'apply_patch', 'tool_input': {'input': patch_text(
            block('proof.tex', RISK), block('helper.py', 'x=1'))}, 'session_id': 'synthetic-cli'}
        output = io.StringIO()
        with mock_patch.object(sys, 'stdin', io.StringIO(json.dumps(data))), mock_patch.object(sys, 'stdout', output):
            self.ops.main()
        self.assertTrue(output.getvalue(), "expected a PostToolUse warning envelope")
        obj = json.loads(output.getvalue())
        self.assertEqual(obj['hookSpecificOutput']['hookEventName'], 'PostToolUse')
        self.assertEqual(self.ops_in(obj['hookSpecificOutput']['additionalContext']), ['divide'])

    def test_main_invalid_json_is_quiet(self):
        output = io.StringIO()
        with mock_patch.object(sys, 'stdin', io.StringIO('not json')), mock_patch.object(sys, 'stdout', output):
            self.ops.main()
        self.assertEqual(output.getvalue(), '')
        self.assertFalse(Path(self.ops.STATE).exists())

    def test_main_wrong_payload_type_is_quiet(self):
        output = io.StringIO()
        with mock_patch.object(sys, 'stdin', io.StringIO('[1, 2]')), mock_patch.object(sys, 'stdout', output):
            self.ops.main()
        self.assertEqual(output.getvalue(), '')

    def test_no_obligation_leaves_state_untouched(self):
        self.write('proof.tex', RISK)
        state = Path(self.ops.STATE).read_bytes()
        log = Path(self.ops.LOG).read_bytes()
        self.assertEqual(self.apply(block('helper.py', RISK), block('quiet.tex', LOCAL_JUST)), '')
        self.assertEqual(Path(self.ops.STATE).read_bytes(), state)
        self.assertEqual(Path(self.ops.LOG).read_bytes(), log)

    def test_persistence_failure_keeps_warning_behavior(self):
        self.ops.STATE = os.path.join(self.tmp.name, 'missing-directory', 'state.json')
        self.assertEqual(self.ops_in(self.write('proof.tex', RISK)), ['divide'])


# A separate unittest per ordering makes every counterexample visible in reports.
def install_patch_case(name, blocks, expected):
    def case(self):
        self.assert_patch(blocks, expected)
    setattr(OpsAcceptance, 'test_' + name, case)


for label, extra in [
    ('unrelated_justification', block('other.tex', JUST)),
    ('python_extension', block('helper.py', 'x=1')),
    ('lean_extension', block('B.lean', CLEAN_LEAN)),
    ('wrong_attribution', block('other.tex', 'Let $z=1$.')),
    ('research_path_filter', block('movie_projects/story.md', JUST)),
]:
    for reverse in [False, True]:
        blocks = [block('proof.tex', RISK), extra]
        install_patch_case(label + ('_reversed' if reverse else ''), blocks[::-1] if reverse else blocks,
                           [('proof.tex', 'divide')])

for reverse in [False, True]:
    suffix = '_reversed' if reverse else ''
    blocks = [block('B.lean', SORRY), block('proof.tex', 'Let $x=1$.')]
    install_patch_case('lean_sorry_not_lost' + suffix, blocks[::-1] if reverse else blocks, [('B.lean', 'sorry')])
    blocks = [block('proof.tex', RISK + ' ' + 'x' * 400), block('other.tex', JUST)]
    install_patch_case('far_justification_correct_attribution' + suffix, blocks[::-1] if reverse else blocks,
                       [('proof.tex', 'divide')])
    blocks = [block('first.tex', 'Let $a=1$.', OLD), block('second.tex', NEW, 'Let $b=2$.')]
    install_patch_case('no_cross_file_quantifier_swap' + suffix, blocks[::-1] if reverse else blocks, [])
    for op, risk, just in [('exchange', EXCHANGE, 'By dominated convergence, $z=0$.'),
                           ('finite', FINITE, 'This other result is numerical evidence.')]:
        blocks = [block('proof.tex', risk), block('other.tex', just)]
        install_patch_case('no_cross_file_' + op + suffix, blocks[::-1] if reverse else blocks, [('proof.tex', op)])

mixed = [('proof.tex', RISK, 'divide'), ('B.lean', SORRY, 'sorry'), ('helper.py', 'x=1', None)]
for i, order in enumerate(itertools.permutations(mixed)):
    install_patch_case(f'mixed_extensions_order_{i}', [block(path, text) for path, text, _ in order],
                       [(path, op) for path, _, op in order if op])

for container in ['hunks', 'multiedit', 'repeated_file_blocks']:
    for reverse in [False, True]:
        for kind in ['justification', 'quantifier']:
            def case(self, container=container, reverse=reverse, kind=kind):
                edits = [(RISK, ''), (JUST, '')] if kind == 'justification' else [('Let $a=1$.', OLD), (NEW, 'Let $b=2$.')]
                if reverse:
                    edits.reverse()
                if container == 'multiedit':
                    out = self.decide('MultiEdit', {'file_path': 'proof.tex', 'edits': [
                        {'new_string': new, 'old_string': old} for new, old in edits]})
                elif container == 'hunks':
                    parts = [block('proof.tex', new, old).split('@@\n', 1)[1] for new, old in edits]
                    out = self.apply('*** Update File: proof.tex\n@@\n' + '@@ later section\n'.join(parts))
                else:
                    out = self.apply(*(block('proof.tex', new, old) for new, old in edits))
                self.assertEqual(self.ops_in(out), ['divide'] if kind == 'justification' else [])
            setattr(OpsAcceptance, f'test_isolation_{container}_{kind}_{"reverse" if reverse else "forward"}', case)

for gap in [5, 1300]:
    for reverse in [False, True]:
        def case(self, gap=gap, reverse=reverse):
            first, last = (JUST, RISK) if reverse else (RISK, JUST)
            out = self.apply('*** Update File: proof.tex\n@@\n+' + first + '\n ' + 'x' * gap + '\n+' + last + '\n')
            self.assertEqual(self.ops_in(out), [] if gap < self.ops.WINDOW else ['divide'])
        setattr(OpsAcceptance, f'test_context_distance_{gap}_{"reverse" if reverse else "forward"}', case)
    def case(self, gap=gap):
        out = self.apply('*** Update File: proof.tex\n@@\n+Dividing\n ' + 'x' * gap + '\n+by $x$ gives $y=1$.\n')
        self.assertEqual(out, '')
    setattr(OpsAcceptance, f'test_context_cannot_join_operation_{gap}', case)

for field in ['patch', 'input', 'command']:
    def case(self, field=field):
        out = self.decide('apply_patch', {field: patch_text(block('proof.tex', RISK))})
        self.assertEqual(self.ops_in(out), ['divide'])
    setattr(OpsAcceptance, 'test_patch_input_field_' + field, case)

for ext, text, expected in [
    ('proof.md', RISK, ['divide']), ('proof.txt', RISK, ['divide']), ('proof.tex', EXCHANGE, ['exchange']),
    ('proof.tex', FINITE, ['finite']), ('notes.md', 'Dividing the work by two teams.', []),
    ('movie_projects/script.md', RISK, []), ('helper.py', RISK, []), ('B.lean', SORRY, ['sorry']),
    ('B.lean', '/- no sorry -/\n' + CLEAN_LEAN, []), ('B.lean', '-- sorry\n' + CLEAN_LEAN, []),
]:
    def case(self, ext=ext, text=text, expected=expected):
        self.assertEqual(self.ops_in(self.write(ext, text)), expected)
    setattr(OpsAcceptance, f'test_ordinary_format_{len([x for x in dir(OpsAcceptance) if x.startswith("test_ordinary_format")])}', case)


def main():
    global SOURCE
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()
    SOURCE = args.source.resolve()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(OpsAcceptance)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    report = {'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'tests': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors),
              'passed': result.testsRun - len(result.failures) - len(result.errors),
              'failed_tests': [test.id().split('.')[-1] for test, _ in result.failures + result.errors],
              'synthetic_only': True, 'state_isolated_per_test': True}
    if args.json:
        args.json.write_text(json.dumps(report, indent=2) + '\n')
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
