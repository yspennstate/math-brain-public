"""Positive control: the read-once recursion must agree with a brute-force Walsh
transform, and rho0 must agree with a brute-force restriction computation."""
import itertools, math, random
from math import log2
import ro

def brute(t, n):
    """explicit truth table -> (p, I, H) by Walsh transform."""
    N = 1 << n
    f = [0]*N
    def ev(node, x):
        k = node[0]
        if k == 'const': return node[1]
        if k == 'lit':
            v = (x >> node[1]) & 1
            return v ^ (1 if node[2] else 0)
        a = ev(node[1], x); b = ev(node[2], x)
        return (a & b) if k == 'and' else (a | b)
    for x in range(N):
        f[x] = 1 if ev(t, x) else 0
    p = sum(f)/N
    # +-1 encoding
    g = [1.0 - 2.0*v for v in f]          # 1 -> -1 (true = -1, Hod's convention)
    # Walsh-Hadamard
    a = g[:]
    step = 1
    while step < N:
        for i in range(0, N, step*2):
            for j in range(i, i+step):
                u, v = a[j], a[j+step]
                a[j] = u+v; a[j+step] = u-v
        step *= 2
    a = [v/N for v in a]
    H = 0.0; I = 0.0
    for S in range(N):
        w = a[S]*a[S]
        if w > 1e-18:
            H += w*log2(1.0/w)
            I += w*bin(S).count('1')
    return p, I, H

def brute_rho0(t, n):
    p, I, H = brute(t, n)
    best = None; rows = []
    for i in range(n):
        t0 = ro.restrict(t, i, 0); t1 = ro.restrict(t, i, 1)
        p0, I0, H0 = brute(t0, n); p1, I1, H1 = brute(t1, n)
        inf_i = abs(p1-p0)
        if inf_i <= 1e-15: continue
        dH = H - (H0+H1)/2.0
        rows.append((i, inf_i, dH, dH/inf_i))
    if not rows: return None, rows, (p, I, H)
    return min(r[3] for r in rows), rows, (p, I, H)

def rand_tree(vars_):
    if len(vars_) == 1:
        return ro.lit(vars_[0], random.random() < 0.5)
    k = random.randint(1, len(vars_)-1)
    left = rand_tree(vars_[:k]); right = rand_tree(vars_[k:])
    return (ro.AND if random.random() < 0.5 else ro.OR)(left, right)

if __name__ == '__main__':
    random.seed(11)
    worstH = worstI = worstR = 0.0
    tested = 0
    for n in range(2, 11):
        for _ in range(40):
            t = rand_tree(list(range(n)))
            pr, Ir, Hr = ro.analyse(t)
            pb, Ib, Hb = brute(t, n)
            worstH = max(worstH, abs(Hr-Hb)); worstI = max(worstI, abs(Ir-Ib))
            r1, _, _ = ro.rho0(t)
            r2, _, _ = brute_rho0(t, n)
            if r1 is not None and r2 is not None:
                worstR = max(worstR, abs(r1-r2))
            tested += 1
    print("random read-once trees tested: %d  (n = 2..10)" % tested)
    print("max |H_recursion - H_brute|   = %.3e" % worstH)
    print("max |I_recursion - I_brute|   = %.3e" % worstI)
    print("max |rho0_recursion - brute|  = %.3e" % worstR)
    # the real negative control is negcontrol.py (fault injection); a same-n AND/OR
    # comparison is vacuous here because both have the same spectral entropy.
