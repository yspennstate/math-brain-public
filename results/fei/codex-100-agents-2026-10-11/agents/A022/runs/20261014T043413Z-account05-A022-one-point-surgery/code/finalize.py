from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];BASE=RUN.parents[1];RID=RUN.name
ROOT=Path('~/brain_workers/FEI100_20261011')
PREV=RUN.parent/'20261014T014918Z-account05-A022-one-point-surgery'
claims=json.loads((PREV/'CLAIMS.json').read_text(encoding='utf-8'))
old=claims[0];own=dict(old)
statement=old['exact_statement']+' Growing-edit extension: For every k=2m>=4, paired quadratic bent b, q distinct data vertices v_j, and arbitrary indicators A_j on the same uniform controller cube independent of the data (with unrestricted controller dependence), set a_j=1-2A_j, delta=2^-k and F=b[1-2 sum_j point_(v_j) A_j]. If q<=2^(m-2), then I_ctrl(F)=delta sum_j I(a_j) and H(F)<=K(m,q)I_data(F)+delta sum_j H(a_j), where K=max(4+2log2(e),[4m+2log2(e)+4log2(e)/e]/[m-log2(q)]). If q^2<=2^(m-2), K<8, so H(F)<=8I_data(F)+delta sum_j H(a_j). Every paired access query has d>=1/4 and B<4d; every terminal bill uses actual post-cancellation data influence once. Signed root and terminal spectra and their exact entropy-row decompositions are given in current PROOF.md (4),(7); the root identities and adjacent E(A_j A_l) influence correction hold for every bent reference, while access requires quadratic pairs. Starting with constants/characters and repeatedly applying this guarded construction with fresh independent data blocks and previously constructed controllers gives H<=8I at all finite depths, even when controllers share existing bits. This is a scoped grammar; arbitrary Boolean admission and unguarded dense-edit payment remain open.'
hyp=old['hypotheses']+['Growing-edit result has k=2m>=4 paired quadratic bent data, distinct vertices, arbitrary possibly overlapping controllers independent of the data, and the explicitly stated q support guard.', 'Recursive closure uses fresh data blocks and previously certified controller signs; no arbitrary-function representation is asserted.']
own.update(version=4,exact_statement=statement,hypotheses=hyp,
    statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
    proof_source={'run_id':RID,'new_proof':'PROOF.md','inherited_proofs':[str(PREV/'PROOF.md'),str(PREV/'TWO_VERTEX_PROOF.md')], 'certificate':'out/full_RESULTS.json','cases':'out/full_CASES.json','edge_reconstruction':'out/EDGE_RESULTS.json'},
    proof_dependencies=[{'claim_id':old['claim_id'],'version':3,'scope':'inherited statements; new growing-edit bound is rederived', 'status':'author proved; new review pending'}, {'claim_id':old['claim_id'],'version':2,'scope':'source-complete C005 scalar JS proof, stage3 PROOF section3','status':'author proved; independent full review pending'}],
    status='AUTHOR_PROVED_GUARDED_GROWING_EDIT_AND_RECURSIVE_CLOSURE_PENDING_REVIEW',supersedes=[{'claim_id':old['claim_id'],'version':3}],first_unproved_line=None)
# Preserve inherited external partial review with its original source and scope.
claims[0]=own
(RUN/'CLAIMS.json').write_text(json.dumps(claims,indent=2)+'\n',encoding='utf-8')
pilot=json.loads((RUN/'out/pilot_RESULTS.json').read_text());full=json.loads((RUN/'out/full_RESULTS.json').read_text());edge=json.loads((RUN/'out/EDGE_RESULTS.json').read_text())
assert all(r['verdict']=='PASS' for r in (pilot,full,edge))
checks=sum(r['checks'] for r in (pilot,full,edge))
next_action='Replace the worst-case log(q) leaf loss by the actual conditional negative-set boundary/entropy profile; identify a paid dense-fiber condition that survives common-character cancellation while inheriting all controller entropies. A087 primary, A094 alternate independent reviewer.'
artifacts=['PROOF.md','code/check.py','code/edge.py','out/FROZEN_SPEC.json','out/EDGE_SPEC.json','out/pilot_RESULTS.json','out/full_RESULTS.json','out/full_CASES.json','out/full_LOG_RECEIPTS.json','out/EDGE_RESULTS.json']
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RID,'stream':'B05','packet_id':'A022','gap_id':'G-R-MISMATCH','attempt_id':'A022-stage5-growing-edit-owned-data-bank',
 'method':'exact signed multi-edit spectrum; one physical paired stopping tree; actual edge-isoperimetric terminal bank; depth-independent guarded recursive closure',
 'mathematical_delta':'Arbitrary possibly dependent q controllers admit H<=8I_data+2^-k sum H(a_j) under q^2<=2^(k/2-2), with all signed collisions and adjacent cancellations retained. This gives H<=8I for the corresponding finite recursive grammar at every depth.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_GROWING_EDIT_AND_RECURSIVE_CLOSURE_PROVED; UNIVERSAL_FEI_OPEN; INDEPENDENT_REVIEW_PENDING',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':3,'role':'inherited scoped assertions'},{'claim_id':old['claim_id'],'version':2,'role':'C005 scalar JS proof'}],
 'claims_created_or_changed':[{'claim_id':own['claim_id'],'version':4}], 'source_artifacts':artifacts,'next_consumers':own['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Dense fibers can lose the m-log2(q) data boundary reserve; arbitrary controller entropy stays inherited outside the certified grammar.','No independent acceptance of v4 or universal admission theorem.'],'packet_ids':['A022']}
for name in ('PROGRESS.json','PACKET_DELTA.json'):(RUN/name).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
report=f'''# A022 stage 5: growing edit sets and one terminal data bank

## exact target, quantifiers, hypotheses and units

Uniform Boolean signs, entropy in bits. For every paired quadratic bent sign
on k=2m>=4, q distinct data vertices, and arbitrary indicators A_j on the
same controller cube independent of the data, controllers may overlap or
depend arbitrarily. Write delta=2^-k, a_j=1-2A_j and
F=b[1-2 sum_j point_(v_j) A_j]. Proved under q^2<=2^(m-2):

    H(F)<=8 I_data(F)+delta sum_j H(a_j),
    I_ctrl(F)=delta sum_j I(a_j).

The more general q<=2^(m-2) bound has coefficient K(m,q) explicitly given
in PROOF.md (2). Constants/characters recursively composed by the absolute
guard obey H<=8I at all finite depths, with shared controller bits allowed.
This closes the guarded growing-edit mechanism, not full FEI.

## sources actually read, revisions and theorem locators

Execution protocol 2026-10-11-execution-v2 read in full; entry BOARD snapshot
2026-10-14 04:29 UTC read with targeted B05/B06 and relevant agent followups
(the large full-board output was truncated, so no all-agent audit is claimed).
B05 STREAM_NOTES v2 and own STATUS read at entry. Prior A022 v3 proof and
TWO_VERTEX_PROOF supplied the two-point frontier, and stage3 PROOF section3
supplies the complete scalar JS bound. A028 run 20261014T022306Z REPORT read
for selector overhead/unguarded terminal reserve; A023 run 20261014T022245Z
REPORT read for whole-block geometric payment and its one terminal bank.
Neither report is a theorem premise here. No new web, paper or brain premise.
The all-controller finite census was not repeated.

## complete derivation or exact first unsupported line

PROOF.md contains the complete general proof. Its (4) gives the actual signed
root coefficients, retaining all cross terms before squaring; (5) retains
the adjacent -4delta b(v_j)b(v_l)E(A_j A_l) edge correction. These root
identities hold for all bent references. The access theorem uses quadratic
pairs: query the first bit of each pair, then STOP. Perturbation union mass
gives d>=1/2-q*2^-m>=1/4, so all access is K4-good.

Each reached terminal is a character times a controlled defect set on m
partner bits. Equation(7) is its exact entropy decomposition: joint-empty,
controller-empty/partner-nonempty, and all nonempty controller rows, with
the actual conditional squared signed laws. No row is erased. Entropy is
bounded by tau sum H(a_j)+tau s(8m+4log2(e)+8log2(e)/e), tau=2^-m,
s=sum EA_j. At each controller input the actual negative set has r<=q
points, so edge isoperimetry gives actual data I>=2tau s(m-log2 q).
Under the guard, character multiplication only increases this influence.
The stronger q^2 guard makes the resulting ratio less than8.

Physical terminal reach tau multiplies the spectral inheritance weight tau,
giving delta for each controller exactly once. Influence partition and
the scalar JS<=2d/ln2 telescope finish the theorem. Induction gives the
recursive closure without any rate increase at greater depth. Controllers
sharing bits is allowed because their actual controller edges occur in
disjoint data fibers.

There is no unsupported line within the scoped statements. The first
unsupported universal line is admission of arbitrary Boolean functions to
this guarded recursive grammar, or a substitute paid reserve for dense edit
fibers. At q near2^m the isoperimetric slack degenerates, the common character
may reduce influence, and the access perturbation estimate may fail.
Arbitrary controller entropy remains explicitly inherited outside the grammar.

## executed validation with domain, arithmetic, commands and outputs

Specs frozen before each job: out/FROZEN_SPEC.json and out/EDGE_SPEC.json.
Pilot6 fixtures: k8/q2 adjacent, split-fiber, all-zero and all-one controller
profiles; k12/q3 and q4 shared-fiber profiles. Full12 adds k12/q4 partner
square with all-one/common-AND/all-zero controllers, k16/q8 partner cubes
with all-one/cycling profiles, and a split-first-fiber cube with cycling
profiles. All controllers use two bits: literals, XOR, AND or constants.
Maximum dimension18; no symmetry quotient or automatic escalation.

Executed from the A022 workspace using python -X utf8:

- code/check.py pilot: {pilot['cases']} roots, {pilot['checks']:,} checks,
  {pilot['runtime_seconds']:.6f}s, PASS (60s cap).
- code/check.py full: {full['cases']} roots, {full['checks']:,} checks,
  {full['nodes']} access nodes and {full['leaves']} terminal leaves,
  {full['runtime_seconds']:.6f}s, PASS (1800s cap).
- code/edge.py: {edge['cases']} roots, {edge['checks']} aggregate equalities,
  {edge['runtime_seconds']:.6f}s, PASS. Independently reconstructs actual
  Boolean signs in natural coordinates and directly counts every coordinate
  edge; no Walsh/logarithm helper is imported.

Total {checks:,} checks, including the repeated pilot. Full signed integer
Walsh coefficients are checked frequency by frequency against the exact
multi-edit formula. Influences are rational; entropy equalities use rational
prime-log forms, inequalities use outward80-bit atanh intervals with proved
50-term remainder. Every leaf's raw/character entropy, influence comparison,
empty mass and row marginals are checked. All actual access B<=4d and JS
inequalities, full entropy telescope and physical influence partition pass.
Multiplicities compress entropy sums without changing arithmetic. Exact
case expressions and prime-log interval receipts are in out/. Only runtime
clocks use floating point. Memory estimates180MB/60MB were below the300MB
trigger; peak memory was not measured. Jobs ran sequentially and stayed
within frozen limits. This is author verification, not independent acceptance.

## proof dependencies and changed downstream conclusions

Existing A022-ODDFACE-SURGERY-GAP-LEDGER advances v3 to v4. The prior scoped
claims and the A025 v1 partial review retain their original limits; no new
broad universal candidate is opened. The inherited A021 partial review is
preserved without claiming new review or acceptance of its bundled statement.
New dependence is the explicit scalar JS proof; terminal entropy, signed
interference, actual boundary payment and growth guard are derived here.
No FEI assumption is needed except when admitting externally certified
controller signs; within the recursive grammar that certification is induction.

B05/A023/A028 now have one terminal bank for growing numbers of unequal
controllers, retaining every delta H(a_j), rather than only two-point payment
or renewal of a shared reserve. General bent references have exact root
formulas but do not acquire a paired access policy from this result.
No shared registry was edited or message sent. Independent review is pending.

## one next mathematical action and independent reviewer

{next_action}
Review the phi(M) bound, actual post-cancellation isoperimetry, common-character
influence comparison, both tau factors, and recursive sharing of controller
bits. These are the places where an apparently universal version could lose
its reserve; additional small controller tables would not resolve that gap.

## actual persistence receipts or precise save blocker

Required four protocol files, PROOF.md, scripts and exact outputs saved in
this run. STATUS is two lines; WORKLOG and LEARNED updated. Local receipt
out/ARTIFACT_RECEIPTS.json records byte counts and SHA256, exact field sets,
canonical statement hashes and compatibility equality. No file exceeds20MB.
No save blocker. Supervisor copying, canonical adoption, remote mirrors and
independent acceptance remain unverified.

Universal bridge: This stage moves C019/B05 localized stopping payment from
two edits to arbitrary growing edit counts under q^2<=2^(k/2-2), with one
actual post-cancellation terminal data bank, zero K4 access credit and every
controller entropy inherited once. It also closes a depth-independent H<=8I
recursive grammar. Dense edit fibers and universal admission remain open.
NEXT targets the exact conditional negative-set boundary where this bank
fails, the shortest route toward full FEI because it tests extension of the
payment mechanism beyond the support guard rather than another isolated
finite class or a wider controller census.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(BASE/'STATUS.md').write_text(f'STATE: A022 stage5 complete: growing q edits under q^2<=2^(k/2-2) have H<=8I_data+delta sum H(controllers); recursive guarded grammar H<=8I at every depth; {checks} exact checks PASS; independent review pending; full FEI OPEN.\nNEXT: A087/A094 review; replace worst-case log(q) by actual conditional negative-set boundary/entropy to test a paid dense-fiber extension with complete inherited controller entropy.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (BASE/'WORKLOG.md').open('a',encoding='utf-8') as fp:
    fp.write(f'\n2026-10-14 04:34 UTC stage, saved {stamp}: Read board/B05 notes and consumed A023/A028 terminal-reserve frontiers. Extended two-point surgery to growing q possibly dependent controllers; exact signed root/leaf masses and adjacent E(A_j A_l) corrections retained. Proved general K(m,q), absolute rate8 under q^2<=2^(m-2), one physical/spectral delta bank per controller, and guarded recursive FEI<=8 at every finite depth. Frozen six-root pilot and twelve-root full set through n18 plus separate natural-coordinate edge implementation PASS ({checks} checks). Dense fibers and arbitrary admission remain open. Existing claim v4, no new universal candidate or external edits.\n')
with (BASE/'LEARNED.md').open('a',encoding='utf-8') as fp:
    fp.write('\nStage5 growing edit theorem: k=2m>=4 paired quadratic bent, q distinct vertices, arbitrary possibly dependent A_j independent of data. General q<=2^(m-2): H<=K I_data+2^-k sum H(1-2A_j), K=max(4+2c,[4m+2c+4c/e]/[m-log2 q]), c=log2(e). Strong guard q^2<=2^(m-2) gives K<8. Leaves have s=sum EA_j,u=sum(EA_j)^2, joint-empty mass(1-2tau s)^2, controller-empty nonempty mass4tau u-4tau^2 s^2, nonempty T row mass4tau sum Ahat_j(T)^2. Actual conditional laws retain signed interference. H_leaf<=tau sum H(a_j)+tau s(8m+4c+8c/e); actual post-cancellation isoperimetric I>=2tau s(m-log2 q). Under guard common-character influence increases. Physical reach tau times spectral tau equals delta, no bank renewal. Fresh-data recursive constructions with previously certified shared-bit controllers satisfy H<=8I at every finite depth. Dense q~2^m can lose boundary slack and character/access monotonicity; no arbitrary admission proved. Multiplicity-compressed rational prime-log sums cut validation runtime substantially without replacing exact arithmetic.\n')
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
assert set(progress)=={x if not x.startswith('packet_ids ') else 'packet_ids' for x in protocol['required_per_run']['progress_fields']}
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
for c in claims:
    assert c['statement_sha256']==hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
sources=[ROOT/'BOARD.md',ROOT/'claude/B05/STREAM_NOTES.md',PREV/'PROOF.md',PREV/'TWO_VERTEX_PROOF.md',PREV/'CLAIMS.json',ROOT/'agents/A028/runs/20261014T022306Z-account05-A028-stopping-tree-payment/REPORT.md',ROOT/'agents/A023/runs/20261014T022245Z-account05-A023-amortized-rarity-budget/REPORT.md']
(RUN/'out/SOURCE_INVENTORY.json').write_text(json.dumps([{'path':str(p),'sha256_at_finalize':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources],indent=2)+'\n',encoding='utf-8')
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        data=p.read_bytes();assert len(data)<20*1024*1024
        receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(RUN/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps({'schema':'PASS','compatibility_copy':'IDENTICAL','statement_hashes':'PASS','total_checks':checks,'artifacts':receipts,'mirror':'UNVERIFIED'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'run':RID,'checks':checks,'artifacts':len(receipts),'schema':'PASS'}))
