from pathlib import Path
import json,time,hashlib
R=Path(__file__).resolve().parents[1];O=R/'out'
helper=R.parent/'20261023T065941Z-fleet03-A078-coding-and-padding/code/direct.py'
spec={'version':'direct-affine-coset4','family':'actual two-profile coded NAND2; all3 nonzero parity columns,8x8 explicit biased two-bit profiles,ALL physical shared restrictions','case_count':5184,'symmetry':'none','arithmetic':'direct character sums,Fraction exact edges,independent prime-log24-term outward bounds','memory_estimate_MB':100,'max_runtime_seconds':55,'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest()}
(O/'FROZEN_INDEPENDENT.json').write_text(json.dumps(spec,indent=2),encoding='utf-8',newline='\n');(R/'code/direct.py').write_bytes(helper.read_bytes())
from direct import F,plus,gg,spectrum,entropy,positive,child,influence
from itertools import product
start=time.monotonic();checks=0
def ck(b):
 global checks
 checks+=1;assert b,checks;assert time.monotonic()-start<55
def syndrome(x,P):return (x&3)^(P if (x>>2)&1 else 0)
profiles=[(1,1,1,1),(-1,-1,-1,-1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1),(-1,1,1,1),(1,-1,-1,-1),(1,1,1,-1)]
states=bothmeans=rankstable=0
for P in [1,2,3]:
 for v in profiles:
  for w in profiles:
   for pat in product([-1,0,1],repeat=3):
    actual=[x for x in range(8) if all(b==-1 or (x>>i)&1==b for i,b in enumerate(pat))]
    sy=[syndrome(x,P) for x in actual];ss=set(sy);p=F(1,len(ss));r=len(ss).bit_length()-1;live=[t for t in [0,1] if t in ss];pr=[v,w]
    f=tuple(pr[s][z] if s in [0,1] else 1 if s==2 else -1 for z in range(4) for s in sy)
    H=entropy(f);U=plus(*[(p,entropy(pr[t])) for t in live]);rv=r*p*sum((1-F(sum(pr[t]),4)**2 for t in live),F(0))
    av,aw=spectrum(v),spectrum(w)
    X=plus(*[(p/2,plus((1,gg(a+b)),(1,gg(a-b)),(-2,gg(a)),(-2,gg(b)))) for a,b in list(zip(av,aw))[1:]]) if len(live)==2 else {}
    means=tuple(F(sum(f[z*len(sy)+s] for z in range(4)),4) for s in range(len(sy)))
    Z=plus((1,entropy(means)),(1,{2:rv+1}),*[(-p,gg(F(sum(pr[t]),4))) for t in live])
    states+=1;ck(H==plus((1,U),(1,X),(1,{2:rv-1}),(1,Z)));ck(positive(Z))
    bothmeans+=int(len(live)==2 and sum(v)!=0 and sum(w)!=0)
    for t in live:
     mask=tuple(F(s==t) for s in sy);ck(sum(abs(a) for a in spectrum(mask))==1)
    for j in range(len(actual).bit_length()-1):
     a,b=child(f,j,0),child(f,j,1)
     ck(positive(plus((1,H),(-F(1,2),entropy(a)),(-F(1,2),entropy(b)))))
     # Rank preservation is detected from the ACTUAL image fibers, not a matrix rank routine.
     im0={sy[x] for x in range(len(sy)) if (x>>j)&1==0}
     im1={sy[x] for x in range(len(sy)) if (x>>j)&1==1}
     if im0==im1:
      rankstable+=1;ck(entropy(a)==H==entropy(b))
ck(states==5184)
# Independent original donor edge audit; all13 actual physical coordinates.
truth=[]
for x in range(8192):
 physical=x%64;s=(physical%32)^(17 if physical>>5 else 0);z=(x>>6)%16;pad=(x>>10)%4;y=1-2*((x>>12)&1)
 b=(-1)**((z&1)*((z>>1)&1)+((z>>2)&1)*((z>>3)&1))
 truth.append(y*b if s==0 else y*(1-2*(z==0 and pad==0)) if s==1 else 1 if s.bit_count()<=2 else -1)
truth=tuple(truth);infs=[influence(truth,i) for i in range(13)]
expected=[F(409,1024)]+[F(7,16)]*5+[F(17,1024)]*4+[F(1,1024)]*2+[F(1,16)]
ck(infs==expected);ck(sum(infs)==F(2783,1024));ck(infs[5]==F(7,16))
result={'status':'PASS','exact_assertions':checks,'restricted_states':states,'both_nonzero_mean_states':bothmeans,'rank_preserving_queries':rankstable,'physical_donor_influences':[str(a) for a in infs],'physical_total_influence':str(sum(infs)),'added_parity_influence':str(infs[5]),'runtime_seconds':time.monotonic()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'INDEPENDENT.json').write_text(json.dumps(result,indent=2),encoding='utf-8',newline='\n');print(json.dumps(result))
