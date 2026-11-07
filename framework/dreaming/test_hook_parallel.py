"""test_hook_parallel.py - the dispatcher starts the hooks that run as their own process together.

    python test_hook_parallel.py [--module HOOK_DISPATCH.py] [--old OLD_HOOK_DISPATCH.py]

Three UserPromptSubmit hooks, each its own process that sleeps SLEEP seconds and prints one line, through dispatch()
on a temporary settings file:
 H1 parallel is at least 1.5 x SLEEP faster than HOOK_PARALLEL_SUBPROC=0 (the old one-after-another loop)
 H2 both runs return the same results, in the settings order
 H3 a hook past its budget is killed and reported (rc 1, "timed out"), and the others still arrive
 H4 PreToolUse stays one after another (the event is not in PARALLEL_SUBPROC_EVENTS)
 H5 _unthrottle never raises, and is off with HOOK_UNTHROTTLE=0
With --old, the dispatcher before this change must fail H1 (the check can fail).
"""
import importlib.machinery
import importlib.util
import json
import os
import shutil
import sys
import tempfile
import time

if __name__ == "__main__" and ("-h" in sys.argv[1:] or "--help" in sys.argv[1:]):
    print(__doc__)
    sys.exit(0)

HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.abspath(sys.argv[sys.argv.index("--module") + 1]) if "--module" in sys.argv else os.path.join(HERE, "hook_dispatch.py")
OLD = os.path.abspath(sys.argv[sys.argv.index("--old") + 1]) if "--old" in sys.argv else None
SLEEP = 2.0


def load(path, name):
    if HERE not in sys.path:
        sys.path.insert(0, HERE)
    loader = importlib.machinery.SourceFileLoader(name, path)
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    m.log = lambda *a, **k: None        # the controls do not write the dispatcher's log
    return m


def settings(tmp, event, sleeps):
    blocks = [{"hooks": [{"type": "command", "command": sys.executable,
                          "args": ["-c", "import sys,time; sys.stdin.read(); time.sleep(%g); print('[h%d] done')" % (s, k)]}
                         for k, s in enumerate(sleeps, 1)]}]
    path = os.path.join(tmp, "settings_%s_%d.json" % (event, len(sleeps)))
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"hooks": {event: blocks}}, fh)
    return path


def run(m, event, path, parallel):
    os.environ["HOOK_PARALLEL_SUBPROC"] = "1" if parallel else "0"
    payload = json.dumps({"prompt": "hello", "session_id": "test-parallel", "hook_event_name": event})
    t = time.perf_counter()
    code, out, err, results = m.dispatch(event, payload, None, settings_path=path, force=True, session="test-parallel")
    return time.perf_counter() - t, [(r[1], (r[2] or "").strip()) for r in results]


def cases(m, tmp):
    r = {}
    p3 = settings(tmp, "UserPromptSubmit", [SLEEP, SLEEP, SLEEP])
    seq_t, seq_r = run(m, "UserPromptSubmit", p3, False)
    par_t, par_r = run(m, "UserPromptSubmit", p3, True)
    r["H1"] = (seq_t - par_t >= 1.5 * SLEEP, "H1 parallel %.1f s vs one after another %.1f s" % (par_t, seq_t))
    want = [(0, "[h%d] done" % k) for k in (1, 2, 3)]
    r["H2"] = (seq_r == want and par_r == want, "H2 same results in settings order: %s / %s" % (par_r, seq_r))
    if hasattr(m, "_Spawned"):
        old_budget = m.budget_for
        m.budget_for = lambda event: SLEEP + 3.0
        try:
            pt = settings(tmp, "UserPromptSubmit", [0.1, 60, 0.1])
            t, res = run(m, "UserPromptSubmit", pt, True)
        finally:
            m.budget_for = old_budget
        ok = res[0] == (0, "[h1] done") and res[2] == (0, "[h3] done") and res[1][0] == 1 and t < 30
        r["H3"] = (ok, "H3 a hook past its budget: %.1f s, %s" % (t, res))
    else:
        r["H3"] = (False, "H3 no _Spawned in this dispatcher")
    r["H4"] = ("PreToolUse" not in getattr(m, "PARALLEL_SUBPROC_EVENTS", {"PreToolUse"}),
               "H4 PreToolUse is not started in parallel")
    try:
        a = m._unthrottle()
        os.environ["HOOK_UNTHROTTLE"] = "0"
        b = m._unthrottle()
        r["H5"] = (isinstance(a, bool) and b is False, "H5 _unthrottle -> %r, off -> %r" % (a, b))
    except Exception as e:
        r["H5"] = (False, "H5 _unthrottle raised %r" % (e,))
    finally:
        os.environ.pop("HOOK_UNTHROTTLE", None)
    return r


def main():
    tmp = tempfile.mkdtemp(prefix="hookpar_")
    try:
        fails = []
        r = cases(load(MOD, "hd_under_test"), tmp)
        for k in sorted(r):
            ok, what = r[k]
            print(("PASS  " if ok else "FAIL  ") + what)
            if not ok:
                fails.append(k)
        if OLD:
            ro = cases(load(OLD, "hd_old"), tmp)
            ok = not ro["H1"][0]
            print(("PASS  " if ok else "FAIL  ") + "control: the old dispatcher fails H1 (%s)" % ro["H1"][1])
            if not ok:
                fails.append("control")
        print("ALL PASS" if not fails else "FAILED: " + " ".join(fails))
        return 1 if fails else 0
    finally:
        os.environ.pop("HOOK_PARALLEL_SUBPROC", None)
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
