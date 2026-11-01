import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import numpy as np, time, itertools, json, sys
from orbits import group_closure, orbit_structure
from orbsearch import OrbitModel, run_enum
G = np.load('../logs/numaro_gens.npy')
elems = [(tuple(int(t) for t in r[:9]), int(r[9])) for r in G]
m = 9
def compose(a, b):  # first a then b
    return (tuple(b[0][a[0][i]] for i in range(m)), a[1] * b[1])
def inverse(a):
    inv = [0] * m
    for i in range(m): inv[a[0][i]] = i
    return (tuple(inv), a[1])
subs = {}
for a in elems:
    H = frozenset(group_closure([a], m)); subs[H] = [a]
for a, b in itertools.combinations(elems, 2):
    H = frozenset(group_closure([a, b], m))
    if H not in subs: subs[H] = [a, b]
print('distinct subgroups found:', len(subs))
# conjugacy classes under G144
seen = set(); classes = []
for H, gens in sorted(subs.items(), key=lambda kv: -len(kv[0])):
    if H in seen: continue
    cl = set()
    for g in elems:
        gi = inverse(g)
        cl.add(frozenset(compose(compose(gi, h), g) for h in H))
    seen |= cl
    classes.append((H, gens))
print('conjugacy classes:', len(classes))
results = []
limit = int(sys.argv[1]) if len(sys.argv) > 1 else 15
for H, gens in classes:
    t = time.time()
    M = OrbitModel(m, list(H))
    nfree = int((~M.forced).sum())
    dual = any(s < 0 for p, s in H)
    rec = dict(order=len(H), dual=dual, orbits=M.no, free=nfree)
    if nfree <= limit:
        R, V = run_enum(M, topk=3)
        rec['best'] = float(R[0]); rec['v'] = V[0].tolist(); rec['time'] = round(time.time() - t, 1)
        # best without holes? report hole count
        c0 = M.c0(V[0]); rec['holes'] = int((c0 == 0).sum())
    results.append(rec)
    print(rec, flush=True)
json.dump(results, open('../logs/subgroups_m9.json', 'w', encoding='utf-8'), indent=1)
