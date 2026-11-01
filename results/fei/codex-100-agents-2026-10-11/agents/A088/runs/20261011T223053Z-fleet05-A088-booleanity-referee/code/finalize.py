from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
team=Path(r'~\brain_workers\FEI100_20261011')
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
claims=[];original=[];receipts=[]
audit=ROOT/'AUDIT.md';ah=hashlib.sha256(audit.read_bytes()).hexdigest()
for i in [31,32,33,36,37,38,66,67,68]:
    p=next((team/'agents'/('A%03d'%i)/'runs').glob('*/CLAIMS.json'))
    data=json.loads(p.read_text(encoding='utf-8-sig'))
    for c in data:
        if not c['claim_id'].startswith('A%03d-'%i):continue
        original.append({'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'claim':c})
        c=json.loads(json.dumps(c))
        plain=hashlib.sha256(c['exact_statement'].encode()).hexdigest()
        combined=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
        assert c['statement_sha256'] in [plain,combined],(c['claim_id'],'statement hash mismatch')
        computed=c['statement_sha256']; hash_convention='UTF8 exact_statement' if computed==plain else 'canonical JSON statement+hypotheses'
        assert set(c)==set(protocol['required_per_run']['claim_fields'])
        record={'reviewer':'fleet05/A088','verdict':'ACCEPT_AT_STATED_SCOPE','lead_verdict':'HOLDS','method':'Independent algebraic reconstruction and applicable exact non-Boolean scope diagnostic; separate integer/Fraction/certified-log checker; no substantive repair supplied','source':str(audit),'sha256':ah,'reviewer_conflict':False,'shared_registry_adoption':'PENDING_B20'}
        c['review_records'].append(record)
        c['status']='INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE_PENDING_INDEX_ADOPTION'
        claims.append(c)
        receipts.append({'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':computed,'hash_convention':hash_convention,'plain_statement_sha256':plain,'source_claims':str(p),'verdict':'ACCEPT_AT_STATED_SCOPE','lead_verdict':'HOLDS','reviewer_conflict':False})
assert len(claims)==13
(ROOT/'CLAIMS.json').write_text(json.dumps(claims,indent=2),encoding='utf-8')
(ROOT/'out/ORIGINAL_CLAIMS.json').write_text(json.dumps(original,indent=2),encoding='utf-8')
(ROOT/'out/REVIEW_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
progress={
'protocol_revision':protocol['revision'],'run_id':ROOT.name,'stream':'B18','packet_id':'A088','gap_id':'G-BOOLEANITY','attempt_id':'A088-independent-booleanity-audit-1','method':'Independent proof reconstruction with exact signed-phase, physical-coupling and normalized-real scope controls',
'mathematical_delta':'Thirteen v1 claims accepted independently at stated scopes, including late-arrival A068 quadratic packets relative to recovered C001; genuine Boolean phase/arithmetic/fair-child uses isolated; 94511 exact assertions passed; full FEI and complete erasure/reference payment remain open',
'deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_AUDIT','mathematical_status':'SCOPED_CLAIMS_REVIEWED_FULL_FEI_OPEN',
'claim_versions_used':[{'claim_id':c['claim_id'],'version':c['version'],'statement_sha256':c['statement_sha256']} for c in claims],
'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':c['version'],'change':'A088 independent ACCEPT_AT_STATED_SCOPE review; no theorem change'} for c in claims],
'source_artifacts':['AUDIT.md','REPORT.md','out/SOURCE_MANIFEST.json','out/ORIGINAL_CLAIMS.json','out/REVIEW_RECEIPTS.json','out/VALIDATION.json','out/SUPPLEMENT_VALIDATION.json','out/COUPLED_PHASE_CERTIFICATE.json','out/A068_VALIDATION.json'],
'next_consumers':['A031','A033','A034','A036','A039','A040','A057','A064','A070','A094','A097','B20'],
'next_action':'Audit the first source-complete A039 physical-child Delta/reference-reset transfer on the sparse activated bent-defect tree, retaining A037 erased labels and terminal entropy',
'stagnant_substantive_attempts':0,'blockers':['No source-complete theorem at inspected cutoff for A034,A035,A039,A040,A069,A070; future audit dependencies only','Supervisor index adoption and mirror verification unobserved'],'packet_ids':['A088']}
fields=[s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(fields)
for name in ['PROGRESS.json','PACKET_DELTA.json']:(ROOT/name).write_text(json.dumps(progress,indent=2),encoding='utf-8')
inventory={}
for i in list(range(31,41))+list(range(66,71)):
    folder=team/'agents'/('A%03d'%i)/'runs'
    inventory['A%03d'%i]=[str(p) for p in folder.rglob('*') if p.is_file() and p.name in ['CLAIMS.json','REPORT.md','derivation_checkpoint.md']]
(ROOT/'out/FINAL_SOURCE_INVENTORY.json').write_text(json.dumps({'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':inventory,'review_cutoff':'The thirteen source-bound claims in ORIGINAL_CLAIMS.json; any later arrivals are pending next-stage audit'},indent=2),encoding='utf-8')
(AGENT/'STATUS.md').write_text('STATE: A088 stage complete locally: thirteen scoped v1 claims independently accepted; 94,511 exact assertions PASS; full FEI OPEN; adoption pending.\nNEXT: Audit A039 physical-child Delta/reference-reset transfer in A037 fair coupling, retaining erased labels and terminal entropy; A094 challenge this review.\n',encoding='utf-8')
entry='2026-10-12: Consumed late-arrival A068 quadratic context-rank theorem before closing stage; independent packet/polar-rank and cyclic q=5 checks passed 71258 assertions. Final total 13 scoped claim reviews and 94511 exact assertions; C001 regular-core dependency explicitly preserved. Required files and hashes finalized locally; full FEI OPEN.'
if entry not in (AGENT/'WORKLOG.md').read_text(encoding='utf-8'):
    with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+entry+'\n')
entry='Quadratic-sign control products have affine-flat spectra with entropy equal to polar rank and <=2I. With distinct private data labels, their Fourier packets remain disjoint under arbitrary control overlap, giving H(F)=H(h)+E H(a_S). A regular Boolean core then inherits C_reg D_x+2I_z via the recovered threshold theorem; normalized real symmetric monotone cores do not inherit that entropy estimate. Private-label identification reintroduces coherent collisions.'
if entry not in (AGENT/'LEARNED.md').read_text(encoding='utf-8'):
    with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+entry+'\n')
schema={'status':'PASS','claim_count':len(claims),'claim_fields_exact':True,'progress_fields_exact':True,'statement_hashes_valid':True,'packet_delta_matches_progress':(ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()}
(ROOT/'out/SCHEMA_CHECK.json').write_text(json.dumps(schema,indent=2),encoding='utf-8')
artifacts=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        b=p.read_bytes();assert len(b)<20*1024*1024
        artifacts.append({'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(ROOT/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps({'local_only':True,'files':artifacts},indent=2),encoding='utf-8')
print(json.dumps({**schema,'run':str(ROOT),'artifact_count':len(artifacts)}))
