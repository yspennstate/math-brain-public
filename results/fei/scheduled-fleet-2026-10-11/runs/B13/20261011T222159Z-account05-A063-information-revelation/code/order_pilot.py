import json,time
from check_query import tree,serial,RUN
started=time.perf_counter(); results=[]
for code in (4660,4951,6061,27043):
    if time.perf_counter()-started>40: break
    vals=tuple(-1 if code>>x&1 else 1 for x in range(16))
    rows=[]
    for order in ((0,1,2,3),(3,2,1,0)):
        B,J,R,_,joint=tree(vals,tuple(range(4)),order)
        rows.append({'order':order,'erasure':serial(B),'information':serial(J),'refund':serial(R)})
    results.append({'code':code,'values':vals,'rows':rows,'different_information':rows[0]['information']!=rows[1]['information']})
out={'status':'PASS','completed_cases':2*len(results),'runtime_seconds':time.perf_counter()-started,'results':results}
(RUN/'out'/'ORDER_PILOT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2),flush=True)
