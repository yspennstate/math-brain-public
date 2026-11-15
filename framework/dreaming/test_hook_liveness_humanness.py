"""Controls for hook_liveness._humanness_check_status (13 Nov 2026): a weekly humanness run that ends without a
RESULT line must raise the alarm; a run with a result must not.

    python -X utf8 test_hook_liveness_humanness.py [--module path/to/hook_liveness.py]

Builds throwaway log folders; nothing live is read or written.
"""
import importlib.util
import os
import shutil
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]
MOD = os.path.abspath(ARGS[ARGS.index("--module") + 1]) if "--module" in ARGS else os.path.join(HERE, "hook_liveness.py")
NOW = time.time()
DAY = 86400.0
RUN = "04:31:15 running woken session on the voice battery (claude -p, ~1-3 min)\n"
KILL = "04:39:23 WATCHDOG: check exceeded 8 min - killing\n"
PASS = "04:33:02 RESULT: PASS - no AI-tells, idiolect present. The mind still reads human.\n04:33:02 humanness check complete\n"
REGR = "04:33:02 RESULT: REGRESSION - AI-tells crept into a woken session.\n"
WEAK = "04:33:02 RESULT: WEAK - no AI-tells but little idiolect.\n"


def load():
    spec = importlib.util.spec_from_file_location("hook_liveness_under_test", MOD)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def folder(root, name, logs):
    """logs: list of (age in days, text); files get a BOM like the PowerShell writer's."""
    d = os.path.join(root, name)
    os.makedirs(d)
    for i, (age, text) in enumerate(logs):
        p = os.path.join(d, "humanness_check_2026%04d_000000.log" % i)
        with open(p, "w", encoding="utf-8-sig", newline="\r\n") as fh:
            fh.write(text)
        t = NOW - age * DAY
        os.utime(p, (t, t))
    return d


def main():
    m = load()
    if not hasattr(m, "_humanness_check_status"):
        print("ABSENT: this hook_liveness.py has no _humanness_check_status")
        return 1
    f = m._humanness_check_status
    root = tempfile.mkdtemp(prefix="hl_humanness_")
    checks = []
    try:
        line, bad = f(folder(root, "three_dead", [(4, RUN + KILL), (11, RUN + KILL), (18, RUN + KILL), (25, RUN + PASS)]), NOW)
        checks.append(("three killed runs raise the alarm", len(bad) == 1 and "3 run(s) in a row" in bad[0]))
        checks.append(("and the line says result NONE", "result NONE" in line))
        line, bad = f(folder(root, "healthy", [(3, RUN + PASS), (10, RUN + KILL)]), NOW)
        checks.append(("a pass after an old kill is quiet", bad == [] and "result PASS" in line))
        line, bad = f(folder(root, "weak", [(2, RUN + WEAK)]), NOW)
        checks.append(("WEAK is quiet (not a hard fail)", bad == [] and "result WEAK" in line))
        line, bad = f(folder(root, "regression", [(2, RUN + REGR)]), NOW)
        checks.append(("REGRESSION is reported", len(bad) == 1 and "REGRESSION" in bad[0]))
        line, bad = f(folder(root, "stale", [(20, RUN + PASS)]), NOW)
        checks.append(("a pass 20 days old says the task looks dead", len(bad) == 1 and "20 days ago" in bad[0]))
        line, bad = f(folder(root, "in_flight", [(0.005, RUN), (4, RUN + PASS)]), NOW)
        checks.append(("a run in flight is not judged", bad == [] and "in flight" in line))
        line, bad = f(folder(root, "in_flight_after_dead", [(0.005, RUN), (4, RUN + KILL)]), NOW)
        checks.append(("a run in flight does not hide the dead one before it", len(bad) == 1 and "1 run(s) in a row" in bad[0]))
        line, bad = f(folder(root, "hung", [(0.05, RUN)]), NOW)
        checks.append(("a log 72 min old with no result counts as dead", len(bad) == 1))
        line, bad = f(folder(root, "empty", []), NOW)
        checks.append(("no log at all is stated, not alarmed", bad == [] and "never ran" in line))
        line, bad = f(folder(root, "dead_and_stale", [(15, RUN + KILL)]), NOW)
        checks.append(("dead and stale gives both problems", len(bad) == 2))
    finally:
        shutil.rmtree(root, ignore_errors=True)
    failed = [n for n, ok in checks if not ok]
    for n, ok in checks:
        print("%-58s %s" % (n, "ok" if ok else "FAIL"))
    print("%s - %d controls, %d failed" % ("PASS" if not failed else "FAIL", len(checks), len(failed)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
