from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
run=R.name
sha=lambda b:hashlib.sha256(b).hexdigest()
def save(name,obj): (R/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
statement=('For every finite ordered priority controller formed by disjoint point tests A_1,...,A_k of arbitrary positive widths and selecting pairwise disjoint independent Boolean data cores u_1,...,u_k with default +1, every finite adaptive physical restriction tree respecting priority order for control queries, with arbitrary data interruptions, has H(F)<=U_root+R_root+(3/ln2)T_data+(8+2/ln2)Pi_ctrl+E[H_leaf-U_leaf-R_leaf]. Here U=sum p_j[H(u_j)-eta((Eu_j)^2)], R=sum eta(p_j)Var(u_j), T_data=sum visited-node weights p_j beta_j^2, and Pi_ctrl is same-tree actual controller influence spent. At controller-resolved leaves the final term is eta((Eu_leaf)^2)<=I_leaf/ln2. The local repeated-fallback point test F=A u+(1-A)G, with u,G on disjoint blocks, satisfies D_control-kappa<=(8+2/ln2)Inf_control even though the same G occurs in both children. All entropy units are bits. There is no depth, width or number-of-stages bound, and inherited U and unresolved terminal entropy are retained.')
claim={'claim_id':'A059-INTERRUPTED-PRIORITY-STOPPING-PAYMENT','version':1,'exact_statement':statement,'hypotheses':['Finite uniform physical cube; pairwise disjoint controller point-test blocks and independent disjoint data-core blocks; genuine Boolean signs.','Controller queries respect priority order; arbitrary adaptive data interleavings and finite frontiers; irrelevant blocks skipped.','Repeated fallback data between children allowed; distinct selected cores do not share physical data.','Bits; eta(0)=0; unresolved stopping profile retained, no universal inherited-core entropy bound.'],'statement_sha256':sha(statement.encode()),'contributors':['A059'],'proof_source':{'run_id':run,'path':'PRIORITY_PROOF.md','locators':'Equations (1)-(4), direct repeated-fallback Fourier sectors and ordered priority induction'},'proof_dependencies':[{'claim_id':'A059-INTERLEAVED-BIASED-STOPPING-RESERVE','version':1,'scope':'signed data drift, independently accepted by A091 source run 20261014T013816Z'},{'claim_id':'A091-POINT-CONTROLLER-RESIDUAL-AND-BOUNDARY','version':1,'scope':'resolved terminal profile and physical JS inequality reconstructed; accepted locally in REVIEW_A091.md'},'Elementary binary entropy/Hellinger inequality proved here; exact Fourier algebra; physical same-tree influence conservation'],'review_records':[],'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A087','A091','A090','A057','A064','B12','B20']}
save('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':run,'stream':'B12','packet_id':'A059','gap_id':'G-A059-DECOMPOSITION-DEPTH','attempt_id':'A059-depth-3','method':'Direct repeated-fallback Fourier sector identity and fine reserve reset; same-tree stopped payment; source-bound A091/A087 reviews','mathematical_delta':'Pays interrupted arbitrary-width ordered priority control at 8+2/ln2, uniformly in depth and number of stages. Exact coarsening profile conversion and local mean-migration obstruction s/2 retained as ancillary. Shared outer killed-child price identified as A087 overlap and not a new claim.','deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_STOPPING_THEOREM; FULL_FEI_OPEN','claim_versions_used':['A059-INTERLEAVED-BIASED-STOPPING-RESERVE@1 (accepted by A091)','A091-POINT-CONTROLLER-RESIDUAL-AND-BOUNDARY@1 (reviewed here)','A087-OWNED-CONTROLLER-REVEAL-AND-RESOLVED-CONTINUATION@1 (killed/independent-child scope reviewed here; repeated-fallback excluded)'],'claims_created_or_changed':['A059-INTERRUPTED-PRIORITY-STOPPING-PAYMENT@1'],'source_artifacts':['REPORT.md','PRIORITY_PROOF.md','PROOF.md','REVIEW_A091.md','REVIEW_A087.md','code/check.py','code/exact.py','code/priority.py','out/FROZEN_SPEC.json','out/PRIORITY_FROZEN_SPEC.json','out/validation.json','out/priority_validation.json','out/SOURCE_SNAPSHOTS.json','out/RECEIPTS.json'],'next_consumers':claim['next_consumers'],'next_action':'A091/A090 independently reconstruct the repeated-fallback identity, then test a controller query of a later priority event before an earlier event is resolved using the same fine reserve; do not reopen paid outer or control-only classes.','stagnant_substantive_attempts':0,'blockers':['Arbitrary controller order and arbitrary controller residual payment remain open.','Inherited arbitrary core entropy and unresolved terminal payment are not bounded universally.'],'packet_ids':['A059']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
report='''# A059 stage 3: interrupted priority stopping payment

## exact target, quantifiers, hypotheses and units

Prove a physical stopping theorem with no bound on formula depth for exclusive disjoint-core compositions. The proved scope is ordered priority controllers built from arbitrary-width disjoint point tests, arbitrarily many tests, and arbitrary adaptive data interruptions. All entropy and reserve units are bits. The exact theorem is PRIORITY_PROOF.md (4); the inherited U and actual stopping profile remain explicit. An actual growing-depth family has d point tests of width d and d private literals: d^2+d inputs and a prescribed worst-case controller path of depth d^2. The same constant covers data queries inserted during each point test. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read the full execution protocol v2, BOARD snapshot 2026-10-14 02:53 UTC, B12 STREAM_NOTES v2 (2026-10-11 23:30 UTC), own STATUS and prior run proof/kernel. Read A091 run 20261014T013816Z REPORT, CLAIMS and POINT_CONTROL_PAYMENT.md: point price and terminal profile. Read A087 run 20261014T020842Z REPORT, CLAIMS and PROOF.md in full: killed-child/independent-child payment, r=s=1 continuation, and its explicit interrupted r=2 repeated-fallback next gap. A028 control-only arbitrary-width priority payment was learned from A087/BOARD; its proof is not a dependency and no independent acceptance of A028 is asserted. Source paths and SHA256 snapshots are in out/SOURCE_SNAPSHOTS.json.

## complete derivation or exact first unsupported line

PRIORITY_PROOF.md derives the fine reserve release kappa=q Var(u)+[eta(1-q)-eta(1-2q)/2]Vbar and the exact erasure sector identity for F=A u+(1-A)G with the SAME G in both children. Removing the first release and bounding the three remaining terms by 4qd, 8qd and 4qd gives B-kappa<=8 Inf. Physical JS adds 2 Inf/ln2. This is valid after arbitrary data restrictions. Ordered priority induction and the independently accepted signed data drift telescope to (4) with no accumulated depth factor. Controller-resolved terminal is eta(m^2)<=I_leaf/ln2.

PROOF.md also records exact coarse/fine terminal conversion q[T_P-eta(M^2)+s Var(state means)] and an actual Boolean mean-migration witness: querying one of two equiprobably selected literals increases the merging potential by s/2 times actual data influence. This refutes a fixed-price local helper, not FEI. Its mixed outer price overlaps A087's already-proved killed-child theorem and is expressly not claimed as novel.

First unsupported universal line: an arbitrary exclusive controller admits a physical tree whose every controller residual is paid at a universal same-tree influence rate. Even querying later priority tests before earlier tests are settled is outside this stage's theorem. Arbitrary initial core entropy and unresolved terminal payment remain explicit.

## executed validation with domain, arithmetic, commands and outputs

Frozen specifications precede both jobs. Exact Fraction FWHT and rational linear combinations of prime logarithms; signs use 32-term atanh bounds with a proved rational tail. Floating-point values measure runtime only. Commands from A059 cwd:

    python -X utf8 runs/'''+run+'''/code/check.py --pilot
    python -X utf8 runs/'''+run+'''/code/check.py
    python -X utf8 runs/'''+run+'''/code/priority.py --pilot
    python -X utf8 runs/'''+run+'''/code/priority.py

Mixed-state pilot PASS: 16 roots, 64 trees, 2728 assertions, 19.414 s. Main PASS: 560 roots, 1984 trees, 12032 frontiers, 81734 assertions, 854 outer nodes and 1255 terminal conversions, 231.099 s. Includes every 3-label one-bit internal map, all ordered one-bit Boolean core pairs, outer widths 1..3, four policies, and four two-bit fixtures; no symmetry reduction. The exact migration ratio s/2 is certified for s=1..64; its infinite extension is analytic, not a finite inference.

Repeated-fallback pilot PASS: 2 roots, 36 live query states, 324 assertions, 0.048 s. Main PASS: 48 roots, 1008 live private A query states, 9072 assertions, 0.765 s: (r,s)=(2,1),(3,1),(2,2), all 16 ordered one-bit Boolean core pairs, every surviving A prefix and all 9 combinations of earlier core restrictions. Direct full-function Walsh erasure agrees exactly with the new formula. Main jobs ran sequentially, with estimated memory 180 MB each, so memok threshold was not reached. Max truth table was 128 entries in the second job. Actual peak RSS was not measured. No dimension escalation occurred. These finite checks supplement the all-dimensional analytic proof.

## proof dependencies and changed downstream conclusions

Consume A059 interleaved reserve v1 as independently accepted by A091; independently reconstruct A091 point/profile scope and A087 killed/independent-child scope without substantive source repair (REVIEW_A091.md and REVIEW_A087.md). The stream review cap is addressed by these source reviews before the one new candidate is finalized. The new repeated-fallback formula supplies the boundary A087 specifically left open. It permits arbitrary-width priority tests interrupted by data and arbitrary numbers of stages, while retaining one fine reserve and actual terminal. Initial reserve funding is not reused. No arbitrary-order extension or universal FEI conclusion follows.

## one next mathematical action and independent reviewer

A091, alternate A090, should independently reconstruct equations (2),(3), including the off-label release. The next mathematical action is to expose a later priority controller while an earlier test remains undecided, and derive its exact residual under the same fine reserve. That isolates the remaining order restriction rather than reopening a settled control-only family.

## actual persistence receipts or precise save blocker

Required four protocol files, proofs, source reviews, frozen specs, scripts and exact validation outputs are saved in this run; rolling STATUS/WORKLOG/LEARNED are updated. out/RECEIPTS.json records SHA256 and sizes, generated after artifact writes, and out/SCHEMA_CHECK.json verifies exact protocol keys and compatibility equality. Files are below 20 MB. Only A059 files were written. GitHub/brain mirroring is supervisor work and is not verified here. No save blocker.

Universal bridge: This stage advances C019 stopping-tree payment by removing both priority width and depth bounds in the presence of arbitrary data interruptions: controller debt costs at most (8+2/ln2) times same-tree controller influence, and resolved terminals cost at most I_leaf/ln2. The repeated fallback is retained coherently rather than falsely declaring children independent. C018 for arbitrary controllers, arbitrary controller order, inherited arbitrary-core entropy and unresolved terminal profiles remain unpaid. The NEXT is the first out-of-order priority query: removing that order restriction tests the exact obstruction between this stopped theorem and a universal controller payment, rather than producing another isolated class estimate.
'''
(R/'REPORT.md').write_text(report,encoding='utf-8')
(A/'STATUS.md').write_text('STATE: Interrupted arbitrary-width ordered priority stopping payment proved locally at 8+2/ln2; 90806 exact assertions PASS; A091/A087 scoped reviews accepted; full FEI OPEN.\nNEXT: A091/A090 review repeated-fallback identity; derive fine-reserve residual when a later priority test is queried before an earlier test is settled.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+' '+run+': Read board/lead/status and A091/A087. Mixed outer reconstruction overlapped A087; recorded provenance, did not claim novelty. Exact grouping/migration helper obstruction retained. Derived interrupted reused-fallback point-test payment 8+2/ln2 and arbitrary-width/many-stage priority stopping theorem. Main checks PASS 81734 + 9072 assertions. Independent scoped source reviews saved; one new claim pending review. No full FEI claim.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+': Reused fallback F=A u+(1-A)G does not need independent children. Fine release is qVar(u)+[eta(1-q)-eta(1-2q)/2]Vbar. Exact B=qVar(u)+(q-2q^2)(Var(G)+(m-n)^2)+Var(G)Phi((1-q)^2,q^2)+Phi((n+q(m-n))^2,q^2(m-n)^2). This gives D-kappa<= (8+2/ln2)Inf and ordered priority stopping with arbitrary widths/stages/data interruptions. Arbitrary control order remains open. Coarse/fine mean-migration correction cannot be repaid per data query at fixed rate: literal witness ratio s/2. A087 already owns the mixed killed-child 3+2/ln2 theorem.\n')
base=Path(r'~\brain_workers\FEI100_20261011')
sources=[base/'BOARD.md',base/'claude/B12/STREAM_NOTES.md',A/'runs/20261013T235852Z-fleet05-A059-decomposition-depth/PROOF.md',A/'runs/20261013T235852Z-fleet05-A059-decomposition-depth/code/check.py']
for agent,rid,files in [('A091','20261014T013816Z-fleet05-A091-composition-referee',['REPORT.md','CLAIMS.json','POINT_CONTROL_PAYMENT.md']),('A087','20261014T020842Z-fleet05-A087-restriction-referee',['REPORT.md','CLAIMS.json','PROOF.md'])]:
 sources += [base/'agents'/agent/'runs'/rid/file for file in files]
save('out/SOURCE_SNAPSHOTS.json',[{'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sources])
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))['required_per_run']
cf=set(protocol['claim_fields']);pf={x.split(' (')[0] for x in protocol['progress_fields']}
assert set(claim)==cf
assert set(progress)==pf
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert all(p.stat().st_size<20*1024*1024 for p in R.rglob('*') if p.is_file())
save('out/SCHEMA_CHECK.json',{'status':'PASS','claim_keys':len(cf),'progress_keys':len(pf),'compatibility_equal':True,'report_sections':protocol['report_fields'],'full_fei':'OPEN'})
receipts=[{'path':str(p.relative_to(R)),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(R.rglob('*')) if p.is_file() and p.name!='RECEIPTS.json']
receipts += [{'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in [A/'STATUS.md',A/'WORKLOG.md',A/'LEARNED.md']]
save('out/RECEIPTS.json',receipts)
print(json.dumps({'status':'SAVED','run':run,'receipts':len(receipts),'claim_keys':len(cf),'progress_keys':len(pf)}))
