"""Controls for the per-prompt hook's shared memory-folder read (spread_recall._mem_names and _load_superseded).

 F1 outside the hook (_SHARE_LIST off) the name scan lists the folder with os.listdir, as before
 F2 in the hook the scan takes the bulk stat read: the same .md names, _MEM_STATS holds their stats, and the read is
    left in embedding_artifact._PREFETCH for the loader's next call
 F3 that handoff is taken once by the next _bulk_md_stats call for the folder
 F4 SPREAD_SHARED_LIST=0 lists as before
 F5 MEM_NAMES, when set by a caller, still wins
 F6 supersession gets the shared read's slugs as known_slugs in the hook, and None outside it
 F7 the lightweight loader's own folder read (memory_stats) becomes _MEM_STATS

    python test_shared_folder_read.py      (a few seconds; ALL PASS at the end)
"""
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
TMP = tempfile.mkdtemp(prefix="shared_read_")
os.environ["HOME"] = os.environ["USERPROFILE"] = TMP
os.environ.pop("SPREAD_SHARED_LIST", None)
import embedding_artifact as ea
import spread_recall as sr

results = []


def check(ok, what):
    results.append(ok)
    print(("PASS  " if ok else "FAIL  ") + what)


mem = os.path.join(TMP, "memory")
os.makedirs(mem)
for name in ["alpha_note.md", "beta_note.md", "MEMORY.md", "notes.txt"]:
    with open(os.path.join(mem, name), "w", encoding="utf-8") as fh:
        fh.write(name)
sr.MEM = mem
native = ea._bulk_md_stats(mem) is not None
ea._PREFETCH = None

sr._SHARE_LIST, sr._MEM_STATS = False, None
check(sorted(sr._mem_names()) == sorted(os.listdir(mem)) and sr._MEM_STATS is None, "F1 outside the hook: os.listdir")

if native:
    sr._SHARE_LIST = True
    names = sr._mem_names()
    md = sorted(n for n in os.listdir(mem) if n.endswith(".md"))
    check(sorted(names) == md and sorted(sr._MEM_STATS) == md and ea._PREFETCH is not None
          and ea._PREFETCH[2] is sr._MEM_STATS, "F2 in the hook: the bulk read's .md names, stats kept, handed on")
    held = ea._PREFETCH[2]
    check(ea._bulk_md_stats(mem) is held and ea._PREFETCH is None, "F3 the handoff is taken once")
else:
    print("SKIP  F2-F3: no bulk reader on this system")

sr._SHARE_LIST, sr._MEM_STATS = True, None
os.environ["SPREAD_SHARED_LIST"] = "0"
check(sorted(sr._mem_names()) == sorted(os.listdir(mem)) and sr._MEM_STATS is None, "F4 SPREAD_SHARED_LIST=0 lists")
del os.environ["SPREAD_SHARED_LIST"]

sr.MEM_NAMES = lambda: ["given.md"]
check(sr._mem_names() == ["given.md"], "F5 MEM_NAMES wins")
sr.MEM_NAMES = None

seen = []
sr.active_supersessions = lambda mem_dir, index_path=None, known_slugs=None: seen.append(known_slugs) or {}
sr._MEM_STATS = None
sr._load_superseded()
sr._SHARE_LIST = False
sr._load_superseded()
want = {"alpha_note", "beta_note", "MEMORY"} if native else None
check(seen[0] == want and seen[1] is None, "F6 supersession gets the shared slugs in the hook, None outside")


class Loaded:
    memory_stats = {"x.md": (1, 2)}


ea.load_verified_embeddings_lightweight = lambda *a, **k: Loaded()
sr._MEM_STATS = None
try:
    got = sr._load_embeddings()
except Exception as e:
    got = e
check(isinstance(got, Loaded) and sr._MEM_STATS == {"x.md": (1, 2)}, "F7 the loader's folder read becomes _MEM_STATS")

print("ALL PASS" if all(results) else "FAILED %d of %d" % (results.count(False), len(results)))
sys.exit(0 if all(results) else 1)
