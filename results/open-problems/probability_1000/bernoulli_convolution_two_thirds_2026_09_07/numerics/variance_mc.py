# -*- coding: utf-8 -*-
"""Monte Carlo of the referee's variance quantity for the two-thirds Bernoulli measure.

mu_n = law of U = frac(2^n Y), Y = (1/3) sum_k B_k (2/3)^k.   2U = H + Z, H in {0,1}, Z in [0,1).
u_n(Z) = E[(-1)^H | Z],  V_n = (-1)^{floor(3Z)} u_n(Z),  W = frac(3Z).
Quantities per n:  j_n = log2 - H(H|Z)  (binned, Miller-Madow corrected),  D_n = j_n - j_{n+1},
                   E_W[Var(V_n | W)]  (binned over W, noise-bias corrected).
Referee's inequality to check:  D_n >= (1/2) E[Var(V_n|W)].
Target to probe:                E[Var] >= K j_n^{1+theta}  ->  slope of log E[Var] against log j_n.
"""
import numpy as np, math, sys, json, time
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 12
BW = int(sys.argv[3]) if len(sys.argv) > 3 else 512          # W bins; Z bins = 3*BW
DIG = 64
rng = np.random.default_rng(20260907)
lam = 2.0/3.0
t0 = time.time()
Y = np.empty(N)
CH = 1_000_000
for s in range(0, N, CH):
    e = min(N, s+CH)
    bits = rng.integers(0, 2, size=(e-s, DIG), dtype=np.int8)
    y = np.zeros(e-s)
    for k in range(DIG-1, -1, -1):
        y = bits[:, k] + lam*y
    Y[s:e] = y/3.0
print(f"N={N} samples, {DIG} digits, {time.time()-t0:.1f}s; Y range [{Y.min():.4f},{Y.max():.4f}]")

def hb(p):
    p = np.clip(p, 1e-300, 1-1e-300)
    return -(p*np.log(p) + (1-p)*np.log(1-p))

BZ = 3*BW
rows = []
for n in range(0, NMAX+2):
    U = np.mod(Y*(2.0**n), 1.0)
    twoU = 2.0*U
    H = np.floor(twoU).astype(np.int64)          # 0/1
    Z = twoU - H
    z = np.minimum((Z*BZ).astype(np.int64), BZ-1)
    n0 = np.bincount(z[H == 0], minlength=BZ).astype(float)
    n1 = np.bincount(z[H == 1], minlength=BZ).astype(float)
    tot = n0 + n1
    mask = tot > 0
    p1 = np.where(mask, n1/np.maximum(tot, 1), 0.5)
    HcondZ = np.sum(tot[mask]/N * hb(p1[mask]))
    occupied = int(mask.sum())
    HcondZ_mm = HcondZ + (occupied)/(2.0*N)          # Miller-Madow: one free parameter per bin
    j_raw = math.log(2) - HcondZ
    j_mm = math.log(2) - HcondZ_mm
    # variance over the three preimages of W
    u = np.where(mask, (n0 - n1)/np.maximum(tot, 1), 0.0)     # u_hat per Z-bin
    i_idx = np.arange(BZ)//BW; w_idx = np.arange(BZ) % BW
    sign = np.where(i_idx % 2 == 0, 1.0, -1.0)
    V = sign*u
    nw = np.zeros((3, BW)); Vw = np.zeros((3, BW)); s2 = np.zeros((3, BW))
    for i in range(3):
        sel = i_idx == i
        nw[i, w_idx[sel]] = tot[sel]; Vw[i, w_idx[sel]] = V[sel]
        s2[i, w_idx[sel]] = (1 - u[sel]**2)/np.maximum(tot[sel], 1)   # sampling variance of u_hat
    massw = nw.sum(axis=0); p = nw/np.maximum(massw, 1)
    var_raw = (p*Vw**2).sum(axis=0) - ((p*Vw).sum(axis=0))**2
    bias = (p*(1-p)*s2).sum(axis=0)
    EVar_raw = float(np.sum(massw/N * var_raw)); EVar = float(np.sum(massw/N * (var_raw - bias)))
    rows.append(dict(n=n, j_raw=j_raw, j=j_mm, EVar_raw=EVar_raw, EVar=EVar, occupied=occupied,
                     min_count=float(tot[mask].min())))
    print(f"n={n:2d}  j_raw={j_raw:.6f}  j_mm={j_mm:.6f}  E[Var] raw={EVar_raw:.3e} corrected={EVar:.3e}  bins={occupied} min_count={tot[mask].min():.0f}", flush=True)

print("\n n    j_n       D_n=j_n-j_{n+1}   0.5*E[Var]   D_n - 0.5E[Var]   E[Var]/j_n   E[Var]/j_n^2")
for k in range(0, NMAX+1):
    j, jn = rows[k]['j'], rows[k+1]['j']; D = j - jn; ev = rows[k]['EVar']
    print(f"{k:2d}  {j:.6f}   {D:+.6f}       {0.5*ev:.3e}    {D-0.5*ev:+.3e}      {ev/j:.4f}      {ev/j**2:.3f}")
# power fit E[Var] ~ K j^(1+theta) on n = 1..NMAX (drop n=0)
good = [r for r in rows[1:NMAX+1] if r['j'] > 0 and r['EVar'] > 0]
xs = np.array([math.log(r['j']) for r in good]); ys = np.array([math.log(r['EVar']) for r in good])
A = np.vstack([xs, np.ones_like(xs)]).T
slope, icpt = np.linalg.lstsq(A, ys, rcond=None)[0]
print(f"\nleast-squares fit log E[Var] = ({slope:.3f}) log j + ({icpt:.3f})  ->  1+theta = {slope:.3f}, theta = {slope-1:.3f}, K = e^icpt = {math.exp(icpt):.3f}")
# also the exponent of j_n itself against n
good2 = [r for r in rows[2:NMAX+1] if r['j'] > 0]
xn = np.array([math.log(r['n']) for r in good2]); yj = np.array([math.log(r['j']) for r in good2])
sl2 = np.linalg.lstsq(np.vstack([xn, np.ones_like(xn)]).T, yj, rcond=None)[0][0]
print(f"fit log j_n = ({sl2:.3f}) log n + ...   (paper: exponent >= -0.52; referee sharpened: -0.538)")
json.dump(dict(N=N, DIG=DIG, BW=BW, rows=rows, fit=dict(slope=slope, intercept=icpt, j_exponent=sl2)),
          open(f"~/bc23_lean/numerics/variance_mc_N{N}_BW{BW}.json", "w"), indent=1)
print("wrote variance_mc.json", f"{time.time()-t0:.0f}s")
