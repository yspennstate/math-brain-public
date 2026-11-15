"""Symbolic audit of the two-point Hessian determinant identity."""
import sympy as s
from pathlib import Path
w,x,y,z,c,l=s.symbols('w x y z c l',real=True)
t=x*y-w*z
# Use w=1-x-y-z and c^2=xy-wz only after forming the determinant.
a=x+z;b=y+z
grad=[s.Matrix([b-1,a-1,-2*c]),s.Matrix([1-b,-a,2*c]),
      s.Matrix([-b,1-a,2*c]),s.Matrix([b,a,-2*c])]
G=s.zeros(3)
for p,v in zip([w,x,y,z],grad):G+=v*v.T/p
M=s.Matrix([[0,1,0],[1,0,0],[0,0,-2]])
P=w*x*y*z;B=x*y-t*(w+z)
expected=2/P*(2*t+B*l-P*l**3)
# Symbolic identity under normalization, and the physical c^2 relation.
poly=s.together((G-l*M).det()-expected)
num=s.fraction(poly)[0]
num=s.Poly(num,c).rem(s.Poly(c*c-t,c)).as_expr()
zero=s.factor(num.subs(w,1-x-y-z))
assert zero==0,zero
result='det(G-l M) = 2/(wxyz) [2t + (xy-t(w+z))l - wxyz l^3]\n'
result+='Verified by symbolic polynomial reduction using c^2=xy-wz and w+x+y+z=1.\n'
Path('data').mkdir(exist_ok=True)
Path('data/two_point_symbolic.txt').write_text(result)
print(result)
