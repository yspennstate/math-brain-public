import json
from pathlib import Path
import sympy as S
out=Path(__file__).parent
checks=0

def ck(test):
    global checks
    assert bool(test)
    checks+=1

def eq(a,b=0):
    ck(S.expand(a-b)==0)

a,b,c,q=S.symbols('x y z q',real=True)
T=S.Matrix([[a,q,q],[q,b,q],[q,q,c]])
eq(T.det(),a*b*c-q*q*(a+b+c)+2*q**3)
eq(T[:2,:2].det(),a*b-q*q)
r1,r2,r3=S.symbols('r1 r2 r3',positive=True)
k1,k2,k3=S.symbols('k1 k2 k3',real=True)
d1,d2,d3=S.symbols('d1 d2 d3',real=True)
x1,y1,x2,y2,x3,y3=S.symbols('x1 y1 x2 y2 x3 y3',real=True)
z=[x1+S.I*y1,x2+S.I*y2,x3+S.I*y3]
# Edges are oriented 23,31,12; diagonals have the complementary index.
K=S.Matrix([[d1,z[2],S.conjugate(z[1])],[S.conjugate(z[2]),d2,z[0]],[z[1],S.conjugate(z[0]),d3]])
angular=[S.I*k*z0 for k,z0 in zip([k1,k2,k3],z)]
A=S.Matrix([[0,angular[2],S.conjugate(angular[1])],[S.conjugate(angular[2]),0,angular[0]],[angular[1],S.conjugate(angular[0]),0]])
t,u=S.symbols('t u',real=True)
Q=S.expand(z[0]*z[1]*z[2]);qr=S.re(Q).expand();qi=S.im(Q).expand()
x=[S.expand(S.re(z0)**2+S.im(z0)**2) for z0 in z]
kv=S.Matrix([k1,k2,k3]);di=[d1,d2,d3]
TK=S.diag(*[di[i]*x[i] for i in range(3)])+qr*(S.ones(3)-S.eye(3))
basepoly=(K+t*A).det().expand()
eq(S.diff(basepoly,t).subs(t,0),-2*qi*(k1+k2+k3))
eq(S.diff(basepoly,t,2).subs(t,0),-2*(kv.T*TK*kv)[0])
u1,u2,u3,e1,e2,e3=S.symbols('u1 u2 u3 e1 e2 e3',real=True)
uv=[u1,u2,u3]
rad=[u0*z0 for u0,z0 in zip(uv,z)]
R=S.Matrix([[e1,rad[2],S.conjugate(rad[1])],[S.conjugate(rad[2]),e2,rad[0]],[rad[1],S.conjugate(rad[0]),e3]])
mix=S.diff((K+t*A+u*R).det().expand(),t,u).subs({t:0,u:0})
eq(mix,-2*qi*((u1+u2+u3)*(k1+k2+k3)-(u1*k1+u2*k2+u3*k3)))
# Exact atom jets, including normalization and all mixed accelerations.
def atom(M,mask):
    cols=[M[:,j] if mask>>j&1 else S.eye(3)[:,j]-M[:,j] for j in range(3)]
    return S.Matrix.hstack(*cols).det().expand()
psum=0;vsum=0;asum=0
for mask in range(8):
    p=atom(K+t*A,mask)
    eps=(-1)**(3-mask.bit_count())
    eq(S.diff(p,t).subs(t,0),eps*(-2*qi*(k1+k2+k3)))
    mixed=S.diff(atom(K+t*A+u*R,mask),t,u).subs({t:0,u:0})
    eq(mixed,eps*mix)
    psum+=p.subs(t,0);vsum+=S.diff(p,t).subs(t,0);asum+=S.diff(p,t,2).subs(t,0)
eq(psum,1);eq(vsum);eq(asum)
# Tetrahedron relabeling is atom preserving at arbitrary measured diagonals.
C=2*K-S.eye(3);dc=[C[i,i] for i in range(3)]
bc=[C.extract([j for j in range(3) if j!=i],[j for j in range(3) if j!=i]).det().expand() for i in range(3)]
cc=C.det().expand()
for mask in range(8):
    sig=[1 if mask>>i&1 else -1 for i in range(3)]
    eta=sig[0]*sig[1]*sig[2]
    zz=[sig[(i+1)%3]*sig[(i+2)%3] for i in range(3)]
    pp=(1+sum(bc[i]*zz[i] for i in range(3))+eta*(cc+sum(dc[i]*zz[i] for i in range(3))))/8
    eq(atom(K,mask),pp)
# Nonzero, mixed-inertia, score-carrying asymmetric witness.
K0=S.Matrix([[S.Rational(1,5),S.Rational(1,10),(1+S.I)/20],
              [S.Rational(1,10),S.Rational(3,5),S.Rational(1,10)],
              [(1-S.I)/20,S.Rational(1,10),S.Rational(4,5)]])
A0=S.Matrix([[0,S.I/10,(1-S.I)/20],[-S.I/10,0,S.I/10],[(1+S.I)/20,-S.I/10,0]])
for J in [K0,S.eye(3)-K0]:
    for n in [1,2,3]:ck(J[:n,:n].det()>0)
for i in range(3):
    eq(A0[i,i])
    for j in range(i+1,3):eq(S.re(S.conjugate(K0[i,j])*A0[i,j]))
eq(A0.det(),-S.Rational(1,1000));eq(S.trace(A0))
# A nonzero determinant and trace zero imply full rank and mixed inertia.
p0=[atom(K0,m) for m in range(8)]
v0=[S.diff(atom(K0+t*A0,m),t).subs(t,0) for m in range(8)]
a0=[S.diff(atom(K0+t*A0,m),t,2).subs(t,0) for m in range(8)]
for m in range(8):
    ck(p0[m]>0);eq(v0[m],(-1)**(3-m.bit_count())*S.Rational(3,1000))
eq(a0[7],-S.Rational(4,125));eq(a0[0],-S.Rational(9,500))
FI=sum(v0[i]**2/p0[i] for i in range(8))
# The first/last diagonal entries are .2/.8 with nonzero incident edges,
# so the spectral .2I..8I slab fails by exact two-by-two principal minors.
ck((K0-S.eye(3)/5)[:2,:2].det()<0)
ck((4*S.eye(3)/5-K0).extract([1,2],[1,2]).det()<0)
# Full angular matrix and mixed block formula checked on three radial/diagonal probes.
logs=[S.symbols('l'+str(m),real=True) for m in range(8)]
tau=logs[0]+logs[3]+logs[5]+logs[6]-logs[7]-logs[1]-logs[2]-logs[4]
lambda0=[]
for i in range(3):
    js=[j for j in range(3) if j!=i]
    masks=[0,1<<js[0],1<<js[1],(1<<js[0])|(1<<js[1])]
    lambda0.append(logs[masks[1]]+logs[masks[2]]-logs[masks[0]]-logs[masks[3]])
xx=[abs(K0[1,2])**2,abs(K0[2,0])**2,abs(K0[0,1])**2]
qq=S.re(K0[0,1]*K0[1,2]*K0[2,0]);hh=S.im(K0[0,1]*K0[1,2]*K0[2,0])
potential=sum(a0[m]*logs[m] for m in range(8))
formula=2*sum(xx[i]*lambda0[i] for i in range(3))+2*tau*(sum(K0[i,i]*xx[i] for i in range(3))+6*qq)
eq(potential,formula)
for ii in range(3):
    R0=S.zeros(3);R0[ii,ii]=1
    vr=[S.diff(atom(K0+u*R0,m),u).subs(u,0) for m in range(8)]
    mjet=[S.diff(atom(K0+t*A0+u*R0,m),t,u).subs({t:0,u:0}) for m in range(8)]
    ell=sum((-1)**(3-m.bit_count())*vr[m]/p0[m] for m in range(8))
    computed=sum(v0[m]*vr[m]/p0[m]+mjet[m]*logs[m] for m in range(8))
    eq(computed,-6*hh*ell)
Atheta=S.Matrix([[0,S.I*k3*K0[0,1],-S.I*k2*K0[0,2]],
                  [-S.I*k3*K0[1,0],0,S.I*k1*K0[1,2]],
                  [S.I*k2*K0[2,0],-S.I*k1*K0[2,1],0]])
vtheta=[S.diff(atom(K0+t*Atheta,m),t).subs(t,0) for m in range(8)]
atheta=[S.diff(atom(K0+t*Atheta,m),t,2).subs(t,0) for m in range(8)]
JP=sum(1/p for p in p0)
P=S.diag(*[2*xx[i]*(lambda0[i]+tau*K0[i,i])-2*tau*qq for i in range(3)])+(2*tau*qq+4*hh**2*JP)*S.ones(3)
eq(sum(vtheta[m]**2/p0[m]+atheta[m]*logs[m] for m in range(8)),(kv.T*P*kv)[0])
for uu in [(1,0,0),(0,1,0),(0,0,1),(2,-3,5)]:
    R0=S.zeros(3)
    for jj,(row,col) in enumerate([(1,2),(2,0),(0,1)]):
        R0[row,col]=uu[jj]*K0[row,col]
        R0[col,row]=S.conjugate(R0[row,col])
    vr=[S.diff(atom(K0+u*R0,m),u).subs(u,0) for m in range(8)]
    mjet=[S.diff(atom(K0+t*Atheta+u*R0,m),t,u).subs({t:0,u:0}) for m in range(8)]
    ell=sum((-1)**(3-m.bit_count())*vr[m]/p0[m] for m in range(8))
    computed=sum(vtheta[m]*vr[m]/p0[m]+mjet[m]*logs[m] for m in range(8))
    eq(computed,2*hh*((tau*sum(uu)-ell)*sum(kv)-tau*sum(uu[i]*kv[i] for i in range(3))))
result={'status':'PASS','exact_assertions':checks,'witness_atoms':[str(p) for p in p0],
        'witness_fisher':str(FI),'witness_full_acceleration':str(a0[7]),'witness_empty_acceleration':str(a0[0]),
        'witness_direction_determinant':str(A0.det()),'scope':'all angular directions at all strict Hermitian three-site bases; mixed six-dimensional Schur complement remains unproved'}
(out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
