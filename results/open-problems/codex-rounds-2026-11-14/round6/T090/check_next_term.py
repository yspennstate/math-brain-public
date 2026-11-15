#!/usr/bin/env python3
"""Small audits and rational enclosures for the next Gaussian moment term.

OMP_NUM_THREADS=1 nice -n 15 python3 -B check_next_term.py
Only the Fraction bounds are certified; quadrature and ODE rows are diagnostics.
"""

import math
import os
import resource
import sys
import time
from fractions import Fraction as F

EULER = 0.57721566490153286060651209
LN2 = math.log(2)


def integrate(f, a, b, tol=2e-13):
    def rec(a, b, fa, fm, fb, whole, budget, depth):
        m = (a+b)/2
        fl, fr = f((a+m)/2), f((m+b)/2)
        left = (m-a)*(fa+4*fl+fm)/6
        right = (b-m)*(fm+4*fr+fb)/6
        delta = left+right-whole
        if abs(delta) <= 15*budget:
            return left+right+delta/15
        if depth == 0:
            raise ArithmeticError("quadrature depth exhausted")
        return rec(a, m, fa, fl, fm, left, budget/2, depth-1) + rec(
            m, b, fm, fr, fb, right, budget/2, depth-1)
    m = (a+b)/2
    fa, fm, fb = f(a), f(m), f(b)
    return rec(a, b, fa, fm, fb, (b-a)*(fa+4*fm+fb)/6, tol, 24)


def scaled_e1(u):
    # Continued fraction for exp(u)*E1(u), used only at u>=1.
    b = u+1
    c, d = 1e300, 1/b
    h = d
    for n in range(1, 400):
        an = -n*n
        b += 2
        d = 1/(an*d+b)
        c = b+an/c
        delta = c*d
        h *= delta
        if abs(delta-1) < 2e-15:
            return h
    raise ArithmeticError("continued fraction exhausted")


def ein(u):
    if u <= 1:
        term, total = u, u
        for n in range(2, 90):
            term *= -u/n
            add = term/n
            total += add
            if abs(add) < 2e-17:
                break
        return total
    return EULER+math.log(u)+math.exp(-u)*scaled_e1(u)


def cumulative(t):
    if t < 1:
        return -LN2*math.expm1(-t) + (1+math.exp(-t))*ein(t)-ein(2*t)
    # Algebraically equal to the small-t formula, but preserves the tail.
    e = math.exp(-t)
    return e*(ein(t)-LN2+scaled_e1(t))-e*e*scaled_e1(2*t)


def alternating_bounds(n, terms=60):
    # I_n=sum_{k>=0} (-1)^k (1/3)^(n+k)/(n+k).
    assert terms % 2 == 0
    lower = sum(((-1)**k * F(1, 3**(n+k)*(n+k))
                 for k in range(terms)), F(0))
    upper = lower+F(1, 3**(n+terms)*(n+terms))
    assert 0 < lower < upper
    return lower, upper


def certified_j(nmax=20):
    lower, upper = F(0), F(0)
    for n in range(1, nmax+1):
        lo, hi = alternating_bounds(n)
        lower += lo*lo/n
        upper += hi*hi/n
    tail = F(1, 9**(nmax+1)*(nmax+1)**3)*F(9, 8)
    return lower, upper+tail


def arctan_bounds(inverse, terms):
    assert terms % 2 == 0
    lower = sum(((-1)**k*F(1, (2*k+1)*inverse**(2*k+1))
                 for k in range(terms)), F(0))
    return lower, lower+F(1, (2*terms+1)*inverse**(2*terms+1))


def decimal_interval(lo, hi, digits=20):
    scale = 10**digits
    left = lo.numerator*scale//lo.denominator
    right = (hi.numerator*scale+hi.denominator-1)//hi.denominator
    def render(integer):
        return f"{integer//scale}.{integer%scale:0{digits}d}"
    return f"[{render(left)}, {render(right)}]"


def zero_energy(g, hmax):
    # Radial zero-energy scattering diagnostic, not a positive-energy solve.
    left, right = -40.0, math.log(80)
    n = math.ceil((right-left)/hmax)
    h, eta = (right-left)/n, g/(4*math.pi)
    f, p = 1.0, 0.0
    def acceleration(w, value):
        return -eta*math.exp(w-math.exp(w))*value
    for j in range(n):
        w = left+j*h
        k1f, k1p = p, acceleration(w, f)
        k2f = p+h*k1p/2
        k2p = acceleration(w+h/2, f+h*k1f/2)
        k3f = p+h*k2p/2
        k3p = acceleration(w+h/2, f+h*k2f/2)
        k4f = p+h*k3p
        k4p = acceleration(w+h, f+h*k3f)
        f += h*(k1f+2*k2f+2*k3f+k4f)/6
        p += h*(k1p+2*k2p+2*k3p+k4p)/6
    return f/p-right+4*math.pi/g-EULER+LN2


def main():
    start = time.monotonic()
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU,
                       (min(60, hard) if hard != resource.RLIM_INFINITY else 60, hard))
    print("CPU soft limit: 60 s; effective niceness:", os.getpriority(os.PRIO_PROCESS, 0))
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

    lo, hi = certified_j()
    print("certified J:", decimal_interval(lo, hi))
    print(f"exact rational interval width < {float(hi-lo):.3e}")
    j_series = float((lo+hi)/2)

    # Machin identity pi=16*atan(1/5)-4*atan(1/239).
    a_lo, a_hi = arctan_bounds(5, 40)
    b_lo, b_hi = arctan_bounds(239, 12)
    pi_lo, pi_hi = 16*a_lo-4*b_hi, 16*a_hi-4*b_lo
    d_lo, d_hi = lo/(64*pi_hi**3), hi/(64*pi_lo**3)
    c2_lo, c2_hi = lo/(16*pi_hi**2), hi/(16*pi_lo**2)
    print("certified d=<h,QAQ h>:", decimal_interval(d_lo, d_hi))
    print("certified C2 (log coefficient):", decimal_interval(c2_lo, c2_hi))

    # Check F via its positive mixture, independent of the E1 implementation.
    errors = []
    for t in (1e-5, .1, .99, 1, 1.01, 2, 10, 40):
        mixture = integrate(lambda p: math.exp(-t)*t if p == 0 else
                            math.exp(-t)*(-math.expm1(-p*t))/(p*(1+p)), 0, 1)
        errors.append(abs(cumulative(t)-mixture))
    assert max(errors) < 2e-12
    print(f"F vs positive mixture: 8 cases PASS; max error {max(errors):.3e}")

    radial = integrate(lambda w: cumulative(math.exp(w))**2, -36, math.log(80))
    kernel = integrate(lambda w: -2*math.exp(w)*math.exp(-math.exp(w)) *
                       (LN2-ein(math.exp(w)))*w*cumulative(math.exp(w)),
                       -36, math.log(80))
    def compact_integrand(x, y):
        z = x*y
        quotient = 1.0 if z == 0 else -math.log1p(-z)/z
        return quotient/((1+x)*(1+y))
    compact = integrate(lambda x: integrate(lambda y: compact_integrand(x,y),
                                           0, 1/3, 2e-14), 0, 1/3)
    print(f"J positive rational series: {j_series:.16f}")
    print(f"J radial F^2 integral:     {radial:.16f}")
    print(f"J direct log-max kernel:   {kernel:.16f}")
    print(f"J compact double integral:{compact: .16f}")
    for value in (radial, kernel, compact):
        assert abs(value-j_series) < 2e-11

    dilog = math.fsum(4.0**(-n)/(n*n) for n in range(1, 60))
    c1, c2 = dilog/(4*math.pi), j_series/(16*math.pi**2)
    print(f"C1={c1:.16f}; C2={c2:.16f}")
    print(f"relative order-g^2 coefficient C2+C1^2/2={c2+c1*c1/2:.16f}")
    print("zero-energy diagnostic: (residual-C1*g)/g^2 -> C2")
    print("g        adjusted coefficient    difference from C2    step difference")
    values = []
    for g in (.5, .25, .125, .0625):
        coarse = (zero_energy(g, .004)-c1*g)/(g*g)
        fine = (zero_energy(g, .002)-c1*g)/(g*g)
        values.append(fine)
        print(f"{g:<8g} {fine:.12f} {fine-c2: .3e} {abs(fine-coarse):.3e}")
        assert abs(fine-coarse) < 2e-8
    extrapolated = 2*values[-1]-values[-2]
    print(f"linear extrapolation: {extrapolated:.12f}; error {extrapolated-c2:.3e}")
    assert abs(extrapolated-c2) < 2e-7
    assert all(abs(a-c2) > abs(b-c2) for a,b in zip(values, values[1:]))

    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = raw if sys.platform == "darwin" else raw*1024
    print(f"elapsed seconds: {time.monotonic()-start:.3f}; peak RSS MiB: {rss/1024**2:.3f}")
    assert rss < 1024**3
    print("PASS: exact rational enclosures and independent floating-point diagnostics")


if __name__ == "__main__":
    main()
