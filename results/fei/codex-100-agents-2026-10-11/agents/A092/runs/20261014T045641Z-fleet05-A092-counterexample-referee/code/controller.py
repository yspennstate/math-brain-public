import check as C
from fractions import Fraction as F
import time,json
START=time.perf_counter();t=tuple((-1 if x&3==3 else 1)*(-1 if x>>2==7 else 1) for x in range(32))
pd=C.spectrum((1,1,1,1,1,1,1,-1),(2,3,4))
for kind,refc in [('flat',{s:F(1,4) for s in range(4)}),('nonflat',{0:F(1,2),1:F(1,4),2:F(1,8),3:F(1,8)})]:
 q={s|z:p*v for s,p in refc.items() for z,v in pd.items()}
 r=C.audit(t,0,24,'CONTROLLER_'+kind,q,matched_fresh=True)
 C.ck(not r['entropy_drift'] and not r['conditional_inherited_KL'] and not r['conditional_fresh_KL'] and not r['conditional_reset'])
 C.save(r['name']+'.json',r)
C.ck(time.perf_counter()-START<60)
out={'status':'PASS','cases':2,'primary_assertions':C.COUNT,'entropy_helper_assertions':C.E.ASSERTIONS,'runtime_seconds':time.perf_counter()-START}
C.save('CONTROLLER_RESULT.json',out);print(json.dumps(out))
