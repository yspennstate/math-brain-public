#!/usr/bin/env python3
"""Deterministic, standard-library audits for PROOF.md.

No finite-coupling eigenvalues or rigorous numerical intervals are claimed.
Run with OMP_NUM_THREADS=1 nice -n 15 python3 -B check_prefactor.py
"""

import math
import resource
import sys
import time

EULER = 0.57721566490153286060651209


def integrate(f, a, b, tol=2e-12):
    """Adaptive Simpson quadrature; recursion storage is bounded by 24 levels."""
    def rec(a, b, fa, fm, fb, whole, tol, depth):
        mid = (a + b) / 2
        fl = f((a + mid) / 2)
        fr = f((mid + b) / 2)
        left = (mid - a) * (fa + 4 * fl + fm) / 6
        right = (b - mid) * (fm + 4 * fr + fb) / 6
        delta = left + right - whole
        if abs(delta) < 15 * tol:
            return left + right + delta / 15
        if depth == 0:
            raise ArithmeticError("quadrature depth exhausted")
        return rec(a, mid, fa, fl, fm, left, tol / 2, depth - 1) + rec(
            mid, b, fm, fr, fb, right, tol / 2, depth - 1
        )

    mid = (a + b) / 2
    fa, fm, fb = f(a), f(mid), f(b)
    return rec(a, b, fa, fm, fb, (b - a) * (fa + 4 * fm + fb) / 6, tol, 24)


def panel_integral(f, a, b):
    n = max(1, math.ceil(b - a))
    return sum(integrate(f, a + (b-a)*j/n, a + (b-a)*(j+1)/n)
               for j in range(n))


def log_integral(weight):
    # For 0<u<1 use u=exp(-w); for u>=1 use the original variable.
    # Tails beyond w=50 and u=80 are negligible at the printed precision.
    return integrate(lambda w: -w * weight(math.exp(-w)) * math.exp(-w), 0, 50) + integrate(
        lambda u: weight(u) * math.log(u), 1, 80
    )


def zero_energy_coefficients(g, step):
    """Radial zero-energy ODE in w=log(r^2/(4s)); s scales out.

    F''(w)=-eta*exp(w-exp(w))*F(w), eta=g/(4*pi).
    At large w, F=A+B*w. This is a diagnostic, not a positive-energy solve.
    """
    eta = g / (4 * math.pi)
    left, right = -32.0, math.log(80.0)
    n = math.ceil((right-left) / step)
    h = (right-left) / n
    f, derivative = 1.0, 0.0

    def acceleration(w, f):
        return -eta * math.exp(w - math.exp(w)) * f

    for j in range(n):
        w = left + j*h
        k1f = derivative
        k1d = acceleration(w, f)
        k2f = derivative + h*k1d/2
        k2d = acceleration(w+h/2, f+h*k1f/2)
        k3f = derivative + h*k2d/2
        k3d = acceleration(w+h/2, f+h*k2f/2)
        k4f = derivative + h*k3d
        k4d = acceleration(w+h, f+h*k3f)
        f += h*(k1f+2*k2f+2*k3f+k4f)/6
        derivative += h*(k1d+2*k2d+2*k3d+k4d)/6
    return f-right*derivative, derivative


def main():
    start = time.monotonic()
    for label, kind, cap in (
        ("CPU seconds", resource.RLIMIT_CPU, 60),
        ("address space", resource.RLIMIT_AS, 256*1024**2),
    ):
        try:
            soft, hard = resource.getrlimit(kind)
            requested = cap if hard == resource.RLIM_INFINITY else min(cap, hard)
            resource.setrlimit(kind, (requested, hard))
            print(f"soft resource limit {label}: {requested}")
        except (OSError, ValueError) as exc:
            print(f"soft resource limit {label} unavailable: {exc}")

    log_exp = log_integral(lambda u: math.exp(-u))
    log_max = log_integral(lambda u: 2*math.exp(-u)*(-math.expm1(-u)))
    assert abs(log_exp + EULER) < 2e-10
    assert abs(log_max - (math.log(2)-EULER)) < 2e-10
    print(f"integral exp(-u) log(u): {log_exp:.14f}; expected {-EULER:.14f}")
    print(f"E log(max(U,V)): {log_max:.14f}; expected {math.log(2)-EULER:.14f}")

    max_distance_error = 0.0
    for s in (0.01, 0.5, 1.0, 3.0, 100.0):
        convolution = (math.log(8*s) + log_exp) / 2
        angular = (math.log(4*s) + log_max) / 2
        theory = (math.log(8*s) - EULER) / 2
        max_distance_error = max(max_distance_error, abs(convolution-angular), abs(convolution-theory))
        a = (math.log(2)-EULER-convolution)/(2*math.pi)
        prefactor = math.exp(4*math.pi*a)
        assert abs(prefactor / (math.exp(-EULER)/(2*s)) - 1) < 2e-10
    print(f"5 covariance scales: log-distance/prefactor checks PASS; max discrepancy {max_distance_error:.3e}")
    print(f"s=1 prefactor: {math.exp(-EULER)/2:.14f}")

    print("heat resolvent: a, J(a)+log(a), error from -2*Euler")
    for a in (1e-2, 1e-6, 1e-12, 1e-30):
        y = math.log(a)
        j = panel_integral(lambda w: math.exp(-math.exp(w)-math.exp(y-w)), y-math.log(80), math.log(80))
        remainder = j+y+2*EULER
        assert abs(remainder) <= 4*math.sqrt(a) + 2e-10
        if a <= 1e-12:
            assert abs(remainder) < 1e-9
        print(f"{a:8.1e} {j+y: .14f} {remainder: .3e}")

    print("zero-energy ODE diagnostic (not finite-g eigenvalues)")
    print("g        A/B+4*pi/g         residual from Euler-log(2)    step discrepancy")
    largest_step_error = 0.0
    residuals = []
    for g in (2.0, 1.0, 0.5, 0.25, 0.125):
        a1, b1 = zero_energy_coefficients(g, 0.004)
        a2, b2 = zero_energy_coefficients(g, 0.002)
        step_error = abs(a1/b1-a2/b2)
        largest_step_error = max(largest_step_error, step_error)
        assert step_error < 1e-8
        adjusted = a2/b2 + 4*math.pi/g
        residual = adjusted - EULER + math.log(2)
        residuals.append(abs(residual))
        print(f"{g:<7g} {adjusted: .12f} {residual: .12f} {step_error:.3e}")
    assert all(a > b for a, b in zip(residuals, residuals[1:]))
    assert residuals[-1] < 0.004
    print(f"max RK4 step discrepancy: {largest_step_error:.3e}")

    elapsed = time.monotonic()-start
    raw_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = raw_rss if sys.platform == "darwin" else raw_rss*1024
    print(f"elapsed seconds: {elapsed:.3f}; peak RSS MiB: {rss/1024**2:.3f}")
    assert rss < 1024**3
    print("PASS: floating-point audits only; the theorem is proved analytically in PROOF.md")


if __name__ == "__main__":
    main()
