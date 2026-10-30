from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import time,json,sys,hashlib
ROOT=Path(__file__).resolve().parents[1];START=time.monotonic()
PILOT='--pilot' in sys.argv;checks=states=transitions=0
def ck(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
 if time.monotonic()-START>(55 if PILOT else 120):raise TimeoutError('frozen cap')
def fw(tt):
 w=list(tt);s=1
 while s<len(w):
  for k in range(0,len(w),2*s):
   for j in range(k,k+s):a,b=w[j],w[j+s];w[j],w[j+s]=a+b,a-b
  s*=2
 return w
def insert(v,i,b):return (v&((1<<i)-1))|((v>>i)<<(i+1))|(b<<i)
def edges(tt,j):return Q(sum(tt[x]!=tt[x^(1<<j)] for x in range(len(tt))),len(tt))
def refs(p,profile):
 if not profile:return p
 denom=sum(range(2,len(p)+1));return (p[0],)+tuple((1-p[0])*Q(s+1,denom) for s in range(1,len(p)))
a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1);b=tuple(1-x*x for x in a)
aa=tuple(Q(x,16) for x in fw(a));bb=tuple(Q(x,16) for x in fw(b));beta=sum(x*x for x in bb)
ck(beta==Q(3,8))
def run_core(g,L,D):
 global states,transitions
 n=len(g).bit_length()-1;N=n*L
 cw=fw(g);p=tuple(Q(x*x,len(g)**2) for x in cw);mu=Q(cw[0],len(g))
 coreinf=tuple(edges(g,j) for j in range(n))
 for depth in range(D+1):
  for chosen in combinations(range(N),depth):
   for values in product((0,1),repeat=depth):
    states+=1;fixed=dict(zip(chosen,values));remaining=[j for j in range(N) if j not in fixed]
    groups=[[k for k,j in enumerate(remaining) if j//L==c] for c in range(n)]
    ck(all(groups))
    eta=[sum(v for j,v in fixed.items() if j//L==c)%2 for c in range(n)]
    masks=[sum(1<<k for c in range(n) if J>>c&1 for k in groups[c]) for J in range(1<<n)]
    ck(len(set(masks))==1<<n)
    tt=[]
    for x in range(1<<len(remaining)):
     y=sum((eta[c]+sum(x>>k&1 for k in groups[c]))%2<<c for c in range(n))
     tt.append(g[y])
    w=fw(tt);expected=[0]*len(tt)
    for J,mask in enumerate(masks):expected[mask]=cw[J]*(1<<(len(remaining)-n))*(-1 if sum(eta[c] for c in range(n) if J>>c&1)%2 else 1)
    ck(w==expected);ck(sum(v*v for v in w)==len(tt)**2)
    pp=tuple(Q(x*x,len(tt)**2) for x in w)
    ck(sorted(x for x in pp if x)==sorted(x for x in p if x))
    ck(Q(w[0],len(tt))==mu)
    for k,j in enumerate(remaining):ck(edges(tt,k)==coreinf[j//L])
    ck(sum(Q(w[s]*w[s],len(tt)**2)*s.bit_count() for s in range(len(tt)))==sum(len(groups[c])*coreinf[c] for c in range(n)))
    for profile in (0,1):
     R=refs(p,profile);qq=[Q(0)]*len(tt)
     for J,mask in enumerate(masks):qq[mask]=R[J]
     ck(sum(qq)==1)
     ck(sorted((x,y) for x,y in zip(pp,qq) if x or y)==sorted((x,y) for x,y in zip(p,R) if x or y))
     if depth==D:continue
     for k,j in enumerate(remaining):
      if not profile:transitions+=1
      ck(len(groups[j//L])>=2)
      pm=tuple(pp[insert(v,k,0)]+pp[insert(v,k,1)] for v in range(len(tt)//2))
      qm=tuple(qq[insert(v,k,0)]+qq[insert(v,k,1)] for v in range(len(tt)//2))
      ck(all(not(pp[insert(v,k,0)] and pp[insert(v,k,1)]) for v in range(len(tt)//2)))
      ck(all(not(qq[insert(v,k,0)] and qq[insert(v,k,1)]) for v in range(len(tt)//2)))
      # One common deterministic spectral bit implies conditional KL=0 even for reference-only atoms.
      ck(all(not pm[v] or pp[insert(v,k,0)]*qm[v]==qq[insert(v,k,0)]*pm[v] for v in range(len(pm))))
      for outcome in (0,1):
       child=tuple(tt[insert(v,k,outcome)] for v in range(len(tt)//2));ch=fw(child)
       cp=tuple(Q(v*v,len(child)**2) for v in ch)
       ck(cp==pm);ck(Q(ch[0],len(child))==mu)
      # A033 FULL coarse vacuum+tail law, for BOTH tag signs, equals its inherited reference.
      ck(qq[1<<k]==0)
      for sig in (1,-1):
       pv=tuple((aa[u]+sig*mu*bb[u])**2 for u in range(16))
       qv=tuple((aa[u]+sig*mu*bb[u])**2+bb[u]**2*qq[1<<k] for u in range(16))
       ck(pv+(beta*(1-mu*mu),)==qv+(beta*(1-mu*mu),))
       ck(sum(pv)+beta*(1-mu*mu)==1)

for n in (1,2,3):
 cores=product((1,-1),repeat=1<<n)
 if PILOT and n==3:break
 for g in cores:run_core(g,2,1)
for g in product((1,-1),repeat=4):
 if PILOT:break
 run_core(g,3,2)
if not PILOT:
 for g in ((-1,1,1,1),(1,-1,-1,1),(1,1,-1,-1),(1,1,1,1)):run_core(g,4,3)
out={'status':'PASS','pilot':PILOT,'helper':'A033-parity-block-zero-window-v1','physical_face_states':states,'internal_query_transitions':transitions,'exact_assertions':checks,'runtime_seconds':time.monotonic()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out'/('pilot.json' if PILOT else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
