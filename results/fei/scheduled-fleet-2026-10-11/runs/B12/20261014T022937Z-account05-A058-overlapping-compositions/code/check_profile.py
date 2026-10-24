import sys
sys.dont_write_bytecode=True
import arithmetic as a
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import time,json
ROOT=Path(__file__).resolve().parents[1];checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
@lru_cache(None)
def node(g,h,kinds,L):
 f=a.wrapper(g,h);ag,ah=a.fft(g),a.fft(h);cs=a.rows(kinds);R=a.potential(g,h,kinds);K=4*L+3
 ck(sum((abs(ag[c]) for c in cs),Q(0))<=L);ck(sum((abs(ah[c]) for c in cs),Q(0))<=L)
 ck(a.ent(f)==a.add(a.scale(a.add(a.ent(g),a.ent(h)),Q(1,2)),R))
 data=Q(0)
 for i,k in enumerate(kinds):
  ig,ih=a.inf(g,i),a.inf(h,i);inf=a.inf(f,i+1);data+=inf
  ck(inf==(ig+ih)/2)
  direct=a.add(a.erase(f,i+1),a.scale(a.add(a.erase(g,i),a.erase(h,i)),Q(-1,2)))
  if k=='S':
   formula=a.add(*(a.add(a.scale(a.add(a.Phi((ag[c]+ah[c])**2,(ag[c|1<<i]+ah[c|1<<i])**2),a.Phi((ag[c]-ah[c])**2,(ag[c|1<<i]-ah[c|1<<i])**2)),Q(1,4)),a.scale(a.add(a.Phi(ag[c]**2,ag[c|1<<i]**2),a.Phi(ah[c]**2,ah[c|1<<i]**2)),Q(-1,2))) for c in cs if not c&1<<i))
  else:
   left,right=(ag,ah) if k=='X' else (ah,ag)
   formula=a.add(*(a.shift(left[c],left[c|1<<i],right[c]) for c in cs))
  ck(direct==formula);ck(a.absle(direct,(4 if k=='S' else 2)*L*inf));ck(a.absle(direct,1))
  children=[]
  for b in (0,1):
   gg,hh=a.restrict(g,i,b),a.restrict(h,i,b);kk=kinds[:i]+kinds[i+1:]
   children.append(a.potential(gg,hh,kk))
  delta=a.add(R,a.scale(a.add(*children),Q(-1,2)))
  ck(a.absle(delta,K*inf))
 ck(not R or a.bounds(R)[0]>=0);ck(a.absle(R,K*data))
 if not kinds:ck(not R)
def save(mode,roots,visits,start):
 out={'mode':mode,'roots':roots,'node_visits':visits,'distinct_nodes':node.cache_info().currsize,'exact_assertions':checks,'seconds':time.perf_counter()-start,'failures':0,'arithmetic':'Fraction, exact prime-log expressions and outward rational atanh-series enclosures'}
 (ROOT/'out'/('check_'+mode+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
def two(mode):
 start=time.perf_counter();roots=visits=0;limit=16 if mode.endswith('pilot') else 256;kinds=('S','S','X','Y')
 for gc,hc in product(range(16),repeat=2):
  if roots>=limit:break
  g=tuple(1 if t&4 or gc&(1<<(t&3)) else -1 for t in range(16))
  h=tuple(-1 if t&8 else (1 if hc&(1<<(t&3)) else -1) for t in range(16))
  for assignments in product((-1,0,1),repeat=4):
   gg,hh,kk=g,h,kinds
   for i in range(3,-1,-1):
    if assignments[i]>=0:
     gg,hh=a.restrict(gg,i,assignments[i]),a.restrict(hh,i,assignments[i]);kk=kk[:i]+kk[i+1:]
   node(gg,hh,kk,2);visits+=1
  roots+=1
 save(mode,roots,visits,start)
def rare(mode):
 start=time.perf_counter();roots=visits=0;limit=16 if mode.endswith('pilot') else 256;kinds=('S',)*4+('X','Y')
 menu=[(15,v) for v in (0,1,5,15)]+[(7,v) for v in (0,3)]+[(3,v) for v in (0,3)]
 for (gm,gv),(hm,hv),gs,hs in product(menu,menu,(-1,1),(-1,1)):
  if roots>=limit:break
  g=tuple(gs*(-1 if not t&16 and t&gm==gv else 1) for t in range(64))
  h=tuple(hs*(-1 if not t&32 and t&hm==hv else 1) for t in range(64))
  node(g,h,kinds,3);visits+=1
  for i in range(6):
   for b in (0,1):
    node(a.restrict(g,i,b),a.restrict(h,i,b),kinds[:i]+kinds[i+1:],3);visits+=1
  roots+=1
 save(mode,roots,visits,start)
if __name__=='__main__':
 mode=sys.argv[1]
 (two if mode.startswith('two') else rare)(mode)
