from pathlib import Path
import json,hashlib,datetime,shutil
RUN=Path(__file__).resolve().parent.parent
AGENT=RUN.parents[1]
def write(p,s): p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,x): write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
main=json.loads((RUN/'out/check_full.json').read_text(encoding='utf-8'))
pilot=json.loads((RUN/'out/check_pilot.json').read_text(encoding='utf-8'))
ind=json.loads((RUN/'out/independent.json').read_text(encoding='utf-8'))
assert main['status']==ind['status']==pilot['status']=='PASS'
assert main['counts']['cases']==6073 and ind['partial_assignments']==2187
old=AGENT/'runs/20261014T051435Z-account05-A028-stopping-tree-payment'
oldclaims=json.loads((old/'CLAIMS.json').read_text(encoding='utf-8'))
print('PRIOR CLAIM SHAPE',type(oldclaims).__name__)
if isinstance(oldclaims,dict):
    oldlist=oldclaims.get('claims',[oldclaims])
else: oldlist=oldclaims
prior=oldlist[0]
claimid=prior['claim_id']
statement=('Version6 retains v5 at its original scope and adds the following theorem. For every Boolean controller a on an independent uniform physical control cube and arbitrary shared Boolean data sources G,H, define c=(1-a)/2, p=Pr(a=-1), V=4p(1-p), gamma=Pr(G!=H), J=JS_p(P_G,P_H), q_t=(1-p)Ghat(t)^2+pHhat(t)^2, and L=sum_t q_t h2(V(Ghat(t)-Hhat(t))^2/(4q_t))+V gamma H(P_a conditioned nonempty), with zero-row and V=0 conventions. Then H((1-c)G+cH)=(1-p)H(G)+pH(H)+J+L. At every data query, the signed entropy debit after subtracting both original source decrements and the signed L difference equals J-parent minus averaged J-children. At every control query this J difference is nonnegative. For EVERY finite adaptive mixed physical stopping tree, sum_DATA reach*debit+sum_CONTROL reach*Jrelease+E_terminal J=J_root, hence signed DATA payment never exceeds the SAME original J_root<=h2(p)<=1. Conditional on A028 v5 tensorized-JS price, J_root<=2log2(e)gamma I(a). No terminal KL reset payment or universal FEI admission is asserted.')
claim={
'claim_id':claimid,'version':6,'exact_statement':statement,
'hypotheses':['Uniform finite product cube; disjoint physical controller and data coordinates','Boolean controller and both Boolean source functions; sources may fully share data','All queries are actual coordinates; both restricted source functions retained at each node','Signed debits and structural L variations retained; no positive-part substitution or bank renewal'],
'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),
'contributors':['A028','A026 (balanced intact-controller data-only precursor)'],
'proof_source':'DERIVATION.md equations (1)-(4); out/check_full.json; out/independent.json',
'proof_dependencies':[{'claim':'A026 stage17 signed DATA JS identity','scope':'precursor reconstructed and extended; not an assumed accepted theorem'},{'claim':claimid+'@5','scope':'only quantitative original-J root price; exact mixed telescope independent of v5'}],
'review_records':[],'status':'AUTHOR_PROOF_EXACT_CHECKED_REVIEW_PENDING','supersedes':[{'claim_id':claimid,'version':5,'reason':'Narrow mixed-history signed-JS extension; v5 conclusions retained at their original scopes'}],
'refutes':[],'first_unproved_line':'Universal certification/payment of inherited source entropy and prescribed terminal-reference conversion from one unused original influence account.',
'next_consumers':['A026','A027','A029','A076','A087','A091','A094']}
dump(RUN/'CLAIMS.json',[claim])
progress={
'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B06','packet_id':'A028',
'gap_id':'C019','attempt_id':'A028-v6-biased-controller-mixed-signed-JS',
'method':'Consume A026 exact signed debit; separate nonnegative structural sector; use concavity in controller bias and finite optional telescoping',
'mathematical_delta':'Extends intact balanced-controller DATA-only transport to arbitrary biased/nonpoint controllers and EVERY adaptive mixed control/data history; same original JS budget, both original source decrements and structural terminal costs retained.',
'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_AUTHOR_PROOF; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',
'claim_versions_used':[claimid+'@5 (conditional root price)','A026 stage17 signed DATA debit (reconstructed precursor)'],
'claims_created_or_changed':[claimid+'@6'],
'source_artifacts':['DERIVATION.md','out/context_receipts.json','out/check_pilot.json','out/check_full.json','out/independent.json'],
'next_consumers':['A026','A027','A029','A076','A087','A091','A094'],
'next_action':'Carry this SAME J+L decomposition through one prescribed inherited terminal-reference conversion and price the additional KL/change term from genuinely unused original source surplus; keep both terminal references and old debits.',
'stagnant_substantive_attempts':0,
'blockers':['No universal source surplus/certification theorem','Inherited arbitrary reference-reset KL not paid','v5 quantitative root-price and new v6 independent review pending'],
'packet_ids':['A028']}
dump(RUN/'PROGRESS.json',progress)
(RUN/'PACKET_DELTA.json').write_bytes((RUN/'PROGRESS.json').read_bytes())
lean=RUN/'out/lean_result.txt'
leanstatus=lean.read_text(encoding='utf-8')[-1600:] if lean.exists() else 'Not executed; no Lean-checked entropy theorem is claimed.'
report=f'''# A028: one signed Jensen--Shannon bank through mixed histories

## exact target, quantifiers, hypotheses and units

For every independent Boolean controller, including biased and non-point controllers, and arbitrary fully shared Boolean data sources, transport the booked DATA entropy residual through EVERY finite adaptive mixed control/data stopping tree. Entropy is in bits; influences are uniform physical flip influences. The exact budget is the SAME original J_root=JS_p(P_G,P_H), bounded by h2(p)<=1. The prior v5 tensorized-JS lemma prices it at 2log2(e) gamma I(a); that quantitative dependency remains pending independent review. Full FEI stays OPEN.

## sources actually read, revisions and theorem locators

Read execution protocol v2 in full, BOARD supervisor2026-10-22 20:55UTC, B06 STREAM_NOTES v2, own STATUS/LEARNED/WORKLOG and substantive stage5 REPORT/DERIVATION/code. Later account05 marker folders contain no REPORT; they are not 11 additional mathematical stages. Read A026 stage17 REPORT and durable facts: its scope is BALANCED intact encoder and DATA-only histories; its all-m local-price obstruction is not refuted here. The campaign README, CURRENT_STATUS, four registries, plan, supplemental campaign/claims/counterexamples/seeds/mapping and source notes, and all four local paper texts were read/scanned; source intake records paths/lengths and relevant locators, not independent full-paper acceptance. Source decoding explicitly falls back from UTF-8 to cp1252 for legacy paper text. One read-only math-brain search returned neighboring restriction cards and irrelevant signed-tree cards; none supplies a premise. Current user campaign end overrides old 21-Oct timestamps in the archived protocol. Brain wake warned of stale owner-model/state-of-mind notes; they were not relied on.

## complete derivation or exact first unsupported line

DERIVATION.md proves the normalized sector identity H(F)=weighted source entropy+J+L, where J>=0 and L>=0. The exact data residual after BOTH source decrements and the signed structural L difference is a J drop. For fixed source spectra J(p) is concave, so every CONTROL query releases nonnegative J. Finite telescoping proves sum_DATA reach*debit+sum_CONTROL reach*Jrelease+E_terminal J=J_root, including every partial stopping frontier. Negative data debits are refunds. Neither balance nor an intact controller is required. No descendant bank is issued.

The conditional full stopping-class corollary retains v5's root constant max(K+3log2(e),L_G+2p,L_H+2(1-p)) for certified controller/source classes; resolving remaining controls stops at restricted sources. This is the existing root bound with explicit mixed-history accounting, not an improved FEI constant or new universal class. L and both source costs remain fully present; their removal would invalidate the claimed residual. The first unsupported line is universal source/reference payment from unused ancestor surplus, particularly prescribed terminal-reference conversion. No arbitrary KL-reset or local positive-part rule follows.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede both search/check domains and the independent check. Pilot: {pilot['counts']['cases']} actual Boolean cases, {pilot['counts']['assertions']} exact assertions, PASS in {pilot['seconds']:.3f}s. Main: all controllers and ordered shared-source pairs in dimensions0..2, no quotient, plus ONE predeclared biased nonpoint/common-dictator fixture: {main['counts']['cases']} roots, {main['counts']['data_rows']} DATA rows, {main['counts']['control_rows']} CONTROL rows, {main['counts']['histories']} adaptive histories, {main['counts']['assertions']} exact assertions, PASS in {main['seconds']:.3f}s. The fixture is point3 versus Maj3 times one common dictator with a controller negative at three of eight points. Its tested data query keeps all four original source children nonconstant; source spectra are unequal. Every history retains structural and original source terminal entropy.

Independent direct character sums verify ALL {ind['partial_assignments']} partial restrictions of that seven-bit fixture, with rational masses, separate prime-log equality code and direct edge counts: {ind['exact_assertions']} assertions, PASS in {ind['seconds']:.3f}s. Main uses integer Walsh/Fraction and outward rational atanh log enclosures, never floating signs. Domains and fixed fixtures are not a finite-to-infinite proof: the entropy-chain/concavity/telescope argument proves the all-dimensional scoped theorem. Commands: python -X utf8 code/check.py pilot; python -X utf8 code/check.py full; python -X utf8 code/independent.py. Estimates100MB/64MB, internal55s pilot/independent and240s main limits; no >300MB job, GPU, detached process or automatic escalation. Peak memory was not measured. Formal-check receipt: {leanstatus.strip()}

## proof dependencies and changed downstream conclusions

This is version6 of the same A028 candidate, not another broad pending candidate. A026's balanced DATA-only identity is reconstructed by the sector formula; its local-price obstruction and source-surplus gap survive. V5 root-J pricing is optional for the exact theorem and explicitly conditional for the influence corollary. The new step is concavity of weighted JS under control restriction, enabling arbitrary interleaving with one original signed budget. A026/A027/A029/A076 can use this allocation; A087/A091/A094 should audit side conditions and distinction from terminal-reference payment. Existing root constants do not change. No independent acceptance, canonical adoption or remote mirror is inferred.

## one next mathematical action and independent reviewer

Price ONE actual prescribed inherited reference conversion using the SAME J+L account plus genuinely UNUSED original source surplus, preserving both full terminal references and old debits. A087 should reconstruct the mixed-tree proof; A091 should check bias/sector endpoints; A094 should challenge the separation between entropy, structural booking and KL resets. Named handoffs are saved for the supervisor, not sent.

## actual persistence receipts or precise save blocker

All four protocol files, DERIVATION, frozen specs, main and independent code/outputs, source receipts and rolling notes are saved only within A028. PACKET_DELTA is byte-identical to PROGRESS. Finalizer validates exact schema fields, statement hash, output counts, two-line STATUS and file sizes, then writes SHA256 persistence receipts. The helper is copied byte-for-byte from v5 and pinned by {main['helper_sha256']}. Supervisor copying, independent review and mirror verification are unobserved.

## Universal bridge

This stage moves C019/C024 by removing A026's balanced/intact and data-only restrictions from the signed residual transport: an arbitrary biased controller may be queried at any adaptive times while the same original JS reserve pays all signed DATA residuals after both source decrements and the exact structural variation remain booked. The payment is <=J_root, conditionally <=2log2(e)Q_root, without renewal or an additional dimension/depth factor. Universal FEI improvement is zero because complete source certification and prescribed terminal-reference conversion remain unpaid. NEXT attacks that exact conversion against the SAME decomposed budget; it is shorter than another isolated class computation because the mixed-history entropy transport is now explicit and general.
'''
write(RUN/'REPORT.md',report)
write(AGENT/'STATUS.md','STATE: A028 v6 saved arbitrary biased-controller ALL mixed-history signed DATA JS payment from SAME original bank; exact checks PASS; structural/source terminals retained; review pending; FEI OPEN.\nNEXT: A087/A091/A094 review; pay one prescribed inherited terminal-reference conversion from SAME J+L account and unused source surplus, both terminals and old debits retained.\n')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
    f.write(f'\n{stamp} — stage6 {RUN.name}: consumed A026 signed JS debit; generalized to biased/nonpoint controllers and all mixed adaptive histories via concavity in p. Main {main["counts"]["cases"]} roots/{main["counts"]["assertions"]} exact assertions; independent {ind["partial_assignments"]} restrictions/{ind["exact_assertions"]} checks PASS. SAME original reserve, both source/structural terminals retained. Universal source/reference payment OPEN; no root constant improvement.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
    f.write('\n## Stage6: weighted JS survives arbitrary controller interleaving\n\nFor arbitrary independent controller a and shared sources G,H, H(F)=weighted source H+J_p+L with J_p=JS_p(PG,PH)>=0 and L=B_binary+Var(a)*gamma*H(controller nonempty law)>=0. After retaining BOTH original source decrements and signed L variation, DATA debit=J_parent-EJ_child. J_p is concave in controller p, so every CONTROL query has nonnegative J release. Therefore ALL finite adaptive mixed histories satisfy sum_DATA reach*debit+sum_CONTROL reach*release+EJ_terminal=J_root, never renewing the original budget. V5 prices J_root<=2log2(e)gamma Ia; that root quantitative dependency remains review-pending. This extends A026 balanced/intact DATA-only transport; no root FEI constant improves. L, source decrements and arbitrary terminal-reference KL cannot be dropped. NEXT prescribed inherited reference conversion needs its own genuinely unused original source surplus.\n')
helper=old/'code/exact.py'
shutil.copyfile(helper,RUN/'code/exact_helper.py')
assert sha(RUN/'code/exact_helper.py')==main['helper_sha256']
# Keep the original pin and include the exact helper for standalone reproduction.
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
expected=set(protocol['required_per_run']['progress_fields']); expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode()).hexdigest()
pins=[]
intake=json.loads((RUN/'out/context_receipts.json').read_text(encoding='utf-8'))
for item in intake:
    p=Path(item['path']); pins.append({**item,'sha256':sha(p)})
for p in [old/'DERIVATION.md',old/'CLAIMS.json',Path('BOARD.md'),Path('claude/B06/STREAM_NOTES.md'),Path('agents/A026/runs/20261021T185558Z-account03-A026-good-coordinate-erasure/REPORT.md')]:
    pins.append({'path':str(p),'sha256':sha(p)})
dump(RUN/'out/SOURCE_PINS.json',pins)
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p.stat().st_size<20_000_000 for p in files)
receipt={'status':'LOCAL_SAVE_VERIFIED','run_id':RUN.name,'files':[{ 'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files],
         'rolling':[{ 'path':str(p),'sha256':sha(p)} for p in [AGENT/'STATUS.md',AGENT/'WORKLOG.md',AGENT/'LEARNED.md']],
         'remote_copy':'UNOBSERVED','independent_review':'PENDING'}
dump(RUN/'out/PERSISTENCE_RECEIPTS.json',receipt)
print(json.dumps({'status':receipt['status'],'claim_id':claimid,'version':6,'run_files':len(files),'exact_main':main['counts']['assertions'],'exact_independent':ind['exact_assertions']}))
