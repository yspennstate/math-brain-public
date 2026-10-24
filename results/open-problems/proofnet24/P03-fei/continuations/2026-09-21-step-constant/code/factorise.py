"""Does the read-once spectrum factorise by gate pattern?
Claim: for f = AND(a,b) on disjoint variable sets, writing S = S_A u S_B,
    mu_f(S) = mass(pattern) * mu_a(S_A | pattern_A) * mu_b(S_B | pattern_B)
where pattern records whether S_A, S_B are empty, the four masses are
    w_empty, It_a - w_ab, It_b - w_ab, w_ab   (the AND gate weights),
and mu_a(.|empty) is the point mass at the empty set.
If true, B is computable by a recursion in O(n) instead of a 2^n spectrum."""
import numpy as np, itertools, random
import ro, control
from erasure import spectrum

def check(t, nA_vars, n):
    """t must be AND(a,b) or OR(a,b) at the root"""
    a, b = t[1], t[2]
    A = sorted(set(ro.leaves(a))); B = sorted(set(ro.leaves(b)))
    mu = spectrum(control_truth(t, n), n)
    # a and b on their own variable sets, relabelled to 0..k-1
    ra = relabel(a); rb = relabel(b)
    mua = spectrum(control_truth(ra, len(A)), len(A))
    mub = spectrum(control_truth(rb, len(B)), len(B))
    # masses by pattern, read off mu
    idx = np.arange(1 << n)
    maskA = 0
    for i in A: maskA |= (1 << i)
    maskB = 0
    for i in B: maskB |= (1 << i)
    SA = idx & maskA; SB = idx & maskB
    pat = (SA != 0).astype(int)*2 + (SB != 0).astype(int)
    mass = [float(mu[pat == p].sum()) for p in range(4)]
    # predicted: within each pattern, product of conditioned marginals
    worst = 0.0
    condA = {0: None, 1: mua.copy()}
    condA[1][0] = 0.0; s = condA[1].sum(); condA[1] = condA[1]/s if s > 0 else condA[1]
    condB = {0: None, 1: mub.copy()}
    condB[1][0] = 0.0; s = condB[1].sum(); condB[1] = condB[1]/s if s > 0 else condB[1]
    posA = {v: k for k, v in enumerate(A)}; posB = {v: k for k, v in enumerate(B)}
    for S in range(1 << n):
        sa = S & maskA; sb = S & maskB
        ia = 0
        for v in A:
            if sa >> v & 1: ia |= 1 << posA[v]
        ib = 0
        for v in B:
            if sb >> v & 1: ib |= 1 << posB[v]
        p = (1 if sa else 0)*2 + (1 if sb else 0)
        fa = 1.0 if sa == 0 else (condA[1][ia] if condA[1] is not None else 0)
        fb = 1.0 if sb == 0 else (condB[1][ib] if condB[1] is not None else 0)
        pred = mass[p]*fa*fb
        worst = max(worst, abs(pred - mu[S]))
    return worst, mass

def relabel(t):
    vs = sorted(set(ro.leaves(t))); m = {v: k for k, v in enumerate(vs)}
    def go(node):
        if node[0] == 'lit': return ('lit', m[node[1]], node[2])
        if node[0] == 'const': return node
        return (node[0], go(node[1]), go(node[2]))
    return go(t)

def control_truth(t, n):
    idx = np.arange(1 << n)
    def ev(node):
        k = node[0]
        if k == 'const': return np.full(1 << n, node[1], dtype=np.int8)
        if k == 'lit':
            v = ((idx >> node[1]) & 1).astype(np.int8)
            return (1 - v) if node[2] else v
        x = ev(node[1]); y = ev(node[2])
        return (x & y) if k == 'and' else (x | y)
    return ev(t)

if __name__ == '__main__':
    random.seed(4)
    worst_all = 0.0; tested = 0
    for n in range(2, 13):
        for _ in range(12):
            t = control.rand_tree(list(range(n)))
            if t[0] not in ('and', 'or'): continue
            w, mass = check(t, None, n)
            worst_all = max(worst_all, w); tested += 1
    print("pattern factorisation checked on %d random read-once trees (n=2..12)" % tested)
    print("worst |predicted mu(S) - true mu(S)| = %.3e" % worst_all)
    print("VERDICT:", "factorisation HOLDS" if worst_all < 1e-12 else "factorisation FAILS - do not build on it")
