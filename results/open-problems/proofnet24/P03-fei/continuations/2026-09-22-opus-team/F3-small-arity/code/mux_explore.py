"""Selector-expansion remainders of the prime three-input gates.

For a gate G and an input i with bias r, Shannon expansion G = x_i ? G_1 : G_0 gives the exact identity
    D_G = (1-r) D_{G_0} + r D_{G_1} + R_i,
    R_i = d (Gamma(r) + h(V_r)) + (1-r) Gamma(p_0) + r Gamma(p_1) - Gamma(p_out) - JS_r(mu_0, mu_1) - H(S_i | S_{-i}),
with d = Pr[G_0 != G_1], p_0, p_1 the output measures of G_0, G_1 and mu_0, mu_1 their biased spectral laws.  The same
cocycle holds for W with remainder r(1-r) d (1-d) ... (computed numerically here as W_G - (1-r) W_0 - r W_1).
For MUX(s,a,b) expanded on a: G_0 = AND(not s, b), G_1 = OR(s, b).  This script evaluates R_i on a logit grid that reaches
the faces, for every prime class and every expansion input, and reports min R_i and min R_i/(d r(1-r)).
usage: mux_explore.py <npz> <c_margin>"""
import sys, os, json, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fgate as F
F.lowprio()

npz, cm = sys.argv[1], float(sys.argv[2])
pot = F.Pot(npz, cm)
PRIME = {22: "one-hot", 23: "MAJ3 (neg.)", 24: "EQ3", 25: "Q3 {000,110,001}", 27: "MUX"}
k = 3; n = 8
u = np.concatenate([np.linspace(-24, -6, 10), np.linspace(-5.5, 5.5, 45), np.linspace(6, 24, 10)])
U = np.array(np.meshgrid(u, u, u, indexing="ij")).reshape(3, -1).T
P = 1 / (1 + 2.0 ** (-U))


def restrict(vals, i, b):
    """table of the 2-input gate G with input i fixed to b (b=1: true), inputs in order of the remaining indices"""
    o = [j for j in range(k) if j != i]
    t = np.empty(4)
    for y in range(4):
        x = (b << i)
        for l, j in enumerate(o):
            x |= ((y >> l) & 1) << j
        t[y] = vals[x]
    return t, o


res = {}
for tt, name in PRIME.items():
    vals = F.pm_from_int(tt, k)
    DG, WG, po, It = F.stats(vals, P, pot)
    for i in range(k):
        g0, o = restrict(vals, i, 0); g1, _ = restrict(vals, i, 1)
        D0, W0, p0, _ = F.stats(g0, P[:, o], pot)
        D1, W1, p1, _ = F.stats(g1, P[:, o], pot)
        r = P[:, i]
        R = DG - (1 - r) * D0 - r * D1
        RW = WG - (1 - r) * W0 - r * W1
        # d = Pr[G_0 != G_1] under the other two biases
        xo = ((np.arange(4)[:, None] >> np.arange(2)) & 1)
        pr = np.prod(np.where(xo[None, :, :] == 1, P[:, o][:, None, :], 1 - P[:, o][:, None, :]), 2)
        d = (pr * (g0 != g1)[None, :]).sum(1)
        scale = d * r * (1 - r)
        ok = scale > 1e-300
        j = int(np.argmin(R)); jn = int(np.argmin(np.where(ok, R / np.where(ok, scale, 1), 1e9)))
        res[(tt, i)] = dict(minR=float(R[j]), at=[float(x) for x in P[j]], minRn=float(R[jn] / scale[jn]), atn=[float(x) for x in P[jn]],
                            RW_min=float(RW.min()))
        print("%-18s expand on input %d: min R = %+.4e at p=%s ; min R/(d r(1-r)) = %+.4e at p=%s ; min W-remainder %.2e"
              % (name, i, R[j], ["%.3g" % x for x in P[j]], R[jn] / scale[jn], ["%.3g" % x for x in P[jn]], RW.min()), flush=True)
    j = int(np.argmin(DG))
    print("%-18s D_G min on grid %+.4e at p=%s; W>1e-6: min D/W %+.4e" % (name, DG[j], ["%.3g" % x for x in P[j]],
          float(np.min(np.where(WG > 1e-6, DG / np.maximum(WG, 1e-300), 1e9)))))
