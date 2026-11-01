import unittest
from proof_receipt import classify, digest, exit_code, target_commands

RAW = b'theorem Target : True := True.intro\n'
SHA = digest(RAW)
GOOD = "TARGET_KIND Target: theorem=true\n'Target' does not depend on any axioms\n"


class ReceiptTests(unittest.TestCase):
    def call(self, output=GOOD, **overrides):
        args = dict(source_sha256=SHA, reviewed_sha256=SHA, target='Target')
        args.update(overrides)
        return classify(0, output, **args)

    def test_clean_target(self):
        r = self.call()
        self.assertTrue(r['formal_target_verified'])
        self.assertEqual(r['translation_fidelity'], 'UNVERIFIED')
        self.assertFalse(r['mathematical_falsity_established'])
        self.assertEqual(exit_code(r), 0)

    def test_windows_newlines(self):
        self.assertTrue(self.call(GOOD.replace('\n', '\r\n'))['formal_target_verified'])

    def test_permitted_transitive_axioms(self):
        out = "TARGET_KIND Target: theorem=true\n'Target' depends on axioms: [propext, Classical.choice, Quot.sound]\n"
        self.assertTrue(self.call(out)['formal_target_verified'])

    def test_compilation_is_not_theorem(self):
        self.assertEqual(self.call('', target=None)['status'], 'COMPILED_NO_NAMED_TARGET')
        self.assertEqual(exit_code(self.call('', target=None)), 3)

    def test_unreviewed_source_can_spoof_receipts_but_cannot_certify(self):
        self.assertEqual(self.call(GOOD, reviewed_sha256=None)['status'], 'COMPILED_SOURCE_UNREVIEWED')

    def test_changed_review_hash(self):
        self.assertEqual(self.call(reviewed_sha256=digest(RAW + b' '))['status'], 'SOURCE_REVIEW_MISMATCH')

    def test_definition_is_not_theorem(self):
        self.assertEqual(self.call(GOOD.replace('true', 'false'))['status'], 'TARGET_NOT_THEOREM')

    def test_other_target_cannot_satisfy_receipt(self):
        self.assertFalse(self.call(GOOD.replace('Target', 'Other'))['formal_target_verified'])

    def test_missing_axioms(self):
        self.assertEqual(self.call('TARGET_KIND Target: theorem=true\n')['status'], 'TARGET_AXIOMS_MISSING_OR_AMBIGUOUS')

    def test_missing_kind(self):
        self.assertEqual(self.call("'Target' does not depend on any axioms\n")['status'], 'TARGET_KIND_MISSING_OR_AMBIGUOUS')

    def test_duplicate_spoofed_receipts_rejected(self):
        self.assertFalse(self.call(GOOD + GOOD)['formal_target_verified'])
        self.assertFalse(self.call(GOOD + "'Target' does not depend on any axioms\n")['formal_target_verified'])

    def test_partial_or_trailing_marker_text_rejected(self):
        for bad in [GOOD.replace('any axioms\n', 'any axioms trailing\n'),
                    GOOD.replace('TARGET_KIND', 'prefix TARGET_KIND')]:
            self.assertFalse(self.call(bad)['formal_target_verified'])

    def test_custom_axiom_and_sorry(self):
        for axiom, status in [('FalseAxiom', 'UNAPPROVED_AXIOMS'), ('sorryAx', 'ADMITTED_TARGET')]:
            out = "TARGET_KIND Target: theorem=true\n'Target' depends on axioms: [" + axiom + ']\n'
            self.assertEqual(self.call(out)['status'], status)

    def test_malformed_axioms(self):
        for value in ['propext,', ',propext', 'propext garbage', '']:
            out = "TARGET_KIND Target: theorem=true\n'Target' depends on axioms: [" + value + ']\n'
            self.assertFalse(self.call(out)['formal_target_verified'])

    def test_evidence_missing_or_changed(self):
        self.assertEqual(self.call(evidence_integrity=False)['status'], 'EVIDENCE_DRIFT_OR_MISSING')

    def test_timeout_never_establishes_falsity(self):
        r = self.call(timed_out=True)
        self.assertEqual(r['status'], 'RUNTIME_UNVERIFIED')
        self.assertFalse(r['mathematical_falsity_established'])

    def test_compile_failure_never_establishes_falsity(self):
        r = classify(1, 'unsolved goals', source_sha256=SHA, reviewed_sha256=SHA, target='Target')
        self.assertEqual(r['status'], 'COMPILE_FAILED')
        self.assertFalse(r['mathematical_falsity_established'])

    def test_target_injection_rejected(self):
        for target in ['X\n#eval 1', 'X;Y', 'A..B', '.A', 'A.', 'A B', '«x»']:
            with self.assertRaises(ValueError):
                target_commands(target)
        self.assertIn('getConstInfo ``A.theoremName', target_commands('A.theoremName'))


if __name__ == '__main__':
    unittest.main()
