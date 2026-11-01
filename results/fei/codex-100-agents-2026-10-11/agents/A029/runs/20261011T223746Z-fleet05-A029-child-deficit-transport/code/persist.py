"""Persist protocol fields and receipts, confined to this agent directory."""
import hashlib,json,datetime
from pathlib import Path
RUN=Path(__file__).resolve().parents[1]; AGENT=RUN.parents[1]
def dump(path,obj):path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement=('Scoped child-deficit benchmarks: for every nonconstant uniform-cube Boolean sign on n=1..4, '
 'the best relevant one-coordinate entropy-drop/influence ratio minus the best nonempty physical '
 'adaptive depth-at-most-two tree ratio lies in [0,2], with equality exactly for signed AND2 '
 '(including irrelevant-variable extensions) and four-variable bent functions. '
 'For the original B05 family at every even k>=4, r=2k, delta=2^-k, p=2^-r, '
 'both actual selector children have D_4>=p(k-3), and their selector parent has '
 'D_4>=p[k-3-delta(3k+1/2)]>0.')
hyp=['Actual Boolean signs; independent fair physical inputs; entropy in bits; ordinary total influence',
     'Finite ratio claim only n<=4; relevant root and optional branch-dependent relevant second query',
     'B05 claim only its stated quadratic bent core and one-point sign flip, all-zero activation r=2k, even k>=4',
     'No arbitrary terminal deficit is assumed nonnegative']
payload=json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()
claim={
 'claim_id':'A029-CHILD-DEFICIT-BENCHMARKS','version':1,'exact_statement':statement,
 'hypotheses':hyp,'statement_sha256':hashlib.sha256(payload).hexdigest(),'contributors':['fleet05/A029'],
 'proof_source':['REPORT.md','B05_TRANSPORT.md','CHILD_DEFICIT_TRANSPORT.tex','code/census.py','code/verify.py','code/structure.py'],
 'proof_dependencies':[
  {'claim_id':'C005','version':'source ERASURE_REDUCTION.md sections 1,2','status':'PROVED_BASELINE'},
  {'claim_id':'B06-R2','version':'STREAM_NOTES.md v1 2026-10-11 22:38Z','status':'BASELINE_REUSED_NOT_RECLAIMED'},
  {'claim_id':'B05-SPARSE-ACTIVATION-VARIANCE-REFUND-NOGO','version':1,'status':'INDEPENDENTLY_REVIEWED_CONSTRUCTION_ONLY'}],
 'review_records':[], 'status':'AUTHOR_PROVED_SCOPED_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A028','A052','A064','A087','A094','B06 lead']}
dump(RUN/'CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B06','packet_id':'A029',
 'gap_id':'G-R-MISMATCH','attempt_id':'A029-child-deficit-transport-01',
 'method':'Certified exhaustive depth<=2 comparison; actual-child B05 analytic reserve; physical-cut ownership controls',
 'mathematical_delta':'Maximum r1-r2 exactly 2 through n=4; all 976 ties classified; B05 selector debt paid by proved actual child D4 for all even k>=4; repeated-slack sum falsified by parity',
 'deliverable_status':'COMPLETE_LOCAL_SAVED_PENDING_REVIEW',
 'mathematical_status':'SCOPED_BENCHMARKS_PROVED_FULL_FEI_OPEN',
 'claim_versions_used':claim['proof_dependencies'],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','CLAIMS.json','SPEC.json','VERIFY_SPEC.json','STRUCTURE_SPEC.json',
 'B05_TRANSPORT.md','CHILD_DEFICIT_TRANSPORT.tex','SLACK_FLOW.json','out/census_n4.json','out/verification.json','out/structure.json'],
 'next_consumers':['A028','A052','A064','A087','A094','B06 lead'],
 'next_action':'Test depth-two gain<=2 on an arbitrary-core physical selector; derive a structural bound or explicit counterfamily while retaining actual terminal deficits',
 'stagnant_substantive_attempts':0,
 'blockers':['Universal arbitrary-seed terminal deficit remains unproved','Independent agent review and supervisor mirror verification pending'],
 'packet_ids':['A029']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)
sources=[]
ROOT=Path('~/mop_fei100/reports/fei-2026-10-11')
paths=[ROOT/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
SUP=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
paths += [SUP/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += [SUP/'sources'/x for x in ['ERASURE_REDUCTION.md','BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','LOG_ALLOCATION_CURATED.md']]
TEAM=Path('~/brain_workers/FEI100_20261011')
paths += [TEAM/'BOARD.md',TEAM/'claude/B06/STREAM_NOTES.md']
paths += list((TEAM/'context').glob('*.txt'))
paths += [ROOT/'runs/B05/20261011T193057Z-fleet01-B05-rare-restrictions/REPORT.md',ROOT/'runs/B19/20261011T195038Z-fleet01-B19-independent-review/REPORT.md']
for path in paths:
    data=path.read_bytes();sources.append({'path':str(path),'size_bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'read_scope':'See REPORT.md source locators; hash receipt does not assert full semantic review'})
dump(RUN/'SOURCE_RECEIPTS.json',sources)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A029 local stage complete: certified n<=4 depth-two gain max 2, all 976 ties classified; B05 actual-child D4 payment proved; review pending; full FEI OPEN.\nNEXT: A087/A094 review; test arbitrary-core selector depth-two gain with terminal deficits retained, then hand the scoped reserve interface to A064.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} A029 stage 1. Read protocol, board and B06 v1 direction; replaced identity rederivation by depth-two gain census. Frozen n<=3 pilot 0.019s; n<=4 integer/interval census 11.917s, 65,804 nonconstant cases and 3,799,698 trees; max gain exactly 2. Second direct-Walsh/different-log/min-cost implementation 22.648s reproduces all 976 ties. Classified 896 essential-four ties as all quadratic bent signs. Proved original B05 child D4>=p(k-3) and parent D4>=p[k-3-delta(3k+1/2)]>0 for all even k>=4; 19 rational formula checks. Saved cut ownership and parity overcount witness. Universal terminal seed deficit remains unpaid. Independent review/mirror pending.\n')
(AGENT/'LEARNED.md').write_text('''# A029 durable facts, stage 1

1. For all actual Boolean functions n<=4, best one-coordinate physical entropy-drop/influence minus best adaptive depth<=2 tree ratio is in [0,2]. Exact maximum 2; 976 equality tables: signed AND2 extensions plus all 896 four-variable bent functions. Two rigorous implementations agree.
2. Bent mask854: H=4,I=2; root0 children masks30/17 have H=2 each,I=2/1. Reveal the entropy-preserving independent character in child30. PiH=2,PiI=1, terminal H=2 remains. This is genuine child reserve transport, not terminal entropy deletion.
3. B05 even k>=4 with p=2^-2k and delta=2^-k: both actual children D4>=p(k-3), parent D4>=p[k-3-delta(3k+1/2)]>0. Proof uses exact activation coefficients, h(t)<=(1-t)/ln2, H(core)<=k, and scalar JS. No arbitrary-core FEI hypothesis.
4. Refine cuts by replacement. Never add D(internal child) to its descendant expansion. Parity has true reserve Km but summed internal weighted deficits Km(m+1)/2, showing unbounded repeated counting.
5. AND2 times arbitrary h has a paid depth-two tree PiH=2,PiI=1 leaving signed h; D_K= D_K(h)+(K-2). A cheap local tree does not pay universal terminal entropy.
6. Follow B06 R2 without re-claiming its identity. Primary exhaustive ties initially looked like AND2 only in n<=3; n=4 adds bent functions. Do not extrapolate equality classification from the pilot.
''',encoding='utf-8')
artifacts=[]
for path in sorted(RUN.rglob('*')):
 if path.is_file() and path.name!='ARTIFACT_RECEIPTS.json':
  data=path.read_bytes();assert len(data)<20*1024*1024
  artifacts.append({'path':str(path.relative_to(RUN)),'size_bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
dump(RUN/'ARTIFACT_RECEIPTS.json',{'persisted_utc':now,'local_only':True,'artifacts':artifacts})
protocol=json.loads((ROOT/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert json.loads((RUN/'PROGRESS.json').read_text())==json.loads((RUN/'PACKET_DELTA.json').read_text())
assert (AGENT/'STATUS.md').read_text().count('\n')==2
print(json.dumps({'status':'PASS','artifacts':len(artifacts),'run_directory':str(RUN),'statement_sha256':claim['statement_sha256'],'protocol_fields_exact':True},indent=2))
