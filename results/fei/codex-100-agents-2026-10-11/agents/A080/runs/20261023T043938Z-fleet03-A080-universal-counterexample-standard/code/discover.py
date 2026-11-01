"""Fixed finite Boolean family discovery; floating output is NOT proof."""
from pathlib import Path
from itertools import product, combinations
from functools import lru_cache
import math,json,time,sys
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
T=[('P',0)]+[('A',m) for m in range(6)]+[('L',m) for m in range(2,7)]
ROOT=T.index(('L',6));start=time.perf_counter()
def truth(t):
 k,m=t
 return (1,) if k=='P' else tuple(-1 if x in ({0} if k=='A' else {0,1,2}) else 1 for x in range(1<<m))
def actions(t):
 k,m=t
 if k=='P' or not m:return []
 if k=='A':return [(0,T.index(('A',m-1)),0)]
 return [(0,T.index(('A',m-2)),T.index(('A',m-1)))]+([(2,T.index(('L',m-1)),0)] if m>=3 else [])
ACT=[actions(t) for t in T]
def ell(p):return -p*math.log2(p) if p>0 else 0.
def core(t):
 tab=truth(t);n=len(tab);w=list(tab);s=1
 while s<n:
  for a in range(0,n,2*s):
   for j in range(a,a+s):u,v=w[j],w[j+s];w[j],w[j+s]=u+v,u-v
  s*=2
 sq=[(a/n)**2 for a in w];mu=w[0]/n;var=1-mu*mu
 return mu,var,sum(i.bit_count()*p for i,p in enumerate(sq)),sum(map(ell,sq))
C=[core(t) for t in T];NEG={0,1,2,4,8,16,32,6,17,40}
K=tuple(1 if (z<<2) in NEG else -1 for z in range(16))
@lru_cache(None)
def full(ts):
 cs=[C[t] for t in ts];co=list(map(float,K))
 for j,(mu,v,I,H) in enumerate(cs):
  for b in range(16):
   if b>>j&1:continue
   x,y=co[b],co[b|1<<j];co[b]=(1+mu)*x/2+(1-mu)*y/2;co[b|1<<j]=(x-y)/2
 ps=[]
 for b,c in enumerate(co):
  p=c*c
  for j in range(4):
   if b>>j&1:p*=cs[j][1]
  ps.append(p)
 assert abs(sum(ps)-1)<1e-10
 qs=[sum(p for b,p in enumerate(ps) if b>>j&1)/cs[j][1] if cs[j][1] else 0. for j in range(4)]
 H=sum(map(ell,ps))+sum(q*(c[3]-ell(c[1])-ell(1-c[1])) for q,c in zip(qs,cs));I=sum(q*c[2] for q,c in zip(qs,cs))
 return H,I,4*I-H
def repl(s,j,t):return s[:j]+(t,)+s[j+1:]
@lru_cache(None)
def hull(ts,allowed):
 best=max(0.,-full(ts)[2]);winner=None
 for j in allowed:
  for coord,a,b in ACT[ts[j]]:
   z=(hull(repl(ts,j,a),allowed)[0]+hull(repl(ts,j,b),allowed)[0])/2
   if z>best:best=z;winner=(j,coord,a,b)
 return best,winner
def main():
 pilot='--pilot' in sys.argv;root=(ROOT,)*4
 if pilot:
  for a,b in product(range(12),repeat=2):full((a,b,ROOT,ROOT))
  print(json.dumps({'status':'DISCOVERY_ONLY','profiles':full.cache_info().currsize,'root_pair_hull':hull(root,(0,1))[0],'seconds':time.perf_counter()-start}));return
 for ts in product(range(12),repeat=4):full(ts)
 checks=[];best=None;bestfull=None;paths={}
 for pair in combinations(range(4),2):
  states=[tuple(t if j==pair[0] else u if j==pair[1] else ROOT for j in range(4)) for t,u in product(range(12),repeat=2)]
  states.sort(key=lambda s:sum(T[x][1] for x in s),reverse=True)
  credit={root:-full(root)[2]};parent={};route={root:[]}
  for s in states:
   if s not in credit:continue
   a=credit[s]
   if s[pair[0]]!=ROOT and s[pair[1]]!=ROOT:
    allneed=hull(s,(0,1,2,3))[0]
    fullrec={'pair':pair,'state':s,'types':[T[x] for x in s],'credit':a,'full_required':allneed,'extra':allneed-a,'path':route[s]}
    if bestfull is None or fullrec['extra']>bestfull['extra']:bestfull=fullrec
    for j in range(4):
     if j in pair:continue
     required=hull(s,(j,))[0];gap=required-a
     rec={'pair':pair,'state':s,'types':[T[x] for x in s],'third_core':j,'credit':a,'third_required':required,'extra':gap,'path':route[s]}
     checks.append(rec)
     if best is None or gap>best['extra']:best=rec
   for j in pair:
    for coord,b0,b1 in ACT[s[j]]:
     kids=[repl(s,j,b) for b in (b0,b1)];mean=sum(hull(k,pair)[0] for k in kids)/2
     for ans,kid in enumerate(kids):
      ac=hull(kid,pair)[0]+a-mean
      if ac<credit.get(kid,float('inf')):
       credit[kid]=ac;parent[kid]=(s,j,coord,ans);route[kid]=route[s]+[{'core':j,'coordinate':coord,'answer':ans,'parent':s,'child':kid}]
  paths[str(pair)]={'reachable_states':len(credit),'root_R':hull(root,pair)[0]}
 assert time.perf_counter()-start<55
 out={'status':'FLOAT_DISCOVERY_NOT_PROOF','full_profiles':full.cache_info().currsize,'admission_cases':len(checks),'largest_extra':best,'largest_full_extra':bestfull,'pair_summary':paths,'full_root_hull':hull(root,(0,1,2,3))[0],'original_credit':-full(root)[2],'seconds':time.perf_counter()-start}
 assert time.perf_counter()-start<55
 (R/'out/DISCOVERY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
