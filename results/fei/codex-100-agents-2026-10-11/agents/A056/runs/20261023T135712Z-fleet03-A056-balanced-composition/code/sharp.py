from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
t=time.perf_counter()
cases=[]
for d in range(2,65):
 a=(d-1)**5;b=4**d
 assert a<=b
 assert (a==b)==(d==5)
 cases.append({'d':d,'lhs':str(a),'rhs':str(b),'equality':a==b})
assert 5**5<4**6
out={'status':'PASS','cases':cases,'constant':'2/5','sharp_actual_Boolean_witness':'parity_5; each queried influence1 and rho=log2(4)/5=2/5','all_d_proof':'Check d2..5 explicitly. For d>=5, (d/(d-1))^5<4, since 5^5<4^6; hence (d-1)^5<=4^d inductively.','runtime_seconds':time.perf_counter()-t,'full_FEI':'OPEN'}
(R/'out'/'SHARP_RESELECTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2))
