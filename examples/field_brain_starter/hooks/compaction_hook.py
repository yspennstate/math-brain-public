"""Keep every context compaction as a record, so the next session can read what this one was doing.

When an agent's context fills up, the runtime replaces the conversation with a summary the agent writes itself: what
it was asked, what it finished, what it still owes, where it stopped. That summary is the session's own account of its
work, and it is usually lost the next time the context is cleared. This hook files it in memory/ as a project record,
the same format new_record.py writes, so recall.py finds it, check_store.py checks it, and the dream links it.

Each saved compaction:
- is named compaction_<session>_<hash>_<date> and indexed in MEMORY.md, newest first;
- links to the same session's previous compaction ([[...]] under Related), so a long session reads as a chain;
- is linked in the request ledger as `produced` by the request the session was working on (from request_hook.py's
  state), so asking about the request later also finds the compaction;
- has e-mail addresses and home folders replaced (<email>, <home>), like every request in the ledger.
The same summary seen twice (a hook that fires again, a backfill over a transcript already read) is saved once.

Claude Code: wire it under SessionStart with the matcher "compact". After a compaction the runtime starts the
session again with source "compact"; the hook reads the newest compaction summary from the transcript and prints one
line naming the saved record.
Codex has no compaction event. Wire it under UserPromptSubmit: on each prompt it reads the end of the session's
rollout and saves a compaction it has not seen. A Codex compaction whose summary is stored only in encrypted form has
no text to save, and is skipped.

    python3 hooks/compaction_hook.py --selftest                 # two compactions and a repeat, in a scratch store
    python3 hooks/compaction_hook.py --backfill FILE [FILE ...]  # every compaction in old transcripts, oldest first

hooks/print_wiring.py prints the block for both runtimes. Standard library only. Any error prints nothing and
writes nothing more: a hook must never block a session.
"""
import hashlib
import io
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
MEM = os.environ.get("BRAIN_MEM_DIR", os.path.join(ROOT, "memory"))
STATE = os.environ.get("BRAIN_HOOK_STATE", os.path.join(HERE, ".state"))
TAIL = 4 * 1024 * 1024    # the newest compaction is near the end of the transcript
MAX_BODY = 40000          # a summary longer than this is cut, with a note saying so


def text_of(content):
    """Message content as plain text: a string, or the text parts of a list of blocks."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text")
    return ""


def summary_of(rec):
    """The compaction summary in one transcript line, or "" if the line is not a compaction.

    Claude Code marks the summary message with isCompactSummary. Codex writes a record of type "compacted" whose
    payload carries the summary as message (older builds: summary)."""
    if not isinstance(rec, dict):
        return ""
    if rec.get("isCompactSummary") is True:
        return text_of((rec.get("message") or {}).get("content")).strip()
    pay = rec.get("payload") if isinstance(rec.get("payload"), dict) else rec
    if rec.get("type") == "compacted" or pay.get("type") == "compacted":
        text = pay.get("message") or pay.get("summary") or ""
        return text_of(text).strip() if not isinstance(text, str) else text.strip()
    return ""


def compactions(path, tail=None):
    """Every (time, summary) in a transcript, oldest first; with tail, only those in its last `tail` bytes."""
    found = []
    with open(path, "rb") as fh:
        if tail:
            fh.seek(0, 2)
            fh.seek(max(0, fh.tell() - tail))
        data = fh.read()
    for raw in data.split(b"\n"):
        if b"isCompactSummary" not in raw and b"compacted" not in raw:
            continue
        try:
            rec = json.loads(raw.decode("utf-8", "replace"))
        except ValueError:
            continue    # the first line of a tail read is usually cut
        text = summary_of(rec)
        if text:
            found.append((str(rec.get("timestamp") or ""), text))
    return found


def load_state(state):
    path = os.path.join(state, "compactions.json")
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {"seen": {}, "last": {}}


def save_state(state, data):
    os.makedirs(state, exist_ok=True)
    path = os.path.join(state, "compactions.json")
    with open(path + ".tmp", "w", encoding="utf-8") as fh:
        json.dump(data, fh)
    os.replace(path + ".tmp", path)


def gist(text, n=150):
    """The first sentence or so, for the record's description and index line."""
    line = " ".join(text.split())
    line = re.sub(r"<([a-z-]+)>.*?</\1>", " ", line)    # lists the runtime wraps in tags (tools used, and so on)
    line = re.sub(r"(?:This session is being continued|The summary below covers)[^.]*\.\s*", "", line)
    line = re.sub(r"^\s*(?:Summary:\s*)?(?:1\.\s*Primary Request and Intent:?\s*)?", "", line).strip()
    return line[:n].rstrip() + ("..." if len(line) > n else "")


def save(summary, session, when, mem=MEM, state=STATE, ledger=None):
    """File one compaction as a record. Returns its slug, or None when the same summary was saved before."""
    import new_record
    import request_hook
    text = request_hook.redact(summary)
    key = hashlib.sha1(" ".join(text.split()).encode("utf-8")).hexdigest()
    st = load_state(state)
    if key in st["seen"]:
        return None
    try:
        at = datetime.fromisoformat(when.replace("Z", "+00:00")) if when else datetime.now(timezone.utc)
    except ValueError:
        at = datetime.now(timezone.utc)
    sess = re.sub(r"[^a-z0-9]", "", (session or "nosession").lower())[:8] or "nosession"
    slug = "compaction_%s_%s_%s" % (sess, key[:8], at.strftime("%Y_%m_%d"))
    path = os.path.join(mem, slug + ".md")
    desc = "Compaction of session %s at %s: %s" % (sess, at.strftime("%Y-%m-%d %H:%M"), gist(text))
    body = text if len(text) <= MAX_BODY else text[:MAX_BODY] + "\n\n[cut at %d characters]" % MAX_BODY
    out = ["---", "name: " + slug, "description: " + desc.replace("\n", " "), "metadata:", "  type: project",
           "status: provisional", "---", "",
           "The session's own summary of its work when its context was compacted. It says what the session was",
           "asked, did and still owed at that moment; check anything it calls done before relying on it.", "", body]
    prev = st["last"].get(session or "")
    if prev and os.path.exists(os.path.join(mem, prev + ".md")):
        out += ["", "Related: [[%s]] (the same session's previous compaction)." % prev]
    os.makedirs(mem, exist_ok=True)
    new_record.write_atomic(path, "\n".join(out) + "\n")
    with new_record.IndexLock(mem):
        index = os.path.join(mem, "MEMORY.md")
        lines = open(index, encoding="utf-8").read().splitlines() if os.path.exists(index) else ["# Memory index"]
        first = next((i for i, l in enumerate(lines) if l.startswith("- ")), len(lines))
        lines.insert(first, "- [%s](%s.md) - [PROVISIONAL] %s" % (slug, slug, desc))
        new_record.write_atomic(index, "\n".join(lines) + "\n")
    turn = os.path.join(state, "request_" + re.sub(r"[^A-Za-z0-9_-]", "_", session or "")[:80] + ".json")
    if session and ledger and os.path.exists(turn):
        try:
            with open(turn, encoding="utf-8") as fh:
                rid = json.load(fh)["id"]
            with open(ledger, "a", encoding="utf-8") as fh:
                fh.write(json.dumps({"op": "link", "id": rid, "node": slug, "rel": "produced",
                                     "at": datetime.now(timezone.utc).isoformat(timespec="seconds")},
                                    sort_keys=True) + "\n")
        except (OSError, ValueError, KeyError):
            pass
    st["seen"][key] = slug
    st["last"][session or ""] = slug
    save_state(state, st)
    return slug


def emit(text, runtime, event):
    if not text:
        return
    if runtime == "claude":
        sys.stdout.write(text + "\n")
    else:
        sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": text}}))


def selftest():
    import check_store
    work = tempfile.mkdtemp(prefix="brain_compaction_")
    mem, state = os.path.join(work, "memory"), os.path.join(work, "state")
    ledger = os.path.join(work, "requests.jsonl")
    os.makedirs(state)
    with open(os.path.join(state, "request_s1.json"), "w", encoding="utf-8") as fh:
        json.dump({"id": "req_000000000001", "records": []}, fh)
    claude = os.path.join(work, "claude.jsonl")
    lines = [{"type": "user", "message": {"content": "Cut the harbour film to twelve minutes."}},
             {"type": "user", "isCompactSummary": True, "timestamp": "2026-03-09T10:00:00Z",
              "message": {"content": "Summary: cutting the harbour film; the opening is done, the storm scene is next."}},
             {"type": "user", "isCompactSummary": True, "timestamp": "2026-03-09T14:00:00Z",
              "message": {"content": [{"type": "text", "text": "Summary: the cut runs 12:04; the storm scene is done. "
                                       "Mail the editor at someone@example.org with the file in C:\\Users\\ana\\cuts."}]}}]
    with open(claude, "w", encoding="utf-8") as fh:
        fh.write("\n".join(json.dumps(x) for x in lines) + "\n")
    codex = os.path.join(work, "codex.jsonl")
    with open(codex, "w", encoding="utf-8") as fh:
        fh.write(json.dumps({"type": "compacted", "timestamp": "2026-03-10T08:00:00Z",
                             "payload": {"message": "Summary: the support queue is down to four tickets."}}) + "\n")
    made = [save(t, "s1", w, mem, state, ledger) for w, t in compactions(claude)]
    again = [save(t, "s1", w, mem, state, ledger) for w, t in compactions(claude, tail=TAIL)]
    other = [save(t, "c2", w, mem, state, ledger) for w, t in compactions(codex)]
    second = open(os.path.join(mem, made[1] + ".md"), encoding="utf-8").read() if made[1] else ""
    links = [json.loads(l) for l in open(ledger, encoding="utf-8")] if os.path.exists(ledger) else []
    errors = check_store.check(mem)[0]
    checks = [
        ("both Claude compactions saved", all(made) and len(made) == 2),
        ("the second links to the first", made[0] and ("[[%s]]" % made[0]) in second),
        ("e-mail and home folder redacted", "<email>" in second and "<home>" in second and "ana" not in second),
        ("the same summaries again save nothing", again == [None, None]),
        ("the Codex compaction saved", other[0] is not None),
        ("the request ledger links the request to both", sum(1 for l in links if l.get("rel") == "produced") == 2),
        ("check_store finds no errors", not errors),
    ]
    for name, ok in checks:
        print("%s  %s" % ("ok  " if ok else "FAIL", name))
    if errors:
        print("\n".join("        " + e for e in errors[:5]))
    bad = sum(1 for _, ok in checks if not ok)
    print("compaction_hook selftest:", "ok" if not bad else "%d failure(s)" % bad)
    return 1 if bad else 0


def main():
    argv = sys.argv[1:]
    runtime = argv[argv.index("--runtime") + 1] if "--runtime" in argv else "codex"
    import request_hook
    ledger = request_hook.default_ledger()
    if "--selftest" in argv:
        return selftest()
    if "--backfill" in argv:
        files = argv[argv.index("--backfill") + 1:]
        files = [f for f in files if not f.startswith("--")]
        n = 0
        for path in files:
            session = os.path.splitext(os.path.basename(path))[0]
            for when, text in compactions(path):
                n += save(text, session, when, ledger=ledger) is not None
        print("saved %d compaction(s) from %d file(s)" % (n, len(files)))
        return 0
    try:
        raw = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8", errors="replace").read()
        payload = json.loads(raw) if raw.strip() else {}
        path = str(payload.get("transcript_path") or "")
        if not path or not os.path.exists(path):
            return 0
        found = compactions(path, tail=TAIL)
        if not found:
            return 0
        when, text = found[-1]
        slug = save(text, str(payload.get("session_id") or ""), when, ledger=ledger)
        if slug:
            emit("[compaction] this session's summary is saved as %s; `python recall.py --id %s` reads it back."
                 % (slug, slug), runtime, str(payload.get("hook_event_name") or "SessionStart"))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
