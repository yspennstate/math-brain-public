"""Controls for heed_weekly_report.section_corrections counting both MISTAKES.md entry forms (27 Sep, an agent).

Points each module's MEM at a temporary directory holding a small MISTAKES-shaped ledger, so the controls read and
write nothing live, and compares the live report with the version before the change (the brain repository at
91e123ea40, or a path given as the first argument). Last, both versions count the live ledger, read-only.

    python test_heed_corrections_count.py [OLD_HEED_WEEKLY_REPORT_PY]
"""
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

DR = os.path.dirname(os.path.abspath(__file__))
FAILS = []
NOW = time.mktime((2026, 9, 27, 12, 0, 0, 0, 0, -1))     # the window is 20 Sep 12:00 - 27 Sep 12:00

BOTH = """# Corrections

- **2026-09-24 (a bold entry inside the window)** -> wrong: x. Lesson: y; reflex: none yet
- **2026-09-10 (a bold entry outside the window)** -> wrong: x.
- 2026-09-25 06:10 local time (agentx, topic): a dated entry inside the window. Rule: z.
  - 2026-09-26 an indented dated sub-item that belongs to the entry above
- 2026-09-22 (agentx): another dated entry inside the window that cites **2026-08-01** in passing.
- 2026-09-02 (agentx): a dated entry outside the window.
A sentence mentioning 2026-09-26 in the middle of some prose.
"""
NOISE = """# Corrections

  - 2026-09-26 an indented dated item with no parent
A sentence mentioning 2026-09-26 in the middle of some prose.
-- 2026-09-25 a rule line, not a bullet
"""
BOLD_ONLY = """# Corrections

- **2026-09-21 morning** one. Lesson: a.
- **2026-09-26** two, which cites **2026-09-23** mid-text.
- **2026-08-30** three, outside the window.
"""


def load(path, name):
    if not path.endswith(".py"):                  # the loader only takes a .py name
        dst = os.path.join(tempfile.mkdtemp(prefix="heed_old_"), name + ".py")
        shutil.copy(path, dst)
        path = dst
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def old_path(tmp):
    if len(sys.argv) > 1:
        return sys.argv[1]
    repo = os.path.join(os.path.expanduser("~"), "brain-repo")
    blob = subprocess.run(["git", "-C", repo, "show", "91e123ea40:12_cognitive_architecture/dreaming/heed_weekly_report.py"],
                          capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
    if "def section_corrections" not in blob:
        raise SystemExit("could not read the old report from git history; pass its path as the first argument")
    p = os.path.join(tmp, "heed_weekly_report_old.py")
    open(p, "w", encoding="utf-8").write(blob)
    return p


def count(mod, text, now=NOW):
    d = tempfile.mkdtemp(prefix="heed_mem_")
    open(os.path.join(d, "MISTAKES.md"), "w", encoding="utf-8").write(text)
    mod.MEM = d                                   # read at call time, not bound as a default argument
    line = mod.section_corrections(now)[0]
    m = re.search(r"last 7d: (\d+)", line)
    return int(m.group(1)) if m else None


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  " + detail) if detail and not ok else ""))
    if not ok:
        FAILS.append(name)


def main():
    tmp = tempfile.mkdtemp(prefix="heed_test_")
    new = load(os.path.join(DR, "heed_weekly_report.py"), "heed_live")
    old = load(old_path(tmp), "heed_old")
    live_mem = new.MEM
    n, o = count(new, BOTH), count(old, BOTH)
    check("1 both forms inside the window count (1 bold + 2 dated)", n == 3, "got %s" % n)
    check("2 the old report counted only the bold one", o == 1, "got %s" % o)
    z = count(new, NOISE)
    check("3 an indented dated item, a date in prose and a '--' line do not count", z == 0, "got %s" % z)
    bn, bo = count(new, BOLD_ONLY), count(old, BOLD_ONLY)
    check("4 a ledger in the bold form alone counts exactly as before", bn == bo == 3, "new %s old %s" % (bn, bo))
    now = time.time()
    ln, lo = count(new, open(os.path.join(live_mem, "MISTAKES.md"), encoding="utf-8").read(), now), None
    lo = count(old, open(os.path.join(live_mem, "MISTAKES.md"), encoding="utf-8").read(), now)
    print("live ledger, last 7 days: %s now, %s before the change" % (ln, lo))
    check("5 on the live ledger the new count is at least the old one", ln is not None and lo is not None and ln >= lo)
    print("%d of 5 controls pass" % (5 - len(FAILS)))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
