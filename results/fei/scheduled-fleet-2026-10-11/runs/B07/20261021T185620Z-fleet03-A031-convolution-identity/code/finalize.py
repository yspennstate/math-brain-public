from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
check=read(R/'out/CHECK.json');repro=read(R/'out/REPRODUCTION.json')
assert len(check['cases'])==18 and len(repro['records'])==3
tail=F(check['tail']['strict_margin_lower']);finite=min(F(z['remaining_original_17_bank'][0]) for z in check['cases'])
assert min(tail,finite)>F(1,16)
leanpath=R/'out/LEAN_RESULT.json';raw=leanpath.read_bytes()
if raw[:2] in [b'\xff\xfe',b'\xfe\xff']:leanpath.write_text(raw.decode('utf-16'),encoding='utf-8')
lean=read(leanpath);lean_status=lean['result']['status']
claim_id='A031-TRIANGLE-SAME-ORIGINAL-BANK-WEAK-RESET'
statement=('For every integer L>=1, let f_L=2 product_{j=1}^3(1-1_{input_Ej=0})-1 with E1={x,a,c}, E2=X2 union{a,b}, E3=X3 union{b,c}, X2 and X3 disjoint L-bit private blocks. Let p_s be the entire squared Walsh spectrum of f_L restricted to x=s, and prescribe Q_s(T)=Q_s(T+b)=(p_s(T)+p_s(T+b))/2 for b notin T. With bits, oriented M=sum_i sum_T p(T+i)log2((p(T)+p(T+i))/p(T+i)) and full conditional spectral entropy B_x, M(f_L)+B_x(f_L)+(CE(p_0,Q_0)+CE(p_1,Q_1))/2+1/16 <17 I_private(f_L), where the single ORIGINAL private owner is {x} union X2 union X3. The signed average fresh-reference reset relative to R(T)=p(T)+p(T+x) equals 1-average_s B_b(p_s)-J_x, is negative for L=1 and positive for every L>=2; for L>=16 it exceeds 1/4-2^-L(L+3/2). Any finite adaptive no-reset continuation carries the full expected terminal CE under the same original bank and retained old M debit; this does not pay later prescribed fresh resets or all physical phase-channel costs.')
claim={
 'claim_id':claim_id,'version':1,'exact_statement':statement,
 'hypotheses':['actual Boolean zero-point clause triangle exactly as stated','L is any positive integer; private blocks disjoint and disjoint from four shared/singleton labels','normalized uniform Walsh transform; logs base two','root reference is its entire actual spectrum; child references prescribed by b-row fair lifting','all previous root M, both child CE bills and all carried terminal debts retained; no reserve renewal'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A031'],'proof_source':['DERIVATION.md sections 1-6','code/check_reset.py','out/CHECK.json','code/reproduce.py','out/REPRODUCTION.json'],
 'proof_dependencies':[{'source':'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents/sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md','locator':'section 2 one-bit J_x<=(2/ln2)Inf_x','use':'positive reset lower bound only; joint bank theorem does not need this upper bound'}],
 'review_records':[],'status':'AUTHOR_PROOF_WITH_EXACT_CERTIFICATES_INDEPENDENT_REVIEW_PENDING','supersedes':None,'refutes':[],
 'first_unproved_line':'No gap in scoped author derivation/certificate; universal first unpaid line is paying a next prescribed fresh reference or admitting an arbitrary signed core against the SAME unused ancestor bank with both complete terminal bills and old debits. Independent-agent and formal acceptance remain pending.',
 'next_consumers':['A035','A096','A088','A094']}
write(R/'CLAIMS.json',[claim])
sources=[]
base=Path(r'~/mop_fei100');fleet=A.parents[1]
paths=[base/'reports/fei-2026-10-11'/s for s in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]
paths += [fleet/'BOARD.md',fleet/'claude/B07/STREAM_NOTES.md',Path(r'~/AGENTS.md')]
paths += [A/'runs/20261014T075717Z-fleet05-A031-convolution-identity'/s for s in ['REPORT.md','DERIVATION.md','HEREDITARY_BOUNDARY.md']]
paths += [fleet/'agents/A035/runs/20261021T164849Z-fleet03-A035-signed-cancellation-countersearch'/s for s in ['REPORT.md','DERIVATION.md']]
paths += [fleet/'agents/A096/runs/20261014T094929Z-fleet05-A096-live-gap-ledger/REPORT.md']
for p in paths:
    assert p.exists(),p
    sources.append({'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size})
write(R/'out/SOURCE_MANIFEST.json',sources)
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B07','packet_id':'A031','gap_id':'G-BOOLEANITY','attempt_id':'A031-stage17-same-bank-width-exhaustion-weak-reset',
 'method':'signed inclusion-exclusion before squares; exact compressed likelihood laws; paid complete child-reference conversion; finite rational certificates plus analytic Boolean point-defect tail; independent direct-character reconstruction',
 'mathematical_delta':'The existing (1,L,L) exhausted-private fixture now pays an actually positive prescribed weak-shared b-reference reset, old root M debit, both full child CE bills and arbitrary finite no-reset continuations from SAME original rate17 private bank, with uniform >1/16 spare. No universal FEI constant improvement.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUTHOR_PROOF_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':['A031 prior triangle signed expansion/root-width exhaustion (rederived, not imported as an unreviewed premise)','A096 stage6 no-reset CE transport (rederived)','BLOCK_RESTRICTION_IDENTITY section2 J_x bound'],
 'claims_created_or_changed':[claim_id+'@1'],'source_artifacts':['DERIVATION.md','REPORT.md','out/CHECK.json','out/REPRODUCTION.json','out/SOURCE_MANIFEST.json','out/CONTEXT_INTAKE.json','out/LEAN_RESULT.json'],
 'next_consumers':['A035','A096','A088','A094'],
 'next_action':'After the paid weak-shared b reset, prescribe the next fresh reference on an actual active b query and charge its signed price, old M and both full terminal references to the SAME unused >1/16 ancestor reserve; do not repeat no-reset telescoping or renew private influence.',
 'stagnant_substantive_attempts':0,'blockers':['universal initial source/reference payment and later prescribed resets remain open','independent-agent review pending','Lean '+lean_status,'supervisor copy and remote mirrors unverified'], 'packet_ids':['A031']}
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)
report=f'''# A031: the width-exhausting triangle pays a positive weak-reference reset

## exact target, quantifiers, hypotheses and units

For every integer L>=1 in the actual Boolean triangle E1={{x,a,c}}, E2=X2+{{a,b}}, E3=X3+{{b,c}}, |X2|=|X3|=L, the SAME ORIGINAL private-influence bank pays the old root oriented M, the x-query erasure and BOTH full prescribed child-reference cross entropies, with more than 1/16 bit left at rate17. References Q_s fair-lift the actual child spectral b-marginal; they are complete normalized finite-cost laws, not deleted carrier sectors. The incoming reference is explicitly the actual root spectrum marginalized over x. The reset price is positive for every L>=2 despite b's root influence tending to zero. All logarithms are bits. This repairs the earlier disappearing-owner fixture; it is not full FEI or a new general class-constant claim.

## sources actually read, revisions and theorem locators

Read machine AGENTS, full execution-v2 protocol, current BOARD (2026-10-21 18:58 UTC), B07 lead v2 and own rolling files. The later own run folders hold .final markers; the last substantive proof remains 20261014T075717Z. Its REPORT/DERIVATION/HEREDITARY_BOUNDARY identify the exact failed child-private-bank renewal. Read A035's 20261021T164849Z REPORT/DERIVATION sections2-5 (zero-carrier repair and both conditional channels) and A096 stage6 REPORT (complete-reference no-reset transfer already closed). Do not claim their generic continuation again as new mathematics. Read campaign README/status, parse all required registries, inspect the plan, supplement documents/sources and the four paper texts at their relevant scope locators; out/CONTEXT_INTAKE and CONTEXT_EXCERPTS record this limited context intake. No full-paper re-audit or external-literature novelty claim. Read-only math recall supplies only leads and no premise. SOURCE_MANIFEST pins critical source bytes. The current user campaign end2026-10-23 14:49UTC overrides the archived21October endpoint. Wake reported stale personal-context notes; current campaign instructions govern.

## complete derivation or exact first unsupported line

DERIVATION sections1-2 retain all eight signed union-containment terms before squaring. Physical children use u+v and u-v, and the SAME incoming law R is u^2+v^2. The exact conversion is Delta=1-average B_b(child)-J_x. Sections3-5 prove the rate17 joint bank inequality: L1..15 have exact rational log certificates; for every L>=16 the Boolean comparison with a three-bit defect yields H+M<=H(defect)+M(defect)+(2L^2+10L+548)2^-L. A retained empty-frequency discrimination gives J_x>1/4. The resulting single tail endpoint has margin >1/16, as do all finite certificates. Separately, J_x<3 Inf_x and average B_b<=h2(Inf_b) prove Delta>1/4-2^-L(L+3/2)>0 in the tail. Boundary L1 has negative price and is retained. Neither child private reserve is renewed.

Section6 carries both paid full references through any finite adaptive no-reset continuation, with all terminal CE retained and the root M debit unchanged. This is an application of the already-closed A096 chain rule. The normalized non-Boolean singleton vector at n=2^18 has norm-one first physical children but bill19-2/n>17(n-3)/n; nonempty convolution2/n excludes it. An arbitrary untouched Boolean spectator retains its entire M and CE debt with coefficient one. First unsupported universal line: price the NEXT prescribed fresh reference, or an arbitrary signed core, against the SAME unused ancestor bank with old debits and both full complementary terminals. No all-dimensional FEI theorem or actual Boolean counterfamily is supplied.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC preceded discovery. V1's target a pilot was refunded; its output is preserved as PILOT_V1_a. FROZEN_SPEC_V2 switches to the untouched weak shared b target before that search, preserving the same bounded width domain. V2 pilot L1,2,4 passed238 assertions in6.6745s. Full command: python -X utf8 code/check_reset.py. It checks L1..15 plus fixed tail fixtures16,32,64: {check['assertions']} exact assertions, {len(check['cases'])} fixtures, {check['runtime_seconds']:.6f}s, below180s. No automatic dimension escalation. Fractions, exact multiplicities and 32-term atanh remainder intervals determine signs; all terminal H, CE, incoming KL, conversion prices and original-bank margins are saved. Proof of the all-L tail is analytic, not a finite extrapolation.

REPRODUCTION_SPEC precedes python -X utf8 code/reproduce.py. Independent direct-character sums (no imported transform, family builder or log kernel), direct physical edges and separate24-term rational logarithms reconstruct L1,2,3; all64 convolution shifts are checked for L1. Result: {repro['assertions']} assertions, {repro['runtime_seconds']:.6f}s, complete output in REPRODUCTION.json. Both implementations are by A031, so this is not independent-agent acceptance. The reproduction also checks the exact non-Boolean guard arithmetic. Risks tested: wrong signed collapse, wrong original source influence, duplicate/omitted multiplicities, discarded zero/reference-only masses, entropy identity sign, negative-price L1 boundary, tail coefficient bounds and unpaid spectator terminals.

The required Lean attempt targets only ((u+v)^2+(u-v)^2)/2=u^2+v^2. Result: {lean_status}, timeout45s; source/compiler/environment hashes are in LEAN_RESULT. No Lean theorem or axiom audit passed and no formal certification is claimed. PowerShell redirected that JSON as UTF16; it was explicitly decoded and saved as UTF8 before validation. Proof rung: author proof with exact finite certificates, independent-agent review pending. Memory estimates60-90MB; compute state was ok with14.8GB available when inspected. No job expected over300MB, no memory-admission threshold crossed, no GPU, dense matrix, detached job, visible window or other-agent mutation. Processes were allowed to finish; no load was shed.

## proof dependencies and changed downstream conclusions

One narrow repair/application claim is saved, with self-contained signed construction, tail proof and exact certificates. The standard one-bit J_x<=(2/ln2)Inf_x bound is read with its elementary proof in BLOCK_RESTRICTION_IDENTITY section2; only the positive-price lower bound needs it. Generic CE conservation is rederived. Old root M payment alone did not pay the entropy of a root actual-spectrum reference: the new JOINT inequality explicitly pays that extra cost and the prescribed reset. No old root theorem is silently extended and no prior partial review becomes full acceptance. The class-specific bank now survives the exact exhausted-owner fixture; universal initial admission and further fresh resets remain open. No new broad universal candidate is opened.

## one next mathematical action and independent reviewer

Prescribe the next fresh reference after an actual active b query, keep the original M debit and the already charged x/reference history, and price both full complementary terminals against the SAME remaining >1/16 ancestor reserve. No-reset continuation needs no further theorem and must not be repeated. A035 is primary independent reviewer; A096/A088/A094 alternate or audit. This is a local source-bound handoff; no message, acceptance or shared-index update is asserted.

## actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and identical PACKET_DELTA use the exact protocol key sets. Code/out, frozen specifications, failed-free-target pilot, full exact certificates, independent reconstruction, source hashes and Lean limit are local. STATUS has two lines; dated WORKLOG is appended; LEARNED records the one-owner repair and precise residual. SCHEMA_CHECK and ARTIFACT_RECEIPTS verify hashes, local bytes and20MB ceilings. No local save blocker. Independent review, canonical adoption, supervisor copy and remote mirrors remain unverified. Only A031 research files are written; mandatory session/checklist tools are separate infrastructure. No git, mail, brain-memory write, trading access or other-agent file mutation.

## Universal bridge

C024 history transfer and C018's signed reference mechanism advance through the specific width-exhaustion obstruction: an actually positive weak-shared b-reference reset, old root M and BOTH full terminal CE bills are paid at SAME original rate17 with uniform >1/16 spare, and all finite no-reset continuations retain that account. Universal FEI constant improvement is zero. The next unpaid step is a prescribed later fresh reference or arbitrary signed-core admission using that SAME unused reserve, without dropping the complementary terminal. NEXT targets the first remaining conversion bill; another root class bound or an automatic no-reset identity would repeat paid work.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
with (R/'DERIVATION.md').open('a',encoding='utf-8') as f:f.write('\nCertificate strengthening: the finite minimum and the analytic tail endpoint both leave more than1/16 bit. out/SCHEMA_CHECK records the exact rational comparison; therefore (2) remains strict after adding1/16 to its left side.\n')
stamp=datetime.now(timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: A031 stage17 saved: all-L exhausted-private triangle pays positive weak-b reset, old root M and BOTH full child CE from SAME rate17 original bank; >1/16 spare; exact checks PASS; FEI OPEN, review pending.\nNEXT: A035/A096/A088/A094 review; price NEXT prescribed fresh reference after active b query from SAME unused >1/16 ancestor reserve with old debits and both full terminals.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp}: Stage17 consumes A035 zero-carrier repair and A096 no-reset closure. Target a pilot refunded; prescribed weak b reset is positive for ALL L>=2. Joint old-M+query-B+both full child CE pays from SAME original17-private owner with >1/16 spare, analytic L>=16 tail and exact L1..15. {check["assertions"]}+{repro["assertions"]} exact assertions; independent-agent review pending; Lean {lean_status}. Universal next fresh reset/arbitrary-core admission unpaid; FEI OPEN.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage17: width exhaustion does not by itself prevent ORIGINAL-owner payment. For actual triangle(1,L,L), root actual-spectrum reference marginalized over sole X1 query can be reset to each child b-row marginal lifted by fair b, while charging old M(root)+B_X1+mean FULL child CE+1/16<17 I_private(ORIGINAL), all L>=1. Reset Delta=1-mean B_b-J_X1; negative L1, positive all L>=2, >1/4-2^-L(L+3/2) for L>=16. Proof uses signed eight-clause expansion before squares, finite rational L1..15 and actual Boolean three-bit-defect tail. Bank survives arbitrary NO-RESET continuations, but not another prescribed reset by assertion. Singleton norm-one nonBoolean control violates payment although first children normalize; full signed admission matters. Root M bound alone never paid root spectral-reference CE; new JOINT inequality does. Full spectator M+CE stays coefficient-one debt.\n')
protocol=read(base/'reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')['required_per_run']
expected=set(protocol['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
assert set(claim)==set(protocol['claim_fields'])
assert claim['statement_sha256']==hashlib.sha256(statement.encode('utf-8')).hexdigest()
assert all(x in report for x in protocol['report_fields'])
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(p.stat().st_size<20*1024*1024 for p in R.rglob('*') if p.is_file())
write(R/'out/SCHEMA_CHECK.json',{'passed':True,'exact_progress_keys':True,'exact_claim_keys':True,'progress_equals_delta':True,'statement_hash':True,'all_files_under_20MB':True,'finite_and_tail_margin_greater_than_1_over_16':True,'finite_margin_outward_lower':str(finite),'tail_margin_outward_lower':str(F(tail.numerator*(1<<80)//tail.denominator,1<<80)),'independent_agent_acceptance':False,'lean_status':lean_status})
receipts=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in sorted(R.rglob('*')) if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json']
write(R/'out/ARTIFACT_RECEIPTS.json',{'saved_at':stamp,'local_only':True,'files':receipts,'supervisor_copy':'UNVERIFIED','remote_mirrors':'UNVERIFIED'})
print(json.dumps({'local_files':len(receipts)+1,'assertions':check['assertions']+repro['assertions'],'margin_gt_1_over_16':True,'lean':lean_status,'full_FEI':'OPEN'}))
