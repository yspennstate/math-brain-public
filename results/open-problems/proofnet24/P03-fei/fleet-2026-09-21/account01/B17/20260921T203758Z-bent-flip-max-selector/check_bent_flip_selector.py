#!/usr/bin/env python3
import json, math

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def b_ratio(n):
    assert n >= 2 and n % 2 == 0
    q = 2.0**(-n)
    s = math.sqrt(q)
    B = 0.0
    for eps in (1.0, -1.0):
        multiplicity = (1.0/q + eps/s)/2.0
        w = q*(1.0 - 2.0*eps*s + 2.0*q)
        t = q/(1.0 - 2.0*eps*s + 2.0*q)
        B += multiplicity*w*h2(t)
    return B/q

def raw_activation_ratio(n):
    D = n+1
    z = 1.0 - 1.0/D
    return ((1.0+z)/2.0)**n

rows=[]
for n in range(2, 22, 2):
    q=2.0**(-n)
    tdepth=n+1
    leaf_upper=2.0**(-tdepth)
    diluted_activation_lower=1.0-2.0**(-(tdepth+1))
    Br=b_ratio(n)
    depth_ratio=n/2.0
    depth_bridge_rhs_ratio=2.0*depth_ratio+math.log2(math.e)
    row={
        'n': n,
        'q': q,
        'B_over_q': Br,
        'depth_over_q': depth_ratio,
        'depth_bridge_rhs_over_q': depth_bridge_rhs_ratio,
        'depth_bridge_gap_over_q': depth_bridge_rhs_ratio-Br,
        'asymptotic_n_plus_log2e': n+math.log2(math.e),
        'raw_dimension_cooling_A_over_q': raw_activation_ratio(n),
        'dilution_depth_t': tdepth,
        'leaf_influence_upper': leaf_upper,
        'x_unique_max_from_upper_bound': leaf_upper < q,
        'diluted_dimension_cooling_A_over_q_lower_bound': diluted_activation_lower,
    }
    assert row['x_unique_max_from_upper_bound']
    assert row['depth_bridge_gap_over_q'] >= -1e-12
    rows.append(row)

assert abs(rows[-1]['B_over_q']-rows[-1]['asymptotic_n_plus_log2e']) < 1e-5
assert rows[-1]['B_over_q'] > 21.44
assert rows[-1]['diluted_dimension_cooling_A_over_q_lower_bound'] > 0.999999
assert rows[-1]['depth_bridge_gap_over_q'] < 1e-5

out={
    'status':'PASS',
    'claim_scope':'exact Boolean unique-maximum activation-only selector adversary plus sharp local depth bridge; not a counterexample to FEI',
    'family':'quadratic bent background plus one-point flip, followed by balanced recursive-majority substitution',
    'rows':rows,
}
print(json.dumps(out, indent=2, sort_keys=True))
