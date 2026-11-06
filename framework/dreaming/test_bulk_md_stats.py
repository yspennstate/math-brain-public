"""Controls for the bulk .md folder read in embedding_artifact.

 B1 on Windows, _bulk_md_stats returns exactly what scandir plus a stat gives: every regular .md file, its size
    and its modification time in ns; other suffixes and a folder named *.md are left out
 B2 a folder of several thousand files (more than one 1 MiB buffer) reads complete and equal
 B3 a handoff left in _PREFETCH for the same folder is returned once, then the folder is read again
 B4 a handoff for another folder, or older than 60 s, is not used
 B5 a missing folder gives None, so the caller's scandir runs (and fails the way it always did)
 B6 optional: BULK_STAT_DIR=<folder> compares a real folder the same way

Off Windows and macOS the reader gives None by design; B1-B2 are then skipped.
    python test_bulk_md_stats.py      (a few seconds; ALL PASS at the end)
"""
if "-h" in __import__("sys").argv[1:] or "--help" in __import__("sys").argv[1:]:
    print((__doc__ or "").strip() or "usage: python %s" % __import__("os").path.basename(__file__))
    raise SystemExit(0)
import os
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import embedding_artifact as ea

results = []


def check(ok, what):
    results.append(ok)
    print(("PASS  " if ok else "FAIL  ") + what)


def scan(d):
    with os.scandir(d) as it:
        return {e.name: (st.st_size, st.st_mtime_ns) for e in it if e.name.endswith(".md") and e.is_file()
                for st in (e.stat(),)}


TMP = tempfile.mkdtemp(prefix="bulk_md_")
small = os.path.join(TMP, "small")
os.makedirs(os.path.join(small, "folder.md"))
for i, name in enumerate(["a.md", "b.md", "notes.txt", "c.md.bak", "long_name_" + "x" * 120 + ".md"]):
    with open(os.path.join(small, name), "w", encoding="utf-8") as fh:
        fh.write("y" * (10 * i + 1))
big = os.path.join(TMP, "big")
os.makedirs(big)
for i in range(6000):
    with open(os.path.join(big, "memory_%05d_%s.md" % (i, "z" * (i % 40))), "w", encoding="utf-8") as fh:
        fh.write("w" * (i % 97))

native = os.name == "nt" or sys.platform == "darwin"
if native:
    got = ea._bulk_md_stats(small)
    check(got == scan(small) and len(got) == 3 and "folder.md" not in got, "B1 equal to scandir, only regular .md files")
    got = ea._bulk_md_stats(big)
    check(got == scan(big) and len(got) == 6000, "B2 a 6,000-file folder reads complete and equal")
else:
    print("SKIP  B1-B2: no bulk reader on this system")

marker = {"m.md": (1, 2)}
ea._PREFETCH = (small, time.monotonic(), marker)
first = ea._bulk_md_stats(small)
second = ea._bulk_md_stats(small)
check(first is marker and second is not marker and ea._PREFETCH is None, "B3 a handoff is used once, then read again")

ea._PREFETCH = (big, time.monotonic(), marker)
a = ea._bulk_md_stats(small)
ea._PREFETCH = (small, time.monotonic() - 61, marker)
b = ea._bulk_md_stats(small)
check(a is not marker and b is not marker, "B4 another folder's or a stale handoff is not used")

check(ea._bulk_md_stats(os.path.join(TMP, "missing")) is None, "B5 a missing folder gives None")

real = os.environ.get("BULK_STAT_DIR")
if real and native:
    check(ea._bulk_md_stats(real) == scan(real), "B6 the real folder reads equal to scandir")

print("ALL PASS" if all(results) else "FAILED %d of %d" % (results.count(False), len(results)))
sys.exit(0 if all(results) else 1)
