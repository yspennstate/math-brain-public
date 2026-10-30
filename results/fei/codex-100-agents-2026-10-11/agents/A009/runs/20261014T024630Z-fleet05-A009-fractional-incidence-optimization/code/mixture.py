import json, math, time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0
def ck(x):
 global checks
 assert x; checks+=1
case=next(c for c in json.loads((ROOT/'out/CHECK.json').read_text())['certificates'] if c['name']=='star5')
c=list(map(F,case['c'])); v=F(case['v']); C=sum(c); lam=[F(3,4),F(1,12),F(1,12),F(1,12)]; edges=case['edges']; y=[F(1,10)]*5
D=math.prod(1+x/4 for x in lam)-1
root={mask:math.prod(lam[e]/4 for e in range(4) if mask>>e&1)/D for mask in range(1,16)}
ck(sum(root.values())==1)
r=[sum(p for mask,p in root.items() if mask>>e&1) for e in range(4)]
original_b=[c[e]-v*r[e] for e in range(4)]; ck(any(x<0 for x in original_b))
threshold=max([(v*r[e]-c[e])/(v*(r[e]-c[e]/C)) for e in range(4) if v*r[e]>c[e]]+[F(0)])
delta=(1+threshold)/2; ck(0<delta<1)
sigma={1<<e:c[e]/C for e in range(4)}; nu={mask:(1-delta)*p+delta*sigma.get(mask,F(0)) for mask,p in root.items()}
ck(sum(nu.values())==1); ck(all(p>0 for p in nu.values()))
rn=[sum(p for mask,p in nu.items() if mask>>e&1) for e in range(4)]; b=[c[e]-v*rn[e] for e in range(4)]; ck(all(x>0 for x in b))
chi_direct=sum((nu[mask]-p)**2/p for mask,p in root.items())
chi_closed=delta**2*(sum((c[e]/C)**2*4*D/lam[e] for e in range(4))-1); ck(chi_direct==chi_closed)
slack=F(0)
for j in range(5):
 row=sum(lam[e] for e,E in enumerate(edges) if j in E); ck(row<=1); slack+=y[j]*(1-row)
phi=F(0)
for e,(u,w) in enumerate(edges):
 z=lam[e]*(y[u]+y[w]); ck(z>0); phi+=(b[e]-z)**2/z
gap=2*(v*chi_direct+slack+phi); ck(gap>=0)
result={'actual_case':'star5','checks':checks,'all_passed':True,'elapsed_seconds':time.perf_counter()-start,'lambda':[str(x) for x in lam],'original_b':[str(x) for x in original_b],'threshold_delta':str(threshold),'chosen_delta':str(delta),'repaired_b':[str(x) for x in b],'root_chi_square_of_mixture':str(chi_direct),'bit_gap_upper':str(gap),'small_gap_or_optimum_asserted':False}
(ROOT/'out/MIXTURE_CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
