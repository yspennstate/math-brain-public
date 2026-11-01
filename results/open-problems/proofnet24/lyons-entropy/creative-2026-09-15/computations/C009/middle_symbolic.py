"""Exact symbolic verification of the arbitrary-middle-diagonal congruence."""
import sympy as S
m,u,v=S.symbols('m u v', nonzero=True)
R=S.zeros(3)
for s1 in [-1,1]:
 for s3 in [-1,1]:
  p=m/4-(u*s1+v*s3)/2;f=-(u*s1+v*s3)/2
  d=S.Matrix([s1*(m/2-v*s3),S.Rational(1,4),s3*(m/2-u*s1)])
  e=S.Matrix([-v*s1*s3,0,-u*s1*s3])
  E=S.Matrix([[0,S.Rational(s1,2),m*s1*s3],[S.Rational(s1,2),0,S.Rational(s3,2)],[m*s1*s3,S.Rational(s3,2),0]])
  R+=(e*d.T+d*e.T)/p-f*d*d.T/p**2+f*E/p
x=2*u/m;y=2*v/m
Delta=(1-(x+y)**2)*(1-(x-y)**2)
A=S.Matrix([[x*x,x**3,0],[x**3,x*x+y*y,y**3],[0,y**3,y*y]])
w=S.Matrix([x,1,y]);P=8*A/Delta+64*x*x*y*y*w*w.T/Delta**2
factors=S.Matrix([[m,S.Rational(1,2),m],[S.Rational(1,2),1/(4*m),S.Rational(1,2)],[m,S.Rational(1,2),m]])
for i in range(3):
 for j in range(3):
  assert S.factor(R[i,j]-factors[i,j]*P[i,j])==0
print('All nine symbolic rational identities for the middle-slice congruence passed.')
