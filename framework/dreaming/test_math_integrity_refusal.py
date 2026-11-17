"""test_math_integrity_refusal.py - a selected card the integrity read refuses refuses the math hook's block
(29 Sep 2026).

    python test_math_integrity_refusal.py [MATH_SENSE.py] [--old OLD_MATH_SENSE.py]

Runs the hook in this process on one synthetic question the live store answers with several cards, in shadow mode
(MATHBRAIN_SHADOW=1) and with a harness session id, and makes the integrity read refuse one of the selected cards. The
store is only read.
 R1 no card refused: the block is served (the control the other rows are read against)
 R2 the first card refused: nothing is served, and the silence names the refusal
 R3 the last card refused: nothing is served
 R4 the integrity budget runs out and the grace read refuses the top card: nothing is served
 R5 the budget runs out and the top card reads back sound: the top card alone is served, as before
    (R4 and R5 are the grace path)
With --old, the hook before this change serves a block when its first card is refused - the runner-up, moved first
(the check can fail).
"""
import importlib.machinery
import importlib.util
import io
import json
import os
import sys

os.environ["MATHBRAIN_SHADOW"] = "1"
HERE = os.path.dirname(os.path.abspath(__file__))
BUILD_SRC = r"~\math-brain-build\src"
ARGS = sys.argv[1:]
MS = os.path.abspath(ARGS[0]) if ARGS and not ARGS[0].startswith("--") else os.path.join(HERE, "math_sense.py")
OLD = os.path.abspath(ARGS[ARGS.index("--old") + 1]) if "--old" in ARGS else None
DREAMING = os.path.join(os.path.expanduser("~"), ".claude", "dreaming")   # the hook's sibling modules
sys.path.insert(0, DREAMING)
sys.path.insert(0, BUILD_SRC)
sys.path.insert(0, HERE)

import math_brain.selection_integrity as SI  # noqa: E402
from math_brain.current_note import NoteReadError, read_current_note  # noqa: E402

QUESTION = "Is every group of prime order cyclic, and how does Lagrange's theorem give that?"
fails, ran = [], []
REFUSE = {"which": None, "exhaust_first_call": False}
GIVEN = []
_real = SI.consistent_hits


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def refusing_consistent_hits(hits, database, **kw):
    hits = list(hits)
    GIVEN.append([h.node.id for h in hits])
    if REFUSE["exhaust_first_call"] and len(GIVEN) == 1:
        raise SI.SelectionUnavailable("integrity_budget_exhausted")     # the first read ran out of time
    which = REFUSE["which"]
    refused = set()
    if which == "first" and hits:
        refused = {hits[0].node.id}
    elif which == "last" and hits:
        refused = {hits[-1].node.id}

    def read(db, node_id, artifact_root=None):
        if node_id in refused:
            raise NoteReadError("stored_node_digest_mismatch")
        return read_current_note(db, node_id, artifact_root=artifact_root)
    return _real(hits, database, reader=read, **kw)


def load(path, name):
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


def ask(m, which, tag, exhaust=False):
    REFUSE["which"], REFUSE["exhaust_first_call"] = which, exhaust
    GIVEN.clear()
    reasons = []
    real_note = m._silence_note
    m._silence_note = lambda data, reason, harness_only=False: (reasons.append(reason),
                                                                 real_note(data, reason, harness_only))
    real_in, real_out = sys.stdin, sys.stdout
    sys.stdin = io.StringIO(json.dumps({"prompt": QUESTION, "session_id": "r69test-" + tag}))
    sys.stdout = io.StringIO()
    try:
        m.main()
    except SystemExit:
        pass
    finally:
        printed = sys.stdout.getvalue()
        sys.stdin, sys.stdout = real_in, real_out
        m._silence_note = real_note
    return printed.strip(), list(GIVEN), reasons


def main():
    SI.consistent_hits = refusing_consistent_hits
    try:
        m = load(MS, "ms_r69_new")
        served, given, reasons = ask(m, None, "none")
        check(bool(served) and given and len(given[0]) >= 2,
              "R1 no card refused: the block is served (%d cards selected, %d chars)"
              % (len(given[0]) if given else 0, len(served)))
        served, given, reasons = ask(m, "first", "first")
        check(not served and any("selected_card_refused" in r for r in reasons),
              "R2 the first card refused: nothing served; silence %r" % reasons[-2:])
        served, given, reasons = ask(m, "last", "last")
        check(not served and any("selected_card_refused" in r for r in reasons),
              "R3 the last card refused: nothing served; silence %r" % reasons[-2:])
        served, given, reasons = ask(m, "first", "grace-first", exhaust=True)
        check(not served and len(given) == 2 and len(given[1]) == 1
              and any("selected_card_refused" in r for r in reasons),
              "R4 budget exhausted, grace read refuses the top card: nothing served; calls %r; silence %r"
              % ([len(g) for g in given], reasons[-2:]))
        served, given, reasons = ask(m, None, "grace-sound", exhaust=True)
        check(bool(served) and len(given) == 2 and len(given[1]) == 1
              and any("grace_top_card" in r for r in reasons),
              "R5 budget exhausted, top card sound: the top card alone is served (calls %r, %d chars)"
              % ([len(g) for g in given], len(served)))
        if OLD:
            o = load(OLD, "ms_r69_old")
            served, given, reasons = ask(o, "first", "old-first")
            check(bool(served), "N1 the hook before this change serves a block when its first card is refused "
                  "(%d chars; the check can fail)" % len(served))
    finally:
        SI.consistent_hits = _real
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
