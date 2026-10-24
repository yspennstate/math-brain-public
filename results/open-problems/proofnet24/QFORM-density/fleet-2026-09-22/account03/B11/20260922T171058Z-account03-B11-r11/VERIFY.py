#!/usr/bin/env python3
"""Regression checks for the ruled-majority-sheet QFORM theorem.

This is algebraic/numerical regression only; the proof is in REPORT.md.
Uses only the Python standard library.
"""
import math
import random


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def sub(a, b):
    return [x-y for x, y in zip(a, b)]


def scale(c, a):
    return [c*x for x in a]


def random_two_frame(rng):
    while True:
        a = [rng.uniform(-1, 1) for _ in range(3)]
        na = norm(a)
        if na > 1e-8:
            u = scale(1/na, a)
            break
    while True:
        b = [rng.uniform(-1, 1) for _ in range(3)]
        b = sub(b, scale(dot(b, u), u))
        nb = norm(b)
        if nb > 1e-8:
            v = scale(1/nb, b)
            return u, v


def q(x):
    return x[0]*x[0] + x[1]*x[1] - x[2]*x[2]


def ruling_point(a, phi, t):
    return [
        a*math.cos(phi) - t*math.sin(phi),
        a*math.sin(phi) + t*math.cos(phi),
        t,
    ]


def ruling_direction(phi):
    return [-math.sin(phi), math.cos(phi), 1.0]


def main():
    rng = random.Random(20260922171058)

    # Geometry: every t-curve lies on q=a^2 and has speed sqrt(2).
    max_q_error = 0.0
    max_speed_error = 0.0
    for _ in range(5000):
        a = 10 ** rng.uniform(-2, 2)
        phi = rng.uniform(-math.pi, math.pi)
        t = rng.uniform(-100, 100)
        p = ruling_point(a, phi, t)
        max_q_error = max(max_q_error, abs(q(p) - a*a))
        d = ruling_direction(phi)
        max_speed_error = max(max_speed_error, abs(dot(d, d) - 2.0))
    assert max_q_error < 2e-10, max_q_error
    assert max_speed_error < 1e-12, max_speed_error

    # Scaling: if D^2>=I and U is an orthonormal 3x2 frame, G=U^T D^2 U>=I.
    min_diag_slack = float('inf')
    min_det_G = float('inf')
    min_det_slack_matrix = float('inf')
    for _ in range(10000):
        u, v = random_two_frame(rng)
        d2 = [1.0 + 9.0*rng.random() for _ in range(3)]
        guu = sum(d2[i]*u[i]*u[i] for i in range(3))
        gvv = sum(d2[i]*v[i]*v[i] for i in range(3))
        guv = sum(d2[i]*u[i]*v[i] for i in range(3))
        detg = guu*gvv - guv*guv
        a11 = guu - 1.0
        a22 = gvv - 1.0
        det_slack = a11*a22 - guv*guv
        min_diag_slack = min(min_diag_slack, a11, a22)
        min_det_slack_matrix = min(min_det_slack_matrix, det_slack)
        min_det_G = min(min_det_G, detg)
        assert a11 >= -2e-12
        assert a22 >= -2e-12
        assert det_slack >= -3e-12
        assert detg >= 1.0 - 3e-12

    constant = math.pi * math.e / math.sqrt(2.0)
    print(f"majority_sheet_constant_pi_e_over_sqrt2={constant:.15f}")
    print(f"max_q_ruling_error={max_q_error:.3e}")
    print(f"max_ruling_speed_sq_error={max_speed_error:.3e}")
    print(f"min_G_diag_slack={min_diag_slack:.6e}")
    print(f"min_det_G={min_det_G:.12f}")
    print(f"min_det_G_minus_I={min_det_slack_matrix:.6e}")
    print("QFORM_RULED_MAJORITY_SHEET_CHECK_PASS")


if __name__ == "__main__":
    main()
