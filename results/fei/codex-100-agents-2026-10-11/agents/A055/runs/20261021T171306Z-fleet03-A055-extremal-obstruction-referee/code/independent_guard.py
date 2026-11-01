"""Direct character enumeration, no imports from the primary checkers."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0;profiles={}
for mask in range(256):
 v=[1 if mask>>x&1 else -1 for x in range(8)]
 w=[sum(v[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(8)) for s in range(8)]
 profile=tuple(sorted(q*q for q in w if q));ii=Q(sum(v[x]!=v[x^(1<<j)] for x in range(8) for j in range(3)),8)
 if profile not in profiles:profiles[profile]={'count':0,'min_I':ii,'minimizers':[]}
 p=profiles[profile];p['count']+=1
 if ii<p['min_I']:p['min_I']=ii;p['minimizers']=[]
 if ii==p['min_I']:p['minimizers'].append(mask)
 assert sum(profile)==64;checks+=1
 if mask in [127,254]:assert profile==(4,4,4,4,4,4,4,36) and ii==Q(3,4);checks+=1
 if mask==126:assert profile==(16,16,16,16) and ii==Q(3,2);checks+=1
 if mask==255:assert profile==(64,) and ii==0;checks+=1
assert set(profiles)=={(64,),(16,16,16,16),(4,4,4,4,4,4,4,36)};checks+=1
assert profiles[(64,)]['min_I']==0;checks+=1
assert profiles[(16,16,16,16)]['min_I']==1;checks+=1
assert profiles[(4,4,4,4,4,4,4,36)]['min_I']==Q(3,4);checks+=1
assert 3**9<2**20 and 3**5<2**8;checks+=2
out={'status':'PASS','tables':256,'assertions':checks,'method':'direct character sums and physical edge counts only; no primary checker imports; three exact spectral-weight profiles prove global K2 maximum','profile_certificate':[{'squared_Walsh_numerators':list(k),'count':v['count'],'min_I':str(v['min_I']),'minimizers':v['minimizers']} for k,v in profiles.items()],'elapsed_seconds':time.perf_counter()-start}
(R/'out/INDEPENDENT_GUARD.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
