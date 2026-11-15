"""Check small rational witnesses and queue the completed C34 proof."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
base=Path(__file__).resolve().parent;now=datetime.now(timezone.utc).isoformat()
record=json.loads((base/'C34_RETURN_LOWER_RESULTS.json').read_text(encoding='utf-8'))
assert record['live_cases_read']==3
assert record['script_sha256']==hashlib.sha256((base/'check_c34_return_means.py').read_bytes()).hexdigest()
witnesses=[]
for sites,bound in [(5,F(119,100)),(9,F(121,100))]:
 c=next(c for c in record['cases'] if c['parameters']['d']==4 and c['sites']==sites)
 assert c['witness'] and c['iterations']==4
 coeff_path=base/c['coefficient_file'];raw=coeff_path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==c['coefficient_sha256']
 coeff=json.loads(raw);classes=coeff['classes']
 sums={key:sum(F(coeff['episodes']['root_bottom_'+key]['exit_means'][e]) for e in classes) for key in classes}
 assert all(v>=bound for v in sums.values())
 x=F(c['x_lower']);assert x*bound>1
 if sites==5:assert x*bound==F(100378699173193,100000000000000)
 else:assert x*bound==F(26172239526499,25000000000000)
 witnesses.append({'sites':sites,'iteration':4,'x_lower':str(x),'root_row_mean_lower':str(bound),'product':str(x*bound),'coefficient_file':c['coefficient_file'],'coefficient_sha256':c['coefficient_sha256']})
(base/'C34_SMALL_WITNESSES.json').write_text(json.dumps({'at':now,'arithmetic':'Fraction; exact root-row comparisons','witnesses':witnesses},indent=2)+'\n',encoding='utf-8')
path=base/'CLAIMS.jsonl';claims=[json.loads(s) for s in path.read_text(encoding='utf-8').splitlines() if s.strip()]
cid='C34_copied_block_infinite_mean'
if not any(c['id']==cid for c in claims):
 claims.append({'id':cid,'version':1,'kind':'route_failure','target':2,
 'statement':'For C33 copied block episodes, downward-rounded lower iterations x_next=A_T+sum B_T,e*x*y_e and y_c_next=A_c+sum B_c,e*x*y_e witness infinite expected upper-process root visits whenever x_n*min_c sum_e D_c,e>=1. Ordinary T4 five-site star and nine-site one-expanded-child blocks both meet this criterion at n=4. Thus these copied upper comparisons cannot prove finite-mean transience by C33 potentials. No conclusion about the ordinary frog model is asserted.',
 'assumptions':['Precisely the C33 independent copied-block law with all ordinary walks and unbounded entries','Only the ancestral path is guaranteed warm on upward entry; other allowed residents wake once per fresh episode','Global root degree d and bulk degree d+1','Positive probability of reaching a returning root episode; finite set of entry categories'],
 'status':'proof (unaudited)','proof_file':'proofs/C34_copied_block_infinite_mean_v1.md',
 'sources':['proofs/C33_site_block_upper_comparison_v1.md','C34_RETURN_LOWER_RESULTS.json','C34_SMALL_WITNESSES.json','check_c34_return_means.py'],
 'gap':'Independent review of the return-family decomposition, root-generation argument and exact coefficient certificates is pending. No ordinary T4 bound or novelty claim.',
 'audits':[],'proof_sha256':hashlib.sha256((base/'proofs/C34_copied_block_infinite_mean_v1.md').read_bytes()).hexdigest(),
 'implementation_sha256':record['script_sha256']})
part=path.with_suffix('.jsonl.part');part.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8');part.replace(path)
queue=base/'AUDIT_QUEUE.md'
if cid not in queue.read_text(encoding='utf-8'):
 with queue.open('a',encoding='utf-8') as out:out.write('\nC34_copied_block_infinite_mean | 1 | proofs/C34_copied_block_infinite_mean_v1.md | Exact n=4 first-return witnesses close C33 five-/nine-site unbounded-entry copied upper comparisons for finite mean; no ordinary T4 result.\n')
with (base/'ROUTES.jsonl').open('a',encoding='utf-8') as out:
 out.write(json.dumps({'row':'T127','route':'C33 five-/nine-site fresh copied-resident upper comparisons for finite-mean T4 transience','status':'dead','why':'C34 exact return-family witnesses give nondecaying expected root generations; proof unaudited. This is a route-failure claim about these two copied laws, not the original model.','evidence':['proofs/C34_copied_block_infinite_mean_v1.md','C34_RETURN_LOWER_RESULTS.json','C34_SMALL_WITNESSES.json'],'at':now})+'\n')
status=base/'STATUS.md';lines=status.read_text(encoding='utf-8').splitlines();lines[0]='STATE: WORKING';lines[1]='NEXT: Target2: preserve visited-site information across returning inputs in a stronger upper comparison; C33/C34 queued, tested copied five-/nine-site means diverge by the unaudited C34 proof.'
status.write_text('\n'.join(lines)+f'\n{now} C34 v1 proof and small exact n=4 witnesses queued. Both tested copied upper comparisons have infinite expected root visits, subject to audit; further weights on those laws are stopped. Original T3/T4 classification remains open.\n',encoding='utf-8')
with (base/'REPORT.md').open('a',encoding='utf-8') as out:out.write(f'\n{now} C34 v1 proof (unaudited) saved and queued: exact four-step return witnesses close the tested five-/nine-site copied upper comparisons for finite-first-moment transience. No original-model conclusion. NEXT: retain more visited-site memory across returns.\n')
with (base/'RESULT.md').open('a',encoding='utf-8') as out:
 out.write(f'\n{now} C34 v1, proof (unaudited), closes the tested five- and nine-site copied upper comparisons for finite mean: x4=843518480447/10^12 with root-row mean >=119/100, and x4=216299500219/(250*10^9) with root-row mean >=121/100. Both products exceed one exactly. C34_RETURN_LOWER_RESULTS.json and C34_SMALL_WITNESSES.json contain all coefficients/hashes and rounding records. No further potential search on those two laws is useful. This does not classify ordinary T4. NEXT: persistent visited-site memory across returning inputs.\n')
print(json.dumps({'C34_v1':'proof (unaudited)','witnesses':witnesses,'queued':True,'ordinary_T127':'OPEN'}))
