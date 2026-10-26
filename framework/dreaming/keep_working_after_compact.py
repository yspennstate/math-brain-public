# -*- coding: utf-8 -*-
"""Stop hook: the first time a session tries to stop after a compaction, send it back to its open work.

What it fixes: after a compaction an agent often writes a recap of where it stands and ends the turn, although its
tasks are still open and nothing is waiting on a person. Context notes injected at SessionStart cannot make the agent
take another turn; a Stop hook that answers {"decision": "block"} can.

Rules: once per compaction (keyed by the compact_boundary record's uuid), never while stop_hook_active (no loops),
only when the compaction is in the transcript's last 3 MB and under 6 hours old, and only when the task checklist
(task_checklist_hook.py's store) holds open or working entries under this session's agent id. The reason tells the
agent it may stop with one line when everything is done, or is waiting on a person or a running job, so a finished
agent pays one short turn and nothing more. Silent on any error.

Environment: TASK_CHECKLIST_HOME (the checklist store, as for task_checklist_hook.py; BRAIN_CHECKLIST_STATE names
the state file directly and wins when set), KEEP_WORKING_STATE (where the
once-per-compaction marks live), KEEP_WORKING_FIRES (a JSON-lines log of every nudge).

    python keep_working_after_compact.py --selftest
"""
import io
import json
import os
import sys
import time
from datetime import datetime

HOME = os.path.expanduser("~")
_BRAIN_TREE = os.path.join(HOME, "brain-repo", "12_cognitive_architecture", "task_checklist")
STORE = (os.environ.get("TASK_CHECKLIST_HOME")
         or (_BRAIN_TREE if os.path.isdir(os.path.dirname(_BRAIN_TREE)) else os.path.join(HOME, ".claude", "task_checklist")))
CHECKLIST = os.environ.get("BRAIN_CHECKLIST_STATE") or os.path.join(STORE, "state.json")  # the older name still works
STATE_DIR = os.environ.get("KEEP_WORKING_STATE") or os.path.join(HOME, ".claude", "compact_hooks", "keep_working")
FIRES = os.environ.get("KEEP_WORKING_FIRES") or os.path.join(HOME, ".claude", "brain_graph", "compactions",
                                                               "keep_working_fires.jsonl")
TAIL = 3 * 1024 * 1024
MAX_AGE_S = 6 * 3600
OPEN = ("open", "working")


def last_boundary(path):
    """(uuid, epoch seconds) of the newest compact_boundary in the transcript's tail, or None."""
    try:
        with open(path, "rb") as fh:
            fh.seek(0, 2)
            size = fh.tell()
            fh.seek(max(0, size - TAIL))
            blob = fh.read()
    except OSError:
        return None
    for line in reversed(blob.split(b"\n")):
        if b'"compact_boundary"' not in line:
            continue
        try:
            rec = json.loads(line.decode("utf-8", "replace"))
        except ValueError:
            continue
        if rec.get("subtype") != "compact_boundary":
            continue
        ts = rec.get("timestamp") or ""
        try:
            at = datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()
        except ValueError:
            at = os.path.getmtime(path)
        return rec.get("uuid") or ts, at
    return None


def open_entries(sid, checklist=None):
    try:
        entries = json.load(io.open(checklist or CHECKLIST, encoding="utf-8")).get("entries") or {}
    except (OSError, ValueError):
        return []
    agent = "claude-" + sid[:8]
    rows = [e for e in (entries.values() if isinstance(entries, dict) else entries)
            if isinstance(e, dict) and e.get("agent") == agent and e.get("status") in OPEN
            and sid.startswith(e.get("session") or sid[:8])]   # the 8-character agent id alone can match a twin session
    rows.sort(key=lambda e: e.get("asked_at") or "", reverse=True)
    return rows


def decide(data, *, checklist=None, state_dir=None, now=None):
    """The hook's answer for one Stop event: a {"decision": "block", ...} dict, or None to let the session stop."""
    if data.get("stop_hook_active"):
        return None
    sid = data.get("session_id") or ""
    tpath = data.get("transcript_path") or ""
    if not sid or not tpath:
        return None
    b = last_boundary(tpath)
    if not b:
        return None
    key, at = b
    if (now or time.time()) - at > MAX_AGE_S:
        return None
    state_dir = state_dir or STATE_DIR
    os.makedirs(state_dir, exist_ok=True)
    sp = os.path.join(state_dir, sid + ".json")
    try:
        done = json.load(io.open(sp, encoding="utf-8")).get("nudged") or []
    except (OSError, ValueError):
        done = []
    if key in done:
        return None
    rows = open_entries(sid, checklist)
    # mark first: whatever happens below, this compaction is never nudged twice
    with io.open(sp, "w", encoding="utf-8") as fh:
        fh.write(json.dumps({"nudged": (done + [key])[-50:]}))
    if not rows:
        return None
    listed = "; ".join("%s (%s) %s" % (e.get("id"), (e.get("asked_at") or "")[11:16],
                                      (e.get("working_on") or e.get("asked_words") or "")[:110]) for e in rows[:6])
    more = "" if len(rows) <= 6 else " and %d more" % (len(rows) - 6)
    reason = ("[keep-working] You compacted at %s and are about to stop. A recap is not the end of the job: these are "
              "still open under your id: %s%s. Pick up your next step and keep working on them now. Stop only if every "
              "one is done (close it with the checklist's done), or is waiting on a person's answer or on a job that is "
              "already running and will notify you; then say which in one line."
              % (time.strftime("%H:%M", time.localtime(at)), listed, more))
    return {"decision": "block", "reason": reason, "_open": [e.get("id") for e in rows], "_boundary": key}


def main():
    raw = sys.stdin.buffer.read().decode("utf-8", "replace")
    data = json.loads(raw) if raw.strip() else {}
    out = decide(data)
    if not out:
        return
    try:
        os.makedirs(os.path.dirname(FIRES), exist_ok=True)
        with io.open(FIRES, "a", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps({"at": time.strftime("%Y-%m-%dT%H:%M:%S"), "session_id": data.get("session_id"),
                                 "boundary": out["_boundary"], "open": out["_open"]}) + "\n")
    except OSError:
        pass
    sys.stdout.write(json.dumps({"decision": "block", "reason": out["reason"]}))


def selftest():
    import tempfile

    sid = "0123abcd-0000-4000-8000-000000000000"
    with tempfile.TemporaryDirectory() as tmp:
        tr = os.path.join(tmp, "t.jsonl")
        stamp = datetime.now().astimezone().isoformat()
        with io.open(tr, "w", encoding="utf-8") as fh:
            fh.write(json.dumps({"type": "user", "message": "hi"}) + "\n")
            fh.write(json.dumps({"type": "system", "subtype": "compact_boundary", "uuid": "b1", "timestamp": stamp}) + "\n")
        ck = os.path.join(tmp, "state.json")
        entry = {"id": "T-1", "agent": "claude-0123abcd", "session": sid, "status": "working",
                 "asked_at": "2026-01-01T10:00:00", "working_on": "finish the proof"}
        with io.open(ck, "w", encoding="utf-8") as fh:
            json.dump({"entries": {"T-1": entry}}, fh)
        ev = {"session_id": sid, "transcript_path": tr}
        st = os.path.join(tmp, "state")
        checks = []
        first = decide(ev, checklist=ck, state_dir=st)
        checks.append(("blocks once after a compaction", bool(first) and "T-1" in first["reason"]))
        checks.append(("silent the second time", decide(ev, checklist=ck, state_dir=st) is None))
        checks.append(("silent while stop_hook_active",
                       decide(dict(ev, stop_hook_active=True), checklist=ck, state_dir=os.path.join(tmp, "s2")) is None))
        entry["status"] = "done"
        with io.open(ck, "w", encoding="utf-8") as fh:
            json.dump({"entries": {"T-1": entry}}, fh)
        checks.append(("silent with nothing open", decide(ev, checklist=ck, state_dir=os.path.join(tmp, "s3")) is None))
        checks.append(("silent for an old compaction",
                       decide(ev, checklist=ck, state_dir=os.path.join(tmp, "s4"), now=time.time() + MAX_AGE_S + 60) is None))
        entry["status"] = "open"
        entry["session"] = "0123abcd-ffff"
        with io.open(ck, "w", encoding="utf-8") as fh:
            json.dump({"entries": {"T-1": entry}}, fh)
        checks.append(("ignores a twin session with the same short id",
                       decide(ev, checklist=ck, state_dir=os.path.join(tmp, "s5")) is None))
    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    try:
        main()
    except Exception:
        pass
