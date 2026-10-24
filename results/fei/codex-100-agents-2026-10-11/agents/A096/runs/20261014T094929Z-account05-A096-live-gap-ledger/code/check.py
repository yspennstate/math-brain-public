from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
RUN=Path(__file__).resolve().parents[1]
spec=json.loads((RUN/'out/FROZEN_SPEC.json').read_text())
t0=time.perf_counter();assertions=0;nodes=0;policies=0
def ck(x):
 global assertions
 assertions+=1
 assert x,assertions
 assert time.perf_counter()-t0<55,'frozen runtime guard'
@lru_cache(None)
def factors(n):
 out={};d=2
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d=3 if d==2 else d+2
 if n>1:out[n]=out.get(n,0)+1
 return out
def plus(*terms):
 ans={}
 for c,d in terms:
  for p,v in d.items():ans[p]=ans.get(p,F(0))+c*v
 return {p:v for p,v in ans.items() if v}
def log(q):
 q=F(q);assert q>0
 return plus((1,factors(q.numerator)),(-1,factors(q.denominator)))
def ce(p,q):return plus(*[(v,log(1/q[i])) for i,v in enumerate(p) if v])
def ent(p):return ce(p,p)
def kl(p,q):return plus((1,ce(p,q)),(-1,ent(p)))
def fw(v):
 a=list(v);k=1
 while k<len(a):
  for o in range(0,len(a),2*k):
   for j in range(o,o+k):a[j],a[j+k]=a[j]+a[j+k],a[j]-a[j+k]
  k*=2
 return tuple(F(x,len(v)) for x in a)
@lru_cache(None)
def amplitudes(v):return fw(v)
def spectrum(v):return tuple(a*a for a in amplitudes(tuple(v)))
def insert(t,j,s):return (t&((1<<j)-1))|((t>>j)<<(j+1))|(s<<j)
def child(v,j,s):return tuple(v[insert(t,j,s)] for t in range(len(v)//2))
def fold(q,j):return tuple(q[insert(t,j,0)]+q[insert(t,j,1)] for t in range(len(q)//2))
def influence(v,j):return F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
def total(v):return sum((influence(v,j) for j in range(len(v).bit_length()-1)),F(0))
def lnunit(q):
 z=(q-1)/(q+1);lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(32)),F(0))
 return lo,lo+2*z**65/(65*(1-z*z))
LN2=lnunit(F(2))
@lru_cache(None)
def lint(p):
 q=F(p);k=0
 while q>=2:q/=2;k+=1
 a,b=lnunit(q)
 return a/LN2[1]+k,b/LN2[0]+k
def interval(d):
 lo=hi=F(0)
 for p,c in d.items():
  a,b=lint(p)
  if c<0:a,b=b,a
  lo+=c*a;hi+=c*b
 grid=1<<90
 return F((lo*grid).numerator//(lo*grid).denominator,grid),F(-((-hi*grid).numerator//(-hi*grid).denominator),grid)
def nonnegative(d):
 if not d:return True
 return interval(d)[0]>=0
def unit(v,q,j):
 global nodes
 nodes+=1;p=spectrum(v);m=fold(p,j);qf=fold(q,j)
 ck(sum(q)==sum(qf)==sum(p)==sum(m)==1)
 ck(all(not x or q[i]>0 for i,x in enumerate(p)))
 kids=[child(v,j,s) for s in (0,1)];ps=[spectrum(w) for w in kids]
 a=amplitudes(tuple(v))
 for s,w in enumerate(kids):
  aa=amplitudes(w)
  for t,x in enumerate(aa):ck(x==a[insert(t,j,0)]+(-1)**s*a[insert(t,j,1)])
  ck(sum(ps[s])==1);ck(all(not x or qf[t]>0 for t,x in enumerate(ps[s])))
 ck(all((ps[0][t]+ps[1][t])/2==m[t] for t in range(len(m))))
 B=plus((1,ent(p)),(-1,ent(m)))
 refund=plus((1,kl(p,q)),(-1,kl(m,qf)))
 conditional={}
 for t,x in enumerate(p):
  if x:
   u=t&((1<<j)-1)|((t>>(j+1))<<j)
   conditional=plus((1,conditional),(x,log((x/m[u])/(q[t]/qf[u]))))
 ck(refund==conditional)
 avgce=plus((F(1,2),ce(ps[0],qf)),(F(1,2),ce(ps[1],qf)))
 ck(ce(p,q)==plus((1,B),(1,avgce),(1,refund)))
 J=plus((1,ent(m)),(-F(1,2),ent(ps[0])),(-F(1,2),ent(ps[1])))
 ck(plus((1,kl(p,q)),(-F(1,2),kl(ps[0],qf)),(-F(1,2),kl(ps[1],qf)))==plus((1,refund),(-1,J)))
 ck(total(v)==influence(v,j)+(total(kids[0])+total(kids[1]))/2)
 # Nonnegative conditional KL follows analytically by Gibbs; no precision needed to re-certify zero.
 return kids,qf,B,refund
def replay(v,q,labels,policy,depth=0):
 if not policy or not labels:return {},ce(spectrum(v),q),{}
 jlabel=policy[0];j=labels.index(jlabel)
 kids,qf,B,R=unit(v,q,j);remaining=[k for k in labels if k!=jlabel]
 sub=[replay(kids[s],qf,remaining,policy[1:] if len(policy)>1 else [],depth+1) for s in (0,1)]
 bill=plus((1,B),*[(F(1,2),x[0]) for x in sub]);term=plus(*[(F(1,2),x[1]) for x in sub]);refund=plus((1,R),*[(F(1,2),x[2]) for x in sub])
 ck(ce(spectrum(v),q)==plus((1,bill),(1,term),(1,refund)))
 return bill,term,refund
def root(a,b,r,kind):
 n=a+b;N=1<<n;s=F(1,1<<a);p=F(1,1<<r);rho=4*p/N;lam=2*p/F(1<<b);mu=1-2*s
 g=tuple(-1 if y&((1<<a)-1)==0 else 1 for y in range(N));P=spectrum(g)
 if kind==0:R=P
 elif kind==1:R=tuple(F(1,N) for _ in range(N))
 else:R=tuple(F(t+1,N*(N+1)//2) for t in range(N))
 R0=tuple(mu*mu if t==0 else (1-mu*mu)*R[t]/(1-R[0]) for t in range(N))
 rp=tuple((1-lam)*R0[t]+(lam*mu if t==0 else 0)+rho/N for t in range(N))
 v=tuple((-g[y] if y==0 and u==0 else g[y]) for u in range(1<<r) for y in range(N));pf=spectrum(v)
 marginal=tuple(sum(pf[t+u*N] for u in range(1<<r)) for t in range(N))
 ck(marginal==tuple((1-lam)*P[t]+(lam*mu if t==0 else 0)+rho/N for t in range(N)))
 q=tuple(rp[t]*pf[t+u*N]/marginal[t] for u in range(1<<r) for t in range(N))
 ck(sum(q)==1)
 raw=ce(P,R);cost=ce(pf,q);Ig=total(g);C=2*p*b/N;E=2*p*a/N;J=2*p*r/N
 ck(total(v)==Ig+C-E+J)
 ck(nonnegative(plus((1,raw),(10*(C+E+J),{2:F(1)}),(-1,cost))))
 if kind==0:ck(nonnegative(plus((18*total(v),{2:F(1)}),(-1,cost))))
 return v,q,n,cost
params=[(a,b,r,k) for a in (1,2,3) for b in (0,1,2) for r in (1,2) for k in range(3)]
if '--pilot' in sys.argv:params=[(2,1,1,k) for k in range(3)]
certificates=[]
for a,b,r,k in params:
 v,q,n,cost=root(a,b,r,k);labels=list(range(n+r))
 for j in range(n):
  bill,term,ref=replay(v,q,labels,[j]);policies+=1
  for l in range(n):
   if l==j:continue
   replay(v,q,labels,[j,l]);policies+=1
 # Outcome-adaptive two-step policy, carrying the same coarsened reference on both first children.
 kids,qf,B,R=unit(v,q,0);rem=labels[1:];subs=[]
 for outcome in (0,1):
  target=rem[0] if outcome==0 else rem[-1]
  subs.append(replay(kids[outcome],qf,rem,[target]))
 ck(cost==plus((1,B),(1,R),*[(F(1,2),d) for sub in subs for d in sub]));policies+=1
 # Untouched arbitrary 2-bit terminal, every sign table; reference uniform, full CE=2.
 for mask in range(16):
  h=tuple(1 if mask>>x&1 else -1 for x in range(4));ph=spectrum(h);rh=(F(1,4),)*4
  vp=tuple(x*y for y in h for x in v);qp=tuple(x*y for y in rh for x in q)
  ck(spectrum(vp)==tuple(x*y for y in ph for x in spectrum(v)))
  ck(ce(spectrum(vp),qp)==plus((1,cost),(2,{2:F(1)})))
  childp=child(vp,0,0);qfp=fold(qp,0)
  ck(qfp==tuple(x*y for y in rh for x in qf))
  ck(ce(spectrum(childp),qfp)==plus((1,ce(spectrum(kids[0]),qf)),(2,{2:F(1)})))
 certificates.append({'a':a,'b':b,'r':r,'reference':k,'cost_interval':[str(x) for x in interval(cost)],'root_influence':str(total(v))})
 (RUN/'out/CHECKPOINT.json').write_text(json.dumps({'roots_complete':len(certificates),'assertions':assertions}))
# Actual local-rate obstruction: a=2,b=0,r=1 uniform supplied source. The + active outcome is constant but Q_fold is not vacuum.
v,q,n,cost=root(2,0,1,1);kids,qf,B,R=unit(v,q,0)
constant=kids[1];ck(len(set(constant))==1);ck(total(constant)==0);debt=ce(spectrum(constant),qf);ck(interval(debt)[0]>0)
obstruction={'parameters':[2,0,1],'source_reference':'uniform','query':0,'physical_outcome_bit':1,'complete_child_reference':[str(x) for x in qf],'constant_terminal_CE_interval':[str(x) for x in interval(debt)],'terminal_influence':'0','conclusion':'No finite K pays this prescribed inherited constant-terminal CE by its own influence; ancestor account is required.'}
(RUN/'out/LOCAL_RATE_OBSTRUCTION.json').write_text(json.dumps(obstruction,indent=2)+'\n')
out={'status':'PASS','root_reference_cases':len(params),'policies':policies,'nodes':nodes,'assertions':assertions,'runtime_seconds':time.perf_counter()-t0,'certificates':certificates}
name='PILOT.json' if '--pilot' in sys.argv else 'CHECK.json'
(RUN/'out'/name).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='certificates'},indent=2))
