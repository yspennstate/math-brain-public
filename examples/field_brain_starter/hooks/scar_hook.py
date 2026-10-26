"""PreToolUse hook: before the agent runs a command, warn it when the command looks like one that went wrong before.

A scar is a record of a mistake: a file whose type is feedback and whose slug starts with mistake_ or feedback_, or a
record that MISTAKES.md links. The hook scores the tool call's arguments against those records only, and speaks only
when one matches well. It never blocks the call: it adds one short paragraph the model reads before the tool runs.

    python3 hooks/scar_hook.py --selftest       # three sample commands: two that should warn, one that should not

Wire it under PreToolUse in ~/.codex/hooks.json (or ~/.claude/settings.json) with a matcher for the tools that act,
for example "Bash|apply_patch". See docs/codex-hooks-quickstart.md. Both runtimes take the JSON this prints.
Standard library only. Any error prints nothing: a hook must never block a turn.
"""
import io
import json
import math
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
MEM = os.environ.get("BRAIN_MEM_DIR", os.path.join(os.path.dirname(HERE), "memory"))
STATE = os.environ.get("BRAIN_HOOK_STATE", os.path.join(HERE, ".state"))
TOP = 2              # at most two scars per tool call
MIN_WORDS = 1.0      # stricter than recall: a command is short, so one shared common word must not be enough
MIN_SHARED = 2       # and the record must share at least two words with the command
BODY_CHARS = 500


def scars(recs):
    """The records that describe something that went wrong, plus every record MISTAKES.md links."""
    linked = set()
    path = os.path.join(MEM, "MISTAKES.md")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            linked = set(re.findall(r"\[\[([^\]]+)\]\]", fh.read()))
    out = {}
    for slug, r in recs.items():
        if slug in linked or slug.startswith("mistake_") or slug.startswith("feedback_"):
            out[slug] = r
    return out


def seen_before(session, slug):
    """True when this scar already fired in this session. Warning twice about the same thing teaches skipping."""
    if not session:
        return False
    try:
        os.makedirs(STATE, exist_ok=True)
        path = os.path.join(STATE, "scar_" + re.sub(r"[^A-Za-z0-9_-]", "_", session)[:80] + ".txt")
        fired = set()
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                fired = set(fh.read().split())
        if slug in fired:
            return True
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(slug + "\n")
    except OSError:
        pass
    return False


def warning_for(text, session=""):
    import recall
    all_recs = recall.load(MEM)
    recs = scars(all_recs)
    if not recs or not text.strip():
        return ""
    scores = recall.bm25(recs, text)
    n = max(len(all_recs), 1)
    min_score = MIN_WORDS * math.log(1 + (n - 0.5) / 1.5)
    qwords = set(recall.words(text))
    ranked = []
    for slug, s in scores.items():
        m = recs[slug]["meta"]
        if m.get("superseded_by") or m.get("status") == "superseded":
            continue
        if s >= min_score and len(qwords & set(recs[slug]["terms"])) >= MIN_SHARED:
            ranked.append((s, slug))
    ranked.sort(reverse=True)
    lines = []
    for s, slug in ranked[:TOP]:
        if seen_before(session, slug):
            continue
        m = recs[slug]["meta"]
        body = recs[slug]["body"]
        if len(body) > BODY_CHARS:
            body = body[:BODY_CHARS].rsplit(" ", 1)[0] + " ..."
        lines.append("- %s [%s]\n  %s" % (slug, m.get("status", "unchecked"), body.replace("\n", "\n  ")))
    if not lines:
        return ""
    return ("[brain] This action resembles something that went wrong before. A scar is a question, not an order:"
            " check whether it applies here before you go on.\n" + "\n".join(lines))


def main():
    argv = sys.argv[1:]
    if "--selftest" in argv:
        tests = [
            ("export the master with the usual preset after the editor update", True),
            ("delete the raw camera footage folder to free disk space", True),
            ("list the files in the current folder", False),
        ]
        bad = 0
        for cmd, want in tests:
            got = warning_for(cmd, session="selftest-%d" % time.time_ns())
            ok = bool(got) == want
            bad += not ok
            print("%s  %-62s -> %s" % ("ok  " if ok else "FAIL", cmd, "warns" if got else "silent"))
            if got:
                print("      " + got.splitlines()[1])
        return 1 if bad else 0
    try:
        raw = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8-sig", errors="replace").read()
        payload = json.loads(raw) if raw.strip() else {}
        tool_input = payload.get("tool_input") or {}
        text = tool_input if isinstance(tool_input, str) else " ".join(str(v) for v in tool_input.values())
        text = text[:4000]   # a long patch would match everything; its first lines say what it does
        warning = warning_for(text, str(payload.get("session_id") or ""))
        if warning:
            event = str(payload.get("hook_event_name") or "PreToolUse")
            sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": warning}}))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
