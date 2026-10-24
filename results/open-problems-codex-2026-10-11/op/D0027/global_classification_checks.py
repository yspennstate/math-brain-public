from pathlib import Path
from itertools import product
from fractions import Fraction as F
import json,time
from tensor_checks import matrices,cycle
start=time.monotonic();grid=sorted(set([F(-2),F(-1),F(-4,5),F(-1,2),F(-1,5),F(0),F(1,5),F(1,2),F(4,5),F(1),F(3,2),F(2)]));count=0;positive=[];complete=True
for q,kind,a,b in product([F(1,5),F(1,2),F(4,5)],['C','V'],grid,grid):
 if time.monotonic()-start>120:complete=False;break
 z=matrices(q,a,b,kind)
 if z is None:continue
 states,G=cycle(z[2]);ok=all(G[i][j]>=0 for i in range(32) for j in range(32) if i!=j)
 expected=(kind=='C' and (a,b) in [(F(1),F(0)),(F(0),F(1))]) or (kind=='V' and (a,b) in [(1-q,1-q),(-(1-q),q)])
 assert ok==expected,(q,kind,a,b)
 count+=1
 if ok:positive.append([str(q),kind,str(a),str(b)])
result={'status':'PASS','complete_grid':complete,'global_cycle_size':5,'cases':count,'positive_cases':positive,'elapsed_seconds':time.monotonic()-start}
Path('global_classification_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(result,flush=True)
