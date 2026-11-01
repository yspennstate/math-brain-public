"""Queue-law (paper, C008) code lengths for selector trees with regular leaves.

Gates: h_i = kappa_i AND [g_i = 1] for every leaf with g_i not identically -1 (mutually exclusive).
Inner regular functions: kappa_i (path conjunction, ranked by depth: root = 1) and g_i (desirability order).
theta_s(j) = min(1, (s/r(j))^a), Z_s = e_s(theta_s on R_i), a = 6/5.
Single-root witness (root set {i}, B = A, c = 0) has probability
   2^{-Lambda} * rho_i * 1/(s(s+1)) * prod theta / Z_s * 1/2 ,  rho_i = lam*pi_i (paper) or free (owner code).
Bounds computed (all in bits):
   minW  : h(v) + v Lambda + sum_A p(A) min_i cost_i(A)          [the variational bound (W)]
   sumW  : h(v) + v Lambda + sum_A p(A) log(1/sum_i 2^{-cost_i(A)})  [same law, all single-root witnesses]
   owner : per-gate root odds rho_i = Omega_i / v with a canonical owner per set.
Floating point logarithms: EVIDENCE only.
"""
import math
from fractions import Fraction
import fei_core as fc
from rodt import *


def elem_sym(vals, smax):
    """e_0..e_smax of a list of floats."""
    e = [0.0] * (smax + 1)
    e[0] = 1.0
    for x in vals:
        for s in range(smax, 0, -1):
            e[s] += e[s - 1] * x
    return e


class GateData:
    def __init__(self, st, i, a=A_EXP):
        self.i = i
        path = st.paths[i]
        self.ranks = {}
        for pos, (v, _) in enumerate(path):
            self.ranks[v] = pos + 1
        bv, T = st.leaves[i]
        ok, sign, order = fc.is_unate_regular(T)
        assert ok, "leaf not regular"
        for pos, kloc in enumerate(order):
            self.ranks[bv[kloc]] = pos + 1
        self.R = 0
        for v in self.ranks:
            self.R |= 1 << v
        self.size = len(self.ranks)
        self.a = a
        self._Z = {}
        c = len(path)
        P = (1 + float(st.mu[i])) / 2
        self.p_cell = 2.0 ** (-c)
        self.P = P
        self.pi = min(self.p_cell * P, 0.5)

    def theta(self, s, v):
        return min(1.0, (s / self.ranks[v]) ** self.a)

    def Z(self, s):
        if s not in self._Z:
            vals = [self.theta(s, v) for v in self.ranks]
            self._Z[s] = elem_sym(vals, s)[s]
        return self._Z[s]

    def inner_cost(self, A):
        """-log2 of [1/(s(s+1)) * prod theta/Z_s * 1/2] for A subset of R."""
        s = fc.popcount(A)
        if s > self.size:
            return math.inf
        lp = -math.log2(s * (s + 1)) - 1.0 - math.log2(self.Z(s))
        x = A
        k = 0
        while x:
            if x & 1:
                lp += math.log2(self.theta(s, k))
            x >>= 1
            k += 1
        return -lp


def h2(v):
    v = float(v)
    if v <= 0 or v >= 1:
        return 0.0
    return -v * math.log2(v) - (1 - v) * math.log2(1 - v)


def code_lengths(st, lam=1.0, coef=None, owner_rule=None):
    if coef is None:
        coef = st.predicted_spectrum()
    masses = {S: c * c for S, c in coef.items()}
    H, I, v = H_I_from_masses(masses)
    gates = [GateData(st, i) for i in st.paths if not (st.mu[i] == -1)]
    Lam = sum(math.log1p(lam * g.pi) for g in gates) / math.log(2)
    vf = float(v)
    minW = h2(v) + vf * Lam
    sumW = h2(v) + vf * Lam
    per_set = {}
    for S, m in masses.items():
        if S == 0:
            continue
        costs = []
        for g in gates:
            if (S & ~g.R) == 0:
                costs.append((-math.log2(lam * g.pi) + g.inner_cost(S), g.i))
        assert costs, "no gate contains a support set"
        cmin = min(c for c, _ in costs)
        csum = -math.log2(sum(2.0 ** (-c) for c, _ in costs))
        minW += float(m) * cmin
        sumW += float(m) * csum
        per_set[S] = (cmin, csum, costs)
    return dict(H=H, I=float(I), v=vf, Lam=Lam, minW=minW, sumW=sumW, per_set=per_set,
                gates=gates, masses=masses)


def owner_code_length(st, res, owner):
    """Per-gate root odds rho_i = Omega_i / v for a given owner map S -> gate id."""
    masses = res['masses']
    v = res['v']
    gates = {g.i: g for g in res['gates']}
    Omega = {}
    for S, m in masses.items():
        if S == 0:
            continue
        Omega[owner[S]] = Omega.get(owner[S], 0.0) + float(m)
    rho = {i: Om / v for i, Om in Omega.items()}
    Lam = sum(math.log1p(r) for r in rho.values()) / math.log(2)
    tot = h2(v) + v * Lam
    for S, m in masses.items():
        if S == 0:
            continue
        g = gates[owner[S]]
        assert (S & ~g.R) == 0
        tot += float(m) * (-math.log2(rho[owner[S]]) + g.inner_cost(S))
    return tot


def best_owner(res):
    """Owner = cheapest single-root witness under lam=1 (a valid deterministic map)."""
    return {S: min(costs)[1] for S, (cmin, csum, costs) in res['per_set'].items()}
