"""Exact algebra for the field-polynomial theorem; no sampled sign proof."""
import json
from pathlib import Path
import sympy as s
from explore import build

count=0
def check(x):
    global count
    assert x
    count+=1

def atom(M,mask):
    n=M.rows
    return s.simplify(s.Matrix.hstack(*[(M if mask>>i&1 else s.eye(n)-M)[:,i] for i in range(n)]).det())

def derivative(M,A,mask):
    n=M.rows
    N=s.Matrix.hstack(*[(M if mask>>i&1 else s.eye(n)-M)[:,i] for i in range(n)])
    V=s.Matrix.hstack(*[(A if mask>>i&1 else -A)[:,i] for i in range(n)])
    return s.simplify(N.det()*s.trace(N.inv()*V))

def quadratic(M,basis):
    def f(a): return s.simplify(2*s.trace(M*a.adjugate()))
    return s.Matrix(len(basis),len(basis),lambda i,j:s.simplify((f(basis[i]+basis[j])-f(basis[i])-f(basis[j]))/2))

rows=[]
for b in [s.Rational(1,10),s.Rational(2,7),s.Rational(15,52)]:
    K,basis,ps,vs,pol,c=build(b)
    check(pol[0][:6,:6]==pol[2][:6,:6])
    check(pol[0][6:,6:]==pol[2][6:,6:])
    check(pol[0][:6,6:]==-pol[2][:6,6:])
    check(pol[1][:6,6:]==s.zeros(6,3))
    axial=s.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
    v=s.Matrix([0,-b,b])
    expected=2*c*axial.T*(s.diag(0,1,1)-4*v*v.T)*axial
    check((pol[1][6:,6:]-pol[0][6:,6:]-pol[2][6:,6:]-expected).applyfunc(s.simplify)==s.zeros(3))
    check(8*b*b<1)
    k=K[1:,0]
    for sign,which in [(1,0),(-1,2)]:
        pair=K[1:,1:]+sign*2*k*k.conjugate().T
        velocities=[]
        for A in basis:
            w=A[1:,0]
            velocities.append(A[1:,1:]+sign*2*(w*k.conjugate().T+k*w.conjugate().T)+4*A[0,0]*k*k.conjugate().T)
        pair_form=s.zeros(9)
        for mask in range(4):
            p=atom(pair,mask)
            g=s.Matrix([derivative(pair,A,mask) for A in velocities])
            pair_form+=g*g.T/p
        pair_form-=s.Matrix(9,9,lambda i,j:c*((velocities[i]+velocities[j]).det()-velocities[i].det()-velocities[j].det()))
        check((pol[which]-pair_form/4).applyfunc(s.simplify)==s.zeros(9))
    for root_d in [s.Rational(1,3),s.Integer(1),s.Integer(3)]:
        d=root_d**2;D=s.diag(d,1,1);sqrtD=s.diag(root_d,1,1);E=D-s.eye(3)
        Z=s.simplify((s.eye(3)+E*K).det())
        J=sqrtD*K*(s.eye(3)+E*K).inv()*sqrtD
        U=sqrtD*(s.eye(3)+K*E).inv()
        moved=[U*A*U.conjugate().T for A in basis]
        q=[atom(J,m) for m in range(8)]
        for m in range(8):check(s.simplify(q[m]-ps[m]*d**(m&1)/Z)==0)
        for i,A in enumerate(moved):
            sigma=sum(q[m]*vs[m][i]/ps[m] for m in range(8))
            for m in range(8):check(s.simplify(derivative(J,A,m)-q[m]*(vs[m][i]/ps[m]-sigma))==0)
        Fisher=s.zeros(9)
        for m in range(8):
            grad=s.Matrix([derivative(J,A,m) for A in moved])
            Fisher+=grad*grad.T/q[m]
        true=Z**2*(Fisher-quadratic(c*s.eye(3),moved))
        check((true-pol[0]-d*pol[1]-d*d*pol[2]).applyfunc(s.simplify)==s.zeros(9))
    rows.append({'b':str(b),'odds_ratio':str(ps[1]/ps[0]),'field_values':['1/9','1','9']})

# The center count determinant is checked for its complete symbolic range.
r=s.Symbol('r',positive=True);c=s.Symbol('c',real=True);den=(1-r)*(3+r)
alpha=(36-12*r*r-8*r**3)/den
beta=-16*r**3/den
gamma=16*r*r*(3-2*r)/den
ell=(3+3*r-2*r*r)/(3+r)
check(s.factor(alpha*gamma-beta**2-576*r*r/den)==0)
check(s.factor(alpha-gamma-12*ell)==0)
check(s.factor((alpha-6*c)*(gamma+6*c)-beta**2-(576*r*r/den+72*c*ell-36*c*c))==0)

# Generic non-PH example checks the complete diagonal-field frozen transport.
K=s.Matrix([[s.Rational(1,5),s.Rational(1,20)+s.I/50,s.Rational(1,30)],
 [s.Rational(1,20)-s.I/50,s.Rational(3,5),s.Rational(1,25)+s.I/60],
 [s.Rational(1,30),s.Rational(1,25)-s.I/60,s.Rational(4,5)]])
D=s.diag(s.Rational(4,9),s.Rational(25,16),s.Rational(49,25));sd=s.diag(s.Rational(2,3),s.Rational(5,4),s.Rational(7,5))
E=D-s.eye(3);Z=(s.eye(3)+E*K).det();U=sd*(s.eye(3)+K*E).inv();J=sd*K*(s.eye(3)+E*K).inv()*sd
c1,c2,c3,tau=s.symbols('c1 c2 c3 tau',real=True);C=s.diag(c1,c2,c3)
transport=Z**2*U.det()**2*U.inv()*(C+tau*J)*U.conjugate().T.inv()
explicit=s.zeros(3)
for i,ci in enumerate([c1,c2,c3]):
    k=K[:,i];h=(s.eye(3)-K)[:,i];di=D[i,i]
    explicit+=D.det()/di*(ci*h*h.conjugate().T+di*(ci+tau/2)*(h*k.conjugate().T+k*h.conjugate().T)+di**2*(ci+tau)*k*k.conjugate().T)
check((transport-explicit).applyfunc(s.simplify)==s.zeros(3))
out={'status':'PASS','exact_assertions':count,'cases':rows,'scope':'Exact identities only; uniform Hessian sign is proved analytically in agents/X055.md.'}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
