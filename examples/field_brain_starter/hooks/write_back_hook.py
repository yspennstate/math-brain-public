"""Stop hook: when a turn ends having learned something and no record was written, ask the agent to write it down.

A brain grows only if agents write back. Asking at every stop teaches the agent to ignore the request, so this hook
asks at most once per session, and only when two things hold at the end of the turn:

  1. the agent's last message reads like a lesson ("turned out", "root cause", "the fix was", "next time", ...);
  2. no record in the memory folder changed in the last WINDOW minutes (the agent did not already write it).

When both hold it returns {"decision": "block", "reason": ...}. Codex and Claude Code both read that from a Stop
hook as "do not stop yet; here is what to do", so the agent gets one more step to file the record with
new_record.py. With BRAIN_WRITE_BACK=queue it never blocks: it appends the lesson to memory/WRITE_BACK_QUEUE.md
instead, for a person or the dream cycle to file later.

    python3 hooks/write_back_hook.py --selftest

Wire it under Stop in ~/.codex/hooks.json (or ~/.claude/settings.json). See docs/codex-hooks-quickstart.md.
Standard library only. Any error prints nothing: a hook must never block a turn by crashing.
"""
import datetime as dt
import io
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.environ.get("BRAIN_MEM_DIR", os.path.join(os.path.dirname(HERE), "memory"))
STATE = os.environ.get("BRAIN_HOOK_STATE", os.path.join(HERE, ".state"))
MODE = os.environ.get("BRAIN_WRITE_BACK", "ask")   # "ask" (block once) or "queue" (never block)
WINDOW = 120 * 60                                  # a record written in the last two hours counts as written back
TAIL = 64 * 1024                                   # how much of the transcript to read when no last message is given

LESSON = re.compile(
    r"\b(turned out|root cause|the (real )?cause was|the fix (was|is)|fixed it by|was wrong|my mistake|"
    r"next time|should have|lesson|we learned|it failed because|the problem was)\b", re.I)


def last_text(payload):
    """The agent's closing words. Codex passes last_assistant_message; otherwise read the transcript's tail."""
    text = payload.get("last_assistant_message")
    if isinstance(text, str) and text.strip():
        return text
    path = payload.get("transcript_path")
    if path and os.path.exists(path):
        with open(path, "rb") as fh:
            fh.seek(max(0, os.path.getsize(path) - TAIL))
            return fh.read().decode("utf-8", "replace")
    return ""


def wrote_recently():
    cut = time.time() - WINDOW
    try:
        return any(n.endswith(".md") and os.path.getmtime(os.path.join(MEM, n)) >= cut for n in os.listdir(MEM))
    except OSError:
        return True   # cannot tell: do not nag


def asked_already(session):
    if not session:
        return False
    os.makedirs(STATE, exist_ok=True)
    path = os.path.join(STATE, "writeback_" + re.sub(r"[^A-Za-z0-9_-]", "_", session)[:80] + ".txt")
    if os.path.exists(path):
        return True
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(dt.datetime.now().isoformat(timespec="seconds") + "\n")
    return False


def lesson_line(text):
    """The sentence that carries the lesson, trimmed, so the request can quote it back."""
    m = LESSON.search(text)
    if not m:
        return ""
    start = max(text.rfind(".", 0, m.start()), text.rfind("\n", 0, m.start())) + 1
    end_dot = text.find(".", m.end())
    end = len(text) if end_dot < 0 else end_dot + 1
    return " ".join(text[start:end].split())[:300]


def decide(payload):
    """Return the JSON to print, or "" for silence."""
    if payload.get("stop_hook_active"):
        return ""   # the agent is already continuing because of a Stop hook: never ask twice in a row
    line = lesson_line(last_text(payload))
    if not line or wrote_recently():
        return ""
    if MODE == "queue":
        with open(os.path.join(MEM, "WRITE_BACK_QUEUE.md"), "a", encoding="utf-8") as fh:
            fh.write("- %s %s\n" % (dt.date.today().isoformat(), line))
        return ""
    if asked_already(str(payload.get("session_id") or "")):
        return ""
    reason = ("Before you stop: this turn ended on a lesson (\"%s\") and no record was written. If it will matter to"
              " the next agent, file it in one step with new_record.py (type feedback for a mistake or a rule,"
              " project for a decision; say why, and how to apply it). If it will not matter, stop." % line)
    return json.dumps({"decision": "block", "reason": reason})


def main():
    if "--selftest" in sys.argv[1:]:
        global WINDOW
        WINDOW = 0     # the sample store's records are old: none counts as written this turn
        cases = [
            ({"session_id": "t%d" % time.time_ns(), "last_assistant_message":
              "Done. The banding turned out to be the export preset, which the update had reset to 8-bit."}, True),
            ({"session_id": "t%d" % time.time_ns(), "last_assistant_message": "Done. The cut is uploaded."}, False),
            ({"session_id": "t%d" % time.time_ns(), "stop_hook_active": True, "last_assistant_message":
              "The root cause was the preset."}, False),
        ]
        bad = 0
        for payload, want in cases:
            got = decide(payload)
            ok = bool(got) == want
            bad += not ok
            print("%s  %-90s -> %s" % ("ok  " if ok else "FAIL", payload["last_assistant_message"][:90],
                                       "asks" if got else "silent"))
        return 1 if bad else 0
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
