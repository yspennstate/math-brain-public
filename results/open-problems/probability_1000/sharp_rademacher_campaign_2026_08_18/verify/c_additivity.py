"""Is the correlation excess c additive over independent cycles, and does it see only cycle lengths?

Established this session (brute-force verified m=3..10): the pure m-cycle has
|A| = 3^m + (-1)^m, so c = log2(1 + (-1)^m 3^-m).

Established mechanism: a triangle with two shared coordinates u,v contributes a factor
(2 - [u=v]), which averages to 2*(3/4) but is NOT constant. In a TREE the shared coordinates
entering any one triangle stay independent and uniform, so everything factorises and c = 0 exactly.
Around a CYCLE the last pair is linked through the rest, and that is the correlation.

If that account is right, then for a system whose cycle space has independent cycles of lengths
m_1..m_s, the natural guess is

    |A| / |A|_indep  =  prod_j (1 + (-1)^{m_j} 3^{-m_j})        i.e.   c = sum_j c(m_j).

This tests the guess against exact counts on systems built to have a controlled cycle structure:
  - two disjoint cycles (independent, sharing nothing)
  - two cycles joined at a single coordinate (independent cycles, one shared vertex)
  - two cycles sharing a triangle (NOT independent - the guess should be tested here, not assumed)
  - a theta graph (two vertices joined by three paths: cycle space dim 2, cycles overlap)
  - a cycle with trees hung off it (trees should contribute nothing)

Reports predicted vs exact, and names any shape where the guess fails - a failure is the useful
outcome, since it says which invariant c actually reads.
"""
import itertools
import math

BETA = math.log2(4.0 / 3.0)


def fibre_size(r, T):
    n = 0
    for s in itertools.product((0, 1), repeat=r):
        if all(not (s[a] == s[b] == s[c]) for (a, b, c) in T):
            n += 1
    return n


def is_linear(T):
    return all(len(set(t) & set(u)) < 2 for t, u in itertools.combinations(T, 2))


def cyc_pred(ms):
    p = 1.0
    for m in ms:
        p *= (1.0 + ((-1.0) ** m) / 3.0 ** m)
    return math.log2(p)


def report(name, T, cycles_claimed):
    r = len({x for t in T for x in t})
    # relabel to 0..r-1
    lab = {x: i for i, x in enumerate(sorted({x for t in T for x in t}))}
    T2 = [tuple(lab[x] for x in t) for t in T]
    k = len(T2)
    if not is_linear(T2):
        print("  %-34s NOT LINEAR - skipped" % name)
        return
    if r > 22:
        print("  %-34s r=%d too big - skipped" % (name, r))
        return
    n = fibre_size(r, T2)
    ell = r - math.log2(n)
    c = k * BETA - ell
    pred = cyc_pred(cycles_claimed)
    ok = abs(c - pred) < 1e-9
    print("  %-34s k=%-2d r=%-3d |A|=%-7d c=%+.7f  pred(%s)=%+.7f  %s"
          % (name, k, r, n, c, ",".join(map(str, cycles_claimed)) or "-", pred,
             "MATCH" if ok else "*** MISMATCH"))


def cycle(mm, base_shared, base_priv):
    """m-cycle on given shared/private label pools"""
    return [(base_shared + i, base_shared + (i + 1) % mm, base_priv + i) for i in range(mm)]


print("# c predicted as sum over INDEPENDENT cycles of log2(1 + (-1)^m 3^-m)")
print()

# pure cycles - controls, must match by construction
for m in (3, 4, 5, 6):
    report("pure %d-cycle" % m, cycle(m, 0, 100), [m])

print()
# two disjoint cycles
report("3-cycle + 3-cycle disjoint", cycle(3, 0, 100) + cycle(3, 10, 110), [3, 3])
report("3-cycle + 4-cycle disjoint", cycle(3, 0, 100) + cycle(4, 10, 110), [3, 4])
report("4-cycle + 4-cycle disjoint", cycle(4, 0, 100) + cycle(4, 10, 110), [4, 4])

print()
# a cycle with a pendant triangle (tree part hung off it) - tree part should contribute 0
for m in (3, 4):
    T = cycle(m, 0, 100)
    T = T + [(0, 200, 201)]          # pendant triangle on shared coordinate 0
    report("%d-cycle + pendant triangle" % m, T, [m])
    T2 = cycle(m, 0, 100) + [(100, 202, 203)]   # pendant on a PRIVATE coordinate
    report("%d-cycle + pendant on private" % m, T2, [m])

print()
# two cycles glued at one coordinate
for (m1, m2) in ((3, 3), (3, 4), (4, 4)):
    A = cycle(m1, 0, 100)
    B = cycle(m2, 10, 110)
    # identify shared coordinate 10 of B with 0 of A
    B = [tuple(0 if x == 10 else x for x in t) for t in B]
    report("%d-cycle & %d-cycle at a vertex" % (m1, m2), A + B, [m1, m2])
