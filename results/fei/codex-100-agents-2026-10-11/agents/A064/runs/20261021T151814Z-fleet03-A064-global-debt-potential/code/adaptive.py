from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, sys, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
SOURCE=Path(r'agents\A061\runs\20261014T085352Z-fleet05-A061-entropy-process\out\EXHAUSTIVE_CHECK.json')
START=time.perf_counter(); CAP=55; SCALE=1<<96; ASSERTS=0
def ck(p):
 global ASSERTS
 ASSERTS+=1
 assert p
def add(*xs): return sum((x[0] for x in xs),F()),sum((x[1] for x in xs),F())
def sc(x,c): return (x[0]*c,x[1]*c) if c>=0 else (x[1]*c,x[0]*c)
def sub(x,y):return add(x,sc(y,-1))
def pos(x):return max(F(),x[0]),max(F(),x[1])
def av(x,y):return sc(add(x,y),F(1,2))
def exact(x):return F(x),F(x)
def rounded(lo,hi):return F((lo*SCALE).__floor__(),SCALE),F((hi*SCALE).__ceil__(),SCALE)
@lru_cache(20000)
def lnunit(q):
 ck(1<=q<=2)
 z=(q-1)/(q+1); z2=z*z; p=z; s=F()
 for j in range(32):s+=p/F(2*j+1);p*=z2
 lo=2*s;return rounded(lo,lo+2*p/(65*(1-z2)))
LN2=lnunit(F(2))
@lru_cache(20000)
def logq(q):
 ck(q>0)
 e=q.numerator.bit_length()-q.denominator.bit_length()
 q=q/(1<<e) if e>=0 else q*(1<<(-e))
 if q<1:q*=2;e-=1
 if q>=2:q/=2;e+=1
 lo,hi=lnunit(q)
 return rounded(e+lo/LN2[1],e+hi/LN2[0])
def ent(p):return add(*[sc(logq(q),-q) for q in p if q])
def binary(d):return ent((d,1-d))
def child(t,i,b):
 return tuple(t[(s&((1<<i)-1))|((s>>i)<<(i+1))|(b<<i)] for s in range(len(t)//2))
@lru_cache(12000)
def stats(t):
 n=len(t).bit_length()-1;a=list(t);step=1
 while step<len(a):
  for j in range(0,len(a),2*step):
   for k in range(j,j+step):u,w=a[k],a[k+step];a[k],a[k+step]=u+w,u-w
  step*=2
 p=tuple(F(u*u,len(t)**2) for u in a)
 ck(sum(p)==1)
 ds=tuple(sum((q for s,q in enumerate(p) if s&(1<<i)),F()) for i in range(n))
 for i,d in enumerate(ds):ck(d==F(sum(t[s]!=t[s^(1<<i)] for s in range(len(t))),len(t)))
 H=ent(p);TC=sub(add(*[binary(d) for d in ds]),H)
 return p,ds,H,TC
def product(ds):
 out=[]
 for s in range(1<<len(ds)):
  q=F(1)
  for i,d in enumerate(ds):q*=d if s&(1<<i) else 1-d
  out.append(q)
 return out
@lru_cache(20000)
def transaction(t,i):
 p,ds,H,K=stats(t);cs=(child(t,i,0),child(t,i,1));pcs=[stats(c)[0] for c in cs]
 # The incoming reference is exactly the already booked full product.
 rem=ds[:i]+ds[i+1:];qe=product(rem);reach=[F(),F()];refonly=F()
 for s,q in enumerate(qe):
  s0=(s&((1<<i)-1))|((s>>i)<<(i+1));pe=p[s0]+p[s0|(1<<i)]
  if not pe:refonly+=q
  ks=[pcs[b][s]/(2*pe) if pe else F(1,2) for b in (0,1)]
  ck(sum(ks)==1)
  for b in (0,1):reach[b]+=q*ks[b]
 ck(sum(reach)==1 and min(reach)>0)
 O=sc(logq(4*reach[0]*reach[1]),-F(1,2))
 D=sub(add(O,av(stats(cs[0])[3],stats(cs[1])[3])),K)
 # Algebraic spectator entropy version checks the exact same signed debit.
 J=sub(ent(tuple((pcs[0][s]+pcs[1][s])/2 for s in range(len(p)//2))),av(stats(cs[0])[2],stats(cs[1])[2]))
 B=sub(H,ent(tuple((pcs[0][s]+pcs[1][s])/2 for s in range(len(p)//2))))
 gap=sub(add(*[binary(d) for j,d in enumerate(ds) if j!=i]),av(add(*[binary(d) for d in stats(cs[0])[1]]),add(*[binary(d) for d in stats(cs[1])[1]])))
 alt=sub(sub(add(O,B,J),binary(ds[i])),gap)
 ck(max(D[0],alt[0])<=min(D[1],alt[1]))
 return cs,D,O,refonly
CHOICES={}
@lru_cache(12000)
def worst(t):
 n=len(t).bit_length()-1
 if not n:return exact(0)
 best=exact(0);which=-1
 for i in range(n):
  cs,D,O,Z=transaction(t,i)
  v=add(pos(D),av(worst(cs[0]),worst(cs[1])))
  if v[1]>best[1]:which=i
  best=(max(best[0],v[0]),max(best[1],v[1]))
 CHOICES[t]=which
 return best
def enc(x):return [str(v) for v in x]
def compose(v):return tuple(-1 if not z&1 and z&2 else v[z>>3] if z&1 and z&4 else 1 for z in range(8*len(v)))
def main():
 mode=sys.argv[1];masks=(0,255,25,235) if mode=='pilot' else range(256)
 raw=SOURCE.read_bytes();source=json.loads(raw);initial={}
 for r in source['records']:
  m=r['mask'];val=tuple(F(x) for x in r['first_conversion_signed'])
  if m in initial:ck(initial[m]==val)
  initial[m]=val
 records=[];nodes=0;queries=0;refnodes=0;maxstates=0
 for m in masks:
  v=tuple(1 if m&(1<<s) else -1 for s in range(8));t=compose(v);ac=(child(t,1,0),child(t,1,1))
  S=av(*[sub(exact(4*sum(stats(c)[1],F())),stats(c)[2]) for c in ac]);ck(S[0]>0)
  tail=av(worst(ac[0]),worst(ac[1]));W=add(pos(initial[m]),tail)
  ck(sub(S,W)[0]>0)
  records.append({'mask':m,'root_signed_debit':enc(initial[m]),'original_mean_S4':enc(S),'all_policy_tail_upper_lower':enc(tail),'all_policy_total_booking':enc(W),'remaining_original_owner':enc(sub(S,W)),'one_twentieth_pass':20*W[1]<S[0],'first_worst_coordinates':[CHOICES[c] for c in ac]})
  nodes+=worst.cache_info().currsize;queries+=transaction.cache_info().currsize
  refnodes+=sum(1 for tt in list(CHOICES) for i in range(len(tt).bit_length()-1) if transaction(tt,i)[3]>0)
  maxstates=max(maxstates,stats.cache_info().currsize)
  for f in [stats,transaction,worst,logq,lnunit]:f.cache_clear()
  CHOICES.clear()
  ck(time.perf_counter()-START<CAP)
 out={'status':'PASS','mode':mode,'cores':len(records),'node_count_with_per_core_multiplicity':nodes,'query_count_with_per_core_multiplicity':queries,'reference_only_queries':refnodes,'peak_cached_stats':maxstates,'exact_assertions':ASSERTS,'seconds':time.perf_counter()-START,'source_sha256':hashlib.sha256(raw).hexdigest(),'source_path':str(SOURCE),'records':records}
 (ROOT/'out').mkdir(exist_ok=True)
 (ROOT/'out'/f'{mode.upper()}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k!='records'}))
if __name__=='__main__':main()
