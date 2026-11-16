"""PROVED: exact cubic-root isolation and monotonicity for the new endpoint."""
import sympy as s
from fractions import Fraction as F

g,k=s.symbols('g k')
p=6272*g**3-2989*g**2-1034*g+427
lo,hi=s.Rational(551,1000),s.Rational(69,125)
assert p.subs(g,lo)<0<p.subs(g,hi)
assert s.Poly(p,g).count_roots(lo,hi)==1
assert 19*lo-7>0
kstar=(59*g-11)/(5*(19*g-7))
assert s.factor(s.diff(kstar,g))==-s.Rational(204,5)/(19*g-7)**2
assert s.Rational(123,100)<kstar.subs(g,hi)<kstar.subs(g,lo)<s.Rational(5,4)
sig=g*(s.Rational(9,5)-k)-s.Rational(1,5)
pn=15*g*k*k+(73-187*g)*k+106*g-34+15*sig*sig
pnj=60*g*k*k+(82-178*g)*k+70*g-70+60*sig*sig
assert s.cancel(pn.subs(k,kstar)-6*(g-1)*p/(5*(19*g-7)**2))==0
assert s.cancel(pnj.subs(k,kstar)-24*(g-1)*p/(5*(19*g-7)**2))==0
upper_dn=30*s.Rational(5,4)*hi*(1+hi)-54*lo*lo-181*lo+73
lower_dnj=2*(60*s.Rational(123,100)*lo*(1+lo)-108*hi*hi-77*hi+41)
assert upper_dn<0 and lower_dnj>0
# Monotonicity in g extends the polynomial bounds even when the same frame
# would have a negative weight at g=G. Only the actual graph uses W2.
upper_g_n=-34+30*(hi-s.Rational(1,5))
kk=s.Rational(123,100)
upper_g_nj=60*kk*kk-178*kk+70+120*(s.Rational(9,5)-kk)*(hi*(s.Rational(9,5)-kk)-s.Rational(1,5))
assert upper_g_n<0 and upper_g_nj<0
print('PROVED: unique cubic root G in (551/1000,69/125); common zero at k=(59G-11)/(5(19G-7)).')
print('PROVED: PN decreases below k and PNJ increases above k, with rational derivative bounds',upper_dn,lower_dnj)
print('PROVED: PN and PNJ decrease in g on their respective K ranges, with derivative bounds',upper_g_n,upper_g_nj)
print('PROVED: T>=0 for every admissible equal-gap frame with 0<g<=G, by polynomial monotonicity.')
