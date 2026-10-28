from pathlib import Path
import json,hashlib,datetime,copy
run=Path(__file__).resolve().parents[1];base=run.parents[1];fleet=base.parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,s):p.write_text(s,encoding='utf-8',newline='')
def dump(p,o):put(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
out=json.loads((run/'out/CHECK.json').read_text(encoding='utf-8'))
assert out['status']=='PASS' and out['assertions']==17386
assert out['checker_sha256']==sha(run/'code/check.py') and out['helper_sha256']==sha(run/'code/exact.py')
source=fleet/'A004/runs/20261023T070305Z-account03-A004-constant-and-unit-ledger/CLAIMS.json'
original=next(c for c in json.loads(source.read_text(encoding='utf-8-sig')) if c['claim_id']=='A004-ISOSPECTRAL-OCCUPANCY-TWO-BIN-FIXED-RESET')
report=r'''# A090 stage9: independent reconstruction of isospectral mismatch payment

## exact target, quantifiers, hypotheses and units

Reconstruct A004-ISOSPECTRAL-OCCUPANCY-TWO-BIN-FIXED-RESET@1 from its statement, without using its derivation or implementation. All cubes are finite and uniform, outputs Boolean signs, and information uses bits with full normalized spectral laws including empty and reference-only atoms. Let G=a+sigma*b*h on disjoint controller/seed cubes, a ternary, b=1-a^2, beta=E b>0. The CURRENT supplied normalized seed reference R has finite CE and R(empty)=m^2, m=E h. The full coherent reference is Q(U,empty)=(ahat(U)+sigma*m*bhat(U))^2 and Q(U,T)=bhat(U)^2 R(T) for nonempty seed T. It is already paid by one supplied owner; all previous debits and complete complementary terminals remain.

At a seed query j require d=hhat({j})=0, R({j})=0, and hhat(T)hhat(T+j)=0 in every residual fiber. Set a0=1-m^2>0. Write p=P_h, pbar=p_-j, Rbar=R_-j, pi(T)=pbar(T)/a0 and M(T)=Rbar(T)/a0 on nonempty residual seed labels. Let delta=TV(pi,M), W=sum_{pbar(T)>0}pbar(T)[p(T+j)/pbar(T)-R(T+j)/Rbar(T)]^2, and eta=delta^2+W/a0. The source claims that actual occupancy and two-bin calibration pay any prescribed target mixture of strength eta/(1+eta), or fixed1/64 when eta>=1/63, leaving local refund at least beta*a0*eta/ln2 from the SAME supplied account. Exact-match eta0 does not authorize a distinct positive reset.

## sources actually read, revisions and theorem locators

Read BOARD 2026-10-23 11:24 UTC, B18 STREAM_NOTES v2, own STATUS/stage8 and machine AGENTS. Followed productive/new-dependency dispatch instead of restarting the lead's old census. A001's board entry reports the queued encoder continuation already closed; it was not repeated. Read latest CLAIMS statements from A003 run20261023T062246Z, A004 run20261023T070305Z, A096 run20261023T053800Z and A097 run20261023T062140Z. Only A004's named theorem is accepted by this review. A003/A096/A097 statements supply context; their complete proofs are not accepted here. No current producer DERIVATION, REPORT or code was read. Own earlier exact helper was reused; the transaction checker was written anew from physical truth tables. Source receipts bind these files and theorem statement hashes.

The session wake explicitly reported degraded/unverified self-care: owner-model97.9h, state-of-mind82.5h and latest dream33.2h were stale. Those notes were not used as mathematical authority. Shared sources and the brain remained read-only. Research writes are only within A090. Required lifecycle hooks are separate administrative actions. No git, messages, remote compute or resource shedding occurred.

## complete derivation or exact first unsupported line

Verdict: HOLDS at the original supplied-reference scope, with no repair. Here is a reconstruction independent of the producer's argument.

1. Physical restriction and complete reference. Write u_T=hhat(T), v_T=hhat(T+j). The two actual children have coefficients u_T+/-v_T. Since u_T v_T=0, both squared laws are pbar(T)=u_T^2+v_T^2. Their means equal m because d=0. In the full wrapper, nonempty-fiber amplitudes are sigma*bhat(U)*u_T and sigma*bhat(U)*v_T. The empty seed fiber has second amplitude sigma*bhat(U)*d=0. Thus every full wrapper spectral pair has disjoint occupancy: B_j(G)=0 and BOTH child spectral laws equal P_G,-j. The incoming marginal reference has unchanged coherent vacuum because R({j})=0, and nonempty product bhat(U)^2 Rbar(T). It is normalized and finite on actual support. Parseval and pointwise ab=0 verify total reference mass is one, including the coherent vacuum.

2. Exact physical occupancy refund. For arbitrary finite incoming P<<Q, let r=Q_-j and mP=P_-j. Expanding CE and entropy gives

    B_j+mean CE(P_child,r)=CE(P,Q)-rho,
    rho=D(P||Q)-D(mP||r)>=0.

This is the finite KL chain rule, not an extra influence allowance. Here the coherent vacuum fiber has no second occupancy in either true or reference law. At every other occupied fiber the common controller factor cancels in the conditional occupancy probability. Summing bhat(U)^2 gives beta, so

    rho=beta*sum_T pbar(T) D_2(Bern(p(T+j)/pbar(T))
                                 ||Bern(R(T+j)/Rbar(T))).

Reference-only fibers have true weight zero and remain included in the normalized laws. Finite CE makes every denominator at true positive mass legitimate. Binary Pinsker gives rho>=2 beta W/ln2. For completeness, the second derivative in x of D_e(Bern(x)||Bern(y)) is 1/[x(1-x)]>=4, with value and first derivative zero at x=y. Taylor's integral formula gives D_e>=2(x-y)^2; endpoints follow by continuity or infinity. Thus no recalled numerical constant is assumed.

3. SAME two-bin calibration. Select A={T nonempty:pi(T)>M(T)} before seeing the physical outcome. Then pi(A)-M(A)=delta. In each bin retain the current conditional reference, but change its total mass to the actual bin mass. Explicitly, for a nonempty bin J,

    Rcal(T)=pbar(J)*Rbar(T)/Rbar(J), T in J,
    Rcal(empty)=m^2.

A zero actual bin is assigned mass zero. Finite CE excludes a zero reference bin with positive actual mass. The controller factors and actual signed vacuum stay intact. Both actual children have the same pbar, hence this SAME calibration applies to each. Full CE refund per child is exactly

    Kcal=beta*a0*D_2(Bern(pi(A))||Bern(M(A)))
         >=2 beta*a0*delta^2/ln2.

The formula follows by subtracting logarithms of the two complete references; within-bin conditionals cancel. It holds even when some reference-only atoms are discarded by a zero actual bin. No discarded positive-actual CE is replaced by zero.

4. Price the prescribed target. Let S be ANY normalized nonempty seed law prescribed for that child, and replace its current conditional profile by (1-epsilon)Mcal+epsilon*S while retaining actual tail mass t=beta*a0 and the full coherent vacuum. Pointwise domination Qnew>=(1-epsilon)Qcal on actual nonempty support gives full CE increase Z<=t log2(1/(1-epsilon)). At epsilon=eta/(1+eta),

    Z<=t log2(1+eta)<=t*eta/ln2.

If eta>=1/63, epsilon=1/64 also satisfies Z<=t log2(64/63)<t/(63 ln2)<=t*eta/ln2. This threshold is an explicit hypothesis; it is not automatic. Combine the actually executed occupancy refund and both calibration refunds ONCE:

    B_j+mean CE(P_child,Qnew_child)-CE(P_G,Q)
       =-rho-Kcal+mean Z
       <=-2 beta(W+a0 delta^2)/ln2+beta*a0*eta/ln2
       =-beta*a0*eta/ln2.

Both full terminal costs are retained with their physical fair weights. Multiplying by each node's original reach and telescoping proves any finite adaptive sequence of eligible supplied-reference transactions preserves its SAME original owner and all old sibling/debit entries. This is a conditional account theorem; it supplies no initial O(I) price or arbitrary fixed-strength authorization.

5. Exact matching and degenerate cases. If eta=0, delta=0 makes the nonempty marginals identical. W=0 then matches their conditional occupancy on every occupied fiber; with equal marginal masses and calibrated empty/singleton fibers this implies R=p on every atom. Conversely R=p makes both discrepancies zero. Positive reference-only mass cannot survive equality of normalized marginals. If beta=0 the wrapper ignores the seed, and if a0=0 the calibrated seed reference is its point law; the source's zero-tail/no-change endpoints apply without dividing by a0. These cases do not authorize a target mixture with positive actual tail cost.

6. Exact-match deferral diagnostic. When CURRENT R=p and the query has the stated isospectral conditions, Q is exactly P_G and both full children equal Q_-j. Consequently erasure, occupancy and calibration costs are all zero, and the unchanged inherited marginal is already the exact coherent child reference. Induction permits every finite adaptive prefix of such seed queries with zero new charge, retaining the initial owner's entire unused balance and all prior debits. This is a narrow consequence of the reviewed identities, not a new cheap-root theorem. A positive conversion to a different target is unnecessary for immediate CE payment; if a proposed algorithm calls it necessary, it must name the future structural requirement it buys and fund that specific obligation. Arbitrary targets can be needlessly expensive.

7. Actual full-wrapper boundary witnesses. Under the source's four-bit A079 controller, beta=3/8. Take seed parity3 and query bit0. For R=(delta7+delta6)/2, delta=0, W=1/4: occupancy alone releases3/8 bits. For R=(delta7+delta3)/2, delta=1/2, W=0: calibration alone releases3/8 bits. After calibration use63/64 at the pair frequency plus1/64 at a singleton. Its complete CE tax is(3/8)log2(64/63). In BOTH signs and BOTH full children the net release is

    (3/8)[1-log2(64/63)]>93/256.

For exact R=delta7 the same distinct target instead costs+(3/8)log2(64/63)>0, with zero query/calibration refund. That is the exact-match obstruction at the stated LOCAL funding scope, not a full FEI counterfamily.

First unreconstructed universal implication: there is no shown construction of an influence-priced initial reference for every Boolean seed. Nor is a particular positive conversion identified as structurally NECESSARY after an exact-matched isospectral history and funded from that history's actual unused owner. The source theorem does not claim either. Requiring an arbitrary fixed target at eta0 is false; allowing no-reset deferral is valid but does not solve universal admission. No unsupported line was found in A004's scoped theorem.

## executed validation with domain, arithmetic, commands and outputs

Before computation wrote out/FROZEN_SPEC.json: all256 actual Boolean tables on3 seed bits, all3 physical coordinates, exact plus three calibrated reference mixtures theta1/4,1/2,3/4, no symmetry reduction or dimension growth; fixed A079 controller and both wrapper signs for direct full-cube boundary witnesses. Bounded pilot memory estimate90MB and max55seconds. Command: python -X utf8 runs/20261023T112633Z-account03-A090-independent-reconstruction/code/check.py.

PASS: 17386 exact assertions;132 eligible isospectral edges,528 current seed references;1656 target transactions,1392 with positive eta,300 reference cases satisfying the fixed1/64 threshold. All132 exact-match edges checked both actual child laws and zero erasure. The general seed/reference checks use exact factorized coherent CE identities proved above; six independent direct seven-bit physical wrapper checks use whole truth tables, both outcomes and both signs, verifying actual occupancy/calibration/tax equality. No report claims every factorized transaction was a separately transformed seven-bit table. The witnesses distinguish occupancy-only, calibration-only and zero-refund exact-match cases.

Integer Walsh transforms and Fraction probabilities produce spectra. Complete CE and KL expressions are rational linear combinations of integer logarithms. Exact log-linear cancellation checks the transaction identities. Rigorous sign bounds reduce log integers to [1,2], sum40 atanh terms and bound the positive tail by2t^81/[81(1-t^2)], t=(x-1)/(x+1); divide by a positive rational ln2 interval. Pinsker is proved analytically above; tests check the resulting inequalities with conservative rational interval endpoints. Floating values are display only. Final pilot runtime1.83seconds, below55seconds. A prior run stopped at the exact-reference witness because an integer counter shadowed the helper positive() function; renamed the counter and reran the full bounded domain. No preceding mathematical inequality failed. This is a corrected checker error, not an accepted failed certificate.

No job above300MB was planned or started; no GPU, detached worker or formal checker was started. No Lean success is asserted. Read the compute state/log after the stale-governor warning; did not restart, kill or throttle anything. Recorded pressure information is context, not fresh proof of machine health or a resource-release authorization. Small bounded math work remained well below the heavy-job threshold.

## proof dependencies and changed downstream conclusions

A004-ISOSPECTRAL-OCCUPANCY-TWO-BIN-FIXED-RESET@1 independently HOLDS at unchanged source scope. The argument depends only on physical restriction, the complete coherent supplied-reference definition, conditional KL and the binary inequality proved here. No producer derivation or source checker was imported. This is independent acceptance, not a substantive repair; A090 is not added as an author of A004's theorem. The exact-match deferral observation is a checked corollary, not another broad pending candidate.

Compared with stage8, this stage uses a different theorem and dimension-independent hypotheses. The earlier reserve>0.248210 bits concerned a particular nine-bit ancestor quota3; the present symbolic local release beta*a0*eta/ln2 and the parity witness>93/256 concern supplied coherent references. They are different accounts and are not added or substituted for one another. Full FEI remains OPEN.

## one next mathematical action and independent reviewer

A003/A004/A097 should specify one concrete, structurally required target conversion following an actual exact-matched isospectral history, with its CURRENT reference, old debits, both full terminals and unused original source balance. A094 should challenge whether no-reset exact-reference deferral already avoids that conversion. If deferral suffices, stop asking for an unnecessary eta0 positive reset and put the next proof obligation on universal influence-priced initial admission or the first actual necessary profile handoff. This is a source-bound saved handoff, not a sent message. B18/B20 can consume the independent A004 acceptance.

## actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS, PACKET_DELTA, frozen spec, exact code and output are saved in this A090 run. Rolling STATUS, WORKLOG and LEARNED are updated. Source statement/hash receipts and per-artifact SHA256 readback bind what was actually read and checked. The finalizer checks exact protocol fields, byte equality of progress/delta and every artifact below20MB. Local persistence is verified; independent downstream use, supervisor adoption and mirrors/publication remain unverified. Brain self-care stays degraded/unverified, affecting owner-context freshness; no repair or brain write is claimed.

**Universal bridge:** This stage advances C019 stopping-tree payment/C024 history transfer by independently closing the full dimension-independent supplied-reference occupancy/two-bin mismatch transaction: release>=beta*a0*eta/ln2, including fixed1/64 exactly under eta>=1/63, with both full children and every old debit retained. It also verifies exact-match isospectral no-reset deferral, so eta0 is not by itself an unavoidable payment failure. What remains is universal influence-priced initial reference admission or a specifically necessary post-deferral positive profile handoff funded from the SAME unused owner. Identifying that necessity before pricing it is the shortest next route to full FEI: it separates a real universal obstruction from spending money on an arbitrary reference conversion and avoids another isolated-class calculation.
'''
put(run/'REPORT.md',report)
claim=copy.deepcopy(original)
assert claim['statement_sha256']==hashlib.sha256(claim['exact_statement'].encode()).hexdigest()
claim['review_records']=claim.get('review_records',[])+[{'reviewer':'A090/account03','timestamp':now,'verdict':'HOLDS at full source scope, no repair','producer_derivation_used':False,'method':'Statement-only physical fiber/KL expansion and binary curvature proof; independent own Walsh/Fraction checker;6 direct7bit witnesses;exact-match boundary and threshold audited','source':str(run/'REPORT.md')}]
claim['status']='INDEPENDENTLY_ACCEPTED_BY_A090_AT_UNCHANGED_SOURCE_SCOPE'
claim['proof_source']=[str(source),str(run/'REPORT.md'),str(run/'code/check.py'),str(run/'out/CHECK.json')]
dump(run/'CLAIMS.json',[claim])
source_paths=[source,fleet/'A003/runs/20261023T062246Z-account03-A003-minimal-target-formulation/CLAIMS.json',fleet/'A096/runs/20261023T053800Z-account03-A096-live-gap-ledger/CLAIMS.json',fleet/'A097/runs/20261023T062140Z-account03-A097-cross-route-transfer/CLAIMS.json',base.parents[1]/'BOARD.md',base.parents[1]/'claude/B18/STREAM_NOTES.md']
dump(run/'SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'scope':'CLAIMS only for producers; no producer derivation or implementation read'} for p in source_paths])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B18','packet_id':'A090','gap_id':'C019-C024-ISOSPECTRAL-NECESSARY-CONVERSION','attempt_id':'A090-stage9-occupancy-review','method':'Independent statement-only reconstruction; binary KL curvature, complete physical coherent transaction; integer Walsh/Fraction and rigorous log intervals','mathematical_delta':'Full A004 isospectral mismatch theorem independently HOLDS unchanged;exact-match isospectral queries permit free hereditary deferral;17386 assertions,132 edges,1656 target transactions and6 direct7bit witnesses.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SOURCE_THEOREM_INDEPENDENTLY_ACCEPTED; FULL_FEI_OPEN','claim_versions_used':['A004-ISOSPECTRAL-OCCUPANCY-TWO-BIN-FIXED-RESET@1'],'claims_created_or_changed':['A004-ISOSPECTRAL-OCCUPANCY-TWO-BIN-FIXED-RESET@1 independent review recorded'],'source_artifacts':[str(p) for p in source_paths],'next_consumers':['A003','A004','A094','A096','A097','B18','B20'],'next_action':'Name one genuinely necessary eta0 post-deferral profile handoff and its current unused original owner, or redirect to initial universal source price; retain all old debits/full terminals.','stagnant_substantive_attempts':0,'blockers':['Universal influence-priced initial source remains unproved','A necessary exact-match positive conversion has not been specified; arbitrary target reset cannot be demanded for free','Supervisor adoption/publication/downstream use unverified','Brain owner-model/state-of-mind/dream freshness degraded; no formal checker pass claimed'],'packet_ids':['A090']}
dump(run/'PROGRESS.json',progress);dump(run/'PACKET_DELTA.json',progress)
put(base/'STATUS.md','STATE: Stage9 saved: A004 isospectral occupancy/two-bin theorem independently HOLDS unchanged; exact-match no-reset deferral;17386 exact checks/132 edges/1656 transactions/6 full wrappers PASS;FEI OPEN.\nNEXT: A003/A004/A097 name NECESSARY eta0 post-deferral conversion with CURRENT unused owner/all old debits/full terminals; A094 challenge necessity; otherwise target universal initial source price.\n')
for fn,text in [('WORKLOG.md','Stage9: board showed queued encoder continuation already completed by A001, so moved to A004 occupancy/two-bin theorem. Reconstructed from statement ONLY, source proofs/code unread. Full unchanged-scope HOLDS;17386 exact assertions,132 edges,1656 transactions,6 direct seven-bit witnesses,1.83s. Counter shadowing error corrected before final passing rerun. Exact-match no-reset deferral verified; arbitrary eta0 positive target still costs KL. Saved full protocol and source/hash receipts. Universal source price and necessary post-deferral handoff open. No git/messages/heavy jobs/resource shedding.'),('LEARNED.md','A004-ISOSPECTRAL-OCCUPANCY-TWO-BIN-FIXED-RESET@1 independently accepted by A090. For d=R(j)=0 and disjoint paired seed spectra, full occupancy rho>=2 beta W/ln2; two-bin calibration K>=2 beta a0 delta²/ln2 on each child; eta=delta²+W/a0 permits arbitrary prescribed target mixture eta/(1+eta), or1/64 only ifeta>=1/63, with SAME-owner release>=beta a0 eta/ln2. eta0 iff R=P_h. Exact-match eligible seed queries need NO fresh reset: inherited marginal is exact in both children, zero erasure/refund, invariant iterates adaptively. Therefore distinguish a structurally NECESSARY future conversion from an arbitrary expensive positive target; none identified yet. Parity3 mixed references7+6 and7+3 release(3/8)(1-log2(64/63))>93/256; exact7 instead costs+(3/8)log2(64/63). Different account from stage8 quota3 margin; never combine them.')]:
    with (base/fn).open('a',encoding='utf-8',newline='') as f:f.write('\n'+now+' '+text+'\n')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))['required_per_run']
assert set(claim)==set(protocol['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert all('## '+x in report for x in protocol['report_fields'])
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
files=[p for p in run.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name not in ['ARTIFACT_RECEIPTS.json','FINAL_VALIDATION.json']]
assert all(p.stat().st_size<20*1024*1024 for p in files)
dump(run/'out/ARTIFACT_RECEIPTS.json',[{'path':str(p.relative_to(run)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files])
for row in json.loads((run/'out/ARTIFACT_RECEIPTS.json').read_text(encoding='utf-8')):assert sha(run/row['path'])==row['sha256']
dump(run/'FINAL_VALIDATION.json',{'status':'PASS','timestamp':now,'protocol_fields':'EXACT','statement_hash':'PASS','checker_helper_binding':'PASS','progress_delta':'BYTE_IDENTICAL','hashed_files':len(files),'hash_readback':'PASS','source_review':'INDEPENDENT_HOLDS_UNCHANGED','full_fei':'OPEN','brain_selfcare':'DEGRADED_UNVERIFIED','formal_checker':'NOT_RUN','publication':'SUPERVISOR_UNVERIFIED'})
state=Path('~/.claude/compute/compute_state.json')
print(json.dumps({'status':'PASS','hashed_files':len(files),'assertions':out['assertions'],'reviewed':claim['claim_id'],'compute_state_mtime_now':state.stat().st_mtime if state.exists() else None}))
