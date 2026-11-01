#!/usr/bin/env python3
import sympy as sp
s,t,u,v=sp.symbols('s t u v')
expr=(t**4-1)*(1/(t**4+1)+s**4/((s**4+t**4)*(s**4+1)))*(s**3+t**3+1)-3*(t**3-1)
num,den=map(sp.factor, sp.together(expr).as_numer_denom())
assert sp.rem(num,t-1,t)==0
P=sp.factor(num/(t-1))
Q=sp.Poly(sp.expand(P.subs({s:t+u,t:1+v})),u,v)
coeffs=[c for _,c in Q.terms()]
assert coeffs and all(c.is_Integer and c>0 for c in coeffs)
assert den==(s**4+1)*(s**4+t**4)*(t**4+1)
print('EXACT SYMBOLIC SELF-CHECK PASS')
print('monomials_after_s=t+u_t=1+v:',len(coeffs))
print('min_coefficient:',min(coeffs))
print('max_coefficient:',max(coeffs))
print('denominator_positive_for_s,t>0: YES')
print('sector_gap_inequality_for_s>=t>=1: CERTIFIED')
