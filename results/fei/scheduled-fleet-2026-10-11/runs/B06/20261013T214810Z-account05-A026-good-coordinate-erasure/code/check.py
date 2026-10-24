import sys,json,time,itertools
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parents[0]/'20261011T232716Z-account05-A026-good-coordinate-erasure'/'code'
sys.path.insert(0,str(OLD))
import transitive as b
import transitive_v2 as v
b.logint=v.logint;b.LN2=v.LN2

def erased(W,i):
 N=len(W);e={}
 for t in range(N):
  if not t&(1<<i):b.phi(e,F(W[t]**2,N*N),F(W[t|(1<<i)]**2,N*N))
 return e

def table(mask,states,override=None):
 sizes=[3 if s==0 else 2 for s in states]
 offsets=[];n=1
 for size in sizes:offsets.append(n);n+=size
 a=[]
 for x in range(1<<n):
  key=x&1
  for j,(s,size,o) in enumerate(zip(states,sizes,offsets)):
   signs=[1 if x&(1<<(o+t)) else -1 for t in range(size)]
   if s:signs=[s]+signs
   z=1 if sum(signs)>0 else -1
   if override and override[0]==j:z=override[1]
   if z==1:key|=1<<(j+1)
  a.append(1 if mask&(1<<key) else -1)
 return a,offsets,sizes

def rest(mask,states,j):
 other=states[:j]+states[j+1:]
 n=1+sum(3 if s==0 else 2 for s in other);ap=[];am=[]
 for x in range(1<<n):
  key=x&1;o=1
  for h,s in enumerate(states):
   if h==j:continue
   size=3 if s==0 else 2
   signs=[1 if x&(1<<(o+t)) else -1 for t in range(size)];o+=size
   if s:signs=[s]+signs
   if sum(signs)>0:key|=1<<(h+1)
  ap.append(1 if mask&(1<<(key|(1<<(j+1)))) else -1)
  am.append(1 if mask&(1<<key) else -1)
 return [(u+w)//2 for u,w in zip(ap,am)],[(u-w)//2 for u,w in zip(ap,am)]

def run(m,limit):
 start=time.perf_counter();cases=checks=relevant=0;min_margin=None
 path=ROOT/'out'/('pilot_rows.jsonl' if m==1 else 'main_rows.jsonl')
 assert not path.exists(),'immutable output exists'
 with path.open('w',encoding='utf-8') as out:
  for mask in range(1<<(1<<(m+1))):
   for states in itertools.product((0,1,-1),repeat=m):
    truth,offsets,sizes=table(mask,states);W=b.walsh(truth);N=len(truth)
    assert sum(w*w for w in W)==N*N
    for j,s in enumerate(states):
     A,D=rest(mask,states,j);NR=len(A);delta=F(sum(d*d for d in D),NR)
     AW,DW=b.walsh(A),b.walsh(D);pred={}
     for a,d in zip(AW,DW):b.phi(pred,F((2*a+s*d)**2,4*NR*NR),F(d*d,4*NR*NR))
     if s:b.addlog(pred,2,delta/2)
     # Independent product-bias integration of the outer edge event.
     weighted=F(0)
     for key in range(1<<(m+1)):
      if key&(1<<(j+1)):continue
      mass=F(1,2)
      for h,sh in enumerate(states):
       if h!=j:mass*=F(1,2)+(F(sh,4) if key&(1<<(h+1)) else -F(sh,4))
      if bool(mask&(1<<key))!=bool(mask&(1<<(key|(1<<(j+1))))):weighted+=mass
     assert weighted==delta
     for i in range(offsets[j],offsets[j]+sizes[j]):
      actual=erased(W,i);assert actual==pred
      physical=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(N)),N)
      spectral=F(sum(W[t]**2 for t in range(N) if t&(1<<i)),N*N)
      assert physical==spectral==delta/2;checks+=1
     if delta and not s:
      rhs={};b.lograt(rhs,4/delta,delta/4)
      lo,_=b.interval(rhs);_,hi=b.interval(pred)
      margin=lo+delta/(4*v.LN2[1])-hi
      assert margin>0;relevant+=1
      min_margin=margin if min_margin is None else min(min_margin,margin)
    cases+=1
    out.write(json.dumps({'mask':mask,'states':states,'status':'PASS'})+'\n');out.flush()
    if time.perf_counter()-start>limit:raise RuntimeError('frozen runtime exceeded')
 summary={'helper_version':'A026-biased-history-v1','cases':cases,'coordinate_identity_checks':checks,'relevant_intact_scalar_checks':relevant,'minimum_scalar_margin':str(min_margin),'elapsed_seconds':time.perf_counter()-start,'status':'PASS','arithmetic':'integer Walsh, Fraction influences, canonical exact prime-log equality; 48-term atanh bounds rounded outward at 2^-140'}
 (ROOT/'out'/('pilot_summary.json' if m==1 else 'main_summary.json')).write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(summary,indent=2))

if __name__=='__main__':
 (ROOT/'out').mkdir(exist_ok=True)
 run(int(sys.argv[1]),60 if sys.argv[1]=='1' else 120)
