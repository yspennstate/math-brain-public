# every structure name the script accepts with 16..21 inputs, by family; print the ones with no result file and their
# class count (the script's orbit pass).  usage: python3 missing_names.py CODEDIR RESULTDIR
import sys
import os
import itertools
sys.path.insert(0, sys.argv[1])
import sym_search as S

R = sys.argv[2]
LO, HI = 16, 21
names = []
for a in range(1, 22):
    for b in range(1, 22):
        if LO <= a * b <= HI and a >= 2 and b >= 2:
            names.append("wr_%d_%d" % (a, b))
for depth in (3, 4):
    for t in itertools.product(range(2, 8), repeat=depth):
        p = 1
        for x in t:
            p *= x
        if LO <= p <= HI:
            names.append("wn_" + "_".join(map(str, t)))


def parts(n, mx):
    if n == 0:
        yield ()
    for k in range(min(n, mx), 1, -1):
        for r in parts(n - k, k):
            yield (k,) + r


for n in range(LO, HI + 1):
    for p in parts(n, n - 2):
        if 2 <= len(p) <= 4:
            names.append("pr_" + "_".join(map(str, p)))
for a in range(1, 9):
    for b in range(a, 12):
        E = a * b
        if a >= 2 and LO <= E + a + b <= HI:
            names.append("ev_k%dx%d" % (a, b))
        if a >= 2 and LO <= 2 * E <= HI:
            names.append("ec_k%dx%d" % (a, b))
for a in range(2, 9):
    for b in range(2, 12):
        if LO <= a * b + a <= HI:
            names.append("eh_k%dx%d" % (a, b))
for n in range(4, 8):
    E = n * (n - 1) // 2
    if LO <= E + n <= HI:
        names.append("ev_k%d" % n)
    if LO <= 2 * E <= HI:
        names.append("ec_k%d" % n)
    if LO <= n * (n - 1) <= HI:
        names.append("dg_%d" % n)
    for k in range(2, n - 1):
        import math
        if LO <= math.comb(n, k) <= HI and 2 * k <= n:
            names.append("sub_%d_%d" % (n, k))
names += ["ev_octa", "ec_octa"]
for a in range(2, 6):
    for b in range(a, 6):
        for c in range(b, 11):
            if LO <= a * b * c <= HI:
                names.append("g3_%d_%d_%d" % (a, b, c))
for q in (7, 8, 9, 11, 13, 16, 17, 19):
    for fam, n in (("psl", q + 1), ("pl", q + 1), ("plf", q + 1), ("ap", q), ("al", q), ("alf", q)):
        if LO <= n <= HI:
            names.append("%s_%d" % (fam, q))
        if LO <= 2 * n <= HI:
            names.append("%s_%dc" % (fam, q))
names += ["gl_4", "af_4", "gl_3c", "af_3c", "m11c", "m11t", "m12", "bs_3", "bs_4", "bs_5",
          "fanoc", "fanoc2", "ag23c", "q3vc", "w33c", "pg23", "s8c", "s9c", "s10c", "k33cx1", "k33cx2",
          "ag24", "pg24", "k33c", "k33v", "k34", "k44", "k5c", "k6",
          "gv_heawood", "gv_mobkan", "gv_pappus", "gv_desarg", "gv_dodec", "gv_clebsch", "gv_shrik"]
seen = set()
have = set(os.listdir(R))
miss = 0
for nm in names:
    if nm in seen:
        continue
    seen.add(nm)
    if "sy_%s.txt" % nm in have:
        continue
    try:
        m, gens, _ = S.struct(nm)
    except (SystemExit, Exception) as e:
        print("%s REFUSED %s" % (nm, str(e)[:60]), flush=True); continue
    if not (LO <= m <= HI):
        continue
    reps, cls, sizes = S.orbits(m, gens)
    miss += 1
    print("MISSING %s m %d classes %d" % (nm, m, len(reps)), flush=True)
print("names tried %d, missing %d" % (len(seen), miss))
