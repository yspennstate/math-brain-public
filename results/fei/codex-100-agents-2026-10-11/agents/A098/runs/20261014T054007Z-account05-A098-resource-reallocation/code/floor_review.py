from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json,time,sys
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks
 assert time.perf_counter()-start<55,'Frozen runtime guard'
@lru_cache(None)
def factor(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def addlog(a,w,x):
 assert x>0
 for p,k in factor(x.numerator).items():a[p]+=w*k
 for p,k in factor(x.denominator).items():a[p]-=w*k
def combine(*args):
 out=defaultdict(F)
 for w,a in args:
  for p,c in a.items():out[p]+=w*c
 return {p:c for p,c in out.items() if c}
def cost(p,q):
 out=defaultdict(F)
 for x,y in zip(p,q):
  if x:addlog(out,x,1/y)
 return combine((1,out))
def divergence(p,q):
 out=defaultdict(F)
 for x,y in zip(p,q):
  if x:addlog(out,x,x/y)
 return combine((1,out))
def lnseries(x):
 z=(x-1)/(x+1);N=16
 lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
 return lo,lo+2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
ln2=lnseries(F(2))
@lru_cache(None)
def logbounds(x):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 lo,hi=lnseries(x)
 return F(k)+lo/ln2[1],F(k)+hi/ln2[0]
def enclosure(form):
 lo=hi=F(0)
 for p,c in form.items():
  a,b=logbounds(F(p));lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 return lo,hi
def nonnegative(form):
 if not form:ck(True)
 else:ck(enclosure(form)[0]>=0)
def spectrum(truth):
 n=(len(truth)-1).bit_length();a=truth[:];step=1
 while step<len(a):
  for base in range(0,len(a),2*step):
   for j in range(base,base+step):
    u,v=a[j],a[j+step];a[j],a[j+step]=u+v,u-v
  step*=2
 p=[F(v*v,len(a)**2) for v in a];ck(sum(p)==1)
 influences=[]
 for i in range(n):
  edge=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(len(truth))),len(truth))
  ck(edge==sum(p[s] for s in range(len(p)) if s>>i&1));influences.append(edge)
 return p,influences
def references(p):
 N=len(p)
 return [p[:],[F(1,N)]*N,[F(j+1,N*(N+1)//2) for j in range(N)]]
def root(a,b,r,point):
 n=a+b;N=2**n;s=F(1,2**a);t=F(1,N);p=F(1,2**r)
 source=[-1 if x&((1<<a)-1)==0 else 1 for x in range(N)]
 pg,inf_g=spectrum(source)
 truth=[source[x&(N-1)]+(2 if (x>>n)==0 and (x&(N-1))==(point<<a) else 0) for x in range(2**(n+r))]
 ck(all(x in [-1,1] for x in truth));pf,inf=spectrum(truth)
 Ig=sum(inf_g);C=2*p*t*b;E=2*p*t*a;J=2*r*p*t;If=sum(inf)
 ck(Ig==2*a*s);ck(If==Ig+C-E+J);ck(sum(inf[n:])==J);ck(E<=Ig/2)
 rho=4*p*t;lam=2*p*F(1,2**b);mu=1-2*s;w=[1-lam,lam*mu,rho]
 ck(sum(w)==1 and min(w)>=0)
 vacuum=[F(int(j==0)) for j in range(N)];uniform=[t]*N
 q=[sum(pf[c*N+j] for c in range(2**r)) for j in range(N)]
 for j in range(N):ck(q[j]==w[0]*pg[j]+w[1]*vacuum[j]+w[2]*uniform[j])
 ck(all(x>0 for x in q));ck(sum(q)==1)
 outputs=[]
 for rid,R in enumerate(references(pg)):
  raw=cost(pg,R);R0=[mu*mu if j==0 else (1-mu*mu)*R[j]/(1-R[0]) for j in range(N)]
  ck(sum(R0)==1);cal=cost(pg,R0);nonnegative(combine((1,raw),(-1,cal)))
  Rp=[w[0]*R0[j]+w[1]*vacuum[j]+w[2]*uniform[j] for j in range(N)]
  ck(sum(Rp)==1);ck(all(x>0 for x in Rp));ck(Rp[0]==q[0])
  Q=[Rp[j]*pf[c*N+j]/q[j] for c in range(2**r) for j in range(N)]
  ck(sum(Q)==1)
  ce=cost(pf,Q);D=divergence(pf,Q);Dcal=divergence(pg,R0);kappa=defaultdict(F)
  for j in range(N):
   for weight,Pcomp,Rcomp in zip(w,[pg,vacuum,uniform],[R0,vacuum,uniform]):
    mass=weight*Pcomp[j]
    if mass:addlog(kappa,mass,Pcomp[j]*Rp[j]/(Rcomp[j]*q[j]))
  ck(not combine((1,D),(-w[0],Dcal),(1,kappa)))
  ck(not combine((1,D),(-1,divergence(q,Rp))))
  nonnegative(combine((1,raw),(-1,ce),(1,{2:10*(C+E+J)})))
  # Exact cost-dependent source price: C0=c/Ig, rate 2*C0+10.
  nonnegative(combine((2*If/Ig,raw),(1,{2:10*If}),(-1,ce)))
  if rid==0:
   nonnegative(combine((1,{2:4*Ig}),(-1,raw)))
   nonnegative(combine((1,{2:18*If}),(-1,ce)))
  # Debit equation after the actual erased edges, with K fixed before evaluation.
  for K in [10,18]:
   direct=combine((1,{2:K*If}),(-1,ce))
   lower=combine((1,{2:K*Ig+(K-10)*C-(K+10)*E+(K-10)*J}),(-1,raw))
   nonnegative(combine((1,direct),(-1,lower)))
  outputs.append({'pf':pf,'Q':Q,'ce':ce,'D':D,'If':If})
 return outputs
pilot='pilot' in sys.argv;tensor='tensor' in sys.argv;roots=refs=terminal=0
name='PILOT' if pilot else ('TENSOR' if tensor else 'FLOOR')
with (OUT/(name+'_CASES.jsonl')).open('w',encoding='utf-8') as journal:
 if not tensor:
  domain=[(1,0,1,0)] if pilot else [(a,b,r,k) for a in [1,2,3] for b in [0,1,2] for r in [1,2] for k in range(2**b)]
  for a,b,r,k in domain:
   output=root(a,b,r,k);roots+=1;refs+=len(output)
   journal.write(json.dumps({'a':a,'b':b,'r':r,'dummy_point':k,'references':len(output),'status':'PASS'})+'\n');journal.flush()
 else:
  floors=root(2,1,2,0)
  for table in range(16):
   ph,infs=spectrum([1 if table>>x&1 else -1 for x in range(4)])
   for R in references(ph)[:2]:
    ch=cost(ph,R);dh=divergence(ph,R)
    for floor in floors:
     pt=[u*v for u in ph for v in floor['pf']];qt=[u*v for u in R for v in floor['Q']]
     ck(sum(pt)==sum(qt)==1)
     ck(not combine((1,cost(pt,qt)),(-1,ch),(-1,floor['ce'])))
     ck(not combine((1,divergence(pt,qt)),(-1,dh),(-1,floor['D'])))
     # Influence additivity directly from the tensor spectrum.
     nt=(len(floor['pf'])-1).bit_length();specI=sum(F(s.bit_count())*mass for s,mass in enumerate(pt))
     ck(specI==sum(infs)+floor['If']);terminal+=1
   journal.write(json.dumps({'terminal_table':table,'two_terminal_references_three_floors':'PASS'})+'\n');journal.flush()
receipt={'status':'PASS','root_cases':roots,'reference_cases':refs,'terminal_cases':terminal,'assertions':checks,
 'runtime_seconds':time.perf_counter()-start,'memory_estimate_mb':90,'source_checker_imported':False,'arithmetic':'Fraction/prime-log exact identities; N16 certified signs'}
(OUT/(name+'_CHECK.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
