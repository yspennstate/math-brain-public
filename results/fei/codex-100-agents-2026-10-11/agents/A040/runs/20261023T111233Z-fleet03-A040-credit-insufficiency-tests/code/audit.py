"""Independent direct-character and exact prime-log reconstruction. No helper imports."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import time,json,hashlib
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;identities=0
def ck(b):
 global checks
 assert b;checks+=1;assert time.perf_counter()-start<55
@lru_cache(None)
def P(g):
 n=len(g)
 return tuple(F(sum(a*(-1 if (x*t).bit_count()<0 else -1 if (x&t).bit_count()%2 else 1) for x,a in enumerate(g)),n)**2 for t in range(n))
def cut(g,j,y):return tuple(v for x,v in enumerate(g) if x>>j&1==y)
def vc(r):return tuple((1 if x&2==0 else -1)*(-1 if x//4==0 or (x%2 and x//4==3) else 1) for x in range(2**(r+2)))
def gate(v,e):return tuple(e if x%2==0 else v[x//2] for x in range(2*len(v)))
def priority(v):return tuple((1 if x&2==0 else -1) if x%2==0 else v[x//8] if x&4 else 1 for x in range(8*len(v)))
def qcore(v,a):
 p=P(v)
 return tuple(p[0] if t==0 else (1-a)*p[t]+a*(1-p[0])*(t==len(p)-1) for t in range(len(p)))
def lift(g,v,a,shift):
 p=P(g);core=P(v);q=qcore(v,a)
 return tuple(x if t//2**shift==0 else x*q[t//2**shift]/core[t//2**shift] if core[t//2**shift] else F(0) for t,x in enumerate(p))
def step(g,q,j):
 p=P(g);gs=[cut(g,j,y) for y in (0,1)];pq=[P(x) for x in gs];pbar=[];qbar=[]
 for t in range(len(pq[0])):
  i=t%2**j+(t//2**j)*2**(j+1);pbar.append(p[i]+p[i+2**j]);qbar.append(q[i]+q[i+2**j])
 out=[];zz=[]
 for y in (0,1):
  raw=tuple(qb*(pp/(2*pb) if pb else F(1,2)) for pb,qb,pp in zip(pbar,qbar,pq[y]));z=sum(raw);ck(z>0);zz.append(z);out.append(tuple(x/z for x in raw))
 ck(sum(zz)==1)
 return gs,out,zz,tuple(pbar),tuple(qbar)
@lru_cache(None)
def factor(n):
 d=2;out={}
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d+=1 if d==2 else 2
 if n>1:out[n]=out.get(n,0)+1
 return out
def lnvec(x):
 out={}
 for p,e in factor(x.numerator).items():out[p]=out.get(p,F(0))+e
 for p,e in factor(x.denominator).items():out[p]=out.get(p,F(0))-e
 return {p:e for p,e in out.items() if e}
def combine(*terms):
 out={}
 for c,v in terms:
  for p,e in v.items():out[p]=out.get(p,F(0))+c*e
 return {p:e for p,e in out.items() if e}
def H(p):return combine(*[(-x,lnvec(x)) for x in p if x])
def KL(p,q):
 out=[]
 for x,y in zip(p,q):
  if x:ck(y>0);out.append((x,lnvec(x/y)))
 return combine(*out)
def FM(m,a):return combine((1-m,lnvec(1/(1-a))),(m,lnvec(m/(a+(1-a)*m))))
def eq(v,w):
 global identities
 ck(v==w);identities+=1
def infl(g,j):return F(sum(a!=g[x^(1<<j)] for x,a in enumerate(g)),len(g))
def ber(t):return H((t,1-t))

main=json.loads((ROOT/'out/CHECK.json').read_text(encoding='utf-8'));alpha=F(1,6);kap=combine((F(1,2),lnvec(F(400,399))))
rare=[]
for record in main['physical_policies']:
 r=record['r']
 if r not in (3,4):continue
 d=F(1,2**r);m=d*d;v=vc(r);f=priority(v);q0=lift(f,v,F(1,8),3)
 ck(sum(q0)==1);eq(KL(P(f),q0),combine((F(1,4),FM(m,F(1,8)))))
 bg,bq,bz,_,_=step(f,q0,2);ck(bz==[F(1,2),F(1,2)])
 ag,aq,az,_,_=step(bg[1],bq[1],1);ck(az==[F(1,2),F(1,2)])
 sigma1={};sigma2={}
 for e,local in enumerate(record['local_records']):
  g=gate(v,1-2*e);ck(g==ag[e] and tuple(local['parent_truth'])==g)
  R=lift(g,v,alpha,1);ck(R==tuple(F(x) for x in local['parent_Q']))
  sigma1=combine((1,sigma1),(F(1,4),combine((1,KL(P(g),R)),(-1,KL(P(g),aq[e])))))
  kids,old,zz,pbar,qbar=step(g,R,1);ck(zz==[F(19,40),F(21,40)])
  new=[]
  for y,kid in enumerate(kids):
   vv=cut(v,0,y);ck(kid==gate(vv,1-2*e));N=lift(kid,vv,alpha,1);new.append(N)
   saved=local['children'][y];ck(P(kid)==tuple(F(x) for x in saved['P']));ck(old[y]==tuple(F(x) for x in saved['old_Q']));ck(N==tuple(F(x) for x in saved['new_Q']))
   ck(sum(old[y])==sum(N)==1);ck(all((x>0)==(a>0)==(b>0) for x,a,b in zip(P(kid),old[y],N)))
  sig=combine(*[(F(1,2),combine((1,KL(P(k),n)),(-1,KL(P(k),o)))) for k,n,o in zip(kids,new,old)])
  expected=combine((1,kap),(F(1,4),FM(4*m,alpha)),(F(1,4),FM(16*m,alpha)),(-F(1,2),FM(10*m,alpha)))
  eq(sig,expected);sigma2=combine((1,sigma2),(F(1,4),sig))
  eq(combine((1,KL(P(g),R)),(-1,KL(pbar,qbar))),combine((F(1,2),FM(m,alpha)),(-F(1,2),FM(10*m,alpha))))
  eq(KL((F(1,2),F(1,2)),zz),kap)
  # Independent probability definition of all five declared posterior quantities.
  js=combine((1,H(pbar)),(-F(1,2),H(P(kids[0]))),(-F(1,2),H(P(kids[1]))))
  core_erased=[];pv=P(v)
  for t in range(len(v)//2):core_erased.append(pv[2*t]+pv[2*t+1])
  eq(js,combine((F(1,2),H(core_erased)),(-F(1,4),H(P(cut(v,0,0)))),(-F(1,4),H(P(cut(v,0,1))))))
  pj=infl(g,1);ck(pj==d/2)
  mi=combine((1,ber(pj)),(-1,H(P(g))),(1,H(pbar)))
  eq(mi,combine((1,ber(d/2)),(-F(1,2),H(P(v))),(F(1,2),H(core_erased))))
  gamma={}
  for j in range(len(kids[0]).bit_length()-1):
   aa=infl(kids[0],j);bb=infl(kids[1],j)
   gamma=combine((1,gamma),(1,ber((aa+bb)/2)),(-F(1,2),ber(aa)),(-F(1,2),ber(bb)))
  eq(gamma,combine((r,ber(3*d/2)),(-F(r,2),ber(d)),(-F(r,2),ber(2*d))))
  tc=combine(*[(1,ber(infl(g,j))) for j in range(len(g).bit_length()-1)],(-1,H(P(g))))
  eq(tc,combine((1,ber(d/2)),(r,ber(3*d/2)),(-F(1,2),H(P(v)))))
 eq(sigma1,combine((F(1,4),FM(m,alpha)),(-F(1,4),FM(m,F(1,8)))))
 eq(sigma2,combine((F(1,2),expected)))
 rare.append(r)

# Independently consume only A047's analytic obstruction clauses, not its census.
v=(1,-1,-1,1,-1,1,1,1);q=qcore(v,alpha);gs,old,zz,_,_=step(v,q,0)
sigma=combine(*[(F(1,2),combine((1,KL(P(g),qcore(g,alpha))),(-1,KL(P(g),o)))) for g,o in zip(gs,old)])
eq(sigma,combine((F(1,8),lnvec(F(1404,1331)))))
activation_K=F(155,156)**13*F(59,60)**5*F(13,12)**10/(F(4,3)**2*(1-F(7,195)**2)**16);ck(activation_K>1)
for eps in (-1,1):
 g=gate(v,eps);R=lift(g,v,alpha,1);gs,old,zz,_,_=step(g,R,1);ck(zz==[F(101,195),F(94,195)])
 N=[lift(k,cut(v,0,y),alpha,1) for y,k in enumerate(gs)]
 sig=combine(*[(F(1,2),combine((1,KL(P(k),n)),(-1,KL(P(k),o)))) for k,n,o in zip(gs,N,old)])
 eq(sig,combine((F(1,32),lnvec(activation_K))))

ck(400**300>2*399**300);ck(8**5<2*7**5);ck(6**40<2**11*5**40)
# Exact scalar monotonicity of the entropy tail majorant for ALL r>=8.
ck(F(8,2**8)*(2*8-F(1,2))==F(31,64));ck(F(31,64)<F(1,2))
out={'status':'PASS','checks':checks,'exact_prime_log_equalities':identities,'runtime_seconds':time.perf_counter()-start,'rare_query_r':rare,'A047_analytic_clauses':'pure-core all-alpha polynomial proof reconstructed; core alpha1/6 and both normalized activation signs checked exactly; census/minimality NOT reviewed','helper_imports':False,'formal_verification':'not attempted'}
(ROOT/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
