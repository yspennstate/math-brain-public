"""Line-containment cores on PG(2,3) (13 points) and AG(2,4) (16 points, chosen parallel classes), balanced by
holes, searched over partial cores invariant under a group of collineations (exact balance).
usage: python run_lines.py pg23|ag24 restarts iters T0 T1 [group: full|singer|...]
"""
import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import sys, time, itertools, json
import numpy as np
import designs
from orbits import group_closure
from orbsa2 import Model2
from balsa import balance_greedy, anneal_bal
from holecore import summarize

name = sys.argv[1]; restarts = int(sys.argv[2]); iters = int(sys.argv[3])
T0 = float(sys.argv[4]); T1 = float(sys.argv[5]); grp = sys.argv[6] if len(sys.argv) > 6 else 'full'


def pg23_lines():
    m, perms, pts = designs.pg_group(3, 3, [[[1, 1, 0], [0, 1, 0], [0, 0, 1]]])
    lines = []
    for a, b in itertools.combinations(range(len(pts)), 2):
        pa, pb = np.array(pts[a]), np.array(pts[b])
        L = set()
        for s in range(3):
            for t in range(3):
                if s or t:
                    w = tuple(int(x) % 3 for x in s * pa + t * pb)
                    L.add(pts.index(designs._normalize(w, 3)))
        L = frozenset(L)
        if L not in lines:
            lines.append(L)
    return pts, lines


if name == 'pg23':
    pts, lines = pg23_lines()
    m = 13
    if grp == 'full':
        _, perms = designs.pg23()
    elif grp == 'singer':
        # Singer cycle: multiplication by a primitive element of GF(27) acting on PG(2,3); realised by the
        # companion matrix of x^3 - x - 1 (irreducible over GF(3)) and the Frobenius-type map diag embedding
        C = [[0, 0, 1], [1, 0, 1], [0, 1, 0]]
        _, perms, _ = designs.pg_group(3, 3, [C])
    masks = [sum(1 << i for i in L) for L in lines]
elif name == 'ag24':
    mul = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
    P = [(a, b) for a in range(4) for b in range(4)]
    m = 16
    classes = sys.argv[7].split(',') if len(sys.argv) > 7 else ['inf', '0', '1']
    masks = []
    for sl in classes:
        for c in range(4):
            if sl == 'inf':
                L = [P.index((c, y)) for y in range(4)]
            else:
                s = int(sl)
                L = [P.index((x, mul[s][x] ^ c)) for x in range(4)]
            masks.append(sum(1 << i for i in L))
    # group: translations of GF(4)^2 plus the scalar multiplications (these fix every parallel class)
    idx = {p: i for i, p in enumerate(P)}
    perms = []
    for t in [(1, 0), (0, 1), (2, 0), (0, 2)]:
        perms.append(tuple(idx[(p[0] ^ t[0], p[1] ^ t[1])] for p in P))
    perms.append(tuple(idx[(mul[2][p[0]], mul[2][p[1]])] for p in P))
    # Frobenius (squaring) maps classes 0,1 to themselves and swaps slopes 2,3
    frob = [0, 1, 3, 2]
    if set(classes) <= {'inf', '0', '1'}:
        perms.append(tuple(idx[(frob[p[0]], frob[p[1]])] for p in P))
N = 1 << m
order = len(group_closure([(p, 1) for p in perms], m))
t = time.time()
M = Model2(m, perms)
print(f"{name} ({grp}): m={m} |G|={order} orbits={M.no} build {time.time()-t:.1f}s", flush=True)
x = np.arange(N)
hit = np.zeros(N, dtype=bool)
for mk in masks:
    hit |= (x & mk) == mk
prop = np.where(hit, -1, 1).astype(np.int64)
print(f"  Pr[contains a line] = {int(hit.sum())}/{N}", flush=True)
vprop = np.zeros(M.no, dtype=np.int64)
vprop[M.rep] = prop
assert np.array_equal(M.c0(vprop), prop), "property not invariant under the group"
rng = np.random.default_rng(5)
bestall = (-1e9, None)
for r in range(restarts):
    v0 = balance_greedy(M, vprop, rng, hole_frac=1.0 if r % 2 == 0 else 0.6)
    t = time.time()
    b1, R1 = anneal_bal(M, v0, iters, T0, T1, rng)
    b1, R1 = anneal_bal(M, b1, iters // 4, 1e-9, 1e-10, rng)
    c = M.c0(b1)
    s = summarize(c, m)
    print(f"  restart {r}: R = {R1:.12f} (check {s['R']:.12f}) holes={s['holes']} ncomp={s['ncomp']} maxcomp={s['maxcomp']} "
          f"nvars={s['nvars']} I={s['I']:.5f} H={s['H']:.5f} t={time.time()-t:.0f}s", flush=True)
    if R1 > bestall[0]:
        bestall = (R1, b1.copy())
np.save(f"../logs/lines_best_{name}_{grp}.npy", M.c0(bestall[1]).astype(np.int8))
print("BEST", name, grp, bestall[0])
