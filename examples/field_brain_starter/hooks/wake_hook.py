"""Session-start hook: hand the model the brain's index once, when a session begins, so it knows what the store holds.

recall_hook.py finds records that match a request. That only helps when the request uses a record's words. The index
is the other half: one line per record, newest first, so the agent can see that a delivery spec or a past mistake
exists before anyone asks about it, and recall it by name. This hook prints the index (cut to fit) and the newest
lines of MISTAKES.md, once per session.

Claude Code:   wire it under SessionStart with --runtime claude; it prints plain text, which Claude Code adds to the
               session. It speaks again after a compaction or /clear, when the earlier copy has left the context.
Codex:         wire it under UserPromptSubmit; it prints {"hookSpecificOutput": ...} on the first prompt of a session
               and nothing on later prompts.

    python3 hooks/wake_hook.py --selftest

Standard library only. Any error prints nothing: a hook must never block a session by crashing.
"""
import datetime as dt
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.environ.get("BRAIN_MEM_DIR", os.path.join(os.path.dirname(HERE), "memory"))
STATE = os.environ.get("BRAIN_HOOK_STATE", os.path.join(HERE, ".state"))
MAX_CHARS = 8000      # under the runtimes' ~10,000-character cut, with room for the other hooks
MISTAKES = 5          # newest lines of MISTAKES.md to show
AGAIN = ("compact", "clear")   # Claude Code SessionStart sources after which the index must be given again


def read_lines(name):
    try:
        with io.open(os.path.join(MEM, name), encoding="utf-8") as fh:
            return [ln.rstrip() for ln in fh]
    except OSError:
        return []


def short(line):
    """An index line without its link target: '- [slug](slug.md) - text' becomes '- slug - text'."""
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)


def wake_text():
    index = [short(ln) for ln in read_lines("MEMORY.md") if ln.startswith("- ")]
    if not index:
        return ""
    mistakes = [ln for ln in read_lines("MISTAKES.md") if ln.startswith("- ")][:MISTAKES]
    head = ("[brain] What this store holds, newest first (%d records). A line says a record exists; read it before"
            " relying on it: python3 recall.py --id <slug>, or search with recall.py \"<wording>\" --or \"<another>\"."
            % len(index))
    tail = []
    if mistakes:
        tail = ["", "[brain] Newest recorded mistakes (check before repeating the same kind of work):"] + mistakes
    out, size = [head], len(head) + sum(len(t) + 1 for t in tail)
    for i, ln in enumerate(index):
        if size + len(ln) + 1 > MAX_CHARS:
            out.append("... and %d older records (search finds them)." % (len(index) - i))
            break
        out.append(ln)
        size += len(ln) + 1
    return "\n".join(out + tail)


def first_time(session, source):
    """True the first time a session asks, and again after a compaction or /clear."""
    if not session:
        return True
    os.makedirs(STATE, exist_ok=True)
    path = os.path.join(STATE, "wake_" + re.sub(r"[^A-Za-z0-9_-]", "_", session)[:80] + ".txt")
    if os.path.exists(path) and source not in AGAIN:
        return False
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(dt.datetime.now().isoformat(timespec="seconds") + "\n")
    return True


def decide(payload, runtime):
    """Return the text to print, or "" for silence."""
    if not first_time(str(payload.get("session_id") or ""), str(payload.get("source") or "")):
        return ""
    text = wake_text()
    if not text or runtime == "claude":
        return text
    event = payload.get("hook_event_name") or "UserPromptSubmit"
    return json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": text}})


def main():
    args = sys.argv[1:]
    runtime = args[args.index("--runtime") + 1] if "--runtime" in args else "codex"
    if "--selftest" in args:
        session = "selftest_%s" % dt.datetime.now().strftime("%H%M%S%f")
        first = decide({"session_id": session, "hook_event_name": "SessionStart", "source": "startup"}, "claude")
        again = decide({"session_id": session, "hook_event_name": "UserPromptSubmit"}, "codex")
        after = decide({"session_id": session, "hook_event_name": "SessionStart", "source": "compact"}, "claude")
        print(first)
        print("\n--- %d characters; second call in the same session: %s; after a compaction: %s" % (
            len(first), "silent" if not again else "SPOKE AGAIN", "speaks" if after else "SILENT"))
        return 0 if first and not again and after else 1
    try:
        raw = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8-sig", errors="replace").read()
        out = decide(json.loads(raw) if raw.strip() else {}, runtime)
        if out:
            sys.stdout.write(out)
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
