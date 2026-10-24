from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

run=Path(__file__).resolve().parent.parent
agent=run.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,data):
 (run/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

statement=('For every finite product law Q with marginals q_i and J=sum_i q_i<=1/16, every real sign choice b_S=epsilon_S sqrt(Q(S)) has normalized collision T=H(C_b^2/Z)-log2 Z satisfying abs(T/4-sum_i h2(q_i)+(2+log2(e))*J)<=9*J*sum_i h2(q_i)+15*J^2. All quantities are in bits. With actual spectral Q, B05 activated bent surgery has (T/4-TC)/I ->8/5-log2(e), and (M-T/4)/I ->2+log2(e). Positive-completed addressing and actual full-support one-point-flipped addressing satisfy T/a ->tau where tau=(4e^4-32e+56/e-20/e^2)/(e^4-12e+30/e-13/e^2), TC ->log2(e), M/a ->2 and I/a ->1/2; thus their constant floors are kappa>=tau/2 and c>=4-tau/2. Sparse activation of the full-support flipped addressing family with r=ceil(3log2 a) has I,M->0, H/I->4 and (T/4-TC)/I ->2-log2(e). Frozen exact B05 k=2,4 and positive-completed addressing a=1..4 pass kappa=c=8; a=4 has T/4-TC>77/100 bits. None of these conclusions supplies a universal Boolean lower-divergence payment.')
claim={
 'claim_id':'A036-NORMALIZED-RECOVERY-REPAIR-AND-REFERENCE-GUARDS',
 'version':1,
 'exact_statement':statement,
 'hypotheses':['Universal recovery lemma: normalized signed product-law amplitude, J<=1/16; any phases, zero marginals deleted','Boolean applications: uniform cube, actual product spectral marginals, named B05 and addressing families as defined in REPORT.md','Addressing finite T uses positive completion at spectral zeros; full-support transfer uses the realized negative completion and repriced marginals','Sparse activation uses fresh controls, r=ceil(3log2 a), and the actual changed product reference','All entropy and divergences in bits; TC=M-H; campaign B is erasure, not marginal sum'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
 'contributors':['A036'],
 'proof_source':'REPORT.md Sections 1-8; code/check.py; code/coefficients.py; out/verification.json; out/coefficient_certificate.json',
 'proof_dependencies':[],
 'review_records':[],
 'status':'ANALYTICALLY_PROVED_LOCAL_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],
 'refutes':['Universal zero-price TC>=T/4 for the actual full-support signed product-marginal reference'],
 'first_unproved_line':None,
 'next_consumers':['A037','A038','A039','A040','A064','A088','A094','B08','B20']}
write('CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2',
 'run_id':run.name,
 'stream':'B08',
 'packet_id':'A036',
 'gap_id':'G-A036-NORMALIZED-DIVERGENCE-RECOVERY',
 'attempt_id':'A036-reference-law-divergence-attempt-2',
 'method':'Lead-directed exact B05/addressing contractions, universal near-Dirac reference recovery with paid 9IM+15I^2 error, support/completion and full-support/activation audit',
 'mathematical_delta':'Universal all-phase product-reference recovery error <=9IM+15I^2 for I<=1/16. Exact six-case kappa=c=8 survives; zero-price payment refuted. B05 asymptotic floor 8/5-log2 e; full-support addressing floor tau/2; admitted low-I activation floor 2-log2 e. Universal Boolean lower payment and history reset remain open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT',
 'mathematical_status':'RECOVERY_REPAIR_AND_ROUTE_GUARDS_PROVED_UNREVIEWED; UNIVERSAL_FEI_OPEN',
 'claim_versions_used':[],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
 'source_artifacts':['REPORT.md','code/check.py','code/coefficients.py','out/FROZEN_SPEC.json','out/DERIVATION_CHECKPOINT.md','out/ASYMPTOTIC_CHECKPOINT.md','out/UNIVERSAL_RECOVERY_CHECKPOINT.md','out/verification.json','out/coefficient_certificate.json','out/check_receipt.json','out/source_receipts.json','out/save_receipts.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'In B08 TC restriction ledger on B05 control-first tree, prove or refute a nonreusing source-influence bound for the weighted 9I_h M_h recovery bill plus reference resets and terminal entropy. A088/A094 independently reconstruct the repair.',
 'stagnant_substantive_attempts':0,
 'blockers':['No mathematical access blocker','Universal lower-divergence payment, uncontrolled M, and physical phase/reference reset transport remain unproved','Independent review and supervisor mirror not observed'],
 'packet_ids':['A036']}
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
verify=json.loads((run/'out/verification.json').read_text())
write('out/check_receipt.json',{'commands':['python -X utf8 code/check.py','python -X utf8 code/coefficients.py'],'working_directory':str(run),'exit_codes':[0,0],'six_case_checks_passed':verify['all_assertions_passed'],'pilot_runtime_seconds_diagnostic':verify['runtime_seconds_diagnostic'],'memory_estimate_mb':60,'heavy_job_started':False,'verification_sha256':sha(run/'out/verification.json'),'coefficients_sha256':sha(run/'out/coefficient_certificate.json'),'independent_external_review':False})
sources=[]
paths=[Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B08\STREAM_NOTES.md'),agent/'runs/20261011T214139Z-account05-A036-reference-law-divergence/REPORT.md',Path(r'~\brain_workers\FEI100_20261011\agents\A038\runs\20261011T221733Z-account05-A038-occupancy-term-audit\REPORT.md'),Path(r'~\brain_workers\FEI100_20261011\agents\A040\runs\20261011T225840Z-account05-A040-credit-insufficiency-tests\REPORT.md'),Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
for p in paths:sources.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':'REPORT.md sources section distinguishes actual stage reads and carried context'})
write('out/source_receipts.json',sources)
now=datetime.now(timezone.utc).isoformat()
(agent/'STATUS.md').write_text('STATE: A036 stage 2 saved: universal product-reference recovery error <=9IM+15I^2 for I<=1/16; six exact cases pass constants 8; zero-price collision payment refuted with B05/addressing asymptotic coefficients; review pending; full FEI open.\nNEXT: In B08 TC ledger on B05 control-first tree, pay weighted 9I_h M_h plus actual reference resets once from source influence, retaining terminal entropy; A088/A094 review.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+': Stage 2 followed B08 lead, corrected marginal B to M, and read A038/A040 original reports. Compressed rational contractions verified B05 k=2,4 and addressing a=1..4, all assertions passed in '+str(verify['runtime_seconds_diagnostic'])+' seconds. Proved universal recovery error <=9IM+15I^2 and addressing/B05/activated full-support coefficient guards. No pure point-defect tensor repetition. Saved all protocol artifacts; next is the state-dependent bill in the shared TC tree ledger.\n')
(agent/'LEARNED.md').write_text('''# A036 durable facts

Notation: M=sum_i h2(Inf_i) is marginal entropy; campaign B=sum_i H(S_i|S_-i) is erasure. Stage 1 used B for M; this is only a naming correction, not a theorem correction.

Stage 1: on disjoint point-defect tensors, actual product-marginal Q and actual same-sign amplitudes give TC>=T/4-8I, M<=T/4+8I, and TC>=[M-4I]_+. Raw L is not tensor additive; T=H(v/Z)-log2 Z is. Z=319/256 on the three-bit point defect. This is calibration, not full FEI.

Stage 2 universal recovery: for ANY normalized signed product reference with J=sum marginals<=1/16, abs(T/4-M+(2+log2 e)J)<=9JM+15J^2. It uses a dominant all-empty packet, singleton correlations, an unsigned higher-shift cap, and the exact normalizer. No Booleanity is needed. When J,M->0 recovery is sharp; the lower divergence payment is still unpaid and FEI-strength. The 9JM bill cannot be absorbed dimension-free without controlling M.

B05 k=2,4: exact spectra and collision contractions pass kappa=c=8. Recovery c=4 already fails at k=2. As k->infinity H/I->18/5 and (T/4-TC)/I->8/5-log2 e>0, while (M-T/4)/I->2+log2 e. The positive limit is an eventual zero-price failure, not divergence of H/I.

Addressing: Q(supp P)=(1-1/N)^(N-1), K_shape=0, TC=K_supp. Supported subnormalized b gives T=-2log Q(supp P); conditioned b gives T=0; positive zero completion instead gives T/a->tau=(4e^4-32e+56/e-20/e^2)/(e^4-12e+30/e-13/e^2), about4.7767825426772. Do not conflate references. The completed zero-price failure is certified at a=4 with gap>0.77 bits.

Actual full-support all-zero physical point flips preserve the addressing completed slope via the reusable bound |T_b-T_c|<=h2(rho)+n rho+rho/ln2, rho=(||b||1+||c||1)^2||b-c||2<=1/2. The l1 price is essential. Addressing requires kappa>=tau/2 at large I, but sparse activation into full-support I,M->0 reprices this floor to2-log2 e. Reference changes under hardness embeddings must be tracked.

Exact outputs: rational log/exponential intervals, outward rational-grid serialization. Family spectra and squared correlations can be rational even when amplitude coordinates contain radicals; factor each shifted sqrt(q(1-q)) before contracting phase tables.
''',encoding='utf-8')
claim_fields={'claim_id','version','exact_statement','hypotheses','statement_sha256','contributors','proof_source','proof_dependencies','review_records','status','supersedes','refutes','first_unproved_line','next_consumers'}
progress_fields={'protocol_revision','run_id','stream','packet_id','gap_id','attempt_id','method','mathematical_delta','deliverable_status','mathematical_status','claim_versions_used','claims_created_or_changed','source_artifacts','next_consumers','next_action','stagnant_substantive_attempts','blockers','packet_ids'}
assert set(claim)==claim_fields;assert set(progress)==progress_fields
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert (run/'REPORT.md').read_text(encoding='utf-8').rstrip().splitlines()[-1].startswith('**Universal bridge:**')
files=[]
for p in sorted(run.rglob('*')):
 if p.is_file() and p.name!='save_receipts.json':
  assert p.stat().st_size<20*1024*1024
  files.append({'path':str(p.relative_to(run)),'bytes':p.stat().st_size,'sha256':sha(p)})
write('out/save_receipts.json',{'saved_at_utc':now,'run_directory':str(run),'files':files,'protocol_field_sets_checked':True,'delta_matches_progress':True,'universal_bridge_last_paragraph_checked':True,'all_files_under_20mb':True,'independent_review':'PENDING','supervisor_mirror':'NOT_OBSERVED'})
print(json.dumps({'saved_at_utc':now,'files':len(files)+1,'protocol_fields_checked':True,'universal_bridge_last_paragraph_checked':True,'all_files_under_20mb':True}))
