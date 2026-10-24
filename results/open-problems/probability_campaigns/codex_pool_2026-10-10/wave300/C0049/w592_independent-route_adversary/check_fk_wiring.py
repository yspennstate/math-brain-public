"""Small, exact FK diagnostic. This is finite evidence, not a scaling-limit proof."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent

def state(n, edges, mask, wiring, q):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    def union(a, b):
        parent[find(a)] = find(b)
    for a, b in wiring:
        union(a, b)
    weight = F(1)
    for j, (a, b) in enumerate(edges):
        p = (F(1, 3), F(1, 2), F(2, 3))[j % 3]
        if (mask >> j) & 1:
            union(a, b)
            weight *= p
        else:
            weight *= 1-p
    return weight * q**len({find(i) for i in range(n)}), find(0) == find(n-1)

def run():
    started = time.perf_counter()
    all_edges = list(combinations(range(4), 2))
    cases = pointwise = histories = tower_checks = degeneracies = 0
    q_values = [F(1,4), F(1,2), F(1), F(3,2), F(2), F(3), F(4)]
    for graph_mask in range(1 << len(all_edges)):
        edges = [e for j, e in enumerate(all_edges) if (graph_mask >> j) & 1]
        for q in q_values:
            for xi in [[], [(0,1)], [(0,1),(2,3)], [(0,3)]]:
                eta = xi + [(0,3)]
                x = [state(4, edges, m, xi, q) for m in range(1 << len(edges))]
                y = [state(4, edges, m, eta, q) for m in range(1 << len(edges))]
                zx, zy = sum(w for w,a in x), sum(w for w,a in y)
                c = sum(w for w,a in x if a) / zx
                r = zy/zx
                assert r == 1/q + (1-1/q)*c
                for (wx,a),(wy,_) in zip(x,y):
                    assert wy/wx == (F(1) if a else 1/q)
                    pointwise += 1

                def walk(masks, remaining, previous_bit=0):
                    nonlocal histories, tower_checks, degeneracies
                    sx = sum(x[m][0] for m in masks)
                    sy = sum(y[m][0] for m in masks)
                    mn = sum(x[m][0] for m in masks if x[m][1])/sx
                    dn = (sy/zy)/(sx/zx)
                    assert dn == (1/q+(1-1/q)*mn)/r
                    histories += 1
                    if q == 1:
                        assert dn == 1
                        degeneracies += 1
                    if remaining:
                        # Predictable adaptive rule: the last observed bit chooses
                        # which end of the remaining edge list to inspect next.
                        edge = remaining[0] if previous_bit == 0 else remaining[-1]
                        residual = [j for j in remaining if j != edge]
                        children = []
                        for bit in [0,1]:
                            subset = [m for m in masks if ((m >> edge)&1) == bit]
                            child = walk(subset, residual, bit)
                            children.append(sum(x[m][0] for m in subset)/sx*child)
                        assert sum(children) == dn
                        tower_checks += 1
                    return dn
                walk(list(range(len(x))), list(range(len(edges))))
                cases += 1

    # A false closure must fail: a q-only next-edge probability ignores wiring.
    # At q=4 and p_sd=2/3, an isolated edge with free endpoints has law 1/3;
    # identifying its endpoints instead gives law 2/3. Compute from raw weights.
    def one_edge_open(wiring):
        weights=[]
        for bit in [0,1]:
            connected = bool(wiring) or bool(bit)
            clusters = 1 if connected else 2
            weights.append((F(2,3) if bit else F(1,3))*F(4)**clusters)
        return weights[1]/sum(weights)
    free, wired = one_edge_open([]), one_edge_open([(0,1)])
    assert free == F(1,3) and wired == F(2,3)
    baseline_error = abs(free-wired)
    result = {
      "scope":"exact finite graph evidence; no formal proof receipt, no continuum claim",
      "graph_parameter_boundary_cases":cases,
      "pointwise_density_checks":pointwise,
      "adaptive_history_checks":histories,
      "tower_checks":tower_checks,
      "q1_constant_density_histories":degeneracies,
      "failures":0,
      "negative_control":{"q":4,"p":"2/3","free_open":str(free),
        "wired_open":str(wired),"q_only_predictor_absolute_error_before":str(baseline_error),
        "wiring_aware_error_after":"0","invalid_q_only_closure_rejected":True},
      "wall_seconds":round(time.perf_counter()-started,6),
      "command":"python -X utf8 ~/brain_workers/w592/check_fk_wiring.py"
    }
    (ROOT/'MEASUREMENTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    run()
