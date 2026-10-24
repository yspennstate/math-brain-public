"""Reduced ODEs and the exact order-2 recurrences for r_k and S_n (rigorous route), plus a 30-digit numerical check."""
import sympy as sp
t = sp.symbols('t'); k = sp.symbols('k', integer=True)
R = sp.Function('R')(t); S = sp.Function('S')(t)
def ode_coeffs(expr, f):
    A = sp.expand(expr.coeff(sp.diff(f,t,2))); B = sp.expand(expr.coeff(sp.diff(f,t,1)))
    C = sp.expand(sp.expand(expr - A*sp.diff(f,t,2) - B*sp.diff(f,t,1)).coeff(f))
    g = sp.gcd(sp.gcd(A,B),C)
    return sp.cancel(A/g), sp.cancel(B/g), sp.cancel(C/g)
def rec(A,B,C):
    terms = {}
    for poly, order in ((A,2),(B,1),(C,0)):
        for (i,), a in sp.Poly(poly, t).terms():
            shift = order - i
            fall = sp.prod([(k+shift-s) for s in range(order)]) if order else 1
            terms[shift] = sp.expand(terms.get(shift, 0) + a*fall)
    return terms
# Q = 2F1(-1/2,-1/2;1;t): t(1-t)Q'' + Q' - Q/4 = 0, with Q = (1-t)^{3/2} R
Q = (1-t)**sp.Rational(3,2)*R
e = sp.expand(sp.simplify((t*(1-t)*sp.diff(Q,t,2) + sp.diff(Q,t) - Q/4) * (1-t)**sp.Rational(-3,2) * (1-t)**2))
A,B,C = ode_coeffs(e, R); print("reduced ODE for R:", sp.factor(A), "|", sp.factor(B), "|", sp.factor(C))
tr = rec(A,B,C); print("recurrence r:", {s: sp.factor(v) for s,v in sorted(tr.items())})
# S(t) = t R/(1-t)
Rsub = (1-t)*S/t
eS = sp.expand(sp.simplify((A*sp.diff(Rsub,t,2) + B*sp.diff(Rsub,t,1) + C*Rsub)*t**3))
AS,BS,CS = ode_coeffs(eS, S); print("reduced ODE for S:", sp.factor(AS), "|", sp.factor(BS), "|", sp.factor(CS))
ts = rec(AS,BS,CS); print("recurrence S:", {s: sp.factor(v) for s,v in sorted(ts.items())})
# numerical check of both recurrences on exact rationals
from fractions import Fraction as F
from math import comb
def Cb(j): return F(1) if j==0 else F((-1)**(j-1)*comb(2*j,j), 4**j*(2*j-1))
def p(m): return F((2*m+1)*comb(2*m,m), 4**m)
r = [sum(p(m)*Cb(kk-m)**2 for m in range(kk+1)) for kk in range(25)]
Ssum=[F(0)]; 
for x in r: Ssum.append(Ssum[-1]+x)      # Ssum[n] = S_n
ok_r = all(sum(F(str(sp.nsimplify(v.subs(k,kk)))) * r[kk+s] for s,v in tr.items()) == 0 for kk in range(2,23))
ok_S = all(sum(F(str(sp.nsimplify(v.subs(k,kk)))) * Ssum[kk+s] for s,v in ts.items()) == 0 for kk in range(3,23))
print("exact check r-recurrence:", ok_r, "  S-recurrence:", ok_S)
print("rho_1 = S_2/S_1 =", Ssum[2]/Ssum[1])
