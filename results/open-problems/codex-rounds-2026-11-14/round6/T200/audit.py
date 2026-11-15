"""Exact rational certificates and separate floating-point diagnostics.

Uses only the standard library; writes no files. See LOG.md for commands.
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


def decimal(x):
    x = F(x)
    return D(x.numerator)/D(x.denominator)


def exp_bounds(x, n=50):
    assert 0 < x < n+2
    term, lo = F(1), F(1)
    for j in range(1, n+1):
        term *= x/j
        lo += term
    return lo, lo + term*x/(n+1)/(1-x/(n+2))


def log_bounds(x, n=160):
    assert x > 1
    z = (x-1)/(x+1)
    lo = 2*sum((z**(2*j+1)/(2*j+1) for j in range(n)), F(0))
    return lo, lo+2*z**(2*n+1)/((2*n+1)*(1-z*z))


def pi_bounds():
    def atan(x, n):
        return sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(n)), F(0))
    assert 16*atan(F(1, 5), 8)-4*atan(F(1, 239), 5) > F(314159, 100000)
    return (16*atan(F(1, 5), 40)-4*atan(F(1, 239), 21),
            16*atan(F(1, 5), 41)-4*atan(F(1, 239), 20))


def energy_certificate():
    coeff, partial = F(1), F(0)
    for j in range(8):
        partial += coeff/(2**j*(j+F(3, 4)))
        coeff *= (j+F(1, 4))/(j+1)
    assert partial == F(112206509213551, 78752847495168)
    assert partial > F(178, 125)
    assert 2*F(22, 7)**4 < F(21, 8)**4*F(178, 125)**4
    return F(21, 8)


def gaussian_bound_by_integration(v, a, p):
    # 2a Phi_bar(sqrt(v)) = a - 2a sqrt(v/(2pi))*S.
    # S is the integrated Taylor series of exp(-v u^2/2) on [0,1].
    v, a, p = F(v), F(a), F(p)
    _, pi_hi = pi_bounds()
    n = 80
    assert v/2 < n
    lower = sum(((-v/2)**j/(math.factorial(j)*(2*j+1))
                 for j in range(n)), F(0))
    assert lower > 0 and a > p
    assert 2*a*a*v*lower*lower > pi_hi*(a-p)**2


def baseline():
    pi_lo, _ = pi_bounds()
    j_hi = energy_certificate()
    p, energy_hi = F(16311, 1000000), F(27707, 5000)
    gaussian_bound_by_integration(F(7), F(2), p)
    assert energy_hi**2*pi_lo > 14*j_hi**2
    e_lo, _ = exp_bounds(F(1))
    m = p+energy_hi/(17*e_lo)
    m_hi = F(13623, 100000)
    assert m < m_hi
    _, exp_hi = exp_bounds(F(17, 19))
    assert exp_hi < F(24467, 10000)
    beta = m_hi*F(24467, 10000)
    assert beta == F(333313941, 1000000000) and 3*beta < 1
    g = F(1, 3)-F(3, 11)
    assert g == F(2, 33)
    lo, hi = log_bounds(F(3))
    gap_lo, gap_hi = g/(19*hi), g/(19*lo)
    assert gap_lo > F(29, 10000)
    gap = decimal(g)/(19*D(3).ln())
    assert decimal(gap_lo) < gap < decimal(gap_hi)
    assert abs(float(gap)-2/(627*math.log(3))) < 1e-17
    j_gamma = math.pi**1.5/(math.sqrt(2)*math.gamma(0.75)**2)
    assert abs(j_gamma-2.6220575542921198) < 1e-14
    print(f"J_independent_gamma={j_gamma:.16g}")
    print(f"round5_gaussian_rational_upper={p}")
    print(f"round5_moment_rational_upper={m_hi}")
    print(f"round5_tail_base={beta}; three_times_numerator={3*beta.numerator}")
    print(f"round5_tail_exponent={-decimal(beta).ln()/D(3).ln()}")
    print(f"round5_xi_upper={1-gap}")
    print("ROUND 5 RESULT VERIFIED independently")


def geometry():
    a, b, v = F(19, 10), F(17, 5), F(73, 10)
    t, s, c = (a-1)**2/v, F(43, 2), F(5, 121)
    assert t == F(81, 730) and s*c == F(215, 242)
    # Degree at most ten: eleven exact values verify the Mills polynomial.
    for x in range(11):
        P, Q = x**4+9*x*x+8, x**5+10*x**3+15*x
        Pd, Qd = 4*x**3+18*x, 5*x**4+30*x*x+15
        assert Pd*Q-P*Qd-x*P*Q+Q*Q == -120
    pi_lo, _ = pi_bounds()
    pi0, h0 = F(314159, 100000), F(3847, 100)
    assert pi_lo > pi0
    assert exp_bounds(v/2, 32)[0] > h0
    p, A, elo = F(1311, 100000), F(629, 100), F(1359, 500)
    H = (v*v+9*v+8)/(v*v+10*v+15)
    assert H == F(12699, 14129)
    # p > a sqrt(2/(pi v)) exp(-v/2) H: squared positive quantities.
    assert p*p*pi0*v*h0*h0 > 2*a*a*H*H
    gaussian_bound_by_integration(v, a, p)
    jhi = energy_certificate()
    assert A*A*pi0 > 2*jhi*jhi/t
    assert exp_bounds(F(1), 7)[0] > elo
    moment = p+A/(s*elo)
    m, E = F(151, 1250), F(304, 125)
    assert moment < m and exp_bounds(s*c, 16)[1] < E
    beta = m*E
    assert beta == F(22952, 78125)
    assert b*beta == F(390184, 390625) < 1
    g = 1/(1+a)-b/(b*b+a)
    assert g == F(1800, 19517)
    assert g == (b-1)*(b-a)/((1+a)*(b*b+a))
    # Independent expression from the Green kernel's d,D form.
    d = 1+a
    green_D = (b*b-1)*(b*b-a*a)/(b*b)
    assert d*d+green_D == ((b*b+a)/b)**2
    assert 0 < g*a < 1
    numerator = g*c
    assert numerator == F(9000, 2361557)
    loglo, loghi = log_bounds(b)
    gaplo, gaphi = numerator/loghi, numerator/loglo
    assert exp_bounds(F(49, 40), 10)[0] > b
    coarse = numerator/F(49, 40)
    assert coarse == F(360000, 115716293) > F(31, 10000)
    assert gaplo > coarse
    gap = decimal(numerator)/decimal(b).ln()
    assert decimal(gaplo) < gap < decimal(gaphi)
    assert abs(float(gap)-float(g)*float(c)/math.log(float(b))) < 1e-17
    # Improvement checked independently without subtracting close xi bounds.
    old_loglo, old_loghi = log_bounds(F(3))
    oldgap_hi = F(2, 627)/old_loglo
    assert gaplo > oldgap_hi
    print(f"a={a}; b={b}; v={v}; time={t}; s={s}; c={c}")
    print(f"certified_exit_upper={p}; certified_energy_upper={A}")
    print(f"moment_rational_upper_before_rounding={moment}")
    print(f"rounded_moment_upper={m}; exp_sc_upper={E}")
    print(f"tail_base={beta}; b_times_tail_base={b*beta}")
    print(f"tail_margin_integer={390625-390184}")
    print(f"tail_exponent={-decimal(beta).ln()/decimal(b).ln()}")
    print(f"green_constant={g}; gap_numerator={numerator}")
    print(f"coarse_gap_lower={coarse} > 31/10000")
    print(f"gap_interval=[{decimal(gaplo)}, {decimal(gaphi)}]")
    print(f"xi_upper={1-gap}")
    print(f"gap_ratio_to_round5={gap/(decimal(F(2,627))/D(3).ln())}")
    print("ALL GEOMETRY CERTIFICATE CHECKS PASSED")


def diagnostics():
    # Two representations of the general radial exit CDF. No randomness.
    def spectral(a, t):
        return 1-sum(2*a*(-1)**(n+1)/(n*math.pi)*math.sin(n*math.pi/a)*
                     math.exp(-n*n*math.pi**2*t/(2*a*a))
                     for n in range(1, 501))
    def images(a, t):
        return a*sum(math.erfc(((2*n+1)*a-1)/math.sqrt(2*t))-
                     math.erfc(((2*n+1)*a+1)/math.sqrt(2*t))
                     for n in range(80))
    maxerror = 0.
    for a in (1.2, 1.9, 2., 3.):
        for t in (81/730, .25, .5, 1.):
            first, second = spectral(a,t), images(a,t)
            upper = a*math.erfc((a-1)/math.sqrt(2*t))
            maxerror = max(maxerror, abs(first-second))
            assert abs(first-second) < 3e-14 and 0 <= second <= upper
            if a == 1.9:
                print(f"radial_CDF a={a}; t={t:.16g}; spectral={first:.16g}; "
                      f"images={second:.16g}; upper={upper:.16g}")
    # Check Green formula on a finite radius/angle grid; the proof is analytic.
    a, b = 1.9, 3.4
    g = 1/(1+a)-b/(b*b+a)
    mingreen = float('inf')
    for i in range(21):
        x = i/20
        for j in range(21):
            y = a*j/20
            for k in range(21):
                costheta = -1+k/10
                dsq = x*x+y*y-2*x*y*costheta
                if dsq < 1e-14:
                    continue
                DD = (b*b-x*x)*(b*b-y*y)/(b*b)
                value = 1/math.sqrt(dsq)-1/math.sqrt(dsq+DD)
                assert value >= g-1e-14
                mingreen = min(mingreen, value)
    assert abs(mingreen-g) < 1e-14
    print(f"max_radial_CDF_discrepancy={maxerror:.4g}")
    print(f"grid_Green_minimum={mingreen:.16g}; formula={g:.16g}")
    J = math.pi**1.5/(math.sqrt(2)*math.gamma(.75)**2)
    t, s, c = 81/730, 21.5, 5/121
    p = a*math.erfc((a-1)/math.sqrt(2*t))
    mean = J*math.sqrt(2/(math.pi*t))
    m = p+mean/(math.e*s)
    print(f"unrounded_gaussian_upper={p:.16g}; actual_mean_energy={mean:.16g}")
    print(f"unrounded_moment_bound={m:.16g}; unrounded_tail_base={math.exp(s*c)*m:.16g}")
    print("GEOMETRY DIAGNOSTICS PASSED (not a proof certificate)")


if __name__ == "__main__":
    guard()
    getcontext().prec = 130
    if sys.argv[1:] == ["baseline"]:
        baseline()
    elif sys.argv[1:] == ["geometry"]:
        geometry()
    elif sys.argv[1:] == ["diagnostics"]:
        diagnostics()
    else:
        raise SystemExit("choose baseline, geometry or diagnostics")
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == "darwin" else rss*1024
    assert rss_bytes < 1024**3
    print(f"peak_RSS_bytes={rss_bytes}")
