"""PROVED: ratio-dependent sextic Schur bounds; replay verify_analytic.py."""
from fractions import Fraction as F
from cells import base_value
from padding import base_coefficients

def eta(r):return 2+2*r/(r*r+4*r+1)
def cubic_lower(p,r,which):
    A,B,C=p
    return eta(r)*(3*A-F(3,2))-C if which==0 else r*r*(eta(r)*(3*B-F(3,2))-C)
def lower_value(p,a,r,which):return base_value(p,a,r)+a*a*cubic_lower(p,r,which)
def lower_coefficients(p,a,r,which):
    extra=a*a*cubic_lower(p,r,which)
    return tuple(b+c*extra for b,c in zip(base_coefficients(p,a,r),(16,8,1)))
