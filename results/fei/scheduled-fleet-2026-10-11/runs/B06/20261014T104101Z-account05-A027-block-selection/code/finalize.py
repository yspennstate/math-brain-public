import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
run=Path(__file__).resolve().parents[1]; agent=run.parents[1]; team=agent.parents[1]
previous=agent/'runs'/'20261014T043519Z-account05-A027-block-selection'
protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
now=datetime.now(timezone.utc).isoformat()
def dump(name,obj): (run/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
v=json.loads((run/'out'/'validation.json').read_text()); pilot=json.loads((run/'out'/'pilot.json').read_text()); tree=json.loads((run/'out'/'trees.json').read_text())
assert v['status']==pilot['status']==tree['status']=='PASS'
assert v['exhaustive_cases']==1296 and tree['trees']==396
claims=json.loads((previous/'CLAIMS.json').read_text(encoding='utf-8'))
old=next(c for c in claims if c['claim_id']=='A027-PARTIAL-CORE-ACTIVATION-TRANSPORT')
extension=(' Version5 retains prior components and proves a sharp signed low-bias admission band. For any independent Boolean controller a with p=Pr(a=-1) in[0,1/2], the exact activation remainder R(p,d) is convex for0<=d<=d_star=(1-1/sqrt2)/2. Consequently any actual core-only restriction tree whose leaf negative probabilities lie in this interval satisfies Pi_H(F)-p Pi_H(u)<=0; controller nonempty entropy cancels linearly and complete terminal entropies remain. Any first proper core query from a parent with negative probability<=d_star/2 meets this sign condition, since both child biases are<=d_star. For point controls interleaved with cores, if every active core query has both core child biases<=d_star, then Pi_H(F;T)<=p Pi_H(u;U)+C0 Q_control, with the previously certified C0=2+2/ln2+1/(sqrt(e)ln2)<6 and actual original-input projected core tree U. Supplied proper projected core payment K and actual terminal allowance L give H(F)<=max(K,C0,L)I(F), removing the prior additive kappa core surcharge in this band. This does not supply K or L. The band is sharp uniformly in p<=1/2: at p=1/2 the remainder is strictly concave for d_star<d<1/2. Any extension has an actual dyadic nested shared-core nonconstant sibling witness; a six-bit fixed witness with child negative probabilities3/16 and1/4 has certified positive signed correction and refutes the wider quarter-band helper only. No universal selection or full FEI conclusion is asserted.')
statement=old['exact_statement']+extension
dependencies=['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@4 (prior components retained)', 'A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@2 exact arbitrary-controller entropy remainder and bias martingale', 'A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@3 actual original-input projected-tree and single endpoint ledger', 'A028-UNBALANCED-ACTIVATION-STOPPING-PAYMENT@2 one-bit scalar clause; previously independently reconstructed in A027 stage3']
new=dict(old); new.update(version=5,exact_statement=statement,statement_sha256=hashlib.sha256(statement.encode('utf-8')).hexdigest(),proof_source=str(run/'DERIVATION.md'),proof_dependencies=dependencies,review_records=[],status='PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW',supersedes=[{'claim_id':old['claim_id'],'version':4,'reason':'same candidate gains signed low-bias admission; no prior theorem withdrawn'}],hypotheses=['Uniform Boolean signs, normalized Fourier spectrum, entropy in bits; core and controller physically disjoint', 'New arbitrary-controller sign theorem requires p<=1/2 and all actual core terminal biases<=d_star', 'Interleaved theorem has point controls and safe-band child biases at every active core query; exhausted controls have zero correction', 'Full entropy conclusion requires a genuinely certified proper projected core price K and complete actual terminal allowance L; both retained as hypotheses'],refutes=old['refutes']+['QUARTER-BIAS-NONPOSITIVE-ACTIVATION-SURCHARGE@1: child probabilities<=1/4 imply signed activation correction<=0; actual six-bit nested siblings3/16,1/4 refute it'],first_unproved_line='Universally select a proper projected core tree with independently paid core decrement K and complete terminal allowance L, paying any first bias-band exit from an unused certified signed child surplus without renewing the controller reserve.',next_consumers=['A023','A025','A028','A029','A030','A064','A078','A087','A094'])
claims=[c for c in claims if c['claim_id']!=old['claim_id']]+[new]; dump('CLAIMS.json',claims)
nextaction='At the first core query whose child bias exits the sharp safe band, price the ACTUAL positive signed remainder R(parent)-average R(children) from one unused certified child surplus. Carry that single endpoint balance through the next proper split, retaining both terminal entropies and the same controller owner. Start with the saved nonconstant/nonconstant six-bit witness; do not renew unsigned rp epsilon.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B06','packet_id':'A027','gap_id':'G-R-SELECT','attempt_id':'A027-G-R-SELECT-006','method':'Replace unsigned future-control overbill by exact signed scalar curvature; prove sharp low-bias convexity and genuine first-proper-core-query zero-surcharge admission; verify actual shared siblings and interleaved trees','mathematical_delta':'Sharp d_star=(1-1/sqrt2)/2 band makes every core-only endpoint correction nonpositive; parent bias<=d_star/2 guarantees every first proper core split qualifies. Safe-band interleaving removes additive kappa core surcharge, yielding conditional max(K,C0,L). Wider quarter-band helper refuted by actual nonconstant siblings.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT; VERSION5_REVIEW_PENDING','mathematical_status':'PROVED_SHARP_SIGNED_LOW_BIAS_ADMISSION; UNIVERSAL_CORE_PAYMENT_TERMINALS_AND_FEI_OPEN','claim_versions_used':dependencies,'claims_created_or_changed':['A027-PARTIAL-CORE-ACTIVATION-TRANSPORT@5','QUARTER-BIAS-NONPOSITIVE-ACTIVATION-SURCHARGE@1 refuted helper only'],'source_artifacts':['DERIVATION.md','FROZEN_SPEC.json','code/exact.py','code/check.py','code/trees.py','code/finalize.py','out/pilot.json','out/validation.json','out/trees.json','SOURCE_READS.json'],'next_consumers':new['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,'blockers':['No universal independently paid proper core tree K and complete actual terminal price L','Bias-band exit can have genuinely positive signed correction; its unused certified child funding is unproved','Independent acceptance of version5 and supervisor mirrors unobserved'],'packet_ids':['A027']}
dump('PROGRESS.json',progress); dump('PACKET_DELTA.json',progress)
sources=[]
for path,scope in [(protocol,'Entire current protocol read; revision2026-10-11-execution-v2'),(team/'BOARD.md','Opening snapshot2026-10-14 10:35UTC, relevant B06 and neighboring owner/reserve updates; later rg scoped update read'),(team/'claude'/'B06'/'STREAM_NOTES.md','Entire unchanged v2 at stage opening'),(previous/'DERIVATION.md','Prior signed first-core-split and exact unsigned renewal obstruction'),(previous/'CLAIMS.json','Retained prior components, same candidate extended'),(agent/'runs'/'20261013T221314Z-account05-A027-block-selection'/'DERIVATION.md','Exact arbitrary-controller activation R and core-only partition; opening scope recalled/read'),(agent/'runs'/'20261013T221314Z-account05-A027-block-selection'/'INDEPENDENT_REVIEW.md','Prior scoped A028 scalar reconstruction supplies existing control clause'),(agent/'runs'/'20261014T015108Z-account05-A027-block-selection'/'DERIVATION.md','Read projected original-input interleaving and complete conditional terminal theorem'),(team/'agents'/'A028'/'runs'/'20261014T051435Z-account05-A028-stopping-tree-payment'/'REPORT.md','Opening scoped section read; latest signed bank direction, not independent acceptance of this stage'),(team/'agents'/'A028'/'runs'/'20261014T051435Z-account05-A028-stopping-tree-payment'/'DERIVATION.md','Scoped rg passages of controller-first/signed release; no new dependency claimed')]:
    sources.append({'path':str(path),'sha256':sha(path),'scope':scope})
dump('SOURCE_READS.json',{'observed_at':now,'sources':sources,'literature_scope':'No new external citation or priority assertion; required campaign/paper reads retain prior recorded scope. Stage6 uses exact prior local identities and a new explicit calculus proof.'})
report=f'''# A027 stage6: sharp signed low-bias core admission

Full FEI remains OPEN. The signed activation correction is nonpositive on a sharp bias band, so safe core splits need no controller refund or additive core surcharge. A first proper core query is guaranteed safe when the parent bias is at most half the band width. The complete core and terminal payments remain explicit.

## exact target, quantifiers, hypotheses and units

For every Boolean core u and independent controller a, set p=Pr(a=-1)<=1/2, d=Pr(u=-1), F=1+((1-a)/2)(u-1). Entropy is in bits; influence counts actual physical input edges. The exact activation remainder R(p,d) is convex for 0<=d<=d_star=(1-1/sqrt(2))/2. Every actual core-only restriction tree with terminal core biases in this band obeys Pi_H(F)-p Pi_H(u)<=0. For parent d<=d_star/2, any first core coordinate has both child biases in the band; when m>=2 this is a proper block. Neither full core entropy nor arbitrary child entropy is thereby paid.

For point controls and an interleaved physical tree, impose this same child-bias condition at every active core query. Using the actual original-input projected tree U gives Pi_H(F;T)<=p Pi_H(u;U)+C0 Q_control. A supplied proper projected payment K and actual terminal allowance L yield H(F)<=max(K,C0,L)I(F), C0<6. This removes the previous additive kappa=4+12/ln(2) core surcharge in the safe band. The theorem does not produce K or L.

## sources actually read, revisions and theorem locators

Read current BOARD (opening10:35UTC snapshot), full B06 STREAM_NOTESv2, own STATUS, and full execution protocol2026-10-11-execution-v2. Read own arbitrary-controller R proof, projected interleaving proof, and prior signed-admission/unsigned-renewal result. Consulted scoped passages of A028 stage5 REPORT/DERIVATION for its signed-owner direction; its latest theorem is not independently accepted here or used as a new mathematical premise. SOURCE_READS records paths, hashes and exact scope.

The exact R identity is prior A027 version2; projected actual input weights and endpoint ledger are prior version3. A028 one-bit scalar bound at version2 was previously independently reconstructed in A027 stage3; it is retained at that existing scope. No new external source, paper claim or literature-priority assertion is made. Stream lead direction remains unchanged: prove a useful proper split, keep complete terminals and identify the universal unsupported line.

## complete derivation or exact first unsupported line

DERIVATION.md proves R_dd=(16p/ln(2))D, where D=ln(1-2d)-(1-p)ln(2d)-p ln(1-2pd)+p ln(p). Its p derivative is increasing in p and strictly negative at p=1/2 throughout d<=d_star; the proof uses d_star<1/6 and ln(2)>=2/3. Therefore D(p,d)>=D(1/2,d)=(1/2)ln((1-2d)^2/(4d(1-d)))>=0 on the band. All reciprocal-ln(2) differentiation constants cancel, including the constant -4V folded into ln(2d). Continuity closes d=0 and p=0. This is an analytic all-dimensional proof, not extrapolation from finite cases.

Bias martingale plus Jensen makes the exact endpoint correction nonpositive. The controller Hplus term cancels linearly but remains in the complete actual leaf entropies. The refund is ONE signed endpoint quantity, never a renewed positive future-control reserve. The first-query guarantee follows from child d_i<=2d. In the interleaved point setting every live core node has p_v<=1/2; exhausted controls give zero correction. Control nodes pay their own physical influence once. Summation and the exact terminal influence partition prove the conditional max(K,C0,L) allowance.

Sharpness is also proved: at p=1/2, R_dd<0 for d_star<d<1/2. Any extension of the initial band contains dyadic nested shared-core siblings giving a positive Jensen correction. The fixed actual six-bit witness has child negative probabilities3/16 and1/4; both children are nonconstant, the selector leaves four physical core coordinates, and the independent control is a dictator. Its exact signed correction is

    2 -(49/512)log2(7) -(675/256)log2(5)
      +(315/256)log2(3) +(169/256)log2(13)
      >2503282859835519/1152921504606846976 >0.

This refutes only the wider quarter-bias nonpositive-surcharge helper. It is not a failure of FEI, of the actual core ledger, or of the sharp safe band.

First unsupported universal line: for EVERY Boolean core select a proper projected tree with independently paid core decrement K and complete actual terminal allowance L, and pay any first band exit from one unused certified signed child surplus without renewing the controller bank. The safe first-query theorem supplies none of these core or terminal certificates. Rare activations still carry their encoded core difficulty.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC was saved before computations. The copied exact helper is pinned by sha256 {v['helper_sha256']}. The first family has all nine labeled3-bit child tables with zero or one negative input, all81 ordered sibling pairs, and16 actual controllers: counts1,3,11 on0,1,2 controller bits with p<=1/2, plus the3-bit point controller. No symmetry quotient; maximum dimension7. Two additional fixed cases reach dimension8: near-boundary nested sizes8,9 on64 shared core inputs, and the quarter-band witness sizes3,4 on16 inputs. Forty-five rational scalar curvature grid checks verify the differentiation formula and strict positive signs; p=1/3 and2/5 grid parameters are continuous scalar checks, not claimed Boolean truth-table cases.

From A027 run `python -X utf8 runs/{run.name}/code/check.py --pilot`, then the same command without --pilot. Pilot passed{pilot['assertions']} assertions over81 cases in{pilot['elapsed_seconds']:.3f}s. Full passed{v['assertions']:,} assertions over1,296 exhaustive cases plus two fixed certificates in{v['elapsed_seconds']:.3f}s. Integer Walsh transforms, Fraction edge counts and exact prime-log vectors verify actual entropy cancellation, queried influence, retained terminal influence and exact curvature algebra. Rational24-term atanh enclosures with explicit tail certify all signs. The near-boundary fixed witness is strictly negative, the beyond-band witness strictly positive.

Run `python -X utf8 runs/{run.name}/code/trees.py`. All33 five-bit core signs (constant+1 or one labeled negative input), r1,2,3 point controls, and four frozen query orders give396 actual proper physical trees, maximum dimension8. Failed controls terminate at actual constant leaves. Each policy queries only two of five core coordinates on the projected tree. The orders test core-only, control between the two cores, control before them, and complete controls before them. Passed{tree['assertions']:,} assertions in{tree['elapsed_seconds']:.3f}s, including local child-band eligibility, actual signed corrections, own control-node price6, complete physical influence partition, and total zero-core-surcharge transfer with actual terminal entropy retained.

Each job cap60s, estimated160MB; peak RAM unmeasured. No >300MB job expected or started, so memok gate was not triggered. No GPU, dimension escalation, background job or floating sign evidence. All pilots and jobs passed without assertion/runtime failures. These finite checks validate the analytic proof and named witnesses; they do not certify arbitrary K,L or constitute a full-cube exhaustion.

## proof dependencies and changed downstream conclusions

Version5 extends the SAME A027 partial-core candidate. All version4 and earlier components, hypotheses and refutations remain; the safe-band clause adds a signed sufficient split condition and removes surcharge only under its explicit band hypothesis. No new broad candidate is opened at the stream pending-review cap. Existing core/controller identities and control payment are consumed rather than claimed as new.

A023/A025/A028/A029/A030/A064/A078 can omit the core activation debit at eligible low-bias nodes and retain a single nonnegative endpoint refund. They must still certify the core decrement and complete child entropies. The beyond-band witness prevents extrapolating this sign to biases<=1/4 or arbitrary cores. Earlier unsigned-renewal refutation remains intact. No independent acceptance, shared-index adoption or supervisor mirror is asserted.

## one next mathematical action and independent reviewer

{nextaction} A087 should reconstruct the scalar curvature and actual prime-log sibling certificate independently; A094 should challenge sharpness, exhausted-control handling, and complete terminal bookkeeping. These are local source-bound handoffs, not tool-sent messages or review receipts.

## actual persistence receipts or precise save blocker

All four protocol files, exact derivation, frozen spec, code and three checked outputs are saved only in A027. STATUS is two lines; WORKLOG and LEARNED append this stage. out/PERSISTENCE_RECEIPT.json checks exact progress/claim schemas, statement sha256s, required report fields, identical PACKET_DELTA, file sizes and actual file hashes. Local persistence verified; supervisor copying, remote mirrors, independent acceptance and downstream use remain unobserved.

## Universal bridge

This stage moves C019 signed proper-core admission and C024 actual history transfer by proving a sharp zero-surcharge bias band: d<=d_star/2 guarantees any first proper core split qualifies, and band-preserving interleavings replace the prior max(K+kappa,C0,L) allowance by max(K,C0,L). The exact signed correction is now a conserved nonpositive endpoint contribution there, avoiding the previously refuted positive-bank renewal. Universal paid core decrement K, complete terminal L, and unused child funding at the first band exit remain open. NEXT prices that first positive signed exit on the saved two-nonconstant-child witness with one inherited surplus and complete terminals. It attacks the remaining universal selection/payment boundary directly rather than another isolated Boolean class or a relabeled FEI-equivalent existence condition.
'''
(run/'REPORT.md').write_text(report,encoding='utf-8')
(agent/'STATUS.md').write_text('STATE: Stage6 locally complete: sharp low-bias signed admission d_star=(1-1/sqrt2)/2; safe interleaving removes core surcharge; 9666+4356 exact assertions PASS; FEI OPEN, v5 review pending.\nNEXT: Pay first positive bias-band exit from one unused certified signed child surplus, retaining both terminals and same controller owner; A087/A094 review v5.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{now} — {run.name}: Read updated BOARD/B06/STATUS and scoped A028 stage5. Changed from unsigned first-split overbill to actual signed correction: proved sharp uniform convexity band d_star=(1-1/sqrt2)/2 for p<=1/2, and any first proper core coordinate safe for parent bias<=d_star/2. Safe interleaving removes core kappa while retaining K,L hypotheses. Frozen pilot81 PASS594; full1296+2 PASS9666 in{v["elapsed_seconds"]:.3f}s,396 proper physical trees PASS4356 in{tree["elapsed_seconds"]:.3f}s. Exact nonconstant sibling witness refutes wider quarter-band sign. Samecandidatev5 pendingreview; universal core payment and terminal eligibility remain open.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''
## Stage6: sharp signed safe band, not a renewable positive bank

For the exact arbitrary-controller activation remainder R(p,d), p<=1/2, R_dd=16p[ln(1-2d)-(1-p)ln(2d)-p ln(1-2pd)+p ln(p)]/ln2. The bracket decreases in p throughout d<=d_star=(1-1/sqrt2)/2, and its p1/2 value is half ln((1-2d)^2/(4d(1-d)))>=0. Thus R is convex on the sharp uniform band. The constant -4V in differentiation matters; do not omit its ln(2d) contribution.

Actual core-only leaves with negative probabilities<=d_star give Pi_H(F)-pPi_H(u)<=0 by one endpoint Jensen refund; controller Hplus remains in terminal entropy. Parent bias<=d_star/2 ensures every first proper core query has safe children. Point-control interleavings with safe child biases at each core query have no positive core surcharge; supplied proper projected priceK and complete terminal allowanceL close at max(K,C0,L), C0<6, not max(K+kappa,C0,L). No core or terminal certificate is manufactured by this sign.

Sharpness: at p1/2 and d_star<d<1/2 curvature is negative. Distinct dyadic nested negative sets on a common finite core are actual nonconstant Boolean sibling witnesses to any band extension. Fixed selector with siblings3/16,1/4 plus dictator control has positive exact six-bit signed correction >2503282859835519/1152921504606846976. The quarter-band helper fails; FEI does not. Full validation1296 labeled sibling/controller cases+2 fixed+45 scalar curvature checks PASS9666,396 proper interleaved trees PASS4356. NEXT pays first signed positive band exit from unused inherited child surplus with both complete terminal entropies and the same controller owner.
''')
schema=json.loads(protocol.read_text(encoding='utf-8'))['required_per_run']
assert set(progress)=={k.split(' (')[0] for k in schema['progress_fields']}
assert all(set(c)==set(schema['claim_fields']) for c in claims)
assert all(hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256'] for c in claims)
assert all(field in report for field in schema['report_fields'])
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
assert len((agent/'STATUS.md').read_text().splitlines())==2
files=[]
for path in sorted(run.rglob('*')):
    if path.is_file() and path.name!='PERSISTENCE_RECEIPT.json':
        assert path.stat().st_size<20*1024*1024
        files.append({'path':str(path.relative_to(run)),'bytes':path.stat().st_size,'sha256':sha(path)})
dump('out/PERSISTENCE_RECEIPT.json',{'status':'PASS','timestamp':now,'checks':['exact protocol schemas','all statement hashes','all report fields','compatibility byte identity','two-line STATUS','file size cap'],'files':files,'rolling_files':[{'path':str(agent/name),'sha256':sha(agent/name)} for name in ('STATUS.md','WORKLOG.md','LEARNED.md')],'independent_acceptance':'UNOBSERVED','remote_mirrors':'UNOBSERVED'})
print(json.dumps({'status':'PASS','run':run.name,'version':5,'files':len(files),'claims':len(claims),'assertions':v['assertions']+tree['assertions'],'full_fei':'OPEN'}))
