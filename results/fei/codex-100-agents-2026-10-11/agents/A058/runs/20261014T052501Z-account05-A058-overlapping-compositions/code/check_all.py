import sys
sys.dont_write_bytecode=True
import check as c
import arithmetic as a
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
@lru_cache(None)
def node(g,h,kinds):
 f=a.wrapper(g,h);ag,ah=a.fft(g),a.fft(h);cs=a.rows(kinds)
 iz=Q(sum(x!=y for x,y in zip(g,h)),len(g));c.ck(a.inf(f,0)==iz);c.ck(a.absle(a.erase(f,0),20*iz))
 for i,k in enumerate(kinds):
  jg,jh=a.inf(g,i),a.inf(h,i);jf=a.inf(f,i+1);c.ck(jf==(jg+jh)/2)
  D=a.add(a.erase(f,i+1),a.scale(a.add(a.erase(g,i),a.erase(h,i)),Q(-1,2)))
  c.ck(a.absle(D,(6 if k=='S' else 5)*jf));c.ck(a.absle(a.erase(f,i+1),(14 if k=='S' else 9)*jf))
  c.ck(a.absle(a.erase(g,i),(8 if k=='S' else 4)*jg));c.ck(a.absle(a.erase(h,i),(8 if k=='S' else 4)*jh))
  if k!='S':
   coeff=ag if k=='X' else ah;j=jg if k=='X' else jh
   # Remaining private controls each have p=1/2 in this frozen one-bit domain.
   J=sum((coeff[t|1<<i]**2 for t in cs),Q(0));c.ck(J==j)
   own=g if k=='X' else h
   m=Q(sum(a.restrict(own,i,0)),len(own)//2)
   c.ck(j==Q(1,2)*(1-m));c.ck(j==0 or j>=Q(1,4))
   upper=a.scale(a.Phi(1,J),Q(1,2))
   for sign in (-1,1):
    gap=a.add(upper,a.scale(D,sign));c.ck(not gap or a.bounds(gap)[0]>=0)
def main():
 start=time.perf_counter();limit=16 if sys.argv[1]=='pilot' else 256;roots=visits=0
 for uc,vc in product(range(16),repeat=2):
  if roots>=limit:break
  g,h=c.rootg(uc),c.rooth(vc);kinds=('S','S','X','Y')
  for assignment in product((-1,0,1),repeat=4):
   gg,hh,kk=c.apply(g,h,kinds,assignment);node(gg,hh,kk);visits+=1
  roots+=1
 out={'mode':sys.argv[1],'roots':roots,'state_visits':visits,'distinct_states':node.cache_info().currsize,'exact_assertions':c.count,'seconds':time.perf_counter()-start,'failures':0,'scope':'all partial data restrictions, selector at any such node and each post-selector branch; all-order local prices'}
 (R/'out'/('all_'+sys.argv[1]+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
