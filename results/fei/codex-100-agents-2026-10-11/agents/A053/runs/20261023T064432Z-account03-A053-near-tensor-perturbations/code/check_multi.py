from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache
from collections import Counter
import sys,time,json
import arithmetic as a
RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter();checks=0
def check(v):
 global checks
 checks+=1
 assert v,checks
 if time.perf_counter()-START>55:raise RuntimeError('frozen 55 second guard')
def save(n,x):(RUN/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
@lru_cache(None)
def hf(key,den):
 lo=hi=F(0)
 for z,k in key:
  if z:
   l,u=a.log2(F(z,den));lo-=F(k*z,den)*u;hi-=F(k*z,den)*l
 return lo,hi
def H(w,N):return hf(tuple(sorted(Counter(v*v for v in w).items())),N*N)
def plus(x,y):return x[0]+y[0],x[1]+y[1]
def loss(root,ch0,ch1):return root[0]-(ch0[1]+ch1[1])/2,root[1]-(ch0[0]+ch1[0])/2
def children(g,i):
 n=(len(g)-1).bit_length()
 return [[g[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(1<<(n-1))] for b in (0,1)]
roots=cuts=relevant=zero_beta=empty_saturated=0
def case(seed,sw,E):
 global roots,cuts,relevant,zero_beta,empty_saturated
 n=(len(seed)-1).bit_length();N=len(seed);p=F(1,N);R=len(E)
 g=seed.copy()
 for x in E:g[x]*=-1
 w=a.fwht(g);eh=[v-u for v,u in zip(w,sw)]
 check(sum(v*v for v in eh)==4*R*N)
 check(all(abs(v)<=2*R for v in eh))
 check(sum(v*v for v in w)==N*N)
 support=[s for s,v in enumerate(sw) if v]
 check(len(support)*(n+1)<=N)
 hg=H(w,N);infs=a.infs(g)
 for i in range(n):
  cuts+=1
  beta=M=F(0)
  occupied=[];empty=[]
  for s in range(N):
   if (s>>i)&1:continue
   t=s|(1<<i);check(not(sw[s] and sw[t]))
   if sw[s] or sw[t]:
    anchor,off=(s,t) if sw[s] else (t,s)
    beta+=F(w[off]*w[off],N*N)
    occupied.append((w[anchor],w[off]))
   else:
    M+=F(w[s]*w[s]+w[t]*w[t],N*N);empty.append((w[s],w[t]))
  check(beta<=4*R*R*p/F(n+1));check(M<=4*R*p)
  if beta:check(beta>=4*p*p)
  else:zero_beta+=1
  if M==4*R*p:empty_saturated+=1
  c0,c1=children(g,i);w0=a.fwht(c0);w1=a.fwht(c1)
  # Direct physical restrictions agree with signed sums before squaring.
  for t in range(N//2):
   s=(t&((1<<i)-1))|((t>>i)<<(i+1))
   check(2*w0[t]==w[s]+w[s|(1<<i)])
   check(2*w1[t]==w[s]-w[s|(1<<i)])
  L=loss(hg,H(w0,N//2),H(w1,N//2))
  if R:
   bound=(10*R+F(17,2)*R*R)*p
   check(L[1]<bound)
   if infs[i]:
    relevant+=1;check(infs[i]>=2*p)
    K=5*R+F(17,4)*R*R
    check(L[1]<K*infs[i])
    check(10*R*R*infs[i]-L[1]>F(3,2)*R*R*p)
  else:
   # One nonzero amplitude per row gives identical spectral multisets.
   check(Counter(v*v for v in w if v)==Counter((2*v)**2 for v in w0 if v))
   check(Counter(v*v for v in w if v)==Counter((2*v)**2 for v in w1 if v))
  # Prove the claimed complete original deficit identity at several K.
  childI=(sum(a.infs(c0))+sum(a.infs(c1)))/2
  check(sum(infs)==infs[i]+childI)
 roots+=1
pilot='--pilot' in sys.argv
seeds=[]
for code in range(256):
 f=[-1 if (code>>x)&1 else 1 for x in range(8)];w=a.fwht(f)
 s=[x for x,v in enumerate(w) if v]
 if all((x^y).bit_count()>=3 for x,y in combinations(s,2)):
  seeds.append((f,w))
check(len(seeds)==16)
for f,w in seeds:
 for R in range(3 if pilot else 4):
  for E in combinations(range(8),R):case(f,w,E)
if not pilot:
 seed=a.coded_truth([-1,1,1,1]);w=a.fwht(seed)
 for E in [(0,),(0,1),(0,7),(0,63),(0,1,2),(0,1,7),(0,1,2,3),(0,7,56,63)]:
  case(seed,w,E)
save('PILOT.json' if pilot else 'EXACT_CHECK.json',{'status':'PASS','assertions':checks,'qualifying_n3_seeds':len(seeds),'roots':roots,'coordinate_cuts':cuts,'relevant_cuts':relevant,'zero_beta_cuts':zero_beta,'empty_energy_saturated':empty_saturated,'runtime_seconds':time.perf_counter()-START,'max_n':3 if pilot else 6,'arithmetic':'integer Walsh/edges, exact Fraction, rational atanh24 intervals','pilot':pilot})
print((RUN/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).read_text(encoding='utf-8'))
