"""Feasible intersection arrays, with the multiplicity test, and the largest tau_0/n among them.

The basic monotonicity and integrality conditions on {b_0..b_{d-1}; c_1..c_d} admit path-like arrays such
as {k,1,...,1; 1,...,1} that no graph realises, and those are exactly the arrays with a large tau_0/n.
The standard further test is that the eigenvalue multiplicities be positive integers: the eigenvalues
theta_0 = k > theta_1 > ... > theta_d are those of the tridiagonal intersection matrix, and

    m_j = n / sum_{i=0..d} k_i u_i(theta_j)^2 ,

where u_0 = 1, u_1 = theta/k and c_i u_{i-1} + a_i u_i + b_i u_{i+1} = theta u_i.  An array passing this
is called feasible; it still need not be realised, but the test removes most of the impostors.

Control: the thirteen cubic distance-regular graphs must all pass.
"""
import numpy as np
from fractions import Fraction as F
import sys


def ks(b, c):
    k = [F(1)]
    for i in range(len(b)):
        num = k[i] * b[i]
        if num % c[i] != 0: return None
        k.append(num / c[i])
    return k


def multiplicities(b, c):
    """eigenvalue multiplicities, or None if the array is not integrally feasible"""
    d = len(b)
    a = [b[0] - b[i] - (c[i - 1] if i > 0 else 0) for i in range(d)]
    a = [b[0] - b[0]] + [b[0] - b[i] - c[i - 1] for i in range(1, d)] + [b[0] - c[d - 1]]
    k = ks(b, c)
    if k is None or any(x <= 0 for x in k): return None
    n = sum(k)
    B = np.zeros((d + 1, d + 1))
    for i in range(d + 1):
        B[i, i] = float(a[i])
        if i < d: B[i, i + 1] = float(b[i])
        if i > 0: B[i, i - 1] = float(c[i - 1])
    th = np.sort(np.linalg.eigvals(B).real)[::-1]
    if abs(th[0] - b[0]) > 1e-6: return None
    ms = []
    for t in th:
        u = [1.0, t / b[0]]
        for i in range(1, d):
            nxt = (t * u[i] - c[i - 1] * u[i - 1] - a[i] * u[i]) / b[i]
            u.append(nxt)
        s = sum(float(k[i]) * u[i] ** 2 for i in range(d + 1))
        ms.append(float(n) / s)
    if any(m < 0.5 for m in ms): return None
    if any(abs(m - round(m)) > 1e-6 * max(1.0, m) for m in ms): return None
    if abs(sum(ms) - float(n)) > 1e-4 * float(n): return None
    return ms


def tau_over_n(b, c):
    k = ks(b, c)
    n = sum(k)
    tot = F(0)
    for i in range(1, len(k)):
        tot += sum(k[i:]) / (k[i] * c[i - 1])
    return b[0] * tot / n, int(n)


def enumerate_arrays(k, d):
    res = []
    def rec(b, c):
        i = len(b)
        if i == d:
            if multiplicities(b, c) is not None:
                r, n = tau_over_n(b, c)
                res.append((float(r), n, tuple(b), tuple(c)))
            return
        # b_0 must equal the valency k exactly, or the enumeration leaks in smaller valencies
        # (which is how the cycles, valency 2, were turning up as the extremes for k = 3 and 4)
        brange = [k] if i == 0 else list(range(b[-1], 0, -1))
        for bi in brange:
            lo_c = c[-1] if c else 1
            for ci in range(lo_c, k + 1):
                if i == 0 and ci != 1: continue
                # a_i = k - b_i - c_i >= 0 pairs b_i with c_i, and c_i is c[i-1] in this list
                if i > 0 and bi + c[i - 1] > k: continue
                if ks(b + [bi], c + [ci]) is None: continue
                rec(b + [bi], c + [ci])
    rec([], [])
    return res


if __name__ == '__main__':
    from drg_hitting import DRG
    print("CONTROL: the thirteen cubic distance-regular graphs must be feasible")
    bad = [nm for nm, b, c in DRG if multiplicities(b, c) is None]
    print(f"   {len(DRG) - len(bad)} of {len(DRG)} pass" + (f"; FAILING: {bad}" if bad else ""))

    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    dmax = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    print(f"\n{'k':>3} {'d':>3} {'feasible':>9} {'max tau_0/n':>12} {'n':>8}  array")
    grand = (0.0, None)
    for kk in range(3, kmax + 1):
        for d in range(1, dmax + 1):
            res = enumerate_arrays(kk, d)
            if not res: continue
            res.sort(key=lambda z: -z[0])
            r, n, b, c = res[0]
            print(f"{kk:>3} {d:>3} {len(res):>9} {r:>12.4f} {n:>8}  "
                  f"{{{','.join(map(str,b))};{','.join(map(str,c))}}}", flush=True)
            if r > grand[0]: grand = (r, res[0])
    print(f"\nlargest tau_0/n over feasible arrays of valency 3..{kmax}, diameter up to {dmax}: "
          f"{grand[0]:.4f}")
    r, n, b, c = grand[1]
    print(f"   n = {n}, array {{{','.join(map(str,b))};{','.join(map(str,c))}}}")
