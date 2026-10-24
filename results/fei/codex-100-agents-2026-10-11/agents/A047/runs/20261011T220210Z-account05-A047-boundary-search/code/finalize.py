import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]
campaign=Path(r'~\mop_fei100\reports\fei-2026-10-11')
protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
statement=('For every fixed finite pair of Boolean children g,h in a fixed product-biased Fourier basis, '
           'lim_{p->0}(J_X-M_X)/(p log2(1/p))=2Z+2E(gh)-2<=1/2-2(E(gh)-1/2)^2<=1/2, '
           'where Z=sum_{G_T=0}H_T^2. Equality 1/2 is attained by constant/quarter-defect children '
           'and by balanced children after fresh-character multiplication. If child Fourier supports '
           'are disjoint then M_X=J_X=h2(p) for every p in (0,1).')
claim={'claim_id':'A047-SHARP-FIXED-CHILD-RARE-SELECTOR','version':1,
       'exact_statement':statement,'hypotheses':['finite Boolean sign children','common fixed orthonormal product Fourier basis','fixed interior data biases','independent selector with p down to zero','entropy in bits'],
       'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A047'],
       'proof_source':'REPORT.md complete derivation; BOUNDARY_ASYMPTOTICS.tex',
       'proof_dependencies':[],'review_records':[], 'status':'PROVED_LOCALLY_REVIEW_PENDING',
       'supersedes':[],'refutes':['Endpoint repaired tax coefficient strictly below 1/2'],
       'first_unproved_line':'Uniform finite-p half-tax bound and nonreusing stopping-tree transport remain unproved.',
       'next_consumers':['A092','A087','A049','A050','A042','A071']}
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B10','packet_id':'A047',
 'gap_id':'FEI-B10-A047-INITIAL','attempt_id':'A047-boundary-01','method':'fixed-child analytic expansion, exhaustive integer Walsh pairs, rational log interval certificates',
 'mathematical_delta':'Sharp dimension-independent endpoint coefficient <=1/2, attained with balanced Boolean children; disjoint-support debt zero exactly; unequal-bias AND expansion and 20 finite interval certificates.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'AUXILIARY_THEOREM_PROVED_LOCALLY_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[],'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['REPORT.md','BOUNDARY_ASYMPTOTICS.tex','FROZEN_SPEC.json','FROZEN_SPEC_UNEQUAL.json','BOUNDARY_SEARCH_PLAN.json','code/boundary.py','code/unequal.py','out/results.json','out/unequal.json'],
 'next_consumers':claim['next_consumers'],'next_action':'A092/A087 independent reconstruction; derive finite-p Boolean fiber envelope uniform in dimension and moving biases.',
 'stagnant_substantive_attempts':0,'blockers':['B10 STREAM_NOTES.md absent; independent review and supervisor mirror pending; finite-p uniform remainder not proved'], 'packet_ids':['A047']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected,(set(progress),expected)
report=(R/'REPORT.md').read_text(encoding='utf8')
assert all(x in report for x in protocol['required_per_run']['report_fields'])
(R/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf8')
for name in ('PROGRESS.json','PACKET_DELTA.json'): (R/name).write_text(json.dumps(progress,indent=2),encoding='utf8')
plan={'primary':json.loads((R/'FROZEN_SPEC.json').read_text()),'unequal':json.loads((R/'FROZEN_SPEC_UNEQUAL.json').read_text())}
(R/'BOUNDARY_SEARCH_PLAN.json').write_text(json.dumps(plan,indent=2),encoding='utf8')
source_files=[campaign/name for name in ('EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex')]
source_files.extend([campaign/'runs/B09/20261011T195500Z-account01-B09-biased-restriction-uncertainty/REPORT.md',campaign/'verification/B09_interval_repair_20261011/REPORT.md'])
context=Path(r'~\brain_workers\FEI100_20261011\context')
source_files.extend(context.glob('*.txt'))
source_files.append(Path(r'~\brain_workers\FEI100_20261011\BOARD.md'))
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
source_files.extend(supp/n for n in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md'))
source_files.extend(supp/'sources'/n for n in ('ONE_BIT_ENDPOINT.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','GAMMA_ENDPOINT_LEDGER.md'))
sources=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in source_files]
(R/'out/source_manifest.json').write_text(json.dumps(sources,indent=2),encoding='utf8')
receipts=[]
for p in R.rglob('*'):
    if p.is_file() and p.name!='persistence.json' and '__pycache__' not in p.parts:
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
rolling=[{'path':str(R.parents[1]/name),'sha256':hashlib.sha256((R.parents[1]/name).read_bytes()).hexdigest()} for name in ('STATUS.md','WORKLOG.md','LEARNED.md')]
(R/'out/persistence.json').write_text(json.dumps({'saved_at':datetime.now(timezone.utc).isoformat(),'files':receipts,'rolling':rolling,'schema_checks':'PASS','independent_review':'PENDING','mirror':'NOT_VERIFIED'},indent=2),encoding='utf8')
print('PASS: protocol fields, required report elements, persisted hashes; files',len(receipts))
