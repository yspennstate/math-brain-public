#!/usr/bin/env python3
"""Exact symbolic self-check for the perfect-correlation/disconnected flat mode.

This is not a global Phi certificate. It verifies the finite algebra used in the
P11 2026-09-16T19-11-51Z stuck report: for a diagonal strict two-site kernel
M=diag(alpha,beta), an off-diagonal Hermitian perturbation changes the four DPP
atom probabilities only through s=|z|^2 t^2, has zero quadratic entropy
curvature at t=0, and has a strictly negative quartic coefficient.
"""
import sympy as sp

alpha, beta, s = sp.symbols("alpha beta s", positive=True)

# Exact two-site DPP atoms along M_t=[[alpha,t z],[t z*,beta]],
# with s=|z|^2 t^2.
p0 = (1-alpha)*(1-beta) - s
p12 = alpha*beta - s
p1 = alpha*(1-beta) + s
p2 = beta*(1-alpha) + s
assert sp.expand(p0+p1+p2+p12) == 1

# Product-law cancellation at the diagonal base.
p0_0 = p0.subs(s, 0)
p12_0 = p12.subs(s, 0)
p1_0 = p1.subs(s, 0)
p2_0 = p2.subs(s, 0)
assert sp.expand(p0_0*p12_0-p1_0*p2_0) == 0

H = -sum(p*sp.log(p) for p in (p0,p12,p1,p2))
dH_ds_0 = sp.simplify(sp.expand_log(sp.diff(H,s).subs(s,0), force=True))
d2H_ds2_0 = sp.factor(sp.diff(H,s,2).subs(s,0))
expected_d2 = -1/(alpha*beta*(1-alpha)*(1-beta))
assert dH_ds_0 == 0
assert sp.simplify(d2H_ds2_0-expected_d2) == 0

# If s=|z|^2 t^2, then H(t)=H(0)+1/2 H_ss(0)|z|^4 t^4+O(t^6).
# Thus the t-Hessian vanishes and the quartic coefficient is strictly negative
# for 0<alpha,beta<1 and z != 0.
print("status=PASS")
print("scope=exact_two_site_flat_mode_only_not_global_Phi")
print("dH_ds_at_0=0")
print("d2H_ds2_at_0=-1/(alpha*beta*(1-alpha)*(1-beta))")
print("t2_coefficient=0")
print("t4_coefficient=-|z|^4/(2*alpha*beta*(1-alpha)*(1-beta))")
