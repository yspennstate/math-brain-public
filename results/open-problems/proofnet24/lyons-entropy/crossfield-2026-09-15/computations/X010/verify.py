"""Exact finite checks for X010's all-dimension identities and analytic obstruction."""
from itertools import combinations, permutations, product
from pathlib import Path
import json
import sympy as s

ROOT=Path(__file__).resolve().parent
I=s.I;R=s.Rational
checks=0

def check(cond,label):
 global checks
 if not cond: raise AssertionError(label)
 checks+=1

def zero(x):
 if isinstance(x,s.MatrixBase): return all(s.cancel(z)==0 for z in x)
 return s.cancel(x)==0

def adj(x):return x.conjugate().T

def compound(A,r):
 idx=list(combinations(range(A.rows),r))
 return s.Matrix([[A.extract(a,b).det() for b in idx] for a in idx])

def atom(K,x):return s.cancel((-1)**sum(1-z for z in x)*(K-s.diag(*[1-z for z in x])).det())

def branch_data(bits,p,dp,ddp,Q,history,order):
 ids=[i for i,x in enumerate(bits) if all(x[k]==v for k,v in zip(order,history))]
 w=sum(p[i] for i in ids);a=sum(dp[i] for i in ids);b=sum(ddp[i] for i in ids)
 mat=sum((p[i]*Q[i] for i in ids),s.zeros(Q[0].rows))/w
 return ids,s.cancel(w),s.cancel(a),s.cancel(b),mat.applyfunc(s.cancel)

F=s.Matrix([[1,R(1,5),I/10],[R(1,5),R(6,5),R(1,7)],[-I/10,R(1,7),R(4,5)]])
check(zero(adj(F)-F) and all(F[:j,:j].det()>0 for j in range(1,F.rows+1)),'positive Hermitian odds square root')
N=F.rows; eye=s.eye(N);L=F*F;K=(L*(eye+L).inv()).applyfunc(s.cancel)
rootM=(F*(eye+L).inv()).applyfunc(s.cancel)
M=K*(eye-K)
A=s.Matrix([[R(1,9),R(1,11)+I/13,I/17],[R(1,11)-I/13,-R(1,8),R(1,19)],[-I/17,R(1,19),R(1,7)]])
B=(rootM.inv()*A*rootM.inv()).applyfunc(s.cancel)
bits=list(product((0,1),repeat=N));p=[];dp=[];ddp=[];Pis=[]
for x in bits:
 w=atom(K,x);D=(K-s.diag(*[1-z for z in x])).inv()*A
 sc=s.trace(D);ac=sc**2-s.trace(D*D)
 p.append(w);dp.append(s.cancel(w*sc));ddp.append(s.cancel(w*ac))
 J=[i for i,v in enumerate(x) if v];V=F[:,J]
 Pi=(V*(adj(V)*V).inv()*adj(V)).applyfunc(s.cancel) if J else s.zeros(N)
 Pis.append(Pi)
 check(w>0,'strict atom')
 check(zero(Pi*Pi-Pi) and zero(adj(Pi)-Pi),'orthogonal Petz projection')
 C=Pi-K
 check(zero(sc-s.trace(B*C)),'terminal score')
 check(zero(ac-(s.trace(B*C)**2-s.trace(B*C*B*C))),'terminal acceleration')
check(zero(sum(p)-1) and zero(sum(dp)) and zero(sum(ddp)),'normalization jets')
check(zero(rootM*rootM-M),'positive rational covariance square root')
check(not zero(K*A-A*K),'noncommuting complex test direction')

all_orders=[]
for order in permutations(range(N)):
 matrix_bracket=s.zeros(N);fisher=0;accel_coeff=s.zeros(len(bits),1);levels=[]
 for j,k in enumerate(order):
  level_fisher=0;level_coeff=s.zeros(len(bits),1)
  for hist in product((0,1),repeat=j):
   ids,w,a,b,Q=branch_data(bits,p,dp,ddp,Pis,hist,order[:j])
   branches=[branch_data(bits,p,dp,ddp,Pis,hist+(v,),order[:j+1]) for v in (0,1)]
   (ids0,w0,a0,b0,Q0),(ids1,w1,a1,b1,Q1)=branches
   q=s.cancel(w1/w);RR=(Q1-Q0).applyfunc(s.cancel);C=Q-K
   check(zero(Q-((1-q)*Q0+q*Q1)),'matrix martingale mean')
   check(zero(compound(RR,2)),'rank-one increment')
   check(all(RR[i,i]>=0 for i in range(N)),'rank-one increment PSD')
   check(0<s.trace(RR)<=1,'increment contraction')
   U=[order[z] for z,v in enumerate(hist) if v]
   Pu=(F[:,U]*(L.extract(U,U)).inv()*adj(F[:,U])).applyfunc(s.cancel) if U else s.zeros(N)
   rem=list(order[j:]);W=(eye-Pu)*F[:,rem];wm=W[:,0];Wminus=W[:,1:]
   D=eye+Wminus*adj(Wminus);di=D.inv();r=s.cancel((adj(wm)*di*wm)[0])
   Rgram=(di*wm*adj(wm)*di/r).applyfunc(s.cancel)
   check(zero(RR-Rgram) and zero(q-r/(1+r)),'direct Gram branching formula')
   check(zero(Q0-(Pu+eye-di)),'zero-branch Gram covariance')
   for degree in range(1,N+1):
    got=sum((p[i]*compound(Pis[i],degree) for i in ids),s.zeros(len(list(combinations(range(N),degree)))))/w
    check(zero(got-compound(Q,degree)),'all conditional compound moments')
   S=s.cancel(s.trace(B*C));T=s.cancel(S*S-s.trace(B*C*B*C))
   beta=s.cancel(s.trace(B*RR));gamma=s.cancel(s.trace(B*C*B*RR))
   check(zero(S-a/w) and zero(T-b/w),'prefix score and acceleration')
   qdot=s.cancel(a1/w-w1*a/w**2)
   qddot=s.cancel(b1/w-w1*b/w**2-2*a1*a/w**2+2*w1*a*a/w**3)
   check(zero(qdot-q*(1-q)*beta),'moving conditional first derivative')
   check(zero(qddot+2*q*(1-q)*gamma),'moving conditional second derivative')
   ds=s.cancel(a1/w1-a0/w0);dt=s.cancel(b1/w1-b0/w0)
   check(zero(ds-beta) and zero(dt-2*(S*beta-gamma)),'martingale increments')
   matrix_bracket+=w*q*(1-q)*RR*RR
   level_fisher+=w*q*(1-q)*beta*beta
   coeff=s.zeros(len(bits),1)
   for ix in ids1:coeff[ix]+=p[ix]/w1
   for ix in ids0:coeff[ix]-=p[ix]/w0
   level_coeff+=w*q*(1-q)*dt*coeff
  fisher+=level_fisher;accel_coeff+=level_coeff
  levels.append((s.cancel(level_fisher),level_coeff.applyfunc(s.cancel)))
 check(zero(matrix_bracket-M),'matrix predictable bracket')
 check(zero(fisher-sum(dp[i]**2/p[i] for i in range(len(p)))),'full Fisher bracket')
 check(zero(accel_coeff-s.Matrix(ddp)),'every frozen-log acceleration coefficient')
 total=(fisher+sum(ddp[i]*s.log(p[i]) for i in range(len(p))))
 all_orders.append({'order':[i+1 for i in order],'curvature_display':str(s.N(total,18))})

# A three-site path gives a rigorous negative mean second-level term.
Kt=s.Matrix([[R(1,2),R(1,10),0],[R(1,10),R(11,50),R(1,10)],[0,R(1,10),R(4,5)]])
At=s.Matrix([[0,0,I],[0,0,0],[-I,0,0]])
pt=[];at=[];bt=[]
for x in bits:
 v=atom(Kt,x);D=(Kt-s.diag(*[1-z for z in x])).inv()*At
 pt.append(v);at.append(s.cancel(v*s.trace(D)));bt.append(s.cancel(v*(s.trace(D)**2-s.trace(D*D))))
check(all(v>0 for v in pt),'obstruction strict atoms')
check(all(zero(v) for v in at),'obstruction full atom score is zero')
qs={}
for x,z in product((0,1),repeat=2):
 ix=[j for j,bitsj in enumerate(bits) if bitsj[0]==x and bitsj[2]==z]
 qs[x,z]=s.cancel(sum(pt[j] for j in ix if bits[j][1])/sum(pt[j] for j in ix))
check(qs=={(0,0):R(29,100),(0,1):R(91,400),(1,0):R(1,4),(1,1):R(3,16)},'exact four conditional means')
u=qs[0,0]-qs[1,0];v=qs[0,0]-qs[0,1]
check(zero(qs[1,1]-(qs[0,0]-u-v)) and u>0 and v>0,'additive conditional mean square')
h=lambda q:-q*s.log(q)-(1-q)*s.log(1-q)
corner=h(qs[0,0])+h(qs[1,1])-h(qs[1,0])-h(qs[0,1])
mean_coeff=s.zeros(len(bits),1)
for order in permutations(range(N)):
 k=order[1]
 for hist in product((0,1),repeat=1):
  # Q is immaterial for the scalar exact coefficient calculation here.
  ids,w,a,b,_=branch_data(bits,pt,at,bt,Pis,hist,order[:1])
  br=[branch_data(bits,pt,at,bt,Pis,hist+(z,),order[:2]) for z in (0,1)]
  (ids0,w0,a0,b0,_),(ids1,w1,a1,b1,_)=br
  q=w1/w;dt=b1/w1-b0/w0
  for ix in ids1:mean_coeff[ix]+=w*q*(1-q)*dt*pt[ix]/w1/6
  for ix in ids0:mean_coeff[ix]-=w*q*(1-q)*dt*pt[ix]/w0/6
mean_second=sum(mean_coeff[i]*s.log(pt[i]) for i in range(len(pt)))
# Exact logarithmic identity checked by formal prime logarithm coefficients.
def log_coeff(expr):
 out={}
 for term in s.expand(expr).as_ordered_terms():
  coeff,tail=term.as_coeff_Mul()
  if tail==1:
   if coeff:out[0]=out.get(0,0)+coeff
   continue
  assert tail.func==s.log and tail.args[0].is_Rational
  r=tail.args[0]
  for prime,m in s.factorint(s.numer(r)).items():out[prime]=out.get(prime,0)+coeff*m
  for prime,m in s.factorint(s.denom(r)).items():out[prime]=out.get(prime,0)-coeff*m
 return {k:s.cancel(v) for k,v in out.items() if not zero(v)}
check(not log_coeff(mean_second-R(2,3)*corner),'exact mean second level corner formula')
# Since h''(x)<=-4 on (0,1), corner<=-4*u*v.
negative_upper=s.cancel(-R(8,3)*u*v)
check(negative_upper==-R(1,150),'rigorous negative level bound from h second derivative')
# Full curvature is nevertheless positive by two conditional DPP odds ratios.
odds={}
for center in (0,1):
 pp={(x,z):pt[bits.index((x,center,z))] for x,z in product((0,1),repeat=2)}
 odds[center]=s.cancel(pp[0,0]*pp[1,1]/(pp[1,0]*pp[0,1]))
 check(0<odds[center]<1,'strict conditional negative association')
full=sum(bt[i]*s.log(pt[i]) for i in range(len(pt)))
positive_formula=-2*((1-Kt[1,1])*s.log(odds[0])+Kt[1,1]*s.log(odds[1]))
check(not log_coeff(full-positive_formula),'exact positive total curvature compensation')

cert={'status':'PASS','exact_assertions':checks,'identity_example_dimension':N,
 'orders':all_orders,'obstruction':{'conditional_means':{str(k):str(v) for k,v in qs.items()},
 'mean_second_level_rigorous_upper':str(negative_upper),
 'mean_second_level_display':str(s.N(mean_second,18)),
 'full_curvature_display':str(s.N(full,18)),
 'conditional_odds':{str(k):str(v) for k,v in odds.items()}},
 'scope':'Finite exact checks support the proved all-dimension identities; neither numerical observations nor this example prove universal concavity.'}
(ROOT/'certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(cert,indent=2))
