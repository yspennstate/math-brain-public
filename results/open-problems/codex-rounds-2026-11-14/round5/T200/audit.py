"""Small standard-library audits. Commands are recorded in LOG.md."""

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


def exp_partial(x, n):
    return sum((x**j/math.factorial(j) for j in range(n+1)), F(0))


def exp_interval(x, n):
    assert x > 0 and x < n+2
    lo = exp_partial(x, n)
    return lo, lo+(x**(n+1)/math.factorial(n+1))/(1-x/(n+2))


def log_interval(x, n=100):
    assert x > 1
    z = (x-1)/(x+1)
    lo = 2*sum((z**(2*j+1)/(2*j+1) for j in range(n)), F(0))
    return lo, lo+2*z**(2*n+1)/((2*n+1)*(1-z*z))


def atan_partial(x, n):
    return sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(n)), F(0))


def pi_interval():
    return (16*atan_partial(F(1, 5), 32)-4*atan_partial(F(1, 239), 17),
            16*atan_partial(F(1, 5), 33)-4*atan_partial(F(1, 239), 16))


def beta_series(a, b):
    # Half-interval binomial expansion, evaluated independently in Decimal.
    c, total = D(1), D(0)
    for j in range(180):
        total += c*D(2)**(-j)/(dec(a)+j)
        c *= (1-dec(b)+j)/(j+1)
    return D(2)**(-dec(a))*total


def baseline():
    plo, phi = pi_interval()
    c, s8 = F(1), F(0)
    for j in range(8):
        s8 += c/(2**j*(F(j)+F(3, 4)))
        c *= (F(j)+F(1, 4))/(j+1)
    assert s8 > F(178, 125)
    assert 2*F(22, 7)**4 < F(21, 8)**4*F(178, 125)**4
    assert phi < F(22, 7) and plo > F(177, 100)**2
    assert exp_partial(F(15, 2), 30) > 1800
    elo = exp_partial(F(1), 4)
    ehi = elo+F(1, 120)/(1-F(1, 6))
    assert elo == F(65, 24) and ehi < F(68, 25)
    laplace = F(1, 120)+F(63, 4)/(29*elo*F(177, 100))
    assert laplace == F(324643, 2669160) < F(11, 90)
    assert F(11, 90)*F(68, 25) == F(374, 1125) < F(1, 3)
    pi = (dec(plo)+dec(phi))/2
    beta = 2*beta_series(F(3, 4), F(3, 4))
    raw = beta_series(F(1, 4), F(3, 4))+beta_series(F(3, 4), F(1, 4))
    jvalue = raw/beta
    assert abs(raw-pi*D(2).sqrt()) < D('1e-44')
    moment = 6*D(6).sqrt()*(D(-15)/2).exp()+6*jvalue/(29*D(1).exp()*pi.sqrt())
    gap = 2/(957*D(3).ln())
    assert moment < dec(laplace)
    assert abs(float(gap)-2/(957*math.log(3))) < 1e-17
    # A different substitution for direct potential quadrature:
    # v=x sin(theta)^2 on its left half; theta=(pi/2) z^2.
    def simpson(f, n):
        return (f(0.0)+f(1.0)+sum((4 if i % 2 else 2)*f(i/n)
                                 for i in range(1, n)))/(3*n)
    def left(x, n):
        if x == 0:
            return 0.0
        if x == 1:
            # Its exact beta endpoint is already checked above.
            return math.pi*math.sqrt(2)
        def f(z):
            if z == 0:
                return 0.0
            theta = (math.pi/2)*z*z
            return (2*math.pi*z*x**0.25*math.sqrt(math.sin(theta)) /
                    (1-x*math.sin(theta)**2)**0.25)
        return simpson(f, n)
    for n in (1024, 2048):
        error = max(abs(left(x, n)+left(1-x, n)-math.pi*math.sqrt(2))
                    for x in (0.0, 0.01, 0.2, 0.5, 0.87, 0.999, 1.0))
        assert error < 1e-8
        print(f"independent_potential_mesh={n}; max_error={error:.4g}")
    print(f"J_independent_beta_series={jvalue}")
    print(f"round4_rational_laplace_upper={laplace}")
    print(f"round4_unrounded_laplace={moment}")
    print(f"round4_tail_exponent={-dec(F(374, 1125)).ln()/D(3).ln()}")
    print(f"round4_xi_upper={1-gap}")
    print("ROUND 4 RESULT VERIFIED independently")


def radial():
    plo, phi = pi_interval()
    p = F(16311, 1000000)
    A = F(27707, 5000)
    elo, etheta_hi = F(67957, 25000), F(24467, 10000)
    s, c, theta = F(17), F(1, 19), F(17, 19)
    # Polynomial identity underlying the Mills upper bound. Coefficients
    # are stored in ascending order, independent of symbolic libraries.
    def add(*polys):
        out = [F(0)]*max(map(len, polys))
        for poly in polys:
            for i, x in enumerate(poly):
                out[i] += x
        return out
    def mul(a, b):
        out = [F(0)]*(len(a)+len(b)-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] += x*y
        return out
    def neg(a):
        return [-x for x in a]
    def deriv(a):
        return [i*x for i, x in enumerate(a)][1:]
    P, Q = [8, 0, 9, 0, 1], [0, 15, 0, 10, 0, 1]
    remainder = add(mul(deriv(P), Q), neg(mul(P, deriv(Q))),
                    neg(mul([0, 1], mul(P, Q))), mul(Q, Q))
    assert remainder == [-120]+[0]*10
    # Mills at x=sqrt(7) gives p <= 240 exp(-7/2)/(67 sqrt(14 pi)).
    e35lo = exp_partial(F(7, 2), 24)
    picoarse, e35coarse = F(314159, 100000), F(662309, 20000)
    assert 16*atan_partial(F(1, 5), 8)-4*atan_partial(F(1, 239), 5) > picoarse
    assert plo > picoarse and e35lo > e35coarse
    assert p*p*67**2*14*picoarse*e35coarse**2 > 240**2
    assert A*A*picoarse > 14*F(21, 8)**2
    assert exp_partial(F(1), 10) > elo
    assert exp_interval(theta, 16)[1] < etheta_hi
    m = p+A/(s*elo)
    mround = F(13623, 100000)
    assert m < mround
    base = etheta_hi*mround
    assert base == F(333313941, 1000000000) < F(1, 3)
    # Independent certificate of the Gaussian tail by integrating its
    # Taylor series, rather than using the rational Mills approximation.
    slow = sum(((-F(7, 2))**j/((2*j+1)*math.factorial(j))
                for j in range(60)), F(0))
    shi = slow+F(7, 2)**60/(121*math.factorial(60))
    assert 0 < slow < shi
    assert 56*slow*slow > phi*(2-p)**2
    # Log-series certificate and independent Decimal/libm evaluations.
    l3, u3 = log_interval(F(3))
    numerator = F(2, 627)
    gaplo, gaphi = numerator/u3, numerator/l3
    assert exp_partial(F(1099, 1000), 6) > 3
    assert numerator/F(1099, 1000) > F(29, 10000)
    pi = (dec(plo)+dec(phi))/2
    J = pi*D(2).sqrt()/(2*beta_series(F(3, 4), F(3, 4)))
    Ad = (14/pi).sqrt()*J
    pmills = D(240)/(67*(14*pi).sqrt()*(D(7)/2).exp())
    pgauss = 2-4*(7/(2*pi)).sqrt()*(dec(slow)+dec(shi))/2
    assert pgauss < pmills < dec(p)
    assert (14/pi).sqrt()*dec(F(21, 8)) < dec(A)
    assert D(1).exp() > dec(elo)
    assert dec(theta).exp() < dec(etheta_hi)
    gap = dec(numerator)/D(3).ln()
    assert dec(gaplo) < gap < dec(gaphi)
    assert abs(float(gap)-2/(627*math.log(3))) < 1e-17
    # A separate radial heat-equation expansion at initial radius 1.
    def spectral_exit(t):
        survival = (4/math.pi)*sum((-1)**j/(2*j+1)*
                     math.exp(-(2*j+1)**2*math.pi**2*t/8)
                     for j in range(30))
        return 1-survival
    def reflection_exit(t):
        return 2*sum((-1)**j*math.erfc((2*j+1)/math.sqrt(2*t))
                     for j in range(5))
    for t in (1/18, 1/7, 1/2, 1.0):
        spectral, reflected = spectral_exit(t), reflection_exit(t)
        assert abs(spectral-reflected) < 2e-14
        print(f"exit_CDF t={t:.16g}; radial_spectral={spectral:.16g}; "
              f"reflection={reflected:.16g}; difference={spectral-reflected:.3g}")
    actual_moment_bound = pgauss+Ad/(17*D(1).exp())
    print("Mills_polynomial_remainder=-120 verified")
    print(f"Gaussian_reflection_bound={pgauss}")
    print(f"Mills_upper_at_t_1_over_7={pmills}")
    print(f"certified_exit_upper={p} (two independent rational certificates)")
    print(f"weighted_energy_constant={Ad}")
    print(f"certified_energy_upper={A}")
    print(f"certified_e_lower={elo}; certified_exp_17_over_19_upper={etheta_hi}")
    print(f"rational_moment_upper={m}; rounded_moment_upper={mround}")
    print(f"unrounded_reflection_moment_bound={actual_moment_bound}")
    print(f"certified_tail_base={base}")
    print(f"tail_margin_below_1_over_3={F(1, 3)-base}")
    print(f"certified_tail_exponent={-dec(base).ln()/D(3).ln()}")
    print(f"gap_rational_interval=[{dec(gaplo)}, {dec(gaphi)}]")
    print(f"xi_upper={1-gap}")
    print(f"gap_ratio_to_round4={F(29, 19)}")
    print("ALL RADIAL-EXIT CERTIFICATE CHECKS PASSED")


if __name__ == "__main__":
    guard()
    getcontext().prec = 80
    if sys.argv[1:] == ["baseline"]:
        baseline()
    elif sys.argv[1:] == ["radial"]:
        radial()
    else:
        raise SystemExit("choose baseline or radial")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == "darwin" else rss*1024
    assert rss_bytes < 1024**3
    print(f"peak_RSS_bytes={rss_bytes}")
