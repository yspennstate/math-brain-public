#!/usr/bin/env python3
"""Small standard-library checks of the first Gaussian moment correction.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 -B check_correction.py
The ODE output is a zero-energy diagnostic, not a positive-energy eigenvalue.
"""

import math
import os
import resource
import sys
import time

EULER = 0.57721566490153286060651209


def integrate(f, a, b, tol=2e-12):
    def recurse(a, b, fa, fm, fb, whole, tol, depth):
        mid = (a+b)/2
        fl, fr = f((a+mid)/2), f((mid+b)/2)
        left = (mid-a)*(fa+4*fl+fm)/6
        right = (b-mid)*(fm+4*fr+fb)/6
        delta = left+right-whole
        if abs(delta) <= 15*tol:
            return left+right+delta/15
        if depth == 0:
            raise ArithmeticError("quadrature exhausted")
        return recurse(a, mid, fa, fl, fm, left, tol/2, depth-1) + recurse(
            mid, b, fm, fr, fb, right, tol/2, depth-1)

    mid = (a+b)/2
    fa, fm, fb = f(a), f(mid), f(b)
    return recurse(a, b, fa, fm, fb, (b-a)*(fa+4*fm+fb)/6, tol, 24)


def ein(u):
    if u <= 1:
        term, total = u, u
        for n in range(2, 80):
            term *= -u/n
            add = term/n
            total += add
            if abs(add) < 2e-17:
                return total
        return total
    # Continued fraction for E1(u), multiplied by exp(u).
    b = u+1
    c, d = 1e300, 1/b
    h = d
    for n in range(1, 300):
        an = -n*n
        b += 2
        d = 1/(an*d+b)
        c = b+an/c
        delta = c*d
        h *= delta
        if abs(delta-1) < 2e-15:
            return EULER+math.log(u)+math.exp(-u)*h
    raise ArithmeticError("continued fraction exhausted")


def exponential_average(f):
    return math.fsum(integrate(lambda u: math.exp(-u)*f(u), j, j+1, 5e-14)
                     for j in range(80))


def dilogarithm_quarter():
    return math.fsum(0.25**n/(n*n) for n in range(1, 60))


def zero_energy(g, hmax):
    # For u=r^2/(4s), w=log u, the radial equation is
    # f_ww=-[g/(4*pi)]*exp(w-exp(w))*f. Spatial scale s cancels.
    # Start at w=-40; the omitted regular-end correction is O(g*exp(-40)).
    left, right = -40.0, math.log(80)
    nsteps = math.ceil((right-left)/hmax)
    h = (right-left)/nsteps
    eta = g/(4*math.pi)
    f, p = 1.0, 0.0

    def acc(w, value):
        return -eta*math.exp(w-math.exp(w))*value

    for j in range(nsteps):
        w = left+j*h
        k1f, k1p = p, acc(w, f)
        k2f = p+h*k1p/2
        k2p = acc(w+h/2, f+h*k1f/2)
        k3f = p+h*k2p/2
        k3p = acc(w+h/2, f+h*k2f/2)
        k4f = p+h*k3p
        k4p = acc(w+h, f+h*k3f)
        f += h*(k1f+2*k2f+2*k3f+k4f)/6
        p += h*(k1p+2*k2p+2*k3p+k4p)/6
    # At the outer endpoint f=A+B*w up to the tiny Gaussian tail.
    ratio = f/p-right
    return (ratio+4*math.pi/g-EULER+math.log(2))/g


def main():
    start = time.monotonic()
    for name, kind, cap in (("CPU seconds", resource.RLIMIT_CPU, 60),
                            ("address space", resource.RLIMIT_AS, 256*1024**2)):
        try:
            soft, hard = resource.getrlimit(kind)
            requested = cap if hard == resource.RLIM_INFINITY else min(cap, hard)
            resource.setrlimit(kind, (requested, hard))
            print(f"soft limit {name}: {requested}")
        except (OSError, ValueError) as exc:
            print(f"soft limit {name} unavailable: {exc}")
    print("effective niceness:", os.getpriority(os.PRIO_PROCESS, 0))

    # Check the special-function implementation against its defining integral.
    errors = []
    for u in (0.0, 0.01, 0.5, 1.0, 1.01, 2.0, 5.0, 20.0, 80.0):
        direct = integrate(lambda t: u if t == 0 else -math.expm1(-t*u)/t, 0, 1)
        errors.append(abs(ein(u)-direct))
    assert max(errors) < 2e-11
    print(f"Ein vs defining integral: 9 cases PASS; max error {max(errors):.3e}")

    mean = exponential_average(ein)
    variance = exponential_average(lambda u: (ein(u)-math.log(2))**2)
    double_integral = integrate(
        lambda t: integrate(lambda q: 1/((1+t+q)*(1+t)*(1+q)), 0, 1, 2e-13),
        0, 1, 2e-12)
    series = dilogarithm_quarter()
    assert abs(mean-math.log(2)) < 2e-11
    assert abs(variance-series) < 2e-11
    assert abs(double_integral-series) < 2e-11
    print(f"E Ein(U): {mean:.15f}; log(2): {math.log(2):.15f}")
    print(f"Var Ein(U), radial quadrature: {variance:.15f}")
    print(f"covariance double integral:    {double_integral:.15f}")
    print(f"Li_2(1/4), positive series:    {series:.15f}")
    c = series/(16*math.pi**2)
    correction = series/(4*math.pi)
    print(f"c=||QAv||^2: {c:.15f}")
    print(f"relative/log correction C=4*pi*c: {correction:.15f}")
    for s in (0.001, 0.1, 1, 10, 1000):
        offset = (math.log(4*s)-EULER)/2
        mean_log = (math.log(8*s)-EULER)/2
        var_log = exponential_average(lambda u: (offset+ein(u)/2-mean_log)**2)
        assert abs(var_log/(4*math.pi**2)-c) < 2e-12
    print("Gaussian logarithmic-potential variance: 5 scale checks PASS")

    print("zero-energy ODE diagnostic only; adjusted residual / g -> C")
    print("g        residual/g         error from C       step-halving difference")
    values = []
    for g in (0.5, 0.25, 0.125, 0.0625, 0.03125):
        coarse, fine = zero_energy(g, 0.004), zero_energy(g, 0.002)
        values.append(fine)
        assert abs(coarse-fine) < 2e-8
        print(f"{g:<8g} {fine:.12f} {fine-correction: .3e} {abs(coarse-fine):.3e}")
    errors = [abs(value-correction) for value in values]
    assert all(a>b for a, b in zip(errors, errors[1:]))
    richardson = 2*values[-1]-values[-2]
    print(f"last two couplings, linear extrapolation: {richardson:.12f}")
    print(f"extrapolation error from C: {richardson-correction:.3e}")
    assert abs(richardson-correction) < 2e-7

    raw_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = raw_rss if sys.platform == "darwin" else raw_rss*1024
    print(f"elapsed seconds: {time.monotonic()-start:.3f}; peak RSS MiB: {rss/1024**2:.3f}")
    assert rss < 1024**3
    print("PASS: floating-point audits; the theorem does not depend on them")


if __name__ == "__main__":
    main()
