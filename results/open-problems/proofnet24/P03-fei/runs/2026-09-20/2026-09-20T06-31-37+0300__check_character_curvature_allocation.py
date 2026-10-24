#!/usr/bin/env python3
import json, math, random
from functools import lru_cache
from math import log2, log, sqrt, e, comb

C_CHI = 2.0 + 1.0/(sqrt(e)*log(2.0))
INV_LN2 = 1.0/log(2.0)
TOL = 2e-11

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*log2(p) - (1.0-p)*log2(1.0-p)

def fwht(vals):
    a = [float(x) for x in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    inv = 1.0/n
    return tuple(x*inv for x in a)

def restrict(vals, i, bit):
    N = len(vals)
    n = N.bit_length()-1
    out = []
    for m in range(1 << (n-1)):
        low = m & ((1 << i)-1)
        high = m >> i
        full = low | (bit << i) | (high << (i+1))
        out.append(vals[full])
    return tuple(out)

@lru_cache(None)
def metrics(vals):
    a = fwht(vals)
    p = tuple(x*x for x in a)
    n = len(vals).bit_length()-1
    H = sum(-q*log2(q) for q in p if q > 0.0)
    infl = tuple(sum(q for s,q in enumerate(p) if (s >> i) & 1)
                 for i in range(n))
    I = sum(infl)
    J = sum(min(x, 1.0-x) for x in infl)
    kappa = 1.0-max(p)
    return H, I, J, kappa, infl, p

def B_i(vals, i):
    p = metrics(vals)[5]
    total = 0.0
    for s in range(len(p)):
        if ((s >> i) & 1) == 0:
            a, b = p[s], p[s | (1 << i)]
            m = a+b
            if m > 0.0:
                total += m*h2(b/m)
    return total

def derivative(vals, i):
    g = restrict(vals, i, 0)
    h = restrict(vals, i, 1)
    return tuple(a*b for a,b in zip(g,h))

def curvature2(vals):
    n = len(vals).bit_length()-1
    # Each square {i,k} is counted in I(D_i f) and I(D_k f).
    return 0.5*sum(metrics(derivative(vals,i))[1] for i in range(n))

@lru_cache(None)
def adaptive_tree_charges(vals):
    n = len(vals).bit_length()-1
    if n == 0:
        return (0.0, 0.0)
    # Function-dependent selector: this is deliberately adaptive.
    neg = sum(v < 0 for v in vals)
    i = (neg+n) % n
    inf = metrics(vals)[4][i]
    j = min(inf, 1.0-inf)
    local_curv = metrics(derivative(vals,i))[1]
    g = restrict(vals,i,0)
    h = restrict(vals,i,1)
    cg,jg = adaptive_tree_charges(g)
    ch,jh = adaptive_tree_charges(h)
    return (local_curv + 0.5*(cg+ch),
            j + 0.5*(jg+jh))

def majority_vals(n):
    assert n % 2 == 1
    # bit 0 represents +1 and bit 1 represents -1
    return tuple(1 if x.bit_count() <= n//2 else -1 for x in range(1 << n))

stats = {
    "status": "PASS",
    "constant_C_chi": C_CHI,
    "exhaustive_coordinate_cases": 0,
    "exhaustive_by_dimension": {},
    "max_raw_character_defect_violation": -1e100,
    "max_truncated_character_defect_violation": -1e100,
    "max_kappa_minus_J_violation": -1e100,
    "max_local_curvature_violation": -1e100,
    "max_global_curvature_FEI_violation": -1e100,
    "max_adaptive_curvature_telescope_error": 0.0,
    "max_adaptive_folded_budget_excess": -1e100,
    "largest_strict_Jmin_minus_kappamin_gap": 0.0,
}

# Exhaust every Boolean truth table through n=4.
for n in range(1,5):
    N = 1 << n
    local_count = 0
    for mask in range(1 << N):
        vals = tuple(-1 if (mask >> x) & 1 else 1 for x in range(N))
        H,I,J,kappa,infs,p = metrics(vals)
        C2 = curvature2(vals)
        stats["max_global_curvature_FEI_violation"] = max(
            stats["max_global_curvature_FEI_violation"],
            H - (0.5*C2 + 3.0*INV_LN2*J))
        treeC, treeJ = adaptive_tree_charges(vals)
        stats["max_adaptive_curvature_telescope_error"] = max(
            stats["max_adaptive_curvature_telescope_error"], abs(treeC-C2))
        stats["max_adaptive_folded_budget_excess"] = max(
            stats["max_adaptive_folded_budget_excess"], treeJ-J)

        for i in range(n):
            B = B_i(vals,i)
            inf = infs[i]
            j = min(inf,1.0-inf)
            g,h = restrict(vals,i,0), restrict(vals,i,1)
            kg,kh = metrics(g)[3],metrics(h)[3]
            Jg,Jh = metrics(g)[2],metrics(h)[2]
            km = min(kg,kh)

            stats["max_raw_character_defect_violation"] = max(
                stats["max_raw_character_defect_violation"],
                B-(C_CHI*j+km))
            residual = max(0.0,h2(j)-C_CHI*j)
            stats["max_truncated_character_defect_violation"] = max(
                stats["max_truncated_character_defect_violation"],
                B-(C_CHI*j+min(km,residual)))
            stats["max_kappa_minus_J_violation"] = max(
                stats["max_kappa_minus_J_violation"], kg-Jg, kh-Jh)
            stats["largest_strict_Jmin_minus_kappamin_gap"] = max(
                stats["largest_strict_Jmin_minus_kappamin_gap"],
                min(Jg,Jh)-km)

            dI = metrics(derivative(vals,i))[1]
            stats["max_local_curvature_violation"] = max(
                stats["max_local_curvature_violation"],
                B-(0.5*dI+INV_LN2*j))
            local_count += 1
    stats["exhaustive_by_dimension"][str(n)] = local_count
    stats["exhaustive_coordinate_cases"] += local_count

# Fixed-seed random stress tests in larger dimensions.
rng = random.Random(20260920)
random_plan = {5:1000, 6:500, 7:200}
random_coordinate_cases = 0
random_max_raw = -1e100
random_max_trunc = -1e100
random_max_curv = -1e100
for n,count in random_plan.items():
    N=1 << n
    for _ in range(count):
        vals=tuple(1 if rng.getrandbits(1) else -1 for _ in range(N))
        H,I,J,kappa,infs,p=metrics(vals)
        C2=curvature2(vals)
        random_max_curv=max(random_max_curv,
                            H-(0.5*C2+3.0*INV_LN2*J))
        for i in range(n):
            B=B_i(vals,i)
            inf=infs[i]; j=min(inf,1.0-inf)
            g,h=restrict(vals,i,0),restrict(vals,i,1)
            km=min(metrics(g)[3],metrics(h)[3])
            random_max_raw=max(random_max_raw,B-(C_CHI*j+km))
            residual=max(0.0,h2(j)-C_CHI*j)
            random_max_trunc=max(random_max_trunc,
                                 B-(C_CHI*j+min(km,residual)))
            dI=metrics(derivative(vals,i))[1]
            if B > 0.5*dI+INV_LN2*j+TOL:
                raise AssertionError(("random local curvature",n,i,B,dI,j))
            random_coordinate_cases += 1
stats["random_plan"] = random_plan
stats["random_coordinate_cases"] = random_coordinate_cases
stats["random_max_raw_character_defect_violation"] = random_max_raw
stats["random_max_truncated_character_defect_violation"] = random_max_trunc
stats["random_max_global_curvature_FEI_violation"] = random_max_curv

# Odd-majority obstruction to a nodewise character-defect selector.
majority = []
for n in (3,5,7,9,11,13,15):
    vals=majority_vals(n)
    delta=metrics(vals)[4][0]
    exact_delta=comb(n-1,(n-1)//2)/(2**(n-1))
    B=B_i(vals,0)
    g,h=restrict(vals,0,0),restrict(vals,0,1)
    kg,kh=metrics(g)[3],metrics(h)[3]
    max_child_atom=max(1.0-kg,1.0-kh)
    if abs(delta-exact_delta)>TOL:
        raise AssertionError(("majority influence formula",n,delta,exact_delta))
    if abs(B)>TOL:
        raise AssertionError(("majority B_i parity",n,B))
    if max_child_atom > delta+TOL:
        raise AssertionError(("majority child atom bound",n,max_child_atom,delta))
    majority.append({
        "n": n,
        "influence_delta": delta,
        "B_i": B,
        "min_child_kappa": min(kg,kh),
        "max_child_fourier_atom_mass": max_child_atom,
        "min_kappa_over_j": min(kg,kh)/delta
    })
stats["majority_obstruction"] = majority

# Analytic asymptotic stress marker without constructing the 101-bit truth table.
n=101
delta=comb(100,50)/(2**100)
stats["majority_n101_analytic"] = {
    "influence_delta": delta,
    "proved_min_kappa_over_j_lower_bound": (1.0-delta)/delta
}

# Hard pass/fail gates.
keys = [
    "max_raw_character_defect_violation",
    "max_truncated_character_defect_violation",
    "max_kappa_minus_J_violation",
    "max_local_curvature_violation",
    "max_global_curvature_FEI_violation",
    "max_adaptive_folded_budget_excess",
    "random_max_raw_character_defect_violation",
    "random_max_truncated_character_defect_violation",
    "random_max_global_curvature_FEI_violation",
]
if any(stats[k] > TOL for k in keys):
    stats["status"]="FAIL"
if stats["max_adaptive_curvature_telescope_error"] > TOL:
    stats["status"]="FAIL"

print(json.dumps(stats, indent=2, sort_keys=True))
