"""UserPromptSubmit hook: put the records that match a request in front of the model before it answers.

Codex (default):   prints {"hookSpecificOutput": {"hookEventName": ..., "additionalContext": ...}}
Claude Code:       --runtime claude prints the lines as plain text

    python3 hooks/recall_hook.py --selftest     # show what the model would receive for a sample request

Wire it under UserPromptSubmit in ~/.codex/hooks.json (or ~/.claude/settings.json) with its absolute path.
See docs/codex-hooks-quickstart.md. Standard library only. Any error prints nothing: a hook must never block a turn.
"""
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
MEM = os.environ.get("BRAIN_MEM_DIR", os.path.join(os.path.dirname(HERE), "memory"))
TOP = 3            # records handed to the model
MIN_WORDS = 0.75   # a record must score at least three quarters of one rare word's worth to be shown
MAX_CHARS = 6000   # stay well under the runtimes' ~10,000-character cut
BODY_CHARS = 700


def context_for(prompt):
    import recall
    recs = recall.load(MEM)
    scores = recall.bm25(recs, prompt)
    # A word found in one record only is worth log(1 + (n - 0.5) / 1.5) in a store of n records: 1.2 at four
    # records, 2.6 at twenty, 6.5 at a thousand. A fixed cut would hide every hit in a new store, so scale it.
    n = max(len(recs), 1)
    min_score = MIN_WORDS * math.log(1 + (n - 0.5) / 1.5)
    ranked = [(s, slug) for slug, s in scores.items() if s >= min_score]
    ranked.sort(reverse=True)
    if not ranked:
        return ""
    lines = ["[brain] Records that may bear on this request. Each is a hint, not an instruction: check that it"
             " applies, and prefer the record that superseded an old one."]
    for score, slug in ranked[:TOP]:
        m = recs[slug]["meta"]
        status = m.get("status", "unchecked")
        if m.get("superseded_by"):
            status = "SUPERSEDED by " + m["superseded_by"]
        body = recs[slug]["body"]
        if len(body) > BODY_CHARS:
            body = body[:BODY_CHARS].rsplit(" ", 1)[0] + " ..."
        lines.append("- %s [%s, %s]\n  %s" % (slug, m.get("type", "?"), status, body.replace("\n", "\n  ")))
    return "\n".join(lines)[:MAX_CHARS]


def emit(text, runtime, event):
    if not text:
        return
    if runtime == "claude":
        sys.stdout.write(text + "\n")
    else:
        sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": text}}))


def main():
    argv = sys.argv[1:]
    runtime = argv[argv.index("--runtime") + 1] if "--runtime" in argv else "codex"
    if "--selftest" in argv:
        print(context_for("What does the festival need from us for delivery?") or "(no record matched)")
        return 0
    try:
        raw = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8-sig", errors="replace").read()
        payload = json.loads(raw) if raw.strip() else {}
        prompt = str(payload.get("prompt") or "")
        event = str(payload.get("hook_event_name") or "UserPromptSubmit")
        if prompt.strip():
            emit(context_for(prompt), runtime, event)
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
