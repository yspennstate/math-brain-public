from pathlib import Path
from itertools import combinations
import json,time
B=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;orbits=0;sharp=[]
def ck(b):
 global checks
 assert b
 checks+=1
 assert time.perf_counter()-start<55
for d in range(4):
 N=1<<d;bases=[]
 for v in combinations(range(1,N),d):
  span={0}
  for a in v:span|={x^a for x in tuple(span)}
  if len(span)==N:bases.append(v)
 for z in range(1<<N):
  t=[1 if (z>>x)&1 else -1 for x in range(N)]
  M=sum(a<0 for a in t)
  b=[sum(t[x]!=t[x^v] for x in range(N)) for v in range(N)]
  I=sum(b[1<<j] for j in range(d));best=I
  for v in bases:
   for c in range(N):
    total=sum(N-b[a] if (c&a).bit_count()%2 else b[a] for a in v)
    if d>=2:ck((total-I)%4==0)
    best=min(best,total);orbits+=1
  quantum=2 if d==1 else 4
  if d:ck((I-best)%quantum==0)
  if d==3 and I-best==4:sharp.append(z)
  if d>=2:
   for v in range(1,N):ck(b[v]%4==(2*M)%4 and (N-b[v])%4==(2*M)%4)
ck(bool(sharp))
# Quantitative integer conclusion, including equality at threshold.
abstract=0
for m in range(9):
 for units in range(m,12):
  for C in range(1,9):
   for cap in range(0,97):
    # Reserve lower bound C*units, with positive deficit, ceiling cap/8.
    if 8*C*units<cap:
     ck(8*C*m<cap)
     if cap<=8*C:ck(m==0)
     abstract+=1
out={'status':'PASS','checks':checks,'seconds':time.perf_counter()-start,'signs':278,'affine_basis_character_costs':orbits,'sharp_d3_tables':sharp,'abstract_cases':abstract,'scope':'independent direct input-edge/basis enumeration; no import from primary helper'}
(B/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
