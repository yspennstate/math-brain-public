from fractions import Fraction
from itertools import combinations
import random
import math
import json


def walsh_coeffs(signs, n):
    N = 1 << n
    return [
        Fraction(
            sum(
                signs[x] * (-1 if ((x & S).bit_count() & 1) else 1)
                for x in range(N)
            ),
            N,
        )
        for S in range(N)
    ]


def dual_weight4_relations(n):
    N = 1 << n
    rels = []
    for A in combinations(range(N), 4):
        xr = 0
        for x in A:
            xr ^= x
        if xr == 0:
            rels.append(A)
    return rels


def frustrated(signs, A):
    z = 1
    for x in A:
        z *= signs[x]
    return z == -1


def finite_refund(p, T):
    vals = [float(x) for x in p]
    C = math.log(T + 1.0) - sum(x * math.log(T + x) for x in vals if x)
    H = -sum(x * math.log(x) for x in vals if x)
    HT = sum(x * math.log(1.0 + T / x) for x in vals if x) - math.log(1.0 + T)
    collision_defect = 1.0 - sum(x * x for x in vals)
    return C, H, HT, collision_defect


def main():
    stats = {}
    assertions = 0
    max_refund_ratio = 0.0
    max_identity_err = 0.0
    rng = random.Random(20260921)

    for n in range(2, 5):
        N = 1 << n
        rels = dual_weight4_relations(n)
        gauss = (N - 1) * (N - 2) // 6
        assert len(rels) == (N // 4) * gauss
        assertions += 1

        if n <= 3:
            funcs = [
                [(-1 if (mask >> x) & 1 else 1) for x in range(N)]
                for mask in range(1 << N)
            ]
        else:
            funcs = [
                [rng.choice([-1, 1]) for _ in range(N)]
                for _ in range(400)
            ]

        plaquette_checks = 0
        for signs in funcs:
            wh = walsh_coeffs(signs, n)
            p = [a * a for a in wh]
            C4 = sum(frustrated(signs, A) for A in rels)

            lhs = Fraction(C4, N ** 3)
            rhs = (Fraction(1) - sum((x * x for x in p), Fraction(0))) / 48
            assert lhs == rhs
            assertions += 1

            C, H, HT, collision_defect = finite_refund(p, 2.0)
            err = abs(HT - (H - C))
            max_identity_err = max(max_identity_err, err)
            assert err < 3e-13
            assert C >= -3e-14
            assert C <= collision_defect / 2.0 + 3e-13
            assertions += 3
            if collision_defect > 1e-15:
                max_refund_ratio = max(max_refund_ratio, C / collision_defect)

            for i in range(n):
                ei = 1 << i
                for w in range(1, N):
                    if w & ei:
                        continue
                    for y in range(N):
                        eta_y = signs[y] != signs[y ^ ei]
                        eta_yw = signs[y ^ w] != signs[y ^ w ^ ei]
                        A = (y, y ^ ei, y ^ w, y ^ w ^ ei)
                        assert len(set(A)) == 4
                        assert frustrated(signs, A) == (eta_y != eta_yw)
                        plaquette_checks += 1
                        assertions += 1

        signs = [-1] + [1] * (N - 1)
        C4_total = sum(frustrated(signs, A) for A in rels)
        assert C4_total == gauss

        coord_unique = set()
        for i in range(n):
            ei = 1 << i
            for w in range(1, N):
                if w & ei:
                    continue
                coord_unique.add(tuple(sorted((0, ei, w, ei ^ w))))

        coord_formula = n * (2 ** (n - 1) - 1) - n * (n - 1) // 2
        assert len(coord_unique) == coord_formula
        assertions += 2

        stats[str(n)] = {
            "N": N,
            "weight4_dual_relations": len(rels),
            "functions_checked": len(funcs),
            "plaquette_identity_checks": plaquette_checks,
            "one_point_frustrated_weight4_total": C4_total,
            "one_point_coordinate_aligned_unique": len(coord_unique),
            "coordinate_aligned_fraction": float(Fraction(len(coord_unique), C4_total)),
        }

    out = {
        "status": "PASS",
        "exact_and_numeric_assertions": assertions,
        "max_finite_resolvent_identity_error": max_identity_err,
        "max_C2_over_collision_defect_observed": max_refund_ratio,
        "stats": stats,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
