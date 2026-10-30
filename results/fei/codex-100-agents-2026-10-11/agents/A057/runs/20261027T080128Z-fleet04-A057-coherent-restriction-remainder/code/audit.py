from fractions import Fraction as F
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();ncheck=0
# Independent integer triangular-wave implementation, not the subject's Fraction floor code.
def T(k,den):
 return sum((F(min((k*(1<<j))%den,den-(k*(1<<j))%den),den*(1<<j)) for j in range(4)),F(0))
mins=[None]*17
for mask in range(1<<16):
 cnt=mask.bit_count();edges=0
 for x in range(16):
  for i in range(4):
   if not (x>>i)&1 and ((mask>>x)^(mask>>(x^(1<<i))))&1:edges+=1
 b=F(edges,16)
 assert b>=T(cnt,16);ncheck+=1
 if mins[cnt] is None or b<mins[cnt]:mins[cnt]=b
for k,v in enumerate(mins):
 assert v==T(k,16);ncheck+=1
# Every vertex in the clipped affine partition lies on the16-grid:
# x,y grid; x+y=2k/16; x=y; all pairwise intersections are grid points.
raw=json.loads((R/'out/BOUNDARY_VERTICES.json').read_text(encoding='utf-8'))
actual={(F(x),F(y)):F(g) for x,y,g in raw}
assert set(actual)=={(F(i,16),F(j,16)) for i in range(17) for j in range(17)};ncheck+=1
for i in range(17):
 for j in range(17):
  gap=(T(i,16)+T(j,16)+F(abs(i-j),16))/2-T(i+j,32)
  assert gap==actual[F(i,16),F(j,16)] and gap>=0;ncheck+=1
c=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'))
p=Path(r'agents\A091\runs\20261027T054729Z-fleet04-A091-composition-referee\out\SEED_CERTIFICATE.json')
s=json.loads(p.read_text(encoding='utf-8'))['first_certified_seed'];a,b=map(F,s['H']);l,u=map(F,c['seed']['H'])
assert max(a,l)<=min(b,u);ncheck+=1
assert F(s['mean'])==F(c['seed']['mean']) and F(s['I'])==F(c['seed']['I']);ncheck+=1
assert l-F(9,2)*F(s['I'])>F(1,10);ncheck+=1
assert F(9,2)-2*F(41,20)==F(2,5)>F(1,26);ncheck+=1
out=dict(status='PASS',checks=ncheck,functions=65536,boundary_minima=[str(x) for x in mins],imported_A091_seed='HOLDS unchanged at written finite-seed scope',seconds=time.perf_counter()-start)
(R/'out/AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:out[k] for k in ['status','checks','functions','seconds']}))
