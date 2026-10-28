"""Deterministic entry-point regressions. Never call a solver or emit key text."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

TEST_HOME = Path(__file__).resolve().parent
HERE = Path(os.environ.get("MDLIT_TEST_TARGET") or TEST_HOME)
sys.path.insert(0, str(HERE))
from validity_gate import ValidityError, read_review, text_hash, validate_sample


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ValidityGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wrapper = load_module("md_test_wrapper", HERE / "run_md_wrapper.py")
        cls.grader = load_module("md_test_grader", HERE / "grade_md.py")

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="md-gate-test-", dir=TEST_HOME)
        self.base = Path(self.temp.name)
        self.run = self.base / "run"
        self.run.mkdir()
        self.review = self.base / "VALIDITY_REVIEW.json"
        self.review.write_text(json.dumps({"bad": {"valid": "no"}, "doubt": {"valid": "unsure"},
                                           "good": {"valid": "yes"}}), encoding="utf-8")
        self.items = {i: {"item_id": i, "claim": "test claim " + i,
                          "argument_steps": [{"text": "test step " + i}]}
                      for i in ("bad", "doubt", "good", "unreviewed", "clean")}
        self.keys = {i: {"truth": "clean" if i == "clean" else "flawed", "family_id": "test_operator",
                         "tier": "test", "external_refs": 0} for i in self.items}
        (self.base / "items").mkdir()
        (self.base / "items" / "mdlit.jsonl").write_text(
            "\n".join(json.dumps(v) for v in self.items.values()), encoding="utf-8")
        self.sample = self.make_sample(["good", "unreviewed", "clean"])

    def tearDown(self):
        self.temp.cleanup()

    def make_sample(self, ids):
        return {"item_ids": ids, "validity_gate": read_review(self.review)[1],
                "sampled_text_hash": text_hash(self.items, ids),
                "bank_fingerprint": self.wrapper.rb.bank_fingerprint(self.items)}

    def freeze(self, sample=None):
        (self.run / "SAMPLE.json").write_text(json.dumps(sample or self.sample), encoding="utf-8")

    def wrapper_context(self):
        stack = contextlib.ExitStack()
        stack.enter_context(patch.object(self.wrapper, "REVIEW", str(self.review)))
        stack.enter_context(patch.object(self.wrapper.rb, "RUN", str(self.run)))
        stack.enter_context(patch.object(self.wrapper.rb, "load_bank", return_value=(self.items, self.keys)))
        return stack

    def test_positive_unreviewed_are_explicitly_not_certified(self):
        result = validate_sample(self.sample, self.review, self.items)
        self.assertIn("unreviewed items are not certified", result["scope"])
        self.assertEqual(text_hash(self.items, self.sample["item_ids"]),
                         self.wrapper.rb.sampled_text_hash(self.items, self.sample["item_ids"]))

    def test_no_and_unsure_cannot_enter(self):
        for iid in ("bad", "doubt"):
            with self.subTest(iid=iid), self.assertRaisesRegex(ValidityError, "rejected"):
                validate_sample(self.make_sample([iid]), self.review, self.items)

    def test_changed_review_requires_new_receipt(self):
        self.review.write_text(self.review.read_text() + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValidityError, "current validity receipt"):
            validate_sample(self.sample, self.review, self.items)

    def test_missing_and_malformed_review_fail_closed(self):
        for payload in ("{}", "[]", "{", '{"x":{"valid":"maybe"}}', '{"x":{"valid":[]}}',
                        '{"x":{"valid":"yes"},"x":{"valid":"no"}}'):
            self.review.write_text(payload, encoding="utf-8")
            with self.subTest(payload=payload), self.assertRaises(ValidityError):
                read_review(self.review)
        self.review.unlink()
        with self.assertRaises(ValidityError):
            read_review(self.review)

    def test_same_ids_changed_question_are_blocked(self):
        self.items["good"]["argument_steps"][0]["text"] = "changed in place"
        with self.assertRaisesRegex(ValidityError, "text changed"):
            validate_sample(self.sample, self.review, self.items)

    def test_missing_duplicate_and_unbound_sample_fail(self):
        for sample in ({"item_ids": ["good"]}, self.make_sample(["good", "good"]),
                       dict(self.sample, item_ids=["missing"])):
            with self.subTest(sample=sample), self.assertRaises(ValidityError):
                validate_sample(sample, self.review, self.items)

    def test_actual_serve_blocks_before_transport(self):
        self.freeze(self.make_sample(["bad"]))
        with self.wrapper_context(), patch.object(self.wrapper.rb, "preflight") as transport:
            with self.assertRaisesRegex(SystemExit, "VALIDITY GATE"):
                self.wrapper.rb.cmd_serve(SimpleNamespace(arm="none"))
            transport.assert_not_called()

    def test_actual_serve_allows_valid_sample_to_reach_transport(self):
        self.freeze()
        with self.wrapper_context(), patch.object(self.wrapper.rb, "preflight", return_value=(False, "sentinel")) as transport:
            with contextlib.redirect_stdout(io.StringIO()), self.assertRaisesRegex(SystemExit, "refusing to serve"):
                self.wrapper.rb.cmd_serve(SimpleNamespace(arm="none"))
            transport.assert_called_once_with()

    def test_sampler_excludes_rejected_and_preserves_frozen_sample(self):
        args = SimpleNamespace(n=3, clean_share=1/3, floor=1, stage=0)
        with self.wrapper_context(), patch.object(self.wrapper, "served_anywhere", return_value=set()), contextlib.redirect_stdout(io.StringIO()):
            self.wrapper.cmd_sample_plit(args)
            data = (self.run / "SAMPLE.json").read_bytes()
            sample = json.loads(data)
            self.assertEqual(set(sample["item_ids"]), {"good", "unreviewed", "clean"})
            self.assertEqual(sample["validity_gate"], read_review(self.review)[1])
            with self.assertRaisesRegex(SystemExit, "preserve"):
                self.wrapper.cmd_sample_plit(args)
            self.assertEqual(data, (self.run / "SAMPLE.json").read_bytes())

    def test_sampler_refuses_population_shortfall(self):
        args = SimpleNamespace(n=20, clean_share=.25, floor=1, stage=0)
        with self.wrapper_context(), patch.object(self.wrapper, "served_anywhere", return_value=set()):
            with self.assertRaisesRegex(SystemExit, "not enough eligible"):
                self.wrapper.cmd_sample_plit(args)
            self.assertFalse((self.run / "SAMPLE.json").exists())

    def test_inherited_grade_blocks_before_scoring(self):
        self.freeze(self.make_sample(["bad"]))
        with self.wrapper_context(), patch.object(self.wrapper, "_grade_orig") as score:
            with self.assertRaisesRegex(SystemExit, "VALIDITY GATE"):
                self.wrapper.rb.cmd_grade(SimpleNamespace())
            score.assert_not_called()

    def test_dedicated_grade_blocks_before_reading_keys_or_writing_results(self):
        self.freeze(self.make_sample(["bad"]))
        with patch.object(self.grader, "HERE", str(self.base)), patch.object(self.grader, "load_keys") as keys:
            with patch.object(sys, "argv", ["grade_md.py", "--run", str(self.run)]):
                with self.assertRaisesRegex(SystemExit, "VALIDITY GATE"):
                    self.grader.main()
            keys.assert_not_called()
            self.assertFalse((self.run / "results").exists())

    def test_current_pinned_real_sample_is_rejected(self):
        pinned = Path.home() / "ai-memories-and-functionality/12_cognitive_architecture/audits/evidence/last200_20260906/private/mdlit_validity_before"
        if not pinned.exists():
            self.skipTest("private incident evidence is intentionally not distributed")
        sample = json.loads((pinned / "run_md/SAMPLE.json").read_text(encoding="utf-8"))
        excluded, receipt = read_review(pinned / "VALIDITY_REVIEW.json")
        self.assertEqual(len(excluded), 23)
        self.assertEqual(len(set(sample["item_ids"]) & excluded), 5)
        with self.assertRaisesRegex(ValidityError, "5 validity-rejected"):
            validate_sample(sample, pinned / "VALIDITY_REVIEW.json")

    def test_dedicated_grade_accepts_valid_sample_to_key_loading(self):
        self.freeze()
        with patch.object(self.grader, "HERE", str(self.base)), patch.object(self.grader, "load_keys", side_effect=RuntimeError("passed gate")) as keys:
            with patch.object(sys, "argv", ["grade_md.py", "--run", str(self.run)]):
                with self.assertRaisesRegex(RuntimeError, "passed gate"):
                    self.grader.main()
            keys.assert_called_once_with()

    def test_dedicated_grade_rejects_invalid_extra_arm(self):
        self.freeze()
        extra = self.base / "extra"
        extra.mkdir()
        (extra / "SAMPLE.json").write_text(json.dumps(self.make_sample(["bad"])), encoding="utf-8")
        with patch.object(self.grader, "HERE", str(self.base)), patch.object(self.grader, "load_keys", return_value=self.keys):
            with patch.object(sys, "argv", ["grade_md.py", "--run", str(self.run), "--extra-arm", "test=extra"]):
                with self.assertRaisesRegex(SystemExit, "VALIDITY GATE"):
                    self.grader.main()
            self.assertFalse((self.run / "results").exists())


if __name__ == "__main__":
    if os.name == "nt":
        import ctypes
        kernel = ctypes.windll.kernel32
        kernel.SetPriorityClass(kernel.GetCurrentProcess(), 0x4000)
    unittest.main(verbosity=2)
