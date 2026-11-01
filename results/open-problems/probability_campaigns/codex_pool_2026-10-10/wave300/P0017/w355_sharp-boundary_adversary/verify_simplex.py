"""Bounded exact arithmetic independent of any live store or training process."""
from fractions import Fraction as F
import json
import math
from pathlib import Path
import time

folder = Path(__file__).resolve().parent
gate = json.loads((folder / "COMPUTE_GATE.json").read_text(encoding="utf-8"))
started = time.perf_counter()
checks = 0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1
    if time.perf_counter() - started > gate["max_wall_seconds"]:
        raise TimeoutError("Fresh compute gate exceeded")

def simplex_moment(n, powers):
    return F(math.factorial(n) * math.prod(math.factorial(k) for k in powers), math.factorial(n + sum(powers)))

def beta_integer(p, q):
    return F(math.factorial(p - 1) * math.factorial(q - 1), math.factorial(p + q - 1))

def expanded_beta_integral(p, q):
    # Direct integration after expanding (1-x)^(q-1), independent of factorial formula.
    return sum((F((-1)**j * math.comb(q - 1, j), p + j) for j in range(q)), F(0))

rows = []
for n in gate["dimensions"]:
    check(2 <= n <= gate["max_dimension"], "dimension gate")
    m = n + 1
    a_squared = m * (n + 2)
    for i in range(m):
        powers = [0] * m
        powers[i] = 1
        check(simplex_moment(n, powers) == F(1, m), "simplex first moment")
        for j in range(m):
            powers = [0] * m
            powers[i] += 1
            powers[j] += 1
            covariance = a_squared * (simplex_moment(n, powers) - F(1, m*m))
            check(covariance == F(int(i == j)) - F(1, m), "ambient covariance projector")
    density_normalization = n * (n - 1) * beta_integer(2, n - 1)
    check(density_normalization == 1, "fiber beta density normalization")
    s2_barycentric = 2 * simplex_moment(n, [2] + [0]*n) + 2 * simplex_moment(n, [1, 1] + [0]*(n - 1))
    s2_density = n * (n - 1) * beta_integer(4, n - 1)
    check(s2_barycentric == s2_density == F(6, (n + 1)*(n + 2)), "second moment from two representations")
    conditional_variance_mean = F((n + 1)*(n + 2), 6) * s2_density
    check(conditional_variance_mean == 1, "total conditional variance")
    b = F(1, 2)
    d = 1 - b
    def cutoff_moment(k, integral):
        return n*(n - 1)*d**(n + 3)*sum((F(math.comb(k + 1, r))*b**(k + 1-r)*d**r*integral(5 + r, n - 1) for r in range(k + 2)), F(0))
    denominator = cutoff_moment(0, beta_integer)
    numerator = cutoff_moment(2, beta_integer)
    check(denominator == cutoff_moment(0, expanded_beta_integral), "cutoff energy direct polynomial integration")
    check(numerator == cutoff_moment(2, expanded_beta_integral), "cutoff variance direct polynomial integration")
    ratio = F((n + 1)*(n + 2), 6) * numerator / denominator
    lower_bound = F((n + 1)*(n + 2), 24)
    check(ratio > lower_bound, "weighted energy ratio strict lower bound")
    delta = F(1, 2)
    tail = delta**(n - 1)*(n - (n - 1)*delta)
    check(0 < tail < 1, "positive-probability long-slice event")
    row = {
        "n":n,
        "global_covariance":"identity on H (ambient projector checked exactly)",
        "mean_conditional_variance":str(conditional_variance_mean),
        "ess_sup_conditional_variance":str(F((n + 1)*(n + 2), 6)),
        "mean_conditional_poincare":12/math.pi**2,
        "ess_sup_conditional_poincare":2*(n + 1)*(n + 2)/math.pi**2,
        "probability_S_gt_half_exact":str(tail),
        "weighted_variance_energy_ratio_exact":str(ratio),
        "weighted_variance_energy_ratio":float(ratio),
        "ratio_lower_bound_exact":str(lower_bound),
        "ratio_over_unweighted_mean_poincare":float(ratio)/(12/math.pi**2)
    }
    rows.append(row)
    with (folder / "MEASUREMENTS.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row) + "\n")

receipt = {
    "command":"python -X utf8 -B ~/brain_workers/w355/verify_simplex.py",
    "checks_passed":checks,
    "dimensions":gate["dimensions"],
    "elapsed_seconds":time.perf_counter() - started,
    "baseline":"Unweighted mean fiber Poincare constant 12/pi^2 in every dimension",
    "corrected_comparison":"Energy-weighted test ratio grows quadratically; exact covariance and positive tail probability verified",
    "result":"PASS",
    "formal_proof_receipt":False,
    "independent_referee_check":"pending w356"
}
(folder / "VERIFICATION.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"receipt":receipt,"rows":rows}, indent=2))
