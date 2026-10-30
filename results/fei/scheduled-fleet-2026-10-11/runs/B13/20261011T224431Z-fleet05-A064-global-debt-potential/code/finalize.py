from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
rid=R.name
statement=('On a finite fair physical restriction tree, D_v<=C*d_v+Q_v-E[Q_child|v], E Q_root<=K*B and E[H(leaf)-Q_leaf]<=L*E I(leaf), where B=E sum queried d, imply H(f)<=max(C+K,L)*I(f). The explicit terminal-corrected reserve Q_v=H(g_v)-E[H(leaf)|v] has exact drift D, is nonnegative and has zero leaves. For arbitrary-core point activation F=1+A_r(g-1), p=2^-r, a=1-Eg, control-first Q_root<=8*r*p*a with terminal entropy pH(g) retained. Activated arbitrary bent point-splice cores on even k>=4, r>=1 have separate terminal constant below 3 and reserve certificates at 8 for control-first and 9 for selector-first. The fixed candidates c*eta*log2(1/eta) and c*I_remaining*depth fail on B05 selector roots for every fixed finite c,C>=0 (history c=0 reduces to local failure); CI-H has the wrong payment drift except at D<=C*d. No universal root resource bound or full FEI is claimed.')
hyp=['Actual Boolean signs on finite uniform cubes; normalized Fourier coefficients; bits',
     'Physical fresh-coordinate tree; finite stopping; independent seed and decisions measurable in revealed history',
     'Explicit initial and terminal assumptions in general payment theorem',
     'Point activation uses fresh controls and arbitrary core, whose entropy remains terminal',
     'Bent family has even k>=4 and r>=1; any bent b and vertex v; b flipped at v',
     'History no-go is the stated complete-tree I_remaining*depth formula; physical minority is distinct from spectral minority mass']
payload={'statement':statement,'hypotheses':hyp}
digest=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
claim={'claim_id':'A064-TERMINAL-CORRECTED-GLOBAL-DEBT','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest,'contributors':['A064; arbitrary-bias activation direction credited to A023'],'proof_source':{'run_id':rid,'path':'GLOBAL_DEBT_POTENTIAL.tex','supplement':'REPORT.md and POTENTIAL_OBSTRUCTION_TESTS.md','certificate':'out/VALIDATION.json'},'proof_dependencies':[{'claim_id':'A061-FAIR-TREE-PROCESS','version':1,'scope':'finite physical entropy identity; A087 independently accepted'},{'claim_id':'A062-INFLUENCE-STOPPING-INTERFACE','version':1,'scope':'finite same-tree influence identity; A087 independently accepted'}],'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['fixed physical-minority rarity reserve at every coordinate','stated history I_remaining*depth reserve at every coordinate','CI-H slack as automatic debt drift on an FEI-certified class'],'first_unproved_line':None,'next_consumers':['A065','A077','A029','A037','A087','A094','B20']}
(R/'CLAIMS.json').write_text(json.dumps([claim],indent=2)+'\n',encoding='utf-8')
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':rid,'stream':'B13','packet_id':'A064','gap_id':'G-R-MISMATCH','attempt_id':'A064-terminal-corrected-reserve-v1','method':'Finite-tree terminal correction; explicit coherent activation spectrum; minority/history/sign obstructions; exact interval validation','mathematical_delta':'Boundary-complete potential and both-order unbounded bent-splice certificates; three explicit candidate failures; universal initial payment remains open','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'PROPER_CLASS_PAYMENT_AND_CANDIDATE_NOGOS_PROVED_LOCALLY; UNIVERSAL_GAP_OPEN','claim_versions_used':['A061-FAIR-TREE-PROCESS v1','A062-INFLUENCE-STOPPING-INTERFACE v1; both A087 accepted','A023 arbitrary-bias direct bound reconstructed, not assumed accepted'],'claims_created_or_changed':['A064-TERMINAL-CORRECTED-GLOBAL-DEBT v1'],'source_artifacts':['REPORT.md','GLOBAL_DEBT_POTENTIAL.tex','POTENTIAL_OBSTRUCTION_TESTS.md','out/VALIDATION.json','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json'],'next_consumers':['A065','A077','A029','A037','A087','A094','B20'],'next_action':'Derive shared-control union reserve ownership correction with one exclusive physical influence account and full terminal entropy','stagnant_substantive_attempts':0,'blockers':['Universal initial reserve resource bound and terminal admission remain unproved','Independent review and supervisor mirrors pending'],'packet_ids':['A064']}
for name in ('PROGRESS.json','PACKET_DELTA.json'): (R/name).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
progress_keys=[x.split(' (',1)[0] for x in protocol['progress_fields']]
assert set(progress)==set(progress_keys)
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all('# '+field in report for field in protocol['report_fields'])
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
v=json.loads((R/'out'/'VALIDATION.json').read_text()); assert v['status']=='PASS' and v['exact_assertions']==4105
assert len((A/'STATUS.md').read_text().splitlines())==2
assert hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()==claim['statement_sha256']
sources=json.loads((R/'out'/'SOURCE_RECEIPTS.json').read_text())
base=Path(r'~\brain_workers\FEI100_20261011')
for p in [base/'BOARD.md',base/'claude/B13/STREAM_NOTES.md',base/'agents/A023/runs/20261011T221608Z-fleet05-A023-amortized-rarity-budget/REPORT.md',base/'agents/A062/runs/20261011T220423Z-fleet05-A062-influence-compensator/FAIR_TREE_INFLUENCE_PROCESS.tex',base/'agents/A087/runs/20261011T221055Z-fleet05-A087-restriction-referee/REPORT.md']:
    raw=p.read_bytes(); sources.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'scope':'Read or inspected mathematical source passages as specified in REPORT.md'})
(R/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(sources,indent=2)+'\n',encoding='utf-8')
schema={'status':'PASS','claim_fields':'exact protocol set','progress_fields':'protocol set with explanatory suffix of packet_ids removed','report_fields':'all seven present','compatibility_copy':'identical','statement_hash':'registry canonical JSON convention','files_under_20mb':True}
(R/'out'/'SCHEMA_CHECK.json').write_text(json.dumps(schema,indent=2)+'\n',encoding='utf-8')
files=list(R.rglob('*'))+[A/x for x in ('STATUS.md','WORKLOG.md','LEARNED.md')]
receipts=[]
for p in files:
    if not p.is_file() or p.name=='PERSISTENCE_RECEIPTS.json': continue
    raw=p.read_bytes(); assert len(raw)<20*1024*1024
    receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
out={'saved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'receipts':receipts,'external_mirrors_verified':False,'independent_review_verified':False}
(R/'out'/'PERSISTENCE_RECEIPTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'schema':'PASS','artifacts_hashed':len(receipts),'claims':1,'exact_assertions':v['exact_assertions'],'full_fei':'OPEN'},indent=2))
