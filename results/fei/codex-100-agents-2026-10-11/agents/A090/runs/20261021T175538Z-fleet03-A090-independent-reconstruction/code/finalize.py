from pathlib import Path
import hashlib, json
from datetime import datetime, timezone

run=Path(__file__).resolve().parents[1]
own=run.parents[1]
team=own.parents[1]
campaign=Path(r'math-open-problems/reports\fei-2026-10-11')
supplement=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
now=datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,t):
    assert p.resolve().is_relative_to(own.resolve())
    with p.open('w',encoding='utf-8',newline='') as f:f.write(t)
def save(p,data):write(p,json.dumps(data,ensure_ascii=False,indent=2)+'\n')
check=json.loads((run/'out/CHECK.json').read_text(encoding='utf-8'))
assert check['status']=='PASS' and check['assertions']==286705
assert check['checker_sha256']==sha(run/'code/check.py')
assert check['certified_original_bank_surplus_lower']=='111/200'
assert check['elapsed_seconds']<60
protocol=json.loads((campaign/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
a001=team/'agents/A001/runs/20261014T074909Z-fleet05-A001-quantifier-audit/CLAIMS.json'
a096=team/'agents/A096/runs/20261014T094929Z-fleet05-A096-live-gap-ledger/CLAIMS.json'
a097=team/'agents/A097/runs/20261014T050248Z-fleet05-A097-cross-route-transfer/CLAIMS.json'
sources=[]
def source(p,scope):
    sources.append({'path':str(p),'sha256':sha(p),'review_scope':scope})
for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
    source(campaign/name,'Protocol read in full; other campaign documents inspected at relevant B18/A090 and C019/C024 sections.')
source(team/'BOARD.md','Current board and relevant handoffs')
source(team/'claude/B18/STREAM_NOTES.md','Read in full; productive own next gap takes dispatch priority over old census')
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    source(supplement/name,'Relevant introductory scope and mathematical sections; not blanket re-review')
source(supplement/'sources/ERASURE_REDUCTION.md','Read in full; sections 1 and 4 supply original restriction definitions')
for name in ['threshold_paper_38pp.txt','threshold_paper_29pp_earlier_version.txt','percolation_spectral_pivotal_entropy_30pp.txt','percolation_spectral_pivotal_entropy_31pp_other_version.txt']:
    source(team/'context'/name,'Explicit cp1252 decoding; introduction/targeted locators; current threshold section8.2/Prop8.6 read directly; other results not proof dependencies')
for p in [a001,a096,a097]:source(p,'Theorem statements only; producer derivations/checkers not used')
save(run/'SOURCE_RECEIPTS.json',{'saved_at':now,'sources':sources,'scope_warning':'Hashing source bytes is not an independent review of all their contents.'})
def dependency(p,cid,scope):
    c=next(x for x in json.loads(p.read_text(encoding='utf-8')) if x['claim_id']==cid)
    return {'claim_id':cid,'version':c['version'],'source':str(p),'source_file_sha256':sha(p),'declared_statement_sha256':c['statement_sha256'],'observed_UTF8_statement_sha256':hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest(),'scope':scope}
d1=dependency(a001,'A001-NEUTRAL-CORE-ACTUAL-DATA-TRANSFER','Six quantitative payment bounds only; undefined shadow comparison unreviewed')
d2=dependency(a096,'A096-PAID-FLOOR-NO-RESET-HISTORY','Abstract identity fully reconstructed; A097 application conditional on its supplied floor')
d3=dependency(a097,'A097-NEGATIVE-CELL-FLOOR-SOURCE-BANK','Statement-only conditional premise; floor proof not independently reconstructed')
report=str(run/'REPORT.md')
common={'version':1,'hypotheses':[],'contributors':['A090'],'proof_source':{'path':report,'checker':str(run/'code/check.py'),'output':str(run/'out/CHECK.json')},'proof_dependencies':[],'review_records':[],'supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A001','A004','A081','A086','A094','A096','A097','A099','B20']}
def claim(cid,statement,**extra):
    c=dict(common,claim_id=cid,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest())
    c.update(extra); return c
claims=[
claim('A090-NO-RESET-CONTINUATION-INDEPENDENT-REVIEW',
      'For every finite actual uniform Boolean restriction and normalized reference Q positive on its squared Fourier support, CE(P,Q)=B_j+avg_s CE(P_s,Q_minus_j)+R_j, where Q_minus_j is the spectral marginal and R_j is the full conditional occupancy KL. Hence every finite outcome-adaptive physical tree with only these inherited references obeys erasures plus complete expected terminal H+D plus accumulated conditional KL equals original CE. The A096 constant-child witness has actual influence zero and inherited CE=log2(8/5)>0. The stated A097 application follows conditionally from its supplied original root CE bound; no arbitrary-core floor or paid fresh reset follows.',
      hypotheses=['Finite actual uniform Boolean signs and fresh physical coordinate queries','Normalized complete reference, finite CE, all empty/reference-only mass retained','Finite possibly adaptive stopping tree; reference only marginalized','A097 floor premise required only for the conditional priced corollary'],
      proof_dependencies=[d2,d3],status='INDEPENDENT_SCOPED_RECONSTRUCTION_HOLDS_CONDITIONAL_APPLICATION_RETAINED',
      review_records=[{'reviewer':'A090','timestamp':now,'method':'Statement-only analytic reconstruction plus independent integer spectra, prime-log cancellation, rigorous interval signs and adaptive tree checks','producer_derivation_used':False,'substantive_repair_contributed':False,'scope':'A096 identity, no-reset telescope and constant-child obstruction; priced application conditional'}]),
claim('A090-NEUTRAL-SIX-QUERY-PAYMENT-REVIEW',
      'For the exact nine-bit F=b+1_origin(Maj3-1), where b is positive iff its first three of six data bits are zero, all six data-first/majority-next stopped policies satisfy the numerical rational-log payment and frozen-terminal-escrow inequalities stated in A001-NEUTRAL-CORE-ACTUAL-DATA-TRANSFER@1. Both terminal spectra and the actual encoder erasure are retained. This review does not accept the separate comparison with an undefined pending shadow-plus-inherited reservation.',
      hypotheses=['Specified nine-bit Boolean truth table','Six labeled first data queries then fixed majority coordinate order','Incoming actual signed amplitudes and matching squared reference','Original core quota 4I0=3; no unrecorded previously paid cost'],
      proof_dependencies=[d1],status='PARTIAL_SOURCE_REVIEW_QUANTITATIVE_PAYMENT_HOLDS',
      first_unproved_line='The actual Maj3 encoder erasure differs positively from the pending shadow-plus-inherited reservation: the statement gives no formula defining that reservation.',
      review_records=[{'reviewer':'A090','timestamp':now,'method':'Independent truth-table restriction/Walsh implementation and direct root character sums; exact prime-log margins','verdict':'Six payment conclusions HOLDS; shadow-comparison clause UNRECONSTRUCTED','substantive_repair_contributed':False}]),
claim('A090-NEUTRAL-ALL-TREE-SAME-REFERENCE-BANK',
      'For the specified nine-bit F=b+1_origin(Maj3-1), the exact root entropy is 385/32-(2401/1024)log2(7)-(1575/2048)(log2(3)+log2(5))<489/200. With initial Q=P_F and child references obtained only by marginalization, every finite adaptive stopping tree satisfies sum_v w_v B_v+sum_leaf w_leaf CE(P_leaf,Q_leaf)<=H(F)<489/200<3=4I0. Thus one original core quota pays every no-reset continuation, all executed erasure-prefix charges within that account and full terminal KL, leaving more than111/200 bits. This does not cover arbitrary supplied Q, unrelated pre-existing costs or prescribed fresh floors.',
      hypotheses=['Specified actual nine-bit fixture; six data bits and three fresh majority bits','Matching initial complete squared reference accompanied by true Fourier phases','Finite outcome-adaptive tree querying only fresh physical coordinates','No resets and no unrecorded extra old debit'],
      proof_dependencies=[d2],status='AUTHOR_PROOF_AND_EXACT_CERTIFICATE_PENDING_INDEPENDENT_REVIEW',
      review_records=[{'reviewer':'A086/A094','verdict':'PENDING; A090 is the contributor to this corollary'}])]
fields=set(protocol['required_per_run']['claim_fields'])
assert all(set(c)==fields for c in claims)
save(run/'CLAIMS.json',claims)
next_action='A097/A094 supply one weak non-flat physical query with prescribed fresh child references, actual old debit and remaining original bank; certify signed avg reset tax against conditional KL refund and that same unused reserve. A086/A094 review all-tree fixture corollary.'
progress={
 'protocol_revision':protocol['revision'],'run_id':run.name,'stream':'B18','packet_id':'A090',
 'gap_id':'C019-C024-PAID-FRESH-FLOOR-ADMISSION','attempt_id':'A090-stage6-independent-no-reset-reconstruction',
 'method':'Theorem-statement-only reconstruction; independent integer Walsh/character sums; exact rational prime-log identities and atanh intervals; no producer derivation imported',
 'mathematical_delta':'A096 no-reset conservation independently reconstructed; six A001 quantitative policies independently certified; same fixture now has every adaptive no-reset tree paid by original quota3 with >111/200 unused margin and full terminal KL. Undefined source shadow comparison remains unreviewed; universal paid reset remains open.',
 'deliverable_status':'COMPLETE_LOCAL_SCHEMA_AND_READBACK_VERIFIED',
 'mathematical_status':'FULL_FEI_OPEN_SCOPED_PROOF_AND_EXACT_CERTIFICATE_NEW_COROLLARY_REVIEW_PENDING',
 'claim_versions_used':[d1,d2,d3],
 'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':1,'status':c['status']} for c in claims],
 'source_artifacts':[str(run/x) for x in ['REPORT.md','CLAIMS.json','SOURCE_RECEIPTS.json','code/check.py','out/CHECK.json','out/FROZEN_SPEC.json','out/LEAN.txt']],
 'next_consumers':common['next_consumers'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Universal fresh-reference admission from the same unused bank unproved','A001 pending shadow reservation undefined in supplied statement; comparison unreviewed','Lean RUNTIME_UNVERIFIED after60s; no formal pass','Supervisor mirror/brain adoption and independent corollary acceptance unverified'],
 'packet_ids':['A090']}
expected={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
save(run/'PROGRESS.json',progress);save(run/'PACKET_DELTA.json',progress)
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
status='STATE: Stage 6 complete: A096 no-reset identity and six A001 payment bounds independently HOLD; same fixture ALL adaptive no-reset trees paid once with full terminal KL and >111/200 reserve;286705 exact assertions PASS; shadow comparison unreviewed;FEI OPEN.\nNEXT: A097/A094 expose one prescribed weak non-flat fresh-reference reset with SAME old debit/unused bank; A086/A094 review all-tree corollary; require formula for A001 shadow reservation.\n'
write(own/'STATUS.md',status)
for file,text in [
 ('WORKLOG.md',f'\n{now} — Stage6, fleet03: statement-only A096 channel/no-reset reconstruction; independently replayed all278 truth tables through n3 with three references, six neutral9-bit policies and direct512 root character sums. Final286705 assertions PASS in{check["elapsed_seconds"]:.3f}s. General all-tree corollary on the SAME matching fixture costs<489/200 versus original3, full terminal CE retained. A001 undefined shadow reservation comparison left unreviewed. Lean attempt admitted by memok but RUNTIME_UNVERIFIED at60s, not a pass. Fresh-floor universal tax remains unpaid. Local protocol artifacts saved; no external adoption claimed. NEXT: {next_action}\n'),
 ('LEARNED.md','\nStage6 durable fact: for any finite actual Boolean physical tree with Q inherited solely by spectral marginalization, CE_root = sum w B + E CE_terminal + sum w R, R the full occupancy-conditional KL>=0. Actual child P is recomputed from signed amplitudes, NOT obtained by marginalizing parent P on an outcome. Normalized reference-only support stays in each conditional denominator. For the neutral six-data-bit AND3 point edit by Maj3, H=385/32-2401/1024 log2(7)-1575/2048 log2(15)<489/200, so original quota3 pays EVERY adaptive no-reset history, full terminal H+D and all its executed-prefix erasures, leaving>111/200. A prescribed reset adds avg[CE(P_s,Qnew_s)-CE(P_s,Qold_marginal)] and needs payment from R plus a named unused bank. A cheap universal root reference is FEI-equivalent. A001 shadow-reservation positivity cannot be independently reviewed from its statement without the reservation formula. Lean runtime timeout leaves formal status UNVERIFIED.\n')]:
    with (own/file).open('a',encoding='utf-8',newline='') as f:f.write(text)
text=(run/'REPORT.md').read_text(encoding='utf-8')
assert all('## '+x in text for x in protocol['required_per_run']['report_fields'])
assert text.rstrip().split('\n')[-1].startswith('**Universal bridge:**')
assert len((own/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(run/'out/ARTIFACT_RECEIPTS.json',{'verified_at':now,'status':'LOCAL_READBACK_AND_PROTOCOL_SCHEMA_PASS','artifacts':receipts,'remote_adoption':'UNVERIFIED','new_independent_review':'PENDING'})
print(json.dumps({'status':'LOCAL_COMPLETE','claims':len(claims),'exact_assertions':check['assertions'],'files_hashed':len(receipts),'run':str(run),'status_two_lines':True},indent=2))
