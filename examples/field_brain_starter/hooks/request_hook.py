"""UserPromptSubmit hook: write each request into the request ledger, and say so when it has been asked before.

Every prompt with at least three content words becomes an ask event in the ledger (requests.jsonl beside
recall.py, or --ledger, or $MATH_BRAIN_REQUESTS; see docs/prompts-as-nodes.md). Slash commands and short
follow-ups ("ok do it", "yes") are left out: they mean something only beside the request before them. The event
is the one math_brain.requests writes, with the same id for the same words, so the library, recall.py and the
dream agenda all count it.

The hook prints nothing for a new request. When the same request is already in the ledger it tells the model how
often it was asked, since when, whether it was answered and by which records. A request asked again after it was
answered is the case to notice: the answer did not land, and handing over the same record again will not help.

Run it a second time under Stop with --stop and it links the records written during the turn to the request the turn
was working on: a record created in memory/ since that request (or since the last stop) gets a `produced` link. A
short follow-up ("ok do it") keeps working on the request before it, so its records go there too. Whether a record
ANSWERS the request is a judgement, left to the agent or the dream (ledger.py link ... answered_by); `produced`
only says the record came out of that work. Two agents writing into one store at once can be credited with each
other's records; the dream sees every link and can drop a wrong one by answering it.

Codex (default):   prints {"hookSpecificOutput": {"hookEventName": ..., "additionalContext": ...}}
Claude Code:       --runtime claude prints the lines as plain text

    python3 hooks/request_hook.py --selftest    # ask one request twice in a scratch ledger and show the reply

This hook knows a request again only by its words. With the package installed, `python -m math_brain.request_hook`
also finds earlier requests that are merely similar; use one of the two, not both, or every prompt is recorded twice.

Wire it under UserPromptSubmit beside recall_hook.py. Standard library only. Any error prints nothing and writes
nothing more: a hook must never block a turn.
"""
import hashlib
import io
import json
import os
import re
import sys
import tempfile
import unicodedata
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
MIN_WORDS = 3
MEM = os.environ.get("BRAIN_MEM_DIR", os.path.join(os.path.dirname(HERE), "memory"))
STATE = os.environ.get("BRAIN_HOOK_STATE", os.path.join(HERE, ".state"))

# The next four are math_brain.requests' own rules, copied so the starter needs no install. Change them together.
STOP = frozenset(
    "a an and are as at be by can do does for from has have how i if in is it its me of on or show that the "
    "this to was we what when where which who why will with you".split()
)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
WIN_HOME = re.compile(r"[A-Za-z]:[\\/]+Users[\\/]+[^\\/\s\"']+", re.IGNORECASE)
NIX_HOME = re.compile(r"/(?:home|Users)/[^/\s\"']+", re.IGNORECASE)


def normalize(text):
    text = unicodedata.normalize("NFKD", text or "")
    text = "".join(c for c in text if not unicodedata.combining(c)).lower()
    return " ".join(re.findall(r"[a-z0-9]+", text))


def redact(text):
    return NIX_HOME.sub("<home>", WIN_HOME.sub("<home>", EMAIL.sub("<email>", text)))


def content_words(text):
    return {w for w in normalize(text).split() if w not in STOP and len(w) > 1}


def request_id(text):
    return "req_" + hashlib.sha1(normalize(text).encode("utf-8")).hexdigest()[:12]


def default_ledger():
    return os.environ.get("MATH_BRAIN_REQUESTS") or os.path.join(os.path.dirname(HERE), "requests.jsonl")


def record_names(mem):
    try:
        return sorted(n[:-3] for n in os.listdir(mem) if n.endswith(".md") and not n[:-3].isupper())
    except OSError:
        return []


def state_path(state, session):
    return os.path.join(state, "request_" + re.sub(r"[^A-Za-z0-9_-]", "_", session)[:80] + ".json")


def remember_turn(state, session, rid, mem):
    """Note which request this session is on and which records existed when it was asked."""
    if not session:
        return
    os.makedirs(state, exist_ok=True)
    with open(state_path(state, session), "w", encoding="utf-8") as fh:
        json.dump({"id": rid, "records": record_names(mem)}, fh)


def link_made(ledger, state, session, mem, at=None):
    """At a stop: link every record created since the request (or the last stop) to it as produced."""
    path = state_path(state, session) if session else ""
    if not path or not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as fh:
        turn = json.load(fh)
    now_names = record_names(mem)
    made = [n for n in now_names if n not in set(turn["records"])]
    at = at or datetime.now(timezone.utc).isoformat(timespec="seconds")
    with open(ledger, "a", encoding="utf-8") as fh:
        for n in made:
            fh.write(json.dumps({"op": "link", "id": turn["id"], "node": n, "rel": "produced", "at": at},
                                ensure_ascii=False, sort_keys=True) + "\n")
    turn["records"] = now_names
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(turn, fh)
    return made


def record(prompt, ledger, at=None, session="", state=STATE, mem=MEM):
    """Append the ask; return the lines for the model ("" for a new request, or one that was left out)."""
    text = redact(prompt).strip()
    if not text or text.startswith("/") or len(content_words(text)) < MIN_WORDS:
        return ""
    rid = request_id(text)
    remember_turn(state, session, rid, mem)
    before = None
    if os.path.exists(ledger):
        import recall
        before = recall.load_requests(ledger).get(rid)
    at = at or datetime.now(timezone.utc).isoformat(timespec="seconds")
    event = {"op": "ask", "id": rid, "text": text, "role": "researcher", "at": at}
    folder = os.path.dirname(os.path.abspath(ledger))
    os.makedirs(folder, exist_ok=True)
    with open(ledger, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
    if before is None:
        return ""
    times = before["times"] + 1
    line = "[requests] %s: asked %dx since %s." % (rid, times, before["first"][:10])
    if before["status"] == "answered" or before["reopened"]:
        line += (" It was answered before and is being asked again, so the answer did not land: say what changed"
                 " or what the earlier answer missed rather than handing over the same record.")
    elif before["status"] == "dropped":
        line += " It was dropped earlier; ask whether it is wanted again before working on it."
    else:
        line += " It is still open."
    for rel in ("answered_by", "produced"):
        if before[rel]:
            line += "\n  %s: %s" % (rel.replace("_", " "), ", ".join(before[rel]))
    return line


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
    ledger = argv[argv.index("--ledger") + 1] if "--ledger" in argv else default_ledger()
    if "--selftest" in argv:
        scratch = os.path.join(tempfile.mkdtemp(), "requests.jsonl")
        q = "How long should the harbour film be for the festival?"
        print("first ask: %r" % record(q, scratch, at="2026-03-09T09:00:00+00:00"))
        with open(scratch, "a", encoding="utf-8") as fh:
            fh.write(json.dumps({"op": "link", "id": request_id(q), "rel": "answered_by", "at": "2026-03-10T09:00:00+00:00",
                                 "node": "project_harbour_film_cut_to_twelve_minutes_2026_03_10"}, sort_keys=True) + "\n")
        print("asked again after the answer:\n" + record(q, scratch, at="2026-04-02T09:00:00+00:00"))
        print("short follow-up: %r" % record("ok do it", scratch))
        return 0
    try:
        raw = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8", errors="replace").read()
        payload = json.loads(raw) if raw.strip() else {}
        session = str(payload.get("session_id") or "")
        if "--stop" in argv:
            link_made(ledger, STATE, session, MEM)   # silent: a Stop hook that prints may be read as an order
            return 0
        prompt = str(payload.get("prompt") or "")
        event = str(payload.get("hook_event_name") or "UserPromptSubmit")
        if prompt.strip():
            emit(record(prompt, ledger, session=session), runtime, event)
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
