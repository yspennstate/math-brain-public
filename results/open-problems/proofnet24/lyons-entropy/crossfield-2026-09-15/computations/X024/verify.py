"""Deterministic algebra checks for X024; numerical values are corroboration."""
import itertools
import json
import math
from pathlib import Path
import numpy as np
import sympy as sp

I=sp.I
R=sp.Rational
t=sp.symbols('t', real=True)
signs=list(itertools.product((-1,1),repeat=4))

def kernel(C):
    return sp.eye(4)/2+sp.BlockMatrix([[sp.zeros(2),C/2],[sp.conjugate(C.T)/2,sp.zeros(2)]]).as_explicit()

def direct_atom(K,spins):
    cols=[K[:,j] if spins[j]==1 else (sp.eye(4)-K)[:,j] for j in range(4)]
    return sp.expand(sp.Matrix.hstack(*cols).det(method='domain-ge'))

def fourcycle_density(C,spins):
    a,b,c,d=list(C)
    w=[sp.expand(z*sp.conjugate(z)) for z in (a,b,c,d)]
    u,v,p,q=spins
    edge=[-u*p,-u*q,-v*p,-v*q]
    delta=sp.expand((a*d-b*c)*sp.conjugate(a*d-b*c))
    return sp.expand(1+sum(we*te for we,te in zip(w,edge))+delta*u*v*p*q)

def quat(z,w):
    return sp.Matrix([[z,w],[-sp.conjugate(w),sp.conjugate(z)]])

assertions=0
# Independent exact determinant check for a generic complex four-cycle.
C=sp.Matrix([[(1+2*I)/5,(2-I)/7],[(-2+I)/9,(1-I)/6]])
assert sum(abs(complex(v))**2 for v in C)<1
for spin in signs:
    assert sp.simplify(16*direct_atom(kernel(C),spin)-fourcycle_density(C,spin))==0
    assertions+=1

# Entire affine segment checked polynomially, retaining determinant acceleration.
z0,w0=(3+I)/5,(3+2*I)/5
z1,w1=(2+3*I)/5,(1+3*I)/5
z,w=(1-t)*z0+t*z1,(1-t)*w0+t*w1
C=quat(z,w)
x,y=sp.expand(z*sp.conjugate(z)),sp.expand(w*sp.conjugate(w))
s=x+y
assert sp.simplify(C*sp.conjugate(C.T)-s*sp.eye(2))==sp.zeros(2)
polys=[]
for spin in signs:
    atom=direct_atom(kernel(C),spin)
    q=fourcycle_density(C,spin)
    eta=spin[0]*spin[1]*spin[2]*spin[3]
    r,u=-spin[0]*spin[2],-spin[0]*spin[3]
    grouped=1-s*s if eta==-1 else 1+s*s+2*x*r+2*y*u
    assert sp.expand(16*atom-q)==0
    assert sp.expand(q-grouped)==0
    assertions+=2
    polys.append(atom)
assert sp.expand(sum(polys)-1)==0
assertions+=1

# Exact product factor behind the nonnegative determinant correction.
X,Y=sp.symbols('X Y',nonnegative=True)
S=X+Y
product=sp.prod(1+S*S+2*X*r+2*Y*u for r,u in itertools.product((-1,1),repeat=2))
assert sp.expand(product-(1-S*S)**2*((1-S*S)**2+16*X*Y))==0
assertions+=1

def scalar_data(x,y):
    s=x+y
    q=[1+s*s+2*x*r+2*y*u for r,u in itertools.product((-1,1),repeat=2)]
    b=1-s*s
    grad=np.zeros(2)
    hess=np.zeros((2,2))
    for (r,u),mass in zip(itertools.product((-1,1),repeat=2),q):
        dq=np.array([2*(r+s),2*(u+s)])
        grad+=dq*math.log(mass)/8
        hess+=np.outer(dq,dq)/mass/8
    dq=np.array([-2*s,-2*s])
    grad+=dq*math.log(b)/2
    hess+=np.outer(dq,dq)/b/2
    gamma=math.log1p(16*x*y/(1-s*s)**2)/8
    hess+=2*gamma*np.ones((2,2))
    deficit=sum(mass*math.log(mass) for mass in q)/8+b*math.log(b)/2
    return deficit,grad,hess,gamma

exact_assertions=assertions
max_curvature_error=0.0
records=[]
for at in [R(0),R(1,4),R(1,2),R(3,4),R(1)]:
    p=np.array([float(poly.subs(t,at)) for poly in polys])
    dp=np.array([float(sp.diff(poly,t).subs(t,at)) for poly in polys])
    ddp=np.array([float(sp.diff(poly,t,2).subs(t,at)) for poly in polys])
    exact_curvature=float(np.sum(dp*dp/p+ddp*np.log(p)))
    xv,yv=float(x.subs(t,at)),float(y.subs(t,at))
    f,grad,hess,gamma=scalar_data(xv,yv)
    velocity=np.array([float(sp.diff(x,t).subs(t,at)),float(sp.diff(y,t).subs(t,at))])
    acceleration=np.array([float(sp.diff(x,t,2).subs(t,at)),float(sp.diff(y,t,2).subs(t,at))])
    certificate=float(velocity@hess@velocity+grad@acceleration)
    error=abs(certificate-exact_curvature)
    max_curvature_error=max(max_curvature_error,error)
    assert error<1e-11 and certificate>0 and np.linalg.eigvalsh(hess).min()>0
    zv,wv=complex(z.subs(t,at)),complex(w.subs(t,at))
    jac=np.array([[2*zv.real,2*zv.imag,0,0],[0,0,2*wv.real,2*wv.imag]])
    entry_hess=jac.T@hess@jac+2*np.diag([grad[0],grad[0],grad[1],grad[1]])
    assert np.linalg.eigvalsh(entry_hess).min()>0
    assert abs(f-(4*math.log(2)+float(np.sum(p*np.log(p)))))<1e-12
    assertions+=3
    records.append({'t':str(at),'x':xv,'y':yv,'deficit_curvature':certificate,
                    'minimum_entry_hessian_eigenvalue':float(np.linalg.eigvalsh(entry_hess).min()),
                    'gamma':gamma})
f0=scalar_data(float(x.subs(t,0)),float(y.subs(t,0)))[0]
f1=scalar_data(float(x.subs(t,1)),float(y.subs(t,1)))[0]
fm=scalar_data(float(x.subs(t,R(1,2))),float(y.subs(t,R(1,2))))[0]
output={'recorded_exact_assertions':exact_assertions,'numerical_assertions':assertions-exact_assertions,'maximum_curvature_error':max_curvature_error,
        'endpoint_strength':str(s.subs(t,0)),
        'example_midpoint_entropy_gap':(f0+f1)/2-fm,'deterministic_segment_checks':records,
        'status':'Analytic proof is in agents/X024.md; finite checks are corroboration.'}
Path(__file__).with_name('results.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
