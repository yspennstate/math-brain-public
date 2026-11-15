"""PROVED: exact symbolic derivation of the directional edge-square bound."""
import sympy as s
import verify_new_bounds as audit
from directional_bounds import DIRECTIONS,residual_blocks

alpha,beta=s.symbols('alpha beta')
ui,wi,uj,wj=audit.ui,audit.wi,audit.uj,audit.wj
a,b,la=audit.a,audit.b,audit.la
A,B,C,d,e,f,h=audit.A,audit.B,audit.C,audit.d,audit.e,audit.f,audit.h
pij=alpha*ui*uj+beta*wi*wj
diag=alpha*alpha*A+2*alpha*beta*C+beta*beta*B
Z=a*(alpha*alpha*audit.moment(6,0)+2*alpha*beta*audit.moment(4,2)+beta*beta*audit.moment(2,4))
Z+=b*(alpha*alpha*audit.moment(4,2)+2*alpha*beta*audit.moment(2,4)+beta*beta*audit.moment(0,6))
N=a*(alpha*alpha*d*d+2*alpha*beta*e*e+beta*beta*f*f)
N+=b*(alpha*alpha*e*e+2*alpha*beta*f*f+beta*beta*h*h)
S=alpha*a+beta*b-a*(alpha*A+beta*C)-b*(alpha*C+beta*B)-la*(alpha+beta)/5
assert s.expand(2*audit.pair_sum(audit.weight*pij)-S)==0
assert s.expand(2*audit.pair_sum(audit.weight*pij*pij)-N+Z-la*(alpha*alpha+beta*beta-diag)/5)==0
print('PROVED: arbitrary-direction first and second edge moments matched exactly.')

r,td=s.symbols('r td')
thetas=s.symbols('theta0:'+str(len(DIRECTIONS)))
z=s.symbols('z0:4')
vector=[]
for theta in thetas:
    vector.extend((theta,0,0,0,0))
vector+=[td]+list(z)
blocks=residual_blocks(r,vector)
pol=blocks[0][0]*d*d+2*blocks[0][1]*d*f+blocks[0][2]*f*f
pol+=blocks[1][0]*e*e+2*blocks[1][1]*e*h+blocks[1][2]*h*h
expected=audit.R+td*audit.Nr-td*audit.Jr
expected+=z[0]*(d*d+e*e)+z[1]*(f*f+h*h)+z[2]*e*e+z[3]*f*f
# audit.R uses its own symbol r; SymPy symbols with the same name coincide.
for theta,(aa,bb)in zip(thetas,DIRECTIONS):
    expected-=theta*(aa*aa*d*d+(2*aa*bb+r*aa*aa)*e*e
                      +(bb*bb+2*r*aa*bb)*f*f+r*bb*bb*h*h)
assert s.expand(pol-expected)==0
print('PROVED: directional residual blocks matched exactly for all four directions.')
