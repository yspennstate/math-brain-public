from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1];agent=root.parents[1]
rid=root.name
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
validation=json.loads((root/'out/validation.json').read_text(encoding='utf-8'))
pilot=json.loads((root/'out/pilot.json').read_text(encoding='utf-8'))
statement=('For F=sum_j C_j u_j with a finite exclusive controller partition and pairwise disjoint independent Boolean data cores, '
'every finite adaptive physical tree interleaving data and controller queries admits U=sum q_j[H(u_j)-eta(m_j^2)] and R=sum q_j log2(1/q_j)(1-m_j^2). '
'At a controller query, U is a martingale and kappa=R-E R_child=sum_j q_j V_j D_2(P(X|C_j)||uniform)>=0. '
'At a data query in core j, R-E R_child=q_j log2(1/q_j)beta_j^2 and D_iH(F)<=U+R-E(U_child+R_child)+(3/ln2)q_j beta_j^2. '
'Hence R_root=E R_leaf+sum_data w q_j log2(1/q_j)beta_j^2+sum_controller w kappa, '
'and sum_data w cap+E R_leaf+sum_controller w kappa<=((1+2/e)/ln2)Pi_data+R_root, with R_root<=2I_ctrl(root). '
'The full stopped entropy bound retains E H(F_leaf), U_root-E U_leaf, R_root-E R_leaf and sum_controller w(DH-kappa); no universal price for that residual is asserted.')
hyp=['Finite uniform physical cube; independent disjoint controller and data blocks, each selected core on its own physical cube; Boolean sign outputs.',
'Exclusive selector indicators C_j partition controller assignments; constant output states and biased core outputs are permitted.',
'Each adaptive tree step queries one currently unrevealed physical coordinate and children have fair reach probabilities; arbitrary stopping frontiers and interleavings.',
'H, eta and KL use bits; eta(x)=x log2(1/x). Endpoint caps and zero-probability terms are zero. Shared physical DATA between cores is excluded.']
claim={'claim_id':'A059-INTERLEAVED-BIASED-STOPPING-RESERVE','version':1,'exact_statement':statement,'hypotheses':hyp,
'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
'contributors':['A059','A056/A057 upstream recentered split and positive cap envelope'],
'proof_source':{'run':rid,'path':'PROOF.md','locators':'Sections 1-4; growing-depth test Section 5'},
'proof_dependencies':[{'claim_id':'A056-BIASED-ERASURE','version':2,'scope':'exact signed row split/envelope independently reconstructed here'},
{'claim_id':'A057-EXCLUSIVE-SELECTOR-VARIANCE-CAP-PAYMENT','version':1,'scope':'Sections 1,3,4 independently accepted locally; fresh suffix subclaim not reviewed'},'Elementary physical variance/influence conservation, selector KL concavity and indicator isoperimetry'],
'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
'first_unproved_line':None,'next_consumers':['A056','A057','A091','A090','A024','A064','A097','B12','B20']}
save(root/'CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':rid,'stream':'B12','packet_id':'A059',
'gap_id':'G-A059-DECOMPOSITION-DEPTH','attempt_id':'A059-depth-2','method':'Physical selector reserve supermartingale, exact controller KL reset and signed empty-core cancellation; independent A057 cap reconstruction',
'mathematical_delta':'Extends data-only capped reserve to arbitrary adaptive controller/data interleaving with biased terminal reserves; full signed data drift price 3/ln2 after exact singleton-log cancellation; controller entropy residual remains explicit.',
'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_STOPPING_THEOREM; FULL_FEI_OPEN',
'claim_versions_used':['A056-BIASED-ERASURE-v2','A057-EXCLUSIVE-SELECTOR-VARIANCE-CAP-PAYMENT-v1 (cap/coherent subclaims reviewed here)','A059-GATE-VS-SUBFORMULA-DEPTH-LEDGER-v1 (nonreuse guard)'],
'claims_created_or_changed':['A059-INTERLEAVED-BIASED-STOPPING-RESERVE-v1'],
'source_artifacts':['REPORT.md','PROOF.md','REVIEW_A057.md','code/check.py','out/FROZEN_SPEC.json','out/validation.json','out/REVIEWS.json'],
'next_consumers':['A056','A057','A091','A090','A024','A064','A097','B12','B20'],
'next_action':'Price the actual signed controller residual D_ctrl-kappa together with the biased stopping terminal using one exclusive control/core reserve; first test point-controller activation with an arbitrary retained core.',
'stagnant_substantive_attempts':0,'blockers':['No universal controller-residual/terminal entropy payment; shared data independence still excluded.'],'packet_ids':['A059']}
save(root/'PROGRESS.json',progress);save(root/'PACKET_DELTA.json',progress)
save(root/'out/REVIEWS.json',[{'claim_id':'A057-EXCLUSIVE-SELECTOR-VARIANCE-CAP-PAYMENT','version':1,'reviewer':'A059','verdict':'ACCEPT_SUBCLAIMS_AT_STATED_SCOPE','locators':'PROOF.md Sections 1,3,4; fresh suffix subclaim excluded','source':'REVIEW_A057.md','contributor_to_reviewed_version':False,'method':'Independent conditional entropy/edge reconstruction and fresh actual-restriction checker; source code not imported'}])
report=f'''# exact target, quantifiers, hypotheses and units

A059 B12 decomposition-depth continuation. Prove a stopping frontier with biased terminals, following B12 lead v2 and consuming the now-completed A056 biased split. The new theorem extends A057's independent-core selector reserve from data-only prefixes to ANY finite adaptive interleaving of data and controller queries. Both actual terminal entropy and the terminal selector reserve are retained. H and KL are bits; physical influence is uniform sign-flip probability. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-13 23:59 UTC, B12 STREAM_NOTES v2 (2026-10-11 23:30 UTC), own STATUS/LEARNED, and the full EXECUTION_PROTOCOL revision 2026-10-11-execution-v2. The board's B12/B13 and B05/A024/A095 stopping/ownership reports were used as navigation only. Read actual A056 stage3 REPORT (20261013T215801Z), A056 stage2 BIASED_ERASURE_INTERFACE.json (20261011T233147Z), and A057 stage3 REPORT, PROOF and CLAIMS (20261013T221645Z). Read own prior depth theorem and preserve the no-whole-subformula-charge obstruction. Previous campaign/paper readings remain recorded in the earlier run; no new outside literature input is used. out/SOURCE_RECEIPTS.json pins the source bytes. An attempted .md interface lookup failed because the actual A056 interface is .json; the correct file was then read. No mathematical access blocker remains.

REVIEW_A057.md independently reconstructs the cap and coherent-outer subclaims at their data-only independent-core scope, before this narrow continuation candidate. The separate fresh-activation suffix subclaim is not independently accepted here. This obeys the lead/protocol review-at-cap instruction without claiming a full-chain review of a subclaim not reconstructed.

# complete derivation or exact first unsupported line

PROOF.md gives the full proof. Let F=sum C_j u_j with exclusive controller states and disjoint independent data cores. At a reached physical cylinder set U=sum q_j[H(u_j)-eta(m_j^2)] and R=sum q_j log2(1/q_j)V_j. No balance assumption is made. A controller query preserves U in expectation and releases kappa=sum q_j V_j D_2(P(X|C_j)||fair)>=0. A data query in core j consumes exactly q_j log2(1/q_j)beta_j^2 from R. Therefore R_root=E R_terminal+sum data losses+sum controller kappa for every finite stopping tree, regardless of interleaving or depth.

The signed inner term in A056's biased split is exactly U-E U_child-q_j eta(beta_j^2). A057's cap inequality contains the positive q_j eta(beta_j^2). They cancel before any singleton-log influence price is applied. The full data decrement is at most the change in U+R plus (3/ln2)q_j beta_j^2. This removes the 2/e surcharge for the FULL SIGNED DATA step, not for the standalone positive cap. The positive cap itself has the stopped price sum data cap+E R_terminal+sum controller kappa<=c_data Pi_data+R_root, c_data=(1+2/e)/ln2. Initial reserve funding R_root<=2I_ctrl follows from indicator isoperimetry and actual independent-core mismatch edges.

The theorem's full entropy inequality keeps the exact signed controller residual sum w(D_ctrl-kappa) and the actual terminal H,U,R corrections. The SAME physical influence telescope retains terminal influence. The reserve is funded once; neither controller residual nor terminal entropy is silently paid again from 2I_ctrl. All bias endpoints, zero selector probabilities and constant cores are defined without division. A point-controller/parity-core family with arbitrary growing r+m, interleavings and biased constant terminal cores tests the all-depth theorem. Its existing H<=6I activation bound is only calibration, not advertised as new closure.

First unsupported universal line: the signed controller residual plus its actual stopping terminal and U correction is paid by an exclusive unspent physical influence reserve. If all selected cores are constants then U=R=kappa=0 and this reduces to the entropy path of an arbitrary Boolean controller, so no universal resolution is inferred. Shared physical DATA cores are also excluded; initial edge funding uses their independence.

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before execution. Pilot: {pilot['roots']} roots, {pilot['trees']} trees, {pilot['assertions']} exact assertions PASS, {pilot['elapsed_seconds']:.6f}s. Main: {validation['roots']} roots, {validation['trees']} complete trees with EVERY depth frontier also checked, {validation['assertions']} exact assertions PASS, {validation['elapsed_seconds']:.6f}s. Domain: all 81 three-label maps on two controllers times all 16 ordered one-bit-core pairs (1296 roots), plus two point/priority maps times all 16 two-bit first cores and four one-bit second cores (128 fixtures). Four policies on primary roots include controller-first, data-first, alternating and adaptive maximum actual influence; two interleaved/adaptive policies on fixtures. No symmetry quotient or random sampling. Maximum truth table: five bits; no dimension escalation.

Commands from this run: python -X utf8 code/check.py --pilot; python -X utf8 code/check.py. The checker independently builds actual root/child spectra, selector/core states and Fourier rows with integer FWHT and Fraction arithmetic. Prime-log coefficient vectors verify exact identities; 32-term rational atanh-series with a proved geometric tail verifies signs. The finite standalone cap checks use the slightly weaker 2-nat coefficient rather than certifying 1+2/e numerically; the sharp constant follows analytically. Node tests include the signed empty-row cancellation, cap envelope, raw JS, exact physical conditional-KL reset, initial funding and same-tree influence conservation. Every depth frontier checks stopped reserve identity, full signed entropy bound and positive cap with terminal reserve. Zero selector/variance and constant-output states occur throughout the full domain. Memory estimate 120 MB, not a measured peak; no >300 MB job or heavy search was launched. Pilot was under 60s and main under the frozen 180s budget. Code corrections to the terminal condition and addition of the already-frozen KL/funding assertions occurred before main execution; no mathematical domain changed.

# proof dependencies and changed downstream conclusions

A056's biased interface and A057's selector cap envelope are used only at their stated independent physical-block scope and rederived in PROOF Sections 2-3. Their exact negative inner pair is essential to the 3/ln2 drift. The new KL reserve-reset proof and its stopping conservation are local to this run. The source A057's last scope paragraph contains a stale priority-only sentence despite its Section 3 arbitrary-controller proof; REVIEW_A057 records this editorial inconsistency and follows the actual theorem statement, without changing or repairing source files.

A057 may now move beyond its data-only prefix limitation for the SAME positive cap bank. A024/A064/A097 can use the exact U and R stopping identities with actual biased terminals; formula weights from the earlier A059 tree are not substituted for physical reach probabilities. A056 can attach either controller-first or interleaved frontiers while retaining the controller residual. These are source-bound handoffs, not claims of downstream adoption. New independent review is pending A091/A090. No universal FEI constant changes.

# one next mathematical action and independent reviewer

Price D_ctrl-kappa on a point-controller activation with an arbitrary core retained at the biased frontier, including its exact terminal H-U-R correction and one exclusive control budget. This isolates the only query type left unpriced by the new data drift; do not reprice the positive singleton bank or repeat activation closure. A091 primary reviewer, A090 alternate; A057/A024 should challenge the signed inner cancellation and terminal reserve.

# actual persistence receipts or precise save blocker

REPORT, PROOF, REVIEW_A057, CLAIMS, PROGRESS and identical PACKET_DELTA, code, frozen spec and outputs are saved only in A059's assigned stage directory. STATUS has two lines; WORKLOG and LEARNED append the new facts. out/SCHEMA_CHECK.json verifies exact protocol field sets and digest; out/PERSISTENCE.json records byte lengths and SHA256 readback receipts. Every file is below 20 MB. No shared tree, other agent, brain store, git repository, mail or trading files were modified. Supervisor copying, registry adoption, new independent review and remote mirror verification remain pending; no local save blocker exists.

# Universal bridge

This stage moves C019 stopping-tree payment by proving an exact controller-query KL reset and a depth-independent selector reserve for arbitrary adaptive interleavings with biased terminal cores; exact negative empty-core cancellation improves the signed DATA drift to 3/ln2 without a repeated singleton-log charge. The remaining signed controller entropy and actual terminal H-U-R ledger are explicit and unpaid, and shared data is excluded. NEXT prices precisely that remaining controller step against one exclusive reserve on an arbitrary-core activation, the shortest continuation toward the universal policy rather than another isolated formula-class bound.
'''
(root/'REPORT.md').write_text(report,encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
(agent/'STATUS.md').write_text(f'STATE: A059 interleaved biased stopping reserve and exact controller KL reset proved locally; signed data drift <=3/ln2; {validation["assertions"]} exact checks PASS; full FEI OPEN.\nNEXT: A091/A090 review; price D_ctrl-kappa plus actual biased terminal H-U-R on arbitrary-core point activation with one exclusive control budget.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(f'\n{stamp} | {rid}: consumed A056 biased interface and A057 stage3 cap; independently accepted cap/coherent subclaims. Exact variance-weighted selector KL release now handles arbitrary controller/data interleaving. Negative empty-core pair cancels eta(beta^2), leaving signed data drift 3/ln2. {validation["roots"]} roots/{validation["trees"]} trees/{validation["assertions"]} exact checks PASS. Controller residual and actual terminal remain unpaid; no shared-data claim.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nInterleaved stopping (A059 stage2): U=sum q[H(core)-eta(mean^2)] is a controller-query martingale. R=sum q log2(1/q)Var(core) has exact data loss q log2(1/q)beta^2 and controller release sum q Var D_2(P(bit|state)||fair)>=0. R_root=E R_leaf+all data losses+all controller releases, even under adaptive interleavings. The signed data entropy decrement <=drop(U+R)+(3/ln2)q beta^2: positive eta(beta^2) cancels the negative inner empty pair before pricing. Initial R<=2I_ctrl is funding once, not a second allowance for controller entropy. Remaining controller residual is D_ctrl-kappa and actual terminals H,U,R must be retained. All selected core data cubes must be disjoint.\n')
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected;assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()
save(root/'out/SCHEMA_CHECK.json',{'status':'PASS','claim_fields':len(claim),'progress_fields':len(progress),'compatibility_equal':True})
sourcepaths=[Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B12\STREAM_NOTES.md'),Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
base=Path(r'~\brain_workers\FEI100_20261011\agents')
sourcepaths+=[base/'A056/runs/20261011T233147Z-fleet05-A056-balanced-composition/BIASED_ERASURE_INTERFACE.json',base/'A056/runs/20261013T215801Z-fleet05-A056-balanced-composition/REPORT.md']
sourcepaths+=[base/'A057/runs/20261013T221645Z-fleet05-A057-coherent-restriction-remainder'/x for x in ['REPORT.md','PROOF.md','CLAIMS.json']]
save(root/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sourcepaths])
receipts=[]
for p in sorted(root.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE.json':
  b=p.read_bytes();assert len(b)<20*1024*1024;receipts.append({'path':str(p.relative_to(root)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
for n in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 p=agent/n;b=p.read_bytes();receipts.append({'path':'../../'+n,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save(root/'out/PERSISTENCE.json',{'created_utc':stamp,'readback':'PASS','mirror_verified':False,'receipts':receipts})
print(json.dumps({'status':'PASS','files':len(receipts),'assertions':validation['assertions'],'schema':'exact protocol fields'}))
