from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
from math import comb
import itertools,json,time,sys
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0; roots=0; extras=0
pilot='--pilot' in sys.argv
def ck(x):
 global checks
 checks+=1
 assert x,checks
 assert time.perf_counter()-start<55,'frozen runtime cap'
def walsh(t):
 a=list(t);s=1
 while s<len(a):
  for j in range(0,len(a),2*s):
   for k in range(j,j+s):a[k],a[k+s]=a[k]+a[k+s],a[k]-a[k+s]
  s*=2
 return a
def ln(x):
 z=(x-1)/(x+1);v=sum((2*z**(2*k+1)/Q(2*k+1) for k in range(24)),Q(0));err=2*abs(z)**49/(49*(1-z*z))
 return v-err,v+err
L2=ln(Q(2));ck(L2[0]>Q(2,3))
@lru_cache(None)
def logint(n):
 k=n.bit_length()-1;l,u=ln(Q(n,1<<k));D=1<<72
 lo=k+l/L2[1];hi=k+u/L2[0]
 return Q((lo*D).__floor__(),D),Q((hi*D).__ceil__(),D)
@lru_cache(None)
def ent(key,N):
 lo=hi=Q(0);shift=2*(N.bit_length()-1)
 for a,c in key:
  if a:
   l,u=logint(a);w=Q(c*a*a,N*N);lo+=w*(shift-2*u);hi+=w*(shift-2*l)
 return lo,hi
def entropy(a,N):return ent(tuple(sorted(Counter(abs(x) for x in a).items())),N)
def influence(t):
 return sum((Q(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(len(t).bit_length()-1)),Q(0))
rows=[]
def verify(h,A,V):
 global roots
 N=len(h);M=len(V);p=Q(sum(A),N);e=[1-2*a for a in A];g=[h[x]-A[x] for x in range(N)]
 F=[V[y] if A[x] else h[x] for x in range(N) for y in range(M)]
 fw=walsh(F);aw=walsh(A);gw=walsh(g);vw=walsh(V)
 ck(sum(V)==0);ck(all(not a or z==1 for z,a in zip(h,A)))
 for x in range(N):
  ck(fw[x*M]==gw[x]*M)
  for y in range(1,M):ck(fw[x*M+y]==aw[x]*vw[y])
 ih=influence(h);ie=influence(e);iv=influence(V)
 shared=sum((Q(sum(F[z]!=F[z^(M<<j)] for z in range(N*M)),N*M) for j in range(N.bit_length()-1)),Q(0))
 private=influence(F)-shared
 L=sum((Q(sum(A[x]!=A[x^(1<<j)] and h[x]!=h[x^(1<<j)] for x in range(N)),N) for j in range(N.bit_length()-1)),Q(0))
 ck(shared==ih-L+ie/2);ck(ih<=2*shared);ck(ie<=2*shared);ck(private==p*iv)
 HH=entropy(fw,N*M);Hh=entropy(walsh(h),N);He=entropy(walsh(e),N);HV=entropy(vw,M)
 if p:
  ck(HH[1]<=p*HV[0]+2*Hh[0]+Q(3,4)*He[0]+Q(15,2)*ie)
  # Independent unnormalized indicator-entropy conversion.
  CA=entropy(aw,N);l,u=logint(p.numerator);l2,u2=logint(p.denominator)
  lp_lo=l2-u;lp_hi=u2-l
  ck(CA[1]-p*lp_lo<=He[0]/4+ie)
  if all(z==1 for z in h):ck(He[1]<=2*HH[0])
 else:ck(HH==Hh)
 roots+=1
 rows.append({'d':N.bit_length()-1,'p':str(p),'J':str(shared),'Ih':str(ih),'Ie':str(ie),'private_bits':M.bit_length()-1})
expected=0
for d in range(1,3 if pilot else 4):
 N=1<<d;expected+=sum(comb(N,k)*2**(N-k) for k in range(N//2+1))
 for h in itertools.product((-1,1),repeat=N):
  pos=[i for i,z in enumerate(h) if z==1]
  for k in range(min(N//2,len(pos))+1):
   for chosen in itertools.combinations(pos,k):
    A=[int(i in chosen) for i in range(N)];verify(h,A,(-1,1))
    if not pilot and d==3 and extras<128:
     verify(h,A,tuple(1 if x.bit_count()<2 else -1 for x in range(8)));extras+=1
ck(roots==expected+extras)
# A missing balance hypothesis invalidates the physical lower bounds: constant -1 replaces h-positive set.
h=(-1,1);A=(0,1);V=(-1,);ff=(-1,-1)
ck(influence(ff)==0 and influence(h)>0 and sum(V)!=0)
# Independent direct character sums check the Walsh implementation, including signs.
for t in itertools.product((-1,1),repeat=8):
 direct=[sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(8)) for s in range(8)]
 ck(walsh(t)==direct)
out={'status':'PASS','pilot':pilot,'exact_assertions':checks,'roots':roots,'exhaustive_pairs':expected,'Maj3_extra_roots':extras,'runtime_seconds':time.perf_counter()-start,'full_FEI':'OPEN','coverage':rows}
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='coverage'}))
