#!/usr/bin/env python3
"""
Exact finite certificate for R7-07 / F0012, 2026-09-19.

All arithmetic relevant to the verdict is integer/rational.

Checks:
1. Exact numbers of n x n sign matrices whose characteristic polynomial
   splits over Z[i], n=1,2,3,4.
2. The necessary split-prime filters p=5 and p=13. For n<=4, their
   intersection happens to equal the Gaussian-integral-spectrum event.
3. The fixed-shear weighted ternary-pair partition W_m, m=1,2,3.
4. The weighted subpartition in which both ternary support digraphs are
   acyclic (equivalently permutation-triangularizable), and the
   reverse-order single-pair formula T_m.

No floating-point comparison enters any assertion.
"""
from itertools import product, combinations_with_replacement
from fractions import Fraction
from math import gcd


def matmul(A, B, n):
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def char_elementary(flat, n):
    """e_1,...,e_n for chi(x)=x^n-e1*x^(n-1)+e2*x^(n-2)-..."""
    A = [list(flat[i*n:(i+1)*n]) for i in range(n)]
    traces = []
    P = [row[:] for row in A]
    for k in range(1, n+1):
        if k > 1:
            P = matmul(P, A, n)
        traces.append(sum(P[i][i] for i in range(n)))

    e = [1]
    for k in range(1, n+1):
        num = sum((1 if j % 2 else -1) * e[k-j] * traces[j-1]
                  for j in range(1, k+1))
        assert num % k == 0
        e.append(num // k)
    return tuple(e[1:])


def pmul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return tuple(out)


def gaussian_split_elementary(n, bound):
    """
    Elementary-coefficient tuples of all monic degree-n integer polynomials
    whose roots are Gaussian integers of |root|<=bound.

    Real coefficients force nonreal roots to occur in conjugate pairs.
    Hence the generating factors are:
        x-a
        (x-(a+bi))(x-(a-bi)) = x^2-2ax+(a^2+b^2).
    """
    factors = []
    for a in range(-bound, bound+1):
        factors.append((1, (-a, 1)))
    for a in range(-bound, bound+1):
        for b in range(1, bound+1):
            if a*a + b*b <= bound*bound:
                factors.append((2, (a*a+b*b, -2*a, 1)))

    bydeg = {0: {(1,)}}
    for deg in range(n+1):
        for p in list(bydeg.get(deg, ())):
            for fd, f in factors:
                if deg + fd <= n:
                    bydeg.setdefault(deg+fd, set()).add(pmul(p, f))

    ans = set()
    for p in bydeg[n]:
        desc = list(reversed(p))
        assert desc[0] == 1
        ans.add(tuple(((-1)**k) * c
                      for k, c in enumerate(desc[1:], start=1)))
    return ans


def split_mod_p_elementary(n, p):
    """Elementary tuples mod p for monic degree-n polynomials split over F_p."""
    ans = set()
    for roots in combinations_with_replacement(range(p), n):
        e = [1] + [0]*n
        for r in roots:
            for k in range(n, 0, -1):
                e[k] = (e[k] + r*e[k-1]) % p
        ans.add(tuple(e[1:]))
    return ans


def is_acyclic_support(flat, n):
    """Directed edge i->j iff i!=j and entry(i,j)!=0."""
    adj = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and flat[i*n+j] != 0:
                adj[i][j] = True
    reach = [row[:] for row in adj]
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return all(not reach[i][i] for i in range(n))


def support_counts(n, require_gaussian=True, require_acyclic=False):
    N = n*n
    allowed = gaussian_split_elementary(n, n) if require_gaussian else None
    counts = [0]*(1 << N)
    matrices = 0
    for flat in product((-1,0,1), repeat=N):
        if require_gaussian and char_elementary(flat, n) not in allowed:
            continue
        if require_acyclic and not is_acyclic_support(flat, n):
            continue
        matrices += 1
        mask = 0
        for k,v in enumerate(flat):
            if v:
                mask |= 1 << k
        counts[mask] += 1
    return counts, matrices


def weighted_disjoint_partition(counts, N):
    nonzero = [(s,c,s.bit_count()) for s,c in enumerate(counts) if c]
    W = 0
    for s, cs, bs in nonzero:
        for t, ct, bt in nonzero:
            if s & t == 0:
                W += cs * ct * (2 ** (N-bs-bt))
    return W, len(nonzero)


def reverse_order_partition(m):
    return 16 ** (m*(m-1)//2) * 6**m


def main():
    expected_E = {
        1: (2, 2),
        2: (12, 16),
        3: (256, 512),
        4: (18864, 65536),
    }
    expected_mod = {
        1: (2, 2, 2),
        2: (12, 12, 12),
        3: (256, 344, 256),
        4: (20592, 26288, 18864),
    }

    for n in range(1,5):
        gi = gaussian_split_elementary(n, n)
        split5 = split_mod_p_elementary(n, 5)
        split13 = split_mod_p_elementary(n, 13)
        total = 2**(n*n)
        good = s5 = s13 = s5s13 = 0
        for flat in product((-1,1), repeat=n*n):
            e = char_elementary(flat, n)
            is_good = e in gi
            a = tuple(x % 5 for x in e) in split5
            b = tuple(x % 13 for x in e) in split13
            good += is_good
            s5 += a
            s13 += b
            s5s13 += a and b
        assert (good,total) == expected_E[n]
        assert (s5,s13,s5s13) == expected_mod[n]
        assert good == s5s13
        g = gcd(good,total)
        print(f"E_{n}: {good}/{total} = {good//g}/{total//g}; "
              f"split5={s5}; split13={s13}; both={s5s13}")

    expected_W = {1:6, 2:1160, 3:6580992}
    expected_Wdag = {1:6, 2:1008, 3:4326912}
    expected_good_ternary = {1:3, 2:61, 3:7911}

    for m in range(1,4):
        a, good_ternary = support_counts(m, require_gaussian=True)
        W, masks = weighted_disjoint_partition(a, m*m)
        assert W == expected_W[m]
        assert good_ternary == expected_good_ternary[m]

        adag, dag_matrices = support_counts(
            m, require_gaussian=False, require_acyclic=True)
        Wdag, dag_masks = weighted_disjoint_partition(adag, m*m)
        assert Wdag == expected_Wdag[m]

        T = reverse_order_partition(m)
        print(f"W_{m}={W}; ternary_good={good_ternary}; masks={masks}; "
              f"W_DAG={Wdag}; dag_matrices={dag_matrices}; "
              f"dag_masks={dag_masks}; T_reverse={T}; "
              f"W/T={Fraction(W,T)}; W_DAG/W={Fraction(Wdag,W)}; "
              f"D=W/2^(2m^2)={Fraction(W,2**(2*m*m))}")

    assert Fraction(expected_W[3], 2**18) == Fraction(25707,1024)
    print("D_3 = W_3/2^18 = 25707/1024")
    print("ALL_EXACT_F0012_DISCRETIZATION_CHECKS_PASS")


if __name__ == "__main__":
    main()
