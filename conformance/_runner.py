"""Run the public tools in-process and reduce their printout to the fields a check compares.

Shared by make_cases.py (which writes the reference cases) and verify_install.py (which replays them).
Standard library only; works the same on Linux, macOS and Windows.
"""
import contextlib
import hashlib
import importlib
import io
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repository root
AGENT_TOOLS = os.path.join(ROOT, "agent_tools")
NAVIGATION = os.path.join(ROOT, "navigation")

# A test replay must not write usage logs into the user's home: these switch the logging off.
QUIET_ENV = {"MATH_STRENGTH_NOLOG": "1", "MATHBRAIN_USE_LOG": "0"}

HIT = re.compile(r"^\[(\d+)\] (.*?)  \(id: (\S+?); (\w+); score ([0-9.]+)\)\s*$")
WEAK = re.compile(r"^WEAK MATCH")
WALK_HEAD = re.compile(r"\(id: (\S+?)[;)]")
LINK_COUNT = re.compile(r"(\d+) links?\b")


def prepare_env():
    for k, v in QUIET_ENV.items():
        os.environ.setdefault(k, v)
    # In a live session the hook gives up after 60 s and stays silent. Here it runs in this process, where an
    # abandoned search thread keeps running and slows every later case, so the ceiling is off; the seconds
    # each case took are recorded and the report counts the cases a live session would have timed out on.
    os.environ.setdefault("MATHBRAIN_HARD_DEADLINE_S", "0")
    # The hook's own search budget is 30 s. A loaded laptop needed 72-87 s per prompt and the hook stayed silent
    # (budget_exhausted_before_ranking), which compares nothing. The check gives it ten minutes so it compares what the
    # hook serves; the report counts separately the cases slower than the live 30 s.
    os.environ.setdefault("MATHBRAIN_TIME_BUDGET_S", "600")
    for p in (AGENT_TOOLS, NAVIGATION):
        if p not in sys.path:
            sys.path.insert(0, p)


def _module(name):
    prepare_env()
    if name in sys.modules:
        return sys.modules[name]
    return importlib.import_module(name)


class _Sink(io.StringIO):
    """A captured stream that accepts the tools' sys.stdout.reconfigure(encoding="utf-8") call."""
    encoding = "utf-8"

    def reconfigure(self, *a, **k):
        return None


def capture(fn, argv=None, stdin_text=None):
    """Call fn(argv) (or fn()) with stdout and stderr captured; return (rc, stdout, stderr, seconds)."""
    out, err = _Sink(), _Sink()
    old_in = sys.stdin
    t0 = time.time()
    rc = None
    try:
        if stdin_text is not None:
            sys.stdin = io.StringIO(stdin_text)
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                rc = fn(argv) if argv is not None else fn()
            except SystemExit as e:   # argparse and early exits
                rc = e.code
    finally:
        sys.stdin = old_in
    return rc, out.getvalue(), err.getvalue(), round(time.time() - t0, 3)


def recall(argv):
    return capture(_module("math_recall").main, list(argv))


def parse_search(text):
    hits, weak = [], False
    for line in text.splitlines():
        m = HIT.match(line)
        if m:
            hits.append({"rank": int(m.group(1)), "title": m.group(2), "id": m.group(3),
                         "kind": m.group(4), "score": float(m.group(5))})
        elif WEAK.match(line):
            weak = True
    return {"ids": [h["id"] for h in hits], "titles": [h["title"] for h in hits],
            "scores": [h["score"] for h in hits], "weak": weak, "n": len(hits)}


def parse_walk(text):
    """The walked card's id, its first line of text hashed, and the link lines' target ids (short or long)."""
    lines = text.splitlines()
    head_id = None
    for line in lines[:6]:
        m = WALK_HEAD.search(line)
        if m:
            head_id = m.group(1)
            break
    body = "\n".join(lines[1:])
    link_targets = sorted(set(re.findall(r"\b(?:claim|audit_revision|node|edge)_[0-9a-f]{8,}\b", body)))
    return {"id": head_id, "text_sha16": hashlib.sha256(body.encode("utf-8")).hexdigest()[:16],
            "n_lines": len(lines), "link_targets": link_targets}


def hook(prompt, session_id):
    """Feed one UserPromptSubmit event to math_sense.py and return what it emitted."""
    payload = json.dumps({"hook_event_name": "UserPromptSubmit", "session_id": session_id,
                          "prompt": prompt, "cwd": ROOT})
    ms = _module("math_sense")
    return capture(lambda: ms.main(), None, stdin_text=payload)


def silence_log_path():
    """Where math_sense.py writes one line per silent exit for a test (non-uuid) session id."""
    d = os.path.join(os.path.expanduser("~"), ".claude", "dreaming")
    os.makedirs(d, exist_ok=True)   # the hook writes nothing if the folder is missing
    return os.path.join(d, "mathbrain_silence_harness.tsv")


def hook_with_reason(prompt, session_id):
    """hook(), plus the hook's own silence lines written during the call (why it stayed quiet, if it did)."""
    p = silence_log_path()
    before = os.path.getsize(p) if os.path.exists(p) else 0
    rc, out, err, sec = hook(prompt, session_id)
    reasons = []
    if os.path.exists(p):
        with open(p, encoding="utf-8", errors="replace") as fh:
            fh.seek(before)
            for line in fh.read().splitlines():
                parts = line.split("\t")
                if len(parts) >= 3:   # only lines appended during this call are read
                    reasons.append(parts[2])
    return rc, out, err, sec, reasons


def parse_hook(stdout):
    s = stdout.strip()
    if not s:
        return {"served": False, "ids": [], "chars": 0, "shape_ok": True}
    try:
        d = json.loads(s.splitlines()[-1])
        ctx = d["hookSpecificOutput"]["additionalContext"]
        ok = d["hookSpecificOutput"].get("hookEventName") == "UserPromptSubmit"
    except Exception:
        return {"served": True, "ids": [], "chars": len(s), "shape_ok": False}
    ids = sorted(set(re.findall(r"\b(?:claim|audit_revision)_[0-9a-f]{8,}\b", ctx)))
    return {"served": True, "ids": ids, "chars": len(ctx), "shape_ok": ok}


def nav(argv):
    nq = _module("nav_query")
    fn = getattr(nq, "main")
    return capture(fn, list(argv))


def parse_nav(text):
    ids = re.findall(r"\b(?:nav|file|dir|concept|section)[:_][\w./:-]+", text)
    return {"ids": ids[:10], "n_lines": len(text.splitlines())}


def overlap(a, b, k):
    """How many of the first k of b appear in the first k of a; ids may be shortened prefixes on either side."""
    a, b = a[:k], b[:k]
    n = 0
    for y in b:
        if any(x.startswith(y) or y.startswith(x) for x in a):
            n += 1
    return n
