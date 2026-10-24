#!/usr/bin/env python3
import math, json

TOL = 2e-10

def fwht(vals):
    a = [float(x) for x in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    z = float(len(a))
    return [x/z for x in a]

def entropy(ps):
    return sum(-p*math.log2(p) for p in ps if p > 0.0)

def spectrum_from_values(vals):
    c = fwht(vals)
    return [x*x for x in c]

def spectrum_from_mask(n, mask):
    vals = [1.0 if ((mask >> x) & 1) else -1.0 for x in range(1 << n)]
    return spectrum_from_values(vals)

def prefix_metrics(p, n):
    N = 1 << n
    size = [x.bit_count() for x in range(N)]
    v = [0.0] * N
    for S, ps in enumerate(p):
        if ps == 0.0:
            continue
        k = size[S]
        A = S
        while True:
            a = size[A]
            v[A] += ps / math.comb(k, a)
            if A == 0:
                break
            A = (A - 1) & S

    H = entropy(p)
    I = sum(size[S] * p[S] for S in range(N))
    root = 0.0
    p0 = p[0]
    t0 = 1.0 - p0
    if 0.0 < p0 < 1.0:
        root += -p0*math.log2(p0) - t0*math.log2(t0)
    if t0 > TOL:
        root += t0 * entropy([v[1 << i] / t0 for i in range(n)])

    stop = 0.0
    deletion = 0.0
    edge_marginal = [0.0] * n
    max_conservation_error = 0.0

    for A in range(1, N):
        va = v[A]
        if va <= TOL:
            continue
        a = size[A]
        pa = p[A]
        t = va - pa
        q = pa / va
        if 0.0 < q < 1.0:
            stop += va * (-q*math.log2(q) - (1-q)*math.log2(1-q))
        if t > TOL:
            edge_sum = 0.0
            g = 0.0
            for i in range(n):
                if (A >> i) & 1:
                    continue
                B = A | (1 << i)
                e = v[B] / (a + 1)
                edge_sum += e
                edge_marginal[i] += e
                if e > TOL:
                    g += e * math.log2(t / v[B])
            max_conservation_error = max(max_conservation_error, abs(edge_sum - t))
            deletion += g

    marginal_error = 0.0
    for i in range(n):
        ji = sum(p[S] for S in range(N) if (S >> i) & 1)
        marginal_error = max(marginal_error,
                             abs(edge_marginal[i] - (ji - v[1 << i])))

    tail_error = 0.0
    for a in range(n+1):
        lhs = sum(v[A] for A in range(N) if size[A] == a)
        rhs = sum(p[S] for S in range(N) if size[S] >= a)
        tail_error = max(tail_error, abs(lhs-rhs))

    return {
        "H": H, "I": I, "root": root, "stop": stop, "deletion": deletion,
        "equality_error": abs(H - (root + stop + deletion)),
        "conservation_error": max_conservation_error,
        "deep_edge_marginal_error": marginal_error,
        "tail_error": tail_error
    }

def controlled_majority_values(m):
    n = m + 1
    vals = []
    for x in range(1 << n):
        x0 = 1.0 if (x & 1) else -1.0
        sy = sum(1 if ((x >> (k+1)) & 1) else -1 for k in range(m))
        M = 1.0 if sy > 0 else -1.0
        g = (1.0 + M) / 2.0
        vals.append(1.0 - g + x0*g)
    return vals

def main():
    totals = {
        "boolean_functions_mod_global_sign": 0,
        "max_equality_error": 0.0,
        "max_conservation_error": 0.0,
        "max_deep_edge_marginal_error": 0.0,
        "max_tail_error": 0.0,
        "max_stop_over_I": 0.0,
        "max_deletion_over_I": -1e100,
        "max_root_over_I": 0.0,
        "max_H_over_I": 0.0,
    }
    per_n = {}
    for n in range(1, 5):
        rows = 0
        mx = {"root_I":0.0, "stop_I":0.0, "deletion_I":-1e100, "H_I":0.0}
        for mask in range(0, 1 << (1 << n), 2):
            r = prefix_metrics(spectrum_from_mask(n, mask), n)
            if r["I"] <= TOL:
                continue
            rows += 1
            totals["boolean_functions_mod_global_sign"] += 1
            totals["max_equality_error"] = max(totals["max_equality_error"], r["equality_error"])
            totals["max_conservation_error"] = max(totals["max_conservation_error"], r["conservation_error"])
            totals["max_deep_edge_marginal_error"] = max(totals["max_deep_edge_marginal_error"], r["deep_edge_marginal_error"])
            totals["max_tail_error"] = max(totals["max_tail_error"], r["tail_error"])
            for key, val in [("root_I", r["root"]/r["I"]),
                             ("stop_I", r["stop"]/r["I"]),
                             ("deletion_I", r["deletion"]/r["I"]),
                             ("H_I", r["H"]/r["I"])]:
                mx[key] = max(mx[key], val)
            totals["max_stop_over_I"] = max(totals["max_stop_over_I"], r["stop"]/r["I"])
            totals["max_deletion_over_I"] = max(totals["max_deletion_over_I"], r["deletion"]/r["I"])
            totals["max_root_over_I"] = max(totals["max_root_over_I"], r["root"]/r["I"])
            totals["max_H_over_I"] = max(totals["max_H_over_I"], r["H"]/r["I"])
            if r["stop"] > r["I"] + 1e-9:
                raise AssertionError(("stop>I", n, mask, r))
        per_n[str(n)] = {"tested": rows, **mx}

    controlled = []
    for m in (3,5,7,9):
        n = m+1
        r = prefix_metrics(spectrum_from_values(controlled_majority_values(m)), n)
        controlled.append({
            "m": m, "I": r["I"], "H_over_I": r["H"]/r["I"],
            "root_over_I": r["root"]/r["I"],
            "stop_over_I": r["stop"]/r["I"],
            "deletion_over_I": r["deletion"]/r["I"],
            "equality_error": r["equality_error"]
        })

    if max(totals["max_equality_error"], totals["max_conservation_error"],
           totals["max_deep_edge_marginal_error"], totals["max_tail_error"]) > 1e-8:
        raise AssertionError(totals)

    print(json.dumps({"status":"PASS", "totals":totals, "per_n":per_n,
                      "controlled_majority":controlled}, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
