"""Regression controls for the existing PLIT extractor, selected by --module.

Fixtures exercise source pairing and label retention, not research difficulty.
Run: python test_plit_extractor_pairing.py --module path/to/extract_proofs.py
"""
import argparse
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


PARSER = argparse.ArgumentParser()
PARSER.add_argument('--module', type=Path, required=True)
ARGS, REMAINING = PARSER.parse_known_args()
SPEC = importlib.util.spec_from_file_location('extractor_under_test', ARGS.module)
EXTRACTOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXTRACTOR)

SOURCE = r'''
\documentclass{article}
\begin{document}
\begin{theorem}\label{thm:control}
Let $x$ be a positive real number. Then all of the following three conclusions hold:
\begin{enumerate}\item $x+1>x$.\item $x^2>0$.\item $x^3>0$.\end{enumerate}
\end{theorem}
\begin{proof}[HEADING]
The assumed inequality $x>0$ places the given real number strictly to the right of zero in the usual ordering of the real line.
Multiplication by the positive real number $x$ preserves this strict inequality, and therefore $x^2>0$ follows from the first multiplication.
Multiplying once more by that same positive number preserves the strict ordering again, so $x^3>0$ is the conclusion obtained by the second multiplication.
\end{proof}
\end{document}
'''


class SourcePairingTests(unittest.TestCase):
    def extract(self, heading):
        parent = Path(__file__).resolve().parent
        with tempfile.TemporaryDirectory(prefix='plit-pairing-test-', dir=parent) as directory:
            root = Path(directory).resolve()
            self.assertTrue(root.is_relative_to(parent))
            paper = root/'fixture'
            paper.mkdir()
            (paper/'main.tex').write_text(SOURCE.replace('HEADING', heading), encoding='utf-8')
            with patch.object(EXTRACTOR, 'TEX', str(root)):
                rows, status = EXTRACTOR.process_paper('fixture', {})
            self.assertEqual(status, 'ok')
            self.assertEqual(len(rows), 1)
            return rows[0]

    def test_partial_proof_cannot_certify_entire_statement(self):
        for part in (1, 2, 3):
            with self.subTest(part=part):
                heading = r'Proof of Theorem~\ref{thm:control}, part~(' + str(part) + ')'
                row = self.extract(heading)
                self.assertEqual(row.get('proof_heading'), heading)
                self.assertFalse(row['accept'])
                self.assertEqual(row['reject_reason'], 'partial_statement_proof')

    def test_heading_without_partial_claim_remains_available_for_review(self):
        # Passing this formatting filter does not establish soundness: the
        # separate semantic review must still see the incomplete fixture proof.
        heading = r'Proof of Theorem~\ref{thm:control}'
        row = self.extract(heading)
        self.assertEqual(row.get('proof_heading'), heading)
        self.assertNotEqual(row['reject_reason'], 'partial_statement_proof')

    def test_external_reference_keeps_distinguishing_suffix(self):
        label = 'external-definition-with-a-distinguishing-suffix'
        count = [0]
        rendered = EXTRACTOR.clean_text(r'Use \ref{' + label + '}.', {}, count)
        self.assertIn(label, rendered)
        self.assertEqual(count, [1])

    def test_local_reference_keeps_existing_local_number(self):
        count = [0]
        rendered = EXTRACTOR.clean_text(r'Use \eqref{local-label}.', {'local-label':'eq 2'}, count)
        self.assertEqual(rendered, 'Use (eq 2).')
        self.assertEqual(count, [0])


if __name__ == '__main__':
    unittest.main(argv=['test_plit_extractor_pairing.py', *REMAINING])
