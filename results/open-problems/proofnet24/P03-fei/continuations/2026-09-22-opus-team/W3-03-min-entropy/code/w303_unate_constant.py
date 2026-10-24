"""Explicit FMEI constant for unate functions.

Lemma (explicit KKL): every nonconstant Boolean f with u = I(f)/Var(f), delta = max_i Inf_i(f), satisfies
    ln(1/delta) <= coth(a/2) (ln u + (u-1) a)     for every a > 0.
For unate f: Hinf(f) = min(log2(1/(1-V)), 2 log2(1/delta)) exactly, hence Hinf(f) <= C_u I(f) with
    C_u = sup_{u >= 1} R(u),  R(u) = beta(u) / (u (1 - 2^-beta(u))),
    beta(u) = (2/ln 2) inf_{a>0} coth(a/2) (ln u + (u-1) a)   (any a gives an upper bound).

Part 1: numerical profile of R.  Part 2: rigorous upper bound on sup_u R(u) with mpmath interval
arithmetic: on each cell [u1,u2] of a grid a fixed a is used,
    R(u) <= b/(u1 (1-2^-b)),  b = (2/ln2) coth(a/2) (ln u2 + (u2-1) a),
(t -> t/(1-2^-t) is increasing), and a tail bound for u >= U.
"""
import sys, json
import numpy as np
import mpmath as mp
from mpmath import iv
from scipy.optimize import minimize_scalar
import psutil
_p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])

LN2 = np.log(2.0)


def Bnum(u):
    if u <= 1.0:
        return 0.0
    g = lambda a: (1 / np.tanh(a / 2)) * (np.log(u) + (u - 1) * a)
    r = minimize_scalar(g, bounds=(1e-6, 20.0), method="bounded", options=dict(xatol=1e-12))
    return float(r.fun), float(r.x)


def R(u):
    if u <= 1.0:
        return 1 / LN2, None
    B, a = Bnum(u)
    beta = 2 / LN2 * B
    return beta / (u * (1 - 2.0 ** (-beta))), a


prof = []
us = np.concatenate([1 + np.logspace(-6, 0, 40), np.logspace(np.log10(2.01), 7, 200)])
best = (0, None, None)
for u in us:
    r, a = R(u)
    prof.append([float(u), float(r), a])
    if r > best[0]:
        best = (r, float(u), a)
print(json.dumps(dict(sup_numerical=best[0], at_u=best[1], a_opt=best[2],
                      R_at=[[p[0], p[1]] for p in prof[::20]], limit_large_u=4 / LN2)), flush=True)

# ---------- rigorous bound ----------
iv.dps = 30
two_over_ln2 = iv.mpf(2) / iv.log(iv.mpf(2))


def cell_bound(u1, u2, a):
    a = iv.mpf(a)
    ea = iv.exp(a)
    coth = (ea + 1) / (ea - 1)
    b = two_over_ln2 * coth * (iv.log(iv.mpf(u2)) + (iv.mpf(u2) - 1) * a)
    return b / (iv.mpf(u1) * (1 - iv.power(2, -b)))


# grid in u from 1 to U: geometric in (u-1) near 1, then geometric in u
cells = []
edges = [1.0 + 1e-9 * (1.25 ** k) for k in range(0, 200) if 1e-9 * (1.25 ** k) < 1.0] + [2.0]
e = 2.0
while e < 1e8:
    e *= 1.02
    edges.append(e)
U = edges[-1]
worst = mp.mpf(0)
wcell = None
# first cell [1, 1+1e-9]: R(u) <= b/(1*(1-2^-b)) with b tiny -> about 1/ln 2 + small; bound directly
first = cell_bound(1.0, edges[0], 1.7)
worst = first.b
for (u1, u2) in zip(edges[:-1], edges[1:]):
    _, a = Bnum(0.5 * (u1 + u2))
    cb = cell_bound(u1, u2, a)
    if cb.b > worst:
        worst = cb.b
        wcell = (u1, u2, a)
# tail u >= U: beta(u)/u <= (2/ln2) coth(a/2) (ln U / U + a) for u >= U >= e (ln u / u decreasing),
# and 1/(1-2^-beta(u)) <= 1/(1-2^-beta(U)) since beta is increasing in u.
a_t = iv.mpf(1e-3)
coth_t = (iv.exp(a_t) + 1) / (iv.exp(a_t) - 1)
bU = two_over_ln2 * coth_t * (iv.log(iv.mpf(U)) + (iv.mpf(U) - 1) * a_t)
tail = two_over_ln2 * coth_t * (iv.log(iv.mpf(U)) / iv.mpf(U) + a_t) / (1 - iv.power(2, -bU))
print(json.dumps(dict(rigorous_sup_upper=str(max(worst, tail.b)), grid_worst=str(worst), worst_cell=wcell,
                      tail_bound=str(tail.b), U=U, cells=len(edges))), flush=True)
