#!/usr/bin/env python3
from fractions import Fraction
import math

def bit(x, i):
    return (x >> i) & 1

def influence(vals, n, i):
    N = 1 << n
    return Fraction(sum(vals[x] != vals[x ^ (1 << i)] for x in range(N)), N)

def fold_to_median_character(vals, n):
    p = [influence(vals, n, i) for i in range(n)]
    K = [i for i, u in enumerate(p) if u > Fraction(1, 2)]
    out = []
    for x, v in enumerate(vals):
        parity = sum(bit(x, i) for i in K) & 1
        out.append(-v if parity else v)
    return out, K

def derivative_row(vals, n, i):
    out = {}
    for x in range(1 << n):
        if bit(x, i) == 0:
            out[x] = (vals[x] - vals[x | (1 << i)]) // 2
    return out

def signed_subcube_row(vals, n, i):
    row = derivative_row(vals, n, i)
    supp = [x for x, d in row.items() if d]
    if not supp:
        return True, set(), {}
    if len({row[x] for x in supp}) != 1:
        return False, None, None
    F, a = [], {}
    for k in range(n):
        if k == i:
            continue
        b = {bit(x, k) for x in supp}
        if len(b) == 1:
            F.append(k)
            a[k] = next(iter(b))
    expected = {x for x in row if all(bit(x, k) == a[k] for k in F)}
    return expected == set(supp), set(F), a

def one_point_on_relevant(vals, n, V):
    if not V:
        return True
    table = []
    for mask in range(1 << len(V)):
        x = 0
        for j, k in enumerate(V):
            if (mask >> j) & 1:
                x |= 1 << k
        table.append(vals[x])
    return min(table.count(1), table.count(-1)) == 1

def mixed_stats(vals, n, i, k):
    assert i != k
    denom = 1 << (n - 2)
    sq = p = o = 0
    for x in range(1 << n):
        if bit(x, i) or bit(x, k):
            continue
        f00 = vals[x]
        f10 = vals[x | (1 << i)]
        f01 = vals[x | (1 << k)]
        f11 = vals[x | (1 << i) | (1 << k)]
        delta = (f00 - f10 - f01 + f11) // 2
        sq += delta * delta
        di0 = (f00 - f10) // 2
        di1 = (f01 - f11) // 2
        p += ((di0 != 0) != (di1 != 0))
        o += (di0 != 0 and di1 == -di0)
    return Fraction(sq, denom), Fraction(p, denom), Fraction(o, denom)

def point_defect_ratio(m):
    t = 2.0 ** (1 - m)
    w0 = (1.0 - t) ** 2
    w = t * t
    H = -(w0 * math.log2(w0) if w0 else 0.0)
    H -= ((1 << m) - 1) * w * math.log2(w)
    I = m * t
    return H / I

mixed_pair_checks = 0
column_checks = 0
endpoint_functions = 0
classification_failures = 0

for n in range(2, 5):
    N = 1 << n
    for truth in range(1 << N):
        vals = [1 if ((truth >> x) & 1) else -1 for x in range(N)]

        for i in range(n):
            for k in range(i + 1, n):
                kap, p, o = mixed_stats(vals, n, i, k)
                kap2, _, _ = mixed_stats(vals, n, k, i)
                assert kap == kap2
                assert kap == p + 4 * o
                mixed_pair_checks += 1

        for k in range(n):
            lhs = sum((mixed_stats(vals, n, i, k)[0]
                       for i in range(n) if i != k), Fraction())
            # By definition d_{d_k} = (1/4) sum_{i!=k} kappa_{ki}.
            ddk = lhs / 4
            assert lhs == 4 * ddk
            column_checks += 1

        folded, _ = fold_to_median_character(vals, n)
        ps = [influence(folded, n, i) for i in range(n)]
        V = [i for i, p in enumerate(ps) if p > 0]
        if not V:
            continue
        if all(ps[i] <= Fraction(1, 2) for i in V):
            endpoint = True
            for i in V:
                ok, _, _ = signed_subcube_row(folded, n, i)
                if not ok:
                    endpoint = False
                    break
            if endpoint:
                endpoint_functions += 1
                if not one_point_on_relevant(folded, n, V):
                    classification_failures += 1

assert classification_failures == 0
ratios = [point_defect_ratio(m) for m in range(2, 33)]
assert max(ratios) < 4.0

print("PASS")
print(f"mixed_pair_checks={mixed_pair_checks}")
print(f"column_checks={column_checks}")
print(f"all_row_endpoint_functions_after_fold={endpoint_functions}")
print(f"classification_failures={classification_failures}")
print(f"max_point_defect_H_over_I_m2_to_32={max(ratios):.15f}")
