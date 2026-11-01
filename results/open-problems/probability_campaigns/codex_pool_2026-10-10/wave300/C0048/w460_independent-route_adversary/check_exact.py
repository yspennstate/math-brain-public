"""Bounded exact checks for the C0048 independent reduction; no store access.

Run: python -X utf8 check_exact.py
All arithmetic for finite graph identities is rational. These checks support
an audit; they are not a proof of the infinite-volume conjecture.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import math
import time

ROOT = Path(__file__).resolve().parent
START = time.monotonic()
CPU_START = time.process_time()


def gate():
    if time.process_time() - CPU_START > 10:
        raise RuntimeError("Fresh compute gate exceeded: 10 CPU seconds")
    if time.monotonic() - START > 120:
        raise RuntimeError("Fresh compute gate exceeded: 120 wall seconds")


def clusters(vertices, edges, bits, wired=()):
    parent = list(range(vertices))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        parent[find(a)] = find(b)

    for v in wired[1:]:
        union(wired[0], v)
    for i, (a, b) in enumerate(edges):
        if bits & (1 << i):
            union(a, b)
    return len({find(a) for a in range(vertices)})


def fk(vertices, edges, q, p, wired=()):
    weights = []
    for bits in range(1 << len(edges)):
        o = bits.bit_count()
        k = clusters(vertices, edges, bits, wired)
        # Fixed-color boundary cluster has weight 1, all other clusters q.
        k -= bool(wired)
        weights.append(p**o * (1-p)**(len(edges)-o) * q**k)
    z = sum(weights)
    return [w/z for w in weights]


def edge_marginals(masses, m):
    return [sum(w for bits, w in enumerate(masses) if bits & (1 << i))
            for i in range(m)]


def spin_equalities(vertices, edges, q, boltzmann_equal, fixed):
    variable = [v for v in range(vertices) if v not in fixed]
    z = 0
    scores = [0] * len(edges)
    for colors in product(range(q), repeat=len(variable)):
        sigma = dict(fixed)
        sigma.update(zip(variable, colors))
        equal = [sigma[a] == sigma[b] for a, b in edges]
        w = boltzmann_equal**sum(equal)
        z += w
        for i in range(len(edges)):
            scores[i] += w * equal[i]
    return [Q(s, z) for s in scores]


def logsum(a, b):
    z = max(a, b)
    return z + math.log(math.exp(a-z) + math.exp(b-z))


def main():
    square = [(0, 1), (1, 2), (2, 3), (3, 0)]
    p = Q(1, 2)
    mu = fk(4, square, 3, p)
    nu = fk(4, square, 3, p, (0, 2))
    emu = edge_marginals(mu, 4)
    enu = edge_marginals(nu, 4)
    smu = spin_equalities(4, square, 3, 2, {})
    snu = spin_equalities(4, square, 3, 2, {0: 0, 2: 0})
    assert emu == [Q(11, 43)] * 4
    assert enu == [Q(1, 3)] * 4
    assert all(emu[i]/p == smu[i] for i in range(4))
    assert all(enu[i]/p == snu[i] for i in range(4))
    bound = sum(enu[i]-emu[i] for i in range(4))

    # Enumerate every increasing event on the 4-edge configuration lattice.
    principal = [sum(1 << d for d in range(16) if (d & c) == c)
                 for c in range(16)]
    events = 0
    max_gap = Q(0)
    for event in range(1 << 16):
        if event % 4096 == 0:
            gate()
        if any(event & (1 << c) and event & principal[c] != principal[c]
               for c in range(16)):
            continue
        gap = sum(nu[c]-mu[c] for c in range(16) if event & (1 << c))
        assert 0 <= gap <= bound
        max_gap = max(max_gap, gap)
        events += 1
    assert events == 168
    assert max_gap == Q(275, 1548)

    # Verify the disappearing finite-volume gap by independent enumeration.
    path_cases = 0
    path_evidence = []
    for q, p, length in product((2, 3, 5), (Q(1, 4), Q(1, 2), Q(3, 4)),
                                (1, 2, 4, 8)):
        gate()
        edges = [(i, i+1) for i in range(length)]
        m0 = edge_marginals(fk(length+1, edges, q, p), length)[0]
        m1 = edge_marginals(fk(length+1, edges, q, p, (0, length)), length)[0]
        alpha = p / (p + q*(1-p))
        predicted = (q-1)*(1-alpha)*alpha**length / (1+(q-1)*alpha**length)
        assert m0 == alpha and m1-m0 == predicted and predicted > 0
        path_cases += 1
        if q == 3 and p == Q(1, 2):
            path_evidence.append({"length": length, "gap_exact": str(predicted),
                                  "gap_decimal": float(predicted)})
    for length in (16, 32):
        alpha = Q(1, 4)
        gap = 2*(1-alpha)*alpha**length/(1+2*alpha**length)
        path_evidence.append({"length": length, "gap_exact": str(gap),
                              "gap_decimal": float(gap), "method": "closed form"})

    # Boundary-pressure counterexample: independent finite-state energy sums.
    df = Q(2, 3)
    dg = Q(4, 3)
    assert dg-df == Q(2, 3)
    boundary_cases = 0
    for n, t in product((1, 2, 10, 100, 1000), (-1, -.1, 0, .1, 1)):
        f = logsum(2*n*t, math.log(2))/n
        g = logsum(math.log(2)+2*n*t, 0)/n
        assert abs(f-g) <= math.log(2)/n + 1e-12
        boundary_cases += 1
    gate()
    result = {
        "target": "C0048", "command": "python -X utf8 check_exact.py",
        "result": "PASS", "failures": 0,
        "compute_gate": {"cores": 1, "max_cpu_seconds": 10,
                         "max_wall_seconds": 120, "gpu": False,
                         "max_enumerated_edges": 8},
        "square": {"fk_configurations_per_boundary": 16,
                   "spin_configurations_free": 81, "spin_configurations_wired": 9,
                   "edge_marginal_free": str(emu[0]),
                   "edge_marginal_wired": str(enu[0]),
                   "edge_gap": str(enu[0]-emu[0]),
                   "equal_spin_free": str(smu[0]), "equal_spin_wired": str(snu[0]),
                   "ES_identities_checked": 8,
                   "increasing_events_checked": events,
                   "max_event_gap": str(max_gap), "L1_bound": str(bound)},
        "path": {"enumeration_cases_checked": path_cases, "q3_p_half": path_evidence},
        "boundary_pressure": {"cases_checked": boundary_cases,
                              "pressure_difference_bound": "log(2)/n",
                              "derivative_gap_exact": str(dg-df)},
        "baseline_shortcuts_refuted": [
            "positive finite-volume wired/free gap implies positive limiting gap",
            "uniformly vanishing pressure difference implies vanishing derivative difference"],
        "proof_limit": "Finite rational checks and a constructed counterexample; not an infinite-volume Potts proof.",
        "elapsed_seconds": round(time.monotonic()-START, 6),
        "cpu_seconds": round(time.process_time()-CPU_START, 6)
    }
    (ROOT/'measurements.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
