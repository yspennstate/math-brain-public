# -*- coding: utf-8 -*-
"""The proof-bank and value-in-block evaluators score only a hook call that finished cleanly, and the gate refuses PASS
when one did not (account03/B01, B01-R79-GATE-PROOFBANK-VIB-FAILED-HOOK-OUTPUT-SCORED-20260929; 30 Sep 2026).

    python test_eval_hook_exit.py

P1-P3 and V1-V3 run each evaluator's hook call against a fake hook that exits 7 with valid hook JSON, exits 0 with it,
and exits 0 with output that is not JSON; G0-G3 feed the gate's reader a clean line, failed calls, a timeout and a line
with no count. Nothing live is read or written.
"""
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
FAILS = []


def check(name, ok, detail=""):
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" - " + detail) if detail and not ok else ""))
    if not ok:
        FAILS.append(name)


def fake_hook(td, name, code, body):
    path = os.path.join(td, name + ".py")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("import sys\nsys.stdin.read()\nsys.stdout.write(%r)\nraise SystemExit(%d)\n" % (body, code))
    return path


def main():
    import eval_proof_banks as pb
    import eval_value_in_block as vb
    import math_brain_regression_gate as gate
    td = tempfile.mkdtemp(prefix="evalexit_")
    block = "Target theorem [theorem]: exact value 42\n  (claim_" + "a" * 64 + " | provisional)"
    good = json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": block}})
    exit7, exit0, junk = (fake_hook(td, "h7", 7, good), fake_hook(td, "h0", 0, good), fake_hook(td, "hj", 0, "junk"))
    store = os.path.join(td, "store.sqlite3")
    open(store, "w").close()

    blk, _dt, bad = pb.run_hook(exit7, store, "q", "s")
    check("P1 proof banks: a hook that exited 7 with valid JSON is invalid and not scored", bad == "hook exited 7" and blk == "")
    blk, _dt, bad = pb.run_hook(exit0, store, "q", "s")
    check("P2 proof banks: a clean call is scored as before", bad == "" and blk.startswith("Target theorem"))
    blk, _dt, bad = pb.run_hook(junk, store, "q", "s")
    check("P3 proof banks: output that is not the hook's JSON is invalid", bad == "hook output is not the hook's JSON")

    env = dict(os.environ)
    vb.HOOK = exit7
    blk, ids, _s, bad = vb._run("q", env)
    check("V1 value in block: a hook that exited 7 is invalid and not scored", bad == "hook exited 7" and blk == "" and ids == [])
    vb.HOOK = exit0
    blk, ids, _s, bad = vb._run("q", env)
    check("V2 value in block: a clean call is scored as before", bad == "" and len(ids) == 1)
    vb.HOOK = junk
    blk, ids, _s, bad = vb._run("q", env)
    check("V3 value in block: output that is not the hook's JSON is invalid", bad == "hook output is not the hook's JSON")

    for label, line, breaches, errors in (
            ("G0 a clean line passes", "PROOFBANKS x | invalid 0", 0, 0),
            ("G1 failed calls prevent PASS", "PROOFBANKS x | invalid 2 (hook exited 7: 2)", 1, 0),
            ("G2 a timeout makes the row inconclusive, not a breach", "VIB x | invalid 1 (timeout: 1)", 0, 1),
            ("G3 a line with no invalid count is an error", "VIB x | ALL n=1 served 1 vib 1", 0, 1)):
        row, inst = {"breaches": [], "errors": []}, {}
        gate._invalid_to_row(row, inst, line, "x")
        check(label, len(row["breaches"]) == breaches and len(row["errors"]) == errors, str(row))
    print("%d failed" % len(FAILS))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
