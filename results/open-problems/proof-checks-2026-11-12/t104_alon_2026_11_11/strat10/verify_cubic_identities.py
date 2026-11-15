"""PROVED: algebra linking the new scalar sextic to all cell residual blocks."""
import sympy as S
from fractions import Fraction as F
from cubic_cells import residual_blocks,cubic_lower,CUBIC_DIRECTIONS
from cells import residual_blocks as old_blocks
A,B,C,D,E=S.symbols('A B C D E');d,e,f,h,r=S.symbols('d e f h r');x,y=S.symbols('x y')
# The +/- rotations cancel mixed fourth moments and cross-block cubic terms.
plus=x**3*d+3*x*x*y*e+3*x*y*y*f+y**3*h
minus=x**3*d-3*x*x*y*e+3*x*y*y*f-y**3*h
assert S.expand((plus**2+minus**2)/2-(x**3*d+3*x*y*y*f)**2-(3*x*x*y*e+y**3*h)**2)==0
quartic=x**4*A+4*x**3*y*D+6*x*x*y*y*C+4*x*y**3*E+y**4*B
assert S.expand((quartic+quartic.subs(y,-y))/2-x**4*A-6*x*x*y*y*C-y**4*B)==0
for i,(alpha,beta)in enumerate(CUBIC_DIRECTIONS):
    vec=[F(0)]*30;vec[25+i]=F(1);base=old_blocks(r,vec[:25]);blocks=residual_blocks(r,vec)
    old=sum(v[0]*p*p+2*v[1]*p*q+v[2]*q*q for v,(p,q)in zip(base,((d,f),(e,h))))
    new=sum(v[0]*p*p+2*v[1]*p*q+v[2]*q*q for v,(p,q)in zip(blocks,((d,f),(e,h))))
    norm=alpha*alpha+beta*beta
    ss=((alpha**3*d+3*alpha*beta**2*f)**2+(3*alpha**2*beta*e+beta**3*h)**2)/S.Integer(norm)**3
    assert S.expand(old-new-ss)==0
    assert S.expand(cubic_lower((A,B,C),alpha,beta)-(3*(alpha**4*A+6*alpha**2*beta**2*C+beta**4*B)/S.Integer(norm)**2-S.Rational(3,2)))==0
print('PROVED: all five sextic multipliers, paired rotations, 2x2 residual matrices and affine moment lower terms matched exactly.')
