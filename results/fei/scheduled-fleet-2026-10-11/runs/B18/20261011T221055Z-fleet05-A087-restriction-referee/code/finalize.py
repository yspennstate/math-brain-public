from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];BASE=AGENT.parent
PROTOCOL=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTOCOL.read_text(encoding='utf-8-sig'));now=datetime.now(timezone.utc).isoformat()
sources={
'A021':'20261011T214020Z-fleet05-A021-rare-core-asymptotics',
'A022':'20261011T215800Z-fleet05-A022-one-point-surgery',
'A026':'20261011T214052Z-fleet05-A026-good-coordinate-erasure',
'A027':'20261011T215911Z-fleet05-A027-block-selection',
'A061':'20261011T214516Z-fleet05-A061-entropy-process',
'A062':'20261011T220423Z-fleet05-A062-influence-compensator'}
claims=[];used=[];intake=[];hash_warnings=[]
for agent,run in sources.items():
    directory=BASE/agent/'runs'/run
    for p in directory.iterdir():
        if p.is_file() and p.suffix in ['.md','.tex','.json']:
            data=p.read_bytes();intake.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'inspection':'proof/claim reconstruction for .tex and CLAIMS; other files inventory'})
    p=directory/'CLAIMS.json'
    for original in json.loads(p.read_text(encoding='utf-8-sig')):
        claim=copy.deepcopy(original);actual=hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()
        if actual!=claim['statement_sha256']:hash_warnings.append({'claim_id':claim['claim_id'],'recorded':claim['statement_sha256'],'actual':actual})
        source_statement_hash=claim['statement_sha256'];claim['statement_sha256']=actual
        claim['review_records'].append({'reviewer':'A087','timestamp':now,'verdict':'ACCEPT_AT_STATED_SCOPE','independent_method':'Direct integer character-sum/block-channel reconstruction, exact physical descendants, analytic proof and independent bounded checker','proof_source':str(ROOT/'REPORT.md'),'validation_sources':['out/check_results_identity.json','out/check_results_selection.json','out/check_results_activation.json','out/extra_results.json'],'scope_guard':'No universal FEI conclusion; terminal boundary and original structural hypotheses retained.'})
        claim['review_records'][-1]['source_recorded_statement_sha256']=source_statement_hash
        claim['review_records'][-1]['local_UTF8_exact_statement_sha256']=actual
        claim['status']='INDEPENDENTLY_ACCEPTED_AT_STATED_SCOPE_BY_A087'
        claim['next_consumers']=list(dict.fromkeys(claim['next_consumers']+['A094','B20']))
        claims.append(claim);used.append({'claim_id':claim['claim_id'],'version':claim['version'],'source_artifact':str(p),'review_status':'ACCEPT_AT_STATED_SCOPE'})
statement='For every balanced Boolean core g on a finite uniform cube and k>=1 fresh fair point controls, let q=2^-k and F=1+A_k(g-1). On the physical control-first tree stopped at the first inactive control or at g, A061 one-sided logarithmic charge lambda_s equals the exact magnitude-mismatch KL residual at every active node s: lambda_s=u-u^2+u^2 log2((1-2u+2u^2)/u^2), u=2^-s. Its physically weighted sum is q(k+A_k)<=4kq with A_k=sum_(s=1..k)2^-s[2s-1+log2(1-2^(1-s)+2^(1-2s))]. Queried influence is kq, terminal influence qI(g), and terminal entropy qH(g); no terminal bound on arbitrary cores is implied.'
claims.append({'claim_id':'A087-CONTROL-TREE-LAMBDA-KL-IDENTITY','version':1,'exact_statement':statement,'hypotheses':['Uniform finite cube, Boolean balanced core','Fresh disjoint point controls, k>=1','Control-first stopping and fair physical branch probabilities','Bit entropy; signed/magnitude equality only for these actual children'], 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A087'],'proof_source':str(ROOT/'REPORT.md'),'proof_dependencies':[],'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A021','A023','A028','A061','A064','A094','B20']})
progress={'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B18','packet_id':'A087','gap_id':'G-R-MISMATCH','attempt_id':'A087-restriction-audit-stage-1','method':'Independent direct-character exact physical-block and stopped-tree reconstruction plus analytic remainder/limit audit','mathematical_delta':'Eleven v1 claims accepted at original scope; 74,787 independent exact assertions; balanced control-tree lambda equals magnitude-KL residual with cost <=4k2^-k and arbitrary terminal entropy retained. Full FEI OPEN.','deliverable_status':'COMPLETE_LOCAL_AUDIT_OF_AVAILABLE_CLAIMS','mathematical_status':'ELEVEN_SCOPED_CLAIMS_INDEPENDENTLY_ACCEPTED; UNIVERSAL_FEI_OPEN','claim_versions_used':used,'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'status':c['status']} for c in claims],'source_artifacts':[str(ROOT/'REPORT.md'),str(ROOT/'CLAIMS.json'),str(ROOT/'out/source_inventory.json'),str(ROOT/'out/live_intake.json'),str(ROOT/'code/check.py'),str(ROOT/'code/extras.py')],'next_consumers':['A021','A022','A023','A026','A027','A028','A029','A061','A062','A064','A094','B20'],'next_action':'Audit explicit sparse-bent surgery debt on both selector-first and control-first physical descendants, retaining per-label reserve and terminal entropy; intake the nine remaining packets as completed claims arrive.','stagnant_substantive_attempts':0,'blockers':['B18 STREAM_NOTES absent at supplied path','No complete source claim for A023-A025, A028-A030, A063-A065 at inspected intake; not mathematical refutations','Universal nonreusing logarithmic/terminal payment remains unproved'],'packet_ids':['A087']}
def save(name,value):ROOT.joinpath(name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
save('CLAIMS.json',claims);save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
save('out/live_intake.json',{'timestamp':now,'source_artifacts':intake,'source_statement_hash_warnings':hash_warnings,'unavailable_claim_packets':['A023','A024','A025','A028','A029','A030','A063','A064','A065'],'inventory_is_not_full_document_audit':True})
AGENT.joinpath('STATUS.md').write_text('STATE: A087 independently accepted eleven restriction claims at stated scope; 74,787 exact assertions passed; full FEI OPEN.\nNEXT: Audit sparse-bent surgery tree debt with labelled reserves and terminal entropy; consume remaining nine packets when source-complete.\n',encoding='utf-8')
with AGENT.joinpath('WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{now} — Read protocol/BOARD and available B05/B06/B13 proofs. B18 notes absent. Audited A021,A022,A026,A027,A061,A062: eleven claims accepted at stated scope. Combined pilot stopped at runtime guard; unchanged domain split into sequential phases, all PASS (74,787 assertions). Reconstructed exact lambda=KL residual on balanced control-first trees; terminal entropy remains. Nine unavailable packets not accepted. Saved local review records and source/validation receipts; no external writes.\n')
AGENT.joinpath('LEARNED.md').write_text('''# Durable restriction audit facts

- Physical revealed-block assignments have probabilities 2^-|U| conditional on the independent policy seed and past observations. Spectral packet posteriors do not replace those probabilities. A two-control activated dictator has empty-packet posterior 4/5 versus physical branch 1/2.
- Exact physical block ledger: H(f)-E H(f_z)=H(S_U|S_V)+I(Z;T), I(f)=I_U(f)+E I(f_z). Each original label separately conserves expected queried cost plus terminal influence. Node total influence is not a fresh budget; pathwise influence need not decrease.
- On balanced-core point activation, control-first A061 lambda is exactly the magnitude-KL residual u-u²+u²log2((1-2u+2u²)/u²). Its tree sum is 2^-k(k+A_k)<=4k2^-k; queried influence k2^-k and terminal H=2^-kH(core) must stay separate.
- A021 v1 (two claims), A022 v1 (one), A026 v1 (two), A027 v1 (two), A061 v1 (two), A062 v1 (two) independently accepted by A087. Source statements are preserved in this run's CLAIMS.json. Acceptance does not close full FEI.
- A026 affine dimension <=4 is hereditary under physical projection; nonphysical linear reparametrization cannot replace queries. Direct enumeration reproduces selectable amplitude maxima 0,2,3,7/2. The 32-bit threshold >=24 has exact A_i/I_i=2220940451/536870912>4 and refutes only that proxy constant.
- A027 unrestricted core-block payment is FEI-strength even though the block is proper. Mean-nonnegative core bound K implies FEI K+2; FEI C implies block bound C+5. The exceptional empty-control fiber is essential.
- Fixed-dimensional stopping permits bounded convergence despite arbitrary waits; growing dimension does not. A062 balanced activated bent-product family has uniformly bounded root influence but terminal I and H tending to zero almost surely with expectations tending to 1/2 and equal to 1. Uniform integrability is an independent obligation.
- A022 point-surgery signed mismatch equals minority mass because integer Walsh ratios are even; adjacent surgery can violate this equality. Its fixed-seed occupancy classification is not uniform over arbitrary varying seeds and does not disprove FEI.
- Runtime-limited pilots must persist checkpoints before accepting results. This stage's initial combined pilot saved none and was discarded; sequential unchanged-domain runs supply the certificates. EXTRA_SPEC adjacent count corrected from 36 to 68 without domain change.
- Eight source statement hashes differ from raw UTF-8 exact_statement hashes under the local convention. Source files are unchanged and their byte hashes are pinned; local accepted copies normalize statement_sha256 and preserve each recorded source hash in the review record. This is a metadata discrepancy, not a failed mathematical assertion.
''',encoding='utf-8')
required=protocol['required_per_run'];progress_keys=[field.split(' (')[0] for field in required['progress_fields']]
validation={'report_heading_fields':[field for field in required['report_fields'] if '## '+field in ROOT.joinpath('REPORT.md').read_text(encoding='utf-8')],'claim_field_sets_exact':all(set(c)==set(required['claim_fields']) for c in claims),'progress_field_set_exact':set(progress)==set(progress_keys),'progress_schema_note':'The protocol labels packet_ids with parenthetical explanatory prose; canonical field is packet_ids as required by compatibility section.','packet_delta_equal':ROOT.joinpath('PROGRESS.json').read_bytes()==ROOT.joinpath('PACKET_DELTA.json').read_bytes(),'claim_count':len(claims),'source_statement_hash_warnings':hash_warnings}
assert len(validation['report_heading_fields'])==len(required['report_fields']);assert validation['claim_field_sets_exact'];assert validation['progress_field_set_exact'];assert validation['packet_delta_equal'];assert len(claims)==12
save('out/schema_validation.json',validation)
receipts=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='persistence_receipts.json':
        b=p.read_bytes();assert len(b)<20*1024*1024;receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=AGENT/name;b=p.read_bytes();receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save('out/persistence_receipts.json',{'timestamp':now,'local_only':True,'artifacts':receipts,'regeneration_commands':['python -X utf8 code/read_sources.py','python -X utf8 code/check.py identity','python -X utf8 code/check.py selection','python -X utf8 code/check.py activation','python -X utf8 code/extras.py','python -X utf8 code/finalize.py'],'command_directory':str(ROOT)})
print(json.dumps({'status':'SAVED','accepted_source_claims':len(used),'new_scoped_claims':1,'schema_valid':True,'hash_warnings':hash_warnings,'run':str(ROOT),'receipt_artifacts':len(receipts)},indent=2))
