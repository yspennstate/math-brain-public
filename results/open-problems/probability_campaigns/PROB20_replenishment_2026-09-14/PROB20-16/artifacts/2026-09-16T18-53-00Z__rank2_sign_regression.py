#!/usr/bin/env python3
"""Exact algebraic regression for the sign in PROB20-16 eq. (4.11)."""
import sympy as sp

dlt = sp.symbols("delta", real=True)
q1,q2 = sp.symbols("q1 q2", positive=True)
q3 = 1-q1-q2
e,d,p1,p2,p3 = sp.symbols("e d p1 p2 p3", positive=True)
qs=[q1,q2,q3]
ps=[p1,p2,p3]

# frozen-log sum S = sum p_S'' log p_S
S = 2*dlt*(sp.log(e)+sp.log(d)+sum(q*sp.log(q) for q in qs)
           -sum((1-q)*sp.log(p) for q,p in zip(qs,ps)))

# weighted interaction L = sum q_k log(p_i p_j/(e d q_k))
L = (
    q1*sp.log(p2*p3/(e*d*q1))
    + q2*sp.log(p1*p3/(e*d*q2))
    + q3*sp.log(p1*p2/(e*d*q3))
)
assert sp.simplify(sp.expand_log(S + 2*dlt*L, force=True)) == 0
print("status=PASS")
print("correct_identity=sum_p_second_log_p=-2*delta*L")
print("therefore_minus_H_second=FI-2*delta*L")
