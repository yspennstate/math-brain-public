"""Exact rational example and high-precision evaluation for C077.

Run: python reproduce.py
No random input is used. Symbolic equalities, rather than finite differences,
verify the orbit-score cancellation and the entropy-curvature identity.
"""
import json
import sympy as s
import numpy as np

I=s.I
K=s.Matrix([[s.Rational(1,3),s.Rational(1,10),-I/15],
            [s.Rational(1,10),s.Rational(1,2),s.Rational(1,12)],
            [I/15,s.Rational(1,12),s.Rational(2,3)]])
D=s.diag(0,1,3)
A=I*(D*K-K*D)
z=s.symbols('z', real=True)
p=[]; dp=[]; ddp=[]
for mask in range(8):
    Q=K-s.diag(*[0 if mask>>i&1 else 1 for i in range(3)])
    polynomial=s.expand((-1)**(3-mask.bit_count())*(Q+z*A).det())
    p.append(polynomial.subs(z,0))
    dp.append(s.diff(polynomial,z).subs(z,0))
    ddp.append(s.diff(polynomial,z,2).subs(z,0))
assert sum(p)==1 and min(p)>0
assert dp==[0]*8
assert A.det()==s.Rational(1,150)
f=[-s.log(x) for x in p]
c=s.diag(f[6]-f[2]-f[4]+f[0],
         f[5]-f[1]-f[4]+f[0],
         f[3]-f[1]-f[2]+f[0])
tau=f[7]-f[6]-f[5]-f[3]+f[4]+f[2]+f[1]-f[0]
M=c+tau*K
Hpp=-sum(ddp[j]*s.log(p[j]) for j in range(8))
frozen=2*s.trace(M*A.adjugate())
assert s.expand(Hpp-frozen)==0
u,v,w,t=s.symbols('u v w t', real=True)
Mf=s.diag(u,v,w)+t*K
assert s.expand(s.trace(Mf.adjugate()*A))==0
assert s.expand(Mf.det()*2*s.trace(Mf*A.adjugate())
                +s.trace((Mf.adjugate()*A)**2))==0

Kn=np.array(K.evalf(),dtype=complex)
An=np.array(A.evalf(),dtype=complex)
Mn=np.array(M.evalf(),dtype=complex)
eigK=np.linalg.eigvalsh(Kn)
eigM=np.linalg.eigvalsh(Mn)
rhs=-np.linalg.det(Mn).real*np.trace(np.linalg.solve(Mn,An)@np.linalg.solve(Mn,An)).real
assert abs(rhs-float(Hpp.evalf()))<1e-13

def masses(J):
    return np.array([(-1)**(3-mask.bit_count())*np.linalg.det(
        J-np.diag([not(mask>>i&1) for i in range(3)])).real for mask in range(8)])
def entropy(J):
    ps=masses(J)
    return float(-ps@np.log(ps))
rho=(np.array([0,1,3])[:,None]-np.array([0,1,3])[None,:])**2
flow=[dict(t=t,H=entropy(Kn*np.exp(-t*rho))) for t in [0,.01,.1,.5,1,3]]
eps=1/6
gamma=float(np.prod(eigM)/eigM[-1]**2)
third=(2/eps)**3*(38*np.log(2/eps)+26)
radius=min(eps/2,gamma/(2*third))
out=dict(K=[[str(x) for x in K.row(i)] for i in range(3)],
         A=[[str(x) for x in A.row(i)] for i in range(3)],
         probabilities=[str(x) for x in p],
         first_derivatives=[str(x) for x in dp],
         second_derivatives=[str(x) for x in ddp],
         det_A=str(A.det()),frob_A_squared=str(s.trace(A*A)),
         tau=float(tau.evalf()),c_diagonal=[float(c[i,i].evalf()) for i in range(3)],
         eigenvalues_K=eigK.tolist(),eigenvalues_M=eigM.tolist(),
         entropy_curvature=float(Hpp.evalf()),negative_square=rhs,
         gamma=gamma,affine_radius=radius,gaussian_dephasing=flow)
with open('reproduce.json','w') as fh: json.dump(out,fh,indent=2)
print(json.dumps(out,indent=2))
