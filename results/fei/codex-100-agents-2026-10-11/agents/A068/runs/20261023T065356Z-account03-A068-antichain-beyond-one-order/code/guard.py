from pathlib import Path
from fractions import Fraction as F
import hashlib,importlib.util,json,time
HERE=Path(__file__).resolve().parent.parent
s=importlib.util.spec_from_file_location('obstruction',HERE/'code'/'obstruction.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o)
start=time.monotonic();rows=[];checks=0
for k in range(1,9):
 L=1<<k
 truth=[1 if ((z&1)==0 or (z>>1)==0) else -1 for z in range(2*L)]
 root=[v*v for v in o.direct_walsh(truth)]
 child=[v*v for v in o.direct_walsh(truth[1::2])]
 marginal=[root[2*z]+root[2*z+1] for z in range(L)]
 calibrated=[child[0]]+[(1-child[0])*v/(1-marginal[0]) for v in marginal[1:]]
 assert calibrated==child;checks+=1
 assert sum(root)==sum(child)==sum(calibrated)==1;checks+=1
 assert all(v>0 for v in root);checks+=1
 assert time.monotonic()-start<15
 rows.append({'k':k,'actual_root_source_calibration_equals_actual_child':True})
r={'status':'PASS','cases':len(rows),'assertions':checks,'seconds':time.monotonic()-start,'rows':rows,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'out'/'guard.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in r.items() if k!='rows'}))
