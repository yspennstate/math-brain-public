"""test_claim_vectors_backup_rotation.py - the claim-vector writer keeps the newest three dated copies of the file and
drops the older ones (12 Nov 2026, an agent; peer note of an agent, mesh topic
math-claim-vecs-backup-rotation: a 185 MB copy a day had piled up to 66 files).

    python test_claim_vectors_backup_rotation.py [--vecs MATH_CLAIM_VECS.py] [--old-vecs OLD.py]

Everything happens in a temporary folder; the live vector file is never opened.
 R1  a good write with five older dated copies leaves the newest three (today's and the two before it); the dropped
     copies' manifests go with them and the kept copies keep theirs
 R2  a write whose read-back check fails drops nothing
 R3  names of any other shape are left alone
 R4  a .tmp<pid>.npz another process left more than seven days ago is removed; a fresh one stays; one named for this
     process stays whatever its age
 R5  with fewer copies than the limit nothing is removed
 R6  a dropped copy that cannot be removed (held open, Windows) does not fail the write
With --old-vecs, the writer before this change keeps all six copies (N1), so R1 can fail.
"""
import importlib.machinery
import importlib.util
import os
import sys
import tempfile
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]


def _arg(flag, default=None):
    return os.path.abspath(ARGS[ARGS.index(flag) + 1]) if flag in ARGS else default


VECS = _arg("--vecs", os.path.join(HERE, "math_claim_vecs.py"))
OLD_VECS = _arg("--old-vecs")
fails = []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    if not ok:
        fails.append(what)


def load(py, name):
    # an explicit loader: the copy kept from before a change does not end in .py
    spec = importlib.util.spec_from_file_location(name, py, loader=importlib.machinery.SourceFileLoader(name, py))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


OUT = {"ids": np.array(["a", "b"]), "vecs": np.ones((2, 4), dtype=np.float32)}
TODAY = time.strftime("%Y%m%d", time.gmtime())
OLD_DAYS = ["20260901", "20260902", "20261005", "20261109", "20261110"]   # all before today


def put(folder, name, age_days=0.0, body=b"x"):
    full = os.path.join(folder, name)
    with open(full, "wb") as fh:
        fh.write(body)
    if age_days:
        t = time.time() - age_days * 86400
        os.utime(full, (t, t))
    return full


def fixture(days=OLD_DAYS):
    d = tempfile.mkdtemp(prefix="cvrot_")
    path = os.path.join(d, "claim_embeddings.npz")
    np.savez(path, **OUT)
    for day in days:
        put(d, "claim_embeddings.npz.bak_" + day, body=b"copy " + day.encode())
        put(d, "claim_embeddings.npz.bak_%s.sha256" % day, body=b"0" * 64)
    return d, path


def copies(d):
    return sorted(n for n in os.listdir(d) if ".bak_" in n and not n.endswith(".sha256"))


mv = load(VECS, "mcv_new")

# R1
d, path = fixture()
msg = mv._write(path, OUT, lambda back: True)
want = ["claim_embeddings.npz.bak_" + x for x in ("20261109", "20261110", TODAY)]
check(msg == "" and copies(d) == want, "R1 newest three copies kept after a good write: %s" % copies(d))
left = sorted(n for n in os.listdir(d) if ".bak_" in n and n.endswith(".sha256"))
check(left == [n + ".sha256" for n in want], "R1 dropped copies' manifests gone, kept copies' manifests there")
check(os.path.exists(path) and os.path.exists(path + ".sha256"), "R1 the file and its manifest are in place")

# R2
d, path = fixture()
msg = mv._write(path, OUT, lambda back: False)
check(msg != "" and len(copies(d)) == len(OLD_DAYS) + 1, "R2 a refused write drops nothing (%d copies)" % len(copies(d)))

# R3
d, path = fixture()
others = ["claim_embeddings.npz.bak_2026111", "claim_embeddings.npz.bak_20261101x", "claim_embeddings.npz.bak_notadate",
          "claim_embeddings.next.npz", "claim_embeddings.npz.lock", "other.npz.bak_20260101",
          "claim_embeddings.npz.bak_20260101.tmp", "claim_embeddings.npz.sha256.tmp123", "claim_embeddings.npz.tmpabc.npz"]
for n in others:
    put(d, n, age_days=30)
mv._write(path, OUT, lambda back: True)
check(all(os.path.exists(os.path.join(d, n)) for n in others), "R3 names of other shapes left alone")

# R4
d, path = fixture(days=[])
stale = put(d, "claim_embeddings.npz.tmp999991.npz", age_days=8)
fresh = put(d, "claim_embeddings.npz.tmp999992.npz", age_days=1)
edge = put(d, "claim_embeddings.npz.tmp999993.npz", age_days=6.9)
mv._write(path, OUT, lambda back: True)
check(not os.path.exists(stale), "R4 another process's temporary file, 8 days old, removed")
check(os.path.exists(fresh) and os.path.exists(edge), "R4 temporary files 1 and 6.9 days old stay")
mine = put(d, "claim_embeddings.npz.tmp%d.npz" % os.getpid(), age_days=30)
got = mv._prune(path)
check(os.path.exists(mine) and got == [], "R4 this process's own temporary file stays whatever its age")

# R5
d, path = fixture(days=["20261110"])
mv._write(path, OUT, lambda back: True)
check(len(copies(d)) == 2, "R5 fewer copies than the limit: nothing removed")

# R6
if os.name == "nt":
    d, path = fixture()
    held = open(os.path.join(d, "claim_embeddings.npz.bak_20260901"), "rb")
    try:
        msg = mv._write(path, OUT, lambda back: True)
    finally:
        held.close()
    check(msg == "" and "claim_embeddings.npz.bak_20260901" in copies(d) and len(copies(d)) == 4,
          "R6 a copy held open stays and the write still succeeds: %s" % copies(d))
else:
    print("SKIP  R6 (the held-open refusal is a Windows behaviour)")

# N1
if OLD_VECS:
    old = load(OLD_VECS, "mcv_old")
    d, path = fixture()
    old._write(path, OUT, lambda back: True)
    check(len(copies(d)) == len(OLD_DAYS) + 1, "N1 the writer before the change keeps all %d copies" % len(copies(d)))

print("--- %d failed" % len(fails))
sys.exit(1 if fails else 0)
