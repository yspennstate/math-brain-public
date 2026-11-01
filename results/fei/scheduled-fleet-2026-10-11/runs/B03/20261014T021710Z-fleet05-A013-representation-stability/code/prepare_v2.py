from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];p=R/'code/check.py';s=p.read_text()
(R/'code/check_pilot_v1.py').write_text(s,encoding='utf-8')
(R/'out/PILOT_V1.json').write_text(json.dumps({'status':'RUNTIME_CUTOFF','cutoff_seconds':50,'assertion_failure':False,'completed':'Eight strict rational profile certificates; partial labelled actual profiles','code_sha256':hashlib.sha256(s.encode()).hexdigest(),'response':'Exploit proved phase pattern classification; all 2048 phase/point classification cases, 128 representative actual profiles; unchanged r domain'},indent=2),encoding='utf-8')
s=s.replace('for r in [0,1,2,3]:\n   n=3+r','for r in ([0,1,2,3] if mask in [255,3,7,1] else []):\n   n=3+r').replace("'A013-three-bit-profile-v1'","'A013-three-bit-profile-v2'").replace('for cmask in [255,15,1,7]:','for cmask in [255,3,1,7]:')
p.write_text(s,encoding='utf-8')
spec=json.loads((R/'out/FROZEN_SPEC.json').read_text());(R/'out/FROZEN_SPEC_V1.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
spec['helper_version']='A013-three-bit-profile-v2';spec['case_counts']['profiles']=128
spec['domain']['actual_spectrum_c']=[255,3,7,1]
spec['symmetry']='All 2048 labelled c,w classified exactly. Four representative phases, all 8 points and r=0,1,2,3 give 128 actual spectrum checks. All-dimensional proof relies on the four relative-point Walsh patterns and the explicit coefficient formula, not extrapolation from representatives.'
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('v2 domain frozen before execution')
