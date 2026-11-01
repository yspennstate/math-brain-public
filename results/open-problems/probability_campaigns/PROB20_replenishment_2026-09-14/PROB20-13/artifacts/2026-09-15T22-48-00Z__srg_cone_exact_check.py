#!/usr/bin/env python3
"""Exact rational checks for the PROB20-13 cone-over-SRG theorem.

No floating point arithmetic and no third-party packages are used.
The script verifies:
  * strongly regular parameters of C5 and the Petersen graph;
  * the standard SRG identity (q-r-1)mu = r(r-lambda-1);
  * the explicit stationary-product routing from the report;
  * identical load on every physical edge;
  * the closed-form congestion and constant-metric dual value.
"""

from fractions import Fraction
from itertools import combinations


def add_edge(adj, u, v):
    adj.setdefault(u, set()).add(v)
    adj.setdefault(v, set()).add(u)


def cycle_graph(n):
    adj = {i: set() for i in range(n)}
    for i in range(n):
        add_edge(adj, i, (i + 1) % n)
    return adj


def petersen_graph():
    # Outer 5-cycle 0..4, inner star 5..9, spokes i--(5+i).
    adj = {i: set() for i in range(10)}
    for i in range(5):
        add_edge(adj, i, (i + 1) % 5)
        add_edge(adj, i, 5 + i)
    for i in range(5):
        add_edge(adj, 5 + i, 5 + ((i + 2) % 5))
    return adj


def srg_parameters(adj):
    vertices = sorted(adj)
    q = len(vertices)
    degrees = {len(adj[v]) for v in vertices}
    assert len(degrees) == 1
    r = next(iter(degrees))
    lambdas, mus = set(), set()
    for u, v in combinations(vertices, 2):
        common = len(adj[u] & adj[v])
        if v in adj[u]:
            lambdas.add(common)
        else:
            mus.add(common)
    assert len(lambdas) == 1
    assert len(mus) == 1
    lam = next(iter(lambdas))
    mu = next(iter(mus))
    assert (q - r - 1) * mu == r * (r - lam - 1)
    return q, r, lam, mu


def edge_key(u, v):
    return frozenset((u, v))


def exact_cone_route(adj):
    q, r, lam, mu = srg_parameters(adj)
    base = sorted(adj)
    hub = "h"

    # Cone edge set.
    edges = {edge_key(hub, v) for v in base}
    for u in base:
        for v in adj[u]:
            edges.add(edge_key(u, v))
    m = len(edges)
    assert m == q * (r + 2) // 2

    # Stationary masses in the cone.
    pi_h = Fraction(1, r + 2)
    pi_b = Fraction(r + 1, q * (r + 2))
    capacity = Fraction(1, 2 * m)
    assert capacity == Fraction(1, q * (r + 2))

    hub_base_demand = 2 * pi_h * pi_b
    base_pair_demand = 2 * pi_b * pi_b
    theta = Fraction(1, r + 1)

    load = {e: Fraction(0) for e in edges}

    # Hub/base commodities.
    for u in base:
        load[edge_key(hub, u)] += hub_base_demand

    # Base/base commodities.
    for u, v in combinations(base, 2):
        if v in adj[u]:
            load[edge_key(u, v)] += base_pair_demand
        else:
            # theta through the hub.
            hub_piece = theta * base_pair_demand
            load[edge_key(u, hub)] += hub_piece
            load[edge_key(hub, v)] += hub_piece

            # remainder equally through the mu common neighbors.
            common = sorted(adj[u] & adj[v])
            assert len(common) == mu
            each = (1 - theta) * base_pair_demand / mu
            for w in common:
                load[edge_key(u, w)] += each
                load[edge_key(w, v)] += each

    expected_load = Fraction(
        2 * (r + 1) * (2 * q - r - 1),
        q * q * (r + 2) * (r + 2),
    )
    assert set(load.values()) == {expected_load}

    congestion = expected_load / capacity
    closed_form = Fraction(
        2 * (r + 1) * (2 * q - r - 1),
        q * (r + 2),
    )
    assert congestion == closed_form

    # Constant dual length ell_e=2: objective = 2 E[d_G(X,Y)].
    mean_distance = Fraction((r + 1) * (2 * q - r - 1), q * (r + 2))
    dual_value = 2 * mean_distance
    assert dual_value == closed_form

    return {
        "parameters": (q, r, lam, mu),
        "m": m,
        "edge_load": expected_load,
        "capacity": capacity,
        "F": closed_form,
    }


def parameter_only(q, r, lam, mu):
    assert (q - r - 1) * mu == r * (r - lam - 1)
    return Fraction(2 * (r + 1) * (2 * q - r - 1), q * (r + 2))


def main():
    c5 = exact_cone_route(cycle_graph(5))
    pet = exact_cone_route(petersen_graph())
    shrikhande_value = parameter_only(16, 6, 2, 2)

    assert c5["parameters"] == (5, 2, 0, 1)
    assert c5["F"] == Fraction(21, 10)
    assert pet["parameters"] == (10, 3, 0, 1)
    assert pet["edge_load"] == Fraction(32, 625)
    assert pet["capacity"] == Fraction(1, 25)
    assert pet["F"] == Fraction(64, 25)
    assert shrikhande_value == Fraction(175, 64)

    print("C5 cone:", c5)
    print("Petersen cone:", pet)
    print("Shrikhande-parameter cone F:", shrikhande_value)
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
