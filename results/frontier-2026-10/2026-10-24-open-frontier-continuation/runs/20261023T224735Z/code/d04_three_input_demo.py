"""Reproduce the deterministic two-switch illustration in d04_transversality.md."""

import math
import numpy as np


def matrix_exp_negative(q, t):
    values, vectors = np.linalg.eigh(q)
    return (vectors * np.exp(-values * t)) @ vectors.T


def integrated(q, residual, t):
    eye = np.eye(q.shape[0])
    return np.linalg.solve(q, (eye - matrix_exp_negative(q, t)) @ residual)


def positive_root(func, lo, hi):
    assert func(lo) > 0.0 and func(hi) < 0.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if func(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


one = np.ones(3)
c = np.eye(3) + np.outer(one, one)
p = np.full(3, 0.5)
q0 = c + np.diag(p)
r0 = np.array([1.0, 6.0 / 5.0, 10.0])

# J_1(t)=0 reduces to 61 z^2+61 z-77=0 for z=exp(-3t/2).
z = (-61.0 + math.sqrt(22509.0)) / 122.0
tau = -(2.0 / 3.0) * math.log(z)
j_tau = integrated(q0, r0, tau)
r_tau = matrix_exp_negative(q0, tau) @ r0

q1 = q0.copy()
q1[0, 0] -= p[0]
j1_infinity = np.linalg.solve(q1, r0)
after_switch_j2 = lambda s: (j_tau + integrated(q1, r_tau, s))[1]
s = positive_root(after_switch_j2, 0.0, 1.0)
r_at_second = matrix_exp_negative(q1, s) @ r_tau

print("C=", c.tolist())
print("P=", p.tolist())
print("r0=", r0.tolist())
print("Q0=", q0.tolist())
print("first_phase_J_infinity=", np.linalg.solve(q0, r0).tolist())
print("first_return_time=", format(tau, ".12f"))
print("J_at_first_return=", [format(v, ".12f") for v in j_tau])
print("r_at_first_return=", [format(v, ".12f") for v in r_tau])
print("Q1=", q1.tolist())
print("second_phase_J_infinity=", j1_infinity.tolist())
print("second_return_elapsed=", format(s, ".12f"))
print("second_return_absolute_time=", format(tau + s, ".12f"))
print("r2_at_second_return=", format(r_at_second[1], ".12f"))
