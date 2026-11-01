"""Check the derived cycle formula against brute force, and see what it says about RC.

DERIVED (not fitted): for the m-cycle of NAE triangles - shared coordinates x_1..x_m around the
cycle, each triangle {x_i, x_{i+1}, a_i} carrying its own private a_i, so r = 2m, k = m -

    |A| = 3^m + (-1)^m          independence predicts exactly 3^m
    c   = log2(1 + (-1)^m / 3^m)

Derivation: condition on x. Triangle i is monochromatic-forbidden only through a_i, which is FREE
when x_i != x_{i+1} and FORCED when x_i = x_{i+1}. With y_i = [x_i != x_{i+1}] (sum necessarily
even, going around a cycle), the count is 2 * sum_{j even} C(m,j) 2^j, and
sum_{j even} C(m,j)2^j = (3^m + (-1)^m)/2 by (1+2)^m and (1-2)^m.

Consequences to check, not to assume:
  c > 0  <=>  m EVEN, and then c <= log2(1 + 1/81) ~ 0.0177 for m >= 4
  RC on a pure m-cycle  <=>  d_cb <= m - c/beta  <=>  d_cb <= m - 1  (d_cb integral, c/beta < 1)

The last line is the useful one: on cycles the campaign's PROVED bound d_cb <= k is exactly one
dimension too weak, and RC needs no more than shaving that single dimension.
"""
import itertools
import math

BETA = math.log2(4.0 / 3.0)


def cycle_system(m):
    """triangles {x_i, x_{i+1 mod m}, a_i}; coords 0..m-1 shared, m..2m-1 private."""
    return [(i, (i + 1) % m, m + i) for i in range(m)]


def fibre_size(r, T):
    n = 0
    for s in itertools.product((0, 1), repeat=r):
        if all(not (s[a] == s[b] == s[c]) for (a, b, c) in T):
            n += 1
    return n


print("  m    r   |A| brute   3^m+(-1)^m   match   pred 3^m    c          c/beta    RC needs")
for m in range(3, 11):
    T = cycle_system(m)
    r = 2 * m
    # linearity check: no two triangles may share two coordinates
    lin = all(len(set(t) & set(u)) < 2 for t, u in itertools.combinations(T, 2))
    if r <= 20:
        n = fibre_size(r, T)
    else:
        n = None
    formula = 3 ** m + (-1) ** m
    c = math.log2(1.0 + ((-1.0) ** m) / 3.0 ** m)
    need = m - c / BETA
    print("  %2d  %3d   %9s   %10d   %5s   %8d   %+.7f  %+.6f  d_cb <= %.4f -> %d"
          % (m, r, str(n) if n is not None else "(skip)", formula,
             ("YES" if n == formula else "NO") if n is not None else "-",
             3 ** m, c, c / BETA, need, math.floor(need) if c > 0 else m))
    if not lin:
        print("      NOTE: m=%d is NOT linear (adjacent triangles share two coordinates)" % m)

print()
print("Reading: c > 0 exactly on EVEN m, and it decays like 3^-m. On every even cycle RC asks only")
print("that d_cb be at most m-1, i.e. one below the campaign's proved d_cb <= k. On odd m, c < 0 and")
print("RC is already implied by d_cb <= k with room to spare.")
