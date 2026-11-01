from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
run=Path(__file__).resolve().parents[1]; root=run.parents[1]
campaign=root.parents[1]
protocol=Path(r'~\mop_fei100\reports\fei-2026-10-11/EXECUTION_PROTOCOL.json')
P=json.loads(protocol.read_text(encoding='utf-8'))
def save(name,obj):
    (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
check=json.loads((run/'out/CHECK.json').read_text(encoding='utf-8'))
ind=json.loads((run/'out/INDEPENDENT.json').read_text(encoding='utf-8'))
assert check['status']==ind['status']=='PASS'
statement=('For every k>=2 and Boolean h, F(x,z)=1+1[z=0^k](h(x)-1) is affine spectral influence-minimal iff '
'Pr[h(x)!=h(x+u)]>=max_{i:u_i=1}Inf_i(h) for every nonzero data direction u. '
'Every affine-minimal seed and all its independent tensors satisfy this criterion. For every fixed eta,epsilon,tau>0 and K>=0, '
'uniform FEI(K) is equivalent at the SAME K to FEI(K) on Boolean signs having full affine spectral span, affine spectral influence-minimality, '
'mean>=1-eta, I<=epsilon and max_i Inf_i<=tau. An arbitrary positive-entropy seed is compressed/minimized to g with H(g)=H(f), I(g)<=I(f); '
'activating g^tensor(t) with k=max(2,ceil(sqrt(t))) preserves these structural conditions and its ratio tends to H(g)/I(g)>=H(f)/I(f). '
'These admission roots are not certified minimal-dimensional maximal-deficit witnesses.')
claim=dict(claim_id='A002-AFFINE-MINIMAL-RARE-ADMISSION',version=1,exact_statement=statement,
hypotheses=['finite uniform F_2 cubes; Boolean signs; normalized Walsh spectrum; entropy bits','k>=2 for the exact activation criterion','fixed positive rarity/weakness thresholds; K>=0','seed H>0 only for the ratio construction; constants satisfy FEI directly'],
statement_sha256=hashlib.sha256(statement.encode()).hexdigest(),contributors=['A002'],proof_source='ADMISSION_PROOF.md Sections1--6',
proof_dependencies=['A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1: only affine compression/minimum-basis characterization; independently reconstructed in ADMISSION_PROOF.md Section5','finite Parseval and entropy chain/multiplicity calculations'],
review_records=[{'reviewer':'A002','scope':'author analytic re-derivation; integer/Fraction exact checks; independent direct-character implementation by same author, not independent agent review','result':'PASS; Lean RUNTIME_UNVERIFIED'}],
status='AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line='Universal selected proper-pair payment from actual finite maximality and lower-dimensional nonviolation, spending SAME D_K+S_A and complete terminals.',next_consumers=['A005','A051','A052','A055','A090','A094'])
save('CLAIMS.json',[claim])
progress=dict(protocol_revision=P['revision'],run_id=run.name,stream='B01',packet_id='A002',gap_id='G-R-SELECT',attempt_id='A002-stage7-affine-minimal-activation',method='Exact directional autocorrelation criterion plus affine compression/minimization, independent tensors and rare activation; finite exact certificates.',mathematical_delta='SAME-K arbitrary-seed admission survives new affine-minimum-basis/full-affine-span constraints jointly with arbitrarily fixed rare/weak thresholds; no critical-witness admission or universal payment.',deliverable_status='COMPLETE_LOCAL',mathematical_status='NARROW_ADMISSION_THEOREM_AUTHOR_CHECKED; FULL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',claim_versions_used=['A051-AFFINE-MINIMUM-BASIS-CRITICAL-REDUCTION@1 (scoped Sections2--3 reconstruction)'],claims_created_or_changed=[claim['claim_id']+'@1'],source_artifacts=['ADMISSION_PROOF.md','out/CHECK.json','out/INDEPENDENT.json','out/SOURCE_MANIFEST.json','out/GUARD_CORRECTION.json','out/LEAN.json'],next_consumers=claim['next_consumers'],next_action='A051/A052 combine actual finite maximality and lower-dimensional nonviolation with signed Boolean pair convolution to pay one original proper pair from SAME unused D+S_pair; A090/A094 review admission and criterion.',stagnant_substantive_attempts=0,blockers=['No full FEI proof or Boolean counterfamily','Actual critical witness cannot be replaced by these roots; active restrictions recover seed debt','Independent agent review, registry adoption and supervisor mirror not verified','Lean scalar attempt runtime unverified'],packet_ids=['A002'])
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
save('out/LEAN.json',{'statement':'example (p d : ℝ) (hp : 0 ≤ p) (hq : p ≤ 1/4) (hd : 0 ≤ d) (he : d ≤ 2) : p*d ≤ 1/2 := by nlinarith','status':'RUNTIME_UNVERIFIED','seconds':53.2,'source_sha256':'6676950ceb36d92b23b544c575208f96bd446c9fda9e7bee0db69d01b1a72165','scope':'only scalar p delta<=1/2; no Lean claim, target translation or axiom acceptance'})
report=f'''# exact target, quantifiers, hypotheses and units

A002/B01 stage7 consumes the new A051 affine-minimum-basis endpoint. For every finite uniform Boolean seed, determine whether simultaneous affine spectral influence-minimality, full affine spectral span, and arbitrarily fixed rare/weak thresholds still admit its entropy debt. Entropy is in bits. ADMISSION_PROOF states the exact quantifiers, k>=2 boundary and SAME-K equivalence. Full FEI remains OPEN. The current owner deadline23October2026 14:49UTC supersedes the older read-only protocol clock.

# sources actually read, revisions and theorem locators

Execution protocol2026-10-11-execution-v2 read fully; README/CURRENT_STATUS, registry/packet excerpts and B01 next-action/plan A002 acceptance text inspected. Current BOARD, own STATUS/LEARNED and latest actual A002 stage6 REPORT/INTERACTION_PROOF read. B01 STREAM_NOTESv1 has retired the basic ledgers and requested near-erasure admission, already settled in earlier A002 stages. Protocol dispatch therefore consumes the new A051 stage7 AFFINE_SELECTION Sections1--6 and A00521October REPORT, rather than repeating old ledgers or the finite quartet census. Supplement campaign/claims/counterexamples/seed/mapping introductions and source inventory inspected; scope/composition excerpts of all four supplied paper versions refreshed with explicit cp1252 decoding. No manuscript theorem or web premise is newly used. A read-only two-wording math recall returned background, not an activation/minimum-basis theorem. Wake warned that owner-model/state notes were stale; current instructions govern. Source hashes in out/SOURCE_MANIFEST.json; mutable source hashes are finalization observations, not immutable revisions.

# complete derivation or exact first unsupported line

ADMISSION_PROOF Sections1--6 prove the exact all-direction activation criterion, tensor stability, complete Fourier/entropy/influence ledgers, full-span survival and SAME-K hardness. For activation probability p=2^-k, w_F(u,0)=p w_h(u) and w_F(u,v)=p(1-Eh) for v!=0. All costs are <=1/2 at k>=2, so affine minimality is exactly the raw directional condition. The remaining side condition Inf_i(h)<=1-Eh follows from Boolean disagreement events. Independent tensors preserve the stronger minority-basis inequalities. Compress/minimize the arbitrary seed to g, then activate g^t with k=max(2,ceil sqrt(t)); H/I tends to H(g)/I(g)>=H(f)/I(f), while I->0, mean->1 and all structural constraints persist. Remainders have uniform elementary bounds. A051 Sections2--3 receive a scoped independent analytic reconstruction, not acceptance of selected pair payment.

FIRST UNSUPPORTED UNIVERSAL LINE: actual finite maximality AND lower-dimensional nonviolation must select a proper physical pair paid from SAME D_K+S_pair with complete terminals. The constructed roots fail criticality because proper active restrictions recover a violating seed. No such eligibility is asserted. This is a hardness-map result, no universal FEI constant improvement.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs precede jobs. From A002: python -X utf8 runs/{run.name}/code/check.py --pilot; then without --pilot; then code/independent.py in the same run. Pilot22 seeds/382 assertions PASS in0.0490s. Full278 labelled seeds n0..3,270 nonconstant activation fixtures,48 extra fixed tensor/control fixtures, three named activation guards: {check['assertions']} assertions PASS in{check['seconds']:.4f}s. All spectral directions are tested, not only pairs. Integer FWHT/Fraction probabilities and prime-log linear entropy expressions check every coefficient, influence and entropy multiplicity. Independent direct-character plus all physical translation edges: {ind['fixtures']} seed fixtures/{ind['assertions']} assertions PASS in{ind['seconds']:.4f}s. Same author, separate implementation; not independent agent review.

The first full job correctly rejected a mistaken negative guard for activated majority3. The criterion and coefficient arithmetic were unchanged; majority3 is now the positive guard, parity2 the negative guard. out/GUARD_CORRECTION records the failure; only the subsequent full PASS is counted. Constants, zeros, ties, mu=0 and k1 negative-constant boundary are explicit. No floating-point sign decision. Each job has55s cap, estimated40--70MB RAM; observed peak unmeasured; no>300MB job, GPU, detached process or dimension escalation. Compute status was ok, CPU high, about11GB memory available. Lean scalar attempt returned RUNTIME_UNVERIFIED after53.2s; no formal certification claimed. Proof rung: author-checked analytic proof plus exact finite certificates, independent review pending.

# proof dependencies and changed downstream conclusions

Only A051 affine compression/orbit criterion is used and is independently rederived in Section5. No unproved FEI inequality, erasure payment or external theorem is a premise. The new theorem is a narrow continuation of the existing admission ledger, not another claimed full-FEI proof. Root affine optimality and full span are now shown insufficient to remove arbitrary entropy debt even jointly with rarity/weakness. The complete critical child bank remains unpaid. Physical input blocks are independent in the tensor construction; squared spectral coordinates within each seed block may be correlated.

# one next mathematical action and independent reviewer

A051/A052 should combine finite maximality, lower-dimensional nonviolation and signed Boolean pair convolution to pay one ORIGINAL proper physical pair from the SAME unused D+S_pair bank, retaining both complete terminals. A090/A094 independently review the activation criterion, tensor stability and same-K limit; A005/A055 consume the circularity guard. No messages sent; local source-bound handoff only.

# actual persistence receipts or precise save blocker

Four protocol files, proof, frozen specs, code and exact outputs saved under A002 only. code/finalize.py checks exact protocol field sets, byte-identical PROGRESS/PACKET_DELTA, statement hash, required report headings and20MB cap; out/PERSISTENCE_RECEIPT hashes files and rolling records. STATUS has two lines, WORKLOG/LEARNED updated. Independent agent review, registry adoption, supervisor copy and remote mirror remain unverified. No local save blocker.

## Universal bridge

C019 stopping-tree payment through B11's critical-pair frontier: the new affine minimum-basis/full-span reduction is now proved to remain SAME-K FEI-hard even under simultaneous rare and weak root thresholds. The exact all-direction activation criterion closes this admission question; zero universal entropy is newly paid. What remains is actual criticality and its signed complete child reserve. NEXT uses lower-dimensional nonviolation and finite maximality on one unchanged bank because another root affine-symmetry estimate cannot remove the arbitrary tensor debt demonstrated here.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
(root/'STATUS.md').write_text('STATE: A002 stage7 saved: exact all-direction activation criterion; SAME-K rare/weak/full-span affine-minimal admission; '+str(check['assertions']+ind['assertions'])+' exact checks PASS; FEI OPEN, review pending.\nNEXT: A051/A052 pay one ORIGINAL critical proper pair using finite maximality and lower-dimensional nonviolation from SAME D+S_pair bank; A090/A094 review new admission.\n',encoding='utf-8')
with (root/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' stage7: consumed A051 affine reduction; proved exact raw-direction activation criterion and SAME-K simultaneous rare/weak/full-span affine-minimal admission. Full checker '+str(check['assertions'])+' + direct independent '+str(ind['assertions'])+' assertions PASS. Initial majority3 negative guard failed because activation repairs it; corrected guard preserved in out/GUARD_CORRECTION. Lean runtime unverified; no selected pair or FEI proof.\n')
with (root/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage7: For k>=2 rare activation F=1+1[z=0](h-1), wF(u,0)=p wh(u), wF(u,v!=0)=p(1-Eh). F is affine-minimum-basis iff wh(u)>=max_{i:u_i=1}Inf_i(h); the other condition Inf_i<=1-Eh is automatic Booleanity. Affine-minimal seeds and their tensors satisfy this. Compression/minimization then activation with k=ceil sqrt(t) proves SAME-K hardness jointly with full affine span, arbitrary fixed rare/weak thresholds. Activated majority3 repairs minority minimality and affine rank; activated parity2 fails. These roots fail critical child eligibility: active restrictions recover violating seed. NEXT must use actual finite maximality/lower-dimensional nonviolation and same complete D+S_pair, not root affine constraints alone.\n')
sources=[protocol,campaign/'BOARD.md',campaign/'claude/B01/STREAM_NOTES.md',campaign/'agents/A051/runs/20261021T193146Z-fleet03-A051-near-extremizer-definition/AFFINE_SELECTION.md',campaign/'agents/A005/runs/20261021T155809Z-fleet03-A005-noncircular-endpoint-referee/REPORT.md',root/'runs/20261014T100104Z-fleet05-A002-hardness-preserving-transformations/INTERACTION_PROOF.md']
save('out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'observed_at':stamp} for p in sources])
assert set(progress)=={x.split(' (')[0] for x in P['required_per_run']['progress_fields']}
assert set(claim)==set(P['required_per_run']['claim_fields'])
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert all('# '+h in report for h in P['required_per_run']['report_fields'])
assert len((root/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipts=[]
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
        b=p.read_bytes();assert len(b)<20_000_000
        receipts.append({'path':str(p.relative_to(run)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
save('out/PERSISTENCE_RECEIPT.json',{'status':'PASS','utc':stamp,'schemas':'exact protocol sets; required headings; identical compatibility copy; statement hash; two-line STATUS; <20MB files','local_only':True,'artifacts':receipts})
print(json.dumps({'status':'PASS','run':str(run),'assertions':check['assertions']+ind['assertions'],'files':len(receipts),'full_fei':'OPEN'}))
