from pathlib import Path
import time,json
from fractions import Fraction as F
import exact as e
ROOT=Path(__file__).resolve().parents[1];START=time.perf_counter();N=0;ZERO=0
def ck(x,s):
 global N
 N+=1
 if not x:raise AssertionError(s)
def eq(a,b,s):ck(not e.plus((1,a),(-1,b)),s)
def ge(a,b,s):
 d=e.plus((1,a),(-1,b));ck(not d or e.interval(d)[0]>=0,s)
def ds(t):
 p=tuple(F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t))**2,len(t)**2) for s in range(len(t)))
 n=len(t).bit_length()-1
 d=tuple(F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n))
 for i in range(n):ck(d[i]==sum(p[s] for s in range(len(p)) if s>>i&1),'direct coefficients versus physical edges')
 H=e.ent(p);M=e.plus(*[(1,e.ent((x,1-x))) for x in d]);return p,H,M
def restrict(t,i,b):
 n=len(t).bit_length()-1
 out=[]
 for y in range(1<<(n-1)):
  bits=[y>>j&1 for j in range(n-1)];bits.insert(i,b);x=sum(z<<j for j,z in enumerate(bits));out.append(t[x])
 return tuple(out)
for mask in range(256):
 t=tuple(1 if mask>>x&1 else -1 for x in range(8));p,H,M=ds(t)
 ck(p==e.stats(t)[0],'all original direct spectra agree with FWHT')
 for R in [tuple(F(1,8) for _ in range(8)),tuple((x+F(1,8))/2 for x in p)]:
  K=e.kl(p,R)
  for i in range(3):
   cs=[restrict(t,i,b) for b in (0,1)];st=[ds(c) for c in cs];pc=[x[0] for x in st]
   pe=[];qe=[];qq=[[],[]];reach=[F(),F()]
   for s in range(4):
    bits=[s>>j&1 for j in range(2)];bits.insert(i,0);s0=sum(x<<j for j,x in enumerate(bits));s1=s0+(1<<i)
    a=p[s0]+p[s1];z=R[s0]+R[s1];pe.append(a);qe.append(z)
    if not a and z:ZERO+=1
    for b in (0,1):
     kernel=pc[b][s]/(2*a) if a else F(1,2);qq[b].append(z*kernel);reach[b]+=qq[b][-1]
   ck(sum(reach)==1 and min(reach)>0,'direct prediction normalization')
   refs=[tuple(x/reach[b] for x in qq[b]) for b in (0,1)]
   Ks=[e.kl(pc[b],refs[b]) for b in (0,1)];O=e.kl((F(1,2),F(1,2)),reach);E=e.plus((1,K),(-1,e.kl(pe,qe)))
   eq(K,e.plus((1,E),(1,O),(F(1,2),Ks[0]),(F(1,2),Ks[1])),'independent normalized KL chain')
   ge(E,{},'direct erasure credit nonnegative')
   ge(e.plus((1,K),(2,M)),e.plus((1,O),(F(1,2),Ks[0]),(F(1,2),Ks[1]),(1,st[0][2]),(1,st[1][2])),'direct 2M prefix drift')
   hc,hq,hr,hO,hKs,hE,hz=e.transport(t,i,R)
   ck(hc==cs and hq==[list(x) for x in refs] and hr==reach,'independent full transported laws agree')
 ck(time.perf_counter()-START<55,'runtime guard')
# Positive rejection control: a correlated Boolean spectrum, supported reference R=p.
t=(-1,1,1,1,1,1,1,1);p,H,M=ds(t);TC=e.plus((1,M),(-1,H));K=e.kl(p,p)
ck(not K,'negative-control source-matching reference');ck(e.interval(TC)[0]>0,'actual nonzero correlation')
bad_gap=e.plus((1,K),(1,M),(-1,TC),(-1,M));ck(e.interval(bad_gap)[1]<0,'insufficient one-M surrogate is rejected')
ck(ZERO>0,'reference-only rows actually exercised');ck(time.perf_counter()-START<55,'final runtime guard')
res={'status':'PASS','direct_assertions':N,'scalar_helper_assertions_excluded':e.COUNT,'query_cases':1536,'positive_reference_zero_source_rows':ZERO,'seconds':time.perf_counter()-START,'negative_control':{'surrogate_guard_rejected':True,'gap_interval':e.enciv(bad_gap),'scope':'does not claim optimal one-M policy is false'}}
(ROOT/'out/DIRECT.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8');print(json.dumps(res))
