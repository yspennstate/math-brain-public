from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,time,hashlib,sys
R=Path(__file__).resolve().parents[1];O=R/'out';O.mkdir(exist_ok=True)
A=R.parents[1];old=A/'runs/20261023T124031Z-fleet03-A078-coding-and-padding/code'
sys.path.insert(0,str(old))
from exact import add,logvec,fwht,infl,restrict,entropy,scalar,nonneg,interval
spec=dict(helper_version='A078-majority-complement-discount-v1',family='g=(1+a)/2+(1-a)Maj_(2r+1)/2; f=character_all*g; F=full one-bit parity lift',domain=dict(actual_r=[0,1,2,3,4],rational_bound_r=list(range(1,129))),case_count=dict(actual_roots=5,binomial_bound_rows=128),symmetry='no truth-table reduction; permutation symmetry used only in analytic formulas',arithmetic='Fraction Walsh/edges; exact prime-log vectors and outward log bounds; integer binomial inequalities',memory_estimate_MB=60,max_runtime_seconds=55,helper_sha256=hashlib.sha256((old/'exact.py').read_bytes()).hexdigest())
(O/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
start=time.monotonic();checks=0
def ck(b):
 global checks
 checks+=1;assert b,checks
 assert time.monotonic()-start<55,'frozen pilot runtime cap'
def U(v):
 p=[a*a for a in fwht(v)];pi=p[:]
 for j in range(len(v).bit_length()-1):
  for s in range(len(pi)):
   if not(s>>j)&1:pi[s]+=pi[s|(1<<j)]
 return add(*[(a,logvec(pi[s]/a)) for s,a in enumerate(p) if a])
def lgterm(w,q):return (w,logvec(q))
def serial(v):return {str(p):str(a) for p,a in v.items()}
records=[]
for r in (0,1,2,3,4):
 n=2*r+1;N=n+1;c=Q(comb(2*r,r),4**r)
 coeff={k:((-1)**((k-1)//2))*c*Q(comb(r,(k-1)//2),comb(2*r,k-1)) for k in range(1,n+1,2)}
 b={l:coeff[n-l]**2 for l in range(0,n,2)}
 AA={l:sum((Q(comb(n-l,t-l))*b[t] for t in range(l,n,2)),Q(0)) for l in b}
 d=add((1,scalar(Q(1,4))),*[lgterm(Q(comb(n,l))*b[l]/4,1+1/AA[l]) for l in b])
 uf=add((1,scalar(Q(1,2))),*[lgterm(Q(comb(n,l))*b[l]/2,(1+AA[l])/b[l]) for l in b])
 uF=add((1,uf),(-1,d))
 ts={s:b[s+(s%2)]/4 for s in range(n)}
 Ws={s:sum((Q(comb(n-1-s,t-s))*ts[t] for t in range(s,n)),Q(0)) for s in ts}
 uy=add(*[lgterm(Q(comb(n-1,s))*ts[s],(2*Ws[s]+Q(1,2))/ts[s]) for s in ts],*[lgterm(Q(comb(n-1,s))*ts[s],Ws[s]/ts[s]) for s in ts],lgterm(Q(1,2),1+c*c))
 G=add((-2,d),(n,uF),(-n,uy))
 maj=tuple(1 if 2*x.bit_count()<n else -1 for x in range(1<<n))
 g=tuple(1 if not(x&1) else maj[x>>1] for x in range(1<<N))
 f=tuple(v*(-1 if x.bit_count()%2 else 1) for x,v in enumerate(g))
 F=tuple(f[x^((1<<N)-1)] if z else f[x] for z in (0,1) for x in range(1<<N))
 ck(all(x in (-1,1) for x in F));ck(U(f)==uf);ck(U(F)==uF)
 ck(add((1,U(f)),(-1,U(F)))==d)
 ck(infl(F,N)==Q(1,2));ck(sum((infl(f,i) for i in range(N)),Q(0))==n+Q(1,2)-n*c/2)
 ck(sum((infl(F,i) for i in range(N+1)),Q(0))==n+1-n*c/2)
 ck(entropy(fwht(f))==entropy(fwht(g)));ck(entropy(fwht(F))==entropy(fwht(f)))
 ck(entropy(fwht(g))==add((1,scalar(2)),(Q(1,2),entropy(fwht(maj)))))
 for k in range(1,n+1,2):ck(fwht(maj)[(1<<k)-1]==coeff[k])
 actualG={}
 for j in range(N+1):
  children=[restrict(F,j,v) for v in (0,1)]
  duc=add((1,uF),(-Q(1,2),U(children[0])),(-Q(1,2),U(children[1])))
  actualG=add((1,actualG),(1,duc))
  if j in (0,N):ck(duc==add((-1,d)))
  else:
   ck(U(children[0])==uy);ck(U(children[1])==uy);ck(nonneg(add((-1,duc))))
 ck(actualG==G);ck(nonneg(add((-1,G),(-2,d))))
 if r:
  ck(c*c>=Q(1,4*r));ck(c*c<=Q(1,r+1))
  ck(nonneg(add((1,d),(-1,scalar(Q(1,4))),lgterm(-n*c*c/4,1+1/(c*c)))))
 records.append(dict(r=r,n=n,physical_dimension=N+1,c=str(c),padding_influence='1/2',Iseed=str(n+Q(1,2)-n*c/2),Ilift=str(n+1-n*c/2),d=serial(d),Useed=serial(uf),Ulift=serial(uF),G=serial(G),pad_DeltaU=serial(add((-1,d)))))
for r in range(1,129):
 c=Q(comb(2*r,r),4**r)
 ck(c*c>=Q(1,4*r));ck(c*c<=Q(1,r+1))
 ck((2*r+1)**2*(r+2)<=4*(r+1)**3)
 ck((2*r+1)**2*(r+1)>=4*r*(r+1)**2)
result=dict(status='PASS',exact_assertions=checks,actual_roots=len(records),runtime_seconds=time.monotonic()-start,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),full_FEI='OPEN',scope='fixed finite validation; all-r theorem proved separately')
(O/'FAMILY.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
(O/'CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
