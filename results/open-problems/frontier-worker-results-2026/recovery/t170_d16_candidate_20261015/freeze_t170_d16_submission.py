from pathlib import Path
from datetime import datetime
import hashlib,json,subprocess
H=Path(__file__).resolve().parent;PY='C:/Python314/python.exe';B=Path('~/brain-repo')
M=B/'12_cognitive_architecture/agent_mesh/agent_mesh.py';A='codex-term-362ebe34'
proof=H/'T170-LEAD-D16-001_v1.md';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rp=H/'T170_D16_SUBMISSION.json';assert not rp.exists(),'Already frozen; preserve prior exact submission'
names=['T170-LEAD-D16-001_v1.md','T170_DISCRETE_HORIZONTAL_BOUND.md','prepare_t170_discrete_screen.py','T170_DISCRETE_RATE_RECEIPT.json','t170_discrete_exact.cpp','t170_discrete_exact_d16.txt','T170_DISCRETE_EXACT_BUILD_RECEIPT.json','T170_DISCRETE_D16_EXACT_RECEIPT.json','T170_DISCRETE_D16_EXACT.log','prepare_t170_discrete_exact.py','run_t170_discrete_exact.py','run_polite.py','T170_SCREEN_control17_RECEIPT.json','T170_SCREEN_new16_RECEIPT.json']
deps=[Path('~/brain_workers/w676/T170/proofs/T170-C004_v1.md'),Path('~/brain_workers/w676/T170/proofs/T170-C007_v2.md'),Path('~/brain_workers/w685/T170/proofs/chord5_lower_bound.md'),Path('~/brain_workers/w685/T170/logs/chord5_exact_certificates.json'),Path('~/brain_workers/w683/checks/t170_c012_binding_own.json')]
r={'at':datetime.now().astimezone().isoformat(),'claim':'T170-LEAD-D16-001','version':1,'proof_sha256':sha(proof),'status':'proof candidate, two independent exact-content distinct-account reviews requested; NOT ADMITTED','files':{n:sha(H/n) for n in names},'dependencies':{str(p):sha(p) for p in deps}}
rp.write_bytes((json.dumps(r,indent=2)+'\n').encode())
(H/'CLAIMS.jsonl').open('ab').write((json.dumps({'at':r['at'],'row':'T170','id':r['claim'],'version':1,'status':'proof candidate, unaudited','target':3,'proof':str(proof),'proof_sha256':r['proof_sha256'],'statement':'Exp(1) undirected bond FPP onZ16 nonball via exact discrete horizontal rate and full11slab upward-rounded certificate; margin2615017357267518989/2952790016000000000000>0; conditional audited physical/diagonal premises.'})+'\n').encode())
results=[]
for to in ['codex-w683','codex-term-agent']:
 body=('Exact D16 candidate READY: '+str(proof)+' SHA256 '+r['proof_sha256']+'. Manifest '+str(rp)+' pins14ownartifacts +5dependencies. '
  'Newclaim T170-LEAD-D16-001 v1. mu_axis<=1019722296067/12094627905536 <10649701413/125000000000<=mu_diag; exactmargin2615017357267518989/2952790016000000000000. '
  'New horizontal sigma=30n-2sum_{j<n}popcount(j), allcounts<=10000; unary grid->hypercube embedding +25million finite split inequalities. '
  'Fresh full11stage checked uint64 upward2^-40 recurrence172008828states, no importedcache,229sec. C004v1/C007v2 physical and C003v2 floor remain explicitexactpremises. '
  'Please independently derive boundary/physical substitution, all caps+rates+Gamma faces, fresh integerreplay+strictmargin and Euclideanunits; freeze actualaccountidentity before semantic read. '
  'No literaturepriority/globalminimality or lowerdimclaim; NOT ADMITTED. Existing own independent C012 evaluators may be adapted but do not read own lead numeric outputs until independentderivation. No newagents/subagents. File exactclaimv1/hash PASSorFIX in ownreview files and sendreceipt; authorfolder is myterm, not w676.')
 p=subprocess.run([PY,str(M),'send','--agent',A,'--to',to,'--topic','T170-D16-exact-candidate-review-request','--body',body,'--require-ack'],capture_output=True)
 results.append({'to':to,'exit':p.returncode,'result':p.stdout.decode('utf-8')})
 assert p.returncode==0,p.stderr.decode('utf-8')
(H/'T170_D16_REVIEW_REQUESTS.json').write_bytes((json.dumps(results,indent=2)+'\n').encode())
(H/'NEXT.md').open('ab').write(('\n'+r['at']+': FROZEN newT170D16 candidate '+r['proof_sha256']+'; exact upward root1019722296067/12094627905536, margin2615017357267518989/2952790016000000000000. Manifest14files+5dependencies. Required two independent exact reviews requested from existingw683/account4 and5a8/account3, no newagents. No admission yet; d17-21 remains recorded. Do NOTrerun completedexact229sec. Archive packet nextafterD91admission backupfinished.\n').encode())
print(json.dumps({'proof_sha256':r['proof_sha256'],'requests':results}))
