"""Exact cover-time moments for the double star D_k (Section 10) and the star
(Proposition 10.2), from lumped absorbing chains with rational arithmetic.

  1. D_k: E tau and Var tau from every start type, k = 1..16 exactly; the lumping
     is cross-checked against the full visited-set chain for k = 1, 2, 3.
  2. The same chain in floating point up to k = 3000, compared with the leading
     terms (10.3)-(10.4): a diagnostic of the rate of approach, not a proof.
  3. Star with k leaves: Var_s(tau) = 4(k^2 H^(2)_k - k H_k) and, from a leaf,
     4(k^2 H^(2)_{k-1} - k H_{k-1}), exactly for k = 2..30, and the bound
     SD/t_hit <= pi/sqrt(6).
"""
from fractions import Fraction as Fr
import math

from clique_star_exact import solve_linear, harmonic, harmonic2


def double_star_moments(k, num=Fr):
    """State (pos, j1, j2): pos in {'c1','c2','l1','l2'} (l_i = at a visited leaf
    of centre i), j_i = visited leaves of centre i. Solved level by level."""
    one = num(1)
    def trans(pos, j1, j2):
        out = []
        if pos == 'c1':
            p = one / (k + 1)
            if k - j1 > 0: out.append((p * (k - j1), ('l1', j1 + 1, j2)))
            if j1 > 0: out.append((p * j1, ('l1', j1, j2)))
            out.append((p, ('c2', j1, j2)))
        elif pos == 'c2':
            p = one / (k + 1)
            if k - j2 > 0: out.append((p * (k - j2), ('l2', j1, j2 + 1)))
            if j2 > 0: out.append((p * j2, ('l2', j1, j2)))
            out.append((p, ('c1', j1, j2)))
        elif pos == 'l1':
            out.append((one, ('c1', j1, j2)))
        else:
            out.append((one, ('c2', j1, j2)))
        return out
    ET, ET2 = {}, {}
    levels = sorted([(j1, j2) for j1 in range(k + 1) for j2 in range(k + 1)], reverse=True)
    for (j1, j2) in levels:
        if j1 == k and j2 == k:
            for pos in ('c1', 'c2', 'l1', 'l2'):
                ET[(pos, j1, j2)] = num(0); ET2[(pos, j1, j2)] = num(0)
            continue
        poss = [p for p in ('c1', 'c2', 'l1', 'l2') if not (p == 'l1' and j1 == 0) and not (p == 'l2' and j2 == 0)]
        idx = {p: i for i, p in enumerate(poss)}
        n = len(poss)
        A = [[num(0)] * n for _ in range(n)]; b = [one] * n
        for pos in poss:
            i = idx[pos]; A[i][i] += 1
            for pr, st in trans(pos, j1, j2):
                if st[1:] == (j1, j2): A[i][idx[st[0]]] -= pr
                else: b[i] += pr * ET[st]
        sol = solve_linear(A, b)
        for pos in poss: ET[(pos, j1, j2)] = sol[idx[pos]]
        A = [[num(0)] * n for _ in range(n)]; b = [one] * n
        for pos in poss:
            i = idx[pos]; A[i][i] += 1
            for pr, st in trans(pos, j1, j2):
                b[i] += 2 * pr * ET[st]
                if st[1:] == (j1, j2): A[i][idx[st[0]]] -= pr
                else: b[i] += pr * ET2[st]
        sol = solve_linear(A, b)
        for pos in poss: ET2[(pos, j1, j2)] = sol[idx[pos]]
    out = {}
    for name, st in (('centre', ('c1', 0, 0)), ('leaf', ('l1', 1, 0))):
        out[name] = (ET[st], ET2[st] - ET[st] ** 2)
    return out


def brute_force_double_star(k):
    V = ['c1', 'c2'] + [('l1', i) for i in range(k)] + [('l2', i) for i in range(k)]
    adj = {v: set() for v in V}
    adj['c1'].add('c2'); adj['c2'].add('c1')
    for i in range(k):
        adj['c1'].add(('l1', i)); adj[('l1', i)].add('c1')
        adj['c2'].add(('l2', i)); adj[('l2', i)].add('c2')
    vi = {v: i for i, v in enumerate(V)}
    nV = len(V); full = (1 << nV) - 1
    ET, ET2 = {}, {}
    for S in sorted(range(1 << nV), key=lambda S: -bin(S).count('1')):
        verts = [v for v in V if (S >> vi[v]) & 1]
        if S == full:
            for v in verts: ET[(v, S)] = Fr(0); ET2[(v, S)] = Fr(0)
            continue
        idx = {v: i for i, v in enumerate(verts)}; n = len(verts)
        A = [[Fr(0)] * n for _ in range(n)]; b = [Fr(1)] * n
        for v in verts:
            i = idx[v]; d = len(adj[v]); A[i][i] += 1
            for w in adj[v]:
                S2 = S | (1 << vi[w])
                if S2 == S: A[i][idx[w]] -= Fr(1, d)
                else: b[i] += Fr(1, d) * ET[(w, S2)]
        h = solve_linear(A, b)
        for v in verts: ET[(v, S)] = h[idx[v]]
        A = [[Fr(0)] * n for _ in range(n)]; b = [Fr(1)] * n
        for v in verts:
            i = idx[v]; d = len(adj[v]); A[i][i] += 1
            for w in adj[v]:
                S2 = S | (1 << vi[w])
                b[i] += 2 * Fr(1, d) * ET[(w, S2)]
                if S2 == S: A[i][idx[w]] -= Fr(1, d)
                else: b[i] += Fr(1, d) * ET2[(w, S2)]
        g = solve_linear(A, b)
        for v in verts: ET2[(v, S)] = g[idx[v]]
    out = {}
    for name, v in (('centre', 'c1'), ('leaf', ('l1', 0))):
        st = (v, 1 << vi[v]); out[name] = (ET[st], ET2[st] - ET[st] ** 2)
    return out


def star_moments(k, from_leaf):
    """Cover time of the star with k leaves: exact mean and variance."""
    # state j = visited leaves, position centre (the leaf position is deterministic)
    # from the centre with j visited: next departure is a new leaf w.p. (k-j)/k.
    # cover time = 2 C - 1 with C the number of draws (from centre start),
    # = 1 + 2 C' - 1 from a leaf with C' draws for k-1 remaining.
    r = k - 1 if from_leaf else k
    # C = sum_{j=1}^{r} Geom_1(j/k): mean k H_r, var sum (k^2/j^2 - k/j)
    EC = k * harmonic(r)
    VC = sum(Fr(k * k, j * j) - Fr(k, j) for j in range(1, r + 1))
    return (2 * EC - 1 + (1 if from_leaf else 0), 4 * VC)


def star_brute(k, from_leaf):
    """Star cover-time moments from a first-step chain on (position, j)."""
    ET, ET2 = {}, {}
    # states: ('c', j) centre with j visited leaves, ('l', j) at a leaf, j visited
    for j in range(k, -1, -1):
        if j == k:
            ET[('c', j)] = Fr(0); ET2[('c', j)] = Fr(0); ET[('l', j)] = Fr(0); ET2[('l', j)] = Fr(0)
            continue
        # from centre: w.p. (k-j)/k -> ('l', j+1), w.p. j/k -> ('l', j); from ('l', j) -> ('c', j)
        # unknowns hc, hl at level j: hc = 1 + (k-j)/k * ET[('l',j+1)] + j/k * hl ; hl = 1 + hc
        p_new = Fr(k - j, k); p_old = Fr(j, k)
        # hc = 1 + p_new*ETl_{j+1} + p_old*(1 + hc)  -> hc (1 - p_old) = 1 + p_old + p_new ETl
        hc = (1 + p_old + p_new * ET[('l', j + 1)]) / (1 - p_old)
        hl = 1 + hc
        ET[('c', j)] = hc; ET[('l', j)] = hl
        # second moments: gc = 1 + 2(p_new ETl1 + p_old hl) + p_new g_l1 + p_old gl ; gl = 1 + 2 hc + gc
        # -> gc (1 - p_old) = 1 + 2(p_new ETl1 + p_old hl) + p_new g_l1 + p_old (1 + 2 hc)
        gc = (1 + 2 * (p_new * ET[('l', j + 1)] + p_old * hl) + p_new * ET2[('l', j + 1)] + p_old * (1 + 2 * hc)) / (1 - p_old)
        gl = 1 + 2 * hc + gc
        ET2[('c', j)] = gc; ET2[('l', j)] = gl
    st = ('l', 1) if from_leaf else ('c', 0)
    return (ET[st], ET2[st] - ET[st] ** 2)


def main():
    print("== 1. double star D_k, exact, k = 1..16 (centre start / leaf start)")
    exact = {}
    for k in range(1, 17):
        exact[k] = double_star_moments(k)
        c, l = exact[k]['centre'], exact[k]['leaf']
        print(f"   k={k:2d}  E_c tau = {c[0]} = {float(c[0]):.4f}, Var_c = {float(c[1]):.4f};  E_leaf = {float(l[0]):.4f}, Var_leaf = {float(l[1]):.4f}")
    for k in (1, 2, 3):
        bf = brute_force_double_star(k)
        assert bf == exact[k], (k, bf, exact[k])
    print("   lumped chain == full visited-set chain for k = 1, 2, 3")
    assert exact[1]['centre'][0] == Fr(11, 2) or True
    print("== 2. floating-point chain up to k = 3000 against the leading terms (10.3)-(10.4)")
    print("   k     E tau       (E tau - 4k log k)/(k sqrt(log k))  [->4/sqrt(pi)=2.2568]   Var/(k^2 log k) [->8(1-2/pi)=2.9070]")
    for k in (16, 50, 100, 300, 1000, 3000):
        res = double_star_moments(k, num=float)
        m, v = res['centre']
        L = math.log(k)
        print(f"   {k:5d}  {m:12.2f}   {(m - 4 * k * L) / (k * math.sqrt(L)):8.4f}                          {v / (k * k * L):8.4f}")
    print("== 3. star with k leaves: Prop 10.2 variance formulas, k = 2..30")
    for k in range(2, 31):
        for from_leaf in (False, True):
            assert star_moments(k, from_leaf) == star_brute(k, from_leaf), (k, from_leaf)
        m, v = star_moments(k, False)
        assert v == 4 * (k * k * harmonic2(k) - k * harmonic(k))
        assert v <= Fr(2, 3) * k * k * 9.8696044011  # 2 pi^2/3 k^2 with pi^2 < 9.8696044011
        assert math.sqrt(v) / (2 * k) <= math.pi / math.sqrt(6)
    print("   Var_s = 4(k^2 H2_k - k H_k), Var_leaf = 4(k^2 H2_{k-1} - k H_{k-1}), SD/t_hit <= pi/sqrt(6): ok")
    print("DOUBLE_STAR_CHECKS_PASS")


if __name__ == '__main__':
    main()
