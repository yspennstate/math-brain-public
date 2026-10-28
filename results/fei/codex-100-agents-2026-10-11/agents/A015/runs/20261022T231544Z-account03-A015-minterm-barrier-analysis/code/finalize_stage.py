"""Persist and validate this stage's protocol artifacts, using landed certificates."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
SHARED=AGENT.parents[1]
CAMPAIGN=Path('math-open-problems/reports/fei-2026-10-11')
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,data):p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

pilot=read(RUN/'out/pilot.json');checks=read(RUN/'out/checks.json');review=read(RUN/'out/frontier_review.json')
assert pilot['assertions']==520 and checks['assertions']==173104 and review['status']=='PASS'
assert len(checks['physical'])==31 and len(checks['queue'])==12
assert sum(c['outputs'] for c in checks['queue'])==2004
assert checks['script_sha256']==sha(RUN/'code/check_rare_core.py')
assert review['script_sha256']==sha(RUN/'code/check_frontier_review.py')
total=pilot['assertions']+checks['assertions']+review['assertions']
queue=CAMPAIGN/'source_material/reductions/paper/forests.tex'
a007=SHARED/'agents/A007/runs/20261021T211258Z-account03-A007-root-normalization'
sources=[CAMPAIGN/'EXECUTION_PROTOCOL.json',SHARED/'BOARD.md',SHARED/'claude/B03/STREAM_NOTES.md',
         queue,a007/'REPORT.md',a007/'CLAIMS.json',a007/'KMM_PAYMENT.md',a007/'SCALE_CANCELLATION.md',
         SHARED/'agents/A008/runs/20261021T234312Z-account03-A008-gate-label-compression/REPORT.md',
         SHARED/'agents/A009/runs/20261022T220926Z-account03-A009-fractional-incidence-optimization/REPORT.md',
         SHARED/'agents/A009/runs/20261022T220926Z-account03-A009-fractional-incidence-optimization/LEAFLESS_CERTIFICATE.md']
dump(RUN/'out/source_receipts.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
statement=(
 'For the original conditioned forest queue (gamma=6/5), N equal-width W signed conjunction gates, '
 'and fixed uniform lambda=1/N, if h original gates cover every relevant coordinate, each nonempty '
 'output A has a selected successful event of probability Q(A)>=2^(-1-h log2(N)-(5h-1)W); '
 'the actual whole-output probability Q_*(A)>=Q(A). In particular for F=2 A_r '
 '1_{|x|>=m-t}1_{|y|>=m-t}-1 on disjoint uniform blocks, m>=2, r>=0 and '
 '0<=t<=max(1,floor(m/4)), its unchanged full positive-prime table with N=binom(m,t)^2, '
 'W=2(m-t)+r and lambda=1/N has complete nonempty cross-entropy C_*<=96 I(F), and '
 'H(F)<=107 I(F). In the central-band extension m=2k,t=k,r=0 (k>=1), the same '
 'two-prime coordinate cover exists but (2m)Var(F)/I(F)>=(7/8)sqrt(k+1); this is '
 'an obstruction to uniform dimension-budget payment only, not a queue-cost or FEI lower bound.'
)
claim={
 'claim_id':'A015-BOUNDED-COORDINATE-COVER-RARE-CORE-PAYMENT','version':1,
 'exact_statement':statement,
 'hypotheses':['Uniform independent cube; sign Boolean functions; entropy and ideal lengths in bits',
   'Original queue items(i)-(iv) and eq:forestconditioning, one fixed physical full order per gate, failed and infinite runs retain missing mass',
   'Positive same-width conjunction table; uniform positive packing weights fixed before any output; h selected original gates cover all relevant coordinates',
   'Rare-core bound uses only the stated m,t,r domain; central extension is a dimension-budget obstruction, outside that corollary'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A015'],
 'proof_source':['RARE_CORE_PAYMENT.md','FRONTIER.md','code/check_rare_core.py','code/check_frontier_review.py','out/checks.json','out/frontier_review.json'],
 'proof_dependencies':['Original queue definitions only: forests.tex sha256='+sha(queue)+'; no upstream selected-lift, FEI, root-occupation or transfer lemma is assumed'],
 'review_records':[{'reviewer':'A015','scope':'Author analytic proof plus separate exact event/spectrum implementation; not independent acceptance',
                    'assertions':total}],
 'status':'AUTHOR_PROOF_EXACT_FINITE_CHECKS_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A007','A008','A086','A094','B03','B20']}
dump(RUN/'CLAIMS.json',[claim])

next_action=('For the central-band extension, aggregate all compatible one-root prime events in the same '
             'fixed queue, and estimate their expected subset/rank length instead of using n Var; '
             'independent reconstruction requested from A007/A008, with A086/A094 for constants and scope.')
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B03','packet_id':'A015',
 'gap_id':'C020-COMPLETE-FINAL-REFERENCE-RARE-LEAFLESS-CORE',
 'attempt_id':'A015-stage7-two-original-roots',
 'method':'Direct actual queue event reconstruction, exact Boolean Walsh/pivotal checks, rational interval subset probabilities, analytic binomial bounds, scoped A007 review',
 'mathematical_delta':'Consumes A007 rare-core next target: complete same-prime actual-queue cost <=96 I for vanishing-mass leafless threshold products, all controller counts including zero; bounded-coordinate-cover lemma; exact central-band dimension-budget divergence; no full FEI conclusion.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS_AND_RECEIPTS',
 'mathematical_status':'RESTRICTED_ANALYTIC_CERTIFICATE_FINITE_EXACT_CHECKS_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':['A007-COMBINED-LEAFLESS-PAYMENT-AND-SCALE-CANCELLATION@1 (scoped review and target consumption only; not a proof dependency)'],
 'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['RARE_CORE_PAYMENT.md','FRONTIER.md','REVIEW_A007.md','SEARCH_SPEC.json','REVIEW_SPEC.json','out/source_receipts.json','out/receipts.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Independent review pending; no universal expected-rank/subset payment established',
             'Brain self-care degraded/unverified: wake reports owner model about86h and state of mind about70h stale; current instructions/local mathematics used instead',
             'Supervisor owns remote copies and registry adoption; no publication or mirror verification claimed'],
 'packet_ids':['A015']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)

report=f'''# A015 stage7: a complete queue payment for rare leafless cores

## exact target, quantifiers, hypotheses and units

Pay the COMPLETE final-reference code on A007's rare leafless target, without
assuming a positive controller influence bank. For every m>=2, r>=0 and
0<=t<=max(1,floor(m/4)), use F=2 A_r 1_{{|x|>=m-t}}1_{{|y|>=m-t}}-1 on
n=2m+r uniform independent bits. Keep its full positive-prime table,
N=binom(m,t)^2, W=2(m-t)+r, uniform lambda=1/N and one full physical order
per prime fixed before exposure. All logarithms are base two. The result is
C_*<=96 I(F) for the complete original conditioned queue cross-entropy,
including all output sectors; H(F)<=107 I(F) follows. This class's FEI is
already accessible by threshold composition; the new output is the complete
same-prime queue certificate, not a claim of a novel FEI class or full FEI.

## sources actually read, revisions and theorem locators

Read the current BOARD.md (updated 2026-10-22 23:09 UTC), B03 STREAM_NOTES.md,
own STATUS.md and prior substantive stage6. Read A007's stage
20261021T211258Z REPORT, CLAIMS, KMM_PAYMENT and SCALE_CANCELLATION; consume
its rare high-threshold next target instead of redoing its solved K_m,m
payment. Read A008 stage20261021T234312Z REPORT and A009
stage20261022T220926Z REPORT/LEAFLESS_CERTIFICATE; do not duplicate their
root or deleted-edge results. Original reference definitions are forests.tex,
section Conditioned witness forests, items(i)-(iv), eq:forestconditioning
(first60 lines, read directly); hash {sha(queue)}.
Execution protocol revision2026-10-11-execution-v2 was reread in full.
The initial campaign sources and two paper revisions were read in the
preceding substantive stage; no uninspected paper theorem is used here.
Actual source hashes are in out/source_receipts.json. The owner's Oct23
14:49 UTC campaign deadline supersedes the old deadline in the protocol.

## complete derivation or exact first unsupported line

RARE_CORE_PAYMENT.md contains the full elementary analytic proof. For any
same-width N-gate table with h original gates covering all relevant
coordinates, assign each output coordinate to its first covering gate and
use at most h roots, disjoint nonempty subsets and zero children. Every
factor of this ACTUAL queue event is retained, including absence of all
unused roots and conditioning on nonempty roots. A visit costs at most4W
bits. Exact root probability is (pi/N)^c/[(1+pi/N)^N-1], giving
Q(A)>=2^[-1-h log N-(5h-1)W]. Q is the chosen-event subprobability;
the whole-output queue mass Q_* is larger. Thus this is an upper-cost
certificate, not an invalid lower-cost transfer from a selected family.

Two original primes cover the rare threshold-product family (one for t=0).
Their events give complete cost <=12n Var(F). Exact pivotal counting and a
binomial tail bound give I_g/b>=m, so n Var(F)<=8I(F), including r=0 and
arbitrarily small b. Hence C_*<=96I(F), with no inherited R_g, control-only,
empty-control, rarity or normalization bill left unpaid. Binary entropy
contributes <=11I(F). No source K_ref is assumed or silently dropped.

FRONTIER.md proves that this missing compression is still essential: for
m=2k,t=k,r=0 the same two-prime coordinate cover exists but
n Var(F)/I(F)>=(7/8)sqrt(k+1). This lower-bounds the crude DIMENSION BUDGET
only; it is not a lower bound on Q_* cost or H/I. The exact first unsupported
universal line is an influence payment for the actual expected subset/rank
length on arbitrary covers, without replacing it by a uniform ambient-width
bound. No general representation lemma or full FEI assertion is made.

## executed validation with domain, arithmetic, commands and outputs

Frozen SEARCH_SPEC.json precedes the computations. Commands from this run:
`python -X utf8 code/check_rare_core.py --pilot` passed {pilot['assertions']}
assertions in {pilot['elapsed_seconds']}s, on8 physical instances.
`python -X utf8 code/check_rare_core.py` passed {checks['assertions']} assertions
in {checks['elapsed_seconds']}s. It exhausts every truth input and Fourier
coefficient in31 physical cases: m=2..6, all declared t, r=0..2, plus
(m,t,r)=(8,2,0), max n=16. Separate direct bit-flip influences and tensor
coefficients agree with integer Walsh transforms. It checks5049 scalar
parameter triples through m=64, all2080 visit pairs W<=64, and every one of
2004 nonempty outputs in12 actual-queue cases (m=2..4,t=0,1,r=0,1).
Root probabilities are rational; subset normalizers use rigorously enclosed
dyadic fifth roots of width2^-64. No floating result is an acceptance test.

The separately frozen REVIEW_SPEC.json precedes
`python -X utf8 code/check_frontier_review.py`: {review['assertions']} assertions
passed in {review['elapsed_seconds']}s, including128 central-binomial cases,
127 scalar A007 payment cases and9 changing-posterior scale fixtures.
The combined checks total {total} assertions (pilot overlaps are disclosed).
The all-dimensional theorems follow from the analytic proofs, not finite
extrapolation. No Lean certification or independent acceptance is claimed.
Jobs were bounded below100MB estimated memory and55s runtime; no heavy job
or memok-triggering allocation was launched. Shared compute snapshot had
about2GB available; existing work was left alone. Every job is finished.

## proof dependencies and changed downstream conclusions

The NEW theorem depends only on the original queue definitions, not A007's
selected-lift transfer or A015's earlier one-control theorem. Two nonminimal
roots are permitted queue runs, even when they are outside the old minimal
source-SCC selected family. The reference, table, weights and root normalizer
remain fixed; only the exhibited successful event changes.

REVIEW_A007.md reconstructs the new rational29 payment and finite scale
cancellation identity. This scoped review is conditional on its named
upstream transfer and excludes A015's own upstream inequality and A007's
sharp asymptotic. It is not acceptance of the compound dependency chain.
The new result removes the positive-controller-bank hypothesis from this
specific C020 stress test; no general shared-incidence payment follows.

## one next mathematical action and independent reviewer

{next_action}
This directly attacks the unpaid compression feature rather than proving
another isolated threshold-composition FEI case.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, analytic
proofs, two frozen specs, code and exact outputs are saved locally in this
run. code/finalize_stage.py validates protocol field sets, certificate
script hashes, output case counts and compatibility equality, then writes
and rereads out/receipts.json for every run artifact and the three rolling
files. No research save blocker exists. Supervisor-owned remote copying,
registry adoption and mirror verification are not claimed. Brain self-care
is degraded/unverified: wake reports owner model about86h and state of mind
about70h stale; personal-context recall remains affected, while the local
proof and exact certificates use current instructions and source files.

**Universal bridge:** This stage moves C020 whole-set witness cost by paying
the COMPLETE unchanged-prime queue for a vanishing-mass leafless core, even
with no controls, with constant96. It also proves that a two-prime coordinate
cover alone cannot pay the uniform dimension budget in the central band.
What remains is the actual expected subset/rank payment, and ultimately a
universal representation with bounded influence cost. Aggregating compatible
one-root events in that same central-band stress test is the shortest next
route because it tests exactly the compression absent from minterm coding,
with all final-reference factors exposed; full FEI remains OPEN.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text(
 f'STATE: A015 stage7 saved: complete fixed-prime rare leafless queue cost <=96I; central dimension budget diverges; {total} exact assertions PASS; review pending, full FEI OPEN.\n'
 'NEXT: Aggregate all compatible one-root prime events in the central-band family; pay expected subset/rank length. A007/A008/A086/A094 independent review requested via saved handoff.\n',encoding='utf-8')
entry=(f'\n{stamp} | {RUN.name}: Consumed A007 new rare-core target after its full K_m,m payment. '
       f'Proved bounded-coordinate-cover actual-event certificate and full cost <=96I for rare threshold products, '
       f'r>=0, including vanishing b; central-band dimension-budget ratio >=(7/8)sqrt(k+1). '
       f'{total} exact checks passed; scoped A007 numerical payment/scale review excludes own upstream work. '
       'Complete local artifacts saved; no jobs running; full FEI open and independent review pending.\n')
work=AGENT/'WORKLOG.md';work.write_text(work.read_text(encoding='utf-8')+entry,encoding='utf-8')
learn=(f'\n## {stamp}: complete rare-core queue payment (stage7)\n\n'
       '- Same-width N-gate original conditioned queue, uniform lambda=1/N, h original gates covering all coordinates: '
       'each nonempty A admits an actual selected event Q(A)>=2^[-1-hlog2N-(5h-1)W]. All absence, conditioning, subset and zero-child factors are included. '
       'Q_*>=Q, so this gives an upper cost, never a lower bound for all runs.\n'
       '- F=2 A_r 1_{|x|>=m-t}1_{|y|>=m-t}-1, m>=2,r>=0,0<=t<=max(1,floor(m/4)): '
       'full exact positive-prime table uniform1/binom(m,t)^2 has two-gate coordinate cover, nVar<=8I, complete queue cross-entropy<=96I, H<=107I. '
       'Rare leafless t=1 has b=(m+1)^2/4^m; no positive controller bank needed. Analytic proof and exact checks; independent review pending.\n'
       '- Central extension m=2k,t=k,r=0 retains two-prime coordinate cover but nVar/I>=(7/8)sqrt(k+1). '
       'This obstructs the crude ambient-dimension payment only, not actual queue cost or FEI. Need expected subset/rank compression or a fully paid grouped reference.\n'
       '- A007 scale cancellation reconstructed with exact exponentiation: retain all2^r control subsets, including empty. '
       'Changing the intermediate scaling changes its posterior but not the combined inherited final-scale cost. '
       'Scoped review excludes A015 own prior theorem; constants29 refer to surrogate residual, not actual queue.\n')
learned=AGENT/'LEARNED.md';learned.write_text(learned.read_text(encoding='utf-8')+learn,encoding='utf-8')

protocol=read(CAMPAIGN/'EXECUTION_PROTOCOL.json')['required_per_run']
pf={s.split(' (')[0] for s in protocol['progress_fields']}
assert set(progress)==pf
assert set(claim)==set(protocol['claim_fields'])
assert read(RUN/'PROGRESS.json')==read(RUN/'PACKET_DELTA.json')
for h in protocol['report_fields']:assert '## '+h in report
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
paths=sorted(p for p in RUN.rglob('*') if p.is_file() and p.name!='receipts.json')
paths += [AGENT/name for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]
receipts=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in paths]
assert all(r['bytes']<20_000_000 for r in receipts)
dump(RUN/'out/receipts.json',receipts)
for item in read(RUN/'out/receipts.json'):
    assert sha(Path(item['path']))==item['sha256']
print(json.dumps({'status':'SAVED_AND_VERIFIED','assertions':total,'receipt_files':len(receipts),
                  'claim_id':claim['claim_id'],'statement_sha256':claim['statement_sha256']}))
