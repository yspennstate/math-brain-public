import copy,hashlib,json
from datetime import datetime,timezone
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R.parents[1];B=A.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def put(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
now=datetime.now(timezone.utc).isoformat();main=load(R/'out/CHECKS.json');review=load(R/'out/REVIEW_CHECKS.json')
assert main['status']==review['status']=='PASS'
assert main['cases']==1152 and review['cases']==448 and review['nonzero_singleton_carry_cases']>0
protocolpath=Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json');protocol=load(protocolpath)
src=B/'agents/A041/runs/20261023T135351Z-fleet03-A041-weighted-threshold-fei'
original=next(x for x in load(src/'CLAIMS.json') if x['claim_id']=='A041-SHARP-JOINT-SINGLETON-SOURCE')
assert original['statement_sha256']=='858bf303c4d23127fd913d7bc8c6e670e56b44a2ac6db09f682328ce51ed371f'
payloads=[original['exact_statement'],json.dumps({'statement':original['exact_statement'],'hypotheses':original['hypotheses']},sort_keys=True,separators=(',',':'))]
assert any(hashlib.sha256(x.encode('utf-8')).hexdigest()==original['statement_sha256'] for x in payloads)
assert sha(src/'PROOF.md')==original['proof_source']['sha256']=='e3c5b5114000a4af5804940a62dedda985471c6aed1577f65b62b0ace2b13b8c'
prior=A/'runs/20261023T120324Z-fleet03-A042-bias-endpoint-certificates/code/check.py'
assert sha(R/'code/core.py')==sha(prior)
sources=[protocolpath,B/'BOARD.md',B/'claude/B09/STREAM_NOTES.md',src/'PROOF.md',src/'CLAIMS.json',
 B/'agents/A043/runs/20261023T123418Z-fleet03-A043-prime-gate-decomposition/PROOF.md',
 B/'agents/A045/runs/20261023T132409Z-fleet03-A045-biased-realizability-referee/PROOF.md']
sources+=list(sorted((B/'agents/A044/runs').glob('*/PROOF.md'))[-1:])
put(R/'out/SOURCE_RECEIPTS.json',{'sources':[{'path':str(p),'sha256':sha(p)} for p in sources],'source_statement_proof_hashes_verified':True,'own_helper_copied_unchanged':{'source':str(prior),'sha256':sha(prior)}})
record={'reviewer':'A042/fleet03','verdict':'HOLDS_AT_STATED_SCOPE','source_statement_sha256':original['statement_sha256'],'source_proof_sha256':sha(src/'PROOF.md'),
 'scope':'Optimal all-alpha singleton scale/mantissa source and exact all-depth alternative original owner, retaining genuine singleton carry, imported/full singleton mantissas, refunds and full ordinary-KL reference conventions; universal prime premise remains open',
 'method':'Independent scalar cell proof and two extremizing actual AND controls; physical composition partition, exact prime-log low/high carry and full KL factorization; finite telescope for all depth',
 'source_repair':False,'contributor_conflict':False,'proof':'REVIEW_A041.md','checks':['out/CHECKS.json','out/REVIEW_CHECKS.json'],'at':now}
put(R/'out/A041_REVIEW.json',record)
reviewclaim=copy.deepcopy(original);reviewclaim['review_records'].append(record);reviewclaim['status']='INDEPENDENT_RECONSTRUCTION_HOLDS_AT_STATED_SCOPE_BY_A042'
statement=('For every finite Boolean seed g at an interior independent product law after deterministic contraction, let P_T=v_T*c_T^2 and W_T=v_T*4^-j_T, where1/2<2^j_T|c_T|<=1 on occupied nonempty labels. Put A=sum_single P, M=sum_high P, V=A+M, Z1=sum_single W and Zh=sum_high W. Define complete references Q_all with actual empty mass and nonempty mass VW/Z, and Q_* with actual empty/singleton masses and high mass MW/Zh; let Ka=KL(P||Q_all), Kh=KL(P||Q_*), and K1=A KL(P_single/A||W_single/Z1), omitting empty-sector conditionals. Independently activate F=1-X+Xg with e=Pr(X=1)=2^-k,k>=1, and use its complete paid-sector reference. Then H_F=e[M+(1-e)A], Zhi_F=e[Zh+(1-e)Z1], and full ordinary K_F=e Kh+e(1-e)K1+H_F*d_Bern((1-e)A/[M+(1-e)A]||(1-e)Z1/[Zh+(1-e)Z1]). The true complete composed reference has Ktree=e Kh, so the specialized flat/tree conversion is nonnegative and equals n_F-e n_h-e(1-e)L1. For G(lambda)=sum_high P ln(P/W)+lambda sum_single P ln(P/W)+(M+lambda A)ln[(Zh+lambda Z1)/(M+lambda A)], one has G(0)=Kh,G(1)=Ka,K_F/e=G(1-e); G is monotone and concave, with Gprime=K1+A[ln r+1/r-1]>=0 and Gsecond=-(A Zh-M Z1)^2/[(M+lambda A)(Zh+lambda Z1)^2]<=0, r=A(Zh+lambda Z1)/[Z1(M+lambda A)], under positive sector masses and by continuous conventions otherwise. Hence e(1-e)Ka+e^2 Kh<=K_F<=e Ka and 0<=Ka-K_F/e<=e(Ka-Kh)<=e V ln4 uniformly over all dimensions, seeds and physical product laws. Thus the singleton-preserving rare-activation root reference reinstates the complete ALL-rounded seed KL to first order, with absolute error<=e^2 V ln4, rather than discarding its singleton-rounding bill. Actual corrected entropy, original deficit, full terminal laws and the matching cross entropy retain that seed law; no fresh capacity or second KL is created. Constants/literals and zero sectors use actual zero/unit-atom laws; selector reflection covers corresponding probability-one coordinates. This exact reference endpoint does not prove an arbitrary-prime high-scale bound or full FEI.')
gap='Pay the arbitrary prime/inherited J_hi from genuinely unused ORIGINAL capacity after actual singleton/import/carry debits, retaining all refunds, the complete inherited seed reference, ordinary KL and both full terminal laws.'
claim={'claim_id':'A042-CONCAVE-PAID-REFERENCE-ENDPOINT','version':1,'exact_statement':statement,
 'hypotheses':['Actual finite Boolean sign on independent physical product law; deterministic coordinates contract first','Independent dyadic selector on a physically disjoint wire; natural logarithms','Complete all-rounded and singleton-preserving references keep actual low atoms as specified, all occupied high labels, and ordinary KL','Zero-sector conditionals omitted before division; constants/literals and reflected probability-one endpoints handled physically','Uniform error uses actual V; no renewed source capacity, independent Boolean reset or universal high-scale premise'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A042/fleet03'],
 'proof_source':{'path':'PROOF.md','sha256':sha(R/'PROOF.md')},
 'proof_dependencies':['Direct physical dyadic activation spectrum and complete finite-law KL partition, re-derived','Elementary two-sector transport differentiation and ln r>=1-1/r; exact monotone concavity proof','Prior A042 paid-sector activation definitions; no dependence on the new A041 source or an unproved prime supplier'],
 'review_records':[],'status':'AUTHOR_ANALYTIC_PROOF_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
 'first_unproved_line':gap,'next_consumers':['A041','A043','A044','A045','A091','B09 lead','B20']}
for x in [claim,reviewclaim]:assert set(x)==set(protocol['required_per_run']['claim_fields'])
put(R/'CLAIMS.json',[reviewclaim,claim])
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B09','packet_id':'A042','gap_id':'B09-ORIGINAL-DYADIC-SCALE-PAYMENT','attempt_id':'A042-stage11-concave-reference-endpoint',
 'method':'Exact physical sector KL chain and monotone concave transport; uniform rare-activation error; independent review of sharp all-alpha singleton source with real low-carry compositions',
 'mathematical_delta':'K_paid(activate_e(g))/e approaches K_all(g), not only K_paid(g), uniformly with error<=e(Ka-Kh)<=e V ln4; exact complete-law chain and nonnegative specialized conversion. A041 sharp joint source/owner independently HOLDS; no prime supplier.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_SUPERVISOR_COPY','mathematical_status':'QUANTIFIED_REFERENCE_ENDPOINT_PROVED_EXACT_CHECKS; NEW_INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[original['claim_id']+'@1:'+original['statement_sha256']+' (independent review only; not a premise of endpoint theorem)'],
 'claims_created_or_changed':[claim['claim_id']+'@1',original['claim_id']+'@1: independent HOLDS review'],
 'source_artifacts':['PROOF.md','REVIEW_A041.md','SPEC.json','REVIEW_SPEC.json','out/CHECKS.json','out/REVIEW_CHECKS.json','out/A041_REVIEW.json','out/SOURCE_RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],'next_action':'A043/A044/A045 independently review the complete-KL transport and uniform endpoint; price arbitrary prime J_hi in the SAME unused original account, retaining restored all-rounded seed reference, low-carry commitments and BOTH terminals.',
 'stagnant_substantive_attempts':0,'blockers':['Universal arbitrary-prime J_hi payment remains open','New theorem independent review, supervisor copying/mirror/downstream use unobserved','Session brain self-care degraded: owner-model100.8h, state-of-mind85.4h, dream36.1h stale','Checklist working attempt failed with shared lock timeout; final bookkeeping receipt recorded separately','Compute heartbeat remains stale; not used as current resource admission; no shared service restart'],
 'packet_ids':['A042']}
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
put(R/'PROGRESS.json',progress);(R/'PACKET_DELTA.json').write_bytes((R/'PROGRESS.json').read_bytes())
report=f'''# A042 stage11: complete seed reference at rare bias endpoints

## exact target, quantifiers, hypotheses and units

For EVERY finite Boolean seed and every actual interior product law, determine the complete ordinary-KL endpoint after an independent dyadic activation when final singleton masses are frozen. Prove a quantitative uniform rate, including constants, zero high mass and unit atoms; reflect the selector for probability-one coordinates. Natural logarithms throughout. The original target remains one dimension-independent full FEI theorem; full FEI is OPEN.

## sources actually read, revisions and theorem locators

Current BOARD B09, stream lead v2 and own stage10 STATUS; execution-v2 schema and established prior protocol/literature context. Read latest A04120261023T135351Z PROOF Sections1-4 and CLAIMS, A04520261023T132409Z full PROOF, A04320261023T123418Z and latest A044 proof on split singleton/high owners (bounded intake may truncate their nonessential trailing context; these are not new full-scope reviews). A041's exact source statement and raw proof hashes were independently reproduced in out/SOURCE_RECEIPTS.json. The old binary base-case assignment is closed. Current board asks for actual prime J_hi payment with original owner and complete terminals. No fresh literature audit, novelty claim or source checker counts adopted.

## complete derivation or exact first unsupported line

PROOF.md partitions the actual root high sector into imported seed singletons and seed high labels. It proves the exact full ordinary KL chain K_F=eKh+e(1-e)K1+H_F*d_Bern(r||s), retaining actual empty/singleton masses and all occupied high labels. The complete composed reference has Ktree=eKh, so this specialized reference conversion is nonnegative, although general conversions remain signed. The identity agrees exactly with the previous n_F-e n_h-e(1-e)L1 formula; its normalizer and ordinary KL must change together.

The transport function G(lambda) has G(0)=Kh, G(1)=Ka and K_F/e=G(1-e). Explicit derivatives prove monotonicity and concavity, including zero-sector limits. Consequently e(1-e)Ka+e^2Kh<=K_F<=eKa and 0<=Ka-K_F/e<=e(Ka-Kh)<=e V ln4. This is uniform in seed, dimension and product law, even when the seed varies with e. It shows that rare activation of the NEW paid-sector root reference reinstates the OLD complete all-rounded seed KL at leading order. Matching corrected cross entropy and entropy have the SAME seed law; this is no new source reserve. Constant/literal and unit-atom cases are explicit physical laws.

REVIEW_A041.md independently reconstructs its optimal all-alpha source J1+alpha L1<=max(ln4,2alpha)(2Delta-R), the actual Boolean sharpness controls and the exact all-depth joint owner with genuine C1 retained. At the critical alpha=ln2, the finite sign test simplifies to L1<=2[(2Delta-R)-J1/ln4], avoiding unverified products of logarithms. The arbitrary-depth identity follows from two separately checked low-scale/mantissa partitions and weighted finite telescoping, retaining both full terminal laws. No source repair is supplied. First unsupported universal line: {gap}

## executed validation with domain, arithmetic, commands and outputs

Frozen SPEC.json and REVIEW_SPEC.json precede the jobs. Commands: python -B -X utf8 code/check_endpoint.py --pilot; code/review_joint.py --pilot; code/check_endpoint.py; code/review_joint.py. The reused physical helper is copied byte-for-byte from our OWN prior-stage code; its hash is pinned and source unchanged. No other agent's code was copied or run.

Main PASS:1152 actual dyadic activation roots/{main['exact_assertions']} exact assertions in {main['runtime_seconds']:.3f}s. All16 two-bit seeds at two laws and all256 three-bit seeds at fair law, e=1/2,1/4,1/16,1/1024. Checks include complete physical spectrum, sector KL chain, low-atom retention, concavity chord, monotone upper bound, explicit V ln4 error bank and sharp critical singleton source. Arithmetic is Fraction, canonical prime-log equalities and outward24-term atanh enclosures with proved geometric tail; no floating sign test. Exact zero expressions cancel before enclosure. The continuum/all-arity assertions follow from the written derivative proof, not finite extrapolation.

Independent review PASS:448 genuine compositions/{review['exact_assertions']} exact assertions in {review['runtime_seconds']:.3f}s; all16 binary outer gates,14 nonconstant two-bit children plus one literal, at two physical laws. {review['nonzero_singleton_carry_cases']} fixtures have nonzero singleton carry. Exact low/high scale and mantissa partitions, original deficit, critical source, complete composed references and FULL ordinary-KL chain are retained. Pilots are saved separately. All jobs estimated90MB and below55s; no over300MB job/admission, GPU, detached work, compiler or automatic dimension increase. No formal proof is claimed.

## proof dependencies and changed downstream conclusions

The new reference endpoint is self-contained physical expansion plus finite-law KL and elementary differentiation, pending independent review. A041-SHARP-JOINT-SINGLETON-SOURCE@1 is independently HOLDS at its exact scalar/all-alpha all-depth conditional scope with original author/hypotheses preserved; it is not a premise of the new endpoint theorem. Generic source prerequisites are reconstructed through the unique physical partition, not assumed for repeated wires. Earlier full-carry and high-sector import obstructions remain valid. Downstream cannot replace inherited all-rounded seed KL by only its paid-sector KL at a rare endpoint without the explicit conversion in equation(1); that change would omit a first-order sector bill. No universal prime scale bound or FEI counterfamily is supplied.

## one next mathematical action and independent reviewer

A043/A044/A045 independently reconstruct the concave complete-reference transport, then pay arbitrary prime J_hi from the SAME unused original degree/refund capacity after actual singleton/import/carry debit. Keep restored complete seed reference, the sharp source's committed mantissa, ordinary KL and BOTH terminals. A041/A091 should challenge attempted reuse of that commitment. The exact endpoint is an adversarial universal-supplier interface, not another isolated class census.

## actual persistence receipts or precise save blocker

Four protocol files, proof/review, frozen specs, exact scripts/outputs and source hashes are saved inside the designated A042 run. Finalizer verifies exact schema key sets, source statement/proof hashes, required report fields, identical compatibility-copy bytes, two-line STATUS and20MB limits, then saves local sha256 receipts. WORKLOG and LEARNED append once. Supervisor copying, remote mirror and downstream adoption remain unobserved; no Git or messages were sent. Brain self-care is degraded/unverified: owner-model100.8h, state-of-mind85.4h, dream36.1h stale, affecting personal-context guidance; current research instructions govern. Compute heartbeat13:57:59 stayed unchanged across more than30s, so its resource numbers were not treated as live; no shared service or workload was stopped. Initial checklist working attempt returned shared-lock timeout; final closure outcome is recorded separately. No research job remains running.

## Universal bridge

This stage advances C024 history transfer and C020 whole-set witness cost by proving the exact complete-KL rare-endpoint supplier interface with dimension-free error<=e^2 V ln4, and independently accepting the sharp joint singleton source without renewing its mantissa commitment. The gain is a checked first-order inheritance of the entire all-rounded seed reference even when final singletons are frozen; it supplies no universal FEI constant. Arbitrary prime J_hi still needs payment from genuinely unused ORIGINAL capacity after existing debits, with the restored seed law and both full terminals. That is the shortest NEXT because reference truncation, endpoint approximation and singleton source are now explicit, leaving the actual whole-set scale supplier rather than another paid-sector reformulation as the unresolved step.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
count=main['exact_assertions']+review['exact_assertions']
(A/'STATUS.md').write_text(f'STATE: A042 stage11 COMPLETE_LOCAL: full paid-reference KL/e -> seed ALL-rounded KL; uniform error<=e V ln4;{count} exact assertions PASS; A041 sharp joint source HOLDS; FEI OPEN.\nNEXT: A043/A044/A045 review concave complete-reference endpoint; pay arbitrary prime J_hi from unused ORIGINAL capacity after actual singleton/import/carry debit, preserving restored seed law and BOTH full terminal KLs.\n',encoding='utf-8')
tag='2026-10-23 stage11 20261023T142127Z'
for name,line in [('WORKLOG.md',f'\n{tag}: Proved exact paid-reference activation sector chain and monotone concave KL transport: e(1-e)Ka+e^2Kh<=Kpaid(root)<=eKa, uniform normalized error<=e(Ka-Kh)<=eVln4. The rare endpoint restores full ALL-rounded seed reference despite singleton freezing. Main{main["exact_assertions"]}+review{review["exact_assertions"]} exact assertions PASS; A041 sharp joint source/all-alpha owner independently HOLDS with nonzero low carry retained. Universal prime J_hi unpaid, new review pending, mirror unobserved. Brain self-care degraded, compute heartbeat stale, checklist lock blocked initial update; no research job running.\n'),('LEARNED.md',f'\n{tag}: For independent dyadic activation and singleton-preserving COMPLETE root reference, K_F=eKh+e(1-e)K1+e[M+(1-e)A]d_Bern((1-e)A/[M+(1-e)A]||(1-e)Z1/[Zh+(1-e)Z1]). Thus K_F/e=G(1-e), where G is monotone concave and G(0)=Kh,G(1)=Ka. Exact e(1-e)Ka+e^2Kh<=K_F<=eKa; error to eKa at most e^2(Ka-Kh)<=e^2 Vln4, uniform all seeds/dimensions. Freezing final singletons does NOT remove complete seed singleton-rounding KL at a rare endpoint. A041 optimal joint source J1+alphaL1<=max(ln4,2alpha)(2Delta-R) independently HOLDS; critical check reduces to L1<=2[(2Delta-R)-J1/ln4]. Preserve all original commitments and both full terminal laws.\n')]:
    p=A/name;old=p.read_text(encoding='utf-8') if p.exists() else ''
    if tag not in old:p.write_text(old+line,encoding='utf-8')
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert report.rstrip().split('\n\n')[-1].startswith('This stage advances C024')
assert all(p.stat().st_size<20_000_000 for p in R.rglob('*') if p.is_file())
put(R/'out/RECEIPTS.json',{'status':'PASS','at':now,'files':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(R.rglob('*')) if p.is_file() and p.name!='RECEIPTS.json'],'schema':'PASS','source_hashes':'PASS','compatibility_copy':'IDENTICAL','mirror':'UNOBSERVED_SUPERVISOR_ACTION'})
print(json.dumps({'status':'PASS','main':main['exact_assertions'],'review':review['exact_assertions'],'total':count,'new_claim':claim['claim_id'],'report':str(R/'REPORT.md')}))
