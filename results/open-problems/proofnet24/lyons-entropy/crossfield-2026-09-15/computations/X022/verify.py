"""Exact verification of X022 identities; no numerical Hessian sign is a proof."""
from pathlib import Path
from collections import defaultdict
from itertools import product
import json
import sympy as s

OUT=Path(__file__).resolve().parent
COUNT=0

def check(v):
    global COUNT
    assert v
    COUNT+=1

def real(v):
    v=s.simplify(s.expand_complex(v))
    check(s.im(v)==0)
    return s.re(v)

def logterms(x):
    x=s.Rational(x)
    ans=defaultdict(lambda:s.S.Zero)
    for pr,n in s.factorint(x.p).items(): ans[int(pr)]+=n
    for pr,n in s.factorint(x.q).items(): ans[int(pr)]-=n
    return dict(ans)

# Forms c + sum_p coeff[p] log(p), with rational c,coeff.
def form(c=0): return [s.Rational(c),defaultdict(lambda:s.S.Zero)]
def add(a,b,k=1):
    a[0]+=k*b[0]
    for p,v in b[1].items(): a[1][p]+=k*v
    return a

def addlog(a,coef,x):
    for p,v in logterms(x).items(): a[1][p]+=coef*v

def same(a,b):
    check(s.simplify(a[0]-b[0])==0)
    for p in set(a[1])|set(b[1]): check(s.simplify(a[1][p]-b[1][p])==0)

def val(a):
    return float((a[0]+sum(v*s.log(p) for p,v in a[1].items())).evalf(40))

def atoms(K,E=None):
    n=K.rows
    ans={}
    for bits in product((0,1),repeat=n):
        M=K-s.diag(*[1-x for x in bits])
        p=real((-1)**sum(1-x for x in bits)*M.det())
        check(p>0)
        if E is None: ans[bits]=(p,0,0)
        else:
            R=M.inv()*E
            tr=real(s.trace(R))
            pp=p*tr
            dd=p*real(tr*tr-s.trace(R*R))
            ans[bits]=(p,pp,dd)
    check(sum(x[0] for x in ans.values())==1)
    check(sum(x[1] for x in ans.values())==0)
    check(sum(x[2] for x in ans.values())==0)
    return ans

def ent(K):
    ans=form()
    for p,_,_ in atoms(K).values(): addlog(ans,-p,p)
    return ans

def deriv(K,E):
    ans=form()
    for p,dp,_ in atoms(K,E).values(): addlog(ans,-dp,p)
    return ans

def hess(K,E):
    ans=form()
    for p,dp,dd in atoms(K,E).values():
        ans[0]-=dp*dp/p
        addlog(ans,-dd,p)
    return ans

def path(diag,edges):
    K=s.diag(*diag)
    for i,z in enumerate(edges): K[i,i+1]=z; K[i+1,i]=s.conjugate(z)
    return K

I=s.I
R=s.Rational
K=path([R(2,5),R(9,20),R(1,2),R(11,20),R(3,5)],[(5+I)/100,(7-I)/100,(6+2*I)/100,(4-I)/100])
E=path([R(3,100),R(-2,100),R(1,100),R(4,100),R(-5,100)],[(2-I)/100,(-1+2*I)/100,(3+I)/100,(-2-I)/100])
# Rational Gershgorin margins using |Re z|+|Im z|.
for M in (K,s.eye(5)-K):
    for i in range(5):
        rad=sum(abs(s.re(M[i,j]))+abs(s.im(M[i,j])) for j in range(5) if j!=i)
        check(M[i,i]-rad>=R(7,25))

p,q=K[0,0],K[4,4]
alpha,beta=E[0,0],E[4,4]
# z is the core-to-leaf entry, harmless conjugations disappear in the strengths.
z,v=K[1,0],K[3,4]
eta,nu=E[1,0],E[3,4]
ss,tt=real(z*s.conjugate(z)),real(v*s.conjugate(v))
sdot,tdot=real(eta*s.conjugate(z)+z*s.conjugate(eta)),real(nu*s.conjugate(v)+v*s.conjugate(nu))
eh,nh=real(eta*s.conjugate(eta)),real(nu*s.conjugate(nu))
B=K.extract([1,2,3],[1,2,3]); C=E.extract([1,2,3],[1,2,3])
U=s.diag(1,0,0); V=s.diag(0,0,1)
pis=[1-p,p]; qis=[1-q,q]
rs=[-1/(1-p),1/p]; us=[-1/(1-q),1/q]
F={}; Z={}; CX={}; CY={}; EE={}; FH={}
for x in (0,1): CX[x]=C-(sdot*rs[x]-ss*alpha*rs[x]**2)*U
for y in (0,1): CY[y]=C-(tdot*us[y]-tt*beta*us[y]**2)*V
for x,y in product((0,1),repeat=2):
    F[x,y]=B-ss*rs[x]*U-tt*us[y]*V
    Z[x,y]=C-(sdot*rs[x]-ss*alpha*rs[x]**2)*U-(tdot*us[y]-tt*beta*us[y]**2)*V
    EE[x,y]=ent(F[x,y]); FH[x,y]=hess(F[x,y],Z[x,y])

lhs=hess(K,E)
rhs=form(-alpha**2/(p*(1-p))-beta**2/(q*(1-q)))
for x,y in product((0,1),repeat=2): add(rhs,FH[x,y],pis[x]*qis[y])
paired1=form(); paired2=form()
for y in (0,1):
    W=alpha*CY[y]-eh*U
    add(paired1,deriv(F[1,y],W),2*qis[y])
    add(paired1,deriv(F[0,y],W),-2*qis[y])
for x in (0,1):
    W=beta*CX[x]-nh*V
    add(paired2,deriv(F[x,1],W),2*pis[x])
    add(paired2,deriv(F[x,0],W),-2*pis[x])
rectangle=form()
for x,y in product((0,1),repeat=2): add(rectangle,EE[x,y],(2*x-1)*(2*y-1))
check(any(v!=0 for v in rectangle[1].values()))
add(rhs,paired1);add(rhs,paired2);add(rhs,rectangle,2*alpha*beta)
same(lhs,rhs)
# Verify joint atoms and both changing-weight jets independently.
full=atoms(K,E)
cond={xy:atoms(F[xy],Z[xy]) for xy in F}
for bits,(prob,dp,dd) in full.items():
    x,y=bits[0],bits[4]
    cp,cd,cdd=cond[x,y][bits[1:4]]
    check(prob==pis[x]*qis[y]*cp)
    score=alpha*rs[x]+beta*us[y]
    check(s.simplify(dp-pis[x]*qis[y]*(cd+score*cp))==0)
    acc=-2*rs[x]*real((eta-alpha*rs[x]*z)*s.conjugate(eta-alpha*rs[x]*z))*U-2*us[y]*real((nu-beta*us[y]*v)*s.conjugate(nu-beta*us[y]*v))*V
    acc_atom=atoms(F[x,y],acc)[bits[1:4]][1]
    expected=pis[x]*qis[y]*(cdd+acc_atom+2*score*cd+2*alpha*beta*rs[x]*us[y]*cp)
    check(s.simplify(dd-expected)==0)

# Balanced five-path matching likelihood and exact end elimination.
edges=[R(3,10),R(1,5),R(1,6),R(1,4)]
BK=path([R(1,2)]*5,edges)
a,b,c,d=[4*z*z for z in edges]
for bits,(prob,_,_) in atoms(BK).items():
    spins=[2*x-1 for x in bits]; ts=[-spins[i]*spins[i+1] for i in range(4)]
    poly=1+a*ts[0]+b*ts[1]+c*ts[2]+d*ts[3]+a*c*ts[0]*ts[2]+a*d*ts[0]*ts[3]+b*d*ts[1]*ts[3]
    Q=1+a*ts[0];RR=1+d*ts[3]
    check(poly==Q*RR+b*ts[1]*RR+c*ts[2]*Q)
    check(prob==poly/32)
check(b/(1-a)+c/(1-d)==R(43,108))

# Exact obstruction: sixth-order core potential is not jointly convex in strengths.
aa,bb,cc,dd=s.symbols('a b c d',real=True)
def Am(m,x):return ((1+x)**(-m)+(1-x)**(-m))/2
G6=(bb**6*Am(5,aa)+cc**6*Am(5,dd))/30+(bb**4*cc**2*Am(3,aa)*Am(1,dd)+bb**2*cc**4*Am(1,aa)*Am(3,dd))/2
point={aa:R(1,5),bb:R(1,5),cc:R(3,10),dd:R(1,10)}
hh=s.hessian(G6,(aa,bb,cc,dd)).subs(point)
vect=s.Matrix([-6,5,-5,3])
negative=s.factor((vect.T*hh*vect)[0])
check(negative==R(-10575079233625,116376761622528))
check(negative<0)
check(point[bb]/(1-point[aa])+point[cc]/(1-point[dd])==R(7,12))

# A chord example where every internal edge ratio is independently moving.
e0=[R(1,5),R(1,8),R(1,10),R(1,6)]; e1=edges
check(all(y>x for x,y in zip(e0,e1)))
check(e0[1]/e0[2]!=e1[1]/e1[2])
K0=path([R(1,2)]*5,e0);K1=BK; tau=R(1,2)
gap=form();add(gap,ent((K0+K1)/2));add(gap,ent(K0),-R(1,2));add(gap,ent(K1),-R(1,2))
quartic=8*sum((x**4+y**4)/2-((x+y)/2)**4 for x,y in zip(e0,e1))
check(quartic>0)
result={
 'status':'PASS', 'exact_assertions':COUNT,
 'moving_mean_identity':{'left_hessian':val(lhs),'right_hessian':val(rhs),'first_paired_correction':val(paired1),'second_paired_correction':val(paired2),'entropy_rectangle':val(rectangle),'weighted_rectangle':val(rectangle)*float(2*alpha*beta)},
 'sixth_order_obstruction':{'strength_point':['1/5','1/5','3/10','1/10'],'direction':[-6,5,-5,3],'quadratic':str(negative),'physical_ratio':'7/12'},
 'aligned_chord':{'endpoint_strength_ratio':'43/108','entropy_gap':val(gap),'quartic_lower_bound':str(quartic),'quartic_decimal':float(quartic)},
 'note':'All identity and sign assertions are exact rational/formal-prime-log checks. Decimal entropies are illustrations, not universal certificates.'}
OUT.joinpath('certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
