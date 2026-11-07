"""Controls for bm25.refresh_in_memory(found=): the caller's own scan stands in for a second one.

 F1 with found, the folder is not scanned again and the merged payload equals the one from a fresh scan
 F2 found=None scans once, as before
 F3 an empty found pair returns (None, 0, 0) without loading the index
 F4 a control: a found pair different from the scan changes the answer (the pair is what gets merged)

    python test_refresh_found.py      (a second; ALL PASS at the end; temp folder only)
"""
if __name__ == "__main__" and __import__("sys").argv[1:2] in (["-h"], ["--help"]):
    print((__doc__ or "").strip() or "run with no arguments")
    raise SystemExit(0)

import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bm25

results = []
N_CHECKS = 5


def check(ok, what):
    results.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + what)


tmp = tempfile.mkdtemp(prefix="refresh_found_")
saved = (bm25.fresh_memories, bm25._load_payload, bm25.read_merge_frozen)
scans, loads = [], []
PAIR = (["m1", "m2"], ["old"])


def fake_fresh(mem_dir, out, *a, **k):
    scans.append(1)
    return list(PAIR[0]), list(PAIR[1])


def fake_load(out):
    loads.append(1)
    return {"n": 2, "avgdl": 2.0, "df": {"graph": 2, "walk": 1, "stale": 1},
            "dl": {"old": 2, "keep": 2}, "tf": {"old": {"graph": 1, "stale": 1}, "keep": {"graph": 1, "walk": 1}}}


try:
    mem = os.path.join(tmp, "mem")
    os.makedirs(mem)
    for slug, text in (("m1", "spectral graph bound"), ("m2", "random walk limit measure")):
        with open(os.path.join(mem, slug + ".md"), "w", encoding="utf-8", newline="") as f:
            f.write("---\nname: %s\ndescription: \"%s\"\n---\n\n%s\n" % (slug, text, text))
    out = os.path.join(tmp, "index.json")
    bm25.fresh_memories, bm25._load_payload, bm25.read_merge_frozen = fake_fresh, fake_load, lambda o: False

    scanned = bm25.refresh_in_memory(mem, out)
    n_scan = len(scans)
    del scans[:]
    given = bm25.refresh_in_memory(mem, out, found=(list(PAIR[0]), list(PAIR[1])))
    check(given == scanned and given[1] == 2 and given[2] == 1 and not scans,
          "F1 with found: no second scan, same payload, added 2, removed 1")
    check(n_scan == 1, "F2 found=None scans the folder once")

    del loads[:]
    check(bm25.refresh_in_memory(mem, out, found=([], [])) == (None, 0, 0) and not loads and not scans,
          "F3 an empty found pair returns (None, 0, 0) without loading the index")

    other = bm25.refresh_in_memory(mem, out, found=(["m1"], []))
    check(other != scanned and other[1] == 1 and other[2] == 0 and "old" in other[0]["tf"],
          "F4 control: a different found pair changes the merged payload")
    check("m2" not in other[0]["tf"] and "m2" in scanned[0]["tf"] and "old" not in scanned[0]["tf"],
          "F4 control: only the documents named in the pair are merged or dropped")
except Exception as e:
    check(False, "raised %s: %s" % (type(e).__name__, e))
finally:
    bm25.fresh_memories, bm25._load_payload, bm25.read_merge_frozen = saved
    shutil.rmtree(tmp, ignore_errors=True)

ok = all(results) and len(results) == N_CHECKS
print("ALL PASS" if ok else "FAILED %d of %d" % (N_CHECKS - results.count(True), N_CHECKS))
sys.exit(0 if ok else 1)
