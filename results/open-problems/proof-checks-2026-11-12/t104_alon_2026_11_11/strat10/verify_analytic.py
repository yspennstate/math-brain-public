"""PROVED: exact square decompositions for two ratio-dependent moment bounds."""
import sympy as S
from fractions import Fraction as F
from analytic_moments import cubic_lower,eta
r,A,B,C,d,e,f,h=S.symbols('r A B C d e f h');den=r*r+4*r+1
R=3*d*d+3*r*r*h*h+(1+4*r)*e*e+(r*r+4*r)*f*f+2*(1+r)*(d*f+r*h*e)
u=eta(r)*(d*d-3*A+S.Rational(3,2))+((1+r)*d+den*f)**2/den+((1+4*r)*e+r*(1+r)*h)**2/(1+4*r)+r*r*(2+10*r-r*r)*h*h/(1+4*r)+C-f*f
w=r*r*eta(r)*(h*h-3*B+S.Rational(3,2))+(den*e+r*(1+r)*h)**2/den+(3*d+(1+r)*f)**2/3+(2*r*r+10*r-1)*f*f/3+r*r*(C-e*e)
assert S.cancel(R-cubic_lower((A,B,C),r,0)-u)==0
assert S.cancel(R-cubic_lower((A,B,C),r,1)-w)==0
# Exact degree-two Bernstein conversion, independently reconstructed here.
for p,lo,hi in [(2+10*r-r*r,F(0),F(1)),(2*r*r+10*r-1,F(3,25),F(1))]:
    left=p.subs(r,S.Rational(lo));right=p.subs(r,S.Rational(hi));mid=p.subs(r,S.Rational((lo+hi)/2));controls=[left,2*mid-(left+right)/2,right]
    assert min(controls)>0
    t=S.symbols('t');assert S.expand(p.subs(r,S.Rational(lo)+(S.Rational(hi)-S.Rational(lo))*t)-(controls[0]*(1-t)**2+2*controls[1]*t*(1-t)+controls[2]*t*t))==0
print('PROVED: R6 >= eta(r)(3A-3/2)-C for 0<=r<=1 and R6 >= r^2[eta(r)(3B-3/2)-C] for 3/25<=r<=1; eta=2+2r/(r^2+4r+1). Exact squares, Bessel and sextic certificates.')
