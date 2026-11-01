"""Bounded direct Walsh checks and closed-form diagnostics; no external writes."""
import json
import math
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GATE = {"max_direct_core_dimension": 10, "max_truth_table_entries": 2048,
        "closed_form_dimensions": list(range(4, 42, 2)), "max_wall_seconds": 55,
        "no_gpu": True, "no_training": True, "no_exhaustive_function_search": True}

def entropy(coefficients):
    return math.fsum(-a*a*math.log2(a*a) for a in coefficients if a)

def walsh(values):
    a = list(map(float, values))
    width = 1
    while width < len(a):
        for start in range(0, len(a), 2*width):
            for offset in range(width):
                i, j = start+offset, start+offset+width
                u, v = a[i], a[j]
                a[i], a[j] = u+v, u-v
        width *= 2
    return [v/len(a) for v in a]

def core_value(bits, n):
    # bit 0 represents x=+1, bit 1 x=-1; each pair is negative only at 11.
    return -1 if sum(((bits >> j) & 3) == 3 for j in range(0,n,2)) % 2 else 1

def closed(n):
    r, p = 2.0**(-n/2), 2.0**(-n)
    def phi_delta(v):
        return (1+v)**2 * 2*math.log1p(v)/math.log(2)
    def L(u):
        return math.fsum([(1+r)/2*phi_delta(-u*r), (1-r)/2*phi_delta(u*r)])
    gap = n*p + L(2)/2 - L(1)
    total_influence = n/2 + (n+1)*p
    return {"core_n": n, "variables": n+1, "I_t": p, "delta_t": gap,
            "delta_t_over_I_t": gap/p, "convexity_lower_bound": n,
            "H_F": n*(1+p)-L(1), "I_F": total_influence,
            "H_F_over_I_F": (n*(1+p)-L(1))/total_influence}

def direct(n):
    size = 1 << n
    assert 2*size <= GATE["max_truth_table_entries"]
    g = [core_value(x,n) for x in range(size)]
    h = list(g)
    h[0] *= -1
    f = g+h
    assert all(v in (-1,1) for v in f)
    ag, ah, af = walsh(g), walsh(h), walsh(f)
    p = 1/size
    err = max(abs(af[s]-(ag[s]-p)) for s in range(size))
    err = max(err, max(abs(af[size+s]-p) for s in range(size)))
    assert err < 1e-13
    assert abs(math.fsum(a*a for a in af)-1) < 1e-13
    influences = [math.fsum(af[s]**2 for s in range(2*size) if s & (1<<i)) for i in range(n+1)]
    edge_influences = [sum(f[x]!=f[x^(1<<i)] for x in range(2*size))/(2*size) for i in range(n+1)]
    assert influences == edge_influences
    assert influences[-1] == p
    assert all(v == .5+p for v in influences[:-1])
    gap = entropy(af)-(entropy(ag)+entropy(ah))/2
    expected = closed(n)
    assert abs(gap-expected["delta_t"]) < 2e-13
    assert gap/p >= n-1e-11
    # Demonstrate quantifier scope by checking a core coordinate too.
    plus = [f[x] for x in range(2*size) if not x&1]
    minus = [f[x] for x in range(2*size) if x&1]
    good_gap = entropy(af)-(entropy(walsh(plus))+entropy(walsh(minus)))/2
    return {**expected, "direct_gap": gap, "coefficient_max_error": err,
            "core_coordinate_increment_ratio": good_gap/influences[0],
            "truth_table_entries": len(f)}

def main():
    started = time.perf_counter()
    rows = [direct(n) for n in (4,6,8,10)]
    formulas = [closed(n) for n in GATE["closed_form_dimensions"]]
    assert all(r["delta_t_over_I_t"] >= r["core_n"]-1e-6 for r in formulas)
    elapsed = time.perf_counter()-started
    assert elapsed < GATE["max_wall_seconds"]
    result = {"gate": GATE, "direct_rows": rows, "closed_form_rows": formulas,
              "wall_seconds": elapsed, "status": "numerical checks passed; analytic proof requires referee"}
    (ROOT/"bent_selector_measurements.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"direct_dimensions": [r["core_n"] for r in rows],
                      "bad_coordinate_ratios": [r["delta_t_over_I_t"] for r in rows],
                      "good_coordinate_ratios": [r["core_coordinate_increment_ratio"] for r in rows],
                      "ratio_at_n40": formulas[-1]["delta_t_over_I_t"], "seconds": elapsed}))

if __name__ == "__main__":
    main()
