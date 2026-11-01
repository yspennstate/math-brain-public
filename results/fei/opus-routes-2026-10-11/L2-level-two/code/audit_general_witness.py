"""Second path for data/general_witness.json and the checks behind NOTES section 5c (s07, 12 Oct 2026).

(1) B and I recomputed by an explicit Sylvester-Hadamard product (no fast transform) on eight of the bench functions.
(2) Corollary R2: on read-once AND/OR/parity formulas the single statistic tau_i (height of the lowest ancestor of i whose
    subtree meets S - i) is an exact witness; with majority gates it is not.
(3) Exact co-occurrence ties on a random table; co-occurrence against tree distance on AND/OR trees; MAJ3 of AND_w, w = 3..6.
Usage: python audit_general_witness.py   (run from the L2-level-two folder; prints to stdout)
"""
import sys, json, math, importlib.util
import numpy as np
spec = importlib.util.spec_from_file_location("gw", "code/general_witness.py"); gw = importlib.util.module_from_spec(spec); spec.loader.exec_module(gw)
rows = {r["name"]: r for r in json.load(open("data/general_witness.json", encoding="utf-8"))["rows"]}

def phi(a, b):
    a = np.asarray(a, float); b = np.asarray(b, float); out = np.zeros(np.broadcast(a, b).shape)
    m = (a > 0) & (b > 0); x, y = a[m], b[m]; s = x + y
    out[m] = -(x * np.log2(x / s) + y * np.log2(y / s)); return out

def hadamard_p(T):
    n = len(T).bit_length() - 1
    Hm = np.array([[1.0]])
    for _ in range(n):
        Hm = np.block([[Hm, Hm], [Hm, -Hm]])      # Sylvester; entry (U, x) = (-1)^{|U & x|}
    return (Hm @ T.astype(float) / len(T)) ** 2, n

def B_I(p, n):
    B = I = 0.0
    for i in range(n):
        U = np.array([u for u in range(1 << n) if not (u >> i) & 1])
        a, b = p[U], p[U | (1 << i)]
        I += b.sum(); B += phi(a, b).sum()
    return B, I

for name, mk in (("tribes 3x4", lambda: gw.tribes(3, 4)), ("andor d3", lambda: gw.andor(3)), ("address k3", lambda: gw.address(3)),
                 ("OR3 of MAJ3", lambda: gw.or_of_maj(3, 3)), ("MAJ3 of AND4", lambda: gw.maj3_of_and(4)),
                 ("dnf n12 t6 w3 s1", lambda: gw.random_dnf(12, 6, 3, 1)), ("random n10 s1", lambda: gw.random_table(10, 1)),
                 ("majority 9", lambda: gw.majority(9))):
    p, n = hadamard_p(mk())
    B, I = B_I(p, n)
    print(f"{name:18s} B/I {B/I:.10f}  json {rows[name]['B_over_I']:.10f}  I {I:.10f} json {rows[name]['I']:.10f}")

def tau_cost(T, block_key, H):
    p = gw.walsh(T) ** 2; n = len(T).bit_length() - 1
    idx = np.arange(1 << n, dtype=np.int64); tot = Bt = I = 0.0
    for i in range(n):
        lo = idx[(idx & (1 << i)) == 0]; pU, pUi = p[lo], p[lo | (1 << i)]
        I += pUi.sum(); Bt += phi(pU, pUi).sum()
        tau = np.full(len(lo), H + 1, dtype=np.int64)
        for h in range(H, 0, -1):
            m = np.zeros(len(lo), dtype=bool)
            for j in range(n):
                if j != i and block_key(j, h) == block_key(i, h):
                    m |= ((lo >> j) & 1) == 1
            tau[m] = h
        tot += gw.cond_entropy(tau, pU, pUi)
    return Bt / I, tot / I

for name, T, key, H in (("andor d3", gw.andor(3), lambda j, h: j >> h, 3), ("andor d4", gw.andor(4), lambda j, h: j >> h, 4),
                        ("AND2-OR3-AND2", gw.and2_or3_and2(), lambda j, h: (j // 2, j // 6, 0)[h - 1], 3),
                        ("OR3 of MAJ3", gw.or_of_maj(3, 3), lambda j, h: (j // 3, 0)[h - 1], 2),
                        ("MAJ3 of AND4", gw.maj3_of_and(4), lambda j, h: (j // 4, 0)[h - 1], 2),
                        ("OR2-XOR3-AND2", gw.table(12, lambda b: np.any(np.logical_xor.reduce(np.all(b.reshape(-1, 2, 3, 2), axis=3), axis=2), axis=1)),
                         lambda j, h: (j // 2, j // 6, 0)[h - 1], 3),
                        ("XOR2-AND3-OR2", gw.table(12, lambda b: np.logical_xor.reduce(np.all(np.any(b.reshape(-1, 2, 3, 2), axis=3), axis=2), axis=1)),
                         lambda j, h: (j // 2, j // 6, 0)[h - 1], 3)):
    b, t = tau_cost(T, key, H)
    print(f"tau witness {name:14s} B/I {b:.12f}  H(S_i|tau)/I {t:.12f}  excess {t-b:.2e}")

ro = json.load(open("data/readonce_witness.json", encoding="utf-8"))["families"]["AND/OR fan-in 2, AND on top"]
print("readonce JSON row type:", type(ro), (ro[:1] if isinstance(ro, list) else list(ro)[:5]))

T = gw.random_table(10, 1); p = gw.walsh(T) ** 2; n = 10; idx = np.arange(1 << n)
cnts = []
for i in range(n):
    lo = idx[(idx & (1 << i)) == 0]; pUi = p[lo | (1 << i)]
    c = sorted(round(float(pUi[((lo >> j) & 1) == 1].sum()) * 2**18) for j in range(n) if j != i)
    cnts.append(len(set(c)))
print("random n10 s1 distinct co-occurrence values per i:", cnts)
# (1) co-occurrence of leaf 0 with leaves at tree distance h, AND/OR fan-2 trees, AND on top
for d in (3, 4):
    T = gw.andor(d); p = gw.walsh(T) ** 2; n = 1 << d; idx = np.arange(1 << n)
    lo = idx[(idx & 1) == 0]; pUi = p[lo | 1]
    byh = {}
    for j in range(1, n):
        h = (j ^ 0).bit_length()          # height of the lowest common ancestor of leaves 0 and j
        byh.setdefault(h, set()).add(round(float(pUi[((lo >> j) & 1) == 1].sum()), 12))
    print(f"andor d{d}: c_0j by LCA height", {h: sorted(v) for h, v in sorted(byh.items())})
# (2) MAJ3 of AND_w: B, eq+lev, eq-count, tau as w grows
for w in (3, 4, 5, 6):
    R = gw.analyse(gw.maj3_of_and(w), f"MAJ3 of AND{w}")
    print(f"MAJ3 of AND{w}: n {R['n']} H/I {R['H_over_I']:.3f} B/I {R['B_over_I']:.4f} eq+lev {R['eq+lev_over_I']:.4f} "
          f"ecnt {R['eq-count_over_I']:.4f} level {R['level_over_I']:.4f} first {R['first_over_I']:.4f}")
# (4) X009, the selector bit t alone: B_t / eps_t against log2(1/eps_t) + 1/ln 2 (SEL referee, RIG sections 2-3)
for m in (4, 6, 8, 10, 12, 14):
    F = gw.x009(m); n = m + 1; p = gw.walsh(F) ** 2; idx = np.arange(1 << n, dtype=np.int64); t = 1 << m
    lo = idx[(idx & t) == 0]; a, b = p[lo], p[lo | t]
    eps = float(b.sum()); Bt = float(phi(a, b).sum())
    print(f"X009 m{m:2d}: eps_t {eps:.3e}  B_t/eps_t {Bt/eps:.6f}  log2(1/eps_t) + 1/ln2 {math.log2(1/eps) + 1/math.log(2):.6f}  "
          f"share of B {Bt/sum(float(phi(p[idx[(idx & (1 << i)) == 0]], p[idx[(idx & (1 << i)) == 0] | (1 << i)]).sum()) for i in range(n)):.2e}")
