"""Fresh price-six boundary verification, no search or parameter escalation."""
from pathlib import Path
import sys,json,time
sys.dont_write_bytecode=True
import kernel as K
from check import raw_profile
from fractions import Fraction as F
start=time.monotonic();rows=[]
seed=bytes(int(x.bit_count()>=2) for x in range(8))
for name,truth in [('majority3',seed)]+[(f'profile{k}',raw_profile(k)) for k in [2,4,6]]:
 n=len(truth).bit_length()-1
 result=K.tree(truth,list(range(n)),'control-first',['data']*n,prices=[F(6)])
 K.check(result['Q_scaled']==((0,0),))
 rows.append({'name':name,**result})
K.check(F(303,128)+F(15,32)-3==-F(21,128))
K.check(F(2)+F(11,32)+F(15,32)==F(45,16)<3)
K.check(81**2<2*64**2 and 3**5<2**8 and 5**3<2**7)
r=Path(__file__).resolve().parents[1]
out={'price':'6','rows':rows,'assertions':K.ASSERTIONS,'seconds':time.monotonic()-start}
(r/'out/BOUNDARY.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'boundary_assertions':K.ASSERTIONS,'seconds':out['seconds']}))
