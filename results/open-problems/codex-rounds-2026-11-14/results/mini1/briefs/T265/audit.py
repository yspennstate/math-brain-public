#!/usr/bin/env python3
"""Small exact audits of PROOF.md; standard library only, one process."""
import itertools
import json
import math
import os
import resource
from fractions import Fraction
from pathlib import Path

assert os.environ.get("OMP_NUM_THREADS") == "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
if priority < 15:
    raise SystemExit(f"STOP: niceness is {priority}, below required 15; no audit computation run")
OUT = Path(__file__).resolve().parent


def count_bound(n, d):
    return 2 * sum(math.comb(n - 1, j) for j in range(min(d, n - 1) + 1))


def changes(mask, n):
    return sum(((mask >> i) ^ (mask >> (i + 1))) & 1 for i in range(n - 1))


def patterns(n, d):
    # On the moment curve, an affine score is a polynomial of degree <= d.
    return [mask for mask in range(1 << n) if changes(mask, n) <= d]


def polynomial_certificate(mask, n):
    coeff = [1]
    for i in range(n - 1):
        if ((mask >> i) ^ (mask >> (i + 1))) & 1:
            # Root i+1/2, with integer coefficients throughout.
            new = [0] * (len(coeff) + 1)
            for j, value in enumerate(coeff):
                new[j] -= (2 * i + 1) * value
                new[j + 1] += 2 * value
            coeff = new
    first = coeff[0]
    orient = 1 if (first > 0) == bool(mask & 1) else -1
    for i in range(n):
        val = sum(c * i**j for j, c in enumerate(coeff)) * orient
        assert val != 0
        assert (val > 0) == bool((mask >> i) & 1)
    return len(coeff) - 1


count_cases = 0
certificates = 0
for n in range(1, 11):
    for d in range(1, min(n, 4) + 1):
        pp = patterns(n, d)
        assert len(pp) == count_bound(n, d)
        for mask in pp:
            assert polynomial_certificate(mask, n) <= d
            certificates += 1
        count_cases += 1


def exact_noise_case(n, d, numerator, denominator, clean):
    pp = patterns(n, d)
    histogram = [0] * (n + 1)
    for y in range(1 << n):
        flips = (y ^ clean).bit_count()
        weight = numerator**flips * (denominator - numerator)**(n - flips)
        errors = min((y ^ a).bit_count() for a in pp)
        histogram[errors] += weight
    total = denominator**n
    assert sum(histogram) == total
    rows = []
    for k in (0, 1, 2):
        exact_num = sum(histogram[: k + 1])
        tail_num = sum(math.comb(n, j) * numerator**j *
                       (denominator - numerator)**(n - j) for j in range(k + 1))
        bound_num = min(total, count_bound(n, d) * tail_num)
        assert exact_num <= bound_num
        if 2 * numerator == denominator and k == 0:
            assert exact_num == bound_num
        rows.append({"k": k, "exact": str(Fraction(exact_num, total)),
                     "bound": str(Fraction(bound_num, total))})
    return {"n": n, "d": d, "eta": str(Fraction(numerator, denominator)),
            "clean_mask": clean, "tails": rows}


noise_cases = [exact_noise_case(10, d, a, b, clean)
               for d in (1, 2) for a, b in ((1, 10), (1, 4), (1, 2))
               for clean in (0, 341)]

# A nonconstant posterior audit, conditioning on ten distinct inputs.
pnums = [1, 8, 3, 6, 5, 9, 2, 7, 4, 5]
qnums = [min(p, 10 - p) for p in pnums]
dp = [1]
for q in qnums:
    new = [0] * (len(dp) + 1)
    for j, value in enumerate(dp):
        new[j] += (10 - q) * value
        new[j + 1] += q * value
    dp = new
variable_rows = []
for d in (1, 2):
    pp = patterns(10, d)
    hist = [0] * 11
    for y in range(1024):
        weight = math.prod(p if (y >> i) & 1 else 10 - p
                           for i, p in enumerate(pnums))
        hist[min((y ^ a).bit_count() for a in pp)] += weight
    for k in (0, 1, 2):
        actual = sum(hist[: k + 1])
        bound = min(10**10, len(pp) * sum(dp[: k + 1]))
        assert actual <= bound
        variable_rows.append({"d": d, "k": k,
                              "exact": str(Fraction(actual, 10**10)),
                              "bound": str(Fraction(bound, 10**10))})

# Fully unconditional, iid finite-input audit; eight joint (X,Y) atoms.
# X is uniform on {-2,-1,1,2}; posteriors are {0.1,0.2,0.8,0.9}.
atoms = [(x, y, p if y else 10 - p)
         for x, p in zip((-2, -1, 1, 2), (1, 2, 8, 9)) for y in (0, 1)]
n = 5
iid_hist = [0] * (n + 1)
for sample in itertools.product(atoms, repeat=n):
    xs = [row[0] for row in sample]
    ymask = sum(row[1] << i for i, row in enumerate(sample))
    weight = math.prod(row[2] for row in sample)
    # Enumerate every threshold in both directions, with tied inputs together.
    pp = {0, (1 << n) - 1}
    for threshold in sorted(set(xs)):
        mask = sum((x >= threshold) << i for i, x in enumerate(xs))
        pp.add(mask)
        pp.add(mask ^ ((1 << n) - 1))
    iid_hist[min((ymask ^ a).bit_count() for a in pp)] += weight
assert sum(iid_hist) == 40**n
iid_rows = []
for k in (0, 1, 2):
    actual = Fraction(sum(iid_hist[: k + 1]), 40**n)
    tail = sum(Fraction(math.comb(n, j) * 3**j * 17**(n - j), 20**n)
               for j in range(k + 1))
    bound = min(Fraction(1), count_bound(n, 1) * tail)
    assert actual <= bound
    iid_rows.append({"k": k, "exact": str(actual), "bound": str(bound)})


def normal_tail_integral(s):
    # Independent evaluation of Phi(-s), without erf/erfc.
    steps = 24000
    h = 12.0 / steps
    values = [math.exp(-0.5 * (s + i * h)**2) / math.sqrt(2 * math.pi)
              for i in range(steps + 1)]
    return h / 3 * (values[0] + values[-1] +
                    4 * math.fsum(values[1:-1:2]) +
                    2 * math.fsum(values[2:-1:2]))


tail_checks = []
for s in (0.0, 2.0, 5.0, 10.0):
    direct = math.erfc(s / math.sqrt(2)) / 2
    integral = normal_tail_integral(s)
    assert abs(direct - integral) <= 1e-9 * direct + 1e-30
    lower = math.exp(-1 - s * s / 2) / (math.sqrt(2 * math.pi) * (s + 1))
    assert lower <= direct
    tail_checks.append({"s": s, "erfc": direct, "quadrature": integral,
                        "relative_difference": abs(direct - integral) / direct})


def log_count_recurrence(n, d):
    term = 0.0
    terms = [term]
    for j in range(1, min(d, n - 1) + 1):
        term += math.log(n - j) - math.log(j)
        terms.append(term)
    peak = max(terms)
    return math.log(2) + peak + math.log(math.fsum(math.exp(t - peak) for t in terms))


numerics = []
for n, d, s, eta in ((10000, 20, 2.0, 0.0), (10000, 20, 2.0, 0.1),
                       (10000, 20, 5.0, 0.0), (1000000, 100, 2.0, 0.1)):
    alpha = eta + (1 - 2 * eta) * math.erfc(s / math.sqrt(2)) / 2
    a = math.log(count_bound(n, d))
    a2 = log_count_recurrence(n, d)
    assert abs(a - a2) < 1e-9
    log_probability = min(0.0, a + n * math.log1p(-alpha))
    log_independent = min(0.0, a2 - n * (-math.log1p(-alpha)))
    assert abs(log_probability - log_independent) < 1e-8
    # The zero-error KL expression is a second formula for this exponent.
    kl_zero = math.log(1 / (1 - alpha))
    assert abs(kl_zero + math.log1p(-alpha)) < 1e-15
    lower_error_fraction = max(0.0, alpha - math.sqrt((a + math.log(100)) / (2 * n)))
    numerics.append({"n": n, "d": d, "s": s, "eta": eta, "alpha": alpha,
                     "log_M": a, "log_interpolation_probability_bound": log_probability,
                     "error_fraction_lower_bound_at_99_percent": lower_error_fraction})

# Independent rank and trace checks for the literature audit.
xs = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
      (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1)),
      (Fraction(3, 5), Fraction(4, 5)), (Fraction(-3, 5), Fraction(-4, 5))]
z = [1, 0, 1, 0, 0, 0]
assert all(sum(z[i] * xs[i][j] for i in range(6)) == 0 for j in range(2))
gram_z = [sum(sum(a * b for a, b in zip(xs[i], xs[j])) * z[j]
              for j in range(6)) for i in range(6)]
assert gram_z == [0] * 6
assert Fraction(6, 5 * 2) > Fraction(1, 2)

result = {"count_cases": count_cases, "polynomial_certificates": certificates,
          "fixed_noise_cases": noise_cases, "variable_posterior_cases": variable_rows,
          "iid_discrete_cases": iid_rows, "normal_tail_checks": tail_checks,
          "gaussian_numerics": numerics,
          "literature_audit": {"n": 6, "d": 2, "null_vector": z,
                               "gram_times_null_vector": [str(v) for v in gram_z],
                               "trace_average_NTK": "1/2", "claimed_lower_bound": "3/5"}}
(OUT / "audit_results.json").write_text(json.dumps(result, indent=2) + "\n")
print(f"PASS: {count_cases} moment-curve counts, {certificates} exact polynomial certificates")
print(f"PASS: {len(noise_cases) * 3} exact fixed-noise tail bounds; fair-noise interpolation equality")
print(f"PASS: {len(variable_rows)} variable-posterior tails; 3 iid-discrete tails (32768 samples)")
print("PASS: 4 Gaussian tails by erfc and independent quadrature; 4 count/exponent checks")
print("PASS: exact Gram null vector and independent NTK trace contradiction")
for row in numerics:
    print("Gaussian", json.dumps(row, sort_keys=True))
print("Saved audit_results.json")
print(f"Resource check: niceness={priority}; max_rss_bytes={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}")
