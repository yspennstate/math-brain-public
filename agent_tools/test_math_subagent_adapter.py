"""test_math_subagent_adapter.py - research subagents get the math store's cards, and a held child is not counted as
served (29 Sep 2026).

    python test_math_subagent_adapter.py [--old OLD_MATH_SENSE.py] [--no-live]

 S1-S3  MATHBRAIN_SHADOW, in-process on the store MATHBRAIN_STORE names (skipped when none is set) (read-only; every write the hook makes is recorded or sent to
        a scratch folder): shadow prints the same block as a normal run and records nothing; a normal run records the
        guard shard, the use log, the session context and the surfaced row
 A1-A10 the adapter with a stand-in hook and a scratch ledger: which calls it answers, what it appends, which arm a
        task falls in, what it writes to the ledger, and that nothing it does can raise
 A11    a math hook that exits with an error is not served, even when it printed a valid block first; an exit 0 with a
        block is; an empty error exit and bad JSON stay failures
 A12    the tool call's id: each row records it, two calls of one task are two child sessions in one arm, and a call
        without one keeps the child id the task alone gives
 E1     end to end through a real math_sense.py subprocess in shadow: an answer inside the time limit, and no
        session shard for the child afterwards (skipped with --no-live)
With --old, the hook before this change ignores MATHBRAIN_SHADOW and records the serve (the check can fail). With
--adapter, the adapter under test is that file; with --old-adapter, the adapter before the A11/A12 change serves the
error exit's block (N11) and gives two calls of one task one child and no call id (N12).
"""
import importlib.machinery
import importlib.util
import io
import json
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]
OLD = os.path.abspath(ARGS[ARGS.index("--old") + 1]) if "--old" in ARGS else None
ADAPTER = (os.path.abspath(ARGS[ARGS.index("--adapter") + 1]) if "--adapter" in ARGS
           else os.path.join(HERE, "math_subagent_adapter.py"))
OLD_ADAPTER = os.path.abspath(ARGS[ARGS.index("--old-adapter") + 1]) if "--old-adapter" in ARGS else None
LIVE = "--no-live" not in ARGS
sys.path.insert(0, HERE)
fails, ran = [], []
TASK = ("What does the Banach fixed point theorem say about a contraction mapping on a complete metric space, and "
        "why is the fixed point unique?")


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def load(path, name):
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


def hook_run(m, shadow, session, scratch):
    """Run m.main() on TASK with every recording site replaced by a recorder; returns (block, calls, files)."""
    calls = []
    m.SHADOW = shadow
    m.SESSION_CONTEXT = True      # off by default; on here so the session-context write is exercised in both arms
    m.HOME = scratch
    os.makedirs(os.path.join(scratch, ".claude", "dreaming"), exist_ok=True)
    m._remember_math_context = lambda sid, prompt: calls.append("context")

    def guard(session_id, node_ids, *, record=True):
        if record:
            calls.append("guard")
        return set()
    m._already_injected = guard
    real_use = m._use_module

    class UseProxy:
        def __getattr__(self, name):
            if name == "log_serve":
                return lambda *a, **k: calls.append("use_log")
            return getattr(real_use(), name)
    m._use_module = lambda: UseProxy()
    sys.path.insert(0, m.BUILD_SRC)
    saved_in, saved_out = sys.stdin, sys.stdout
    sys.stdin = io.StringIO(json.dumps({"hook_event_name": "UserPromptSubmit", "prompt": TASK, "session_id": session}))
    sys.stdout = out = io.StringIO()
    try:
        m.main()
    finally:
        sys.stdin, sys.stdout = saved_in, saved_out
    text = out.getvalue().strip()
    block = json.loads(text[text.find("{"):])["hookSpecificOutput"]["additionalContext"] if text else ""
    d = os.path.join(scratch, ".claude", "dreaming")
    files = sorted(os.listdir(d))
    return block, calls, files


def shadow_tests(ms_path, tmp):
    m = load(ms_path, "ms_shadow_new")
    sid = "3f2a9c1e-5b7d-4e8f-9a10-2b3c4d5e6f70"
    b_shadow, c_shadow, f_shadow = hook_run(m, True, sid, os.path.join(tmp, "home_shadow"))
    m2 = load(ms_path, "ms_shadow_new2")
    b_live, c_live, f_live = hook_run(m2, False, sid, os.path.join(tmp, "home_live"))
    check(bool(b_shadow) and c_shadow == [] and "surfaced.tsv" not in f_shadow,
          "S1 shadow: a block of %d chars, recorded %r, files %r" % (len(b_shadow), c_shadow, f_shadow))
    check(b_live == b_shadow and {"guard", "use_log", "context"} <= set(c_live) and "surfaced.tsv" in f_live,
          "S2 a normal run: the same block (%s), recorded %r, files %r" % (b_live == b_shadow, c_live, f_live))
    if OLD:
        os.environ["MATHBRAIN_SHADOW"] = "1"
        try:
            o = load(OLD, "ms_shadow_old")
        finally:
            os.environ.pop("MATHBRAIN_SHADOW", None)
        o.SHADOW = True     # an attribute the old hook never reads
        _, c_old, f_old = hook_run(o, True, sid, os.path.join(tmp, "home_old"))
        check("guard" in c_old and "surfaced.tsv" in f_old,
              "S3 the hook before this change records the serve under MATHBRAIN_SHADOW=1 (recorded %r; the check can "
              "fail)" % c_old)


def adapter_tests(tmp):
    a = load(ADAPTER, "msa_under_test")
    rows, seen = [], []

    def ledger(row):
        rows.append(row)
        return True, ""

    def runner_with(block):
        def run(task, child, shadow):
            seen.append({"child": child, "shadow": shadow})
            return block, 0.5, ""
        return run

    parent = "8d7c6b5a-4e3f-4a1b-9c8d-7e6f5a4b3c2d"

    def call(tool="Agent", prompt=TASK, description="probe", **extra):
        inp = {"description": description, "prompt": prompt, "subagent_type": "general-purpose", "model": "sonnet"}
        inp.update(extra)
        return {"hook_event_name": "PreToolUse", "tool_name": tool, "tool_input": inp, "session_id": parent}

    block = "[math-brain] Banach fixed point theorem ... claim_0123456789abcdef0123 ..."
    del rows[:], seen[:]
    r = a.decide(call(tool="Bash"), mode="serve", runner=runner_with(block), ledger=ledger)
    check(r is None and rows == [] and seen == [], "A1 a Bash call: no answer, no row, the hook not run")
    r = a.decide(call(prompt="look up x"), mode="serve", runner=runner_with(block), ledger=ledger)
    check(r is None and rows == [] and seen == [], "A2 a task under 40 characters: no answer, no row")
    r = a.decide(call(), mode="shadow", runner=runner_with(block), ledger=ledger)
    check(r is None and len(rows) == 1 and rows[0]["arm"] == "shadow" and rows[0]["answered"] and
          not rows[0]["delivered"] and seen[-1]["shadow"] is True,
          "A3 shadow mode: nothing appended; the row says answered, not delivered; the hook ran in shadow")
    # find a task in each arm: the draw is a hash of the task, so it is fixed for a task
    served_desc = held_desc = None
    for k in range(200):
        _, _, d = a.child_identity(parent, "probe-%d" % k, TASK)
        if d >= a.HOLD and served_desc is None:
            served_desc = "probe-%d" % k
        if d < a.HOLD and held_desc is None:
            held_desc = "probe-%d" % k
    del rows[:], seen[:]
    r = a.decide(call(description=served_desc, run_in_background=True), mode="serve", runner=runner_with(block),
                 ledger=ledger)
    new = (r or {}).get("hookSpecificOutput", {}).get("updatedInput", {})
    check(bool(r) and "permissionDecision" not in r["hookSpecificOutput"] and new.get("prompt") == TASK + a.frame(rows[-1]["delivery"]) + block
          and new.get("run_in_background") is True and new.get("model") == "sonnet" and rows[-1]["arm"] == "served"
          and rows[-1]["delivered"] and seen[-1]["shadow"] is False and rows[-1]["ids"] == ["claim_0123456789abcdef0123"],
          "A4 served: the block is appended after the task, every other field kept, no permission decision")
    r = a.decide(call(description=held_desc), mode="serve", runner=runner_with(block), ledger=ledger)
    check(r is None and rows[-1]["arm"] == "held" and not rows[-1]["delivered"] and seen[-1]["shadow"] is True,
          "A5 held: the hook runs in shadow, nothing is appended, the row says held")
    r = a.decide(call(description=served_desc), mode="serve", runner=runner_with(""), ledger=ledger)
    check(r is None and rows[-1]["answered"] is False, "A6 the hook stays silent: nothing appended, answered false")

    def boom(task, child, shadow):
        raise RuntimeError("hook exploded")
    r = a.decide(call(), mode="serve", runner=boom, ledger=ledger)
    check(r is None, "A7 a failing hook: no answer and no exception")
    k1, c1, _ = a.child_identity(parent, "d", TASK)
    k2, c2, _ = a.child_identity(parent, "d", TASK)
    k3, c3, _ = a.child_identity(parent, "d", TASK + " Also the rate.")
    check(re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-8[0-9a-f]{3}-[0-9a-f]{12}$", c1) is not None and c1 == c2
          and c1 != c3 and c1[:12] != parent[:12],
          "A8 the child's id is uuid-shaped, stable for a task, new for another task, and not the parent's prefix")
    del rows[:], seen[:]
    r = a.decide(call(), mode="off", runner=runner_with(block), ledger=ledger)
    check(r is None and rows == [] and seen == [], "A9 mode off: nothing runs")
    held = sum(1 for k in range(4000) if a.child_identity(parent, "t%d" % k, TASK)[2] < a.HOLD)
    check(abs(held / 4000.0 - a.HOLD) < 0.025, "A10 the held share over 4,000 tasks: %.3f (target %.2f)"
          % (held / 4000.0, a.HOLD))
    exit_codes(a, tmp, parent, call, served_desc, ledger, rows, "A11")
    invocations(a, parent, call, ledger, rows, block, "A12")
    if OLD_ADAPTER:
        old = load(OLD_ADAPTER, "msa_before")
        del rows[:]
        exit_codes(old, tmp, parent, call, served_desc, ledger, rows, "N11")
        invocations(old, parent, call, ledger, rows, block, "N12")
    return a


def stub(tmp, name, printed, code):
    """A stand-in math hook: reads its event, prints `printed`, exits with `code`."""
    path = os.path.join(tmp, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("import sys\nsys.stdin.read()\nsys.stdout.write(%r)\nsys.stdout.flush()\nsys.exit(%d)\n" % (printed, code))
    return path


def exit_codes(a, tmp, parent, call, served_desc, ledger, rows, tag):
    good = json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                              "additionalContext": "[math-brain] leads ... claim_0123456789abcdef0123"}})
    rc7 = stub(tmp, "hook_rc7.py", good, 7)
    rc0 = stub(tmp, "hook_rc0.py", good, 0)
    empty7 = stub(tmp, "hook_empty7.py", "", 7)
    bad0 = stub(tmp, "hook_bad0.py", "not json {", 0)
    results = {n: a.run_math_hook(TASK, "c", True, script=p) for n, p in
               (("rc7", rc7), ("rc0", rc0), ("empty7", empty7), ("bad0", bad0))}
    r = a.decide(call(description=served_desc), mode="serve",
                 runner=lambda task, child, shadow: a.run_math_hook(task, child, shadow, script=rc7), ledger=ledger)
    last = rows[-1] if rows else {}
    if tag == "A11":
        check(results["rc7"][0] == "" and results["rc7"][2] == "rc7" and bool(results["rc0"][0])
              and results["rc0"][2] == "" and results["empty7"][2] == "rc7" and results["bad0"][2] == "bad_json"
              and r is None and last.get("error") == "rc7" and last.get("answered") is False
              and last.get("delivered") is False,
              "A11 an error exit is not served: rc7 %r, rc0 %d chars, empty rc7 %r, bad JSON %r; the served arm's row "
              "%r" % (results["rc7"][2], len(results["rc0"][0]), results["empty7"][2], results["bad0"][2],
                      {k: last.get(k) for k in ("error", "answered", "delivered")}))
    else:
        new = (r or {}).get("hookSpecificOutput", {}).get("updatedInput", {})
        check(bool(results["rc7"][0]) and "claim_0123456789abcdef0123" in new.get("prompt", ""),
              "N11 the adapter before this change serves the block an error exit printed (error %r)"
              % results["rc7"][2])


def invocations(a, parent, call, ledger, rows, block, tag):
    def quiet(task, child, shadow):
        return block, 0.1, ""
    def event(tool_use_id=None):
        ev = call(description="same-task")
        if tool_use_id:
            ev["tool_use_id"] = tool_use_id        # top level of the hook's input, as Claude Code sends it
        return ev
    del rows[:]
    a.decide(event("toolu_first"), mode="shadow", runner=quiet, ledger=ledger)
    a.decide(event("toolu_second"), mode="shadow", runner=quiet, ledger=ledger)
    a.decide(event(), mode="shadow", runner=quiet, ledger=ledger)
    first, second, bare = (rows + [{}, {}, {}])[:3]
    if tag == "A12":
        check(first.get("tool_use_id") == "toolu_first" and second.get("tool_use_id") == "toolu_second"
              and bare.get("tool_use_id") == "" and first.get("child") != second.get("child")
              and first.get("key") == second.get("key") and first.get("arm") == second.get("arm")
              and bare.get("child") == a.child_identity(parent, "same-task", TASK)[1],
              "A12 the call id: recorded %r / %r / %r, two children for one task (%s), one arm (%s), the bare call's "
              "child as before (%s)" % (first.get("tool_use_id"), second.get("tool_use_id"), bare.get("tool_use_id"),
                                        first.get("child") != second.get("child"), first.get("arm") == second.get("arm"),
                                        bare.get("child") == a.child_identity(parent, "same-task", TASK)[1]))
    else:
        check("tool_use_id" not in first and first.get("child") == second.get("child"),
              "N12 the adapter before this change records no call id and gives two calls of one task one child")


def live_test(a, ms_path):
    shards = os.path.join(os.path.expanduser("~"), ".claude", "dreaming", ".math_sense_sessions")
    _, child, _ = a.child_identity("e2e-probe-parent", "e2e", TASK)
    import hashlib
    shard = os.path.join(shards, hashlib.sha1(child.encode()).hexdigest()[:24] + ".json")
    surfaced = os.path.join(os.path.expanduser("~"), ".claude", "dreaming", "surfaced.tsv")
    before = os.path.getsize(surfaced) if os.path.exists(surfaced) else -1
    block, seconds, error = a.run_math_hook(TASK, child, shadow=True, script=ms_path)
    after = os.path.getsize(surfaced) if os.path.exists(surfaced) else -1
    check(bool(block) and seconds < a.KILL_S and not error and not os.path.exists(shard) and before == after,
          "E1 a real hook in shadow: %d chars in %.1f s (error %r); no shard for the child; surfaced.tsv unchanged"
          % (len(block), seconds, error))


def main():
    tmp = tempfile.mkdtemp(prefix="msa_test_")
    try:
        ms_path = os.path.join(HERE, "math_sense.py")
        store = os.environ.get("MATHBRAIN_STORE", "")
        has_store = bool(store) and os.path.exists(store)
        if has_store:
            shadow_tests(ms_path, tmp)
        else:
            print("SKIP S1-S3 and E1: MATHBRAIN_STORE names no store, so the math hook stays silent")
        a = adapter_tests(tmp)
        if LIVE and has_store:
            live_test(a, ms_path)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
