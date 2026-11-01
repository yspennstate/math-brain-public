#!/usr/bin/env python3
"""PROB10-03 / R14 bounded-run self-check.

EXACT part:
  * verifies the rational centered-Hessian contraction compiler;
  * verifies the rational Psi Taylor lower bound.

NUMERICAL_ONLY part:
  * scouts the B->0 boundary equation for the complete second lift.

No numerical value in this file is a rigorous source-bracket endpoint.
"""
from fractions import Fraction as Q
import itertools
import math
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import brentq
from scipy.special import ndtr

# Fixed rational preconditioner from the previous R14 certificate.
A11, A12 = Q(-1601, 20), Q(-493, 12500)
A21, A22 = Q(-60418, 25), Q(-5789, 2500)

# New smaller weighted box: |p-p_c| <= 1/2000, |B-B_c| <= 1/50.
rp, rB = Q(1, 2000), Q(1, 50)

# The centered-Hessian hypotheses in the companion proof imply these
# whole-box Jacobian intervals exactly.
Jbounds = [
    [Q(-131, 5000), Q(-63, 2500)],   # H_p
    [Q(81, 200000), Q(19, 40000)],   # H_B
    [Q(5337, 200), Q(5403, 200)],    # alpha_p
    [Q(-114, 125), Q(-217, 250)],    # alpha_B
]

worst = None
for j11, j12, j21, j22 in itertools.product(*Jbounds):
    m11 = 1 - (A11*j11 + A12*j21)
    m12 = -(A11*j12 + A12*j22)
    m21 = -(A21*j11 + A22*j21)
    m22 = 1 - (A21*j12 + A22*j22)
    scaled = (m11, m12*rB/rp, m21*rp/rB, m22)
    norm = max(abs(scaled[0]) + abs(scaled[1]),
               abs(scaled[2]) + abs(scaled[3]))
    if worst is None or norm > worst[0]:
        worst = (norm, (j11, j12, j21, j22), scaled)

q = worst[0]
assert q == Q(62439, 312500)
assert q < 1

# Deliberately loose center residual hypothesis.
eps_H = Q(1, 10**6)
eps_alpha = Q(1, 50000)
eta = max((abs(A11)*eps_H + abs(A12)*eps_alpha)/rp,
          (abs(A21)*eps_H + abs(A22)*eps_alpha)/rB)
assert eta == Q(202097, 1250000)
assert eta < 1 - q

print("EXACT_CENTERED_HESSIAN_COMPILER_PASS")
print("q", q, float(q))
print("1-q", 1-q, float(1-q))
print("eta", eta, float(eta))
print("eta_lt_1_minus_q", eta < 1-q)
print("worst_vertex", worst[1])
print("worst_scaled_matrix", worst[2])

# Psi Taylor compiler.  Hypotheses on Q:
# Psi(center) >= 7/500,
# |Psi_p(center)| <= 1, |Psi_B(center)| <= 1/25,
# |Psi_pp| <= 2, |Psi_pB| <= 1/5, |Psi_BB| <= 1/20.
psi_lower = (Q(7, 500) - rp - Q(1, 25)*rB
             - Q(1, 2)*(Q(2)*rp*rp
                        + 2*Q(1, 5)*rp*rB
                        + Q(1, 20)*rB*rB))
assert psi_lower == Q(50751, 4000000)
assert psi_lower > 0
print("psi_lower", psi_lower, float(psi_lower))
print("psi_positive", psi_lower > 0)

# NUMERICAL_ONLY scout of the boundary equation derived in the proof artifact.
# u(x)=(x-1)_+, r_p=T_{sqrt(p)}u, and the B->0/D->1 boundary condition is
# E[r_p(Z)^2] = p E[u(G)^2].
n = 300
hn, hw = hermgauss(n)
z = hn*np.sqrt(2.0)
w = hw/np.sqrt(np.pi)
phi = lambda x: np.exp(-x*x/2)/np.sqrt(2*np.pi)
mu1 = float(np.sum(w*np.maximum(z-1, 0)**2))

def boundary_F(p):
    s = math.sqrt(1-p)
    mu = math.sqrt(p)*z - 1
    a = mu/s
    r = mu*ndtr(a) + s*phi(a)
    return float(np.sum(w*r*r) - p*mu1)

root_p = brentq(boundary_F, 0.1, 0.2)
print("NUMERICAL_ONLY_boundary_mu1", repr(mu1))
print("NUMERICAL_ONLY_boundary_root_p", repr(root_p))
print("NUMERICAL_ONLY_F_root", repr(boundary_F(root_p)))
print("ALL_SELF_CHECKS_PASS")
