"""Adversarial clean-room controls; no bank questions or heldout answers."""
import copy
import unittest

from proof_bank_gate import digest, evaluate


def fixture():
    item = {"item_id": "fixture-a", "schema": "plit-item/v1", "bank_version": "fixture",
            "claim": "A positive real number has positive square.", "prompt": "Check the argument.",
            "argument_steps": [{"n": 1, "text": "Let x be positive."},
                               {"n": 2, "text": "Multiplying by x reverses x > 0, so x squared < 0."}]}
    key = {"item_id": item["item_id"], "truth": "flawed", "fault_step": 2}
    source = {"item_id": item["item_id"], "item_sha256": digest(item), "key_sha256": digest(key),
              "paper_id": "fixture-paper-v1", "proof_group": "fixture-proof-a",
              "source_locator": "clean-room control, argument A", "license_uri": "fixture:original",
              "source_file_sha256": "0" * 64, "claim": item["claim"],
              "original_steps": ["Let x be positive.", "Multiplying by positive x preserves x > 0, so x squared > 0."]}
    review = {"item_id": item["item_id"], "schema": "semantic-proof-review/v1",
              "item_sha256": digest(item), "key_sha256": digest(key), "source_sha256": digest(source),
              "role": "author", "reviewer_id": "author-control", "valid": "yes",
              "complete_source_read": True, "source_fidelity": True, "self_contained": True,
              "original_sound": True, "research_substance": True,  # gate-field control only
              "reason": "Positive multiplication does not reverse the order.",
              "source_fidelity_reason": "Compared both complete lines.",
              "soundness_reason": "Order preservation under a positive multiplier.",
              "exactly_one_semantic_defect": True, "first_invalid_step": 2,
              "defect_explanation": "The order-reversal rule needs a negative multiplier.",
              "minimal_repair": "Preserve the inequality.", "falsifier": "Take x = 1."}
    second = dict(review, role="independent", reviewer_id="independent-control")
    return [item], [key], [source], [review, second], [{"item_id": item["item_id"], "split": "heldout"}]


class AcceptanceGateTests(unittest.TestCase):
    def test_empty_bank_cannot_report_success(self):
        with self.assertRaisesRegex(ValueError, "empty bank"):
            evaluate([], [], [], [], [])

    def test_bound_complete_evidence_counts_once(self):
        result = evaluate(*fixture())
        self.assertEqual(result["summary"]["semantically_accepted"], 1)

    def test_text_mutation_without_semantic_review_never_counts(self):
        packet = fixture()
        packet[3].clear()
        result = evaluate(*packet)
        self.assertEqual(result["summary"]["structurally_eligible"], 1)
        self.assertEqual(result["summary"]["semantically_accepted"], 0)

    def test_changed_item_invalidates_existing_reviews(self):
        packet = fixture()
        packet[0][0]["argument_steps"][1]["text"] += " This sentence was added later."
        result = evaluate(*packet)
        self.assertEqual(result["summary"]["semantically_accepted"], 0)
        self.assertIn("source_item_binding_mismatch", result["items"][0]["structural_errors"])

    def test_wrong_localization_cannot_receive_full_acceptance(self):
        packet = fixture()
        packet[3][1]["first_invalid_step"] = 1
        self.assertEqual(evaluate(*packet)["summary"]["semantically_accepted"], 0)

    def test_same_author_cannot_supply_independent_confirmation(self):
        packet = fixture()
        packet[3][1]["reviewer_id"] = packet[3][0]["reviewer_id"]
        self.assertEqual(evaluate(*packet)["summary"]["semantically_accepted"], 0)

    def test_negative_review_not_outvoted_by_positive_pair(self):
        packet = fixture()
        packet[3].append(dict(packet[3][1], reviewer_id="third-control", valid="no"))
        result = evaluate(*packet)
        self.assertEqual(result["summary"]["semantically_accepted"], 0)
        self.assertIn("unresolved_review_disagreement", result["items"][0]["structural_errors"])

    def test_paper_versions_cannot_cross_splits(self):
        packet = fixture()
        second = copy.deepcopy(packet)
        for rows in second:
            for row in rows:
                row["item_id"] = "fixture-b"
        packet[2][0]["paper_id"] = "1234.56789v1"
        second[2][0]["paper_id"] = "1234.56789v2"
        second[2][0]["proof_group"] = "fixture-proof-b"
        second[4][0]["split"] = "development"
        result = evaluate(*(a + b for a, b in zip(packet, second)))
        self.assertGreater(result["summary"]["cross_split_groups"], 0)
        self.assertTrue(all("source_family_crosses_splits" in r["structural_errors"] for r in result["items"]))

    def test_duplicate_or_missing_key_fails_closed(self):
        packet = fixture()
        packet[1].append(copy.deepcopy(packet[1][0]))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            evaluate(*packet)
        packet[1].clear()
        with self.assertRaisesRegex(ValueError, "identities differ"):
            evaluate(*packet)

    def test_original_clean_control_must_be_reviewed(self):
        packet = fixture()
        item, key, source = packet[0][0], packet[1][0], packet[2][0]
        item["argument_steps"] = [{"n": n, "text": t} for n, t in enumerate(source["original_steps"], 1)]
        key.update(truth="clean", fault_step=None)
        source.update(item_sha256=digest(item), key_sha256=digest(key))
        packet[3].clear()
        result = evaluate(*packet)
        self.assertEqual(result["summary"]["structurally_eligible"], 1)
        self.assertEqual(result["summary"]["semantically_accepted"], 0)


if __name__ == "__main__":
    unittest.main()
