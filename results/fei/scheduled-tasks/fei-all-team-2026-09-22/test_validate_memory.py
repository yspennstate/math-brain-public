"""Regression checks against the real FEI rollout, with adversarial mutations."""
import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from validate_memory import (validate_claims, validate_deltas,
                             validate_manifest, validate_snapshot)

ROOT = Path(__file__).resolve().parent
CLAIMS_PATH = next((path for path in (
    ROOT / "CLAIMS.json", ROOT.parent / "CLAIMS.json",
    ROOT.parent / "research" / "CLAIMS.json") if path.exists()), ROOT / "CLAIMS.json")
DELTAS_PATH = next((path for path in (
    ROOT / "DELTAS.json", ROOT.parent / "DELTAS.json") if path.exists()), ROOT / "DELTAS.json")


class MemoryRegressionTests(unittest.TestCase):
    def setUp(self):
        self.state = json.loads(CLAIMS_PATH.read_text())
        self.deltas = json.loads(DELTAS_PATH.read_text())
        self.cards = {c["id"]: c for c in self.state["claims"]}
        self.head = "a" * 40
        self.manifest = {key: self.state[key] for key in (
            "programme_id", "control_revision", "state_revision")}
        self.manifest["mandatory_correction_ids"] = [e["id"] for e in self.deltas["events"]]
        self.snapshot = {
            "schema_version": 1, "account": "fleet01", "slot": "B01", "run_id": "test-run-only",
            "next_mathematical_step": "Attempt the unpaid implication from the assigned source.",
            "control_commit": self.head, "manifest_commit": self.head,
            "write_parent_commit": self.head,
            "control_revision": self.state["control_revision"],
            "state_revision": self.state["state_revision"],
            "manifest_revision": self.state["state_revision"],
            "consumed_correction_ids": self.manifest["mandatory_correction_ids"].copy(),
            "remembered_claims": [], "native_memory": {"status": "not_attempted"},
            "full_brain_connected": False,
        }

    def new_claim(self, identifier, dependencies, **changes):
        card = copy.deepcopy(self.cards["TERMINAL-TRIGGER"])
        card.update(id=identifier, dependencies=dependencies, **changes)
        self.state["claims"].append(card)
        return card

    def test_real_source_bound_projection_and_corrections_pass(self):
        self.assertEqual(validate_claims(self.state), [])
        self.assertEqual(validate_deltas(self.deltas, self.state), [])
        self.assertEqual(validate_snapshot(self.snapshot, self.state, self.manifest, self.head), [])

    def test_live_branch_is_not_immutable_proof_provenance(self):
        self.state["sources"]["strong_prime"]["commit"] = "master"
        errors = validate_claims(self.state)
        self.assertTrue(any("immutable SHA" in error for error in errors))

    def test_missing_provenance_cannot_be_replaced_with_a_summary(self):
        self.cards["SAFE-SHAPED-DIRECTION"]["source_refs"] = []
        self.cards["SAFE-SHAPED-DIRECTION"]["sources"] = []
        self.assertTrue(any("missing source provenance" in e for e in validate_claims(self.state)))

    def test_candidate_refutation_cannot_be_applied_to_full_fei(self):
        event = self.deltas["events"][0]
        event["target_claim_id"] = "FEI-FULL"
        errors = validate_deltas(self.deltas, self.state)
        self.assertTrue(any("exceeds its exact target scope" in e for e in errors))
        self.assertEqual(self.cards["FEI-FULL"]["status"], "OPEN")

    def test_refuted_premise_blocks_descendants_but_not_independent_results(self):
        self.new_claim("UNSOUND-CHILD", [{"claim_id": "QUADRATIC-0337-REFUTED", "role": "positive_result"}])
        self.new_claim("STALE-GRANDCHILD", [{"claim_id": "UNSOUND-CHILD", "role": "positive_result"}])
        errors = validate_claims(self.state)
        self.assertTrue(any("UNSOUND-CHILD: positive dependency" in e for e in errors))
        self.assertTrue(any("STALE-GRANDCHILD: downstream" in e for e in errors))
        self.assertFalse(any("TERMINAL-TRIGGER:" in e for e in errors))

    def test_refuted_base_can_still_define_a_new_candidate(self):
        # Actual shaped repair depends on Gamma-dagger only as a definition.
        candidate = self.cards["SHAPED-CURRENT-REPAIR"]
        self.assertIn({"claim_id": "GAMMA-DAGGER-REFUTED", "role": "definition_only"}, candidate["dependencies"])
        self.assertEqual(validate_claims(self.state), [])

    def test_explicit_condition_is_preserved_without_false_promotion(self):
        conditional = self.new_claim(
            "CONDITIONAL-APPLICATION",
            [{"claim_id": "SHAPED-CURRENT-REPAIR", "role": "assumption"}],
            status="CONDITIONAL_IN_SOURCE", remaining_obligations=["Prove the arbitrary-gate inequality."],
        )
        self.assertEqual(validate_claims(self.state), [])
        conditional["status"] = "PROVED_IN_SOURCE"
        self.assertTrue(any("unresolved assumption" in e for e in validate_claims(self.state)))

    def test_finite_or_subclass_evidence_needs_a_universal_bridge(self):
        self.cards["READONCE-64573"]["scope_kind"] = "READ_ONCE"
        self.new_claim("UNJUSTIFIED-FULL-SCOPE", [{"claim_id": "READONCE-64573", "role": "positive_result"}], scope_kind="FULL_FEI")
        self.assertTrue(any("full-scope extension proof" in e for e in validate_claims(self.state)))

    def test_full_fei_promotion_requires_full_target_and_independent_reviews(self):
        self.state["full_fei_status"] = "VERIFIED_PROVED"
        errors = validate_claims(self.state)
        self.assertTrue(any("independent full review" in e for e in errors))
        self.assertTrue(any("no target-scope conclusion" in e for e in errors))

    def test_supersession_does_not_make_an_independent_theorem_false(self):
        self.cards["TERMINAL-TRIGGER"]["lifecycle"] = "SUPERSEDED"
        # The already existing hidden-curvature proof uses the theorem's truth,
        # not a claim that it is the newest candidate; that dependency survives.
        self.assertEqual(validate_claims(self.state), [])
        self.new_claim("CURRENT-ROUTE-DEPENDENT", [{"claim_id": "TERMINAL-TRIGGER", "role": "current_candidate"}])
        errors = validate_claims(self.state)
        self.assertTrue(any("CURRENT-ROUTE-DEPENDENT: current-candidate" in e for e in errors))
        self.assertFalse(any("HIDDEN-CURVATURE-REDUCTION:" in e for e in errors))

    def test_stale_publication_parent_requires_a_fresh_merge(self):
        errors = validate_snapshot(self.snapshot, self.state, self.manifest, "b" * 40)
        self.assertTrue(any("stale write parent" in e for e in errors))

    def test_worker_cannot_silently_restore_refuted_candidate_from_old_memory(self):
        self.snapshot["remembered_claims"] = [{
            "claim_id": "QUADRATIC-0337-REFUTED", "status": "PROVED_IN_SOURCE",
            "candidate_id": "QUADRATIC_0337", "use": "positive_premise",
        }]
        errors = validate_snapshot(self.snapshot, self.state, self.manifest, self.head)
        self.assertTrue(any("stale mathematical status" in e for e in errors))
        self.assertTrue(any("cannot be a positive premise" in e for e in errors))

    def test_missing_mandatory_correction_is_detected(self):
        self.snapshot["consumed_correction_ids"].pop()
        self.assertTrue(any("missing mandatory corrections" in e for e in
                            validate_snapshot(self.snapshot, self.state, self.manifest, self.head)))

    def test_repository_read_is_not_a_native_memory_receipt(self):
        self.snapshot["native_memory"] = {"status": "loaded"}
        errors = validate_snapshot(self.snapshot, self.state, self.manifest, self.head)
        self.assertTrue(any("native memory loaded requires actual receipt" in e for e in errors))

    def test_new_critical_event_is_visible_before_manifest_consolidation(self):
        self.snapshot["remembered_claims"] = [{"claim_id": "TERMINAL-TRIGGER",
            "status": "PROVED_IN_SOURCE", "candidate_id": None, "use": "positive_premise"}]
        inbox = {"pending_events": [{"id": "new-critical-event", "target_claim_id": "TERMINAL-TRIGGER",
                                     "blocks_positive_use": True}]}
        errors = validate_snapshot(self.snapshot, self.state, self.manifest, self.head, inbox)
        self.assertTrue(any("unconsumed live correction" in e for e in errors))
        self.assertTrue(any("pending source-bound challenge" in e for e in errors))
        self.snapshot["consumed_inbox_event_ids"] = ["new-critical-event"]
        self.snapshot["remembered_claims"][0]["use"] = "historical_context"
        self.assertEqual(validate_snapshot(self.snapshot, self.state, self.manifest, self.head, inbox), [])

    def test_existing_claim_identity_and_correction_history_are_immutable(self):
        previous = copy.deepcopy(self.state)
        self.cards["SHAPED-CURRENT-REPAIR"]["candidate_id"] = "SILENT-NEW-FORMULA"
        self.assertTrue(any("immutable candidate_id changed" in e for e in validate_claims(self.state, previous)))
        old_feed = copy.deepcopy(self.deltas)
        self.deltas["events"][0]["correction"] = "Old failure silently removed."
        self.assertTrue(any("immutable correction event was edited" in e for e in validate_deltas(self.deltas, previous, old_feed)))

    def test_artifact_digest_catches_changed_content(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "CURRENT_RESEARCH.md"
            path.write_text("Known source state\n")
            self.manifest["files"] = {"research": {"filepath": path.name,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}}
            self.assertEqual(validate_manifest(self.manifest, self.state, directory), [])
            path.write_text("Different unacknowledged state\n")
            self.assertTrue(any("content hash mismatch" in e for e in validate_manifest(self.manifest, self.state, directory)))


if __name__ == "__main__":
    unittest.main()
