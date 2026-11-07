"""test_math_subagent_receipt.py - the adapter's row is a decision, its faults are known outcomes, its clusters are
counted apart from its calls, and what a child received is read from the child (29 Sep 2026).

    python test_math_subagent_receipt.py [--adapter A.py] [--receipt R.py] [--old-adapter OLD.py] [--no-live]

 D1-D3  the decision: a served row says injection_requested (and `delivered`, the same value); the frame names
        the row's delivery; held and shadow rows request nothing
 F1-F8  ledger faults, each a known outcome and none a served card: a missing folder is made; a folder where the
        ledger should be, a full disk, a row that cannot be written as JSON, a ledger that returns no status and an
        append cut short are each reported by category, the card is withheld and the fault logged; a torn line does not
        swallow the next row; with the fault log broken too the fault reaches stderr, and nothing raises
 C1-C2  clusters: 60 clusters sent five times each read as 300 invocations in 60 clusters, one arm per cluster
 R1-R10 receipts from the child's own transcript, joined by the call id through the meta file: a served child that
        received, opened and cited; a held child that received nothing; an update the child never got; a child that
        never started; a truncated block; a card received and not used; two calls of one task kept apart; the
        PostToolUse evidence; a second sweep that adds nothing; an unfinished child whose citation stays unknown
 N1-N2  with --old-adapter, the adapter before this change serves a card although its ledger cannot be written (the
        review's own check, on the real module) and puts no delivery mark in the frame (the checks can fail)
 L1     the live ledger, read only: every live child on disk was run in shadow and received no frame (skip: --no-live)
"""
import importlib.machinery
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]


def arg(name, default=None):
    return os.path.abspath(ARGS[ARGS.index(name) + 1]) if name in ARGS else default


ADAPTER = arg("--adapter", os.path.join(HERE, "math_subagent_adapter.py"))
RECEIPT = arg("--receipt", os.path.join(HERE, "math_subagent_receipt.py"))
OLD_ADAPTER = arg("--old-adapter")
LIVE = "--no-live" not in ARGS
fails, ran = [], []
TASK = ("What does the Banach fixed point theorem say about a contraction mapping on a complete metric space, and "
        "why is the fixed point unique?")
PARENT = "8d7c6b5a-4e3f-4a1b-9c8d-7e6f5a4b3c2d"
CLAIM = "claim_0123456789abcdef0123"
CLAIM2 = "claim_fedcba9876543210fedc"
BLOCK = "[math-brain] leads, not verdicts ... %s ... %s ..." % (CLAIM, CLAIM2)


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def load(path, name):
    d = os.path.dirname(path)
    if d not in sys.path:
        sys.path.insert(0, d)
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


def call(description="probe", tool_use_id=None, parent=PARENT, prompt=TASK):
    ev = {"hook_event_name": "PreToolUse", "tool_name": "Agent", "session_id": parent,
          "tool_input": {"description": description, "prompt": prompt, "subagent_type": "general-purpose",
                         "model": "sonnet"}}
    if tool_use_id:
        ev["tool_use_id"] = tool_use_id
    return ev


def answering(block):
    return lambda task, child, shadow: (block, 0.1, "")


def description_in(a, arm, parent=PARENT):
    for k in range(400):
        d = "probe-%d" % k
        if a.arm_for("serve", a.child_identity(parent, d, TASK)[2]) == arm:
            return d
    raise RuntimeError("no description in arm %s" % arm)


def decision_tests(a, tmp):
    rows = []

    def ledger(row):
        rows.append(row)
        return True, ""
    served, held = description_in(a, "served"), description_in(a, "held")
    r = a.decide(call(served, "toolu_d1"), mode="serve", runner=answering(BLOCK), ledger=ledger)
    row = rows[-1]
    prompt = (r or {}).get("hookSpecificOutput", {}).get("updatedInput", {}).get("prompt", "")
    check(row.get("injection_requested") is True and row.get("delivered") is True
          and prompt == TASK + a.frame(row["delivery"]) + BLOCK and a.mark(row["delivery"]) in prompt,
          "D1 served: injection_requested %r (delivered %r); the frame names delivery %s"
          % (row.get("injection_requested"), row.get("delivered"), row.get("delivery")))
    r = a.decide(call(held, "toolu_d2"), mode="serve", runner=answering(BLOCK), ledger=ledger)
    check(r is None and rows[-1]["arm"] == "held" and rows[-1]["injection_requested"] is False,
          "D2 held: nothing appended, injection_requested false")
    r = a.decide(call(served, "toolu_d3"), mode="shadow", runner=answering(BLOCK), ledger=ledger)
    check(r is None and rows[-1]["arm"] == "shadow" and rows[-1]["injection_requested"] is False
          and rows[-1]["answered"] is True, "D3 shadow: answered, nothing requested")
    return served, held


def fault_tests(a, tmp, served):
    faults = []

    def fault_log(row):
        faults.append(row)
        return True

    def served_with(ledger):
        del faults[:]
        return a.decide(call(served, "toolu_f"), mode="serve", runner=answering(BLOCK), ledger=ledger,
                        faults=fault_log)
    path = os.path.join(tmp, "new_folder", "deeper", "serves.jsonl")
    ok = a.append_line({"x": 1}, path)
    check(ok == (True, "") and os.path.exists(path), "F1 a missing folder is made and the row written: %r" % (ok,))
    folder = os.path.join(tmp, "a_folder.jsonl")
    os.makedirs(folder)
    r = served_with(lambda row: a.ledger_row(row, folder))
    f = faults[-1] if faults else {}
    check(r is None and f.get("fault") == "open:not_a_file" and f.get("withheld") is True and "prompt" not in f
          and TASK[:20] not in json.dumps(f), "F2 a folder where the ledger should be: withheld, fault %r" % f.get("fault"))
    real_write = os.write

    def full(fd, data):
        raise OSError(28, "No space left on device")
    os.write = full
    try:
        r = served_with(lambda row: a.ledger_row(row, os.path.join(tmp, "full.jsonl")))
    finally:
        os.write = real_write
    check(r is None and (faults[-1] if faults else {}).get("fault") == "write:no_space",
          "F3 a full disk: withheld, fault %r" % (faults[-1] if faults else {}).get("fault"))
    ok = a.append_line({"x": object()}, os.path.join(tmp, "ser.jsonl"))
    check(ok == (False, "serialize"), "F4 a row that is not JSON: %r" % (ok,))
    r = served_with(lambda row: None)
    check(r is None and (faults[-1] if faults else {}).get("fault") == "ledger:no_status",
          "F5 a ledger that returns no status is a fault, not a success: %r" % (faults[-1] if faults else {}).get("fault"))
    torn = os.path.join(tmp, "torn.jsonl")
    a.append_line({"n": 1}, torn)

    def half(fd, data):
        return real_write(fd, data[:len(data) // 2])
    os.write = half
    try:
        r = served_with(lambda row: a.ledger_row(row, torn))
    finally:
        os.write = real_write
    check(r is None and (faults[-1] if faults else {}).get("fault") == "write:short",
          "F6 an append cut short: withheld, fault %r" % (faults[-1] if faults else {}).get("fault"))
    a.append_line({"n": 3}, torn)
    got = a.read_rows(torn)
    check([x.get("n") for x in got] == [1, 3], "F7 the torn line is skipped and does not swallow the next row: %r"
          % [x.get("n") for x in got])
    err = io.StringIO()
    saved = sys.stderr
    sys.stderr = err
    try:
        del faults[:]
        r = a.decide(call(served, "toolu_f8"), mode="serve", runner=answering(BLOCK),
                     ledger=lambda row: a.ledger_row(row, folder),
                     faults=lambda row: a.record_fault(row, folder))
    finally:
        sys.stderr = saved
    check(r is None and "withheld" in err.getvalue() and "open:not_a_file" in err.getvalue(),
          "F8 the fault log broken too: the fault reaches stderr (%r), nothing raises" % err.getvalue().strip()[:90])


def cluster_tests(a, tmp):
    ledger = os.path.join(tmp, "clusters.jsonl")
    for c in range(60):
        for k in range(5):
            a.decide(call("cluster-%d" % c, "toolu_c%d_%d" % (c, k)), mode="serve", runner=answering(""),
                     ledger=lambda row: a.ledger_row(row, ledger), faults=lambda row: True)
    groups, _ = a.summarize(ledger=ledger, receipts=os.path.join(tmp, "none.jsonl"),
                            faults=os.path.join(tmp, "none.jsonl"))
    inv = sum(g["invocations"] for g in groups.values())
    clu = sum(g["clusters"] for g in groups.values())
    rows = a.read_rows(ledger)
    arms = {}
    for r in rows:
        arms.setdefault(r["key"], set()).add(r["arm"])
    check(inv == 300 and clu == 60, "C1 60 clusters sent five times: %d invocations in %d clusters" % (inv, clu))
    check(len(arms) == 60 and all(len(v) == 1 for v in arms.values()) and len({r["child"] for r in rows}) == 300,
          "C2 one arm per cluster, 300 distinct children")


def write_child(projects, parent, agent, tool_use_id, first, turns, stale=True):
    d = os.path.join(projects, "C--proj", parent, "subagents")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "agent-%s.meta.json" % agent), "w", encoding="utf-8") as fh:
        json.dump({"agentType": "general-purpose", "toolUseId": tool_use_id}, fh)
    path = os.path.join(d, "agent-%s.jsonl" % agent)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(json.dumps({"type": "user", "isSidechain": True, "agentId": agent,
                             "message": {"role": "user", "content": first}}) + "\n")
        for t in turns:
            fh.write(json.dumps(t) + "\n")
    if stale:
        old = time.time() - 3600
        os.utime(path, (old, old))
    return path


def said(text, stop="end_turn"):
    return {"type": "assistant", "message": {"role": "assistant", "stop_reason": stop,
                                             "content": [{"type": "text", "text": text}]}}


def tool(inp):
    return {"type": "assistant", "message": {"role": "assistant", "stop_reason": "tool_use",
                                             "content": [{"type": "tool_use", "name": "Bash", "input": inp}]}}


def result():
    return {"type": "user", "message": {"role": "user", "content": [{"type": "tool_result", "content": "ok"}]}}


def receipt_tests(a, rc, tmp, served, held):
    projects = os.path.join(tmp, "projects")
    ledger = os.path.join(tmp, "r_serves.jsonl")
    receipts = os.path.join(tmp, "r_receipts.jsonl")

    def decide(desc, tid, block=BLOCK):
        r = a.decide(call(desc, tid), mode="serve", runner=answering(block), ledger=lambda row: a.ledger_row(row, ledger),
                     faults=lambda row: True)
        rows = [x for x in a.read_rows(ledger) if x["tool_use_id"] == tid]
        prompt = (r or {}).get("hookSpecificOutput", {}).get("updatedInput", {}).get("prompt", TASK)
        return rows[-1], prompt
    r1, p1 = decide(served, "toolu_r1")
    write_child(projects, PARENT, "a1", "toolu_r1", p1,
                [tool({"command": "python brain.py show %s" % CLAIM}), result(), said("By %s, yes." % CLAIM)])
    r2, p2 = decide(held, "toolu_r2")
    write_child(projects, PARENT, "a2", "toolu_r2", p2, [said("The fixed point is unique because ...")])
    r3, p3 = decide(served, "toolu_r3")
    write_child(projects, PARENT, "a3", "toolu_r3", TASK, [said("done")])                  # the update never arrived
    r4, _ = decide(served, "toolu_r4")                                                      # no child at all
    r5, p5 = decide(served, "toolu_r5")
    write_child(projects, PARENT, "a5", "toolu_r5", p5.replace(CLAIM2, "claim_..."), [said("ok")])   # block cut
    r6, p6 = decide(served, "toolu_r6")
    write_child(projects, PARENT, "a6", "toolu_r6", p6, [said("It is unique by the contraction estimate.")])
    r10, p10 = decide(served, "toolu_r10")
    write_child(projects, PARENT, "a10", "toolu_r10", p10, [tool({"command": "ls"})], stale=False)
    got = rc.sweep(ledger=ledger, receipts=receipts, projects=projects)
    st = a.merged_receipts(receipts)

    def s(row):
        return st.get(row["delivery"], {})
    check(s(r1).get("frame_seen") is True and s(r1).get("child_received") is True and s(r1).get("block_complete") is True
          and s(r1).get("source_opened") is True and s(r1).get("cited_in_answer") is True,
          "R1 served, received, opened and cited: %r" % s(r1))
    check(s(r2).get("frame_seen") is False and s(r2).get("child_received") is False and s(r2).get("block_complete") is None,
          "R2 held: the child received nothing (frame %r, mark %r)" % (s(r2).get("frame_seen"), s(r2).get("child_received")))
    check(r3["injection_requested"] and s(r3).get("child_received") is False and s(r3).get("frame_seen") is False,
          "R3 an update the child never got: requested %r, received %r" % (r3["injection_requested"],
                                                                       s(r3).get("child_received")))
    check(r4["injection_requested"] and all(s(r4).get(k) is None for k in a.STAGES),
          "R4 a child that never started: every stage unknown %r" % s(r4))
    check(s(r5).get("child_received") is True and s(r5).get("block_complete") is False,
          "R5 a truncated block: received %r, complete %r" % (s(r5).get("child_received"), s(r5).get("block_complete")))
    check(s(r6).get("child_received") is True and s(r6).get("source_opened") is False
          and s(r6).get("cited_in_answer") is False, "R6 received, not opened, not cited: %r" % s(r6))
    kids = rc.Children(projects)
    check(kids.find(PARENT, "toolu_r1").endswith("agent-a1.jsonl") and kids.find(PARENT, "toolu_r6").endswith(
        "agent-a6.jsonl") and r1["key"] == r6["key"] and r1["delivery"] != r6["delivery"],
          "R7 two calls of one task: one cluster, two deliveries, each joined to its own child")
    post_ok = rc.post({"tool_name": "Agent", "tool_use_id": "toolu_r1",
                       "tool_response": {"status": "async_launched", "agentId": "a1", "prompt": p1}},
                      ledger=ledger, receipts=receipts)
    post_old = rc.post({"tool_name": "Agent", "tool_use_id": "toolu_r3",
                        "tool_response": {"status": "async_launched", "agentId": "a3", "prompt": TASK}},
                       ledger=ledger, receipts=receipts)
    post_none = rc.post({"tool_name": "Agent", "tool_use_id": "toolu_r6", "tool_response": "text only"},
                        ledger=ledger, receipts=receipts)
    post_other = rc.post({"tool_name": "Agent", "tool_use_id": "toolu_unknown", "tool_response": {}},
                         ledger=ledger, receipts=receipts)
    check(post_ok["harness_applied"] is True and post_old["harness_applied"] is False
          and post_none["harness_applied"] is None and post_other is None,
          "R8 PostToolUse: applied %r, not applied %r, no prompt in the result %r, a call the adapter never saw %r"
          % (post_ok["harness_applied"], post_old["harness_applied"], post_none["harness_applied"], post_other))
    again = rc.sweep(ledger=ledger, receipts=receipts, projects=projects)
    check(len(got) >= 6 and again == [], "R9 the first sweep recorded %d rows; a second adds %d" % (len(got), len(again)))
    check(s(r10).get("child_received") is True and s(r10).get("cited_in_answer") is None
          and s(r10).get("source_opened") is None,
          "R10 a child still working: citation and opening unknown (%r, %r)" % (s(r10).get("cited_in_answer"),
                                                                           s(r10).get("source_opened")))


def old_tests(tmp, served):
    old = load(OLD_ADAPTER, "msa_before_mbi")
    folder = os.path.join(tmp, "old_folder.jsonl")
    os.makedirs(folder, exist_ok=True)
    r = old.decide(call(served, "toolu_n1"), mode="serve", runner=answering(BLOCK),
                   ledger=lambda row: old.ledger_row(row, folder))
    check(bool(r), "N1 the adapter before this change serves a card its ledger could not record (the check can fail)")
    prompt = (r or {}).get("hookSpecificOutput", {}).get("updatedInput", {}).get("prompt", "")
    check("(delivery " not in prompt, "N2 the adapter before this change puts no delivery mark in the frame")


def live_test(a, rc):
    got = rc.sweep(dry_run=True)
    rows = {r.get("delivery"): r for r in a.read_rows(a.LEDGER)}
    shadow_clean = all(g.get("frame_seen") in (False, None) for g in got
                       if rows.get(g["delivery"], {}).get("arm") in ("shadow", "held"))
    check(shadow_clean, "L1 live, read only: %d of %d rows have a child on disk; no shadow or held child received a frame"
          % (len(got), len(rows)))


def main():
    tmp = tempfile.mkdtemp(prefix="msr_test_")
    try:
        a = load(ADAPTER, "msa_mbi")
        sys.modules["math_subagent_adapter"] = a
        rc = load(RECEIPT, "msr_mbi")
        served, held = decision_tests(a, tmp)
        fault_tests(a, tmp, served)
        cluster_tests(a, tmp)
        receipt_tests(a, rc, tmp, served, held)
        if OLD_ADAPTER:
            old_tests(tmp, served)
        if LIVE:
            live_test(a, rc)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
