"""Adversarial construction controls. Fixtures are synthetic, not bank questions."""
import copy
import hashlib
from pathlib import Path
import tempfile
import unittest

import build_source_pairs as builder


class PairConstructionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='pair-test-',dir=Path(__file__).resolve().parent)
        self.addCleanup(self.cleanup_fixture)
        self.evidence = Path(self.temp.name) / "fixture.txt"
        self.evidence.write_text("Synthetic test evidence; never a literature source.\n")
        sha = hashlib.sha256(self.evidence.read_bytes()).hexdigest()
        self.source = {"schema": "source-proof-construction/v1", "proof_group": "fixture#p1",
            "paper_id": "fixturev1", "source_locator": "synthetic p1",
            "source_statement_locator": "fixture statement", "source_proof_locator": "fixture proof",
            "claim": "A synthetic parser fixture", "original_steps": ["A", "B", "C"],
            "license_uri": "https://example.invalid/license", "source_url": "https://example.invalid/source",
            "source_version": "synthetic fixture", "source_file_path": str(self.evidence),
            "source_file_sha256": sha, "license_evidence_path": str(self.evidence),
            "license_evidence_sha256": sha, "assumptions": [], "dependencies": []}
        self.proposal = {"proof_group": "fixture#p1", "fault_step": 2,
            "replacement": "D", "defect_explanation": "synthetic explanation",
            "minimal_repair": "Restore B", "falsifier": "synthetic falsifier"}

    def cleanup_fixture(self):
        assert Path(self.temp.name).resolve().is_relative_to(Path(__file__).resolve().parent)
        self.temp.cleanup()

    def make(self, source=None, proposal=None, split="development", exposed=()):
        return builder.construct([source or self.source], [proposal or self.proposal], split, exposed)

    def test_twins_share_proof_and_split_without_acceptance(self):
        packet = self.make()
        self.assertEqual(packet["summary"]["candidate_forms"], 2)
        self.assertEqual(packet["summary"]["distinct_source_proofs"], 1)
        self.assertEqual(packet["summary"]["semantically_accepted_by_this_builder"], 0)
        clean, flawed = packet["items"]
        self.assertEqual([n for n, (a, b) in enumerate(zip(clean["argument_steps"], flawed["argument_steps"]), 1)
                          if a != b], [2])
        self.assertEqual({r["split"] for r in packet["splits"]}, {"development"})
        self.assertNotIn("paper_id", clean)

    def test_file_drift_refuses(self):
        self.evidence.write_text("changed")
        with self.assertRaisesRegex(ValueError, "drift"):
            self.make()

    def test_no_op_refuses(self):
        proposal = dict(self.proposal, replacement="B")
        with self.assertRaisesRegex(ValueError, "no-op"):
            self.make(proposal=proposal)

    def test_boolean_fault_is_not_integer(self):
        with self.assertRaisesRegex(ValueError, "fault step"):
            self.make(proposal=dict(self.proposal, fault_step=True))

    def test_exposed_version_refuses_heldout(self):
        with self.assertRaisesRegex(ValueError, "exposed source family"):
            self.make(split="heldout", exposed=["fixturev99"])

    def test_duplicate_proof_and_alias_refuse(self):
        with self.assertRaisesRegex(ValueError, "multiple proposals"):
            builder.construct([self.source], [self.proposal, self.proposal], "development")
        alias = copy.deepcopy(self.source)
        alias["proof_group"] = "fixture#alias"
        proposal = dict(self.proposal, proof_group=alias["proof_group"])
        with self.assertRaisesRegex(ValueError, "duplicate original proof text"):
            builder.construct([self.source, alias], [self.proposal, proposal], "development")

    def test_packet_cannot_overwrite_old_packet(self):
        path = Path(self.temp.name) / "packet"
        builder.write_packet(self.make(), path)
        with self.assertRaisesRegex(ValueError, "fresh private"):
            builder.write_packet(self.make(), path)


if __name__ == "__main__":
    unittest.main()
