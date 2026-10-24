from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];BASE=RUN.parents[1];RID=RUN.name
ROOT=Path('~/brain_workers/FEI100_20261011')
PREV=RUN.parent/'20261014T043413Z-account05-A022-one-point-surgery'
claims=json.loads((PREV/'CLAIMS.json').read_text(encoding='utf-8'));old=claims[0];own=dict(old)
addition=' Root-density extension: On k data bits with ANY Boolean seed b, distinct per-vertex indicators A_j on a shared controller cube independent of data, a_j=1-2A_j, delta=2^-k, p=delta sum EA_j, V=delta sum[1-(Ea_j)^2], and L=delta sum H(a_j), the exact controller spectral marginal is R=(1-qdelta) point_empty+delta sum_j ahat_j^2. The complete signed root entropy obeys H(F)<=L+k(1+V)+phi(1-V)-delta sum phi((Ea_j)^2), and its exact excess is the nonempty-row label mixing refund plus sum_T R_T[k-H(nu_T)], with actual signed conditional data laws nu_T. Exactly I_ctrl=delta sum I(a_j); I_data>=I(b)-2kp and V<=4p(1-p)<=4p. Thus if k>=4, I(b)>=k/2 and actual expected flip density p<=1/8, then H(F)<=7I_data+L, with NO cardinality or quadratic-pair guard: every vertex can carry a dependent controller. This includes all bent references and supplied high-influence non-flat tensor/parity seeds. If nominal q/2^k<=1/8 or<=1/16, the respective data rates5 and3 suffice. Starting with constants/characters and iterating fresh-data high-influence seeds and previously certified shared-bit controllers under p<=1/8 gives H<=7I at every finite depth. This is a whole-root capacity payment; it does not assert K4-good access, paid prescribed mixed histories, or a renewed leaf bank. Arbitrary target admission and low-influence-seed payment without ambient k/I(b) loss remain open.'
statement=old['exact_statement']+addition
hyp=old['hypotheses']+['Root-density theorem: independent uniform data/controller cubes, distinct edited data vertices, arbitrary Boolean seed; high-influence absolute rates additionally require k>=4, I(seed)>=k/2, and actual p<=1/8.', 'The root data budget is used once with all controller spectra retained; recursive closure admits only previously certified controllers on fresh data blocks.']
own.update(version=5,exact_statement=statement,hypotheses=hyp,
 statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
 proof_source={'run_id':RID,'new_proof':'PROOF.md','inherited_proof':str(PREV/'PROOF.md'),'certificate':'out/full_RESULTS.json','exact_cases':'out/full_CASES.json','separate_edges_and_frontier':'out/EDGE_FRONTIER_RESULTS.json'},
 proof_dependencies=[{'claim_id':old['claim_id'],'version':4,'scope':'inherited statements only; new root-density proof is self-contained','status':'author proved; independent full review pending'}],
 status='AUTHOR_PROVED_ROOT_DENSITY_HIGH_INFLUENCE_EXTENSION_PENDING_INDEPENDENT_REVIEW',
 supersedes=[{'claim_id':old['claim_id'],'version':4}],first_unproved_line=None)
claims[0]=own
(RUN/'CLAIMS.json').write_text(json.dumps(claims,indent=2)+'\n',encoding='utf-8')
pilot=json.loads((RUN/'out/pilot_RESULTS.json').read_text());full=json.loads((RUN/'out/full_RESULTS.json').read_text());edge=json.loads((RUN/'out/EDGE_FRONTIER_RESULTS.json').read_text())
assert all(r['verdict']=='PASS' for r in (pilot,full,edge));checks=sum(r['checks'] for r in (pilot,full,edge))
next_action='Replace ambient k by a complete supplied seed-data spectral reference in (4), and price the signed conditional-data capacity loss from one unused actual seed/child bank after a weak non-flat query; retain exact row mixing refund and all L. A087/A094 review first, A021/A029 consume the source-bound root identity.'
artifacts=['PROOF.md','code/check.py','code/edge.py','out/FROZEN_SPEC.json','out/RECONSTRUCTION_SPEC.json','out/pilot_RESULTS.json','out/full_RESULTS.json','out/full_CASES.json','out/full_LOG_RECEIPTS.json','out/EDGE_FRONTIER_RESULTS.json']
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RID,'stream':'B05','packet_id':'A022','gap_id':'G-R-MISMATCH','attempt_id':'A022-stage6-root-density-no-pair-support-guard',
 'method':'change terminal-only mechanism to exact joint root controller marginal and one actual high-influence seed data budget; signed row mixing refund retained',
 'mathematical_delta':'Removes growing-edit cardinality and quadratic pairing requirements: for any k>=4 seed with I(seed)>=k/2 and expected flip density<=1/8, H<=7I_data+2^-k sum H(a_j), even full-support edits and dependent controllers. All-bent/high-influence recursive grammar has depth-independent rate7. Exact arbitrary-seed row mixture and refund formulas proved.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_ROOT_DENSITY_EXTENSION_PROVED; LOW_INFLUENCE_AND_UNIVERSAL_HISTORY_FEI_OPEN; NEW_REVIEW_PENDING',
 'claim_versions_used':[{'claim_id':old['claim_id'],'version':4,'role':'inherited assertions only; new derivation has no external theorem premise'}],
 'claims_created_or_changed':[{'claim_id':own['claim_id'],'version':5}], 'source_artifacts':artifacts,'next_consumers':own['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Ambient k capacity loses k/I(seed) for low-influence seeds; arbitrary target admission is unproved.','No prescribed later mixed-history payment or independent acceptance of v5.'],'packet_ids':['A022']}
for name in ('PROGRESS.json','PACKET_DELTA.json'):(RUN/name).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
report=f'''# A022 stage 6: root density payment beyond the sparse terminal guard

## exact target, quantifiers, hypotheses and units

Uniform Boolean signs, entropy in bits. For every k>=4 seed b with
I(b)>=k/2, arbitrary distinct data vertices, and arbitrary possibly dependent
indicators A_j on the same uniform controller cube independent of data,
write F=b[1-2 sum point_(v_j) A_j], delta=2^-k, a_j=1-2A_j.
If the actual expected flip density p=delta sum EA_j<=1/8, proved:

    H(F)<=7 I_data(F)+delta sum H(a_j),
    I_ctrl(F)=delta sum I(a_j).

Every vertex can be edited: there is no q guard or paired-quadratic requirement.
All bent signs satisfy the seed capacity condition, as do the declared
non-flat tensor/parity seeds. Fresh-data recursive admission with previously
certified controllers gives H<=7I at every finite depth. Supplied external
controller rate C gives max(7,C). Nominal density q/2^k<=1/8 or1/16 gives
rates5 or3 respectively. Full FEI and arbitrary mixed-history admission OPEN.

## sources actually read, revisions and theorem locators

Protocol 2026-10-11-execution-v2 read in full. Entry BOARD snapshot10:24UTC,
B05 STREAM_NOTES v2 and own STATUS read; the large board output was truncated,
then B05/B06 and relevant A021/A023/A024/A025/A028/A029/A040/A046 entries
were read by targeted search. No all-agent audit is claimed. Prior A022
PROOF.md read for the actual terminal-bank failure. New A021 run
20261014T075029Z REPORT read for ANY-seed two-edit row-profile refund and
its still-unpaid second mixed query. New A029 run20261014T055200Z REPORT
read for finite-label conserved-bank identity and the release-only guard.
These reports guide gap selection but are not accepted theorem premises.
No new web, paper or brain premise. No old exhaustive controller grid repeated.

## complete derivation or exact first unsupported line

PROOF.md is self-contained. Exact signed coefficients retain all geometric
cross terms. Distinct-vertex orthogonality gives the controller-label marginal
R=(1-qdelta)point_empty+delta sum P_j, P_j=ahat_j^2, for ANY seed. Nonempty
row mass is R_T=delta sum ahat_j(T)^2; V=sum_(T!=empty)R_T.
The complete entropy law is H(R)+sum_T R_T H(nu_T), with actual signed
conditional data spectra, including the controller-empty row.

Log-sum gives the exact paid upper bill

    L+k(1+V)+phi(1-V)-delta sum phi((Ea_j)^2),
    L=delta sum H(a_j).

Its exact excess is D_mix+sum_T R_T[k-H(nu_T)], where
D_mix=sum_(T!=empty)R_T H(J|T)>=0. All label mixing and empty-row terms
are shown, and every inherited controller entropy has coefficient delta.
Conditional data entropy uses at most k bits ONCE at the whole root.

Actual data edges change only when an endpoint is flipped, giving
I_data>=I(b)-2kp. PROOF(12) supplies the exact adjacent E(A_j A_l)
cancellation. V<=4p and phi(1-V)<=log2(e)V give H<=L+k(1+4p)+4p log2(e).
With I(b)>=k/2, k>=4 and p<=1/8, that data bill is at most27/4 I_data<7I_data.
The controller identity is coordinatewise exact because edited data fibers
are disjoint. No seed entropy theorem or controller independence is assumed.

This changes the mechanism: dense terminals are not each charged to their
raw boundary. A frozen witness at k6 with first pair bits(1,0,0) flips the
four partner points having first partner bit1. Raw terminal influence1
becomes actual influence0 under the common character. Its root p=1/16
is still admitted and paid by the new whole-root data budget. Thus the
old terminal influence comparison cannot simply lose its support guard.

First unsupported universal line: arbitrary targets admit a high-influence
seed within expected density1/8 with certified controllers, or a low-
influence seed pays the ambient k capacity without k/I(seed) loss. A k8
padded character with no edits has I=1, H=0, but the ambient8 bill exceeds
the rate7 capacity. This refutes that certificate extension, not FEI.
Neither exact row mixture nor bank conservation permits a reset or renewed
payment after an already-booked physical query.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json before pilot/full; RECONSTRUCTION_SPEC.json before separate
edge replay and frontier diagnostics. Fourteen full fixtures: pilot6 contains
k4 bent full16 support with shared-point, cycling-point and half-zero/
half-shared-point controllers on three bits, plus adjacent two-point literal
edits of bent, bent-times-character and parity seeds. Full adds k6 full64
shared/cycling point supports and eight literal edits, k8 full256 supports
with shared/cycling controls for bent, and cycling controls for tensor and
parity seeds, plus a full16 zero-controller baseline. Fixed labelled fixtures,
no symmetry quotient, no all-function claim. Max dimension11. Every seed
has I>=k/2 and every actual p<=1/8; support-full cases violate the old q guard.

Commands use python -X utf8 from the own workspace:

- code/check.py pilot: {pilot['cases']} fixtures, {pilot['checks']} checks,
  {pilot['runtime_seconds']:.6f}s, PASS, frozen60s cap.
- code/check.py full: {full['cases']} fixtures, {full['checks']} checks,
  {full['runtime_seconds']:.6f}s, PASS, frozen1800s cap.
- code/edge.py:14 roots plus2 diagnostics, {edge['checks']} checks,
  {edge['runtime_seconds']:.6f}s, PASS, frozen60s cap.

Total {checks} checks including pilot. Integer signed Walsh verified against
the actual formula at every frequency; rational prime-log identities verify
the exact mixture/refund and whole entropy bill. Every row marginal, exact
adjacent correction, controller influence and density inequality checked.
Rate7 and eligible rates5/3 are outward interval-certified, not floating signs.
Log helper is the pinned own stage2 positive50-term atanh expansion with
proved tail and80-bit outward intervals. Exact expressions/receipts saved.
Separate natural-coordinate Boolean edge enumeration imports no Walsh/log
helper and verifies all root data/controller influences and actual flip
densities, plus the dense-terminal cancellation and low-seed capacity guard.
This is author verification, not independent human review.

Memory estimates110MB and30MB were below300MB; peak memory unmeasured.
Sequential jobs respected caps; no automatic dimension increase or background
process. No mathematical or implementation assertion failed this stage.
Analytic proof, rather than finite extrapolation, establishes all-dimensional
and all-controller claims.

## proof dependencies and changed downstream conclusions

Existing A022-ODDFACE-SURGERY-GAP-LEDGER advances v4 to v5; inherited statements
retain their original scope and the new root proof is self-contained.
No new broad universal candidate is opened. Inherited A025 partial review
and A021 partial review retain their original sources/scopes; no new whole-
bundle acceptance or review of v5 is asserted. A021/A029 source reports
are context only and no circular bank assumption is used.

B05/A021/A023/A028/A029 can use an exact complete controller marginal and
root-data reserve beyond sparse paired leaves, including arbitrary bent
references and dependent dense controllers. The new result pays growing
support at an absolute rate7 whenever actual activation is sparse and the
seed has high data influence. It does not certify a prescribed continuation
with inherited debits, bank release-only payment or arbitrary low-influence
cores. Exact mixing refunds are exposed for such a continuation to use.
No shared registry, other folder or external message was touched.

## one next mathematical action and independent reviewer

{next_action}
Review should check the nonempty-row log-sum refund, actual controller-label
marginal versus physical resets, endpoint-union data influence bound, full
empty-row terms and recursive sharing. NEXT targets the ambient dimension
loss at the actual universal bottleneck, rather than more already-admitted
dense supports or controller truth-table grids.

## actual persistence receipts or precise save blocker

Four protocol files, complete proof, frozen specs, scripts and exact outputs
saved locally. STATUS has two lines; WORKLOG and LEARNED updated. Local
ARTIFACT_RECEIPTS.json verifies schema field sets, statement hashes, identical
PROGRESS/PACKET_DELTA, artifact bytes/SHA256 and20MB limit. No save blocker.
Supervisor copying, external mirrors, independent acceptance and downstream
adoption unverified.

Universal bridge: This stage moves C019/B05 payment beyond the growing-edit
support guard by replacing per-leaf raw boundary charges with one whole-root
data budget. Exact disjoint-fiber controller marginal and signed mixing
refund give H<=7I_data+delta sum H(a_j) for all high-influence seeds at actual
flip density<=1/8, including full support and nonquadratic bent seeds, and
depth-independent recursive rate7. Dense terminal cancellation is exhibited
exactly. Low-influence ambient-dimension loss, arbitrary admission and booked
mixed-history continuation remain. NEXT replaces that ambient data budget
by the same supplied complete seed reference and unused physical surplus,
the shortest route toward full FEI because it confronts the universal
capacity loss instead of extending an already-paid isolated class.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(BASE/'STATUS.md').write_text(f'STATE: A022 stage6 complete: any k>=4 seed I>=k/2, arbitrary dependent full-support edits with expected density<=1/8 have H<=7I_data+delta sum H(controllers); exact root mixture/refund; recursive rate7; {checks} checks PASS; review pending; FEI OPEN.\nNEXT: A087/A094 review; replace ambient k by a complete supplied seed reference and pay its signed conditional-data loss from one unused physical bank, retaining full controller L and booked-history debts.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (BASE/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n2026-10-14 10:30 UTC stage, saved {stamp}: Read new board/B05 notes and A021 ANY-seed/A029 conserved-bank reports. Changed from dense terminal-only boundary payment to exact root controller-label mixture R=(1-qdelta)point_empty+delta sum P_j. Derived complete log-sum refund and one ambient-data capacity bill, paid by actual high seed influence: any k>=4 I(seed)>=k/2, expected flips p<=1/8 gives H<=7I_data+delta sum H(a_j), arbitrary nominal q including full support and nonquadratic seeds. Recursive fresh-data grammar rate7; nominal-density refinements5/3. Frozen14 fixtures plus separate edge replay and2 exact frontier diagnostics PASS, {checks} checks. Dense-leaf influence monotonicity fails explicitly but new root theorem covers it. Low-influence ambient k loss is the honest universal gap; no bank renewal or paid later mixed history claimed. Existing claim v5, independent review pending.\n')
with (BASE/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage6 root density: arbitrary Boolean seed b, distinct data vertex flips with dependent indicators on independent controls. Exact controller spectral marginal R=(1-qdelta)point_empty+delta sum ahat_j^2, V=delta sum(1-mean(a_j)^2), p=delta sum EA_j. Full H<=L+k(1+V)+phi(1-V)-delta sum phi(mean(a_j)^2), L=delta sum H(a_j); exact excess is nonempty label-mixing refund plus sum R_T[k-H(nu_T)]. Actual I_data>=I(b)-2kp, V<=4p(1-p), I_ctrl=delta sum I(a_j). For k>=4 I(b)>=k/2,p<=1/8, H<=7I_data+L with no cardinality or paired quadratic guard; all bent and high-I tensor/parity seeds admitted. Nominal qdelta<=1/8 gives5 and<=1/16 gives3. Fresh-data recursive certified-controller grammar H<=7I at all depths. Dense k6 fixed-first(1,0,0) fiber flips four points with first partner1: raw terminal I1 becomes actual0, global p1/16; cannot remove old character/boundary guard but new root capacity pays. Low-I padded character k8,p0 has ambient bill8>7I despite actual H0; no FEI refutation, only certificate loss. Exact spectral mixture is not a conditional physical reset and does not license reusing a booked seed bank.\n')
protocol_path=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json');protocol=json.loads(protocol_path.read_text())
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in claims)
assert set(progress)=={x if not x.startswith('packet_ids ') else 'packet_ids' for x in protocol['required_per_run']['progress_fields']}
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
for c in claims:
    assert c['statement_sha256']==hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
sources=[protocol_path,ROOT/'BOARD.md',ROOT/'claude/B05/STREAM_NOTES.md',PREV/'PROOF.md',PREV/'CLAIMS.json',ROOT/'agents/A021/runs/20261014T075029Z-account05-A021-rare-core-asymptotics/REPORT.md',ROOT/'agents/A029/runs/20261014T055200Z-account05-A029-child-deficit-transport/REPORT.md']
(RUN/'out/SOURCE_INVENTORY.json').write_text(json.dumps([{'path':str(p),'sha256_at_finalize':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources],indent=2)+'\n',encoding='utf-8')
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        data=p.read_bytes();assert len(data)<20*1024*1024
        receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(RUN/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps({'schema':'PASS','compatibility_copy':'IDENTICAL','statement_hashes':'PASS','total_checks':checks,'artifacts':receipts,'mirror':'UNVERIFIED'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'run':RID,'checks':checks,'artifacts':len(receipts),'schema':'PASS'}))
