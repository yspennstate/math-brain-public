from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
RUN=Path(__file__).resolve().parents[1]; OWN=RUN.parents[1]
def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def save(p,x):Path(p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
protocolpath=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=load(protocolpath); out=load(RUN/'out/CHECK.json')
assert out['status']=='PASS' and not out['pilot'] and out['source_cases']==15 and out['active_query_reset_cases']==15 and out['repaired_endpoint_cases']==15
assert all(F(a['complete_original_quota_margin']['lower'])>F(303343,10**6) for a in out['rows'])
assert all(F(a['same_original_margin']['lower'])>F(107981,10**6) for a in out['repaired_endpoint'])
assert out['seconds']<55
now=datetime.now(timezone.utc).isoformat()
source=OWN.parent/'A001/runs/20261023T000044Z-account03-A001-quantifier-audit'
review=OWN.parent/'A090/runs/20261022T235050Z-account03-A090-independent-reconstruction'
prior=OWN/'runs/20261022T220858Z-account03-A004-constant-and-unit-ledger'
assert sha(RUN/'code/exact.py')==sha(prior/'code/check_reference.py')
inputs=[protocolpath,OWN/'STATUS.md',OWN/'LEARNED.md',OWN.parent.parent/'BOARD.md',OWN.parent.parent/'claude/B01/STREAM_NOTES.md']
inputs += [source/n for n in ('REPORT.md','DERIVATION.md','CLAIMS.json','code/check_reset.py','out/CHECK.json')]
inputs += [review/n for n in ('REPORT.md','CLAIMS.json')]+[prior/'CLAIMS.json',prior/'code/check_reference.py']
save(RUN/'out/SOURCE_MANIFEST.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':'stage source review; A090 report opening and source-review record only, not its two additional claims'} for p in inputs])
(RUN/'out/INPUT_STATUS.md').write_bytes((OWN/'STATUS.md').read_bytes())
old=next(c for c in load(prior/'CLAIMS.json') if c['claim_id']=='A004-SHARP-REFERENCE-RESET-AND-SAME-BANK-FRONTIER')
external=next(c for c in load(review/'CLAIMS.json') if c['claim_id']=='A090-A004-SHARP-RESET-INDEPENDENT-RECONSTRUCTION')
assert external['proof_dependencies'][0]['declared_statement_sha256']==old['statement_sha256']
old['review_records']+=external['review_records'];old['status']='INDEPENDENTLY_ACCEPTED_BY_A090; RECEIPT_CONSUMED_BY_A004'
old['proof_source']=[str(prior/x) for x in old['proof_source']]
audited=next(c for c in load(source/'CLAIMS.json') if c['claim_id']=='A001-INDEPENDENT-CANONICAL-RESET-SAME-BANK')
audited['proof_source']=[str(source/x) for x in audited['proof_source']]
audited['review_records'].append({'reviewer':'A004/account03','at':now,'verdict':'HOLDS unchanged for new source-floor normalization, real-parameter rectangle, on-only bound and failing endpoint','independent_method':'Independent A004 exact arithmetic helper; new physical spectra and direct/signed liability reconstruction; no A001 helper imported. A004 does not independently review its own prior dependency; A090 source acceptance is separately consumed.','proof':str(RUN/'DERIVATION.md')})
audited['status']='NEW_CANONICAL_CALCULATIONS_INDEPENDENTLY_ACCEPTED_BY_A004'
statement=('For the specified neutral six-data-bit AND3 point edit encoded by fresh Maj3, original quota3, first query y3 and book the old 1/8-mixture and admitted source-canonical resets with initial lambda in[0,1], alpha in[0,3/4]. Then query any active data coordinate in the on-child, keep the actual conditional-KL refund and all old debits, reset its edited daughter by source formula(1) with k2,r4 and beta in[0,1], and explicitly reset the constant daughter to its constant source law. With the retained old sibling unchanged at alpha3/4, the complete liability is <3-303343/1000000 bits. Changing that retained sibling to its source reference alpha_new in[3/4,1] is also paid from the SAME original account, leaving >107981/1000000 bits, with worst parameters beta=alpha_new=1. Both new local outcomes and the retained original nonconstant sibling are included as complete terminal cross-entropies. The same margin funds every subsequent adaptive stopping tree with marginal-reference continuation and no fresh reset. The earlier first-frontier source endpoint(1,1) remains a valid failure; the newly paid frontier includes an actual active query and different daughter references. No arbitrary-root FEI or universal canonical-reset theorem follows.')
hyp=['One actual specified uniform nine-bit Boolean sign source; full spectral laws include empty atoms','Exact source prescriptions in DERIVATION(1); positive on actual supports; no arbitrary replacement reference','Original quota3 and initial root/mixture/source debits retained; signed reset bookkeeping and actual KL refund','Initial real lambda in[0,1], alpha in[0,3/4]; real beta in[0,1], alpha_new in[3/4,1]','Global expected account with reaches1/4,1/4,1/2; no separately allocated child solvency or fresh bank','Later finite adaptive physical queries use current reference marginals, both outcomes retained, no fresh reset; logs bits']
new={'claim_id':'A004-ACTIVE-QUERY-CANONICAL-FRONTIER-REPAIR','version':1,'exact_statement':statement,'hypotheses':hyp,'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A004/account03; A001 supplies initial source prescriptions'],'proof_source':['DERIVATION.md','code/check.py','code/exact.py','out/FROZEN_SPEC.json','out/CHECK.json'],'proof_dependencies':['A001-INDEPENDENT-CANONICAL-RESET-SAME-BANK@1 new bounds reconstructed here','A004-SHARP-REFERENCE-RESET-AND-SAME-BANK-FRONTIER@1, independently accepted by A090','Finite cross-entropy convexity and actual physical marginal identity, reconstructed here'],'review_records':[],'status':'WRITTEN_PROOF_AND_EXACT_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':'Influence-priced arbitrary-source reference admission; fresh prescribed reset after a genuinely mixed data/controller or dummy query in the already reset daughter from SAME remaining original owner.','next_consumers':['A001','A003','A090','A094','A096','A097','B01','B20']}
claims=[old,audited,new]
for c in claims:assert set(c)==set(protocol['required_per_run']['claim_fields'])
save(RUN/'CLAIMS.json',claims)
delta='A001 source-canonical rectangle and failing endpoint independently HOLD; A090 acceptance of prior A004 lemma consumed. One active query plus nonempty-profile reset and maximally spread retained-sibling reference paid from SAME quota3, margin>107981/1e6 bits; no universal FEI improvement.'
nextaction='A001/A090/A094 review new active-query refund and three-terminal SAME-bank proof; then price one mixed dummy/controller exposure plus fresh source prescription in the already reset daughter, old maximal-spread sibling and all debits retained, using ONLY remaining >107981/1e6 owner.'
progress={'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B01','packet_id':'A004','gap_id':'G-R-SELECT / C024 prescribed-reference transfer','attempt_id':'A004-stage18-active-canonical-frontier','method':'Independent source review; signed conditional-KL refund and explicit nonempty-profile source reset; convex endpoint proof','mathematical_delta':delta,'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SCOPED_WRITTEN_PROOF_AND_EXACT_CERTIFICATE; FULL_FEI_OPEN; NEW_REVIEW_PENDING','claim_versions_used':['A001-INDEPENDENT-CANONICAL-RESET-SAME-BANK@1','A004-SHARP-REFERENCE-RESET-AND-SAME-BANK-FRONTIER@1','A090-A004-SHARP-RESET-INDEPENDENT-RECONSTRUCTION@1'],'claims_created_or_changed':[c['claim_id']+'@1 '+('new' if c is new else 'review receipt') for c in claims],'source_artifacts':['DERIVATION.md','out/SOURCE_MANIFEST.json','out/CHECK.json','out/FROZEN_SPEC.json','code/check.py'],'next_consumers':new['next_consumers'],'next_action':nextaction,'stagnant_substantive_attempts':0,'blockers':['Universal arbitrary-root admission and mixed-profile reset costs remain open','New independent review, supervisor adoption and remote mirror unverified','Formal compiler launch refused by memory admission'],'packet_ids':['A004']}
assert set(progress)==set(k.split(' (')[0] for k in protocol['required_per_run']['progress_fields'])
save(RUN/'PROGRESS.json',progress);save(RUN/'PACKET_DELTA.json',progress)
report=f'''# exact target, quantifiers, hypotheses and units

Full FEI remains OPEN: one dimension-independent C must bound H<=CI for every Boolean sign on every finite uniform cube. This stage moves the SAME original quota3 through one active physical data query and a genuine canonical nonempty-profile reset on the saved neutral AND3/Maj3 source. It then pays the retained sibling's maximally spread source reference, which failed at the earlier frontier. All claims include both new outcomes and the old sibling, all complete terminal references and empty atoms; units are bits and ordinary physical flip influence.

# sources actually read, revisions and theorem locators

Read the 23 October03:14 UTC BOARD B01 and relevant review/transfer entries, unchanged B01 STREAM_NOTES v1, own STATUS/LEARNED and prior exact helper. Read A001 run20261023T000044Z DERIVATION in full, CLAIMS and checker; reconstruct its new source equations(1)--(5) and parameter endpoints. Read A090 run20261022T235050Z report opening and its A004-source review record, validating the matching statement digest before consuming that acceptance. Its two additional claims are not newly accepted. Protocol2026-10-11-execution-v2 governs schemas and baseline retirement; the user's later campaign end controls. Previously inspected campaign/paper baselines are not reaudited. SOURCE_MANIFEST pins actual source bytes; INPUT_STATUS preserves the rolling input.

# complete derivation or exact first unsupported line

DERIVATION supplies the complete signed ledger, real-parameter proof and all-history induction. A001's new canonical rectangle, on-only bound and failed first-frontier endpoint independently HOLD at original scope. The source reference on the edited daughter changes from k3,r5 to k2,r4 after a real active query. Its canonical normalizer equals the actual data marginal at parameter0; full normalization and actual-support positivity are explicit.

Writing M_in=3-C_in, actual local conditional-KL refund c, new edited/constant reset costs E_a,E_d and retained-sibling extra cost E_far, the SAME remaining account is exactly M_in+c/2-E_a/4-E_d/4-E_far/2. Original H(F)-T0, old mixture resets and both old canonical debits remain in this equation. No new child 4I-H is credited. The constant daughter's incoming CE is released only by its explicitly booked reset to the exact constant source law.

Intermediate margin>303343/10^6; after maximal spreading on the retained original nonconstant sibling, margin>107981/10^6. The first-frontier source(1,1) still fails by>153188/10^6: the newly paid frontier has a real active query and different daughter references, so these numbers measure different liabilities. Convexity and KL-minimality at parameter0 certify EVERY real beta in[0,1], alpha_new in[3/4,1], all admitted initial source parameters, all three active choices, and every later adaptive no-reset marginal-reference continuation. This does not pay an arbitrary future reset or an arbitrary root.

First unsupported universal line: source/reference admission priced by O(I) for arbitrary Boolean roots, and a hereditary bound for a prescribed fresh reset after genuinely mixed data/controller/dummy exposure. The fixed Maj3/point source kernel remains essential.

# executed validation with domain, arithmetic, commands and outputs

Frozen spec precedes the search. Command: python -X utf8 -B code/check.py --pilot, then python -X utf8 -B code/check.py. Final output: {out['assertions']} exact assertions PASS in {out['seconds']:.6f} seconds,15 source parameter cases,15 active-query/reset cases,15 repaired retained-sibling endpoints. All22 labeled Boolean tables through n2 and36 local reference identities cover constant, dictator, parity and nearly constant endpoints. The initial pilot is saved separately; the widened pilot passed before full execution. Only the final full count is credited. Two final checks added source on-only margins and96 actual-zero atom removals so the independent source review covers its entire new statement; no hypothesis was weakened.

The exact arithmetic helper is byte-identical to A004's previously independently implemented helper, not imported from A001. Physical truth-table restriction, Fraction spectra, exact prime-log maps and rational atanh intervals with proved tails and outward dyadic rounding verify direct and signed accounts separately. Final readback explicitly checks lower bounds>303343/10^6 and>107981/10^6. Floating-point displays determine no sign. The continuum is an analytic convexity conclusion, not an extrapolation from five grid points.

Memory estimate90MB, explicit runtime cap55 seconds; no automatic dimension escalation, GPU, detached job or large search. Lean admission returned1: physical free1.6GB versus required4.0GB; commit free12.6GB versus required8.0GB. No compiler was launched. The proposed scalar phase identity and precise admission record are in FORMAL_STATUS; the rung is written proof plus exact certificates, NOT Lean-checked. No other's running work is stopped.

# proof dependencies and changed downstream conclusions

Consume A090's unchanged independent acceptance of A004-SHARP-REFERENCE-RESET-AND-SAME-BANK-FRONTIER@1 with matching digest. A004's review of A001 addresses its NEW canonical normalization, source costs, continuum and endpoint; A004 does not independently review its own prior dependency. No repair to A001 is needed. The new active-query result is author-complete and awaits independent reconstruction by A001/A090/A094. No universal FEI constant improves. A failed reference payment remains distinct from a Boolean FEI counterexample.

# one next mathematical action and independent reviewer

{nextaction} This is a saved handoff, not a sent message. General no-reset histories below the newly paid frontier are closed analytically, so another depth census would repeat paid work. A094 should specifically challenge support zeros, the constant terminal refund, cross-sibling ownership and the initial-vs-final parameter quantifiers.

# actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and byte-identical PACKET_DELTA, DERIVATION, frozen specification, executable code, pilot/full outputs, formal-admission record and source hashes are saved only inside A004. Rolling STATUS has exactly two lines; WORKLOG and LEARNED record the new facts. PERSISTENCE_RECEIPT checks schemas, claimed rational thresholds, statement hashes and file sizes. New review, supervisor adoption and remote mirrors remain unverified; no git, email or brain research write is performed. Administrative checklist calls are the explicitly required exception. Brain self-care remains degraded because owner-model/state notes are stale; they supply no mathematical premise.

**Universal bridge:** This stage moves C019/C024 by independently validating A001's prescribed source-reset input, then paying a real active query, a changed nonempty canonical daughter profile and the retained sibling's maximal source spread from the SAME diminished original quota3, with >107981/10^6 bits left and all three complete terminals retained. It replaces an unpaid fresh-reset continuation by an explicit checked one; the universal constant improvement is zero. Arbitrary-source admission and mixed-profile reset pricing remain open. NEXT uses the already reset daughter, old maximally spread sibling and ONLY the remaining original owner, because that tests the exact missing hereditary transfer rather than enlarging an isolated finite census.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(OWN/'STATUS.md').write_text('STATE: A004 stage18 saved: A001 canonical source bounds independently HOLD; active query plus fresh nonempty-profile and maximal sibling resets paid SAME quota3, >107981/1e6 left; '+str(out['assertions'])+' exact checks PASS; review pending; FEI OPEN.\nNEXT: A001/A090/A094 review; price one mixed dummy/controller query-reset in ALREADY reset daughter using SAME remaining >107981/1e6 owner, maximally spread old sibling/all debits/full terminals retained.\n',encoding='utf-8')
with (OWN/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+now+' stage18: '+delta+' '+str(out['assertions'])+' exact checks PASS; memory gate refused formal launch, no work stopped. NEXT '+nextaction+'\n')
with (OWN/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage18: A090 independent acceptance of A004 sharp reset consumed. A001 source canonical rectangle independently reconstructs. On neutral AND3/Maj3, active on-child query k3,r5->k2,r4 releases actual conditional KL and explicit constant-child CE reset refund. Exact SAME-owner margin Mnew=Min+c/2-Ea/4-Ed/4-Efar/2. Maximal source spreading failed first frontier(-.153188 bits) but is paid AFTER real query/different daughter references(+.107981 bits); do not confuse the liabilities or renew S4. Canonical edited law Rprime=(1-e/s)[(1-z)Pg+zV]+(e/s)mu delta_empty+2e/2^r, joint kernel actual source p(S,T)/q(T); q>0 and Rprime0=q at both used parameter pairs. Convex KL-minimality proves real beta/alpha intervals. Further mixed-profile resets and arbitrary-core admission remain open.\n')
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len((OWN/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert hashlib.sha256(statement.encode('utf-8')).hexdigest()==new['statement_sha256']
files=[]
for p in RUN.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
        assert p.stat().st_size<20*1024*1024
        files.append({'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(RUN/'out/PERSISTENCE_RECEIPT.json',{'status':'PASS','at':now,'claims_schema':'exact','progress_schema':'exact','checked_full_assertions':out['assertions'],'files':files,'remote_mirror':'UNVERIFIED'})
print(json.dumps({'status':'SAVED_READBACK_VALIDATED','assertions':out['assertions'],'claims':len(claims),'files':len(files),'margin_lower':'107981/1000000'}))
