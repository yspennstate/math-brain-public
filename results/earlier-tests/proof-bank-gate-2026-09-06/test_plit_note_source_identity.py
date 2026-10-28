"""PLIT source-exclusion regressions; point PLIT_NOTES_UNDER_TEST at a candidate.

These execute the note builder's real ranking/exclusion with a small isolated
store. The inherited runner is replaced only for tokenization and file output.
No private source, answer key, or solver call is used.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sqlite3
import sys
import tempfile
import types
import unittest


class SourceIdentityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        candidate = os.environ.get("PLIT_NOTES_UNDER_TEST")
        if not candidate:
            self.skipTest("Set PLIT_NOTES_UNDER_TEST to the exact candidate notes builder")
        self.rb = types.ModuleType("run_bank10k")
        self.rb._tok = lambda s: re.findall(r"[a-z0-9]+", s.lower())
        self.rb.STORE = str(self.root / "store.sqlite")
        self.rb.sample_fingerprint = lambda ids: hashlib.sha256(json.dumps(ids).encode()).hexdigest()
        self.rb.dump_atomic = lambda p, obj: Path(p).write_text(json.dumps(obj), encoding="utf-8")
        previous = sys.modules.get("run_bank10k")
        sys.modules["run_bank10k"] = self.rb
        self.addCleanup(lambda: sys.modules.pop("run_bank10k", None) if previous is None else sys.modules.__setitem__("run_bank10k", previous))
        spec = importlib.util.spec_from_file_location("notes_candidate", candidate)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.original = {"item_id": "calibration", "claim": "A finite positive measure has the dyadic mass criterion.",
                         "argument_steps": [{"step": 1, "text": "The dyadic mass follows by integration."}]}
        self.item = dict(self.original)
        self.paper = "2609.00001"
        self.statement_hash = hashlib.sha256(self.original["claim"].encode()).hexdigest()
        self.own_id = "lit_" + self.statement_hash[:20]
        self.missing_node_provenance = False

    def source_record(self):
        return {"item_id": self.item["item_id"], "item_sha256": hashlib.sha256(json.dumps(self.item, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest(),
                "paper": self.paper + "v2", "source_statement_sha256": self.statement_hash}

    def run_builder(self, manifest=None, exclude=True):
        con = sqlite3.connect(self.rb.STORE)
        con.execute("create table nodes (id text, kind text, title text, body text, metadata_json text)")
        for nid, title, body in [(self.own_id, "Dyadic criterion", self.original["claim"]),
                                  ("lit_other_result", "Dyadic mass lemma", "Finite positive measure dyadic mass integration")]:
            meta = {} if self.missing_node_provenance else {"paper": self.paper + "v1"}
            con.execute("insert into nodes values (?,?,?,?,?)", (nid, "literature_statement", title, body, json.dumps(meta)))
        con.commit()
        con.close()
        items = self.root / "items.jsonl"
        items.write_text(json.dumps(self.item) + "\n", encoding="utf-8")
        self.rb.ITEMS = str(items)
        (self.root / "SAMPLE.json").write_text(json.dumps({"item_ids": [self.item["item_id"]]}), encoding="utf-8")
        args = ["notes", "--run", str(self.root), "--store", self.rb.STORE, "--label", "brain_v3"]
        if exclude:
            args.append("--exclude-own-paper")
        if manifest is not None:
            path = self.root / "source_manifest.jsonl"
            path.write_text(json.dumps(manifest) + "\n", encoding="utf-8")
            args += ["--item-source-manifest", str(path)]
        old = sys.argv
        try:
            sys.argv = args
            self.module.main()
        finally:
            sys.argv = old
        return json.loads((self.root / "brain_v3_notes.json").read_text(encoding="utf-8"))

    def test_original_statement_excludes_source_paper(self):
        result = self.run_builder()
        self.assertEqual(result["notes"]["calibration"], [])
        self.assertEqual(result["own_stats"]["own_paper_known"], 1)

    def test_context_repair_without_identity_refuses_before_output(self):
        self.item["claim"] = "Let the measure be finite and positive. " + self.item["claim"]
        with self.assertRaisesRegex(ValueError, "cannot resolve"):
            self.run_builder()
        self.assertFalse((self.root / "brain_v3_notes.json").exists())

    def test_bound_manifest_survives_context_repair_and_paper_version(self):
        self.item["claim"] = "Let the measure be finite and positive. " + self.item["claim"]
        result = self.run_builder(self.source_record())
        self.assertEqual(result["notes"]["calibration"], [])
        self.assertEqual(result["own_stats"]["own_paper_known"], 1)

    def test_changed_step_invalidates_complete_item_binding(self):
        source = self.source_record()
        self.item["argument_steps"] = [{"step": 1, "text": "Another mathematical argument."}]
        with self.assertRaisesRegex(ValueError, "complete item"):
            self.run_builder(source)

    def test_answer_fields_are_rejected(self):
        source = self.source_record()
        source["fault_step"] = 1
        with self.assertRaisesRegex(ValueError, "unexpected"):
            self.run_builder(source)

    def test_unattributed_literature_cannot_pass_paper_exclusion(self):
        self.missing_node_provenance = True
        with self.assertRaisesRegex(ValueError, "unresolved paper"):
            self.run_builder(self.source_record())

    def test_no_exclusion_preserves_ordinary_ranking(self):
        self.missing_node_provenance = True
        result = self.run_builder(exclude=False)
        self.assertEqual(len(result["notes"]["calibration"]), 2)


if __name__ == "__main__":
    unittest.main()
