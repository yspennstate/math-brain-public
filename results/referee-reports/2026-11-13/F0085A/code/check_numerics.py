"""Independent small-instance checks for allocation and periodic components."""
from collections import deque
import json
import numpy as np
from torus_allocation import Preferences, allocate, audit_stability, sites_for, components

def greedy_reference(centres, sites, L, quota):
    delta = np.abs(centres[:, None, :] - sites[None, :, :])
    delta = np.minimum(delta, L - delta)
    ds = np.einsum("ijk,ijk->ij", delta, delta)
    order = np.argsort(ds.ravel(), kind="stable")
    owner = np.full(len(sites), -1, dtype=int)
    held = np.zeros(len(centres), dtype=int)
    for edge in order:
        c, s = divmod(int(edge), len(sites))
        if owner[s] == -1 and held[c] < quota:
            owner[s] = c
            held[c] += 1
    return owner

def bfs_components(mask, connectivity):
    n = len(mask)
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if connectivity == 8:
        steps += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    seen = {}
    largest, wind = 0, np.zeros(2, dtype=bool)
    for y in range(n):
        for x in range(n):
            if not mask[y, x] or (y, x) in seen:
                continue
            queue = deque([(y, x)])
            seen[y, x] = np.array([0, 0])
            size = 0
            while queue:
                u = queue.popleft()
                size += 1
                for dy, dx in steps:
                    v = ((u[0] + dy) % n, (u[1] + dx) % n)
                    if not mask[v]:
                        continue
                    lift = seen[u] + [dx, dy]
                    if v in seen:
                        wind |= lift != seen[v]
                    else:
                        seen[v] = lift
                        queue.append(v)
            largest = max(size, largest)
    return largest, tuple(wind.astype(int))

def main():
    rng = np.random.default_rng(8501)
    allocation_cases = 0
    for nc in (1, 4, 11, 27):
        sites, n = sites_for(4, 4)
        centres = rng.uniform(0, 4, (nc, 2))
        pref = Preferences(centres, sites, 4, 3)  # force list expansion
        for quota in (1, 5, 15, 80):
            owner, distance, held, _ = allocate(pref, quota)
            ref = greedy_reference(centres, sites, 4, quota)
            assert np.array_equal(owner, ref), (nc, quota)
            audit_stability(pref, quota, owner, distance, held)
            allocation_cases += 1
    component_cases = 0
    for n in (3, 5, 11):
        masks = [np.zeros((n, n), bool), np.ones((n, n), bool), np.eye(n, dtype=bool)]
        for p in (.1, .3, .5, .7, .9):
            masks += [rng.random((n, n)) < p for _ in range(20)]
        for mask in masks:
            for conn in (4, 8):
                actual = components(mask, conn)
                size, wind = bfs_components(mask, conn)
                assert actual["largest"] == size, (n, conn, actual, size)
                assert (actual["wrap_x"], actual["wrap_y"]) == wind, (n, conn, actual, wind)
                component_cases += 1
    print(json.dumps({"allocation_cases_against_global_edge_reference": allocation_cases,
                      "periodic_component_cases_against_lifted_BFS": component_cases,
                      "status": "passed"}, indent=2))

if __name__ == "__main__":
    main()
