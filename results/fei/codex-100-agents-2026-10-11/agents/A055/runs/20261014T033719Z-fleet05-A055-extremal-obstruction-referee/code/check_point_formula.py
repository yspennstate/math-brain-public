from pathlib import Path
from fractions import Fraction as Q
import json,time
r=Path(__file__).resolve().parents[1];start=time.perf_counter();records=[]
for n in range(2,9):
 name=f'full_n{n}_mask1.json' if n<=3 else f'full_point_defect{n}.json'
 x=json.loads((r/'out'/name).read_text());p=Q(1,1<<n)
 formula=16*Q(n*(n-1),2)*p*p/((1-4*p+16*p*p)*(1-4*p+8*p*p))
 assert Q(x['O_total'])==0 and Q(x['T'])==formula
 records.append({'n':n,'T':str(formula),'orientation':'0'})
out={'status':'PASS','assertions':7,'runtime_seconds':time.perf_counter()-start,'records':records}
(r/'out/POINT_FORMULA_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
