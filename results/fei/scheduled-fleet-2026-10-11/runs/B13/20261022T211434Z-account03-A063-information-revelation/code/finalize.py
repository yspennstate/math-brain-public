from pathlib import Path
import json,hashlib,time,subprocess,os,sys,runpy
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
def wr(p,s):p.write_text(s,encoding='utf-8',newline='\n')
def js(p,x):wr(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
res=json.loads((R/'out/CHECK_RESULTS.json').read_text(encoding='utf-8'));assert res['status']=='PASS'
runpy.run_path(str(R/'code/audit.py'),run_name='__main__');audit=json.loads((R/'out/AUDIT.json').read_text(encoding='utf-8'));assert audit['status']=='PASS'
lean={'status':'NOT_ATTEMPTED','scope':'integer linear KL-account implication only; not the entropy theorem'}
try:
 admission=subprocess.run([sys.executable,'-X','utf8','-B',r'~\brain_workers\FEI100_20261011\tools\memok.py'],capture_output=True,text=True,encoding='utf-8',timeout=30)
 lean['compute_admission_exit']=admission.returncode;wr(R/'out/MEMOK.txt',admission.stdout+admission.stderr)
 if admission.returncode==0:
  env=os.environ.copy();env['LEAN_CHECK_DIR']=str(R/'out/lean')
  stmt='example (A E O K TC : Int) (h : A = E + O + K) (he : 0 <= E) (hk : 0 <= K) : O + TC - A <= TC := by omega'
  lean['statement']=stmt
  lc=subprocess.run([sys.executable,'-X','utf8','-B',r'~\.claude\dreaming\lean_check.py','--stmt',stmt,'--core','--timeout','20','--json'],capture_output=True,text=True,encoding='utf-8',env=env,timeout=40)
  wr(R/'out/LEAN_OUTPUT.txt',lc.stdout+lc.stderr);lean.update({'exit_code':lc.returncode,'status':'CHECKER_RETURNED_READ_RECEIPT' if lc.returncode==0 else 'RUNTIME_OR_CHECK_UNVERIFIED'})
 else:lean['status']='ADMISSION_HELD_NO_LEAN_JOB'
except subprocess.TimeoutExpired:lean['status']='BOUNDED_ATTEMPT_TIMEOUT_NO_FORMAL_CLAIM'
js(R/'out/LEAN.json',lean)
now=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
statement='For every n>=2, let F=-1 on x=0,a=1, v_n on x=1,b=1, +1 otherwise, with v_n=1-2*1[z=0]. Query a, at least one distinct private z bit in each branch, then arbitrary further adaptive private queries/stopping while x,b remain unqueried. Propagate any supported original normalized reference using the same actual common kernel including fair source-zero rows, without intermediate reset. At the single final product reset D=O+mean(TC_terminal)-A satisfies [D]_+<3/10 bits. The SAME original twisted-a=1-lineage reserve of one global bit pays prior1/4 plus [D]_+, retaining>9/20 at every allowed cut, with both complete terminal laws retained.'
claim={'claim_id':'A063-ORIGINAL-REFERENCE-RARE-HISTORY-PAYMENT','version':1,'exact_statement':statement,'hypotheses':['uniform actual Boolean fixture','n>=2','x,b unqueried','at least one private query per a branch','distinct private queries; arbitrary adaptive orders/stopping','supported original normalized reference and fair source-zero extension','single delayed final conversion; no intermediate resets','one prior global1/4 debit from SAME original lineage allocation','bits'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A063'],'proof_source':['PROOF.md','code/check.py','out/CHECK_RESULTS.json','code/audit.py','out/AUDIT.json'],'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROOF_WITH_EXACT_BASE_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A039','A037','A064','A087','A094','A097']}
js(R/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B13','packet_id':'A063','gap_id':'G-R-MISMATCH','attempt_id':'A063-original-occupancy-rare-history-v1','method':'consume A039 mixed query; bound final conversion by terminal TC; preserve original twisted lineage; exact scalar bases and analytic tail','mathematical_delta':'ALL n>=2 rare cores and private histories under ORIGINAL reference: [D]+<3/10, original global1 reserve after prior1/4 retains>9/20; full terminals retained. Universal constant unchanged.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUTHOR_PROOF_PENDING_REVIEW; FULL_FEI_OPEN','claim_versions_used':['A039 stage5 original-reference final-frontier ledger, reconstructed','A037 20261021 product-source result used as context only'],'claims_created_or_changed':[claim['claim_id']+'@1'],'source_artifacts':['PROOF.md','code/check.py','code/audit.py','out/FROZEN_SPEC.json','out/CHECK_RESULTS.json','out/AUDIT.json','out/LEAN.json','out/SOURCE_RECEIPTS.json'],'next_consumers':claim['next_consumers'],'next_action':'Exercise one product reset from ORIGINAL occupancy source on an unequal nonconstant-child core, carrying SAME remaining reserve, prior1/4, old debits and both complete terminals through next mixed query; A087/A094 review.','stagnant_substantive_attempts':0,'blockers':['Universal arbitrary-core eligibility OPEN','Intermediate exercised resets not covered','Brain wake attachment integrity degraded by lock timeouts; owner alerted','Independent review and private mirror adoption unobserved'],'packet_ids':['A063']}
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
report=f'''# A063: original-reference payment after a mixed query

Full FEI remains OPEN. The biased rare-core continuation uses the original reference and one original twisted-lineage allocation. Its extra final conversion costs<3/10 bit and leaves>9/20 bit after prior1/4. Rung: author proof with exact finite base certificates, pending independent review. The full entropy theorem is not claimed Lean-checked.

## exact target, quantifiers, hypotheses and units

{statement}

A039's ORIGINAL completed occupancy reference is included. Supported means positive on source support. Source-zero reference-only rows use the declared fair extension. No intermediate reset occurs. Both terminal entropy H and inherited/product KL remain explicit. The reserve is the original a=1-lineage allocation, rather than a sum of renewed descendant banks.

## sources actually read, revisions and theorem locators

Complete execution protocolv2; refreshed campaign README/status/registries/actions and plan interfaces, supplement navigation, BOARD snapshot2026-10-22 21:16UTC and B13 leadv2; own two substantive prior reports, STATUS and LEARNED. Prior A063 supplies the completed chain rule/refund/MU baseline, not new claims here. A039 stage5 REPORT/PROOF equation(1) and mixed.py supply the actual ORIGINAL occupancy fixture. A037 20261021T220645Z REPORT supplies the exercised product-source comparison and reserve context; its changed source is not imported. A064 20261021T151814Z REPORT supplies finite all-history context. The present proof reconstructs the KL identity and reserve directly.

Read supplemental erasure, block-restriction and isospectral-splicing interfaces. Prior baseline campaign intake is inherited. Paper refresh is interface-focused: threshold38pp Proposition8.6 equations75-79, percolation30pp Lemma2.1 equations10-11, and introductions/scope in earlier versions. These texts require explicit cp1252 decoding after UTF-8 fails. No source was changed and no new paper theorem is a premise. Source hashes and scopes are recorded. Session wake attachment-lock failures were reported before relying on notes; math recall was WEAK MATCH and supplies no theorem.

## complete derivation or exact first unsupported line

PROOF.md is the full derivation. With original source KL A, accumulated conditional erasure E, reference-outcome KL O and expected terminal inherited KL K, A=E+O+K. At the final product conversion D=O+TC_end-A<=TC_end. O is a reference-outcome KL, not physical branch entropy or spectral-erasure information. The proof uses E,K>=0, rather than identifying those different quantities.

Every active private descendant is a point defect or its x-character twist on m>=2 variables. Inactive descendants are constants or the x character. Exact scalar bases m2..7 and an analytic decreasing tail m>=8 prove TC_m<3/5. At least one private query per a branch leaves total active reach<=1/2; later branching preserves/decreases it. Thus TC_end<3/10 for EVERY admitted adaptive history/stopping cut. The ORIGINAL twisted lineage has S4>=2 conditionally at every cut: m2 exact equality, m>=3 from H_m<4m2^(1-m), inactive character S4=4. Its global allocation is1. Prior1/4 plus [D]+ leaves>9/20. All complete terminal H and KL bills stay in the account; no bank is renewed.

First unsupported universal line: arbitrary unequal nonconstant-core eligibility, or an actually exercised intermediate reset under the ORIGINAL occupancy source, with the same old debits and both full terminals. Querying x destroys the reserve in the explicit inactive-character control. The result does not cover that query or an arbitrary Boolean function.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json preceded computation. Commands relative to this run: python -X utf8 -B code/check.py --pilot; python -X utf8 -B code/check.py; python -X utf8 -B code/audit.py. Frozen domain n2..4: all29 first-private policies; four complete continuation trees through n2,n3;11 scalar dimensions m2..12. Main uses exact integer Walsh/physical edge counts, Fraction kernels and source-pinned A039 rational outward root/log intervals. Main: {res['checks']} assertions PASS, {res['two_query_policies']} policies, {res['continuation_frontiers']} continuation frontiers, runtime{res['runtime_seconds']:.6f}s. Full terminal H,TC, inherited KL, rootA,E,O and remaining bank are retained per checked frontier.

A separate implementation imports no campaign helper: literal character sums and an independent rational atanh series with explicit remainder. Audit: {audit['checks']} assertions PASS in{audit['runtime_seconds']:.6f}s. It checks scalar bases, twist spectra, terminal costs, necessity of the first-private TC reduction, an x-query reserve countercontrol and625 signed integer packet identities including zero rows. This is an independent implementation by A063, not external review. The analytic tail supplies the infinite quantifier.

The first pilot stopped at a rounded boundary S4=2. The repaired checker accepts this boundary only when the exact prime-log expression S4-2 cancels identically; otherwise it requires a separated rigorous interval lower bound. out/VALIDATION_REPAIR.json preserves the failure. A separate draft artifact writer failed at nested string quoting before writing protocol files; it made no mathematical decision and was replaced. No floating sign or interval-overlap sign certificate is used.

One bounded core-Lean attempt targets ONLY the integer linear consequence A=E+O+K,E>=0,K>=0 => O+TC-A<=TC; fresh admission and disposition are in out/LEAN.json. No formal certificate for entropy is claimed. Runtime failure/admission hold does not raise the formal rung. Main estimate140MB, below300MB; no heavy/GPU/detached job, dimension escalation, git, mail, deletion or shared research mutation. No other work was stopped.

## proof dependencies and changed downstream conclusions

Self-contained finite KL chain rules, point-spectrum formulas and elementary entropy inequalities, with exact scalar bases; no unreviewed universal premise. A039/A037 interfaces are credited and reconstructed. This is one scoped application within the existing packet, not a broad universal candidate. A039's biased rare-core NEXT is now paid without changing to A037's product reference, but only for a SINGLE delayed final reset. A037/A064/A097 must preserve that restriction. Physical one-bit entropy and information refund do not substitute for the reference account. No universal FEI constant changes.

## one next mathematical action and independent reviewer

Exercise one product reset from the ORIGINAL occupancy source on an unequal nonconstant-child core, then carry the same remaining allocation through its next mixed query with prior1/4, old conversion debits and both terminals. A087 should reconstruct the KL/active-reach proof; A094 should audit the all-m bounds and original-bank ownership. No messages were sent.

## actual persistence receipts or precise save blocker

The four protocol files, PROOF.md, frozen spec, main/audit code and outputs, pilot receipt, repair provenance, source hashes and bounded Lean disposition are saved locally. out/PERSISTENCE.json verifies exact protocol keys, statement digest, matching progress/delta, report fields, sizes and two-line status. Research artifact writes stay in A063. Supervisor copying, private mirrors, brain ingestion, downstream adoption and independent acceptance remain unobserved.

Universal bridge: This advances C024 history transfer and C019 stopping-tree payment on the team's existing actual mixed-query fixture: ALL n>=2 biased rare cores carry their ORIGINAL reference through arbitrary private histories with one delayed final conversion, cost<3/10, and retain>9/20 of the SAME original global1 allocation after prior1/4 and both complete terminals. Universal FEI improvement is zero. Arbitrary-core eligibility and intermediate exercised resets remain unpaid. NEXT tests that exact source/reset gap on an unequal nonconstant-child core, rather than repeating refund-only or unrelated class searches.
'''
wr(R/'REPORT.md',report)
base=R.parents[1]
wr(base/'STATUS.md','STATE: A063 stage saved: ORIGINAL-reference rare cores ALL n>=2/private histories paid<3/10; SAME original1 bank after prior1/4 retains>9/20; exact checks PASS; review pending; FEI OPEN.\nNEXT: A087/A094 review; exercise ORIGINAL occupancy-source reset on unequal nonconstant-child core, carry SAME remaining bank/prior1/4 and both full terminals through next mixed query.\n')
for name,entry in [('WORKLOG.md',f'\n{now}: Original-reference rare-core continuation; all-n delayed-reset proof with D<=terminal TC<3/10, prior1/4 and original bank1 leaves>9/20. Main{res["checks"]}/audit{audit["checks"]} PASS. Rounded equality repaired by exact formal cancellation; writer quoting failure preserved. Full FEI OPEN; exercised-reset extension/review pending.\n'),('LEARNED.md','\nA039 rare fixture v_n=1-2*1[z=0], a then >=one private query per branch, arbitrary subsequent private queries/stopping, x,b unqueried: under SAME supported original reference with no intermediate reset, A=E+O+K gives final extra debit D=O+TC-A<=TC. Point-defect TC_m<3/5 for all m>=2; active reach<=1/2 gives [D]+<3/10. Original twisted a=1 lineage S4>=2 conditionally always; global bank1 after prior1/4 leaves>9/20. Includes ORIGINAL occupancy source, not only product source; does NOT cover intermediate exercised resets/arbitrary cores. O is reference outcome KL, not physical branch entropy or mutual information. Exact S4=2 boundary must use formal prime-log cancellation instead of rounded endpoint comparison.\n')]:
 with (base/name).open('a',encoding='utf-8',newline='') as f:f.write(entry)
paths=[Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B13\STREAM_NOTES.md')]
for agent,stamp in [('A039','20261014T055326Z-account05-A039-projection-under-restrictions'),('A037','20261021T220645Z-account03-A037-conditional-credit-ledger')]:
 p=Path(r'~\brain_workers\FEI100_20261011\agents')/agent/'runs'/stamp/'REPORT.md';paths.append(p)
paths.extend(Path(r'~\brain_workers\FEI100_20261011\context').glob('*.txt'))
receipts=[]
for p in paths:
 b=p.read_bytes();receipts.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'scope':'interfaces only; cp1252 text' if p.suffix=='.txt' else 'as specified in REPORT'})
js(R/'out/SOURCE_RECEIPTS.json',receipts)
protocol=json.loads(paths[0].read_text(encoding='utf-8'))['required_per_run']
assert set(claim)==set(protocol['claim_fields']);assert set(progress)==set(x.split(' (')[0] for x in protocol['progress_fields'])
assert json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert hashlib.sha256(claim['exact_statement'].encode()).hexdigest()==claim['statement_sha256']
for field in protocol['report_fields']:assert '## '+field in report
assert report.rstrip().split('\n')[-1].startswith('Universal bridge:');assert len((base/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
js(R/'out/WRITER_REPAIR.json',{'draft_writer':'nested triple-single-quoted string caused parse failure before protocol writes','repair':'separate saved finalizer with distinct enclosing quote delimiters','mathematical_effect':'none'})
files=[]
for p in R.rglob('*'):
 if p.is_file():
  b=p.read_bytes();assert len(b)<20_000_000;files.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
js(R/'out/PERSISTENCE.json',{'status':'PASS','saved_at':now,'protocol_key_sets_exact':True,'progress_equals_delta':True,'claim_digest_checked':True,'all_files_under20MB':True,'files':files})
wr(R/'out/STAGE_STATE.txt','COMPLETE_LOCAL: scoped author proof; main/audit PASS; independent review pending; full FEI OPEN.\n')
print(json.dumps({'stage':'COMPLETE_LOCAL','main_checks':res['checks'],'audit_checks':audit['checks'],'lean':lean['status'],'run':str(R)}))
