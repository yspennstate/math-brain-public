from fractions import Fraction as F
from pathlib import Path
import json,time,sys
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'out').mkdir(exist_ok=True)
START=time.monotonic(); checks=0; nodes=0; releases=0; biased=0; ghosts=0
def ck(b):
 global checks
 checks+=1
 assert b
 if time.monotonic()-START>55: raise TimeoutError('frozen 55s runtime limit')
@lru_cache(maxsize=16384)
def factors(n):
 d=2;ans={}
 while d*d<=n:
  while n%d==0: ans[d]=ans.get(d,0)+1;n//=d
  d+=1
 if n>1:ans[n]=ans.get(n,0)+1
 return ans
def add(*xs):
 a={}
 for x in xs:
  for p,c in x.items():a[p]=a.get(p,F(0))+c
 return {p:c for p,c in a.items() if c}
def scale(x,c):return {p:v*c for p,v in x.items() if v*c}
def logq(x):
 x=F(x);return add(factors(x.numerator),{p:-c for p,c in factors(x.denominator).items()})
def KL(p,q):
 ans={}
 for a,b in zip(p,q):
  if a:ck(b>0);ans=add(ans,scale(logq(a/b),a))
 return ans
def H(p):return scale(KL(p,[F(1)]*len(p)),-1)
def spectrum(f):
 n=len(f);return [F(sum(f[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(n)),n)**2 for s in range(n)]
def calibrate(p,q):
 global releases
 t=p[0];z=q[0]
 if t==1:qn=list(p);b=F(1)
 else:
  ck(z<1);b=(1-t)/(1-z);qn=[t]+[b*x for x in q[1:]]
 d=KL([t,1-t],[z,1-z]);ck(add(KL(p,q),scale(d,-1))==KL(p,qn))
 ck(sum(qn)==1)
 if d:releases+=1
 return qn,d
def split(f,q,completion):
 global nodes,biased,ghosts
 nodes+=1
 p=spectrum(f);m=len(f)//2
 fs=[f[t::2] for t in [0,1]];ps=[spectrum(g) for g in fs]
 R=[p[2*s]+p[2*s+1] for s in range(m)]
 Z=[q[2*s]+q[2*s+1] for s in range(m)]
 ck(all((ps[0][s]+ps[1][s])/2==R[s] for s in range(m)))
 k=[[ps[t][s]/(2*R[s]) if R[s] else (F(1,2) if completion==0 else F(t==1)) for s in range(m)] for t in [0,1]]
 ghosts+=sum(bool(Z[s] and not R[s]) for s in range(m))
 r=[sum(Z[s]*k[t][s] for s in range(m)) for t in [0,1]]
 ck(sum(r)==1 and min(r)>0)
 if r[0]!=F(1,2):biased+=1
 qs=[[Z[s]*k[t][s]/r[t] for s in range(m)] for t in [0,1]]
 E=add(KL(p,q),scale(KL(R,Z),-1));O=KL([F(1,2)]*2,r)
 ck(KL(p,q)==add(E,O,scale(add(*(KL(ps[t],qs[t]) for t in [0,1])),F(1,2))))
 return fs,ps,qs,E,O
def tree(f,q,depth=0):
 p=spectrum(f);qc,d=calibrate(p,q)
 if len(f)==1:return d
 fs,ps,qs,E,O=split(f,qc,depth%2)
 totals=[tree(fs[t],qs[t],depth+1) for t in [0,1]]
 total=add(d,E,O,scale(add(*totals),F(1,2)))
 ck(total==KL(p,q))
 return total
def witness():
 f=[1,1,1,-1];p=spectrum(f);q=list(map(lambda x:F(x,128),[63,1,32,32]))
 ck(p==[F(1,4)]*4);ck(all(qi>=F(1,32)*pi for qi,pi in zip(q,p)))
 qc,d=calibrate(p,q)
 old=split(f,q,0);new=split(f,qc,0)
 ck(old[4]=={});ck(new[4]==scale(logq(F(4225,3264)),F(1,2)))
 ck(qc==[F(1,4),F(3,260),F(24,65),F(24,65)])
 # 4*(Onew-d) is log2 of this positive rational.
 ratio=F(4225,3264)**2/F(32,63)/F(96,65)**3
 ck(ratio>1);ck(scale(add(new[4],scale(d,-1)),4)==logq(ratio))
 # Near the positive-support boundary: limiting gap >0 iff 2^8>3^5.
 ck(2**8>3**5)
 tree(f,q)
 return {'p':[str(x) for x in p],'q':[str(x) for x in q],'q_calibrated':[str(x) for x in qc], 'four_times_gap_log_argument':str(ratio),'exact_sign':'strictly positive'}
w=witness()
counts={}
for n in range(1,int(sys.argv[1]) + 1 if len(sys.argv)>1 else 4):
 refs=0;N=1<<n
 for bits in range(1<<N):
  f=[1 if bits>>x&1 else -1 for x in range(N)];p=spectrum(f)
  # All original ordered pairs, including collisions and source-zero witnesses.
  for a in range(N):
   for b in range(N):
    if n==3 and a!=b and a!=0:continue
    q=[x/3+F((s==a)+(s==b),3) for s,x in enumerate(p)]
    qc,d=calibrate(p,q)
    for completion in [0,1]:
     fs,ps,qs,E,O=split(f,qc,completion)
     new=[];ds=[]
     for t in [0,1]:
      qt,dt=calibrate(ps[t],qs[t]);new.append(qt);ds.append(dt)
     ck(KL(p,q)==add(d,E,O,scale(add(*ds),F(1,2)),scale(add(*(KL(ps[t],new[t]) for t in [0,1])),F(1,2))))
    # History-adapted all-depth completion, both branches, all conditional nodes.
    if a==b or (a==0 and b==N-1):tree(f,q)
    refs+=1
 counts[str(n)]=refs
 result={'status':'PASS','n_completed':n,'counts':counts,'assertions':checks,'nodes':nodes,'nonzero_calibrations':releases,'biased_query_outcomes':biased,'ghost_rows':ghosts,'runtime_seconds':time.monotonic()-START,'witness':w}
 (ROOT/'out/CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps(result))
