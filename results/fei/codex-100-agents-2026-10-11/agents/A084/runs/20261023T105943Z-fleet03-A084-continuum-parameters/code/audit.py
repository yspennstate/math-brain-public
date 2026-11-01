"""Direct physical restriction/mask audit for a small guard/parity account."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,sys
import seed_engine as e
RUN=Path(__file__).resolve().parents[1]
C=0
def ck(v):
 global C
 assert v
 C+=1
def delete(mask,i):return (mask&((1<<i)-1))|((mask>>(i+1))<<i)
@lru_cache(None)
def kids(t,i):return tuple(tuple(t[x] for x in range(len(t)) if x>>i&1==b) for b in range(2))
@lru_cache(None)
def stats(t):
 n=(len(t)-1).bit_length();N=len(t)
 W=[sum(y*(-1 if (b&x).bit_count()%2 else 1) for x,y in enumerate(t)) for b in range(N)]
 ck(sum(z*z for z in W)==N*N)
 for x,y in enumerate(t):ck(sum(w*(-1 if (b&x).bit_count()%2 else 1) for b,w in enumerate(W))==N*y)
 H={};I=F(0)
 for b,w in enumerate(W):
  p=F(w*w,N*N);I+=p*b.bit_count()
  if w:H=e.add(H,e.mul(e.lp(F(abs(w),N)),-2*p))
 edges=sum(F(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N) for i in range(n))
 ck(edges==I)
 return H,I
def main():
 start=time.perf_counter();d=int(sys.argv[1]) if len(sys.argv)>1 else 1;ck(d in [0,1,2])
 n=d+4
 t=tuple(((-1 if (x&3)==0 else 1) if ((x>>2)&((1<<d)-1))==0 else 1)*(-1 if (x>>(d+2)).bit_count()%2 else 1) for x in range(1<<n))
 results=[]
 for K in [F(1),F(3,2)]:
  @lru_cache(None)
  def deficit(t):
   H,I=stats(t);return e.pos(e.add(H,{2:-K*I}))
  @lru_cache(None)
  def hull(t,M):
   best=deficit(t)
   for i in range((len(t)-1).bit_length()):
    if not(M>>i&1):continue
    v=e.mean([hull(c,delete(M,i)) for c in kids(t,i)])
    if e.cmp(v,best)>0:best=v
   return best
  @lru_cache(None)
  def capital(t,M):
   best=deficit(t);nfree=(len(t)-1).bit_length()
   for i in range(nfree):
    if not(M>>i&1):
     v=capital(t,M|1<<i)
     if e.cmp(v,best)>0:best=v
    else:
     children=kids(t,i);mask=delete(M,i);rs=[hull(c,mask) for c in children];r=e.mean(rs)
     for c,R in zip(children,rs):
      v=e.add(capital(c,mask),e.neg(R),r)
      if e.cmp(v,best)>0:best=v
   return best
  R=hull(t,(1<<n)-1);T=capital(t,0);ck(e.cmp(T,R)>=0)
  a={2:2-K};ck(e.cmp(T,a)>=0)
  # Original guard-only allocation leaves every actual selector-zero prefix unchanged.
  v=t;mask=((1<<d)-1)<<2
  for left in range(d,0,-1):
   ck(not hull(v,mask))
   c0,c1=kids(v,2);cm=delete(mask,2)
   ck(not hull(c0,cm) and not hull(c1,cm))
   ck(stats(c1)[0]=={})
   v,mask=c0,cm
  ck(not hull(v,0))
  # Reveal both parity coordinates: entropy seed2, influence seed1, same deficit.
  v=kids(kids(v,2)[0],2)[0];ck(stats(v)==({2:F(2)},F(1)))
  ck(deficit(v)==a)
  results.append({'d':d,'K':str(K),'full_hull':e.pack(R),'robust_capital':e.pack(T),'seed_deficit':e.pack(a),'augmented_states':capital.cache_info().currsize,'hull_states':hull.cache_info().currsize,'guard_only_credit_changes':'all exactly0'})
  ck(time.perf_counter()-start<55)
 result={'direct_physical_audit':'PASS','d':d,'bits':n,'assertions':C+e.CHECKS,'results':results,'runtime_seconds':time.perf_counter()-start,'scope':'Small independent physical controls, not a computation on the51-bit witness.'}
 (RUN/'out'/f'AUDIT_d{d}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='results'}))
if __name__=='__main__':main()
