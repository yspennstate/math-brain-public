"""Does RC have a counterexample family? K_{n,n} as the sharing graph.

Proved today: |A| / (2^r (3/4)^k) = Z = < prod_{edges}(1 - x_u x_v / 3) >, an Ising partition
function at coupling -1/3 on the sharing graph G. RC (with the campaign's proved d_cb <= k) is

    RC  <=>  Z <= (4/3)^{k - d_cb}      i.e.   c = log2 Z <= beta (k - d_cb).

Every edge factor lies in [2/3, 4/3], and it is 4/3 exactly when x_u != x_v. So on a BIPARTITE
graph the two configurations that align with the bipartition make every factor 4/3 at once:

    Z >= 2 * (4/3)^E / 2^V.

Take G = K_{n,n}. It is legal for a linear triangle system: each edge (i,j) becomes a triangle
{u_i, v_j, private_ij}, no two triangles share two coordinates because no two vertices span two
edges. So k = n^2, r = 2n + n^2.

Then log2 Z >~ n^2 beta - 2n + 1, so ell = k*beta - c <~ 2n - 1 while k = n^2, and RC demands

    d_cb <= (2n - 1)/beta ~ 4.82 n     against the trivial ceiling d_cb <= k = n^2.

If d_cb on this family grows faster than linearly in n, RC IS FALSE. That is a far more concrete
target than anything the campaign has had.

This computes Z exactly for K_{n,n} (closed form by symmetry: only the number of + signs in each
part matters), reports ell and the d_cb threshold RC needs, and checks the closed form against
brute force at small n.
"""
import itertools
import math
from fractions import Fraction

BETA = math.log2(4.0 / 3.0)


def Z_Knn_exact(n):
    """Z = 2^-2n SUM_{p,q} C(n,p) C(n,q) (2/3)^{same} (4/3)^{diff}
    where a has p pluses, b has q pluses; same = pq + (n-p)(n-q), diff = p(n-q) + (n-p)q."""
    tot = Fraction(0)
    for p in range(n + 1):
        for q in range(n + 1):
            same = p * q + (n - p) * (n - q)
            diff = p * (n - q) + (n - p) * q
            w = Fraction(math.comb(n, p) * math.comb(n, q))
            tot += w * Fraction(2, 3) ** same * Fraction(4, 3) ** diff
    return tot / Fraction(2) ** (2 * n)


def Z_bruteforce_fibre(n):
    """|A| / (2^r (3/4)^k) computed from the actual triangle system, small n only."""
    U = list(range(n))
    V = list(range(n, 2 * n))
    T = []
    priv = 2 * n
    for i in U:
        for j in V:
            T.append((i, j, priv))
            priv += 1
    r = priv
    if r > 20:
        return None, len(T), r
    cnt = 0
    for s in itertools.product((0, 1), repeat=r):
        if all(not (s[a] == s[b] == s[c]) for (a, b, c) in T):
            cnt += 1
    return cnt / ((2.0 ** r) * 0.75 ** len(T)), len(T), r


print("  n    k=n^2   r        Z (exact)          c=log2 Z     ell        RC needs d_cb <=   vs k")
for n in range(2, 13):
    k = n * n
    r = 2 * n + k
    Z = Z_Knn_exact(n)
    Zf = float(Z)
    c = math.log2(Zf)
    ell = k * BETA - c
    need = ell / BETA
    print("  %2d  %6d %5d   %18.10f   %+9.4f   %8.4f   %10.3f        %d"
          % (n, k, r, Zf, c, ell, need, k))

print()
print("cross-check of the closed form against the actual triangle system (small n only):")
for n in (2, 3):
    ratio, k, r = Z_bruteforce_fibre(n)
    Z = float(Z_Knn_exact(n))
    if ratio is None:
        print("   n=%d  k=%d r=%d  brute force too big" % (n, k, r))
    else:
        print("   n=%d  k=%d r=%d  fibre ratio %.10f   closed form %.10f   %s"
              % (n, k, r, ratio, Z, "MATCH" if abs(ratio - Z) < 1e-9 else "*** MISMATCH ***"))

print()
print("Reading: ell stays ~linear in n while k grows quadratically, so the d_cb budget RC allows")
print("grows LINEARLY while the number of triangles grows QUADRATICALLY. RC on this family is the")
print("claim that d_cb is O(n) on a system with n^2 triangles.")
