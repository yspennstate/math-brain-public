"""B15 exploratory checker for the global one-sided Fourier magnitude flow.

This script computes a new statistic
    A(f) = sum_i L_i(f),
where L_i is the one-sided Fourier magnitude-gradient cost used in the
restriction identity.  It does not prove FEI.

Checks:
1. Exhaustive maximum of A/I for Boolean functions through n=4.
2. Exact-hash reconstruction of the published 18-variable Numaro seed.
3. Influence-weighted aggregate recursion under balanced self-composition
   through depth 15, using the exact composition identity from the preceding
   B15 report.
4. Rare-tribes values from the exact closed formula already proved for L_i/I_i.
"""
from __future__ import annotations
import hashlib
import math
import numpy as np

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
 (TOP, BOT),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
 ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00",
  "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
 ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
 ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]

def fwht(a):
    a = np.asarray(a, dtype=np.int64).copy()
    h = 1
    while h < a.size:
        b = a.reshape(-1, 2*h)
        x = b[:, :h].copy()
        y = b[:, h:].copy()
        b[:, :h] = x + y
        b[:, h:] = x - y
        a = b.reshape(-1)
        h *= 2
    return a

def coeffs_from_truth(vals):
    vals = np.asarray(vals, dtype=np.int64)
    return fwht(vals).astype(np.float64) / vals.size

def coordinate_stats(coeff, i):
    bit = 1 << i
    low = np.arange(coeff.size, dtype=np.int64)
    low = low[(low & bit) == 0]
    u = np.abs(coeff[low])
    v = np.abs(coeff[low | bit])
    vv = v*v
    alpha = float(np.sum(vv))
    mask = (u > v) & (v > 0)
    L = float(np.sum(vv[mask] * np.log2(u[mask]/v[mask])))
    singleton = abs(float(coeff[bit]))
    return alpha, L, singleton, u, v

def aggregate_ratio(coeff):
    n = int(round(math.log2(coeff.size)))
    I = 0.0
    A = 0.0
    rel = []
    for i in range(n):
        alpha, L, _, _, _ = coordinate_stats(coeff, i)
        I += alpha
        A += L
        if alpha > 0:
            rel.append(L/alpha)
    return A/I if I else 0.0, min(rel) if rel else 0.0, I

def exhaustive_small():
    out = {}
    for n in range(1, 5):
        N = 1 << n
        best_agg = (-1.0, None)
        best_selector = (-1.0, None)
        for mask in range(1 << N):
            vals = np.array([1 if ((mask >> x) & 1) else -1 for x in range(N)],
                            dtype=np.int64)
            agg, selector, I = aggregate_ratio(coeffs_from_truth(vals))
            if I == 0:
                continue
            if agg > best_agg[0]:
                best_agg = (agg, mask)
            if selector > best_selector[0]:
                best_selector = (selector, mask)
        out[n] = {
            "max_A_over_I": best_agg[0],
            "argmax_truth_mask": best_agg[1],
            "max_min_L_over_Inf": best_selector[0],
            "selector_argmax_truth_mask": best_selector[1],
        }
    return out

def reconstruct_numaro():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    seen = base
    hosts = []
    for mask in masks:
        assert mask.bit_count() == 2 and not (seen & mask)
        seen |= mask
        hosts.append([x for x in range(512) if (mask >> x) & 1])
    core = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)],
                    dtype=np.int64)
    table = np.tile(core, (1 << 9, 1))
    for j, cells in enumerate(hosts):
        active = (np.arange(1 << 9) & (1 << j)) != 0
        table[np.ix_(active, np.array(cells, dtype=int))] = -1
    table = table.ravel()
    digest = hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()
    assert digest == EXPECTED_SHA
    assert int(table.sum()) == 0
    return table

def M_from_uv(u, v, q):
    mask = (u > 0) & (v > 0)
    return float(np.sum(v[mask]**2 *
                        np.maximum(0.0, np.log2(u[mask]/(v[mask]*q)))))

def numaro_aggregate(depth_max=15):
    table = reconstruct_numaro()
    coeff = coeffs_from_truth(table)
    classes = {"C": 0, "A": 9}
    stats = {}
    for name, i in classes.items():
        alpha, L, singleton, u, v = coordinate_stats(coeff, i)
        stats[name] = {
            "alpha": alpha, "L": L, "s": singleton, "u": u, "v": v,
            "ell": L/alpha
        }
    assert abs(stats["C"]["alpha"] - 57/256) < 1e-15
    assert abs(stats["C"]["s"] - 57/256) < 1e-15
    assert abs(stats["A"]["alpha"] - 1/256) < 1e-15
    assert abs(stats["A"]["s"] - 1/256) < 1e-15

    base_agg, base_selector, base_I = aggregate_ratio(coeff)
    states = {
        (1, 0): (9*stats["C"]["alpha"],
                 9*stats["C"]["alpha"]*stats["C"]["ell"]),
        (0, 1): (9*stats["A"]["alpha"],
                 9*stats["A"]["alpha"]*stats["A"]["ell"]),
    }
    rows = [{
        "depth": 1,
        "aggregate_L_over_I": sum(w for m,w in states.values()) /
                              sum(m for m,w in states.values())
    }]
    cache = {}
    for depth in range(2, depth_max+1):
        nd = {}
        for (nc, na), (mass, wrat) in states.items():
            q = stats["C"]["s"]**nc * stats["A"]["s"]**na
            p = stats["C"]["alpha"]**nc * stats["A"]["alpha"]**na
            z = q*q/p
            for name in ("C", "A"):
                st = stats[name]
                keym = (nc, na, name)
                if keym not in cache:
                    cache[keym] = M_from_uv(st["u"], st["v"], q)
                inc = z * cache[keym] / st["alpha"]
                factor = 9 * st["alpha"]
                key = (nc + (name == "C"), na + (name == "A"))
                m2 = mass * factor
                w2 = wrat * factor + m2 * inc
                if key in nd:
                    nd[key] = (nd[key][0] + m2, nd[key][1] + w2)
                else:
                    nd[key] = (m2, w2)
        states = nd
        rows.append({
            "depth": depth,
            "aggregate_L_over_I": sum(w for m,w in states.values()) /
                                  sum(m for m,w in states.values())
        })

    theta = max(st["s"]**2/st["alpha"] for st in stats.values())
    sstar = min(st["s"] for st in stats.values() if st["s"] > 0)
    ellstar = max(st["ell"] for st in stats.values())
    tail_bound = sum(theta**(d-1) *
                     ((d-1)*math.log2(1/sstar) + ellstar)
                     for d in range(depth_max+1, 1000))
    return {
        "truth_table_sha256": EXPECTED_SHA,
        "seed_A_over_I": base_agg,
        "seed_min_L_over_Inf": base_selector,
        "seed_I": base_I,
        "class_C_L_over_Inf": stats["C"]["ell"],
        "class_A_L_over_Inf": stats["A"]["ell"],
        "theta": theta,
        "sstar": sstar,
        "ellstar": ellstar,
        "depth_rows": rows,
        "analytic_uniform_tail_bound_after_depth_max": tail_bound,
    }

def rare_tribes_ratio(m, w):
    eps = 2.0**(-w)
    q = 1.0-eps
    c = abs(2*q**m-1)
    a1 = 2*eps*q**(m-1)
    term0 = 4*eps**2*q**(2*m-2)*max(0.0, math.log2(c/a1))
    Q = 2**w-1
    term1 = 4*eps**2*q**(m-1)*(1-q**(m-1))*math.log2(Q)
    inf = 2*eps*q**(m-1)
    return (term0+term1)/inf

def main():
    print("EXHAUSTIVE_SMALL")
    for n, row in exhaustive_small().items():
        print(n, row)
    print("NUMARO_AGGREGATE")
    nr = numaro_aggregate()
    for k, v in nr.items():
        if k != "depth_rows":
            print(k, v)
    for row in nr["depth_rows"]:
        print("depth", row["depth"], row["aggregate_L_over_I"])
    print("RARE_TRIBES")
    for a, w in [(1,12),(2,12),(3,12),(4,16),(6,18)]:
        m = 2**a+1
        print("a", a, "m", m, "w", w, "A_over_I_equals_L_over_Inf",
              rare_tribes_ratio(m,w))

if __name__ == "__main__":
    main()
