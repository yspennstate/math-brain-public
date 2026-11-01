"""Exercise real retrieval and CLI projection on four exact, captured math cards."""
from __future__ import annotations

import contextlib
import argparse
import importlib.util
import io
import json
import os
import sys
import time
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
arguments = argparse.ArgumentParser()
arguments.add_argument("--code-root", type=Path, default=ROOT / "repo/src")
settings = arguments.parse_args()
os.environ["MATH_BRAIN_SEMANTIC"] = "0"
sys.path.insert(0, str(settings.code_root))
from math_brain import cli as proposed
from math_brain import semantic
from math_brain.models import GraphNode, NodeKind

spec = importlib.util.spec_from_file_location("math_brain._w357_baseline_cli", ROOT / "snapshot/cli.py")
baseline = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(baseline)
captured = json.loads((ROOT / "BRAIN_CARDS.json").read_text(encoding="utf-8"))
nodes = tuple(GraphNode(id=row["id"],kind=NodeKind(row["kind"]),title=row["title"],body=row["body"],
                        metadata=json.loads(row["metadata_json"]),created_at=row["created_at"])
              for row in captured["cards"])
assert len(nodes) == 4
load_bearing = next(n for n in nodes if "Theorem 3.13" in n.title)


class CapturedReadOnlyStore:
    def __enter__(self):
        return self
    def __exit__(self,*args):
        return False
    def iter_nodes(self):
        return iter(nodes)
    def iter_edges(self,**kwargs):
        return iter(())


def run_cli(module, background, decision, include=False, query=None, min_support=None):
    if query is None:
        query = load_bearing.title
    args = ["recall", "captured-read-only-cards.sqlite3", query, "--limit", "1"]
    if decision:
        args.append("--decision")
    if include:
        args.append("--with-statements")
    if min_support is not None:
        args.extend(["--min-support",str(min_support)])
    stream = io.StringIO()
    with patch.object(module.ResearchStore,"open_read_only",return_value=CapturedReadOnlyStore()), \
         patch.object(module,"_background_enabled",return_value=background), contextlib.redirect_stdout(stream):
        code = module.main(args)
    assert code == 0
    return json.loads(stream.getvalue())


def rows(output):
    return output if isinstance(output,list) else output["hits"]


def strip_statement_fields(output):
    copied = json.loads(json.dumps(output))
    for row in rows(copied):
        row.pop("statement",None)
        row.pop("statement_provenance",None)
    return copied


def main():
    started = time.perf_counter()
    assert not semantic.enabled(), "four-card projection check must not load a query model"
    measurements = []
    for background in (False,True):
        for decision in (False,True):
            old = run_cli(baseline,background,decision)
            compatible = run_cli(proposed,background,decision)
            new = run_cli(proposed,background,decision,include=True)
            assert old == compatible, "opt-out projection changed"
            assert strip_statement_fields(new) == old, "ranking, trace, abstention or background changed"
            assert rows(new)[0]["id"] == load_bearing.id
            assert rows(new)[0]["statement"] == load_bearing.body, "statement cropped or changed"
            assert rows(new)[0]["statement_provenance"]["statement_fidelity_reviewed"] is False
            if isinstance(new,dict) and "background" in new:
                assert all("statement" not in item for item in new["background"])
            old_text = json.dumps(old,ensure_ascii=False)
            new_text = json.dumps(new,ensure_ascii=False)
            terms = ("Γ ≻0", "uniformly")
            measurements.append({"background":background,"decision":decision,
                                 "before_visible_load_bearing_hypotheses":sum(term in old_text for term in terms),
                                 "after_visible_load_bearing_hypotheses":sum(term in new_text for term in terms),
                                 "before_bytes":len(old_text.encode()),"after_bytes":len(new_text.encode()),
                                 "selected_id":load_bearing.id,"default_output_identical":True,
                                 "complete_statement_preserved":True})
    # A high support gate must remain an abstention even when full statements are requested.
    old = run_cli(baseline,False,True,min_support=1e6)
    new = run_cli(proposed,False,True,include=True,min_support=1e6)
    assert old["abstained"] and new["abstained"]
    assert strip_statement_fields(new) == old
    assert sum(r["before_visible_load_bearing_hypotheses"] for r in measurements)==0
    assert sum(r["after_visible_load_bearing_hypotheses"] for r in measurements)==8
    receipt = {"command":"python -X utf8 test_recall_statements.py",
               "input_source":"BRAIN_CARDS.json: four exact-ID cards read in mode=ro",
               "query":load_bearing.title,
               "scope":"CLI statement visibility; not a recall-accuracy or theorem-validity benchmark",
               "cases":measurements, "before_visible_hypotheses":0, "after_visible_hypotheses":8,
               "projection_modes_checked":4, "default_compatibility_cases_passed":4,
               "abstention_preserved":True, "background_remains_identifier_only":True,
               "sqlite_writes":0,"live_source_writes":0,"model_loads":0,
               "semantic_mode":"explicitly off in this process", "code_root":str(settings.code_root),
               "elapsed_seconds":time.perf_counter()-started}
    (ROOT / "RECALL_MEASUREMENTS.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    (ROOT / "CLI_BEFORE.json").write_text(json.dumps(run_cli(baseline,False,False),indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (ROOT / "CLI_AFTER.json").write_text(json.dumps(run_cli(proposed,False,False,True),indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(receipt,indent=2))


if __name__=="__main__":
    main()
