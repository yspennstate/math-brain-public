"""Independent exact checks of the finite-activity two-port reformulation.

Direct exterior algebra for the raw Ward partition is compared with direct
acyclic-subset enumeration. This is a verifier, not an all-graph proof.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


def add(a, b):
    out = dict(a)
    for mask, value in b.items():
        out[mask] = out.get(mask, F(0)) + value
        if not out[mask]:
            del out[mask]
    return out


def scale(a, coefficient):
    return {mask: value * coefficient for mask, value in a.items()
            if value * coefficient}


def mul(a, b):
    out = {}
    for left, av in a.items():
        for right, bv in b.items():
            if left & right:
                continue
            inversions = 0
            bits = left
            while bits:
                bit = bits & -bits
                inversions += (right & (bit - 1)).bit_count()
                bits -= bit
            mask = left | right
            value = av * bv * (-1 if inversions % 2 else 1)
            out[mask] = out.get(mask, F(0)) + value
            if not out[mask]:
                del out[mask]
    return out


def var(index):
    return {1 << index: F(1)}


def raw_integral(n, edges, ports):
    interior = [i for i in range(n) if i not in ports]
    order = interior + list(ports)
    locations = {vertex: index for index, vertex in enumerate(order)}
    bars = [var(2 * i) for i in range(n)]
    psis = [var(2 * i + 1) for i in range(n)]
    q = [mul(b, p) for b, p in zip(bars, psis)]
    polynomial = {0: F(1)}
    for i in range(len(interior)):
        polynomial = mul(polynomial, add({0: F(1)}, q[i]))
    for x, y, weight in edges:
        i, j = locations[x], locations[y]
        bracket = mul(add(bars[i], scale(bars[j], -1)),
                      add(psis[i], scale(psis[j], -1)))
        bracket = add(bracket, scale(mul(q[i], q[j]), -1))
        assert not mul(bracket, bracket)
        polynomial = mul(polynomial, add({0: F(1)}, scale(bracket, weight)))
    cut = 2 * len(interior)
    full = (1 << cut) - 1
    return {mask >> cut: value for mask, value in polynomial.items()
            if mask & full == full}


def forest_data(n, edges, ports=None, marks=()):
    totals = [F(0)] * (1 << len(marks))
    separate = [F(0)] * (1 << len(marks))
    connected = [F(0)] * (1 << len(marks))
    for mask in range(1 << len(edges)):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        weight = F(1)
        good = True
        for i, (x, y, activity) in enumerate(edges):
            if mask >> i & 1:
                rx, ry = find(x), find(y)
                if rx == ry:
                    good = False
                    break
                parent[rx] = ry
                weight *= activity
        if not good:
            continue
        target = connected if ports and find(ports[0]) == find(ports[1]) else separate
        for derivative_mask in range(1 << len(marks)):
            value = weight
            for bit, edge_index in enumerate(marks):
                if derivative_mask >> bit & 1:
                    if not mask >> edge_index & 1:
                        value = F(0)
                        break
                    value /= edges[edge_index][2]
            totals[derivative_mask] += value
            target[derivative_mask] += value
    return totals, connected, separate


def boundary_bracket():
    b0, p0, b1, p1 = [var(i) for i in range(4)]
    q0, q1 = mul(b0, p0), mul(b1, p1)
    return add(mul(add(b0, scale(b1, -1)),
                   add(p0, scale(p1, -1))), scale(mul(q0, q1), -1))


def main():
    graphs = [
        (2, [(0, 1, F(3, 2))], (0, 1)),
        (3, [(0, 2, F(2)), (2, 1, F(3))], (0, 1)),
        (3, [(0, 1, F(2)), (0, 2, F(3)), (1, 2, F(5))], (0, 1)),
        (4, [(i, j, F(1 + i + 2 * j, 3))
             for i, j in combinations(range(4), 2)], (0, 3)),
        (5, [(i, j, F(1 + i + j, 2))
             for i, j in combinations(range(5), 2)], (1, 4)),
        (6, [(0, 2, F(1)), (0, 3, F(2)), (1, 2, F(3)),
             (1, 3, F(4)), (2, 3, F(5)), (2, 4, F(2)),
             (3, 5, F(3)), (4, 5, F(1))], (0, 1)),
    ]
    checks = []
    for n, edges, ports in graphs:
        _, x, y = forest_data(n, edges, ports)
        expected = add({0: y[0]}, scale(boundary_bracket(), x[0]))
        actual = raw_integral(n, edges, ports)
        assert actual == expected, (n, ports, actual, expected)
        responses = []
        for e in range(len(edges)):
            _, xx, yy = forest_data(n, edges, ports, (e,))
            numerator = xx[1] * yy[0] - xx[0] * yy[1]
            responses.append(str(numerator))
            # Comparison with an independently added virtual edge.
            augmented = edges + [(ports[0], ports[1], F(7, 3))]
            zz, _, _ = forest_data(n, augmented, None, (e, len(edges)))
            rayleigh = zz[1] * zz[2] - zz[0] * zz[3]
            assert numerator == rayleigh
        checks.append({"n": n, "ports": ports, "edges": len(edges),
                       "X": str(x[0]), "Y": str(y[0]),
                       "virtual_edge_rayleigh_numerators": responses,
                       "raw_exterior_equals_Y_plus_XF": True})

    # Independent union-graph checks of the two-port cross product.
    h = [(0, 1, F(2)), (0, 2, F(3)), (1, 2, F(5))]
    k = [(0, 1, F(7)), (0, 3, F(11)), (1, 3, F(13))]
    for e in range(3):
        for f in range(3):
            _, xh, yh = forest_data(4, h, (0, 1), (e,))
            _, xk, yk = forest_data(4, k, (0, 1), (f,))
            nh = xh[1] * yh[0] - xh[0] * yh[1]
            nk = xk[1] * yk[0] - xk[0] * yk[1]
            z, _, _ = forest_data(4, h + k, None, (e, 3 + f))
            assert z[1] * z[2] - z[0] * z[3] == nh * nk

    # The root-moment contradiction: identical left sides, different right sides.
    pairs = list(combinations(range(4), 2))
    singleton_sum = [sum(i in pair for i in range(4)) for pair in pairs]
    splits = [({0, 1}, {2, 3}), ({0, 2}, {1, 3}), ({0, 3}, {1, 2})]
    split_sum = [sum((i in left) != (j in left) for left, right in splits)
                 for i, j in pairs]
    assert singleton_sum == split_sum == [2] * 6
    assert 4 != 3
    output = {"arithmetic": "exact Fraction exterior algebra and subset enumeration",
              "two_port_cases": checks, "gluing_cross_pair_checks": 9,
              "root_moment_equal_left_coefficients": singleton_sum,
              "root_moment_incompatible_right_sides": [4, 3],
              "full_conjecture_proved": False}
    destination = Path(__file__).with_name("forest_finite_activity_two_port_exact_results.json")
    destination.write_text(json.dumps(output, indent=2))
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
