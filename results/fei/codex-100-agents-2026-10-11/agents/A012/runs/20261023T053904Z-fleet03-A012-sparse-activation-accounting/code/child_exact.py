from pathlib import Path
from fractions import Fraction as F
import json,sys,time,hashlib
R=Path(__file__).resolve().parents[1];mode=sys.argv[1];N=64 if mode=='author' else 32
T0=time.perf_counter();checks=0;smallest=None;witness=None;hist={};digest=hashlib.sha256()
def ck(x):
 global checks
 assert x,checks;checks+=1
def fw(a):
 a=list(a);h=1
 while h<16:
  for k in range(0,16,2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
logs={k:(k**N).bit_length()-1 for k in range(1,17)}
for k,l in logs.items():ck(2**l<=k**N<2**(l+1))
edge_masks=[sum(1<<s for s in range(16) if not(s>>j&1)) for j in range(4)]
w=[16]+[0]*15;signs=[1]*16
for step in range(65536):
 if mode=='author':
  phase=step;w=fw([1-2*((phase>>s)&1) for s in range(16)])
 else:
  phase=step^(step>>1)
  if step:
   s=(step&-step).bit_length()-1;old=signs[s];signs[s]=-old
   for t in range(16):w[t]-=2*old*(1-2*((s&t).bit_count()%2))
 squares=[x*x for x in w];ck(sum(squares)==256)
 energy=sum(t.bit_count()*x for t,x in enumerate(squares))
 edges=[((phase^(phase>>(1<<j)))&edge_masks[j]).bit_count() for j in range(4)]
 ck(energy==32*sum(edges));ck(sum(squares[t] for t in range(16) if t&8)==32*edges[3])
 # H<=8-2/(256N)sum w^2 floor(log2(abs(w)^N)).
 gap=F(4*energy*N-8*256*N+2*sum(x*x*logs[abs(x)] for x in w if x),256*N)
 if energy:
  ck(gap>=F(1,8))
  if smallest is None or gap<smallest:smallest=gap;witness=phase
 else:ck(phase in (0,65535));ck(gap==0)
 key=(sum(x!=0 for x in w),energy);hist[str(key)]=hist.get(str(key),0)+1
 digest.update(phase.to_bytes(2,'little'));digest.update(bytes(edges))
 ck(time.perf_counter()-T0<55)
ck(F(16,15)**8<2)
out={'status':'PASS','mode':mode,'cases':65536,'assertions':checks,'smallest_certified_nonconstant_4I_minus_H':str(smallest),'witness':witness,'lower_log_power':N,'reference_allowance':'log2(16/15)<1/8, by exact (16/15)^8<2','histogram':hist,'physical_edge_digest':digest.hexdigest(),'seconds':time.perf_counter()-T0}
(R/'out'/('CHILD_'+mode+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='histogram'}))
