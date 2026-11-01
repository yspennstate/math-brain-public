from itertools import combinations


def closure(n, edges):
    R = set(edges)
    changed = True
    while changed:
        changed = False
        add = set()
        for a, b in R:
            for c, d in R:
                if b == c and (a, d) not in R:
                    add.add((a, d))
        if add:
            R |= add
            changed = True
    return frozenset(R)


def poset_width(n, R):
    best = 0
    for mask in range(1, 1 << n):
        vs = [i for i in range(n) if (mask >> i) & 1]
        if all((u, v) not in R and (v, u) not in R
               for u, v in combinations(vs, 2)):
            best = max(best, len(vs))
    return best


def cover(x, a, n, R):
    return (x, a) in R and not any(
        z not in (x, a) and (x, z) in R and (z, a) in R
        for z in range(n)
    )


total = width3 = forks = strict = 0
for n in range(2, 7):
    pairs = list(combinations(range(n), 2))
    seen = set()
    for mask in range(1 << len(pairs)):
        R = closure(
            n,
            [pairs[k] for k in range(len(pairs)) if (mask >> k) & 1],
        )
        if R in seen:
            continue
        seen.add(R)
        total += 1
        if poset_width(n, R) > 3:
            continue
        width3 += 1

        # The natural order 0<...<n-1 is the chosen ambient linear extension.
        # Every finite poset together with a chosen linear extension can be
        # relabelled this way.  We check the local hypotheses used in the proof:
        # adjacent incomparable x,y; two incomparable Hasse successors a,b of x,
        # both incomparable with y; all predecessor distinguishers occur after y.
        for x in range(n - 1):
            y = x + 1
            if (x, y) in R:
                continue
            for a, b in combinations(range(n), 2):
                if len({x, y, a, b}) < 4:
                    continue
                if not cover(x, a, n, R) or not cover(x, b, n, R):
                    continue
                if (a, b) in R or (b, a) in R:
                    continue
                if any(q in R for q in ((y, a), (a, y), (y, b), (b, y))):
                    continue

                Pa = {z for z in range(n) if (z, a) in R}
                Pb = {z for z in range(n) if (z, b) in R}
                D = (Pa - Pb) | (Pb - Pa)
                if any(z <= y for z in D):
                    continue

                forks += 1
                if D:
                    strict += 1

                # The theorem's conclusions: predecessor sets are nested, and
                # the proper difference is a chain.
                assert Pa <= Pb or Pb <= Pa
                diff = (Pa - Pb) if Pb <= Pa else (Pb - Pa)
                assert all((u, v) in R or (v, u) in R
                           for u, v in combinations(diff, 2))

print("POS3_PREDECESSOR_FUNNEL_REGRESSION_PASS")
print("unique_transitive_closures", total)
print("width_le_3", width3)
print("delayed_two_cover_forks", forks)
print("strict_predecessor_difference_cases", strict)
