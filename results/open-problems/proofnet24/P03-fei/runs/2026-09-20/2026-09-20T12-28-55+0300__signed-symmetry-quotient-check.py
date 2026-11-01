#!/usr/bin/env python3
"""
P03 FEI signed-translation quotient checker.

Checks:
  (1) exhaustive Boolean functions through dimension 4 modulo global sign:
      full signed-translation symmetry space, RREF pivot tree, B_i=0 at every
      symmetry-pivot node, equal leaf/root Fourier entropy, and leaf influence
      <= root influence;
  (2) deterministic random oblique signed-symmetry lifts through dimension 8;
  (3) antipodal two-defect family: both previously available surcharge terms
      equal (n-1) times the queried influence while the true local allocation
      B_i is exactly zero (numerically and by spectral support parity).

This is a sanity checker, not an independent proof audit.
"""
import math, random, json
import numpy as np

SEED = 20260920
RNG = random.Random(SEED)

def fwht_int(vals):
    a = np.array(vals, dtype=np.int64).copy()
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            x = a[i:i+h].copy()
            y = a[i+h:i+2*h].copy()
            a[i:i+h] = x + y
            a[i+h:i+2*h] = x - y
        h *= 2
    return a

def fourier_entropy(vals):
    N = len(vals)
    w = fwht_int(vals)
    ans = 0.0
    for z in w:
        if z:
            p = (float(z)/N)**2
            ans -= p*math.log2(p)
    return ans

def total_influence(vals, n):
    if n == 0:
        return 0.0
    c = 0
    for i in range(n):
        bit = 1 << i
        for x in range(1 << n):
            if not (x & bit) and vals[x] != vals[x | bit]:
                c += 1
    return c / float(1 << (n-1))

def influence_i(vals, n, i):
    if n == 0:
        return 0.0
    bit = 1 << i
    c = 0
    for x in range(1 << n):
        if not (x & bit) and vals[x] != vals[x | bit]:
            c += 1
    return c / float(1 << (n-1))

def B_i(vals, n, i):
    if n == 0:
        return 0.0
    N = 1 << n
    w = fwht_int(vals)
    bit = 1 << i
    ans = 0.0
    for t in range(N):
        if t & bit:
            continue
        p0 = (float(w[t])/N)**2
        p1 = (float(w[t | bit])/N)**2
        if p0 and p1:
            s = p0 + p1
            x = p1/s
            ans += s * (-x*math.log2(x) - (1-x)*math.log2(1-x))
    return ans

def signed_symmetry_vectors(vals, n):
    """Return (v,lambda(v)) for all v with f(x+v)=(-1)^lambda f(x)."""
    N = 1 << n
    out = []
    for v in range(N):
        sign = vals[v] * vals[0]
        ok = True
        for x in range(N):
            if vals[x ^ v] != sign * vals[x]:
                ok = False
                break
        if ok:
            out.append((v, 0 if sign == 1 else 1))
    return out

def rref_basis_with_pivots(vectors, n):
    rows = sorted(set(v for v in vectors if v))
    rank = 0
    pivots = []
    for col in range(n):
        idx = None
        for j in range(rank, len(rows)):
            if (rows[j] >> col) & 1:
                idx = j
                break
        if idx is None:
            continue
        rows[rank], rows[idx] = rows[idx], rows[rank]
        pivot = rows[rank]
        for j in range(len(rows)):
            if j != rank and ((rows[j] >> col) & 1):
                rows[j] ^= pivot
        pivots.append(col)
        rank += 1
        if rank == len(rows):
            break
    return rows[:rank], pivots

def restrict_general(vals, n, fixed):
    rem = [i for i in range(n) if i not in fixed]
    out = np.empty(1 << len(rem), dtype=np.int8)
    for y in range(1 << len(rem)):
        x = 0
        for i, b in fixed.items():
            x |= b << i
        for k, i in enumerate(rem):
            if (y >> k) & 1:
                x |= 1 << i
        out[y] = vals[x]
    return out, rem

def check_pivot_tree(vals, n, pivots):
    max_B = 0.0
    nodes = 0
    frontier = [dict()]
    for p in pivots:
        nxt = []
        for fixed in frontier:
            arr, rem = restrict_general(vals, n, fixed)
            local_i = rem.index(p)
            max_B = max(max_B, B_i(arr, len(rem), local_i))
            nodes += 1
            for b in (0, 1):
                ff = dict(fixed)
                ff[p] = b
                nxt.append(ff)
        frontier = nxt
    H0 = fourier_entropy(vals)
    I0 = total_influence(vals, n)
    max_Hdiff = 0.0
    max_Iexcess = 0.0
    for fixed in frontier:
        arr, rem = restrict_general(vals, n, fixed)
        max_Hdiff = max(max_Hdiff, abs(fourier_entropy(arr) - H0))
        max_Iexcess = max(max_Iexcess, total_influence(arr, len(rem)) - I0)
    return nodes, max_B, max_Hdiff, max_Iexcess

def parity(x):
    return x.bit_count() & 1

def make_oblique_lift(r, m):
    """f(y,z)=(-1)^{a.y} g(z+M y), with random M and arbitrary g."""
    n = r + m
    a = RNG.randrange(1 << r)
    rows = [RNG.randrange(1 << m) for _ in range(r)]
    g = np.array([1 if RNG.randrange(2) == 0 else -1 for _ in range(1 << m)], dtype=np.int8)
    vals = np.empty(1 << n, dtype=np.int8)
    for x in range(1 << n):
        y = x & ((1 << r) - 1)
        z = x >> r
        shift = 0
        for j in range(r):
            if (y >> j) & 1:
                shift ^= rows[j]
        vals[x] = (-1 if parity(a & y) else 1) * g[z ^ shift]
    V = [(1 << j) | (rows[j] << r) for j in range(r)]
    return vals, n, V

def child(vals, n, i, bitval):
    out, rem = restrict_general(vals, n, {i: bitval})
    return out

def derivative(vals, n, i):
    return child(vals, n, i, 0) * child(vals, n, i, 1)

def antipodal(n):
    vals = np.ones(1 << n, dtype=np.int8)
    vals[0] = -1
    vals[(1 << n) - 1] = -1
    return vals

stats = {
    "seed": SEED,
    "exhaustive_functions_mod_global_sign": 0,
    "exhaustive_functions_with_nontrivial_signed_symmetry": 0,
    "exhaustive_symmetry_pivot_nodes": 0,
    "max_zero_allocation_B": 0.0,
    "max_leaf_root_entropy_difference": 0.0,
    "max_leaf_influence_minus_root": 0.0,
    "oblique_lift_cases": 0,
    "oblique_pivot_nodes": 0,
    "antipodal_cases": 0,
    "max_antipodal_B": 0.0,
    "max_antipodal_formula_error": 0.0,
}

for n in range(1, 5):
    N = 1 << n
    for mask in range(1 << (N-1)):
        vals = np.ones(N, dtype=np.int8)
        for x in range(1, N):
            if (mask >> (x-1)) & 1:
                vals[x] = -1
        syms = signed_symmetry_vectors(vals, n)
        rows, pivots = rref_basis_with_pivots([v for v, _ in syms], n)
        nodes, mb, mh, mi = check_pivot_tree(vals, n, pivots)
        stats["exhaustive_functions_mod_global_sign"] += 1
        if rows:
            stats["exhaustive_functions_with_nontrivial_signed_symmetry"] += 1
        stats["exhaustive_symmetry_pivot_nodes"] += nodes
        stats["max_zero_allocation_B"] = max(stats["max_zero_allocation_B"], mb)
        stats["max_leaf_root_entropy_difference"] = max(stats["max_leaf_root_entropy_difference"], mh)
        stats["max_leaf_influence_minus_root"] = max(stats["max_leaf_influence_minus_root"], mi)

for _ in range(1500):
    n = RNG.randint(5, 8)
    r = RNG.randint(1, min(3, n-1))
    m = n-r
    vals, n, V = make_oblique_lift(r, m)
    rows, pivots = rref_basis_with_pivots(V, n)
    assert len(rows) == r
    nodes, mb, mh, mi = check_pivot_tree(vals, n, pivots)
    stats["oblique_lift_cases"] += 1
    stats["oblique_pivot_nodes"] += nodes
    stats["max_zero_allocation_B"] = max(stats["max_zero_allocation_B"], mb)
    stats["max_leaf_root_entropy_difference"] = max(stats["max_leaf_root_entropy_difference"], mh)
    stats["max_leaf_influence_minus_root"] = max(stats["max_leaf_influence_minus_root"], mi)

antipodal_rows = []
for n in range(3, 15):
    vals = antipodal(n)
    i = 0
    alpha = influence_i(vals, n, i)
    g0 = child(vals, n, i, 0)
    g1 = child(vals, n, i, 1)
    minor = min(total_influence(g0, n-1), total_influence(g1, n-1))
    curv = 0.5 * total_influence(derivative(vals, n, i), n-1)
    B = B_i(vals, n, i)
    expected_alpha = 2.0**(2-n)
    expected_surcharge = (n-1)*expected_alpha
    err = max(abs(alpha-expected_alpha), abs(minor-expected_surcharge), abs(curv-expected_surcharge))
    stats["antipodal_cases"] += 1
    stats["max_antipodal_B"] = max(stats["max_antipodal_B"], B)
    stats["max_antipodal_formula_error"] = max(stats["max_antipodal_formula_error"], err)
    antipodal_rows.append({
        "n": n,
        "B_i": B,
        "alpha_i": alpha,
        "minor_child_I_over_alpha": minor/alpha,
        "half_derivative_I_over_alpha": curv/alpha,
        "H_over_I": fourier_entropy(vals)/total_influence(vals, n),
    })

tol = 2e-12
status = "PASS"
assert stats["max_zero_allocation_B"] <= tol
assert stats["max_leaf_root_entropy_difference"] <= tol
assert stats["max_leaf_influence_minus_root"] <= tol
assert stats["max_antipodal_B"] <= tol
assert stats["max_antipodal_formula_error"] <= tol

print(json.dumps({"status": status, "stats": stats, "antipodal": antipodal_rows}, indent=2, sort_keys=True))
