# Float evidence: (1) identity J-M = h2(p) - sum_T r_T^2 F(t_T) on random Boolean child pairs with biased bases;
# (2) AND p=1/8,q=1/4 debt vs tau*(1/8) and Delta/2; (3) two-bit block: min over real unit w of
# H(w^2)+H((U1xU2 w)^2) vs U(p1)+U(p2) by multistart local search (evidence for additivity).
import math, random, json, sys, itertools
import numpy as np
from scipy.optimize import minimize
rng = random.Random(20261011)
def h2(x): return 0.0 if x <= 0 or x >= 1 else -x*math.log2(x) - (1-x)*math.log2(1-x)
def H(v):
    v = np.asarray(v, float); v = v[v > 1e-300]; return float(-(v*np.log2(v)).sum())
def U(p, N=20000):
    b = math.asin(math.sqrt(p)); best = 1e9
    for k in range(N+1):
        t = b/2 + (math.pi/4)*k/N; best = min(best, h2(math.sin(t)**2) + h2(math.sin(t-b)**2))
    return best
def biased_coeffs(vals, qs):   # vals: function values on {0,1}^n (index bit i = x_i), product biases qs
    n = len(qs); out = {}
    for S in range(2**n):
        c = 0.0
        for x in range(2**n):
            w = 1.0; chi = 1.0
            for i in range(n):
                xi = (x >> i) & 1; w *= qs[i] if xi else 1-qs[i]
                if (S >> i) & 1: chi *= (xi - qs[i]) / math.sqrt(qs[i]*(1-qs[i]))
            c += w * chi * vals[x]
        out[S] = c
    return out
res = {"identity": [], "and": {}, "two_bit": []}
maxerr = 0.0
for trial in range(300):
    n = rng.choice([1, 2, 3]); qs = [rng.choice([0.1, 0.25, 0.4, 0.5, 0.7]) for _ in range(n)]
    p = rng.choice([0.05, 1/8, 0.3, 0.5, 0.8])
    g = [rng.choice([-1, 1]) for _ in range(2**n)]; hh = [rng.choice([-1, 1]) for _ in range(2**n)]
    G = biased_coeffs(g, qs); Hc = biased_coeffs(hh, qs)
    a = [((1-p)*G[T] + p*Hc[T])**2 for T in G]; bb = [p*(1-p)*(Hc[T]-G[T])**2 for T in G]
    q = [a[i]+bb[i] for i in range(len(a))]
    M = sum(q[i]*h2(bb[i]/q[i]) for i in range(len(q)) if q[i] > 1e-15)
    J = H(q) - (1-p)*H([G[T]**2 for T in G]) - p*H([Hc[T]**2 for T in G])
    beta = math.asin(math.sqrt(p)); s = 0.0
    for T in G:
        x, y = math.sqrt(1-p)*G[T], math.sqrt(p)*Hc[T]; r2 = x*x + y*y
        if r2 < 1e-15: continue
        t = math.atan2(y, x); s += r2*(h2(math.sin(t)**2) + h2(math.sin(t-beta)**2))
    err = abs((J - M) - (h2(p) - s)); maxerr = max(maxerr, err)
    pb = min(p, 1-p); Delta = pb*math.log2((1-pb)/pb) if pb < 0.5 else 0.0
    res["identity"].append([n, p, round(J-M, 12), round(Delta/2, 12)])
res["identity_max_abs_error"] = maxerr
res["identity_max_debt_over_halfDelta"] = max((d/hd if hd > 0 else (0 if d <= 1e-12 else float('inf'))) for _, _, d, hd in res["identity"])
# AND p=1/8 q=1/4
p, q = 1/8, 1/4; u = 4*q*(1-q)
A = [(1-2*p*q)**2, 4*p*(1-p)*q*q, 4*p*p*q*(1-q), 4*p*(1-p)*q*(1-q)]
Mx = H(A) - h2(p*u); Jx = h2(p*u) - p*h2(u)
res["and"] = {"p": p, "q": q, "J_minus_M": Jx - Mx, "tau_star": h2(p) - U(p), "Delta_half": p*math.log2((1-p)/p)/2, "Delta": p*math.log2((1-p)/p)}
# two-bit additivity evidence
def rot(p):
    b = math.asin(math.sqrt(p)); return np.array([[math.cos(b), math.sin(b)], [-math.sin(b), math.cos(b)]])
nprng = np.random.default_rng(7)
for p1, p2 in [(0.05, 0.05), (1/8, 1/4), (0.3, 0.1), (0.25, 0.45), (0.4, 0.4), (0.5, 0.2)]:
    Uk = np.kron(rot(p1), rot(p2))
    def obj(v):
        w = v/np.linalg.norm(v); return H(w**2) + H((Uk@w)**2)
    best = 1e9
    for s in range(400):
        v0 = nprng.normal(size=4); r = minimize(obj, v0, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-12, "maxiter": 4000})
        best = min(best, r.fun)
    add = U(p1) + U(p2)
    Dh = sum(pp*math.log2((1-pp)/pp) for pp in (p1, p2) if pp < 0.5)/2
    res["two_bit"].append({"p1": p1, "p2": p2, "min_found": best, "U1_plus_U2": add, "gap_min_minus_sum": best - add,
                           "debt_bound_HX_minus_min": h2(p1)+h2(p2)-best, "Delta_A_half": Dh})
json.dump(res, open(sys.argv[1], "w"), indent=1)
print("identity max abs error", maxerr, " max debt/(Delta/2) over random pairs", res["identity_max_debt_over_halfDelta"])
print("AND", res["and"])
for r in res["two_bit"]: print(r)
