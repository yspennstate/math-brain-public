"""Worker 056: exact determinantal-entropy resolvent and modular certificates.

Run with Python 3; the standard library suffices.  All matrix, atom, and
derivative checks use fractions.  Logarithm signs and displayed Hessians use
rational intervals from the atanh series, with a proved remainder bound.
There is no random sampling, finite differencing, or numerical integration.
The output is written next to this file, to 056_resolvent_certificate.json.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def add(a, b, scale=F(1)):
    return [[x + scale * y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]


def scale(a, c):
    return [[c*x for x in row] for row in a]


def mul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def sub(a, subset):
    return [[a[i][j] for j in subset] for i in subset]


def det(a):
    n = len(a)
    total = F(0)
    for perm in permutations(range(n)):
        value = F((-1)**sum(perm[i] > perm[j]
                            for i in range(n) for j in range(i+1, n)))
        for i, j in enumerate(perm):
            value *= a[i][j]
        total += value
    return total


def inv(a):
    n = len(a)
    z = [row[:] + erow for row, erow in zip(a, eye(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if z[i][j])
        z[pivot], z[j] = z[j], z[pivot]
        factor = z[j][j]
        z[j] = [x/factor for x in z[j]]
        for i in range(n):
            if i != j:
                factor = z[i][j]
                z[i] = [x-factor*y for x, y in zip(z[i], z[j])]
    return [row[n:] for row in z]


def positive_definite(a):
    return all(det(sub(a, list(range(j)))) > 0
               for j in range(1, len(a)+1))


def det_jet(a, direction):
    n = len(a)
    out = []
    for order in range(3):
        value = F(0)
        for cols in combinations(range(n), order):
            mixed = [[(direction if j in cols else a)[i][j]
                      for j in range(n)] for i in range(n)]
            value += det(mixed)
        out.append(value*(2 if order == 2 else 1))
    return out


def isum(items):
    items = list(items)
    return tuple(sum((p[j] for p in items), F(0)) for j in range(2))


def iscale(c, pair):
    a, b = pair
    return (c*a, c*b) if c >= 0 else (c*b, c*a)


def log_unit(q, terms=70):
    assert 1 <= q <= 2
    x = (q-1)/(q+1)
    lo = 2*sum((x**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    err = 2*x**(2*terms+1)/(F(2*terms+1)*(1-x*x))
    return lo, lo+err


def log_interval(q):
    assert q > 0
    exponent = 0
    while q < 1:
        q *= 2
        exponent -= 1
    while q >= 2:
        q /= 2
        exponent += 1
    return isum([log_unit(q), iscale(exponent, log_unit(F(2)))])


def rounded_interval(pair):
    grid = 10**12
    lo = F(pair[0].numerator*grid // pair[0].denominator, grid)
    hi = F(-((-pair[1].numerator*grid) // pair[1].denominator), grid)
    assert lo <= pair[0] <= pair[1] <= hi
    return {"lower_exact": str(lo), "upper_exact": str(hi),
            "lower_decimal": float(lo), "upper_decimal": float(hi)}


def atom_jet(kernel, direction):
    n = len(kernel)
    ident = eye(n)
    complement = add(ident, kernel, -1)
    r = inv(complement)
    l = add(r, ident, -1)
    b = mul(mul(r, direction), r)
    c = mul(mul(b, complement), b)  # L'' / 2, never discarded.
    gamma = tr(mul(mul(complement, b), mul(complement, b)))
    assert c == mul(mul(mul(mul(r, direction), r), direction), r)
    atoms = []
    for mask in range(1 << n):
        subset = [i for i in range(n) if mask & (1 << i)]
        mixed = [[(kernel if j in subset else complement)[i][j]
                  for j in range(n)] for i in range(n)]
        d_mixed = [[direction[i][j]*(1 if j in subset else -1)
                    for j in range(n)] for i in range(n)]
        p, dp, ddp = det_jet(mixed, d_mixed)
        assert p > 0 and p == det(sub(l, subset))/det(r)
        z = [[F(0) for _ in range(n)] for _ in range(n)]
        if subset:
            local_inverse = inv(sub(l, subset))
            for i, row in enumerate(subset):
                for j, col in enumerate(subset):
                    z[row][col] = local_inverse[i][j]
        delta = add(z, complement, -1)
        delta_b = mul(delta, b)
        score = tr(delta_b)
        kappa = tr(mul(delta_b, delta_b))
        tau = score**2-kappa
        acceleration_atom = tr(mul(z, c))
        # Independently expanded log-atom Hessian, including +2 tr(Z C).
        log_atom_hessian = (2*acceleration_atom
                            - tr(mul(mul(z, b), mul(z, b))) - gamma)
        assert dp == p*score
        assert ddp == p*tau
        assert log_atom_hessian == -kappa
        atoms.append({"S": subset, "p": p, "dp": dp, "ddp": ddp,
                      "score": score, "kappa": kappa, "tau": tau,
                      "acceleration_atom": acceleration_atom})
    fisher = sum((a["dp"]**2/a["p"] for a in atoms), F(0))
    assert sum(a["p"] for a in atoms) == 1
    assert sum(a["dp"] for a in atoms) == 0
    assert sum(a["ddp"] for a in atoms) == 0
    assert sum(a["p"]*a["kappa"] for a in atoms) == fisher
    for i in range(n):
        assert sum(a["p"] for a in atoms if i in a["S"]) == kernel[i][i]
        assert sum(a["dp"] for a in atoms if i in a["S"]) == direction[i][i]
        assert sum(a["ddp"] for a in atoms if i in a["S"]) == 0
    curvature = isum(iscale(-a["ddp"], log_interval(a["p"])) for a in atoms)
    hessian = isum([(-fisher, -fisher), curvature])
    mean_acceleration = sum(a["p"]*a["acceleration_atom"] for a in atoms)
    correction = isum(iscale(-2*a["p"]*(a["acceleration_atom"]-mean_acceleration),
                            log_interval(a["p"])) for a in atoms)
    return {"atoms": atoms, "L": l, "fisher": fisher,
            "curvature": curvature, "hessian": hessian,
            "nonlinear_L_correction": correction}


def trace_resolvent(l, subset, u):
    if not subset:
        return F(0)
    local = add(sub(l, subset), eye(len(subset)), u)
    return tr(inv(local))


def curvature_resolvent(data, u):
    l, atoms = data["L"], data["atoms"]
    uncentered = sum((a["ddp"]*trace_resolvent(l, a["S"], u)
                     for a in atoms), F(0))
    centered = F(0)
    for a in atoms:
        value = trace_resolvent(l, a["S"], u)
        value -= sum((1/(l[i][i]+u) for i in a["S"]), F(0))
        assert value >= 0  # Nonnegativity still does not control the signed sum.
        centered += a["ddp"]*value
    assert centered == uncentered
    return centered


def entropy_interval(kernel):
    n = len(kernel)
    complement = add(eye(n), kernel, -1)
    probabilities = []
    for mask in range(1 << n):
        mixed = [[(kernel if mask & (1 << j) else complement)[i][j]
                  for j in range(n)] for i in range(n)]
        probabilities.append(det(mixed))
    assert all(p > 0 for p in probabilities) and sum(probabilities) == 1
    return isum(iscale(-p, log_interval(p)) for p in probabilities)


def stringify(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: stringify(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [stringify(item) for item in value]
    return value


ident = eye(3)
l0 = [[F(1), F(1, 2), F(1, 2)],
      [F(1, 2), F(1), F(1, 3)],
      [F(1, 2), F(1, 3), F(1)]]
assert positive_definite(l0) and det(l0) == F(5, 9)
l = scale(l0, 20)
k0 = add(ident, inv(add(ident, l)), -1)
assert positive_definite(k0) and positive_definite(add(ident, k0, -1))
assert k0[0][0] == F(1060, 1143)

# Claim 3: failure of supermodularity for an individual trace resolvent.
resolvent_difference = (trace_resolvent(l0, [0, 1, 2], F(0))
                        - trace_resolvent(l0, [0, 1], F(0))
                        - trace_resolvent(l0, [0, 2], F(0))
                        + trace_resolvent(l0, [0], F(0)))
assert resolvent_difference == F(-1, 30)

edge = [[F(0), F(0), F(0)],
        [F(0), F(0), F(1)],
        [F(0), F(1), F(0)]]
edge_data = atom_jet(k0, edge)
assert edge_data["L"] == l
edge_resolvent_0 = curvature_resolvent(edge_data, F(0))
edge_resolvent_20 = curvature_resolvent(edge_data, F(20))
assert edge_resolvent_0 == F(35, 27432) > 0
assert edge_resolvent_20 == F(-991, 1200150) < 0
edge_curvature_formula = isum([
    iscale(2*(1-k0[0][0]), log_interval(F(8, 9))),
    iscale(2*k0[0][0], log_interval(F(80, 81)))])
assert edge_data["curvature"][0] <= edge_curvature_formula[1]
assert edge_curvature_formula[0] <= edge_data["curvature"][1]
assert edge_data["curvature"][1] < 0

# The large-u coefficient of the resolvent equals 4 sum |L_ij|^2 det(A_ij).
tail_coefficient = 4*sum((l[i][j]**2*det(sub(edge, [i, j]))
                         for i in range(3) for j in range(i+1, 3)), F(0))
assert tail_coefficient == F(-1600, 9)

# Claim 2: a non-coordinate, noncommuting positive-plane direction.
plane = [[F(1, 5), F(2, 5), F(0)],
         [F(2, 5), F(4, 5), F(0)],
         [F(0), F(0), F(1)]]
assert mul(plane, plane) == plane and tr(plane) == 2 and det(plane) == 0
assert mul(k0, plane) != mul(plane, k0)
assert all(plane[i][i] > 0 for i in range(3))
plane_data = atom_jet(k0, plane)
for atom in plane_data["atoms"]:
    assert atom["kappa"] >= 0
    assert atom["score"]**2 <= 2*atom["kappa"]
positive_mass = sum((max(a["ddp"], 0) for a in plane_data["atoms"]), F(0))
negative_mass = sum((max(-a["ddp"], 0) for a in plane_data["atoms"]), F(0))
assert positive_mass == negative_mass <= plane_data["fisher"]/2
dependence = log_interval(F(9, 5))
theorem_bound = isum([(-plane_data["fisher"], -plane_data["fisher"]),
                      iscale(plane_data["fisher"]/2, dependence)])
assert dependence[1] < 2
assert plane_data["hessian"][1] < theorem_bound[0] < 0
atom_ratio_lower_bound = det(l)
assert atom_ratio_lower_bound == F(40000, 9)
assert log_interval(atom_ratio_lower_bound)[0] > 2
# Unequal pair probabilities exclude cardinality-uniform base kernels.
assert det(sub(l, [0, 1])) != det(sub(l, [1, 2]))

# A complete comparable endpoint segment, not just a pointwise example.
eta = F(1, 1000)
k1 = add(k0, plane, eta)
assert positive_definite(k1) and positive_definite(add(ident, k1, -1))
r_norm_bound = F(41)
delta_l_bound = eta*r_norm_bound**2/(1-eta*r_norm_bound)
assert delta_l_bound == F(1681, 959) < 2
det_correlation_lower_bound = F(40000, 9)/22**3
assert det_correlation_lower_bound == F(5000, 11979)
assert log_interval(1/det_correlation_lower_bound)[1] < 1
l1 = add(inv(add(ident, k1, -1)), ident, -1)
assert all(l1[i][i] < 22 for i in range(3))
assert det(l1) >= det(l)
midpoint = scale(add(k0, k1), F(1, 2))
chord_gap = isum([entropy_interval(midpoint),
                  iscale(F(-1, 2), entropy_interval(k0)),
                  iscale(F(-1, 2), entropy_interval(k1))])
chord_gap_lower_bound = F(1, 750000)*F(1, 4)
assert chord_gap[0] > chord_gap_lower_bound


def summarized_data(data):
    return {"fisher_exact": data["fisher"],
            "fisher_decimal": float(data["fisher"]),
            "curvature": rounded_interval(data["curvature"]),
            "entropy_hessian": rounded_interval(data["hessian"]),
            "nonlinear_L_correction": rounded_interval(data["nonlinear_L_correction"]),
            "atoms": data["atoms"]}


result = {
    "worker": "056",
    "method": "Exact rational algebra and rational logarithm intervals; no sampling.",
    "K0": k0,
    "L0_normalized": l0,
    "L": l,
    "edge_direction": edge,
    "positive_plane_direction": plane,
    "edge": summarized_data(edge_data),
    "positive_plane": summarized_data(plane_data),
    "resolvent": {
        "trace_inverse_second_difference_L0": resolvent_difference,
        "curvature_integrand_at_zero": edge_resolvent_0,
        "curvature_integrand_at_twenty": edge_resolvent_20,
        "large_u_times_u_cubed_limit": tail_coefficient,
        "integrated_curvature_closed_formula": rounded_interval(edge_curvature_formula)},
    "dependence_bound": {
        "det_correlation": det(l0),
        "minus_log_det_correlation": rounded_interval(dependence),
        "positive_plane_hessian_upper_bound": rounded_interval(theorem_bound),
        "atom_ratio_lower_bound": atom_ratio_lower_bound},
    "complete_segment": {
        "K1": k1,
        "eta": eta,
        "L_increment_operator_norm_upper_bound": delta_l_bound,
        "det_correlation_uniform_lower_bound": det_correlation_lower_bound,
        "uniform_chord_coefficient": F(1, 750000),
        "midpoint_chord_gap": rounded_interval(chord_gap),
        "midpoint_proved_lower_bound": chord_gap_lower_bound},
    "all_assertions_passed": True,
}
output = Path(__file__).with_name("056_resolvent_certificate.json")
output.write_text(json.dumps(stringify(result), indent=2)+"\n")
print(json.dumps({"all_assertions_passed": True,
                  "output": str(output),
                  "K0": stringify(k0),
                  "resolvent_at_zero": str(edge_resolvent_0),
                  "resolvent_at_twenty": str(edge_resolvent_20),
                  "edge_hessian": rounded_interval(edge_data["hessian"]),
                  "plane_hessian": rounded_interval(plane_data["hessian"]),
                  "plane_theorem_bound": rounded_interval(theorem_bound),
                  "midpoint_chord_gap": rounded_interval(chord_gap)}, indent=2))
