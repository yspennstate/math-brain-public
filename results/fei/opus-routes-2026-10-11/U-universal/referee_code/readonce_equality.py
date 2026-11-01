"""Equality case of Lemma G-key / Theorem G (referee finding).

Claim checked here by brute force: for a read-once formula over AND/OR gates with possibly negated literals,
every Walsh set S in the support satisfies |fhat(S)| = 2^{|S|-1} I_S(f) exactly, so Theorem G
H = 2(I - Var) + 2U - p0 log2(1/p0) is an identity.  Control: read-once formulas that use XOR or MAJ3 gates
must show strict inequalities.
Exact integers for the lemma (W_S^2 4^n == 4^{|S|-1} Pi_S^2), float for the theorem."""
import json
import numpy as np
from rlib import walsh, superset_sum, popcounts, Spec

rng = np.random.default_rng(2026)


def rand_formula(nleaves, gates):
    """returns a function X(+-1 matrix) -> values, built as a random binary read-once tree; literals negated at random."""
    if nleaves == 1:
        neg = rng.random() < 0.5
        return (lambda X, c=[0]: (-1 if neg else 1) * X[:, 0]), 1
    left = int(rng.integers(1, nleaves))
    fa, na = rand_formula(left, gates); fb, nb = rand_formula(nleaves - left, gates)
    g = gates[int(rng.integers(len(gates)))]
    neg = rng.random() < 0.3

    def f(X, fa=fa, fb=fb, na=na, g=g, neg=neg):
        a = fa(X[:, :na]); b = fb(X[:, na:])
        if g == 'AND':
            v = np.where((a == -1) & (b == -1), -1, 1)
        elif g == 'OR':
            v = np.where((a == -1) | (b == -1), -1, 1)
        else:  # XOR
            v = a * b
        return -v if neg else v
    return f, na + nb


def check(gates, trials, nmax):
    eq_all = 0; tested = 0; strict_cases = 0; min_slack = 1e9; max_slack = 0
    for t in range(trials):
        n = int(rng.integers(2, nmax + 1))
        f, nv = rand_formula(n, gates)
        N = 1 << nv; xs = np.arange(N)
        X = np.stack([1 - 2 * ((xs >> i) & 1) for i in range(nv)], 1)
        tab = f(X).astype(np.int64)
        if abs(tab.sum()) == N:
            continue
        W = walsh(tab); P = [int(w) * int(w) for w in W]
        Pi = superset_sum(np.array(P, dtype=object)); pc = popcounts(nv)
        allEq = True
        for S in range(1, N):
            if P[S] == 0:
                continue
            if P[S] * N * N != (4 ** (int(pc[S]) - 1)) * int(Pi[S]) ** 2:
                allEq = False
        sp = Spec.from_tables(tab)
        H = float(sp.H()[0]); I = float(sp.I()[0]); U = float(sp.U()[0]); Var = float(sp.Var()[0]); p0 = 1 - Var
        slack = 2 * (I - Var) + 2 * U - (p0 * np.log2(1 / p0) if p0 > 0 else 0.0) - H
        tested += 1; eq_all += int(allEq); strict_cases += int(not allEq)
        min_slack = min(min_slack, slack); max_slack = max(max_slack, slack)
    return dict(tested=tested, all_S_equal=eq_all, some_S_strict=strict_cases, min_thmG_slack=min_slack, max_thmG_slack=max_slack)


out = {}
out['AND_OR_with_negations'] = check(['AND', 'OR'], 200, 12)
out['with_XOR_gates_control'] = check(['AND', 'OR', 'XOR'], 200, 12)
print(json.dumps(out, indent=1))
with open('readonce_equality_results.json', 'w', encoding='utf-8') as fh:
    json.dump(out, fh, indent=1)
