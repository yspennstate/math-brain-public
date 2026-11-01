import sys
sys.dont_write_bytecode=True
import check as c
import arithmetic as a
from itertools import product,permutations
from fractions import Fraction as Q
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
def main():
 start=time.perf_counter();mono=(0,1,2,4,3,5,6)
 phases=sorted(sum((1<<x for x in range(8) if sum(bool(code&1<<j) and x&m==m for j,m in enumerate(mono))%2),0) for code in range(128))
 c.ck(len(set(phases))==128)
 maps=[]
 for perm,trans in product(permutations(range(3)),range(8)):
  maps.append(tuple(sum(((x>>perm[i])&1)<<i for i in range(3))^trans for x in range(8)))
 transformed={u:[sum(((u>>m[x])&1)<<x for x in range(8)) for m in maps] for u in phases}
 c.ck(all(v in phases for values in transformed.values() for v in values))
 groups={}
 for u,v in product(phases,repeat=2):
  canonical=min(tuple(sorted((tu,tv))) for tu,tv in zip(transformed[u],transformed[v]))
  groups[canonical]=groups.get(canonical,0)+1
 c.ck(sum(groups.values())==16384)
 c.ck(all(96%n==0 for n in groups.values()))
 limit=16 if sys.argv[1]=='pilot' else len(groups)
 for u,v in sorted(groups)[:limit]:
  kinds=('S','S','S','X','Y')
  g=tuple((1 if u&1<<(x&7) else -1) if not x&8 else 1 for x in range(32))
  h=tuple((1 if v&1<<(x&7) else -1) if not x&16 else 1 for x in range(32))
  c.state(g,h,kinds,'shared')
  # Every original quadratic phase coordinate has gap0 or>=1/2.
  for mask in (u,v):
   phase=tuple(1 if mask&1<<x else -1 for x in range(8))
   for i in range(3):c.ck(a.inf(phase,i)==0 or a.inf(phase,i)>=Q(1,2))
 out={'mode':sys.argv[1],'labelled_pairs':16384,'total_orbits':len(groups),'checked_representatives':limit,'exact_assertions':c.count,'seconds':time.perf_counter()-start,'failures':0,'orbit_sizes':{str(k):sum(v==k for v in groups.values()) for k in sorted(set(groups.values()))},'symmetry':'physical shared translations/permutations and branch/controller exchange with selector flip'}
 (R/'out'/('orbits_'+sys.argv[1]+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
 if sys.argv[1]=='full':(R/'out/orbit_coverage.json').write_text(json.dumps([{'u':u,'v':v,'labelled_orbit_size':n} for (u,v),n in sorted(groups.items())],indent=2),encoding='utf-8')
 print(json.dumps(out))
if __name__=='__main__':main()
