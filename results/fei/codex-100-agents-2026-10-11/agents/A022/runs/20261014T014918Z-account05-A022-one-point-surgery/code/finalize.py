from pathlib import Path
import json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1];BASE=RUN.parents[1];RID=RUN.name
PREV=RUN.parent/'20261013T220954Z-account05-A022-one-point-surgery'
ROOT=Path('~/brain_workers/FEI100_20261011')
old=json.loads((PREV/'CLAIMS.json').read_text(encoding='utf-8'))[0]
source_run=ROOT/'agents/A021/runs/20261014T011316Z-account05-A021-rare-core-asymptotics'
source=json.loads((source_run/'CLAIMS.json').read_text(encoding='utf-8'))[0]
pilot=json.loads((RUN/'out/pilot_RESULTS.json').read_text())
full=json.loads((RUN/'out/full_RESULTS.json').read_text())
edge=json.loads((RUN/'out/EDGE_RECONSTRUCTION.json').read_text())
witness=json.loads((RUN/'out/CONTRAST_OVERLAP_WITNESSES.json').read_text())
two=json.loads((RUN/'out/TWO_VERTEX_RESULTS.json').read_text())
assert all(x['verdict']=='PASS' for x in (pilot,full,edge,witness,two))
assert full['cases']==6672 and pilot['cases']==352 and edge['cases']==6672 and witness['cases']==7
assert two['cases']==8
checks=sum(x['checks']+x['support_checks']+x['kernel_checks'] for x in (pilot,full))+edge['checks']+witness['checks']+two['checks']
new_statement=' Additional one-point controller theorem: Let k=2m>=4, b be the paired quadratic bent sign, v any data vertex, A any indicator on any number of fresh uniform controller bits, a=1-2A, alpha=EA, delta=2^-k, and F=b(x)(1-2*1_(x=v)*A(z)). Query only the first coordinate in each bent pair and STOP with all partners/controllers retained. Every access node has d>=1/2-2^-m>=1/4 and B/d<=8-3log2(3)<4; no inactive-branch fairness or bounded-contrast hypothesis is required. Exactly I_ctrl(F)=delta I(a) and H(F)<=7 I_data(F)+delta H(a), so H(a)<=C I(a) implies H(F)<=max(7,C)I(F). The exceptional leaf has reach tau=2^-m and, before its common character shift, is q=1-2*1_(t=w)*A(z); its complete entropy is phi((1-2tau alpha)^2)+(2^m-1)phi(4tau^2 alpha^2)+tau[H(a)-phi((1-2alpha)^2)]+8tau alpha(1-alpha)m. The character shift increases its raw data influence 2m tau alpha and preserves controller influence. All controller entropy is retained with final coefficient delta; only the actual terminal data reserve pays its spreading and alpha log alpha terms. For every bent reference (including nonquadratic), the signed root spectrum is bhat(S)*1_(T=empty)-2delta b(v)chi_S(v)Ahat(T), and its complete entropy is N_plus phi((beta-2delta alpha)^2)+N_minus phi((beta+2delta alpha)^2)+delta[H(a)-phi((1-2alpha)^2)]+8delta alpha(1-alpha)k, beta=2^(-k/2),N_plus/minus=(2^k plus/minus 2^(k/2))/2,phi(u)=u log2(1/u),phi(0)=0. The all-bent root identity does not extend the stopping policy beyond paired quadratic references. Arbitrary-controller FEI, multi-vertex unequal controller terminal payment, and constant-leaf zero-credit completion remain open.'
new_statement+=' Additional two-vertex theorem: For every paired quadratic bent k=2m>=6, distinct data vertices v,w, and arbitrary indicators A,B on the same uniform independent-of-data controller cube (with any dependence between A and B), F=b[1-2*1_(x=v)*A-2*1_(x=w)*B] has K4-good paired data access, I_ctrl=delta[I(1-2A)+I(1-2B)], and H(F)<=9I_data+delta[H(1-2A)+H(1-2B)]. The exact signed root cross terms are retained. Adjacent data edges contribute -4delta b(v)b(w)E(AB) to their data direction, and the leaf data bank uses the actual post-cancellation influence. No inherited controller entropy is omitted or paid twice. Growing edit sets without a data-support guard remain open.'
new_statement=new_statement.replace('Arbitrary-controller FEI, multi-vertex unequal controller terminal payment, and constant-leaf zero-credit completion remain open.','Arbitrary-controller FEI and constant-leaf completion remain open; unequal two-point controllers are handled by the subsequent theorem.')
statement=old['exact_statement'].replace('No extension to arbitrary cores, overlapping controls or zero-cost constant-leaf completion is asserted.','That fair-selector theorem has its original restricted scope; it does not certify arbitrary data cores or constant-leaf completion.')+new_statement
hyp=['Inherited v1/v2 statements keep their own original fair-selector, fresh-control, pattern and dimension hypotheses.']+old['hypotheses'][1:]+[
    'Additional one-point theorem: paired quadratic bent data k>=4 even; one fixed data vertex; arbitrary indicator controller independent of all data bits; no controller balance or point-block assumption',
    'All-bent root spectrum/entropy identity needs only a flat Boolean Fourier spectrum; the stopping theorem needs explicit quadratic pairs',
    'All access and terminal accounts use one physical stopping tree; the complete delta H(controller sign) bill is retained',
    'Two-vertex extension has paired quadratic k>=6, distinct vertices and arbitrary possibly dependent controllers; exact adjacent-edge cancellation retained']
own=dict(old)
own.update(version=3,exact_statement=statement,hypotheses=hyp,
    statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hyp},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
    proof_source={'run_id':RID,'new_proof':'PROOF.md','two_vertex_proof':'TWO_VERTEX_PROOF.md','inherited_proof':str(PREV/'PROOF.md'),
        'finite_certificate':'out/full_RESULTS.json','cases':'out/full_CASES.jsonl','edge_reconstruction':'out/EDGE_RECONSTRUCTION.json','contrast_overlap_witnesses':'out/CONTRAST_OVERLAP_WITNESSES.json'},
    proof_dependencies=[{'claim_id':old['claim_id'],'version':2,'scope':'inherited assertions and C005 scalar proof; paired access and new terminal entropy are rederived here','status':'author proved; full independent review pending'}],
    supersedes=[{'claim_id':old['claim_id'],'version':2}],
    status='AUTHOR_PROVED_SCOPED_CONTROLLER_EXTENSION_PENDING_INDEPENDENT_REVIEW',first_unproved_line=None,
    next_consumers=['A021','A023','A025','A027','A028','A029','A064','A087','A094','B05'])
review=dict(source)
review['review_records']=source['review_records']+[{'reviewer':'A022','verdict':'HOLDS_UPPER_POINT_SWITCH_PRICE_AND_K6_K7_CONSEQUENCES_ONLY',
    'source':str(RUN/'REVIEW_A021.md'),'scope':'DERIVATION.md sections1-2 only; no acceptance of whole bundled claim or its lower supremum/application',
    'repair_contribution':False}]
review['status']='PARTIAL_INDEPENDENT_REVIEW_FULL_BUNDLE_PENDING'
(RUN/'CLAIMS.json').write_text(json.dumps([own,review],indent=2)+'\n',encoding='utf-8')
next_action='Extend the exact signed exceptional-fiber spectrum to growing edit sets; determine a data-dimension/support-size guard under which one actual terminal data bank pays all collisions at an absolute rate, retaining every controller entropy. A087 primary, A094 alternate review.'
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RID,'stream':'B05','packet_id':'A022','gap_id':'G-R-MISMATCH',
    'attempt_id':'A022-stage4-arbitrary-controller-one-point-owned-data-reserve',
    'method':'consume bounded-contrast closure; independent scoped A021 price review; large-contrast data-first access with exact all-bent spectrum and complete inherited-controller entropy',
    'mathematical_delta':'Removes fair-selector/bounded-contrast requirement for one-/two-point quadratic-bent surgery: arbitrary dependent controllers have zero K4 access charge; H<=7I_data+delta H(a) for one point and H<=9I_data+delta[H(a)+H(c)] for two. Exact root/leaf log terms and adjacent E(AB) cancellation retained.',
    'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS','mathematical_status':'SCOPED_EXTENSION_PROVED; ARBITRARY_CONTROLLER_FEI_AND_UNIVERSAL_C019_OPEN; NEW_REVIEW_PENDING',
    'claim_versions_used':[{'claim_id':old['claim_id'],'version':2,'role':'inherited scoped ledger and scalar JS proof'},
        {'claim_id':source['claim_id'],'version':1,'role':'source-bound upper-price partial review and gap selection; not a new theorem premise'}],
    'claims_created_or_changed':[{'claim_id':own['claim_id'],'version':3},{'claim_id':source['claim_id'],'version':1,'change':'scoped independent review only; source statement unchanged'}],
    'source_artifacts':['PROOF.md','TWO_VERTEX_PROOF.md','REVIEW_A021.md','out/FROZEN_SPEC.json','out/pilot_RESULTS.json','out/full_RESULTS.json','out/full_CASES.jsonl','out/full_LOG_RECEIPTS.json','out/RECONSTRUCTION_SPEC.json','out/EDGE_RECONSTRUCTION.json','out/WITNESS_SPEC.json','out/CONTRAST_OVERLAP_WITNESSES.json','out/TWO_VERTEX_SPEC.json','out/TWO_VERTEX_RESULTS.json'],
    'next_consumers':own['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
    'blockers':['No arbitrary-controller entropy certificate; growing numbers of edited vertices may exhaust terminal data reserve. No independent human review of new A022 v3 yet.'],
    'packet_ids':['A022']}
for name in ('PROGRESS.json','PACKET_DELTA.json'):(RUN/name).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
report=f'''# A022 stage 4: one-point switches with arbitrary overlapping controllers

## exact target, quantifiers, hypotheses and units

Uniform Boolean signs, entropy in bits. For every paired quadratic bent sign
b on even k>=4, every vertex v, and every indicator A on any number of
independent uniform controller bits, F=b(1-2*1_(x=v)*A). No balance,
point-block width, overlap or contrast restriction on A. Establish exact
spectral logarithmic terms and one-use data access/terminal ownership.
New scoped target is proved: I_ctrl=2^-k I(1-2A) and
H(F)<=7I_data+2^-k H(1-2A). The arbitrary controller terminal is explicitly
inherited. TWO_VERTEX_PROOF.md also proves H<=9I_data+delta[H(1-2A)+H(1-2B)]
for two distinct vertices and arbitrary dependent controllers, k>=6.
Full FEI and universal stopping payment remain OPEN.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json read in full (2026-10-11-execution-v2); BOARD.md
snapshot 2026-10-14 01:41 UTC, B05 STREAM_NOTES v2 and own STATUS were
read at entry. Own prior v2 CLAIMS and PROOF.md provide the earlier paired
policy and complete scalar JS proof. A023 run 20261013T223305Z REPORT.md
was read for its single consumed separator reserve and terminal scope.
A021 run 20261014T011316Z REPORT.md, CLAIMS.json and DERIVATION.md §§1-2
and the start of §3 were read for bounded-contrast closure and the remaining
large-contrast cost. REVIEW_A021.md independently accepts only the upper
price/K6/K7 subclaims; its lower supremum and three-event application are
not accepted as a whole bundle. Source inventory hashes are locally saved.
No new paper, percolation or brain premise; old four-order census and A021's
bounded-contrast controller grid were not repeated.

## complete derivation or exact first unsupported line

PROOF.md §§1-4 is the complete scoped proof. It gives the actual signed root
coefficients bhat(S)1_(T=empty)-2delta b(v)chi_S(v)Ahat(T). All nonempty
controller rows are flat across data labels and contribute exactly
delta[H(1-2A)-phi((1-2alpha)^2)]+8delta alpha(1-alpha)k.
The controller-empty row has the two exact bent alignment masses. These
root formulas also hold for every bent sign, while the access proof uses
explicit quadratic pairing.

Query only the first bit in each pair, then STOP. Reference derivative is
1/2; a surviving point perturbation changes it by at most
2alpha*2^(-(k-q)), so d>=1/2-2^(-k/2)>=1/4 without any fair inactive branch.
Thus every access node is K4-good. One exceptional fiber retains q=1-2*point*A
up to a character. Equation(3) gives its full entropy, including empty rows.
Its alpha-log-alpha and data-spreading terms are bounded by7 times raw
partner influence; the character can only increase that data influence.
No controller influence pays this local term. The exceptional leaf's reach
and its spectral inheritance weight are BOTH tau=2^(-k/2), so the final
controller entropy bill is delta H(1-2A), not tau H(1-2A).

Exactly I_data=I_access+I_terminal,data and I_ctrl=delta I(1-2A) is entirely
terminal. JS is bounded by2d/ln2 using the explicit prior scalar proof.
Since 4+2/ln2<7, telescope gives the displayed one-use bound. If the
controller sign satisfies H<=C I, the full root bound is max(7,C)I.
This is a conditional inheritance statement, not an arbitrary-controller
certificate or a zero-credit completion to constant leaves.

TWO_VERTEX_PROOF.md closes the first unequal-reference collision: exact signed
interference and the adjacent -4delta b(v)b(w)E(AB) data-edge correction
are retained. The common exceptional leaf has actual post-cancellation
data influence >=2tau(m-1)(EA+EB), and its complete entropy is at most
tau[H(1-2A)+H(1-2B)]+9I_leaf,data. Every controller bill inherits once.

First unsupported universal line: arbitrary controller entropy is paid
without a terminal certificate, or growing numbers of edited vertices
admit a uniform terminal data-reserve bound without a support-size guard.
No such implication is made. The one-point large-contrast log is now paid
by a named actual data reserve, not by renewing whole child influence.

## executed validation with domain, arithmetic, commands and outputs

Specs were frozen before each search: FROZEN_SPEC.json,
RECONSTRUCTION_SPEC.json, WITNESS_SPEC.json and TWO_VERTEX_SPEC.json. Main pilot: k=4 all16
vertices, every controller on t=0,1,2 (22 tables):352 roots. Full: every
controller on t=0..3 (278 tables), k=4 all16 vertices, k=6 vertices
0,1,21,63 and k=8 vertices0,1,85,255:6672 labelled roots. No symmetry
quotient. Main maximum dimension is11. Seven separate witnesses include
controller-first point switches k=4,6,8 and two explicit OR/XOR three-event
overlapping four-bit controllers on k=4,8, maximum dimension12.

Executed commands from own A022 folder, each using python -X utf8:

- code/check.py pilot: {pilot['checks']+pilot['support_checks']+pilot['kernel_checks']:,} checks,
  {pilot['runtime_seconds']:.6f}s, PASS.
- code/check.py full: {full['checks']+full['support_checks']+full['kernel_checks']:,} checks,
  {full['runtime_seconds']:.6f}s, PASS. Exact root/leaf entropy formulas,
  influence partition and terminal-inclusive inequality all checked.
- code/edge_reconstruct.py: {edge['cases']} roots, {edge['fibers']} physical
  fibers, {edge['checks']:,} checks, {edge['runtime_seconds']:.6f}s, PASS.
  Uses direct natural-coordinate Boolean edge counts and no Walsh/log kernel.
- code/witness.py:7 cases, {witness['checks']:,} checks,
  {witness['runtime_seconds']:.6f}s, PASS. The k=8 controller-first root is
  rigorously K4-bad, while the paired data-access policy is good. Both
  OR/XOR overlap replays retain their full weighted controller entropy.
- code/two_vertex.py:8 frozen cases, {two['checks']:,} checks,
  {two['runtime_seconds']:.6f}s, PASS. Same-fiber adjacent versus distinct-fiber
  edits at k=6,8 with overlapping four-bit OR/XOR/literal controllers;
  exact signed cross-spectrum, E(AB) cancellation and full terminal bill.

Total {checks:,} executed checks. Integer signed Walsh, Fraction influences,
exact rational prime-log expressions, outward80-bit log intervals from a
positive50-term atanh series with proved remainder. Root and leaf identities
are symbolic equality, not numerical closeness. Full records and prime-log
receipts are saved in out/. Only runtime clocks use floating point.
Memory estimates180 MB main/60 MB edge/70 MB witnesses/100 MB two-vertex; below300 MB trigger.
Peak memory is not claimed measured. Pilot/witness limits60s and full/edge
limits1800s were respected; jobs sequential, no GPU/background job or
automatic dimension escalation. Second implementation is author verification,
not an independent human acceptance.

## proof dependencies and changed downstream conclusions

Existing A022-ODDFACE-SURGERY-GAP-LEDGER advances v2 to v3, preserving inherited
scope and adding the one-/two-point controller theorems. It opens no new broad
universal candidate. C005 scalar proof is source-complete in prior PROOF §3;
the new signed spectra, mutation bound and terminal payment are rederived.
A021-POINT-SWITCH-RELATIVE-BIAS-PRICE v1 receives local partial review only
for its upper price and constant consequences; source statement/hash unchanged,
no repair contribution and no acceptance of its entire bundled theorem.
A025's inherited v1 constant-child review remains restricted to that subclaim.
All new A022 conclusions await independent review.

Downstream change: A021/A025 need not price every controller-first large-
contrast query for a single quadratic-bent point edit. Data-first paired
access is uniformly K4-good, regardless of controller overlap or width;
its exact terminal data bank pays the logarithmic spreading, and arbitrary
controller entropy is carried at its actual delta weight. A023's consumed
separator reserve is not renewed. A064's unfinished-core/controller question
now has a source-complete one-point data-first comparison. No shared registry
or other agent's folder was edited; no message was sent.

## one next mathematical action and independent reviewer

{next_action}
Review must check both factors of tau, the raw/character-shifted influence
comparison, adjacent E(AB) cancellation and the distinction between all-bent
root identities and paired quadratic access. This targets growing signed
collision ownership, not another exhaustive small controller census.

## actual persistence receipts or precise save blocker

All required protocol files, PROOF.md, TWO_VERTEX_PROOF.md, REVIEW_A021.md, code and exact outputs
saved locally in this run. STATUS has two lines, WORKLOG appended and LEARNED
updated. out/ARTIFACT_RECEIPTS.json records bytes/SHA256; finalize.py checks
field sets, compatibility equality, canonical statement hashes and20 MB cap.
No save blocker; supervisor copies, canonical adoption, independent acceptance,
remote mirrors and downstream use remain unverified.

Universal bridge: This stage moves C019/B05 localized odd-face payment at
the large-contrast one-point interface. It removes inactive-branch fairness
from paired access, gives zero K4 access credit for arbitrary overlapping
controllers, and pays the exact leaf spreading terms from terminal data
influence while retaining delta H(controller) intact. The first unequal-
reference collision is also paid at coefficient9, including actual adjacent
edge cancellation. Arbitrary controller FEI and growing edit sets remain
unpaid. NEXT determines the support-size guard for one data bank across
many such collisions, the shortest route toward universal ownership because
it tests reserve scaling rather than enlarging a paid controller grid.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
(BASE/'STATUS.md').write_text(f'STATE: A022 stage4 complete: arbitrary-controller one-/two-point paired access K4-good; exact log/cross formulas; H<=7 or9 I_data plus complete inherited controller entropy; {checks} checks PASS; A021 upper-price scoped HOLDS; FEI OPEN.\nNEXT: A087/A094 review; derive a support-size/data-dimension guard for growing edit sets with one actual terminal data bank and all inherited controller entropies.\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (BASE/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n2026-10-14 01:49 UTC stage, saved {stamp}: Consumed A021 bounded-contrast closure and independently reconstructed its upper-price/K6/K7 subclaims only. Changed to data-first point-surgery access before arbitrary overlapping controllers: all-even-k>=4 K4-good access, exact all-bent signed root entropy and complete character-shifted terminal spectrum. Proved H<=7I_data+delta H(controller); then closed two unequal-controller point edits at coefficient9 for k>=6, retaining signed cross-spectrum and adjacent -4delta b(v)b(w)E(AB) correction. Only actual terminal data influence pays spreading, with all controller entropy inherited once. Main6672 roots,7 contrast/overlap witnesses,8 two-vertex certificates and independent edge reproduction PASS; total{checks} checks. Arbitrary-controller FEI and growing edit-set ownership remain open; extended existing A022 claim to v3 without a new broad candidate.\n')
with (BASE/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage4 one-point arbitrary-controller transport: F=b(x)(1-2*1_(x=v)*A(z)), quadratic paired bent k=2m>=4 and arbitrary independent indicator A. Expose first bit of every pair, then STOP. Surviving perturbation measure alpha 2^{-(k-q)} gives d>=1/2-2^-m>=1/4 without controller fairness; every access node K4-good. One leaf of reach tau=2^-m is chi_L times q=1-2*point*A; its exact entropy is phi((1-2tau alpha)^2)+(2^m-1)phi(4tau^2alpha^2)+tau[H(a)-phi((1-2alpha)^2)]+8tau alpha(1-alpha)m. Raw partner I=2m tau alpha, and character shift only increases it for m>=2. H_leaf<=tau H(a)+7 I_leaf,data, so global H(F)<=7I_data+delta H(a), I_ctrl=delta I(a), delta=tau^2; no controller I is spent on alpha-log-alpha. Root signed spectrum and its two bent alignment masses are exact for ALL bent signs, but the good stopping schedule specifically needs quadratic pairs. TWO-POINT extension: arbitrary possibly dependent A,B at distinct vertices, k>=6, has H<=9I_data+delta[H(a)+H(c)] and I_ctrl=delta[I(a)+I(c)]. Adjacent data-edge correction is -4delta b(v)b(w)E(AB), and same-fiber raw terminal data I>=2tau(m-1)(EA+EB) uses the actual post-cancellation boundary. Spectral cosets have signed amplitudes u+z,u-z before squaring. Controller hardness is inherited; growing edit sets require a support-size guard or new reserve. A021 upper-price/K6/K7 subclaims independently HOLDS only; no whole-bundle acceptance or repair contribution.\n')
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
assert all(set(c)==set(protocol['required_per_run']['claim_fields']) for c in (own,review))
assert set(progress)=={x if not x.startswith('packet_ids ') else 'packet_ids' for x in protocol['required_per_run']['progress_fields']}
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
for c in (own,review):
    digest=hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert digest==c['statement_sha256']
sources=[ROOT/'BOARD.md',ROOT/'claude/B05/STREAM_NOTES.md',PREV/'PROOF.md',PREV/'CLAIMS.json',source_run/'REPORT.md',source_run/'DERIVATION.md',source_run/'CLAIMS.json',ROOT/'agents/A023/runs/20261013T223305Z-account05-A023-amortized-rarity-budget/REPORT.md']
(RUN/'out/SOURCE_INVENTORY.json').write_text(json.dumps([{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources],indent=2)+'\n',encoding='utf-8')
receipts=[]
for p in sorted(RUN.rglob('*')):
    if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
        data=p.read_bytes();assert len(data)<20*1024*1024
        receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(RUN/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps({'schema':'PASS','compatibility_copy':'IDENTICAL','statement_hashes':'PASS','total_checks':checks,'artifacts':receipts,'mirror':'UNVERIFIED'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'run':RID,'total_checks':checks,'artifacts':len(receipts),'schema':'PASS','largest_bytes':max(r['bytes'] for r in receipts)}))
