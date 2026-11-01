#!/usr/bin/env python3
"""
R08 exact checker, 2026-09-16.

Exact arithmetic only (fractions.Fraction / integers).

Checks:
  1. R08-L003 off-axis transfer identity and sharpness family.
  2. Exact small finite-square Exp(1) FPP hitting-time expectations, k=1,2,3,
     as a failed finite-block route diagnostic.
  3. Independent audit of R09-PASSAGE-L1:
       * exact l1-ball count in Z^3;
       * exact shell count;
       * exact endpoint inequalities behind the 5/3 arcsin-sqrt derivative bound;
       * exact finite check that cube-boundary points have l1 norm >= L.
"""

from fractions import Fraction
from functools import lru_cache

def nu(p, q, u, x, y):
    # Square-symmetric norm used for sharpness of R08-L003:
    # max(|x|, |y|, [u/(p+q)] (|x|+|y|)).
    return max(
        Fraction(abs(x)),
        Fraction(abs(y)),
        u * Fraction(abs(x) + abs(y), p + q),
    )

def check_l003():
    cases = 0
    for p in range(1, 13):
        for q in range(0, p + 1):
            if p + q == 0:
                continue
            # u ranges over exact rational points in [p,p+q].
            den = 7
            for j in range(den + 1):
                u = Fraction(p * den + j * q, den)
                assert Fraction(p) <= u <= Fraction(p + q)
                axis = nu(p, q, u, 1, 0)
                w = nu(p, q, u, p, q)
                diag = nu(p, q, u, 1, 1)
                assert axis == 1
                assert w == u
                assert diag == 2 * u / Fraction(p + q)
                lhs_gap = 2 * axis - diag
                rhs_transfer = 2 * (axis - w / Fraction(p + q))
                assert lhs_gap == rhs_transfer

                # Finite exact triangle-inequality stress on the explicit norm.
                for x1 in range(-2, 3):
                    for y1 in range(-2, 3):
                        for x2 in range(-2, 3):
                            for y2 in range(-2, 3):
                                assert nu(p,q,u,x1+x2,y1+y2) <= (
                                    nu(p,q,u,x1,y1) + nu(p,q,u,x2,y2)
                                )
                cases += 1
    return cases

def grid_expected_fraction(k):
    """
    Expected infection time from (0,0) to (k,k) in the finite
    (k+1)x(k+1) nearest-neighbor square with iid Exp(1) edge times.

    Exact CTMC recursion. If infected set S does not contain target, each
    uninfected v is infected at rate equal to the number of S-v boundary
    edges. The next-event holding time is Exp(total boundary-edge count).
    """
    W = k + 1
    verts = [(i,j) for i in range(W) for j in range(W)]
    idx = {v:i for i,v in enumerate(verts)}
    n = len(verts)
    source = idx[(0,0)]
    target = idx[(k,k)]
    neigh = [[] for _ in range(n)]
    for (x,y), i in idx.items():
        for z in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if z in idx:
                neigh[i].append(idx[z])

    @lru_cache(None)
    def E(mask):
        if (mask >> target) & 1:
            return Fraction(0)
        rates = {}
        total = 0
        for u in range(n):
            if (mask >> u) & 1:
                for v in neigh[u]:
                    if not ((mask >> v) & 1):
                        rates[v] = rates.get(v,0) + 1
                        total += 1
        assert total > 0
        value = Fraction(1, total)
        for v, rate in rates.items():
            value += Fraction(rate, total) * E(mask | (1 << v))
        return value

    value = E(1 << source)
    return value, E.cache_info().currsize

def check_small_blocks():
    expected = {
        1: Fraction(5,4),
        2: Fraction(30757,14400),
        3: Fraction(5675443731448268047,1935723847680000000),
    }
    states = {}
    for k, target in expected.items():
        value, nstates = grid_expected_fraction(k)
        assert value == target
        # The finite-block upper mu(1,1) <= E T_k / k is still > 0.9
        # for k<=3, hence cannot by itself combine with an axis lower ~0.3
        # to certify the frozen gap.
        assert value / k > Fraction(9,10)
        states[k] = nstates
    return expected, states

def brute_l1_ball(L):
    c = 0
    for x in range(-L,L+1):
        for y in range(-L,L+1):
            for z in range(-L,L+1):
                if abs(x)+abs(y)+abs(z) <= L:
                    c += 1
    return c

def check_r09_passage_l1():
    # Exact shell and ball formulas in Z^3.
    for L in range(0, 13):
        V_formula = (4*L**3 + 6*L**2 + 8*L + 3)//3
        assert (4*L**3 + 6*L**2 + 8*L + 3) % 3 == 0
        assert brute_l1_ball(L) == V_formula
        if L >= 1:
            shell = brute_l1_ball(L) - brute_l1_ball(L-1)
            assert shell == 4*L*L + 2

    # Exact endpoint algebra behind Psi'(s)<=5/3 on [1/10,1/2].
    # Psi'(s)^2 = 1/[4s(1-s)].  It is enough to prove
    # 9 <= 100 s(1-s).  The concave quadratic attains its minimum
    # on this interval at an endpoint.
    lo, hi = Fraction(1,10), Fraction(1,2)
    assert 100*lo*(1-lo) == 9
    assert 100*hi*(1-hi) == 25
    assert Fraction(1, 4*lo*(1-lo)) == Fraction(25,9)  # squared equality at lo
    assert Fraction(1, 4*hi*(1-hi)) == 1

    # pc>=1/5 and delta<=1/10 imply pc-delta>=1/10.
    assert Fraction(1,5) - Fraction(1,10) == Fraction(1,10)

    # Every point on the l_infinity boundary of [-L,L]^3 has l1 norm >= L.
    for L in range(1,9):
        for x in range(-L,L+1):
            for y in range(-L,L+1):
                for z in range(-L,L+1):
                    if max(abs(x),abs(y),abs(z)) == L:
                        assert abs(x)+abs(y)+abs(z) >= L

    return 13, 8

def main():
    nsharp = check_l003()
    block_values, states = check_small_blocks()
    lmax, cubemax = check_r09_passage_l1()

    print("R08 exact checker")
    print("R08-L003 sharpness cases:", nsharp)
    print("R08-L003 finite exact norm triangle stress: PASS")
    for k in sorted(block_values):
        v = block_values[k]
        print(f"finite-square k={k}: E[T]={v} = {float(v):.15f}; states={states[k]}")
    print("finite-square diagnostic: PASS")
    print("R09-PASSAGE-L1 l1-ball/shell formulas through L=12: PASS")
    print("R09-PASSAGE-L1 Psi'<=5/3 endpoint algebra: PASS")
    print("R09-PASSAGE-L1 cube-boundary l1 check through L=8: PASS")
    print("R09-PASSAGE-L1 independent audit: PASS")
    print("PASS")

if __name__ == "__main__":
    main()
