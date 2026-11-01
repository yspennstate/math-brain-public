"""Rigorous derivation of the recurrences for r_k and S_n from generating functions.
r_k = sum_{m<=k} p_m q_{k-m}, p_m = (3/2)_m/m!  (P(t) = (1-t)^{-3/2}),  q_j = C(1/2,j)^2 = ((-1/2)_j/j!)^2  (Q = 2F1(-1/2,-1/2;1;t)).
Q satisfies t(1-t) Q'' + Q' - Q/4 = 0.  R = P Q.  Sum_{n>=0} S_n t^n = t R/(1-t) with S_n = sum_{k<n} r_k."""
import sympy as sp
t = sp.symbols('t')
R = sp.Function('R')(t)
Q = (1-t)**sp.Rational(3,2) * R                      # Q = R / P
ode_Q = sp.expand(t*(1-t)*sp.diff(Q,t,2) + sp.diff(Q,t) - Q/4)
ode_R = sp.simplify(ode_Q / (1-t)**sp.Rational(-1,2))   # clear the fractional power
ode_R = sp.expand(sp.simplify(ode_R * (1-t)**sp.Rational(1,2) / (1-t)**sp.Rational(1,2)))
# write as A(t) R'' + B(t) R' + C(t) R = 0 with polynomial coefficients
d2, d1, d0 = sp.symbols('d2 d1 d0')
expr = sp.expand(sp.simplify(ode_Q * (1-t)**sp.Rational(-3,2) * (1-t)**2))   # multiply to polynomial coefficients
expr = sp.expand(expr)
A = sp.expand(expr.coeff(sp.diff(R,t,2))); B = sp.expand(expr.coeff(sp.diff(R,t,1)))
C = sp.expand(expr - A*sp.diff(R,t,2) - B*sp.diff(R,t,1)).coeff(R)
print("ODE for R:  A R'' + B R' + C R = 0 with")
print("  A =", sp.factor(A)); print("  B =", sp.factor(B)); print("  C =", sp.factor(C))
# translate to a recurrence: R = sum r_k t^k.  Coefficient of t^k in A R'' + B R' + C R.
k = sp.symbols('k', integer=True)
r = sp.Function('r')
def coeff_rec(A,B,C):
    # A = sum a_i t^i etc.  contribution of t^i * R^{(j)}: sum_k r_k * (k)_j t^{k-j+i} -> shift
    terms = {}
    for poly, order in ((A,2),(B,1),(C,0)):
        P = sp.Poly(poly, t)
        for (i,), a in P.terms():
            # term a t^i R^{(order)} contributes a * (k+order-i)!/(k-i)! ... r_{k+order-i} to coefficient of t^k
            shift = order - i
            fall = sp.prod([ (k+shift - s) for s in range(order)])   # (k+shift)(k+shift-1)...(k+shift-order+1)
            terms[shift] = terms.get(shift, 0) + a*fall
    return terms
terms = coeff_rec(A,B,C)
print("recurrence for r: sum over shift s of coeff * r_{k+s} = 0 :")
for s in sorted(terms): print("   shift", s, ":", sp.factor(sp.expand(terms[s])))
# S generating function: S(t) = t R/(1-t)  => R = (1-t) S / t; plug into the ODE for R and get the ODE for S, then the recurrence
S = sp.Function('S')(t)
Rsub = (1-t)*S/t
exprS = sp.expand(sp.simplify((A*sp.diff(Rsub,t,2) + B*sp.diff(Rsub,t,1) + C*Rsub) * t**3))
AS = sp.expand(exprS.coeff(sp.diff(S,t,2))); BS = sp.expand(exprS.coeff(sp.diff(S,t,1))); CS = sp.expand(exprS - AS*sp.diff(S,t,2) - BS*sp.diff(S,t,1)).coeff(S)
print("ODE for S: A_S =", sp.factor(AS), " B_S =", sp.factor(BS), " C_S =", sp.factor(CS))
termsS = coeff_rec(AS,BS,CS)
print("recurrence for S_n (coefficient of t^k):")
for s in sorted(termsS): print("   shift", s, ":", sp.factor(sp.expand(termsS[s])))
