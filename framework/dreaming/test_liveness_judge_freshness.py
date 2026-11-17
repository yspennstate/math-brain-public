"""test_liveness_judge_freshness.py - the waking liveness report says when the reflex judge or its precision table has
stopped, on a 36-hour clock (29 Sep 2026).

    python test_liveness_judge_freshness.py [--module HOOK_LIVENESS.py] [--old OLD_HOOK_LIVENESS.py]

hook_liveness.main() runs with its folder pointed at a throwaway directory (so the streams it reads and the two files it
writes are the fixture's) and with its git, GitHub and Codex probes stubbed; its report is read from stdout.
 J1 verdicts and table written 20 hours ago: both "fresh"
 J2 written 40 hours ago: both "STALE", named in the report's DATA-FLOW section
 J3 another stream 40 hours old stays fresh (the three-day clock is unchanged for the rest)
With --old, the module before this change must not name either file at 40 hours (the check can fail).
"""
import contextlib
import importlib.machinery
import importlib.util
import io
import os
import shutil
import sys
import tempfile
import time

if __name__ == "__main__" and ("-h" in sys.argv[1:] or "--help" in sys.argv[1:]):
    print(__doc__)
    sys.exit(0)

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]
MOD = os.path.abspath(ARGS[ARGS.index("--module") + 1]) if "--module" in ARGS else os.path.join(HERE, "hook_liveness.py")
OLD = os.path.abspath(ARGS[ARGS.index("--old") + 1]) if "--old" in ARGS else None
fails, ran = [], []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def load(path, name):
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


def report(path, name, hours):
    """hook_liveness's DATA-FLOW lines with the two judge files and outcomes.jsonl written `hours` ago"""
    td = tempfile.mkdtemp(prefix="liveness_judge_")
    try:
        m = load(path, name)
        m.HERE = td
        m.SNAP = os.path.join(td, ".hook_liveness_snap.json")
        for fn in ("_dream_commits_unpushed", "_last_dream_commit_age", "_index_coverage"):
            if hasattr(m, fn):
                setattr(m, fn, lambda *a, **k: None)
        if hasattr(m, "_codex_sessions_in_window"):
            m._codex_sessions_in_window = lambda *a, **k: False
        t = time.time() - hours * 3600.0
        for fn in ("judged_nightly.jsonl", "reflex_precision.json", "outcomes.jsonl"):
            p = os.path.join(td, fn)
            with open(p, "w", encoding="utf-8") as fh:
                fh.write("{}\n")
            os.utime(p, (t, t))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            try:
                m.main()
            except SystemExit:
                pass
        text = out.getvalue()
        start = text.find("DATA-FLOW")
        end = text.find("FIRE-RECENCY", start)
        return text[start:end if end > 0 else None]
    finally:
        shutil.rmtree(td, ignore_errors=True)


def line_of(section, fn):
    return next((ln.strip() for ln in section.splitlines() if ln.strip().startswith(fn)), "")


def main():
    fresh = report(MOD, "hl_new_20", 20)
    stale = report(MOD, "hl_new_40", 40)
    j, r = line_of(fresh, "judged_nightly.jsonl"), line_of(fresh, "reflex_precision.json")
    check("fresh" in j and "fresh" in r, "J1 20 hours: %s | %s" % (j, r))
    j, r = line_of(stale, "judged_nightly.jsonl"), line_of(stale, "reflex_precision.json")
    check("STALE" in j and "STALE" in r, "J2 40 hours: %s | %s" % (j, r))
    o = line_of(stale, "outcomes.jsonl")
    check("fresh" in o, "J3 another stream at 40 hours keeps the three-day clock: %s" % o)
    if OLD:
        old = report(OLD, "hl_old_40", 40)
        check(not line_of(old, "judged_nightly.jsonl") and not line_of(old, "reflex_precision.json"),
              "N1 the module before this change does not watch either file (the check can fail): %r, %r" % (
                  line_of(old, "judged_nightly.jsonl"), line_of(old, "reflex_precision.json")))
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
