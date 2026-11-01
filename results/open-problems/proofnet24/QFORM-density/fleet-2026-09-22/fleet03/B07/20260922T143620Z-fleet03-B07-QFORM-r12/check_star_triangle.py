from fractions import Fraction
from itertools import combinations


def compositions(n, k, prefix=()):
    if k == 1:
        yield prefix + (n,)
        return
    for i in range(n + 1):
        yield from compositions(n - i, k - 1, prefix + (i,))


def main(N=12):
    vertices = tuple(range(4))
    edges = tuple(combinations(vertices, 2))
    total = 0
    collar = 0
    min_margin = None

    for counts in compositions(N, len(edges)):
        total += 1
        w = {e: Fraction(c, N) for e, c in zip(edges, counts)}
        rho = sum(
            w[e] * w[f]
            for e in edges
            for f in edges
            if set(e).isdisjoint(f)
        )

        # Exact check of rho = 1 - sum q_v^2 + sum w_e^2.
        q = {
            v: sum(w[e] for e in edges if v in e)
            for v in vertices
        }
        rhs = Fraction(1) - sum(x * x for x in q.values()) + sum(
            x * x for x in w.values()
        )
        assert rho == rhs

        if rho > Fraction(1, 64):
            continue
        collar += 1

        star = max(q.values())
        triangle = max(
            sum(w[tuple(sorted(e))] for e in combinations(T, 2))
            for T in combinations(vertices, 3)
        )
        target = Fraction(47, 64)
        assert star >= target or triangle >= target
        margin = max(star, triangle) - target
        min_margin = margin if min_margin is None else min(min_margin, margin)

    print("QFORM_STAR_TRIANGLE_CHECK_PASS")
    print("denominator", N)
    print("all_edge_distributions", total)
    print("rho_le_1_over_64", collar)
    print("minimum_max_star_triangle_margin_over_47_64", min_margin)


if __name__ == "__main__":
    main()
