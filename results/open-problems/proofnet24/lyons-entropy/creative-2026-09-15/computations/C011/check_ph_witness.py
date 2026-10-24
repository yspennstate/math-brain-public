"""Symbolic identities and direct finite-atom checks for the PH parity witness."""
from fractions import Fraction as F
import itertools,json,math
import numpy as np
import sympy as s

t,m=s.symbols('t m',positive=True)
v=(3-2*t)/4; D=(1-t)*(3+t); den=m+4*t*t
b=t/(2*den)
obj=s.factor(m*v-m*m*t*b+m*m*den*b*b)
closed=m*D/4+m*t**4/den
assert s.simplify(obj-closed)==0
margin_num=16*t*t+4*m*(1-t)**2*(1+2*t)-m*m*D
assert s.simplify(1-obj-margin_num/(4*den))==0
# Full two-dimensional optimum, after x=m*a and y=2*m*t*b.
J=s.Matrix([[3+m*v,-1-m/4],[-1-m/4,1+m/(4*t*t)]])
u=s.Matrix([3,-1]); opt=s.factor(3-(u.T*J.inv()*u)[0])
opt_closed=m*(8*t*t*(3-2*t)+3*m*D)/(32*t*t+4*m*(3+t*t-2*t**3)+m*m*D)
assert s.simplify(opt-opt_closed)==0
# Obstruction constants at the exact rational edge r=15/52.
tr=12*F(15,52)**2
assert tr==F(675,676)
assert (3+tr)/(3*(1-tr))==901
vr=(3-2*tr)/4
assert vr==F(339,1352)
assert 3*6*vr/(3+6*vr)==F(1017,1015)

atoms=np.array(list(itertools.product([0,1],repeat=3)))
spin=2*atoms-1
samples=[]
for edge in [.01,.1,.2,.28,15/52,.28867]:
    tv=12*edge*edge;mv=math.log((3+tv)/(3*(1-tv)))
    K=np.eye(3,dtype=complex)/2+1j*edge*np.array([[0,1,-1],[-1,0,1],[1,-1,0]])
    prob=[];Qinv=[]
    for atom in atoms:
        Q=K-np.diag(1-atom)
        prob.append((-1)**int(3-sum(atom))*np.linalg.det(Q).real)
        Qinv.append(np.linalg.inv(Q))
    prob=np.array(prob)
    parity=spin.prod(1);ncenter=atoms.sum(1)-1.5
    beta=tv/(2*(mv+4*tv*tv))
    gv=ncenter/mv+beta*parity
    covariance=sum(px*z*mv*Qi for px,z,Qi in zip(prob,gv,Qinv))
    direct=mv**3*(prob@gv**2)+np.linalg.norm(np.eye(3)-covariance)**2
    formula=mv*(3-2*tv)/4-mv*mv*tv*tv/(4*(mv+4*tv*tv))
    assert abs(direct-formula)<2e-9
    # Direct minimization over all six degree-one/two Walsh features.
    features=np.column_stack([spin[:,i] for i in range(3)]+[spin[:,i]*spin[:,j] for i,j in ((0,1),(0,2),(1,2))]).astype(float)
    features-=prob@features
    V=features.T@(prob[:,None]*features)
    B=[sum(px*z*mv*Qi for px,z,Qi in zip(prob,features[:,i],Qinv)) for i in range(6)]
    J6=mv**3*V+np.array([[np.trace(x@y).real for y in B] for x in B])
    u6=np.array([np.trace(x).real for x in B])
    direct6=3-u6@np.linalg.solve(J6,u6)
    A=mv*(3-2*tv)/4
    formula6=3*A/(3+A)
    assert abs(direct6-formula6)<2e-8
    samples.append({'r':edge,'t':tv,'m':mv,'witness_objective':formula,'degree_two_minimum':formula6})
print(json.dumps({'symbolic_identities_passed':3,'exact_rational_constants_passed':4,'finite_atom_checks':samples,'proof_status':'Analytic proof is in agents/C011.md; floating-point entries are supplementary formula checks.'},indent=2))
