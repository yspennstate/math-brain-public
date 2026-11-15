#!/usr/bin/env python3
"""Deterministic audits for PROOF.md. Standard library; no file writes."""
import ctypes
import math
import os
import resource
import sys
import time


def guard():
    libc = ctypes.CDLL(None, use_errno=True)
    libc.getpriority.argtypes = (ctypes.c_int, ctypes.c_uint)
    libc.getpriority.restype = ctypes.c_int
    ctypes.set_errno(0)
    priority = libc.getpriority(0, 0)
    assert not ctypes.get_errno() and priority >= 15, priority
    assert os.environ.get("OMP_NUM_THREADS") == "1"
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    print(f"niceness={priority}; threads=1; CPU cap=60s")


def simpson(fun, lo, hi, n=4096):
    if lo == hi:
        return 0.
    step = (hi-lo)/n
    return step/3 * math.fsum((fun(lo), fun(hi),
        4*math.fsum(fun(lo+i*step) for i in range(1, n, 2)),
        2*math.fsum(fun(lo+i*step) for i in range(2, n, 2))))


def close(x, y, tol=3e-9):
    assert abs(x-y) <= tol, (x, y, abs(x-y), tol)


def gamma(v):
    return v*math.exp(-v) if v > 0 else 0.


def tv(a):
    if not a:
        return 0.
    return -math.expm1(-a)*math.exp(-a/math.expm1(a))


def cdf_gap(v, a):
    # F(v)-F(v-a), stable for small a and v>=a.
    return math.exp(-v)*((1+v-a)*math.expm1(a)-a)


def maximize_gap(a):
    # Derivative-free independent location of the maximizing CDF gap.
    lo, hi = a, a+5
    for _ in range(100):
        left, right = (2*lo+hi)/3, (lo+2*hi)/3
        if cdf_gap(left, a) < cdf_gap(right, a):
            lo = left
        else:
            hi = right
    return cdf_gap((lo+hi)/2, a)


def bessel(n, r):
    # Independent defining-series implementation, for moderate r only.
    term = (r/2)**n/math.factorial(n)
    terms = [term]
    for k in range(1, 150):
        term *= -(r*r/4)/(k*(n+k))
        terms.append(term)
        if abs(term) < 1e-19:
            break
    return math.fsum(terms)


def main():
    guard()
    start = time.monotonic()

    # Recover normalization and two radial moments from the ORIGINAL
    # tilted exponential density, without sampling a gamma variable.
    max_moment_error = 0.
    for t in (-4., -1., -.1, 0., .1, 1., 4.):
        a = t*t
        normalizer = simpson(lambda u: (u-a)*math.exp(-u)/4,
                             a, a+45)
        close(normalizer, math.exp(-a)/4)
        moments = []
        for k in (0, 1, 2):
            raw = simpson(lambda u: u**k*(u-a)*math.exp(-u)/4,
                          a, a+45)/normalizer
            moments.append(raw)
        expected = (1., a+2, a*a+4*a+6)
        for got, want in zip(moments, expected):
            close(got, want, 2e-7)
            max_moment_error = max(max_moment_error, abs(got-want))
        # Same normalization independently gives the old saddle density.
        phi = math.exp(-a/2)/math.sqrt(2*math.pi)
        close(phi*normalizer/math.pi,
              math.exp(-1.5*a)/(4*math.pi*math.sqrt(2*math.pi)))
    print(f"original determinant tilt: 7 levels; max moment error={max_moment_error:.3e}")

    max_tv_error = 0.
    print("a, exact TV, half-L1 quadrature, independent max CDF gap:")
    for a in (1e-6, 1e-4, .01, .1, 1., 4., 16.):
        c = a/(-math.expm1(-a))
        integral = .5*math.fsum(simpson(
            lambda v: abs(gamma(v)-gamma(v-a)), lo, hi)
            for lo, hi in ((0., a), (a, c), (c, a+45)))
        got = tv(a)
        optimized = maximize_gap(a)
        close(integral, got)
        close(optimized, got, 1e-13)
        assert 0 < got <= min(1., a/math.e)*(1+1e-14)
        max_tv_error = max(max_tv_error, abs(integral-got))
        print(f"{a:.6g} {got:.12g} {integral:.12g} {optimized:.12g}")
    print(f"TV max quadrature error={max_tv_error:.3e}")
    for a in (.1, .03, .01):
        correction = (tv(a)-a/math.e)/(a**3)
        close(correction, -1/(24*math.e), 2e-5)
    print(f"TV cubic coefficient checked against {-1/(24*math.e):.12f}")

    # Substitution g=v^2 removes the integrable endpoint singularity.
    inverse_mean = simpson(lambda v: 2*v*v*math.exp(-v*v), 0, 10)
    close(inverse_mean, math.sqrt(math.pi)/2, 1e-12)
    for a in (1e-6, .01, 1., 16.):
        expected_amplitude_change = simpson(
            lambda v: 2*v**3*math.exp(-v*v)*2*a/
                      (math.sqrt(v*v+a)+v), 0, 10)
        assert 0 < expected_amplitude_change <= a*inverse_mean*(1+1e-13)
    print(f"coupling inverse-radius moment={inverse_mean:.12f}; four amplitude bounds passed")

    # Check the covariance normalization independently by the angular
    # spectral integral, and recover the latent radius from an annulus.
    r, s, theta, psi = 1.3, 2.1, .4, 1.1
    x, y = r*math.cos(theta), r*math.sin(theta)
    xx, yy = s*math.cos(psi), s*math.sin(psi)
    spectral = simpson(lambda alpha: math.cos(
        (x-xx)*math.cos(alpha)+(y-yy)*math.sin(alpha)),
        0, 2*math.pi)/(2*math.pi)
    mode_cov = bessel(0,r)*bessel(0,s)+2*math.fsum(
        bessel(n,r)*bessel(n,s)*math.cos(n*(theta-psi))
        for n in range(1, 30))
    close(spectral, mode_cov, 1e-12)
    print(f"angular spectral / Fourier covariance error={abs(spectral-mode_cov):.3e}")

    phase, g, radius = .73, 1.7, 1.3
    angles = [2*math.pi*j/256 for j in range(256)]
    j0, j2 = bessel(0,radius), bessel(2,radius)
    def field(t, angle):
        high = math.sqrt(2)*math.fsum(bessel(n,radius)*(
            math.cos(n)*math.cos(n*angle)+math.sin(n/2)*math.sin(n*angle))
            for n in range(3, 12))
        return (t*j0+2*math.sqrt(t*t+g)*j2*
                math.cos(2*angle-phase)+high)
    for t in (-2., 0., .1, 2.):
        values = [field(t, angle) for angle in angles]
        close(math.fsum(values)/len(values), t*j0, 1e-12)
        cosine = 2*math.fsum(v*math.cos(2*a) for v,a in zip(values,angles))/len(values)
        sine = 2*math.fsum(v*math.sin(2*a) for v,a in zip(values,angles))/len(values)
        recovered = (cosine*cosine+sine*sine)/(4*j2*j2)
        close(recovered, t*t+g, 1e-12)
        lam1, lam2 = (-t+math.sqrt(t*t+g))/2, (-t-math.sqrt(t*t+g))/2
        close(lam1*lam2, -g/4, 1e-12)
        assert lam1 > 0 > lam2
    print("four circle-mean / latent-radius / saddle-eigenvalue audits passed")

    # Stress the coupling near a flat saddle, with both signs of t,s.
    tests = 0
    for g in (1e-16, 1e-8, .1, 1., 100.):
        for t,s in ((0.,.1),(-.1,.1),(-2.,1.),(0.,4.)):
            a = abs(t*t-s*s)
            amplitude = 2*a/(math.sqrt(g+t*t)+math.sqrt(g+s*s))
            assert amplitude <= a/math.sqrt(g)*(1+1e-14)
            if t == -s:
                assert amplitude == 0
            tests += 1
    print(f"{tests} small-determinant / opposite-level coupling cases passed")

    elapsed = time.monotonic()-start
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = rss/(1024**2) if sys.platform == 'darwin' else rss/1024
    assert rss_mib < 1024 and elapsed < 60
    print(f"PASS; elapsed={elapsed:.3f}s; peak RSS={rss_mib:.2f} MiB")


if __name__ == '__main__':
    main()
