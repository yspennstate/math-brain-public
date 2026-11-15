from pathlib import Path
from datetime import datetime
from fractions import Fraction as F
import hashlib,json,subprocess
H=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();proof=H/'T170-LEAD-ROLLING-D14-001_v1.md'
assert not (H/'T170_D14_SUBMISSION.json').exists(),'Already frozen'
native=json.loads((H/'T170_THREE_COMPRESSED_d14_C256_RECEIPT.json').read_bytes());ind=json.loads((H/'T170_THREE_COMPRESSED_d14_C256_PYTHON_RECEIPT.json').read_bytes());fault=json.loads((H/'T170_THREE_ACTUAL_FAULT_RECEIPT.json').read_bytes());control=json.loads((H/'T170_THREE_FRACTION_CONTROL_RECEIPT.json').read_bytes())
assert native['alpha_units']==ind['alpha_units']==native['alpha0_units']==98624416626
assert native['states']==ind['states']==256**3 and fault['actual_violation_units']>0 and control['status'].startswith('PASS')
names=['T170-LEAD-ROLLING-D14-001_v1.md','T170_ROLLING_WINDOW_ROUTE.md','T170_DISCRETE_HORIZONTAL_BOUND.md','T170_DISCRETE_RATE_RECEIPT.json','prepare_t170_discrete_screen.py','t170_three_compressed.cpp','check_three_compressed.cpp','run_three_compressed.py','verify_three_compressed_python.py','check_three_actual_fault.py','T170_THREE_ACTUAL_FAULT_RECEIPT.json','check_three_window_fraction_controls.py','T170_THREE_FRACTION_CONTROL_RECEIPT.json','T170_THREE_COMPRESSED_d14_C256_PYTHON_RECEIPT.json','T170_THREE_COMPRESSED_BUILD_RECEIPT.json','T170_THREE_CONSTRUCTIVE_CHECK_BUILD_RECEIPT.json','build_three_compressed.py','build_three_checker.py','run_polite.py']
for C in [2,128,256]:
 for kind in ['BASE.json','INPUT.txt','RECEIPT.json']:names.append(f'T170_THREE_COMPRESSED_d14_C{C}_{kind}')
old=json.loads((H/'T170_D16_SUBMISSION.json').read_bytes());deps={p:h for p,h in old['dependencies'].items() if Path(p).name in ['chord5_lower_bound.md','chord5_exact_certificates.json']};assert len(deps)==2
for p,h in deps.items():assert sha(Path(p))==h
axis=F(49312208313,549755813888);floor=F(91464273436,10**12);assert axis<floor
r={'at':datetime.now().astimezone().isoformat(),'claim':'T170-LEAD-ROLLING-D14-001','version':1,'proof_sha256':sha(proof),'status':'NOT ADMITTED; two full exact independent distinct-account audits required','files':{n:sha(H/n) for n in names},'dependencies':deps,'axis':str(axis),'diagonal_floor_down':str(floor),'gap':str(floor-axis),'scope':'New controlled three-slab physical comparison and compact constructive bias, all2^24 finite states checked. Retained audited C003v2 diagonal premise; no priority/fullT170 claim.'}
(H/'T170_D14_SUBMISSION.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
with (H/'CLAIMS.jsonl').open('ab') as f:f.write((json.dumps({'at':r['at'],'claim':r['claim'],'version':1,'sha256':r['proof_sha256'],'status':'candidate','submission':'T170_D14_SUBMISSION.json'})+'\n').encode())
M='~/brain-repo/12_cognitive_architecture/agent_mesh/agent_mesh.py';requests=[]
for to in ['codex-w683','codex-term-agent']:
 body=f'After current D16/D15 priority, full exact distinct-account review requested: NEW frozenD14 {proof}, SHA {r["proof_sha256"]}, manifest {H/"T170_D14_SUBMISSION.json"}. Three-slab canonical geometry/Poisson control extends rolling method, full proof restated. C256 compact65536base values definesall16777216biasunits by signed-ceil DP, A0=98624416626/S2^40. Native plus independent57.7sec unbounded Python FULLreplay agree, all65536base requirements max98624394809<A0; C2independent8state stationary/cycle61803/119341/selfrewardfault; actualwrongbase row reconstructed/rejected. Axis.0896983844<d14floor.091464273436. Please freezeactualaccountbeforesemanticread/end, auditnewthree-slab proof/completeconstructor/allstates/diagonal. First Python fault boolean only algebra; supplementaryactualrow receipt explicitlycorrects scope, originalvalidfullreplayunchanged. No newagents, no admission until2audits. Own packet backup next.'
 p=subprocess.run(['C:/Python314/python.exe',M,'send','--agent','codex-term-362ebe34','--to',to,'--topic','T170-D14-three-slab-exact-audit','--body',body,'--require-ack'],capture_output=True,text=True,encoding='utf-8');assert p.returncode==0,p.stderr;requests.append({'to':to,'response':p.stdout})
(H/'T170_D14_REVIEW_REQUESTS.json').write_text(json.dumps(requests,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:r[k] for k in ['claim','proof_sha256','axis','gap']}))
