"""Stop hook: after a compaction, do not let the agent stop while the request it was working on is still open.

Right after a compaction the agent has just been handed a summary of its own session, and the commonest failure is
to read that summary as a final report and stop, with the work unfinished and nothing waiting on anyone. This hook
refuses that one stop, once, and tells the agent which request is still open (docs/brain-building/keep-working-stop-hook.md).

It blocks only when all of these hold, and is silent otherwise:

  1. the runtime is not already continuing because of a Stop hook (stop_hook_active);
  2. compaction_hook.py has saved a compaction for this session, and that record is under MAX_AGE hours old;
  3. this compaction has not been used to block before (the hook writes that down before it decides);
  4. request_hook.py's state names the request this session was working on, and the ledger still has it open.

The reason it returns names the request and the two legitimate ways out: finish it and link the record that
answers it (ledger.py link <id> <record> answered_by), or stop with one line saying what it is waiting on. A finished
agent therefore pays one short turn at most, and a session that never compacted is never blocked.

    python3 hooks/keep_working_hook.py --selftest

Wire it under Stop in ~/.claude/settings.json or ~/.codex/hooks.json; hooks/print_wiring.py prints the block. Codex has
no compaction event, so there it fires after the compaction compaction_hook.py found on a later prompt. Standard
library only. Any error prints nothing: a hook on the stop path must never be the reason a session cannot end.
"""
import io
import json
import os
import re
import shutil
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
MEM = os.environ.get("BRAIN_MEM_DIR", os.path.join(ROOT, "memory"))
STATE = os.environ.get("BRAIN_HOOK_STATE", os.path.join(HERE, ".state"))
LEDGER = os.environ.get("MATH_BRAIN_REQUESTS") or os.path.join(ROOT, "requests.jsonl")
MAX_AGE = 6 * 3600   # a compaction older than this is not "just now"


def safe(session):
    return re.sub(r"[^A-Za-z0-9_-]", "_", session)[:80]


def read_json(path, default):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


def decide(payload, mem=MEM, state=STATE, ledger=LEDGER, now=None):
    """Return the JSON to print, or "" for silence."""
    import recall
    if payload.get("stop_hook_active"):
        return ""
    session = str(payload.get("session_id") or "")
    if not session:
        return ""
    slug = read_json(os.path.join(state, "compactions.json"), {}).get("last", {}).get(session)
    path = os.path.join(mem, "%s.md" % slug) if slug else ""
    if not path or not os.path.exists(path) or (now or time.time()) - os.path.getmtime(path) > MAX_AGE:
        return ""
    used = os.path.join(state, "keepworking_%s.txt" % safe(session))
    if os.path.exists(used) and open(used, encoding="utf-8").read().strip() == slug:
        return ""
    os.makedirs(state, exist_ok=True)
    with open(used, "w", encoding="utf-8") as fh:   # written before deciding: this compaction never blocks twice
        fh.write(slug + "\n")
    rid = read_json(os.path.join(state, "request_%s.json" % safe(session)), {}).get("id")
    reqs = recall.load_requests(ledger) if rid and os.path.exists(ledger) else {}
    req = reqs.get(rid)
    if not req or req["status"] != "open":
        return ""
    reason = ("You compacted (%s) and are about to stop. A recap is not the end of the job: the request you were"
              " working on is still open in the ledger: %s \"%s\". Pick it up from your summary and keep working."
              " When it is done, link the record that answers it: python ledger.py link %s <record> answered_by."
              " Stop only if it is done, or is waiting on someone's answer or on a job that is already running;"
              " then say which in one line." % (slug, rid, req["text"][:200], rid[:12]))
    return json.dumps({"decision": "block", "reason": reason})


def selftest():
    work = tempfile.mkdtemp(prefix="brain_keepworking_")
    try:
        mem, state, ledger = (os.path.join(work, n) for n in ("memory", "state", "requests.jsonl"))
        os.makedirs(mem)
        os.makedirs(state)
        rid, slug = "req_0123456789ab", "compaction_s1_abcdef12_2026_03_30"
        with open(os.path.join(mem, slug + ".md"), "w", encoding="utf-8") as fh:
            fh.write("---\nname: %s\n---\nsummary\n" % slug)
        with open(os.path.join(state, "compactions.json"), "w", encoding="utf-8") as fh:
            json.dump({"seen": {}, "last": {"s1": slug, "s2": slug}}, fh)
        for s in ("s1", "s2", "s3"):
            with open(os.path.join(state, "request_%s.json" % s), "w", encoding="utf-8") as fh:
                json.dump({"id": rid, "records": []}, fh)
        with open(ledger, "w", encoding="utf-8") as fh:
            fh.write(json.dumps({"op": "ask", "id": rid, "text": "Deliver the harbour film at twelve minutes",
                                 "role": "researcher", "at": "2026-03-30T09:00:00+00:00"}) + "\n")

        def ask(sid, **kw):
            return decide(dict(session_id=sid, **kw), mem, state, ledger)

        cases = [("open request after a compaction blocks", bool(ask("s1")), True),
                 ("the same compaction does not block twice", bool(ask("s1")), False),
                 ("stop_hook_active is never blocked", bool(ask("s2", stop_hook_active=True)), False),
                 ("a session that never compacted is not blocked", bool(ask("s3")), False),
                 ("a compaction older than six hours is not blocked",
                  bool(decide({"session_id": "s2"}, mem, state, ledger, now=time.time() + MAX_AGE + 60)), False)]
        with open(ledger, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"op": "link", "id": rid, "node": slug, "rel": "answered_by",
                                 "at": "2026-03-30T10:00:00+00:00"}) + "\n")
        cases.append(("an answered request is not blocked", bool(ask("s2")), False))
        bad = 0
        for label, got, want in cases:
            ok = got == want
            bad += not ok
            print("%-52s %s" % (label, "ok" if ok else "FAIL (%s)" % ("blocked" if got else "silent")))
        return 1 if bad else 0
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main():
    if "--selftest" in sys.argv[1:]:
        return selftest()
    try:
        raw = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8-sig", errors="replace").read()
        out = decide(json.loads(raw) if raw.strip() else {})
        if out:
            sys.stdout.write(out)
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
