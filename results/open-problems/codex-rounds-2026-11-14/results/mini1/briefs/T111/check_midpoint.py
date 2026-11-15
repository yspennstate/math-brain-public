"""Reproduce finite-law checks of PROOF.md; no stochastic simulation.

Run with OMP_NUM_THREADS=1 and nice -n 15. Outputs stay beside this file.
The floating checks illustrate the theorem; its proof does not depend on them.
"""

import os
import resource
import signal
import time
from pathlib import Path

for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
             "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
if priority < 15:
    os.setpriority(os.PRIO_PROCESS, 0, 15)
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
try:
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    address_space_cap = True
except (ValueError, OSError):
    # Darwin may reject RLIMIT_AS. Array sizes are below a few MB, and
    # actual peak RSS is checked and reported at the end of this bounded run.
    address_space_cap = False
resource.setrlimit(resource.RLIMIT_CPU, (600, 600))
signal.alarm(900)

import csv
import json
import math
from fractions import Fraction

import mpmath as mp
import numpy as np
from scipy.special import ndtr
from scipy.stats import binom

ROOT = Path(__file__).resolve().parent


def limit_ratio(p, lam):
    q = 1 - p
    return (abs(q - p) / 6 + (1 + math.exp(-2 * lam)) / 4) / (
        math.sqrt(2 * math.pi) * (p*p + q*q))


def optimum(lam):
    b = 3 * (1 + math.exp(-2 * lam))
    # Rationalized root avoids cancellation.
    t = 2 / (math.sqrt(b*b + 4) + b)
    p = (1 - t) / 2
    value = (b + math.sqrt(b*b + 4)) / (12 * math.sqrt(2 * math.pi))
    return p, value


def mixture_pmf(n, p, lam):
    """Condition on midpoint count, then evaluate binomial masses.

    Only a certified-by-formula binomial tail (reported as a float) is omitted.
    No renormalization or FFT, and no negative-mass clipping is used.
    """
    eps = lam / n
    assert 0 <= eps < 1
    if lam == 0:
        cutoff = 0
    else:
        cutoff = min(n, int(math.ceil(lam + 12 * math.sqrt(lam + 1) + 24)))
    mass = np.zeros(2*n + 1)
    for j in range(cutoff + 1):
        w = float(binom.pmf(j, n, eps))
        if w:
            k = np.arange(n-j + 1)
            mass[j:2*n-j+1:2] += w * binom.pmf(k, n-j, p)
    omitted = float(binom.sf(cutoff, n, eps))
    return mass, omitted


def statistics(n, p, lam, mass):
    eps = lam / n
    probs = np.array([(1-eps)*(1-p), eps, (1-eps)*p])
    support = np.array([0., 1., 2.])
    mu = float(probs @ support)
    variance = float(probs @ ((support-mu)**2))
    beta3 = float(probs @ (np.abs(support-mu)**3))
    rho = beta3 / variance**1.5
    cdf = np.cumsum(mass)
    normal = ndtr((np.arange(2*n+1)-n*mu)/math.sqrt(n*variance))
    right = cdf-normal
    left = cdf-mass-normal
    ir = int(np.argmax(np.abs(right)))
    il = int(np.argmax(np.abs(left)))
    if abs(right[ir]) >= abs(left[il]):
        delta, k, side = abs(float(right[ir])), ir, "right"
    else:
        delta, k, side = abs(float(left[il])), il, "left"
    ratio = math.sqrt(n)*delta/rho
    return ratio, k, side, mu, variance, rho


def exact_integer_pmf(n, p, lam):
    """Independent integer polynomial multiplication, for rational laws."""
    eps = lam / n
    weights = [(1-eps)*(1-p), eps, (1-eps)*p]
    denom = math.lcm(*(w.denominator for w in weights))
    coeff = [int(w*denom) for w in weights]
    assert sum(coeff) == denom
    values = [1]
    for _ in range(n):
        nxt = [0] * (len(values)+2)
        for k, v in enumerate(values):
            for j, c in enumerate(coeff):
                nxt[k+j] += v*c
        values = nxt
    total = denom**n
    assert sum(values) == total
    return values, total, weights


def high_precision_statistics(n, coefficients, denom, weights):
    def mfrac(x):
        return mp.mpf(x.numerator)/x.denominator
    w = [mfrac(x) for x in weights]
    mu = sum(j*w[j] for j in range(3))
    var = sum(w[j]*(j-mu)**2 for j in range(3))
    rho = sum(w[j]*abs(j-mu)**3 for j in range(3))/var**mp.mpf("1.5")
    cumulative = mp.mpf(0)
    delta = mp.mpf(0)
    pmf = []
    for k, value in enumerate(coefficients):
        atom = mp.mpf(value)/denom
        pmf.append(atom)
        phi = mp.erfc(-(k-n*mu)/mp.sqrt(2*n*var))/2
        delta = max(delta, abs(cumulative-phi))
        cumulative += atom
        delta = max(delta, abs(cumulative-phi))
    assert abs(cumulative-1) < mp.mpf("1e-70")
    return mp.sqrt(n)*delta/rho, pmf


def main():
    start = time.monotonic()
    mp.mp.dps = 90
    p_esseen = (4-math.sqrt(10))/2
    rows = []
    max_mass_error = 0.0
    max_omitted = 0.0
    expansion_checks = []
    for lam in (0., .1, 1., 4.):
        popt, _ = optimum(lam)
        for label, p in (("symmetric", .5), ("Esseen", p_esseen),
                         ("optimized", popt), ("skew", .2)):
            for n in (128, 512, 2048, 8192, 32768):
                pmf, omitted = mixture_pmf(n, p, lam)
                value, k, side, mu, var, rho = statistics(n, p, lam, pmf)
                target = limit_ratio(p, lam)
                mass_error = abs(float(pmf.sum())-1)
                max_mass_error = max(max_mass_error, mass_error)
                max_omitted = max(max_omitted, omitted)
                assert mass_error < 2e-11
                assert omitted < 1e-18
                # Test both CDF endpoint expansions (12) and (14),
                # including their signs and alternating parity correction.
                kgrid = np.arange(2*n+1)
                zgrid = (kgrid-n*mu)/math.sqrt(n*var)
                density = np.exp(-zgrid*zgrid/2)/math.sqrt(2*math.pi)
                parity_expectation = (1-2*lam/n)**n
                parity_term = (1+np.where(kgrid % 2 == 0, 1, -1)*parity_expectation)/4
                skew_term = (1-2*p)*(1-zgrid*zgrid)/6
                scale = density/math.sqrt(n*p*(1-p))
                cdf = np.cumsum(pmf)
                normal = ndtr(zgrid)
                residual_right = float(np.max(np.abs(cdf-normal-scale*(skew_term+parity_term))))
                residual_left = float(np.max(np.abs(cdf-pmf-normal-scale*(skew_term-parity_term))))
                expansion_checks.append(dict(n=n, p=p, lam=lam,
                                             sqrt_n_max_residual=math.sqrt(n)*max(residual_right, residual_left)))
                # Raw moments are computed separately from formula (8).
                a = 1-2*p
                assert abs(mu-(2*p+a*lam/n)) < 5e-16
                expected_var = 4*p*(1-p)+(a*a-4*p*(1-p))*(lam/n)-a*a*(lam/n)**2
                assert abs(var-expected_var) < 5e-16
                rows.append(dict(lam=lam, label=label, p=p, n=n,
                                 finite_ratio=value, limit_ratio=target,
                                 difference=value-target, k=k, side=side,
                                 mu=mu, variance=var, rho=rho,
                                 mass_error=mass_error, omitted_tail=omitted))
    with (ROOT/"midpoint_data.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    # Full finite-distribution audit by a separate arithmetic and algorithm.
    independent = []
    max_pmf_error = 0.0
    max_ratio_error = 0.0
    for p in (Fraction(1, 2), Fraction(2, 5), Fraction(3, 7), Fraction(4, 5)):
        for lam in (Fraction(0), Fraction(1, 10), Fraction(1), Fraction(4)):
            for n in (8, 31, 64):
                nums, den, weights = exact_integer_pmf(n, p, lam)
                exact_ratio, exact_pmf = high_precision_statistics(n, nums, den, weights)
                mix, omitted = mixture_pmf(n, float(p), float(lam))
                ratio, *_ = statistics(n, float(p), float(lam), mix)
                pmf_error = max(abs(mix[k]-float(v)) for k, v in enumerate(exact_pmf))
                ratio_error = abs(ratio-float(exact_ratio))
                max_pmf_error = max(max_pmf_error, pmf_error)
                max_ratio_error = max(max_ratio_error, ratio_error)
                assert pmf_error < 3e-14
                assert ratio_error < 3e-13
                independent.append(dict(p=str(p), lam=str(lam), n=n,
                                        high_precision_ratio=mp.nstr(exact_ratio, 60),
                                        pmf_error=pmf_error, ratio_error=ratio_error))

    # Check reflection invariance and all first-order CDF coefficients.
    reflected, _ = mixture_pmf(511, .8, 1.)
    original, _ = mixture_pmf(511, .2, 1.)
    reflection_error = float(np.max(np.abs(reflected-original[::-1])))
    assert reflection_error < 3e-14
    r1, *_ = statistics(511, .2, 1., original)
    r2, *_ = statistics(511, .8, 1., reflected)
    assert abs(r1-r2) < 3e-13

    # Symmetric even rows have discrepancy P(T_n=n)/2 at their center.
    center_checks = []
    for lam in (0., .1, 1., 4.):
        for n in (1024, 4096, 16384):
            mass, _ = mixture_pmf(n, .5, lam)
            center = math.sqrt(n)*mass[n]*math.sqrt(1-lam/n)/2
            target = (1+math.exp(-2*lam))/(2*math.sqrt(2*math.pi))
            center_checks.append(dict(lam=lam, n=n, scaled_center_error=center,
                                      target=target, difference=center-target))

    values = []
    for lam in (0., .1, 1., 4.):
        p, v = optimum(lam)
        assert abs(v-limit_ratio(p, lam)) < 3e-16
        # Exhaustive auxiliary grid checks the analytic optimizing formula.
        grid_max = max(limit_ratio(k/20000, lam) for k in range(1, 20000))
        assert grid_max <= v + 3e-16
        values.append(dict(lam=lam, maximizing_p=p, K=v, grid_max=grid_max))
    assert abs(values[0]["K"]-(3+math.sqrt(10))/(6*math.sqrt(2*math.pi))) < 1e-16

    # macOS reports ru_maxrss in bytes, unlike Linux's kilobytes.
    import sys
    raw_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = raw_rss if sys.platform == "darwin" else 1024*raw_rss
    assert peak_bytes < 1024**3
    summary = dict(finite_rows=len(rows), independent_exact_cases=len(independent),
                   max_mass_error=max_mass_error, max_omitted_tail=max_omitted,
                   max_independent_pmf_error=max_pmf_error,
                   max_independent_ratio_error=max_ratio_error,
                   reflection_pmf_error=reflection_error,
                   effective_nice=os.getpriority(os.PRIO_PROCESS, 0),
                   address_space_hard_cap_supported=address_space_cap,
                   peak_rss_bytes=peak_bytes, elapsed_seconds=time.monotonic()-start,
                   optimized_constants=values,
                   worst_scaled_cdf_residual_by_n={str(n): max(
                       r["sqrt_n_max_residual"] for r in expansion_checks if r["n"]==n)
                       for n in (128, 512, 2048, 8192, 32768)},
                   final_n_optimized_rows=[r for r in rows if r["label"]=="optimized"
                                           and r["n"]==32768])
    audit = dict(summary=summary, exact_cases=independent, center_checks=center_checks)
    audit["cdf_expansion_checks"] = expansion_checks
    (ROOT/"midpoint_audit.json").write_text(json.dumps(audit, indent=2)+"\n")
    output = json.dumps(summary, indent=2)+"\nAll assertions passed.\n"
    (ROOT/"computation.out").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
