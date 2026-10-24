from pathlib import Path
import hashlib,json,datetime

RUN=Path(__file__).resolve().parents[1]
ROOT=RUN.parents[1]
TEAM=ROOT.parents[1]
SHARED=Path(r'~\mop_fei100\reports\fei-2026-10-11')
def write(name,obj): (RUN/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def digest(statement,hypotheses):
    return hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest()
old=ROOT/'runs'/'20261011T221934Z-account05-A053-near-tensor-perturbations'
lead=TEAM/'claude'/'B11'/'runs'/'20261011T230100Z-claude-B11-block-descent-recentring'
a055=TEAM/'agents'/'A055'/'runs'/'20261011T230118Z-account05-A055-extremal-obstruction-referee'
a052=TEAM/'agents'/'A052'/'runs'/'20261012T003906Z-account05-A052-critical-source-structure'
paths=[TEAM/'BOARD.md',TEAM/'claude'/'B11'/'STREAM_NOTES.md',SHARED/'EXECUTION_PROTOCOL.json',SHARED/'CLAIM_REGISTRY.json',SHARED/'PACKET_STATUS.json',ROOT/'STATUS.md',ROOT/'LEARNED.md',old/'CLAIMS.json',old/'REPORT.md',old/'HIDDEN_TENSOR_DIAGNOSTIC.md',lead/'REPORT.md',lead/'CLAIMS.json',a055/'EMBEDDING_PROOF.md',a055/'REVIEW_A053.md',a055/'CLAIMS.json',a052/'SINGLETON_COLLAPSE.md']
sources=[]
for p in paths:
    b=p.read_bytes()
    sources.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'scope':'Source-bound relevant proof/coordination text; no remote readback'})
write('out/SOURCE_MANIFEST.json',sources)
hyp=['Uniform physical cube; Boolean signs; entropy in bits; n>=2','One-point surgery at an arbitrary vertex; proper block family in the fixed named ambient coordinates','For two-sided quotient continuity, all seed influences >=kappa>2^(1-n); one-sided transfer only needs the selected I_A>2|A|2^-n','E_0=E_1=0,E_2=2,E_3=3,E_m=h2(2^(1-floor(m/2)))+m*2^(1-floor(m/2)) for m>=4','No full FEI claim; exact-product R6 is not refuted; no automatic criticality inheritance']
statement='For g=f-2f(v)*1_v, p=2^-n and a=|A|, |L_A(g)-L_A(f)|<=eta_(n,a)=E_n+2^-a E_(n-a) and |I_A(g)-I_A(f)|<=2ap. If I_A(f)>2ap then phi(g)<=[L_A(f)+eta]/[I_A(f)-2ap]. If every seed influence >=kappa>2p, |phi(g)-phi(f)|<=max_(1<=a<n) eta/[a(kappa-2p)]+4p/[kappa(kappa-2p)] and |R(g)-R(f)|<=E_n/[n(kappa-2p)]+2p/[kappa(kappa-2p)]; a seed slack exceeding their sum transfers phi(g)<R(g). Whole-channel continuity also holds with a(delta_P+delta_Q)+h2(delta_P)+h2(delta_Q), where delta_Q is the edited child spectral TV weighted by 2^-a. The point-defect ratios R_n=H(1-2*1_0)/(2n2^-n) strictly increase to 4. For the exact tensor seed F_n=chi_[n] and its one-point surgery G_n=chi_[n](1-2*1_0), every n>=2 has phi(G_n)>R(G_n), with residual L_A-R(G_n)I_A=2(n-a)2^-n(R_n-R_(n-a))>0 and 1<phi(G_n)/R(G_n)<=n/(n-1). Both values are asymptotic to 8*2^-n. For n>=3 all averaged own-ratio block tests pass although the edited two-bit descendant has ratio 2>R(G_n).'
claim={'claim_id':'A053-DESCENT-CONTINUITY-AND-EQUALITY-BOUNDARY','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':digest(statement,hyp),'contributors':['A053/account05'],'proof_source':'CONTINUITY_PROOF.md sections 1-6; NEAR_TENSOR_DESCENT.tex; code/check_descent.py; out/EXACT_CHECK.json; out/PARITY_CERTIFICATES.json','proof_dependencies':[],'review_records':[],'status':'SOURCE_COMPLETE_ANALYTIC_PROOF_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':['Unversioned inference in B11 STREAM_NOTES.md v2 A053 target: one-point continuity makes all near-tensors inherit phi<=H/I from exact-product R6'],'first_unproved_line':None,'next_consumers':['B11-lead','A051','A052','A054','A055','A090','A094','B20']}
write('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B11','packet_id':'A053','gap_id':'G-A053-CRITICAL-QUANTITATIVE-SEPARATION','attempt_id':'A053-near-tensor-2','method':'Block-weighted entropy continuity; common-mixture joint-channel bounds; influence-denominator-aware quotient transfer; analytic point-defect monotonicity; exact parity-surgery orbit certificates','mathematical_delta':'Proved explicit phi continuity and strict-slack transfer; refuted exact own-ratio inheritance at equality by an all-dimensional one-point perturbation of parity products; separated every averaged block test from individual descendant tests','deliverable_status':'COMPLETE_LOCAL_ARTIFACT_REVIEW_PENDING','mathematical_status':'CONTINUITY_TARGET_PROVED_WITH_SCOPE_REPAIR_FULL_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':['A053-DESCENT-CONTINUITY-AND-EQUALITY-BOUNDARY@1'],'source_artifacts':['REPORT.md','CONTINUITY_PROOF.md','NEAR_TENSOR_DESCENT.tex','LEAD_SCOPE_CORRECTION.md','code/check_descent.py','out/FROZEN_SPEC.json','out/FROZEN_SPEC_FINAL.json','out/EXACT_CHECK.json','out/PARITY_CERTIFICATES.json','out/TIMEOUT.json','out/SOURCE_MANIFEST.json'],'next_consumers':['B11-lead','A051','A052','A054','A055','A090','A094','B20'],'next_action':'At a fixed positive descent price K, retain additive surgery error and individual child deficits; test a quantitative factor-cut slack or healthy-denominator hypothesis on the existing higher-ratio NAND witnesses, with joint channel J_A rather than summed beta pricing','stagnant_substantive_attempts':0,'blockers':['Independent review and supervisor adoption pending','One completed exact pilot; repeat execution reached the internal runtime stop without changing completed certificates'],'packet_ids':['A053']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
protocol=json.loads((SHARED/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all(x in report for x in protocol['required_per_run']['report_fields'])
exact=json.loads((RUN/'out'/'EXACT_CHECK.json').read_text(encoding='utf-8'))
assert exact['status']=='PASS' and exact['proper_block_checks']==3584
ckpath=RUN/'code'/'check_descent.py'
write('out/VALIDATION_RECEIPT.json',{'completed_pilot':exact,'helper_sha256':hashlib.sha256(ckpath.read_bytes()).hexdigest(),'helper_changed_after_completed_pilot':False,'repeat_attempt':'Runtime guard fired at 55 seconds; no completed certificate overwritten','timeout_counts':json.loads((RUN/'out'/'TIMEOUT.json').read_text(encoding='utf-8')),'initial_spec_omission':'Six fixed scalar strict-slack checks were in helper but not the initial prose spec; disclosed and fixed in final accounting before replay','finite_checks_not_all_dimension_proof':True})
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        b=p.read_bytes();assert len(b)<20_000_000
        receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    p=ROOT/name;b=p.read_bytes()
    receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
write('out/PERSISTENCE_RECEIPTS.json',{'saved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'protocol_fields_exact_match':True,'files':receipts,'independent_review':'PENDING','supervisor_adoption':'PENDING','remote_mirror':'NOT_VERIFIED'})
print(json.dumps({'status':'PASS','source_files':len(sources),'saved_files':len(receipts),'protocol_fields':'EXACT_MATCH','assertions':exact['assertions'],'claim_sha256':claim['statement_sha256']},indent=2))
