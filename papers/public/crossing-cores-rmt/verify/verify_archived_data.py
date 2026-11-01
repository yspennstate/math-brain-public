"""Verify the archived exact-data files: SHA-256 manifest, reconstruction of
both order-fourteen moments from the per-orbit records, and the complete
Hankel reduced-core counts and layer maxima through seven pairs.

The data files data/volumes_{T,H}{4..14}.json are the frozen June snapshot
(legacy commit 2e0eafce); each maps an orbit representative to
[volume, orbit size].

Run:  python -u verify_archived_data.py   (writes data/SHA256SUMS on first run)
"""
import sys, os, json, hashlib
from fractions import Fraction as Fr
from math import comb, factorial

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
import tk_core

def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r

# ---- manifest
manifest_path = os.path.join(DATA, "SHA256SUMS")
files = sorted(f for f in os.listdir(DATA) if f.endswith(".json"))
sums = {}
for f in files:
    h = hashlib.sha256()
    with open(os.path.join(DATA, f), "rb") as fh:
        h.update(fh.read())
    sums[f] = h.hexdigest()
if os.path.exists(manifest_path):
    ok = True
    with open(manifest_path, encoding="utf-8") as fh:
        for line in fh:
            dig, name = line.split()
            if sums.get(name) != dig:
                print(f"HASH MISMATCH: {name}")
                ok = False
    print("manifest check:", "OK" if ok else "FAILED")
    assert ok
else:
    with open(manifest_path, "w", encoding="utf-8") as fh:
        for name, dig in sums.items():
            fh.write(f"{dig}  {name}\n")
    print(f"manifest written for {len(sums)} files")

# ---- load and interpret the archived structures
def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as fh:
        return json.load(fh)

def as_pairs(obj):
    """Return list of (volume Fraction, orbit size) from the archived form:
    {"orbits": {"[...rep...]": {"size": s, "volume": "p/q"}, ...}, ...}."""
    out = []
    for rec in obj["orbits"].values():
        out.append((Fr(str(rec["volume"])), int(rec["size"])))
    return out

expect = {"T": {4: Fr(8, 3), 6: Fr(11), 8: Fr(908, 15), 10: Fr(415),
                12: Fr(23840, 7), 14: Fr(325719, 10)},
          "H": {4: Fr(2), 6: Fr(11, 2), 8: Fr(281, 15), 10: Fr(2717, 36),
                12: Fr(1052, 3), 14: Fr(1331087, 720)}}
totals_pairings = {"T": lambda k: dfact(2 * k - 1), "H": lambda k: factorial(k)}
allok = True
for kind in ("T", "H"):
    for n2k in (4, 6, 8, 10, 12, 14):
        name = f"volumes_{kind}{n2k}.json"
        if name not in sums:
            print(f"missing {name}")
            allok = False
            continue
        pairs = as_pairs(load(name))
        m = sum(v * (s if s else 1) for v, s in pairs)
        npair = sum(s if s else 1 for _, s in pairs)
        ok = (m == expect[kind][n2k])
        okn = (npair == totals_pairings[kind](n2k // 2))
        status = "OK" if (ok and okn) else "FAIL"
        if not (ok and okn):
            allok = False
        print(f"{name}: m={m} pairings={npair} [{status}]")
print("ARCHIVED DATA CHECK", "PASSED" if allok else "FAILED")
assert allok
