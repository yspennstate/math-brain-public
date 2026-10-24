#!/usr/bin/env python3
"""
Targeted certificate for the account04/B14 FEI existential-selector run.

Family: disjoint width-w tribes with s tribes. This is NOT a full-FEI
certificate.  It verifies the repaired low-influence selector
    B_i + j(p_i) <= C_H p_i
for every member of this structured family (hence in particular every low-influence member).

The proof in REPORT.md derives all formulas. Here we:
  * evaluate finite width-2 cases with interval arithmetic (s=1 is exact);
  * certify an analytic width-2 tail using a monotone upper envelope;
  * interval-subdivide the same upper envelope for widths 3 and 4;
  * certify an elementary width>=5 uniform upper bound;
  * report exact restriction ratio Delta_i H / p_i and H/I separately.

Only mpmath interval arithmetic is used for numerical inequalities.
"""
import json
from fractions import Fraction
import mpmath as mp
from mpmath import iv

mp.mp.dps = 80

C_H_DEC = "6.4547837"
TAU_H_DEC = "0.1805540237871973049"
C_H = mp.mpf(C_H_DEC)
TAU_H = mp.mpf(TAU_H_DEC)

def h_mp(x):
    x = mp.mpf(x)
    if x == 0 or x == 1:
        return mp.mpf(0)
    return -x*mp.log(x, 2) - (1-x)*mp.log(1-x, 2)

def j_mp(x):
    x = mp.mpf(x)
    if x == 0:
        return mp.mpf(0)
    return 1 - h_mp(mp.mpf("0.5") + mp.sqrt(x*(1-x)))

def h_iv(x):
    return -(x*iv.ln(x) + (1-x)*iv.ln(1-x))/iv.ln(2)

def j_iv(x):
    return 1 - h_iv(iv.mpf("0.5") + iv.sqrt(x*(1-x)))

def lo(x):
    return float(x.a)

def hi(x):
    return float(x.b)

def istr(x):
    return [repr(lo(x)), repr(hi(x))]

def exact_p(w, s):
    # p = 2/(2^w) * ((2^w-1)/2^w)^(s-1)
    b = 2**w
    a = b-1
    return Fraction(2 * a**(s-1), b**s)

def tribes_mp(w, s):
    a = mp.mpf(2**w-1)
    b = a+1
    q = a/b
    p = mp.mpf(2)/b * q**(s-1)
    WA = 2*p*(a-1)/b
    WB = (a*a+1)*(2*p/b-p*p)
    x0 = (1-a*p)**2
    WC = x0+p*p
    t = 1/(a*a+1)
    t0 = p*p/WC
    B = WA + WB*h_mp(t) + WC*h_mp(t0)
    JS = WA + WB*j_mp(t) + WC*j_mp(t0)
    Delta = B+JS
    R = (B+j_mp(p))/p

    # Full spectral entropy without truth-table expansion:
    # empty mass (2 q^s - 1)^2; for m active blocks, each nonempty
    # subset choice in each block has common squared coefficient c_m.
    b0 = (2*q**s-1)**2
    H = -b0*mp.log(b0,2) if b0 else mp.mpf(0)
    for m in range(1, s+1):
        N = mp.binomial(s,m)*a**m
        cm = 4*q**(2*(s-m))*b**(-2*m)
        H += N*(-cm*mp.log(cm,2))
    I = w*s*p
    return {
        "p": p, "B": B, "JS": JS, "Delta": Delta, "R": R,
        "H": H, "I": I, "H_over_I": H/I,
        "WA": WA, "WB": WB, "WC": WC, "t": t, "t0": t0
    }

def tribes_R_iv(w, s):
    # Use exact rational p injected as a one-point enclosure.
    pf = exact_p(w,s)
    p = iv.mpf(pf.numerator) / iv.mpf(pf.denominator)
    a = iv.mpf(2**w-1)
    b = a+1
    WA = 2*p*(a-1)/b
    WB = (a*a+1)*(2*p/b-p*p)
    x0 = (1-a*p)**2
    WC = x0+p*p
    t = 1/(a*a+1)
    t0 = p*p/WC
    B = WA + WB*h_iv(t) + WC*h_iv(t0)
    R = (B+j_iv(p))/p
    return p, R

def c_a_iv(a_int):
    a = iv.mpf(a_int)
    t = 1/(a*a+1)
    return (a*a+1)*h_iv(t)

def U_iv(a_int, p):
    a = iv.mpf(a_int)
    ca = c_a_iv(a_int)
    A0 = 2*(a-1)/(a+1)
    B0 = 2*ca/(a+1)
    cstar = 2/iv.ln(2)
    return A0 + B0 - ca*p + h_iv(p*p)/p + cstar

def tail_U_bound(a_int, delta):
    # h(p^2)/p <= p log_2(e/p^2), increasing for p <= delta < e^-1/2.
    a = iv.mpf(a_int)
    ca = c_a_iv(a_int)
    A0 = 2*(a-1)/(a+1)
    B0 = 2*ca/(a+1)
    cstar = 2/iv.ln(2)
    d = iv.mpf(delta)
    return A0+B0+cstar+d*(1-2*iv.ln(d))/iv.ln(2)

def subdivide_U(a_int, pmax_dec, delta_dec="0.0001", cells=5000):
    # Rational subdivision endpoints based on the given decimals.
    pmax = Fraction(pmax_dec)
    delta = Fraction(delta_dec)
    span = pmax-delta
    best_hi = -1.0
    best_cell = None
    for k in range(cells):
        lq = delta + span*Fraction(k,cells)
        rq = delta + span*Fraction(k+1,cells)
        l = iv.mpf(lq.numerator)/iv.mpf(lq.denominator)
        r = iv.mpf(rq.numerator)/iv.mpf(rq.denominator)
        u = U_iv(a_int, iv.mpf([l.a, r.b]))
        uhi = hi(u)
        if uhi > best_hi:
            best_hi = uhi
            best_cell = (lq, rq, istr(u))
    tail = tail_U_bound(a_int, delta_dec)
    return {
        "cells": cells,
        "domain": [delta_dec, pmax_dec],
        "grid_max_upper": best_hi,
        "grid_max_cell": [str(best_cell[0]), str(best_cell[1])],
        "grid_max_interval": best_cell[2],
        "tail_domain": ["0", delta_dec],
        "tail_upper": hi(tail),
        "certified_upper": max(best_hi, hi(tail)),
    }

result = {
    "status": "PASS" ,
    "scope": "structured-family repaired-selector certificate; not full FEI",
    "C_H": C_H_DEC,
    "tau_H": TAU_H_DEC,
    "width2_finite": [{"s": 1, "p_exact": "1/2", "R_exact": "4", "R_upper_below_C_H": True, "Delta_over_p": "4", "H_over_I": "2"}],
}

# width 2: the low-influence integer cases s=5,...,10.
for s in range(2,11):
    p_iv, R_iv = tribes_R_iv(2,s)
    vals = tribes_mp(2,s)
    row = {
        "s": s,
        "p_exact": str(exact_p(2,s)),
        "p_interval": istr(p_iv),
        "R_interval": istr(R_iv),
        "R_upper_below_C_H": hi(R_iv) < float(C_H),
        "Delta_over_p": mp.nstr(vals["Delta"]/vals["p"], 30),
        "H_over_I": mp.nstr(vals["H_over_I"], 30),
    }
    if not row["R_upper_below_C_H"]:
        result["status"] = "FAIL"
    result["width2_finite"].append(row)

# width 2 tail s>=11.
p11q = exact_p(2,11)
p11 = iv.mpf(p11q.numerator)/iv.mpf(p11q.denominator)
U11 = U_iv(3,p11)

# Derivative lower bound for U on (0,p11]:
# d/dp[h(p^2)/p] >= -log_2 z -(1+z)/((1-z)ln2), z=p^2.
# The RHS decreases with z on our range; evaluate at p11 and subtract c_a.
z11 = p11*p11
deriv_lb = -iv.ln(z11)/iv.ln(2) - (1+z11)/((1-z11)*iv.ln(2)) - c_a_iv(3)
tail_ok = lo(deriv_lb) > 0 and hi(U11) < float(C_H)
if not tail_ok:
    result["status"] = "FAIL"
result["width2_tail_s_ge_11"] = {
    "p11_exact": str(p11q),
    "U_p11_interval": istr(U11),
    "derivative_lower_interval_at_p11": istr(deriv_lb),
    "logic": "derivative lower bound is decreasing in z=p^2, so positivity at p11 makes U increasing on (0,p11]",
    "certified": tail_ok,
}

# widths 3 and 4: certify the continuous U envelope, which automatically
# covers all discrete s in the low-influence domain.
w3 = subdivide_U(7, str(Fraction(1,4)), cells=5000)
w4 = subdivide_U(15, str(Fraction(1,8)), cells=5000)
if not (w3["certified_upper"] < float(C_H) and w4["certified_upper"] < float(C_H)):
    result["status"]="FAIL"
result["width3_continuum_U"] = w3
result["width4_continuum_U"] = w4

# widths >=5: elementary uniform envelope, maximized at b=32 and p=1/16.
b = iv.mpf(32)
p = iv.mpf(1)/16
wide_bound = (
    2
    + (2/b)*(1+2*iv.ln(b))/iv.ln(2)
    + p*(1-2*iv.ln(p))/iv.ln(2)
    + 2/iv.ln(2)
)
wide_ok = hi(wide_bound) < float(C_H)
if not wide_ok:
    result["status"]="FAIL"
result["width_ge_5_uniform"] = {
    "bound_interval": istr(wide_bound),
    "certified": wide_ok,
    "ingredients": [
        "A0<2",
        "(2/(a+1))*(a^2+1)h(1/(a^2+1)) <= (2/b) log2(e b^2), b=a+1>=32",
        "h(p^2)/p <= p log2(e/p^2), p<=1/16",
        "j(p)/p <= 2/ln 2"
    ],
}

print(json.dumps(result, indent=2, sort_keys=True))
if result["status"] != "PASS":
    raise SystemExit(1)
