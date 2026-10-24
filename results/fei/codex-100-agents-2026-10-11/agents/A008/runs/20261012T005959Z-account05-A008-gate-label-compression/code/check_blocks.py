from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import comb,factorial
from pathlib import Path
from collections import Counter
import json,time,sys
PILOT='--pilot' in sys.argv;NMAX=1 if PILOT else 9;LIMIT=59 if PILOT else 899
start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x
 if checks%1000==0 and time.perf_counter()-start>LIMIT:raise TimeoutError('Frozen job deadline')
def rounded(x):
 den=2**80
 lo=F((x[0].numerator*den)//x[0].denominator,den)
 hi=F(-((-x[1].numerator*den)//x[1].denominator),den)
 ck(lo<=x[0]<=x[1]<=hi)
 return lo,hi
def add(x,y):return rounded((x[0]+y[0],x[1]+y[1]))
def scale(a,x):return rounded((a*x[0],a*x[1]) if a>=0 else (a*x[1],a*x[0]))
def logseries(y):
 ck(1<=y<=2)
 z=(y-1)/(y+1);zi=rounded((z,z));z2=rounded((zi[0]**2,zi[1]**2))
 power=zi;val=(F(0),F(0))
 for k in range(24):
  val=add(val,scale(F(2,2*k+1),power))
  power=rounded((power[0]*z2[0],power[1]*z2[1]))
 tail=F(9,196*3**49)
 return rounded((val[0],val[1]+tail))
LN2=logseries(F(2));LOGE=rounded((1/LN2[1],1/LN2[0]))
@lru_cache(None)
def lg(q):
 q=F(q);ck(q>0);k=q.numerator.bit_length()-q.denominator.bit_length()
 y=q/(F(2)**k)
 while y<1:y*=2;k-=1
 while y>=2:y/=2;k+=1
 lo,hi=logseries(y)
 corners=[v/d for v in (lo,hi) for d in LN2]
 return rounded((min(corners)+k,max(corners)+k))
def fifth(x):
 target=x**6;den=2**40;lo=0;hi=den
 while hi-lo>1:
  mid=(lo+hi)//2
  if F(mid,den)**5<=target:lo=mid
  else:hi=mid
 ck(F(lo,den)**5<=target<=F(hi,den)**5)
 return F(lo,den),F(hi,den)
def fwht(a):
 a=a[:];h=1
 while h<len(a):
  for b in range(0,len(a),2*h):
   for j in range(b,b+h):
    x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
  h*=2
 return a
def partitions(n,low=1):
 if not n:yield ()
 for j in range(low,n+1):
  for tail in partitions(n-j,j):yield (j,)+tail
local={}
for w in range(1,NMAX+1):
 count=2**w-1;rank=scale(F(2**(w-1),count),lg(factorial(w)));subset=(F(0),F(0));size=(F(0),F(0))
 for s in range(1,w+1):
  theta=[(F(1),F(1)) if r<=s else fifth(F(s,r)) for r in range(1,w+1)]
  dp=[(F(1),F(1))]+[(F(0),F(0)) for _ in range(s)]
  for th in theta:
   for k in range(s,0,-1):dp[k]=add(dp[k],(dp[k-1][0]*th[0],dp[k-1][1]*th[1]))
  Z=dp[s];Zlog=(lg(Z[0])[0],lg(Z[1])[1])
  exact_weight_average=(F(0),F(0))
  for r in range(s+1,w+1):exact_weight_average=add(exact_weight_average,scale(F(6*s,5*w),lg(F(r,s))))
  cost=add(add(lg(s*(s+1)),Zlog),exact_weight_average)
  weight=F(comb(w,s),count);subset=add(subset,scale(weight,cost));size=add(size,scale(weight,lg(s*(s+1))))
  # An independent subset sum brackets the same elementary symmetric polynomial.
  slo=F(0);shi=F(0)
  for B in combinations(range(w),s):
   plo=F(1);phi=F(1)
   for j in B:plo*=theta[j][0];phi*=theta[j][1]
   slo+=plo;shi+=phi
   ratio=F(1)
   for r in B:ratio*=r+1
   ck(ratio>=factorial(s))
  rank=add(rank,scale(-F(comb(w,s),count),lg(factorial(s))))
  ck(Z[0]<=slo<=shi<=Z[1])
  ck(Z[1]<(F(6)**s)*F(11,4)**s)
 mean_s=F(w*2**(w-1),count)
 # Exact reciprocal identity in every rank.
 for r in range(1,w+1):
  ck(sum((F(comb(r-1,k)*r,2**(r-1)*(k+1)) for k in range(r)),F(0))==2*(1-F(1,2**r)))
 ck(rank[1]<=mean_s);ck(size[1]<mean_s*lg(3)[0])
 local[w]={'rank':rank,'subset_cost':subset,'mean_s':mean_s}
rows=[]
CRES=add((F(16,5),F(16,5)),LOGE)
CCOMP=add(add((F(26,5),F(26,5)),scale(2,lg(3))),scale(2,LOGE))
for n in range(1,NMAX+1):
 for widths in partitions(n):
  blocks=[];offset=0
  for w in widths:blocks.append(((1<<w)-1)<<offset);offset+=w
  vals=[1 if any(x&B==B for B in blocks) else -1 for x in range(2**n)]
  P=[F(z*z,4**n) for z in fwht(vals)]
  ps=[F(1,2**w) for w in widths];qs=[1-p for p in ps]
  Q0=F(1);Dplus=F(1)
  for p,q in zip(ps,qs):Q0*=q;Dplus*=1+p
  D=Dplus-1;v=4*Q0*(1-Q0);I=2*Q0*sum((w*p/q for w,p,q in zip(widths,ps,qs)),F(0))
  ck(P[0]==(1-2*Q0)**2);ck(sum(P)==1)
  ck(sum((S.bit_count()*p for S,p in enumerate(P)),F(0))==I)
  for j in range(n):
   physical=F(sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals))),len(vals))
   ck(physical==sum((p for S,p in enumerate(P) if S>>j&1),F(0)))
  for S,p in enumerate(P):
   if not S:continue
   hatfactor=F(1)
   for B,pi,qi in zip(blocks,ps,qs):hatfactor*=pi if S&B else qi
   ck(p==4*hatfactor*hatfactor)
  root=scale(v,lg(D));R=root;C=root
  for B,w,p,q in zip(blocks,widths,ps,qs):
   mu=4*p*Q0;Il=2*Q0*w*p/q
   ck(sum((prob for S,prob in enumerate(P) if S&B),F(0))==mu)
   ck(mu*local[w]['mean_s']==Il)
   R=add(R,scale(mu,add((F(w),F(w)),scale(F(6,5),local[w]['rank']))))
   C=add(C,scale(mu,add((F(w+1),F(w+1)),local[w]['subset_cost'])))
  root=add(root,(sum((4*p*Q0*w for p,w in zip(ps,widths)),F(0)),)*2)
  ck(root[1]<=scale(I,add((F(2),F(2)),LOGE))[0])
  ck(R[1]<CRES[0]*I);ck(C[1]<CCOMP[0]*I)
  # Direct entropy enclosure; the reference includes its binary split.
  H=(F(0),F(0))
  for prob,multiplicity in Counter(P).items():
   if prob:H=add(H,scale(-prob*multiplicity,lg(prob)))
  h=(F(0),F(0))
  for prob in [v,1-v]:
   if prob:h=add(h,scale(-prob,lg(prob)))
  ck(H[1]<(h[0]+C[0]));ck(h[1]<=2*I)
  rows.append({'widths':widths,'I':str(I),'v':str(v),'residual_interval':[str(x) for x in R],'run_cost_interval':[str(x) for x in C],'entropy_interval':[str(x) for x in H]})
  pp=Path(__file__).resolve().parents[1]/'out'/('PILOT_PARTIAL.json' if PILOT else 'BLOCK_PARTIAL.json')
  pp.write_text(json.dumps({'completed':False,'cases_done':len(rows),'cases_exact':rows},indent=2)+'\n',encoding='utf-8')
ck(len(rows)==(1 if PILOT else 96));ck(CRES[1]<F(47,10));ck(CCOMP[1]+2<F(67,5))
out={'helper':'A008-block-v5','completed':True,'mode':'pilot' if PILOT else 'full','cases':len(rows),'checks':checks,'seconds':time.perf_counter()-start,'residual_constant_interval':[str(x) for x in CRES],'run_constant_interval':[str(x) for x in CCOMP],'cases_exact':rows}
ck(out['seconds']<(60 if PILOT else 900))
p=Path(__file__).resolve().parents[1]/'out'/('PILOT_V5_CHECK.json' if PILOT else 'BLOCK_CERTIFICATES.json');p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='cases_exact'},indent=2))
