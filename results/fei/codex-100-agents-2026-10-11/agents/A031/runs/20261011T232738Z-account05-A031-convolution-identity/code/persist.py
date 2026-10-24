import json,hashlib,datetime
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R.parents[1]
TEAM=A.parents[1];PROTOCOL=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
S=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents/sources')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj):(R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
v=json.loads((R/'out/validation.json').read_text());pilot=json.loads((R/'out/pilot.json').read_text())
t=json.loads((R/'out/tree_validation.json').read_text());cert=json.loads((R/'out/certificates.json').read_text())
assert v['cases']==65812 and t['total_cases']==10 and len(cert['bent_surgery'])==3
b05=TEAM/'claude/B05/runs/20261011T225000Z-claude-B05-odd-face-transport'
old=A/'runs/20261011T214115Z-account05-A031-convolution-identity'
review33=TEAM/'agents/A033/runs/20261011T221704Z-account05-A033-derivative-hierarchy/A031_INDEPENDENT_REVIEW.md'
review88=TEAM/'agents/A088/runs/20261011T223053Z-account05-A088-booleanity-referee/AUDIT.md'
sources=[PROTOCOL,TEAM/'BOARD.md',TEAM/'claude/B07/STREAM_NOTES.md',TEAM/'claude/B05/STREAM_NOTES.md',b05/'REPORT.md',b05/'CLAIMS.json',review33,review88,old/'DERIVATION.md',old/'CLAIMS.json',S/'ERASURE_REDUCTION.md',S/'ERASURE_RIGIDITY.md']
write('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':digest(p),'scope':'Actual read; A088 audit A031 section and B05 report in full; prior erasure/rigidity proofs read previously and erasure theorem rechecked'} for p in sources])
claims=[]
def record(cid,statement,hypotheses,dependencies,refutes):
    payload=json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode('utf8')
    return dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hypotheses,
      statement_sha256=hashlib.sha256(payload).hexdigest(),contributors=['account05/A031'],
      proof_source={'path':str(R/'PHASE_ERASURE.md'),'sha256':digest(R/'PHASE_ERASURE.md')},
      proof_dependencies=dependencies,review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
      supersedes=[],refutes=refutes,first_unproved_line=None,next_consumers=['A088','A094','B07','B05','A025','A064','B20'])
hyp=['Genuine Boolean sign on a finite uniform cube','One actual physical coordinate split','Entropy in bits; all zero and deterministic-sector conventions in PHASE_ERASURE.md']
statement='Let A=(g+h)/2,V=(g-h)/2,F=A+iV for an actual Boolean split, u=Ahat,v=Vhat,d=Inf_i, and M_i be the mutual information of the spectral-sector law with masses u_T^2,v_T^2. Full Booleanity gives F^4=1 and I(F^2)/2=W_i=2 sum_(U nonempty)|U|(sum_T v_T v_(T xor U))^2. With R_i=W_i-d log2(1/d)>=0 and sigma(d)=log2(e)d-(1-d)log2(1/(1-d))>=0, B_i=W_i+log2(e)d-R_i-M_i-sigma(d). In particular B_i+M_i<=W_i+log2(e)d; this bound fails for the normalized non-Boolean coefficient vector (4/5,3/5). In any bound B_i<=alpha I(F^2)+C d valid for all Boolean splits with fixed finite C, necessarily alpha>=1/2, as witnessed by even-dimensional bent one-point phase surgery.'
claims.append(record('A031-FOURTH-ROOT-ERASURE-CREDITS',statement,hyp,[],['universal coordinate bound B_i<=alpha I(F^2)+C d with alpha<1/2','admission of arbitrary normalized real vectors to the phase boundary inequality']))
statement2='For every even r>=2, the Boolean sign f_r(x,y)=(-1)^(x^T(I_r+J_r)y) has flat spectrum, H=2r,I=r,B_i=1,d_i=1/2,M_i=0,W_i=(r-1)/2,R_i=(r-2)/2 for every coordinate. Hence Q_sum=sum_i W_i=r(r-1) and (Q_sum-a sum_i M_i)/I=r-1 for any fixed a>=0. No fixed finite K,a>=0 universally satisfy Q_sum-a sum_i M_i<=K I on all Boolean functions. Subtracting the physical deficits gives Q_sum-sum_i(R_i+M_i)=I on this family. This refutation concerns an all-coordinate aggregate and does not refute localized bad-node tree payment.'
claims.append(record('A031-SPECTRAL-CREDIT-ONLY-PHASE-NOGO',statement2,hyp,[],['universal Q_sum-a sum_i M_i<=K I with finite K,a>=0']))
# Record accepted original B05 versions without changing their statements or contributors.
for c in json.loads((b05/'CLAIMS.json').read_text()):
    if c['claim_id'] in ['B05-ODDFACE-ISO-PAYMENT','B05-ODDFACE-TELESCOPE']:
        c['review_records'].append({'reviewer':'account05/A031','verdict':'ACCEPT_AT_STATED_SCOPE',
          'source':str(R/'B05_INDEPENDENT_REVIEW.md'),'sha256':digest(R/'B05_INDEPENDENT_REVIEW.md'),
          'method':'Independent signed Fourier phase representation, internal-edge proof, and exact physical face/tree checks',
          'contributor_conflict':False,'shared_registry_adoption':'PENDING_B20'})
        c['status']='INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE_PENDING_INDEX_ADOPTION';claims.append(c)
# Import the observed prior A031 review receipts into this run, keeping stage 1 immutable.
for c in json.loads((old/'CLAIMS.json').read_text()):
    c['review_records'] += [{'reviewer':agent,'verdict':'ACCEPT_AT_STATED_SCOPE','source':str(p),'sha256':digest(p),'shared_registry_adoption':'PENDING_B20'} for agent,p in [('account05/A033',review33),('account05/A088',review88)]]
    c['status']='INDEPENDENTLY_RECONSTRUCTED_ACCEPT_AT_STATED_SCOPE_PENDING_INDEX_ADOPTION';claims.append(c)
write('CLAIMS.json',claims)
proofsource={'source':'C005','path':str(S/'ERASURE_REDUCTION.md'),'sha256':digest(S/'ERASURE_REDUCTION.md'),'locators':'sections 1-2, exact entropy drop and JS bound; prior complete proof rechecked'}
write('out/BRIDGE_DEPENDENCIES.json',{'new_local_claims_dependencies':[],'tree_interface_dependencies':[{'claim_id':'B05-ODDFACE-TELESCOPE','version':1,'status':'independently reconstructed by A031 at original scope'},proofsource]})
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B07',packet_id='A031',gap_id='G-BOOLEANITY',
 attempt_id='A031-fourth-root-phase-2',method='Lead-directed route repair: full signed fourth-root phase square, exact spectral and physical deficit credits, sharp bent surgery and dense-bent obstruction',
 mathematical_delta='Retained both credits in the Boolean coordinate bound; boundary coefficient 1/2 sharp; spectral-KL-only aggregate payment refuted by explicit dense bent family; exact C019 credit interface keeps terminal leaves and factor of two.',
 deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='LOCAL_ROUTE_REPAIR_AND_EXACT_OBSTRUCTION; C018_C019_PAYMENT_OPEN; NEW_CLAIMS_REVIEW_PENDING',
 claim_versions_used=[{'claim_id':'B05-ODDFACE-TELESCOPE','version':1,'scope':'only exact tree interface; independently reconstructed, no payment hypothesis used'},proofsource],
 claims_created_or_changed=[{'claim_id':c['claim_id'],'version':c['version'],'change':'new author proof' if c['claim_id'].startswith('A031-FOURTH') or c['claim_id'].startswith('A031-SPECTRAL') else 'source-bound independent-review receipt'} for c in claims],
 source_artifacts=['PHASE_ERASURE.md','B05_INDEPENDENT_REVIEW.md','FROZEN_SPEC.json','TREE_SPEC.json','code/check_phase.py','code/check_tree.py','out/validation.json','out/certificates.json','out/tree_validation.json','out/SOURCE_MANIFEST.json','out/BRIDGE_DEPENDENCIES.json'],
 next_consumers=['A088','A094','B07','B05','A025','A064','B20'],
 next_action='Evaluate the joint-credit positive excess [W-R-M-sigma-(K-log2(e))d]_+ on B05 nested rare-flip trees with terminal reserves, then seek a single-use ownership/selection proof; do not reopen anchor or spectral-credit-only aggregate payment.',
 stagnant_substantive_attempts=0,blockers=['No independent review of the two new repaired-route claims yet','No universal joint-credit tree payment proved','Supervisor registry adoption and external copy not performed by A031'],packet_ids=['A031'])
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)
fields=json.loads(PROTOCOL.read_text(encoding='utf8'))['required_per_run']
assert set(progress)=={x.split(' ')[0] for x in fields['progress_fields']}
assert all(set(c)==set(fields['claim_fields']) for c in claims)
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
write('out/SCHEMA_CHECK.json',{'progress_exact_fields':True,'claims_exact_fields':True,'delta_matches_progress':True,'new_claim_count':2,'existing_versions_reviewed_or_imported':4})
report=f'''# A031 stage 2: phase erasure with both credits retained

## exact target, quantifiers, hypotheses and units
Following B07 lead v1 (2026-10-11 22:40 UTC), drop the anchor/Cauchy payment and prove or refute a Booleanity-specific one-coordinate erasure bound using the fourth-root phase F=E_i f+imaginary_unit*D_i f. Quantifiers are every finite uniform-cube Boolean sign and every actual physical coordinate. Entropies are bits; d=Inf_i; B_i=H(S_i|S_-i). The exact result and its non-Boolean discriminator are PHASE_ERASURE.md (2)-(3). This is route repair and a sharp obstruction, not a new universal FEI constant.

## sources actually read, revisions and theorem locators
Read the 23:19 UTC BOARD.md, B07 STREAM_NOTES.md in full, my rolling status/learned file and prior proof, and execution protocol revision 2026-10-11-execution-v2. The lead's generic-probability calibration objection is accepted: the stage-1 point-defect constant was not evidence of Boolean-specific improvement. Read A033's full A031 independent review and A088 AUDIT.md's A031 section/CLAIMS records; both independently accepted the two prior v1 claims at their precise scopes, subject to supervisor adoption. Read B05 lead STREAM_NOTES.md and the completed run 20261011T225000Z report, Lemmas 1-2 and localized Theorem 4 in particular. Its transient _body.md was absent, then the completed REPORT.md was available and read; no access blocker remains. Rechecked ERASURE_REDUCTION sections 1-2 (C005) and use ERASURE_RIGIDITY section 2 only as source context for the explicitly rederived bent-surgery calculation. Local hashes and exact paths: out/SOURCE_MANIFEST.json. No literature priority claim is made.

## complete derivation or exact first unsupported line
PHASE_ERASURE.md supplies a complete all-dimensional finite-sum derivation. All signed mixed convolutions vanish before the phase square is made real and its energy evaluated. The bound retains spectral-sector KL credit M AND physical isoperimetric deficit R. A normalized real rational vector violates the bound, proving that normalization alone cannot give it. Bent one-point surgery forces coefficient 1/2 on I(F^2), and dense bent phases refute any universal aggregate Q_sum-a sum M<=K I. The known B05 uncredited scalar bound is explicitly credited to its source and independently reconstructed, not counted as new. The all-coordinate total Q_sum is twice B05's Q_odd; the tree interface includes that normalization and every terminal leaf. The first unsupported line is an influence-paid universal joint-credit positive-excess tree budget, or equivalently an influence-paid aggregate residual for C018. Neither is proved. The obstruction does NOT refute B05's localized bad-node tree target.

## executed validation with domain, arithmetic, commands and outputs
Frozen phase pilot: {pilot['cases']} cases, {pilot['integer_assertions']} assertions, {pilot['runtime_seconds']:.3f} seconds. Full fixed census: {v['cases']} actual Boolean split tables on n=1..4, {v['integer_assertions']} assertions, {v['runtime_seconds']:.3f} seconds; no symmetry reduction and no dimension escalation. The distinguished-coordinate encoding covers every Boolean truth table, and other queried coordinates occur after relabelling. Integer real/imaginary Walsh transforms check ALL shifts, signed imaginary cancellation, physical cut versus convolution energy, and exact formal-log coefficients of B_i+M_i=h2(d); edge-isoperimetric comparisons use proved rational logarithm intervals. Separate exact certificates cover dense bent r=2,4, bent surgery m=2,4,6 and the normalized non-Boolean violation. Their displayed floats are not sign certificates. Full rational intervals and their generating code are saved in out/certificates.json.
Commands: python -X utf8 code/check_phase.py --pilot, then --full. A separate pre-frozen tree check ran python -X utf8 code/check_tree.py: {t['total_cases']} complete trees, {t['assertions']} assertions, {t['runtime_seconds']:.3f} seconds, through n=8. It independently counts physical odd faces and checks exact rational influence, formal-log entropy/JS, and complete-tree scalar credit cancellation. Outputs: out/pilot.json, out/validation.json, out/certificates.json, out/tree_validation.json. The census was under its 300-second frozen cap; pilot and tree checks under 60 seconds. Estimated memory below 60 MB, one census job at a time, no job crossing 300 MB, no GPU or background helper.

## proof dependencies and changed downstream conclusions
The new local phase identity and Boolean counterfamilies are self-contained. The tree interface uses C005 and B05-ODDFACE-TELESCOPE v1, independently reconstructed by A031 without a repair to the original. Source-bound acceptance of B05-ODDFACE-ISO-PAYMENT and B05-ODDFACE-TELESCOPE is recorded in B05_INDEPENDENT_REVIEW.md and CLAIMS.json; broader B05 payment remains open. Prior A031 versions are preserved and only observed review receipts are imported into this run. Two new narrow repair/refutation records await independent review; no new broad universal positive candidate is opened amid B07's existing review queue. Changed downstream conclusion: a spectral-KL-only aggregate boundary payment is invalid even on flat Boolean spectra. Physical isoperimetric slack must remain in that currency, or payment must be localized to genuinely bad nodes. No other worker or shared index was edited.

## one next mathematical action and independent reviewer
On the B05 lead's nested rare-flip tower, compute the joint-credit excess D_K=[W-R-M-sigma-(K-log2(e))d]_+ at actual bad nodes with terminal entropy reserved; then seek a nonreusing ownership/selection proof of its expected payment. Reviewer: A088 for the phase identity and dense-bent obstruction; A087 or A094 for the C019 terminal/factor-of-two interface. This is a saved handoff, not a tool-sent message.

## actual persistence receipts or precise save blocker
The prescribed REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are local, with code and out subdirectories. out/SCHEMA_CHECK.json verifies the protocol field sets and compatibility equality. out/ARTIFACT_RECEIPTS.json records local sizes and SHA256 hashes. STATUS.md has the required two lines; WORKLOG.md is appended and LEARNED.md records the correction and durable phase facts. No local save blocker exists. Supervisor mirror, registry adoption, independent acceptance of the new claims and downstream use are not inferred.

## Universal bridge

This stage moves the B07 lead's fourth-root coordinate target directly into C018 and the C019 stopping-tree interface: it identifies the exact two-credit residual, proves the local boundary coefficient 1/2 cannot improve, and eliminates the false spectral-credit-only aggregate payment through a fully Boolean unbounded family. It supplies no new absolute FEI constant. The remaining obligation is a universally influence-paid joint-credit positive-excess tree bill with terminal reserves; the exact aggregate identity is C018-strength and remains unpaid. NEXT uses the nested rare-flip stress family already selected by B05 and retains both credits before taking a positive part, so it tests the precise surviving sufficient universal mechanism instead of generating another isolated class theorem. A successful ownership/selection proof there must still extend to arbitrary Boolean nodes; numerical or finite success alone will not establish that extension.
'''
(R/'REPORT.md').write_text(report,encoding='utf8')
(A/'STATUS.md').write_text('STATE: A031 stage 2 complete: fourth-root phase credits and sharp coefficient proved; spectral-KL-only aggregate payment refuted; 65812 splits/1445290 exact assertions plus 10 trees checked; review pending; FEI OPEN.\nNEXT: Test joint-credit positive excess on B05 nested rare-flip trees with terminal reserves; A088/A087/A094 review, then seek nonreusing C018/C019 ownership or selection.\n',encoding='utf8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf8') as f:f.write(stamp+': Stage 2 followed B07 fourth-root phase target, accepted generic-probability calibration correction, derived exact R+M+sigma credit ledger, coefficient 1/2 sharp, dense bent no-go for spectral-credit-only aggregate. 65812 split tables/1445290 assertions; 10 trees/2650 assertions; source-bound B05 Lemmas 1-2 independently accepted; new claims review pending; universal joint-credit payment OPEN.\n')
with (A/'LEARNED.md').open('a',encoding='utf8') as f:f.write('\nStage 2 correction: point-defect H-Hinf<=4I+o(I) calibration also follows from the generic probability inequality pmax(H-Hinf)^2<=(1-pmax)Var(ell); it was not evidence that Booleanity supplied the improvement. Anchor/Cauchy payment is retired.\nFor F=A+iV from actual Boolean children, full signed constraints A^2+V^2=1 and AV=0 give F^4=1 and real Boolean F^2. W_i=I(F^2)/2=2 sum_U |U|(v*v)(U)^2 is signed phase-boundary energy. B_i=W_i+log2(e)d-R_i-M_i-sigma(d), with physical isoperimetric deficit R_i>=0 and spectral-sector KL M_i>=0. The bound excluding normalized vector (4/5,3/5) uses actual Booleanity; coefficient 1/2 on I(F^2) is sharp by bent one-point surgery.\nDense invertible quadratic phases f_r=(-1)^(x^T(I+J)y), r even, have H=2r,I=r,M_i=0,W_i=(r-1)/2,R_i=(r-2)/2. Therefore (sum_i W_i-a sum_i M_i)/I=r-1 diverges for any fixed a, but subtracting R leaves I. Do not route this all-coordinate obstruction as a refutation of localized bad-node tree payment. Q_sum=sum_i W_i=2Q_odd, whereas a tree spends Q_odd once. The surviving universal target retains R,M,sigma before the positive part and preserves terminal H,I,Q_odd.\n')
receipts=[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in R.rglob('*') if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json']
assert max(p['bytes'] for p in receipts)<20*1024*1024
write('out/ARTIFACT_RECEIPTS.json',receipts)
print(json.dumps({'saved_artifacts':len(receipts),'new_claims':2,'reviewed_or_imported_versions':4,'validation_cases':v['cases'],'protocol_schema':'PASS','run':str(R)},indent=2))
