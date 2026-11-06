"""Controls for spread_recall's description cache (_file_desc, _fdesc_save).

 D1 a first lookup reads the file's description and records it
 D2 with the prompt's shared folder read in _MEM_STATS, a cached entry is answered without calling os.stat
 D3 a shared stat that differs from the recorded one reads the file again
 D4 SPREAD_DESC_STATS=0 stats the file even when _MEM_STATS is set
 D5 the save merges into entries another process wrote since this one read the file
 D6 a file missing from _MEM_STATS falls back to os.stat (and a missing file gives "")

    python test_desc_cache_stats.py      (a second; ALL PASS at the end)
"""
if "-h" in __import__("sys").argv[1:] or "--help" in __import__("sys").argv[1:]:
    print((__doc__ or "").strip() or "usage: python %s" % __import__("os").path.basename(__file__))
    raise SystemExit(0)
import marshal
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
TMP = tempfile.mkdtemp(prefix="desc_cache_")
os.environ["HOME"] = os.environ["USERPROFILE"] = TMP
os.environ.pop("SPREAD_DESC_STATS", None)
import spread_recall as sr

results = []


def check(ok, what):
    results.append(ok)
    print(("PASS  " if ok else "FAIL  ") + what)


mem = os.path.join(TMP, "memory")
os.makedirs(mem)
sr.MEM = mem
sr.DESC_CACHE = os.path.join(TMP, "desc_cache.marshal")


def write(slug, desc):
    with open(os.path.join(mem, slug + ".md"), "w", encoding="utf-8") as fh:
        fh.write('---\nname: %s\ndescription: "%s"\n---\nbody\n' % (slug, desc))
    s = os.stat(os.path.join(mem, slug + ".md"))
    return (s.st_size, s.st_mtime_ns)


def fresh():
    sr._FDESC.clear()


st_a = write("alpha", "first note")
st_b = write("beta", "second note")
fresh()
sr._MEM_STATS = None
check(sr._file_desc("alpha") == "first note" and sr._FDESC["c"]["alpha"][:2] == st_a, "D1 read and recorded")

real_stat = os.stat
calls = []


def counting_stat(p, *a, **k):
    calls.append(p)
    return real_stat(p, *a, **k)


sr._MEM_STATS = {"alpha.md": st_a, "beta.md": st_b}
os.stat = counting_stat
try:
    got = sr._file_desc("alpha")
    check(got == "first note" and not calls, "D2 the shared stat answers the cached entry, no os.stat")

    sr._MEM_STATS = {"alpha.md": (st_a[0] + 1, st_a[1]), "beta.md": st_b}
    sr._FDESC["c"]["alpha"] = (st_a[0] + 1 - 1, st_a[1], "stale text")
    check(sr._file_desc("alpha") == "first note", "D3 a differing stat reads the file again")

    calls.clear()
    os.environ["SPREAD_DESC_STATS"] = "0"
    sr._MEM_STATS = {"alpha.md": st_a}
    sr._file_desc("alpha")
    check(len(calls) == 1, "D4 SPREAD_DESC_STATS=0 stats the file")
    del os.environ["SPREAD_DESC_STATS"]
finally:
    os.stat = real_stat

fresh()
if os.path.exists(sr.DESC_CACHE):
    os.remove(sr.DESC_CACHE)
sr._MEM_STATS = {"alpha.md": st_a, "beta.md": st_b}
sr._file_desc("alpha")
with open(sr.DESC_CACHE, "wb") as fh:            # another hook saved its own entry meanwhile
    marshal.dump({"other": (1, 2, "theirs")}, fh)
sr._fdesc_save()
with open(sr.DESC_CACHE, "rb") as fh:
    disk = marshal.load(fh)
check(disk.get("other") == (1, 2, "theirs") and disk.get("alpha", (0, 0, ""))[2] == "first note",
      "D5 the save merges with what another process wrote")

fresh()
sr._MEM_STATS = {"alpha.md": st_a}
check(sr._file_desc("beta") == "second note" and sr._file_desc("missing") == "", "D6 not in the shared read: os.stat")

print("ALL PASS" if all(results) else "FAILED %d of %d" % (results.count(False), len(results)))
sys.exit(0 if all(results) else 1)
