from pathlib import Path
from fractions import Fraction as F
import json,time
import direct as D
start=time.perf_counter()
t=tuple(-1 if (((s&1)+((s>>2)&1))&1)*((s>>1)&1) else 1 for s in range(16))
Q=tuple(F(s+1,136) for s in range(16));ts,Qs,r,E,O,ks=D.transport(t,Q,0)
D.ck(r==[F(1,2)]*2,'actual u prediction');records=[]
for b in [0,1]:
 cs,Rs,rv,ee,oo,kcs=D.transport(ts[b],Qs[b],0)
 D.ck(rv==[F(15,34),F(19,34)],'exact after-u nonzero pivot prediction')
 D.ck(oo==D.add((F(-1,2),D.A.log(F(285,289)))),'exact pivot outcome KL')
 D.ck(D.A.interval(oo)[0]>0,'strict positive after-u outcome KL')
 records.append({'u':b,'r_v':[str(x) for x in rv],'O_v':D.A.value(oo),'E_v':D.A.value(ee)})
out={'status':'PASS','overlapping_extracted_assertions':D.N,'seconds':time.perf_counter()-start,'primary_total_includes_this':False,'records':records}
D.ck(out['seconds']<10,'frozen extraction runtime')
(Path(__file__).resolve().parents[1]/'out/U_WITNESS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(out))
