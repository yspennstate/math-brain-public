"""Independent exact generator-kernel audit of finite FA-1f chains.

Spin 1 is filled; spin 0 facilitates. No submitted code/data are used.
The state-space matrix is explicitly built, transposed, and row-reduced over Q
by SymPy. Graph reachability and bootstrap closures are checked separately.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1",
                  VECLIB_MAXIMUM_THREADS="1", NUMEXPR_NUM_THREADS="1")
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import resource
import time
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def graph(length, width, periodic, h_cycle=False):
    coords = [(x, y) for x in range(length) for y in range(width)]
    idx = {xy: i for i, xy in enumerate(coords)}
    neighbors, exterior = [], []
    for x, y in coords:
        adjacent, outside = set(), []
        for dx in (-1, 1):
            nx = x + dx
            if periodic:
                nx %= length
            if 0 <= nx < length:
                adjacent.add(idx[nx, y])
            else:
                outside.append((nx, y))
        for dy in (-1, 1):
            ny = y + dy
            if h_cycle and width >= 3:
                ny %= width
            if 0 <= ny < width:
                adjacent.add(idx[x, ny])
        adjacent.discard(idx[x, y])
        neighbors.append(sorted(adjacent))
        exterior.append(outside)
    return coords, neighbors, exterior

def solve(length, width, boundary, q, h_cycle=False):
    periodic = boundary == "periodic"
    coords, neighbors, exterior = graph(length, width, periodic, h_cycle)
    size, a, b = len(coords), q.numerator, q.denominator
    count = 1 << size
    filled = count - 1

    def fixed_vacancy(xy):
        x, y = xy
        return boundary == "empty" or (boundary == "left_seed" and x == -1 and y == 0) or (
            boundary == "alternating" and (x + y) % 2 == 0)

    external_active = [any(fixed_vacancy(xy) for xy in ext) for ext in exterior]

    def allowed(state, site):
        return external_active[site] or any(not (state >> j) & 1 for j in neighbors[site])

    # M = b Q with conventional row-source generator Q.
    M = sp.zeros(count, count)
    legal_neighbors = [[] for _ in range(count)]
    for state in range(count):
        for site in range(size):
            if allowed(state, site):
                dest = state ^ (1 << site)
                rate = a if (state >> site) & 1 else b - a
                M[state, dest] = rate
                M[state, state] -= rate
                legal_neighbors[state].append(dest)
    assert all(sum(M[i, j] for j in range(count)) == 0 for i in range(count))
    kernel = M.T.nullspace()

    # Components computed by search, independently of the linear solver.
    unseen, components = set(range(count)), []
    while unseen:
        start = min(unseen)
        component, todo = {start}, [start]
        unseen.remove(start)
        while todo:
            state = todo.pop()
            for dest in legal_neighbors[state]:
                assert state in legal_neighbors[dest]
                if dest in unseen:
                    unseen.remove(dest)
                    component.add(dest)
                    todo.append(dest)
        components.append(sorted(component))

    def closure(state):
        while True:
            deletions = [i for i in range(size) if (state >> i) & 1 and allowed(state, i)]
            if not deletions:
                return state
            for i in deletions:
                state &= ~(1 << i)

    fibers = {}
    for state in range(count):
        fibers.setdefault(closure(state), []).append(state)
    assert sorted(components) == sorted(fibers.values())
    assert len(kernel) == len(components)
    assert len(components) == (1 if any(external_active) else 2)
    weights = [a ** (size - s.bit_count()) * (b - a) ** s.bit_count() for s in range(count)]
    normalizers = [sum(weights[s] for s in c) for c in components]
    laws = []
    for component, z in zip(components, normalizers):
        law = sp.zeros(count, 1)
        for state in component:
            law[state] = sp.Rational(weights[state], z)
        assert M.T * law == sp.zeros(count, 1)
        assert sum(law) == 1 and min(law) >= 0
        laws.append(law)
    # Every independently obtained kernel basis vector has constant density
    # relative to the product weights on each communicating class.
    for vector in kernel:
        for component in components:
            start = component[0]
            assert all(vector[s] * weights[start] == vector[start] * weights[s] for s in component)
    for i in range(count):
        for j in legal_neighbors[i]:
            assert weights[i] * M[i, j] == weights[j] * M[j, i]

    active_law = next(law for law, c in zip(laws, components) if 0 in c)
    expected = [Fraction(weights[s], b ** size - (b - a) ** size) if s != filled else Fraction(0)
                for s in range(count)] if len(components) == 2 else [Fraction(w, b ** size) for w in weights]
    assert all(Fraction(active_law[s]) == expected[s] for s in range(count))
    return {"length": length, "width": width, "H": "cycle" if h_cycle else "path", "boundary": boundary,
            "q": str(q), "states": count, "kernel_dimension": len(kernel),
            "rank": count - len(kernel), "class_sizes": list(map(len, components)),
            "bp_values": list(fibers), "class_normalizers": normalizers,
            "active_vacancy_marginal": str(sum(Fraction(active_law[s]) for s in range(count) if not s & 1)),
            "laws": [[str(v) for v in law] for law in laws],
            "exact_generator_residual": 0, "kernel_basis_density_check": True,
            "detailed_balance_checked": True}

def main():
    started = time.monotonic()
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    cases = [(3,1), (4,1), (5,1), (3,2), (2,3)]
    results = []
    for length, width in cases:
        for boundary in ("periodic", "filled", "empty", "left_seed", "alternating"):
            for q in (Fraction(1,3), Fraction(2,5)):
                result = solve(length, width, boundary, q)
                results.append(result)
                print(f"{length}x{width} {boundary} q={q}: rank={result['rank']}, classes={result['class_sizes']}", flush=True)
    for length, width, h_cycle in [(4,2,False), (3,3,True)]:
        result = solve(length, width, "periodic", Fraction(5,7), h_cycle)
        results.append(result)
        print(f"{length}x{width} periodic H={'cycle' if h_cycle else 'path'}: rank={result['rank']}", flush=True)
    summary = {"cases": len(results), "max_states": max(r['states'] for r in results),
               "nice": os.getpriority(os.PRIO_PROCESS, 0), "numerical_threads": 1,
               "elapsed_seconds": time.monotonic() - started,
               "peak_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "all_exact_checks_passed": True}
    data = ROOT / "data"
    data.mkdir(exist_ok=True)
    (data / "independent_fa1_results.json").write_text(json.dumps({"summary": summary, "results": results}, indent=2) + "\n")
    print(json.dumps(summary), flush=True)

if __name__ == "__main__":
    main()
