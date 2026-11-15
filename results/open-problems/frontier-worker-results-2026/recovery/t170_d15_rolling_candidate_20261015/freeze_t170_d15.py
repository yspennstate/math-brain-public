from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
import json,hashlib,subprocess
H=Path(__file__).resolve().parent;B=Path('~/brain-repo')
proof=H/'T170-LEAD-ROLLING-D15-001_v1.md';claim='T170-LEAD-ROLLING-D15-001';digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert not (H/'T170_D15_SUBMISSION.json').exists(),'Frozen already'
check=json.loads((H/'T170_ROLLING_INDEPENDENT_BIAS_RECEIPT.json').read_bytes());assert check['status'].startswith('PASS')
r=json.loads((H/'T170_EMBEDDED_d15_C512_RECEIPT.json').read_bytes());alpha=F(r['axis_certificate']);floor=F(88164156999,10**12);assert floor>alpha
names=['T170-LEAD-ROLLING-D15-001_v1.md','T170_ROLLING_WINDOW_ROUTE.md','T170_DISCRETE_HORIZONTAL_BOUND.md','T170_DISCRETE_RATE_RECEIPT.json','prepare_t170_discrete_screen.py','pilot_t170_rolling_embedded.py','verify_t170_rolling_bias.py','T170_ROLLING_INDEPENDENT_BIAS_RECEIPT.json','check_t170_rolling_controls.py','T170_ROLLING_CONTROL_RECEIPT.json','run_polite.py']
for cap in [2,128,512]:names.extend([f'T170_EMBEDDED_d15_C{cap}_BIAS.json',f'T170_EMBEDDED_d15_C{cap}_RECEIPT.json'])
old=json.loads((H/'T170_D16_SUBMISSION.json').read_bytes())
receipt={'at':datetime.now().astimezone().isoformat(),'claim':claim,'version':1,'proof_sha256':digest(proof),'status':'Candidate NOT ADMITTED; full physical argument new and two distinct-account audits required','files':{n:digest(H/n) for n in names},'dependencies':old['dependencies'],'axis':str(alpha),'diagonal_floor_down':str(floor),'gap':str(floor-alpha)}
(H/'T170_D15_SUBMISSION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
with (H/'CLAIMS.jsonl').open('ab') as f:f.write((json.dumps({'at':receipt['at'],'claim':claim,'version':1,'sha256':receipt['proof_sha256'],'status':'candidate','submission':'T170_D15_SUBMISSION.json'})+'\n').encode())
M=B/'12_cognitive_architecture/agent_mesh/agent_mesh.py';requests=[]
for peer in ['codex-w683','codex-term-agent']:
 body=f'New frozen D15 rolling-window candidate {proof}, SHA {receipt["proof_sha256"]}. Submission {H/"T170_D15_SUBMISSION.json"}. AFTER current D16 priority, request full independent exact-content review on your actual account, start identity before semantic read/end identity. New physical comparison needs fresh audit: adaptive Poisson thinning, canonical aligned-singleton regeneration incl self-front reward, reflection/shape theorem/Dynkin; not inherited Dhar method. Own exact finite262144bias inequalities pass independently, axis{alpha}<floor{floor}, margin~.000344549. Review standalone source + boundary split certificate + diagonal premise, do not infer from my finite PASS. No newagents. No admission until two distinct actual accounts. Please flag any physical flaw first.'
 p=subprocess.run(['C:/Python314/python.exe',str(M),'send','--agent','codex-term-362ebe34','--to',peer,'--topic','T170-D15-new-rolling-method-audit','--body',body,'--require-ack'],capture_output=True,text=True,encoding='utf-8');assert p.returncode==0,p.stderr
 requests.append({'peer':peer,'response':p.stdout})
(H/'T170_D15_REVIEW_REQUESTS.json').write_text(json.dumps(requests,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:receipt[k] for k in ['claim','proof_sha256','axis','gap']}))
