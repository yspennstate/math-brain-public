"""Read-once composition engine (referee's own implementation), exact recursion with float logs.

A node computes the summary of its Boolean function F:
    mu = E F,  and, if F is nonconstant, the normalized nonempty spectral law q with Hq, Uq, Iq,
and, for every variable type v below it, the summaries of the two physical restrictions F|_{x_v = +1}, F|_{x_v = -1}
(with multiplicities, so identical children under a symmetric gate are not enumerated).

Composition (outer gate g on k inputs, inner functions independent with means mu_j):
    law of the active set J is P(J) = ghat_mu(J)^2 (mu-biased transform; inputs with mu_j = +-1 never enter J),
    H(F) = H(P) + sum_j P(j in J) Hq_j,  U(F) = U(P) + sum_j P(j in J) Uq_j,  I(F) = sum_j P(j in J) Iq_j.
At the root:  Delta_v U = U(F) - (U(F_v+) + U(F_v-))/2,  Inf_v = I(F) - (I(F_v+) + I(F_v-))/2,  G = sum_v Delta_v U.
"""
from __future__ import annotations
import math
import numpy as np
from rlib import Spec, restrict_tables

LOG2 = math.log(2)


def _xlog2x(p):
    return 0.0 if p <= 0 else p * math.log2(p)


class Summ:
    __slots__ = ('mu', 'Hq', 'Uq', 'Iq')

    def __init__(self, mu, Hq=0.0, Uq=0.0, Iq=0.0):
        self.mu = mu; self.Hq = Hq; self.Uq = Uq; self.Iq = Iq

    def const(self):
        return abs(self.mu) >= 1 - 1e-15

    def full(self):
        """unnormalized (H, U, I, Var) of the function."""
        p0 = self.mu * self.mu
        if self.const():
            return 0.0, 0.0, 0.0, 0.0
        hb = -_xlog2x(p0) - _xlog2x(1 - p0)
        H = hb + (1 - p0) * self.Hq
        U = (-_xlog2x(p0)) + (1 - p0) * self.Uq      # p0 log2(1/p0) + (1-p0) Uq
        I = (1 - p0) * self.Iq
        return H, U, I, 1 - p0


def summ_from_table(t):
    t = np.asarray(t, dtype=np.int64)
    mu = float(t.mean())
    if abs(mu) == 1.0:
        return Summ(mu)
    sp = Spec.from_tables(t)
    p = sp.p[0].copy(); p0 = p[0]
    q = p.copy(); q[0] = 0.0; q /= (1 - p0)
    sq = Spec(q)
    return Summ(mu, float(sq.H()[0]), float(sq.U()[0]), float(sq.I()[0]))


def gate_law(g, k, mus):
    """P(J) for J subset of [k] (bitmask) under the mu-biased transform of g (table, bit j = 1 iff y_j = -1)."""
    sig = [math.sqrt(max(0.0, 1 - m * m)) for m in mus]
    live = [j for j in range(k) if sig[j] > 1e-15]
    # probabilities of each input pattern y
    py = np.ones(1 << k)
    for y in range(1 << k):
        for j in range(k):
            yj = -1 if (y >> j) & 1 else 1
            py[y] *= (1 + mus[j] * yj) / 2
    P = {}
    for J in range(1 << k):
        if any(((J >> j) & 1) and sig[j] <= 1e-15 for j in range(k)):
            continue
        s = 0.0
        for y in range(1 << k):
            if py[y] == 0:
                continue
            ph = 1.0
            for j in range(k):
                if (J >> j) & 1:
                    yj = -1 if (y >> j) & 1 else 1
                    ph *= (yj - mus[j]) / sig[j]
            s += py[y] * g[y] * ph
        P[J] = s * s
    return P


def law_HU(P, k):
    H = -sum(_xlog2x(v) for v in P.values())
    U = 0.0
    for J, v in P.items():
        if v <= 0:
            continue
        pi = sum(w for K, w in P.items() if (K & J) == J)
        U += v * math.log2(pi / v)
    marg = [sum(v for J, v in P.items() if (J >> j) & 1) for j in range(k)]
    return H, U, marg


def compose_summ(g, k, kids):
    mus = [c.mu for c in kids]
    P = gate_law(g, k, mus)
    Hg, Ug, marg = law_HU(P, k)
    H = Hg + sum(marg[j] * kids[j].Hq for j in range(k) if not kids[j].const())
    U = Ug + sum(marg[j] * kids[j].Uq for j in range(k) if not kids[j].const())
    I = sum(marg[j] * kids[j].Iq for j in range(k) if not kids[j].const())
    p0 = P.get(0, 0.0)
    # mean of F = E_mu g  (its sign matters for later compositions)
    py_mean = 0.0
    for y in range(1 << k):
        w = 1.0
        for j in range(k):
            yj = -1 if (y >> j) & 1 else 1
            w *= (1 + mus[j] * yj) / 2
        py_mean += w * g[y]
    mu = py_mean
    if abs(abs(mu) - 1) < 1e-15:
        return Summ(math.copysign(1.0, mu))
    hb = -_xlog2x(p0) - _xlog2x(1 - p0)
    Hq = (H - hb) / (1 - p0)
    Uq = (U + _xlog2x(p0)) / (1 - p0)
    Iq = I / (1 - p0)
    return Summ(mu, Hq, Uq, Iq)


class Node:
    """kind: 'var' | 'table' | 'gate'."""

    def __init__(self, kind, table=None, gate=None, kids=None, symmetric=False):
        self.kind = kind; self.table = table; self.gate = gate; self.kids = kids or []; self.symmetric = symmetric
        self._s = None; self._r = None

    def summ(self):
        if self._s is None:
            if self.kind == 'var':
                self._s = Summ(0.0, 0.0, 0.0, 1.0)
            elif self.kind == 'table':
                self._s = summ_from_table(self.table)
            else:
                self._s = compose_summ(self.gate, len(self.kids), [c.summ() for c in self.kids])
        return self._s

    def restr(self):
        """list of (multiplicity, Summ for x_v=+1, Summ for x_v=-1) over variable types below this node."""
        if self._r is None:
            if self.kind == 'var':
                self._r = [(1, Summ(1.0), Summ(-1.0))]
            elif self.kind == 'table':
                t = np.asarray(self.table, dtype=np.int64); m = t.size.bit_length() - 1
                self._r = [(1, summ_from_table(restrict_tables(t, i, 1)), summ_from_table(restrict_tables(t, i, -1))) for i in range(m)]
            else:
                k = len(self.kids); base = [c.summ() for c in self.kids]
                out = []
                same = self.symmetric and all(c is self.kids[0] for c in self.kids)
                rng = [0] if same else range(k)
                for j in rng:
                    for (mult, sp, sm) in self.kids[j].restr():
                        kp = list(base); kp[j] = sp
                        km = list(base); km[j] = sm
                        out.append((mult * (k if same else 1), compose_summ(self.gate, k, kp), compose_summ(self.gate, k, km)))
                self._r = out
        return self._r


def root_stats(node):
    H, U, I, Var = node.summ().full()
    G = 0.0; Isum = 0.0; GH = 0.0
    loc = []
    for (mult, sp, sm) in node.restr():
        Hp, Up, Ip, _ = sp.full(); Hm, Um, Im, _ = sm.full()
        inf = I - 0.5 * (Ip + Im)
        dU = U - 0.5 * (Up + Um); dH = H - 0.5 * (Hp + Hm)
        G += mult * dU; GH += mult * dH; Isum += mult * inf
        if inf > 1e-15:
            loc.append((dU / inf, dH / inf, mult))
    return dict(H=H, U=U, I=I, Var=Var, G=G, GH=GH, I_from_infl=Isum,
                H_over_I=H / I, U_over_I=U / I, G_over_I=G / I,
                thmG_ratio_full=H / (2 * (I - Var) + 2 * U - (-_xlog2x(1 - Var))),
                thmG_ratio_weak=H / (2 * (I - Var) + 2 * U),
                min_local_U=min(l[0] for l in loc), max_local_U=max(l[0] for l in loc),
                min_local_H=min(l[1] for l in loc))


def var():
    return Node('var')


def table(t):
    return Node('table', table=np.asarray(t, dtype=np.int64))


def gate(g, kids, symmetric=False):
    return Node('gate', gate=np.asarray(g, dtype=np.int64), kids=kids, symmetric=symmetric)


AND2 = [1, 1, 1, -1]          # -1 iff both inputs -1
OR2 = [1, -1, -1, -1]         # -1 iff some input -1
MAJ3 = [1 if bin(x).count('1') < 2 else -1 for x in range(8)]


def andk(k):
    return [-1 if x == (1 << k) - 1 else 1 for x in range(1 << k)]


def ork(k):
    return [1 if x == 0 else -1 for x in range(1 << k)]


def majk(k):
    return [1 if bin(x).count('1') <= k // 2 else -1 for x in range(1 << k)]
