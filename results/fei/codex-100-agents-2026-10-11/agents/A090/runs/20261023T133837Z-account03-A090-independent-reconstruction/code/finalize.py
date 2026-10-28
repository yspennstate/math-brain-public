from pathlib import Path
import json,hashlib,datetime,copy
run=Path(__file__).resolve().parents[1];base=run.parents[1];fleet=base.parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,s):p.write_text(s,encoding='utf-8',newline='')
def dump(p,o):put(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
out=json.loads((run/'out/CHECK.json').read_text(encoding='utf-8'))
assert out['status']=='PASS' and out['assertions']==131631
assert out['checker_sha256']==sha(run/'code/check.py') and out['helper_sha256']==sha(run/'code/exact.py')
source=fleet/'A004/runs/20261023T124811Z-account03-A004-constant-and-unit-ledger/CLAIMS.json'
original=next(c for c in json.loads(source.read_text(encoding='utf-8-sig')) if c['claim_id']=='A004-NORMALIZER-AWARE-TARGET-FLOOR-TRANSPORT')
report=r'''# A090 stage10: normalizer transport independently holds; its Boolean floor loss is freely repairable

## exact target, quantifiers, hypotheses and units

Independently reconstruct A004-NORMALIZER-AWARE-TARGET-FLOOR-TRANSPORT@1 from its statement and original finite probability/Fourier definitions, without the supplied derivation. Then price the actual floor repair in its stated Boolean witness, using only the CURRENT account and leaving all old debits and the complementary terminal intact. All information is in bits. References are COMPLETE finite-CE subprobabilities of mass s in(0,1], including empty and reference-only atoms; their -log2(s) penalty is retained. The physical cube is uniform, and actual outputs are Boolean signs.

New narrow result: for any actual law P with positive nonempty mass a, complete finite-CE R of mass s, current nonempty conditional M and any prescribed conditional target T, if the true conditional pi dominates c*T, then changing ONLY the current nonempty conditional M to pi restores the c-target floor, preserves total reference mass and vacuum exactly, and has signed full price -a D_2(pi||M)<=0. It is a repair from a previously paid current reference, not initial influence pricing. Applied to A004's exact Boolean witness, the repaired conditional floor is8/21>1/4 and the reached original-owner release is>1/4 bit, with the old full sibling retained.

## sources actually read, revisions and theorem locators

Read BOARD2026-10-23 13:38 UTC, B18 STREAM_NOTES v2, own stage9 STATUS, and crash-restore common.md. Earlier artifacts survived and no prior run was overwritten. Productive/new-dependency dispatch selects the new normalizer bottleneck instead of repeating the old five-variable census. Read latest COMPLETE CLAIMS files from A001 run20261023T112820Z, A003 run20261023T121547Z, A004 run20261023T124811Z and A097 run20261023T121505Z. An initial attempt selected A001's newer active run without CLAIMS and stopped on FileNotFoundError; selection was corrected to completed CLAIMS paths. No claim was inferred from that incomplete run.

Only the named A004 theorem is independently accepted here. Other statements were context, not accepted full dependency chains. No producer DERIVATION or code was read or imported. Own prior Fraction/log helper was reused and modified to factor all bounded integer log atoms completely, preventing symbolic comparisons from mistaking an unfactored composite logarithm for a distinct atom. Source statement and code hashes are recorded.

The required session wake warned that owner-model100.1h, state-of-mind84.7h and dream35.4h are stale. Brain self-care remains degraded/unverified; affected owner-context notes were not mathematical authority. Research writes stay inside A090. Shared sources and brain remain read-only; no git, messages, trading access, remote/GPU jobs, detached work, process stops or resource shedding occurred. Supervisor publication remains unverified.

## complete derivation or exact first unsupported line

**Independent source verdict: HOLDS unchanged; no repair to A004's statement is needed.**

Let p be the parent spectrum and p_b the two true child spectra. The signed Fourier restriction formula gives mean_b p_b=m=M_i p. For any current reference q of mass s, write r=M_i q and define

    raw_b(t)=r(t)*p_b(t)/m(t) if m(t)>0,
    raw_b(t)=r(t) if m(t)=0,
    Z_b=sum_t raw_b(t), q_b=s*raw_b/Z_b.

At m(t)=0 both child masses are zero. The specified reference-only convention therefore gives mean raw=r on EVERY fiber, including zero fibers, and mean Z=s. Finite CE implies Z_b>0 for each normalized actual child. Each q_b has the ORIGINAL mass s and finite child CE; no normalizer disappears.

For two references q0,q1 of this SAME mass, raw is linear in q. Thus raw_lambda=(1-lambda)raw0+lambda raw1 and Z_lambda=(1-lambda)Z0+lambda Z1. Substituting rawk=Zk*qk_child/s proves exactly

    qlambda_child=(1-lambda_b)q0_child+lambda_b*q1_child,
    lambda_b=lambda Z1/[(1-lambda)Z0+lambda Z1].

Iterating along any common physical history gives posterior odds lambda_v/(1-lambda_v)=[lambda/(1-lambda)] L1/L0, Lk=product(Zk/s). This remains valid for adaptive choices because the next coordinate is fixed once the common physical history is fixed. Consequently lambda_v>=c is equivalent to L1/L0>=c(1-lambda)/[lambda(1-c)]. This component-weight condition is sufficient for a c target floor; overlap from the old component can make it unnecessary. No independence of successive normalizers is assumed.

For the exact complete information account, define DeltaH=H(p)-mean H(p_b)=B_i+JS_i. This is the FULL entropy decrement, not just the erasure. Expanding logs on occupied fibers gives

    CE(p_b,q_b)=CE(p_b,r)+H(p_b)-CE(p_b,m)+log2(Z_b/s).

Average p_b=m. With rho=D(p||q/s)-D(m||r/s)>=0 from the conditional KL chain rule,

    DeltaH+mean CE(p_b,q_b)-CE(p,q)
       =-rho+mean log2(Z_b/s)<=0.

The last sign follows from mean Z=s and concavity of log, not from an individual Z_b<=s assertion. References may have ghost mass; it is retained in Z, in the finite CE and in the subprobability term. If only physical erasure B is booked instead, the complete increment has the additional favorable term -JS_i. These two conventions must not be interchanged silently.

The source's explicit witness is reconstructed from its Boolean truth table, not its recorded outputs: f=+1 only at index0 on3 bits, query bit0, 256q0=(144,1,1,1,106,1,1,1), 256q1=(144,80,15,13,1,1,1,1), lambda=1/4. Both references have mass1 and empty mass9/16. For the nonconstant child the true law is P=(1/4,1/4,1/4,1/4), and exact inheritance gives

    qtarget=(7/12,35/96,5/192,5/192),
    qcurrent=(659/2484,85/1242,1615/2484,10/621),
    lambda_child=32/207.

Indeed qcurrent(1)=85/1242<qtarget(1)/4=35/384. Its conditional nonempty ratio to the target is272/2555<1/4. Thus the source's claimed fixed-floor loss is correct, including after vacuum recalibration, which leaves the conditional profiles unchanged. This does not refute the once-paid A001 quarter-frontier transaction or FEI.

**New free-repair corridor and the same actual witness.** Let a=1-P(empty)>0, w=s-R(empty)>0, pi=P_nonempty/a and M=R_nonempty/w. Finite CE ensures M>0 on occupied pi. Install

    Rstar(empty)=R(empty), Rstar(t)=w*pi(t) for t nonempty.

Mass and vacuum are unchanged. Subtraction of the COMPLETE costs, retaining the same vacuum and tail-mass terms, proves

    CE(P,Rstar)-CE(P,R)=-a D_2(pi||M)<=0.

If pi(t)>=c*T(t), the new conditional reference satisfies the desired c-target likelihood floor. This is a sufficient corridor for a nonpositive repair, not a universal assertion that every target can be installed for free. A full-target floor additionally depends on the target/current vacuum and tail masses; it is separately checked in the witness below.

In the actual source witness, pi=(1/3,1/3,1/3) and T=(7/8,1/16,1/16), hence min_t pi(t)/T(t)=8/21>1/4. Keep its CURRENT vacuum659/2484 and install

    Rstar=(659/2484,1825/7452,1825/7452,1825/7452).

This also satisfies the FULL atomwise inequality Rstar>=qtarget/4, including the empty atom. Its signed node price is exactly -(3/4)D_2(pi||M)<0. Keep the actual constant sibling at its full old inherited reference. With the original fair reach1/2 of the repaired child, the SAME ancestor account releases exactly (3/8)D_2(pi||M)>1/4 bit. Earlier erasure/DeltaH, admission, source and reset debits are unchanged; they cancel on both sides of this one signed transaction, not by being dropped. The checker compares both full terminal bills directly. Numerically the release is about0.5446896579 bits; the claim uses the certified rational lower bound1/4.

If the prior frontier first recalibrates the vacuum to its actual value1/4, the same conditional repair becomes the exact P law. The conditional ratio8/21 remains, and the repair price is still -(3/4)D(pi||M) because the actual tail mass is unchanged. The full target floor also holds: each actual atom1/4 exceeds one quarter of every target atom. Thus the witness remains freely repairable before or after the mentioned vacuum recalibration. The new result does not contradict the earlier floor LOSS: it installs a separately priced conditional calibration AFTER the loss, without changing the original reference prescription.

A guard against overpromotion is an actual two-bit character with P=delta at one nonempty label, matched incoming R=P, and a target point at another nonempty label. Requiring a quarter floor at the target forces at least1/4 reference mass away from the true atom, so any normalized repair costs at least log2(4/3)>0. Here pi does NOT dominate the target and the free-repair corridor correctly fails. This is an elementary actual Boolean boundary proof, not a new FEI counterfamily or a newly executed search.

**First unreconstructed universal implication:** arbitrary histories need not keep their true conditional profile above the required target floor, and the source supplies no uniform likelihood corridor for them. Outside this corridor one must identify the required compatible policy/target and pay its actual minimum conversion cost from the remaining SAME owner. A universal initial O(I) source price or an entropy coefficient contraction below1 is also unproved. The concrete A004 loss witness alone no longer demonstrates an unpaid repair: the explicit negative-cost repair above resolves it. The reviewed A004 transport theorem itself has no unreconstructed line at its stated scope.

## executed validation with domain, arithmetic, commands and outputs

Frozen before execution: out/FROZEN_SPEC.json, helper versionA090-normalizer-review-v1, all256 Boolean tables on3 bits, all3 coordinates, both actual children, masses1 and1/2, lambda1/4,1/2,3/4, no symmetry reduction or dimension increase. Also one specified two-query common physical path per truth table and the exact witness/repair. Estimate90MB, runtime guard55seconds; no job above300MB, so no heavy-job memok clearance was needed. Command: python -X utf8 runs/20261023T133837Z-account03-A090-independent-reconstruction/code/check.py.

PASS:131631 exact assertions,4608 parent transactions,9216 child mixture identities,256 two-query paths and2592 actual-zero-fiber occurrences, in32.67seconds. Integer Walsh and Fraction reconstruct every actual law. Exact prime-log identities check the full entropy-decrement/CE account with -log(s), normalizer signs, child mass conservation and the retained old-sibling repair transaction. Rational40-term atanh intervals with proved tail2t^81/[81(1-t^2)], t=(x-1)/(x+1), certify signs; integer logs are reduced to[1,2] and divided by a positive ln2 interval. Floats in CHECK are display only. The new witness release>1/4 is explicitly interval-checked, not inferred from its decimal. No inequality failure, timeout or aborted math pilot occurred. No formal checker was started or claimed to pass.

## proof dependencies and changed downstream conclusions

A004-NORMALIZER-AWARE-TARGET-FLOOR-TRANSPORT@1 independently HOLDS unchanged. The derivation uses only physical signed Fourier restriction, linearity of raw inheritance, KL chain rule and log concavity. A090 does not repair its source statement and remains eligible as its independent reviewer. The added free-repair corridor/witness is an A090 contribution, separately marked pending independent review, not independent acceptance of A090's own extension. Other A001/A003/A097 claims were not fully reviewed in this stage.

Downstream: fixed floor inheritance still cannot be assumed, but the displayed failure can be repaired without spending the diminished owner. Use the verified normalizer-dependent weights, inspect actual target overlap, and apply the free corridor where it holds before asserting a positive tariff. The new0.5446896579-bit release concerns this A004 reference-loss witness; it is NOT the earlier stage8 quota3 reserve0.2482104604, nor stage9's supplied-wrapper release>93/256. Different physical accounts are never added or substituted. Full FEI remains OPEN.

## one next mathematical action and independent reviewer

A004/A001/A094 should independently check this exact negative-cost repair and state one required continuation that accepts the installed floor with its retained mass/vacuum. For histories where pi does not dominate the needed target, determine the actual least CE floor projection and compare its reached cost to the SAME unused original source margin, including all old U/prefix/reset bookings and both complete terminals. A097's declared floor-class minimum is a useful comparison, not an automatic compatible-policy certificate. A003/B20 should continue demanding a noncircular universal source estimate or contraction below1. This report is a saved handoff; no message was sent.

## actual persistence receipts or precise save blocker

All four protocol files, frozen spec, independent code, CHECK, source receipts and hash manifests are saved inside this A090 run. STATUS, WORKLOG and LEARNED are updated. The finalizer verifies exact schemas, original statement hash, progress/delta byte equality, code/check binding, artifacts below20MB and per-file SHA256 readback. No new current checklist id was supplied for this invocation; no old entry was falsely closed. Previous stage's shared checklist-lock blocker remains an administrative historical receipt, not a math failure. Supervisor adoption, mirrors, publication and downstream independent review of the new repair remain unverified. Brain self-care remains degraded/unverified; no brain maintenance or repair is claimed.

**Universal bridge:** This stage advances C019 stopping-tree payment/C024 history transfer by independently closing the full normalizer-aware mixture inheritance theorem, then paying the actual quarter-floor repair in its Boolean loss witness at NEGATIVE cost from the SAME owner. The repaired conditional likelihood floor is8/21>1/4 and the reached account gains>1/4 bit, with vacuum, reference mass, old debits and the full sibling preserved. What remains is a useful required policy accepting the installed floor, and a compatible payment or likelihood corridor outside the true-profile dominance region; universal initial source pricing/contraction is still open. The shortest next route is to test that required policy against the CURRENT actual profile and price only a necessary projection outside the free corridor, rather than treating normalizer loss itself as an unpaid universal obstruction or proving another isolated class bound.
'''
put(run/'REPORT.md',report)
review=copy.deepcopy(original)
assert review['statement_sha256']==hashlib.sha256(review['exact_statement'].encode()).hexdigest()
review['review_records']=review.get('review_records',[])+[{'reviewer':'A090/account03','timestamp':now,'verdict':'HOLDS at unchanged full scope; no repair','producer_derivation_used':False,'method':'Own signed Fourier/raw mixture/KL reconstruction;131631 exact assertions; full zero-fiber/subprobability and entropy-decrement convention audit','source':str(run/'REPORT.md')}]
review['status']='INDEPENDENTLY_ACCEPTED_BY_A090_AT_UNCHANGED_SCOPE'
review['proof_source']=[str(source),str(run/'REPORT.md'),str(run/'code/check.py'),str(run/'out/CHECK.json')]
statement='For every actual spectral probability P with nonempty mass a>0 and complete finite-CE subprobability R of mass s in(0,1], let pi be the true conditional nonempty profile and M the current reference conditional nonempty profile. If pi>=c*T for a prescribed nonempty target probability T and0<c<1, replacing ONLY M by pi preserves total mass and vacuum, restores the conditional c-target floor, and has exact signed complete price -a D_2(pi||M)<=0. For A004 stated AND3 floor-loss witness at query0, the current reference(659/2484,85/1242,1615/2484,10/621) is repaired to(659/2484,1825/7452,1825/7452,1825/7452); its conditional floor against target(7/8,1/16,1/16) is8/21>1/4 and the FULL repaired law dominates one quarter of target child(7/12,35/96,5/192,5/192). Retaining the old complete sibling and every prior debit, the SAME original owner gains(3/8)D_2((1/3,1/3,1/3)||M)>1/4 bit. This is a conditional reference repair, not universal source pricing or automatic hereditary floor inheritance.'
cid='A090-FREE-TARGET-FLOOR-REPAIR-CORRIDOR'
claim={'claim_id':cid,'version':1,'exact_statement':statement,'hypotheses':['Finite uniform Boolean Fourier laws;complete reference mass s and vacuum fixed;positive actual/current nonempty masses','Current complete reference already supplied/paid;all old source/reset debits and full complementary terminals retained','Conditional true-profile dominance pi>=c*T is explicit;full atomwise floors require separate vacuum/tail-mass check','Witness is actual positive-only-at-origin AND3 with source references and fair physical reach1/2'],'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A090/account03; A004 supplies the original floor-loss witness'],'proof_source':['REPORT.md','code/check.py','code/exact.py','out/CHECK.json'],'proof_dependencies':['Finite conditional KL identity, proved here','A004-NORMALIZER-AWARE-TARGET-FLOOR-TRANSPORT@1 independently accepted for source transport;explicit witness recomputed'],'review_records':[],'status':'CHECKED_PROOF_AND_EXACT_CERTIFICATE_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':'Required compatible policy accepting the installed floor;needed projection outside true-profile dominance paid from same unused owner;universal influence-priced initial source or contraction<1.','next_consumers':['A001','A003','A004','A094','A097','B18','B20']}
dump(run/'CLAIMS.json',[review,claim])
source_paths=[source,fleet/'A001/runs/20261023T112820Z-account03-A001-quantifier-audit/CLAIMS.json',fleet/'A003/runs/20261023T121547Z-account03-A003-minimal-target-formulation/CLAIMS.json',fleet/'A097/runs/20261023T121505Z-account03-A097-cross-route-transfer/CLAIMS.json',base.parents[1]/'BOARD.md',base.parents[1]/'claude/B18/STREAM_NOTES.md',Path('~/CRASH_RESTORE_2026_10_23_1330/common.md')]
dump(run/'SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in source_paths])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run.name,'stream':'B18','packet_id':'A090','gap_id':'C019-C024-NORMALIZER-FLOOR-REPAIR','attempt_id':'A090-stage10-normalizer-and-free-corridor','method':'Statement-only independent source reconstruction;integer Walsh/Fraction/log certificates;KL conditional-profile repair and complete original-owner ledger','mathematical_delta':'A004 normalizer theorem HOLDS unchanged;actual Boolean quarter-floor loss witness freely repaired at conditional ratio8/21, SAME-owner release>1/4;131631 exact assertions,4608 transactions,9216 child mixtures,256 paths.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'SOURCE_INDEPENDENTLY_ACCEPTED;NEW_NARROW_REPAIR_PENDING_REVIEW;FULL_FEI_OPEN','claim_versions_used':['A004-NORMALIZER-AWARE-TARGET-FLOOR-TRANSPORT@1'],'claims_created_or_changed':['A004-NORMALIZER-AWARE-TARGET-FLOOR-TRANSPORT@1 independent review',cid+'@1'],'source_artifacts':[str(p) for p in source_paths],'next_consumers':['A001','A003','A004','A094','A097','B18','B20'],'next_action':'Supply required policy accepting installed mass/vacuum/floor;price only necessary floor projection outside pi>=c*T from CURRENT same unused owner,all old debits/full siblings retained.','stagnant_substantive_attempts':0,'blockers':['Required downstream floor policy compatibility not supplied','No general likelihood corridor or same-bank payment outside free true-profile dominance','Universal initial source pricing/contraction unproved','New repair independent review and supervisor adoption/publication unverified','Brain self-care owner/state/dream freshness degraded;no formal checker pass claimed'],'packet_ids':['A090']}
dump(run/'PROGRESS.json',progress);dump(run/'PACKET_DELTA.json',progress)
put(base/'STATUS.md','STATE: Stage10 saved: A004 normalizer transport independently HOLDS; its AND3 floor loss freely repaired at ratio8/21>1/4,SAME-owner release>1/4;131631 exact checks PASS;new repair review pending;FEI OPEN.\nNEXT: A004/A001/A094 review repair and supply REQUIRED compatible floor policy; outside pi>=c*T price minimum projection from CURRENT same unused owner/all old debits/full siblings;initial source price open.\n')
for fn,txt in [('WORKLOG.md','Stage10: read current board/B18/status/restore. Latest A001 active folder lacked CLAIMS; corrected read-only selection to completed files. Reconstructed A004 normalizer transport from statement only, no producer proof/code. HOLDS unchanged: full DeltaH, true-zero ghosts, mass s and log normalizers retained. New free true-profile corridor repairs stated AND3 floor loss: ratio272/2555 ->8/21, mass/vacuum unchanged, old sibling retained, same-owner release>1/4.131631 exact checks/4608 transactions/9216 child mixtures/256 two-query paths PASS in32.67s. No heavy job, no formal checker, git/messages or resource shedding. Required policy compatibility and universal source price remain open.'),('LEARNED.md','A004-NORMALIZER-AWARE-TARGET-FLOOR-TRANSPORT@1 independently accepted. Raw inheritance is linear but normalized child mixture weight uses Z1/Z0; along histories posterior odds multiply actual Zk/s. Full DeltaH+mean CE increment=-rho+mean log2(Z/s)<=0; physical B-only adds -JS. New A090-FREE-TARGET-FLOOR-REPAIR-CORRIDOR@1: fixing current mass/vacuum and replacing conditional M by true pi costs -a D(pi||M), so restores any target cT with pi>=cT for free. A004 AND3 loss witness has true pi uniform3,T=(7/8,1/16,1/16);repair ratio8/21>1/4, full floor also holds; SAME owner gains.5446896579>1/4. This repairs that witness, not hereditary floors universally; a distinct character target may force log(4/3)>0. Need actual compatible continuation or projection price outside corridor, not another optional reset.')]:
    with (base/fn).open('a',encoding='utf-8',newline='') as f:f.write('\n'+now+' '+txt+'\n')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))['required_per_run']
for c in [review,claim]:assert set(c)==set(protocol['claim_fields'])
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert all('## '+x in report for x in protocol['report_fields'])
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
files=[p for p in run.rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.name not in ['ARTIFACT_RECEIPTS.json','FINAL_VALIDATION.json']]
assert all(p.stat().st_size<20*1024*1024 for p in files)
dump(run/'out/ARTIFACT_RECEIPTS.json',[{'path':str(p.relative_to(run)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files])
for row in json.loads((run/'out/ARTIFACT_RECEIPTS.json').read_text(encoding='utf-8')):assert sha(run/row['path'])==row['sha256']
dump(run/'FINAL_VALIDATION.json',{'status':'PASS','timestamp':now,'protocol_fields':'EXACT','source_statement_hash':'PASS','checker_helper_binding':'PASS','progress_delta':'BYTE_IDENTICAL','hashed_files':len(files),'hash_readback':'PASS','source_review':'INDEPENDENT_HOLDS_UNCHANGED','new_repair':'PENDING_INDEPENDENT_REVIEW','full_fei':'OPEN','brain_selfcare':'DEGRADED_UNVERIFIED','formal_checker':'NOT_RUN','publication':'SUPERVISOR_UNVERIFIED','checklist':'No new invocation id supplied;previous lock failure not overridden'})
print(json.dumps({'status':'PASS','hashed_files':len(files),'assertions':out['assertions'],'source_review':review['claim_id'],'new_repair':cid,'owner_release_lower':'1/4','next':'required policy compatibility/outside-corridor projection;full FEI OPEN'}))
