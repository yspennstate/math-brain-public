"""Exact algebraic checks for X095; universal sign claims are proved in the report."""
import json
from pathlib import Path
import sympy as s
I=s.I
checks=[]
def check(name, expression):
    assert s.simplify(expression)==0, (name,s.simplify(expression))
    checks.append(name)
def yes(name, value):
    assert bool(value),name
    checks.append(name)

def atoms(K):
    p=[]
    for mask in range(8):
        Q=K-s.diag(*[0 if mask>>i&1 else 1 for i in range(3)])
        p.append(s.expand((-1)**(3-mask.bit_count())*Q.det()))
    return p

# Exact generic determinant block expansion, allowing complex off-support entries.
a,b,delta,t=s.symbols('a b delta t',positive=True)
u,v,d,x,y,z,w=s.symbols('u v d x y z w',real=True)
D=s.diag(a,b)
B=s.Matrix([[u,x+I*y],[x-I*y,v]])
wvec=s.Matrix([z+I*w,1+2*I])
K=s.diag(a,b,delta)
A=B.row_join(wvec).col_join(s.Matrix([[s.conjugate(wvec[0]),s.conjugate(wvec[1]),d]]))
P=a*b;T=u/a+v/b;vv=d+delta*T
poly=s.Poly((K+t*A).det(),t)
check('generic full-atom first derivative',poly.coeff_monomial(t)-P*vv)
Hdet=B.det()/P
acc=2*P*(vv*T-delta*(T*T-Hdet)-(wvec.conjugate().T*D.inv()*wvec)[0])
check('generic full-atom second derivative',2*poly.coeff_monomial(t*t)-acc)

# Exact completion and sharp elementary two-eigenvalue inequality.
tau,p=s.symbols('tau p',positive=True)
vt,tt,hh,ww=s.symbols('vt tt hh ww',real=True)
lhs=P*vt**2/(delta*(1-p))-2*tau*P*(vt*tt-delta*(tt**2-hh)-ww)
rhs=P/(delta*(1-p))*(vt-tau*delta*(1-p)*tt)**2+2*tau*P*ww+delta*P*(2*tau*(tt**2-hh)-tau**2*(1-p)*tt**2)
check('one-event exact square completion',lhs-rhs)
l1,l2=s.symbols('l1 l2',real=True)
check('two-eigenvalue trace determinant square',(l1+l2)**2/4-l1*l2-(l1-l2)**2/4)

# Original nonreal rational witness: every logarithmic comparison is rational.
eps=s.Rational(1,10**20)
K0=s.Matrix([[1,1,2],[1,2,2-I],[2,2+I,5]])/10
K=K0+eps*s.eye(3)
check('rank-two seed characteristic polynomial',K0.charpoly().as_expr().subs(K0.charpoly().gen,t)-t*(t-s.Rational(1,10))*(t-s.Rational(7,10)))
pv=atoms(K)
yes('all eight witness atoms positive',all(x>0 for x in pv))
check('witness normalization',sum(pv)-1)
ratios=[pv[2]*pv[4]/(pv[0]*pv[6]),pv[1]*pv[4]/(pv[0]*pv[5]),pv[1]*pv[2]/(pv[0]*pv[3])]
for j,r in enumerate(ratios):
    yes('face ratio lower '+str(j+1),r>3)
    yes('face ratio upper '+str(j+1),r<([5,16,5][j]))
rtau=pv[0]*pv[3]*pv[5]*pv[6]/(pv[1]*pv[2]*pv[4]*pv[7])
yes('tau exceeds 30',rtau>3**30)
yes('tau below 60',rtau<2**60)
yes('exp2 greater than5 via series',sum(s.Rational(2)**j/s.factorial(j) for j in range(4))>5)
yes('exp3 greater than16 via series',sum(s.Rational(3)**j/s.factorial(j) for j in range(5))>16)
yes('spectral inverse sum below103',(s.Rational(1,10)+eps)**-2+(s.Rational(7,10)+eps)**-2<103)
yes('rare full atom less epsilon',pv[7]<eps)
yes('compensation loss below1e-14',eps*60**2*103<s.Rational(1,10**14))
yes('sqrt5 lower bound',5>s.Rational(11,5)**2)
yes('epsilon frozen comparison',3*eps<s.Rational(1,600))
yes('frozen test vector negative with bounds',7-30*s.Rational(143,600)==-s.Rational(3,20))

# Test full 9D reduction at a rational base with symbolic identity independent
# of the logarithm choice; use rational c,tau to keep every matrix exact.
K=s.Matrix([[s.Rational(1,5),s.Rational(1,10),I/20],[s.Rational(1,10),s.Rational(3,5),s.Rational(1,10)],[-I/20,s.Rational(1,10),s.Rational(4,5)]])
pv=atoms(K)
cs=[s.Rational(2),s.Rational(3),s.Rational(2)];tv=s.Rational(1)
M=s.diag(*cs)+tv*K;dm=M.det()
E=[]
for mask in range(1,8):
    Q=K-s.diag(*[0 if mask>>i&1 else 1 for i in range(3)])
    E.append((-1)**(3-mask.bit_count())*Q.adjugate())
V=s.diag(*pv[1:])-s.Matrix(pv[1:])*s.Matrix(pv[1:]).T
W=s.diag(*[1/x for x in pv[1:]])+s.ones(7)/pv[0]
check('seven-event covariance inverse',(V*W-s.eye(7)).norm())
TM=s.Matrix(7,7,lambda i,j:s.trace(M*E[i]*M*E[j]))
vm=s.Matrix([s.trace(M*e) for e in E]);CM=TM+dm*V
r=CM.inv()*vm
ss=(vm.T*r)[0]
Ast=M
for j in range(7):Ast-=r[j]*M*E[j]*M
jet=s.Matrix([s.trace(e*Ast) for e in E])
FI=(jet.T*W*jet)[0]
QQ=FI-2*s.trace(M*Ast.adjugate())
check('full atom explicit adverse-ray identity',QQ-dm*(3-ss)*(ss-2))
check('full atom trace identity',s.trace(M.inv()*Ast)-(3-ss))
check('polynomial scalar determinant identity',(vm.T*CM.adjugate()*vm)[0]-2*CM.det()-CM.det()*(ss-2))

# One frozen phase split and transformed full gradient, exactly over Q(i,sqrt).
K=K0+s.Rational(1,100)*s.eye(3)
k=[K[1,2],K[2,0],K[0,1]]
rho=[s.sqrt(s.expand_complex(zz*s.conjugate(zz))) for zz in k]
Q=k[0]*k[1]*k[2];RR=s.prod(rho);qq=s.re(Q)
# Choose half-angle exp(i theta/2) using Q's nonreal sign.
cc=s.sqrt((RR+qq)/(2*RR));sn=-s.sqrt((RR-qq)/(2*RR))
ph=(cc+I*sn)
rots=[zz/rr/s.expand_complex(ph) for zz,rr in zip(k,rho)]
# Rotations are algebraic; checking squared gradients removes nested radicals.
for i in range(3):
    j=(i+1)%3;kk=(i+2)%3
    dd=(-K[i,i]*s.conjugate(k[i])+k[j]*k[kk])*rots[i]
    check('phase radial derivative '+str(i+1),s.re(s.expand_complex(dd))-cc*(rho[j]*rho[kk]-K[i,i]*rho[i]))
    check('phase angular derivative '+str(i+1),s.im(s.expand_complex(dd))-sn*(rho[j]*rho[kk]+K[i,i]*rho[i]))

out={'status':'PASS','exact_assertions':len(checks),'checks':checks,'universal_concavity_proved':False,'witness_epsilon':'1/10^20','certificate':'fixed-diagonal curvature > (1-10^-14) norm_F^2 while frozen form is indefinite'}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
