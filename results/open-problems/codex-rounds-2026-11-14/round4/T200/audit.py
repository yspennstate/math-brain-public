"""Independent baseline and weighted-energy certificates.

OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py weighted
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py potential
Uses the standard library only; writes no files.
"""

import ctypes
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
import math
import os
import resource
import sys


def guard():
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    libc = ctypes.CDLL(None, use_errno=True)
    ctypes.set_errno(0)
    priority = libc.getpriority(0, 0)
    assert ctypes.get_errno() == 0 and priority >= 15
    print(f"niceness={priority}; OMP_NUM_THREADS=1; CPU_limit=60s")


def dec(x):
    x = F(x)
    return D(x.numerator) / D(x.denominator)


def atan_sum(x, n):
    return sum(((-1)**j * x**(2*j+1) / (2*j+1) for j in range(n)), F(0))


def pi_bounds():
    return (16*atan_sum(F(1, 5), 40)-4*atan_sum(F(1, 239), 19),
            16*atan_sum(F(1, 5), 41)-4*atan_sum(F(1, 239), 20))


def log_bounds(x, n=100):
    assert x > 1
    z = (x-1)/(x+1)
    lower = 2*sum((z**(2*j+1)/(2*j+1) for j in range(n)), F(0))
    return lower, lower+2*z**(2*n+1)/((2*n+1)*(1-z*z))


def exp_sum(x, n):
    return sum((x**j/math.factorial(j) for j in range(n+1)), F(0))


def baseline():
    # New certificates, rather than importing the earlier worker's verifier.
    pilo, pihi = pi_bounds()
    assert pilo > F(177, 100)**2
    assert exp_sum(F(15, 2), 30) > 1800
    elo = exp_sum(F(1), 6)
    ehi = elo+F(1, math.factorial(7))/(1-F(1, 8))
    assert elo > F(27, 10) and ehi < F(11, 4)
    laplace = F(1, 120)+F(16)/(30*F(27, 10)*F(177, 100))
    assert laplace == F(68779, 573480) < F(3, 25)
    assert F(3, 25)*F(11, 4) == F(33, 100) < F(1, 3)
    green = F(1, 3)-F(3, 11)
    assert green == F(2, 33)
    assert 2*(F(2)-F(2, 3)) == F(8, 3)
    l3, u3 = log_bounds(F(3))
    gap_lo, gap_hi = green/(30*u3), green/(30*l3)
    pi = (dec(pilo)+dec(pihi))/2
    p = 6*D(6).sqrt()*(D(-15)/2).exp()
    moment = p+16/(30*D(1).exp()*pi.sqrt())
    gap = 1/(495*D(3).ln())
    assert dec(gap_lo) < gap < dec(gap_hi)
    assert abs(float(gap)-(2/33)/(30*math.log(3))) < 1e-17
    print(f"baseline_laplace_bound={moment}")
    print(f"baseline_rational_laplace_upper={laplace}")
    print(f"baseline_tail_exponent={-(D(33)/100).ln()/D(3).ln()}")
    print(f"baseline_xi_upper={1-gap}")
    print("ROUND 3 RESULT VERIFIED independently")


def weighted():
    pilo, pihi = pi_bounds()
    # B(3/4,3/4)=2^(1/4) S. Positive binomial expansion on [0,1/2].
    coeff, slo = F(1), F(0)
    for n in range(24):
        slo += coeff/(2**n*(F(n)+F(3, 4)))
        coeff *= (F(n)+F(1, 4))/(n+1)
        if n == 7:
            s8 = slo
    # The omitted tail starts at n=24 and has term ratios <1/2.
    shi = slo+2*coeff/(2**24*(F(24)+F(3, 4)))
    jbound = F(21, 8)
    assert s8 == F(112206509213551, 78752847495168) > F(178, 125)
    assert pihi < F(22, 7)
    assert 2*F(22, 7)**4 < jbound**4*F(178, 125)**4
    # J^4=2*pi^4/S^4. This entirely rational comparison certifies J<21/8.
    assert 2*pihi**4 < jbound**4*slo**4
    assert (16*atan_sum(F(1, 5), 8)-4*atan_sum(F(1, 239), 5)
            > F(177, 100)**2)
    assert pilo > F(177, 100)**2
    assert exp_sum(F(15, 2), 30) > 1800
    elo = exp_sum(F(1), 4)
    ehi = elo+F(1, 120)/(1-F(1, 6))
    assert elo == F(65, 24) and ehi < F(68, 25)
    energy_numerator = 6*jbound
    assert energy_numerator == F(63, 4) < 16
    laplace_upper = F(1, 120)+energy_numerator/(29*elo*F(177, 100))
    rounded = F(11, 90)
    assert laplace_upper < rounded
    tail_base = rounded*F(68, 25)
    assert tail_base == F(374, 1125) < F(1, 3)
    l3, u3 = log_bounds(F(3))
    numerator = F(2, 33*29)
    gaplo, gaphi = numerator/u3, numerator/l3
    # A plain rational display bound from log(3)<1.099.
    assert exp_sum(F(1099, 1000), 6) > 3
    assert numerator/F(1099, 1000) > F(19, 10000)
    pi = (dec(pilo)+dec(pihi))/2
    smid = (dec(slo)+dec(shi))/2
    beta = D(2).sqrt().sqrt()*smid
    jvalue = pi*D(2).sqrt()/beta
    # A separate positive series directly for B(1/4,3/4), with pi not used.
    def beta_half_series(a, b):
        c, total = D(1), D(0)
        for n in range(160):
            total += c*D(2)**(-n)/(dec(a)+n)
            c *= (1-dec(b)+n)/(n+1)
        return D(2)**(-dec(a))*total
    beta2 = 2*beta_half_series(F(3, 4), F(3, 4))
    numerator2 = (beta_half_series(F(1, 4), F(3, 4))+
                  beta_half_series(F(3, 4), F(1, 4)))
    jvalue2 = numerator2/beta2
    assert dec(slo)*D(2).sqrt().sqrt() < beta2 < dec(shi)*D(2).sqrt().sqrt()
    assert abs(numerator2-pi*D(2).sqrt()) < D('1e-45')
    assert abs(jvalue-jvalue2) < D('1e-8')
    assert jvalue2 < dec(jbound)
    energy = 6*jvalue2/pi.sqrt()
    exitbound = 6*D(6).sqrt()*(D(-15)/2).exp()
    laplace = exitbound+energy/(29*D(1).exp())
    uniform_laplace29 = exitbound+16/(29*D(1).exp()*pi.sqrt())
    assert laplace < dec(laplace_upper) < dec(rounded)
    assert uniform_laplace29 > 1/(3*D(1).exp())
    gap = dec(numerator)/D(3).ln()
    assert dec(gaplo) < gap < dec(gaphi)
    assert abs(float(gap)-(2/33)/(29*math.log(3))) < 1e-17
    print(f"beta_series_terms=24; beta_series_width={dec(shi-slo)}")
    print(f"first_eight_series_terms={s8}")
    print(f"first_eight_margin_above_178_over_125={s8-F(178, 125)}")
    print("J_upper_verified_two_rational_ways=True")
    print(f"optimal_time_energy_J={jvalue2}")
    print(f"certified_J_upper={jbound}")
    print(f"weighted_expected_energy_times_r={energy}")
    print(f"uniform_expected_energy_times_r={16/pi.sqrt()}")
    print(f"energy_reduction_fraction={1-jvalue2/(D(8)/3)}")
    print(f"weighted_laplace29_bound={laplace}")
    print(f"uniform_laplace29_bound={uniform_laplace29}")
    print(f"critical_laplace_for_threshold_1_over_29={1/(3*D(1).exp())}")
    print(f"rational_laplace_upper={laplace_upper}")
    print(f"rational_laplace_margin={rounded-laplace_upper}")
    print(f"rounded_laplace_upper={rounded}")
    print(f"certified_tail_base={tail_base}")
    print(f"tail_margin_below_1_over_3={F(1, 3)-tail_base}")
    print(f"certified_tail_exponent={-dec(tail_base).ln()/D(3).ln()}")
    print(f"gap={gap}")
    print(f"xi_upper={1-gap}")
    print(f"gap_ratio_to_round3={F(30, 29)}")
    print("ALL WEIGHTED-ENERGY CERTIFICATE CHECKS PASSED")


def potential():
    """Independent direct quadrature diagnostic, not an interval certificate."""
    def simpson(f, n):
        assert n % 2 == 0
        return (f(0.0)+f(1.0)+sum((4 if j % 2 else 2)*f(j/n)
                                 for j in range(1, n)))/(3*n)

    def beta_integrand(z):
        den = z**4+(1-z)**4
        return 4*z*z*(1-z)**2/den**1.5

    def left_integral(x, n):
        if x == 0:
            return 0.0
        def f(z):
            den = z**4+(1-z)**4
            if x == 1:
                return 4*z*z/den
            return (x**0.25*4*z*z*(1-z)/den /
                    ((1-x)*z**4+(1-z)**4)**0.25)
        return simpson(f, n)

    target = math.pi*math.sqrt(2)
    errors = []
    for n in (1024, 2048):
        beta = simpson(beta_integrand, n)
        maxerror = 0.0
        for x in (0.0, 0.001, 0.01, 0.125, 0.25, 0.5, 0.9, 0.999, 1.0):
            raw = left_integral(x, n)+left_integral(1-x, n)
            maxerror = max(maxerror, abs(raw-target))
        jvalue = target/beta
        assert abs(jvalue-2.6220575542921198) < 1e-9
        assert maxerror < 1e-9
        errors.append(maxerror)
        print(f"mesh={n}; direct_beta={beta:.16g}; direct_J={jvalue:.16g}; "
              f"max_potential_error={maxerror:.3g}")
    assert errors[1] < errors[0]/8
    print("DIRECT POTENTIAL QUADRATURE DIAGNOSTIC PASSED (not a proof certificate)")


if __name__ == "__main__":
    guard()
    getcontext().prec = 65
    if sys.argv[1:] == ["baseline"]:
        baseline()
    elif sys.argv[1:] == ["weighted"]:
        weighted()
    elif sys.argv[1:] == ["potential"]:
        potential()
    else:
        raise SystemExit("choose baseline, weighted or potential")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == "darwin" else rss*1024
    assert rss_bytes < 1024**3
    print(f"peak_RSS_bytes={rss_bytes}")
