#!/usr/bin/env python3
"""Exact symbolic self-check for C29-DC34-EXACT-HULL-03.

This does not replace the written proof.  It verifies the directional
second derivatives, algebraic identities for the lower boundary, endpoint
chords, and non-affineness of the two curved boundary pieces.
"""
import sympy as sp

s, t, a, r = sp.symbols("s t a r", positive=True)

g = s*t
q2 = s*t - t*(1-t)/a
ell = s+t-1

def d2(f, vec):
    H = sp.hessian(f, (s,t))
    v = sp.Matrix(vec)
    return sp.factor((v.T*H*v)[0])

def check(name, got, expected):
    got = sp.factor(got)
    expected = sp.factor(expected)
    ok = sp.simplify(got-expected) == 0
    print(f"{name}: got={got}; expected={expected}; PASS={ok}")
    if not ok:
        raise AssertionError(name)

# Directional convexity / concavity checks for e_s, e_t, and d=(1,-a).
check("g_horizontal_second", d2(g,(1,0)), 0)
check("g_vertical_second", d2(g,(0,1)), 0)
check("g_third_second", d2(g,(1,-a)), -2*a)
check("q2_horizontal_second", d2(q2,(1,0)), 0)
check("q2_vertical_second", d2(q2,(0,1)), 2/a)
check("q2_third_second", d2(q2,(1,-a)), 0)

# Put r=t+a*s.  Then q2=t(r-1)/a on a third-direction fiber.
check("q2_r_form", q2.subs(s,(r-t)/a), t*(r-1)/a)
check("q2_minus_ell_factor", q2-ell, (t-1)*(a*s-a+t)/a)

# Endpoint chord identities in the middle and upper r-regimes.
# Middle regime 1<=r<=a: endpoints are s=(r-1)/a,t=1 and s=r/a,t=0.
check("middle_q2_top_endpoint", q2.subs({s:(r-1)/a,t:1}), (r-1)/a)
check("middle_q2_bottom_endpoint", q2.subs({s:r/a,t:0}), 0)
# Upper regime a<=r<=a+1: endpoints are s=(r-1)/a,t=1 and s=1,t=r-a.
check("upper_ell_top_endpoint", ell.subs({s:(r-1)/a,t:1}), (r-1)/a)
check("upper_ell_right_endpoint", ell.subs({s:1,t:r-a}), r-a)

Hg = sp.hessian(g,(s,t))
Hq = sp.hessian(q2,(s,t))
print("Hessian_g=", Hg.tolist(), "det=", sp.factor(Hg.det()))
print("Hessian_q2=", Hq.tolist(), "det=", sp.factor(Hq.det()))
if sp.factor(Hg.det()) != -1 or sp.factor(Hq.det()) != -1:
    raise AssertionError("curved boundary Hessian determinant")

print("ALL_EXACT_CHECKS_PASS")
