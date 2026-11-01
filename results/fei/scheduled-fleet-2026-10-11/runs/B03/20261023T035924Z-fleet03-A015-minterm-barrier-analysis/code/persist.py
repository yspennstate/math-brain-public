"""Land protocol records and verify final artifacts; safely idempotent rolling append."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

RUN=Path(__file__).resolve().parents[1];AGENT=RUN.parents[1];SHARED=AGENT.parents[1]
CAMPAIGN=Path('~/mop_fei100/reports/fei-2026-10-11')
A008=SHARED/'agents/A008/runs/20261023T024024Z-fleet03-A008-gate-label-compression'
A014=SHARED/'agents/A014/runs/20261023T032009Z-fleet03-A014-overlap-beyond-worst-case-read'
PRIOR=AGENT/'runs/20261022T231544Z-fleet03-A015-minterm-barrier-analysis'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

pilot=read(RUN/'out/pilot.json');full=read(RUN/'out/checks.json')
assert pilot['assertions']==1831 and full['assertions']==79937
assert full['script_sha256']==sha(RUN/'code/check.py')
assert full['transport']['functions']==256 and full['transport']['queries']==3072
assert sum(x['outputs'] for x in full['central']['queue'])==270
assert len(full['central']['physical'])==3
total=pilot['assertions']+full['assertions']
source=next(x for x in read(A008/'CLAIMS.json') if x['claim_id']=='A008-CENTRAL-PRIME-COMPATIBLE-ROOT-AGGREGATION')
canonical=json.dumps({'statement':source['exact_statement'],'hypotheses':source['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False)
assert hashlib.sha256(canonical.encode('utf-8')).hexdigest()==source['statement_sha256'],'source hash convention'
imported=json.loads(json.dumps(source))
imported['review_records'].append({'reviewer':'A015','role':'Independent reconstruction, no repair; motivating prior A015 obstruction is not a proof dependency',
 'verdict':'HOLDS_FULL_STATED_SCOPE_USING_ESTABLISHED_THRESHOLD_THEOREM_A',
 'evidence':[str(RUN/'REVIEW_A008.md'),str(RUN/'out/checks.json')]})
imported['status']='INDEPENDENTLY_REVIEWED_A015_AT_STATED_SCOPE'
imported['proof_source']=[str(A008/'CENTRAL_PAYMENT.md'),str(A008/'out/full.json'),str(RUN/'REVIEW_A008.md')]
statement=('For every finite uniform-cube sign Boolean function f and every fixed strictly positive nonempty-set subprobability q '
 '(sum q<=1), define C(f;q)=h2(Var(f))+sum_{A nonempty} fhat(A)^2 log2(1/q(A)). For a query i in dimension at least2, '
 'supply BOTH restrictions with q_i(T)=(q(T)+q(T union {i}))/(1-q({i})) for nonempty T avoiding i. Then '
 'Delta_i=C(f;q)-(C(f_+;q_i)+C(f_-;q_i))/2>=0, with the exact categorical/Jensen/Bernoulli-KL/original-phase '
 'decomposition in SUBPROBABILITY_TRANSPORT.md(3)-(5). After queried set D, q_D(A)=sum_{B subset D}q(A union B)/(1-e_D), '
 'e_D=sum_{nonempty B subset D}q(B), and its missing mass is (1-sum q)/(1-e_D); thus the source is independent of query '
 'order and observed bits given D. Every finite adaptive tree/stopping cut has exact account '
 'sum_internal reach Delta+sum_leaves reach C(f_leaf;q_D)=C(f;q), all terms nonnegative, with constants cost zero. '
 'This is supplied-reference transport only: no universal root-cost bound or arbitrary-reset payment is asserted.')
claim={'claim_id':'A015-SUBPROBABILITY-ORIGINAL-REFERENCE-HISTORY-TRANSFER','version':1,
 'exact_statement':statement,
 'hypotheses':['All logs/costs in bits; physical independent uniform cube; sign Boolean f',
 'q is fixed before later restriction outcomes and positive on every nonempty physical subset; total<=1',
 'For dimension1 or constant leaves handle full child costs directly; zero masses use0log0=0',
 'The invariant reference is the original q projected with cemetery mass retained, not a new restricted prime-table queue'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A015'],
 'proof_source':['SUBPROBABILITY_TRANSPORT.md','code/check.py','out/checks.json'],
 'proof_dependencies':['Direct Walsh restriction identity, entropy coarsening, binary concavity and nonnegativity of KL; all reconstructed in the proof',
 'A014 DERIVATION.md(9)-(11) is the independently reviewed normalized antecedent, not an assumed unreviewed clique root-cost theorem'],
 'review_records':[{'reviewer':'A015','role':'Author proof and independently implemented exact rational verification, not independent-agent acceptance',
 'verdict':'PASS','evidence':['out/checks.json','SUBPROBABILITY_TRANSPORT.md']}],
 'status':'AUTHOR_PROOF_EXACT_CHECKS_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A008','A014','A007','A086','A094','A096','A097','B03','B20']}
dump(RUN/'CLAIMS.json',[imported,claim])
next_action=('Pay the ORIGINAL compatible-prime/rank reference on a genuinely nonsymmetric implicant table from influence, '
 'without replacing it by an entropy comparison; preserve this cemetery-aware source and all old debits under restriction. '
 'A008/A014/A086/A094 should independently reconstruct the supplied-reference extension; A007/A008 consume the central review.')
sources=[SHARED/'BOARD.md',SHARED/'claude/B03/STREAM_NOTES.md',CAMPAIGN/'EXECUTION_PROTOCOL.json',
 CAMPAIGN/'source_material/reductions/paper/forests.tex',SHARED/'context/threshold_paper_38pp.txt',
 A008/'REPORT.md',A008/'CLAIMS.json',A008/'CENTRAL_PAYMENT.md',A014/'REPORT.md',A014/'CLAIMS.json',A014/'DERIVATION.md',
 PRIOR/'RARE_CORE_PAYMENT.md',PRIOR/'FRONTIER.md',PRIOR/'CLAIMS.json']
dump(RUN/'out/SOURCE_RECEIPTS.json',[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sources])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN.name,'stream':'B03','packet_id':'A015',
 'gap_id':'C024-ORIGINAL-QUEUE-SUBPROBABILITY-HISTORY-TRANSFER',
 'attempt_id':'A015-stage8-central-review-cemetery-projection',
 'method':'Independent actual queue root-sum reconstruction; universal coefficient-pair transport with cemetery mass; exact rational power identities and live Boolean negative control',
 'mathematical_delta':'A008 central251I/5 claim independently HOLDS at stated scope; A014 normalized full-projection(9)-(11) scoped HOLDS; strict subprobability extension preserves the same original queue through all adaptive histories, with full binary wrappers and old debits. Conditional applications: rare-core root fleet107I, central account256I/5. Full FEI OPEN.',
 'deliverable_status':'COMPLETE_LOCAL_PROTOCOL_FILES_PROOFS_CHECKS_RECEIPTS',
 'mathematical_status':'SOURCE_REVIEW_COMPLETE_SUPPLIED_REFERENCE_EXTENSION_PENDING_REVIEW_UNIVERSAL_ROOT_PAYMENT_OPEN',
 'claim_versions_used':[source['claim_id']+'@1 (independently reviewed; threshold baseline explicit)',
 'A014-INTERFERENCE-COMPLETE-CRITERION-AND-PP-GUARD@6 (scoped9-11 only)',
 'A015-BOUNDED-COORDINATE-COVER-RARE-CORE-PAYMENT@1 (conditional root-cost application, author proof not independently accepted here)'],
 'claims_created_or_changed':[claim['claim_id']+'@1',source['claim_id']+'@1: A015 independent review record, statement/version unchanged'],
 'source_artifacts':['SUBPROBABILITY_TRANSPORT.md','REVIEW_A008.md','REVIEW_A014.md','FROZEN_SPEC.json','out/checks.json','out/SOURCE_RECEIPTS.json','out/RECEIPTS.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal original-reference root cost for nonsymmetric Boolean covers remains unpaid; no full FEI claim',
 'New subprobability extension awaits independent-agent acceptance; prior rare-tail root certificate remains pending review',
 'Brain self-care degraded/unverified: owner model90.3h and state-of-mind74.9h stale; personal-context freshness affected, not used in mathematical proof',
 'Supervisor owns publication/remote copying; remote persistence and adoption unverified'],
 'packet_ids':['A015']}
dump(RUN/'PROGRESS.json',progress);dump(RUN/'PACKET_DELTA.json',progress)
report=f'''# A015 stage8: original queue payment survives adaptive restrictions

## exact target, quantifiers, hypotheses and units

Consume the current central-band closure instead of duplicating it, then
carry a paid actual queue through restriction histories without a hidden
normalization or a renewed budget. Bits; sign Boolean functions on uniform
cubes. The supplied-reference theorem holds for EVERY f, EVERY fixed
q(A)>0 on nonempty sets with sum q<=1, and EVERY finite adaptive restriction
tree/stopping cut. Its full cost is h2(Var f)+sum_nonempty p(A)log(1/q(A)).
It does not assert a dimension-independent root payment for arbitrary f.

## sources actually read, revisions and theorem locators

Read current BOARD.md dated2026-10-23 03:54 UTC, B03 STREAM_NOTES v2,
machine AGENTS.md, current scheduled owner-control README and own STATUS.
A008 had already solved our saved central-band NEXT: read its
20261023T024024Z REPORT, CLAIMS and CENTRAL_PAYMENT in full. Read A014
20261023T032009Z REPORT/DERIVATION in full and identify its version6 claim;
review scope is DERIVATION(9)-(11), not the complete clique package.
Source forest queue definitions/normalizer are inherited from the preceding
stage and reconstructed in the independent checker. Threshold38pp text
Theorem A, Creg<8.937<9, reread using its actual cp1252 encoding. Older paper
versions and campaign baseline remain inherited reads, not new rereads.
Execution protocol2026-10-11-execution-v2 field contract reread; exact source
hashes are in out/SOURCE_RECEIPTS.json. One read-only math-brain recall
returned the known Boolean-convolution/coordinate-entropy guards and
threshold publication card; no recalled card supplies a proof premise.

## complete derivation or exact first unsupported line

REVIEW_A008.md independently reconstructs EVERY root-name/absence/rarity,
size/subset/child-count and compatible-output sum factor. Verdict HOLDS for
A008-CENTRAL-PRIME-COMPATIBLE-ROOT-AGGREGATION@1 at its unchanged statement
hash, using its explicitly established threshold Theorem A dependency.
Compatible one-root runs remove the uniform label cost before logarithms;
two disjoint original roots handle high-degree outputs. Orbit entropy then
pays rank cost and the threshold theorem pays that entropy. The6/5 entropy
coefficient is not an absorption proof of universal FEI.

REVIEW_A014.md reconstructs normalized full-CE projection/calibration and
stopping telescoping ONLY, using coefficient pairs and a categorical split.
No full bundled-clique acceptance is implied. SUBPROBABILITY_TRANSPORT.md
extends that supplied-reference mechanism to strict queue subprobabilities:

    q_i(T)=[q(T)+q(T+i)]/[1-q({{i}})].

Its missing mass is (1-sum q)/(1-q({{i}})), so failed/infinite runs remain
present. The exact parent-minus-average-full-child cost is the sum of a
categorical coarsening gap, binary Jensen gap, singleton Bernoulli KL and
ORIGINAL within-pair phase cross-entropy. All are nonnegative. On queried D,

    q_D(A)=sum_(B subset D)q(A union B)/(1-e_D),
    e_D=sum_(nonempty B subset D)q(B).

Thus one ORIGINAL reference reaches both children and all query orders;
reach-weighted old debits plus full stopped terminal costs equal root cost.
This is not the queue rebuilt from each restricted function's prime table,
nor does its CE decrease equal true entropy decrement. A genuinely changed
reference after a reset still requires its actual conversion bill.

Conditional on A015's pending-review stage7 root payment, every adaptive
history on its rare activated core uses the SAME107I original full account.
For the independently reviewed central A008 family, the full account is
<=256I/5, since nonempty cost<=251I/5 and h2(v)<=1<=I. This does not change
the nonempty251I/5 claim. A008's optional261I/5 used the weaker general
wrapper<=2I; our256I/5 uses I>=1 only on its named family. The earlier96I
A015 value is likewise NONEMPTY cost;107I is its FULL wrapped cost.

The exact first unsupported universal line remains an influence payment
for the ORIGINAL compatible-prime/rank cost on arbitrary nonsymmetric
Boolean covers. Supplied-reference transport cannot create the root bound.
Full FEI remains OPEN; the new theorem is not a universal representation lemma.

## executed validation with domain, arithmetic, commands and outputs

Frozen FROZEN_SPEC.json precedes both computations. From this run:
`python -X utf8 code/check.py --pilot`: {pilot['assertions']} exact assertions,
{pilot['elapsed_seconds']}s,8 Boolean tables and one central queue.
`python -X utf8 code/check.py`: {full['assertions']} exact assertions,
{full['elapsed_seconds']}s. All256 three-bit Boolean functions, all3 queries,
four fixed references give3072 query/reference cases. References include
normalized, strict subprobability, nonuniform and a positive smoothed Maj3
spectrum with cemetery mass. Every signed full-CE identity and sign is
certified by exponentiating rational log sums to exact Fraction products;
no tolerance or floating-point sign accepts a case. Direct child truth
restrictions independently verify Walsh coefficient-pair algebra.

Twenty-four reference/query-order combinations verify the ORIGINAL-source
formula and missing mass at every proper prefix. Central k=1,2,3 physical
spectra agree with tensor coefficients and pivotal influences; k=1,2 also
agree with independent direct character sums. Every270 nonempty output in
the k=1,2 queues is enumerated against actual prime lists and rotated fixed
orders.32-bit outward fifth-root intervals enclose weights and subset
normalizers; exact root sums verify the good/bad probability bounds and
complete selected-event subprobability. Good block-degree identities are
checked for k<=12. These are finite checks of separately supplied proofs,
not finite-to-universal extrapolation.

LIVE negative control: actual Maj3 with the fixed positive subreference
(3/4)[(1023/1024)P_Maj3+(1/1024)Unif(nonempty)] has a strictly negative
cost decrease when the conditioning denominator is omitted. Exact rational
power certificate is in out/checks.json; restoring the denominator passes.
The checker explicitly requires the wrong sign to fail.

Total {total} assertions including overlapping pilot checks. No Lean
certification claimed. Estimated memory95MB, max runtime55s, observed
full script wall time{full['elapsed_seconds']}s. No >300MB admission or
heavy job was required. Shared snapshot showed4226MB available and85.9%
live commit usage; existing ffmpeg/Python/Claude work was left untouched.
No background worker, GPU, remote machine or automatic dimension increase.

## proof dependencies and changed downstream conclusions

A008@1 now has an independent A015 review at its exact stated scope; no
statement/version or source hash changes. The threshold theorem remains
an explicit established dependency; its entire paper proof is not audited
again here. A014@6 normalized projection(9)-(11) has a scoped independent
review, with its clique/occupation package excluded. The subprobability
extension is proved directly from coefficient pairs, entropy coarsening,
concavity and KL positivity, and awaits independent review. Its applications
clearly distinguish independently reviewed central root payment from A015's
own still-pending rare-tail root payment. Failed queue mass is carried rather
than normalized away. Child references are inherited projections with
actual binary wrappers, not fresh covers or newly budgeted spectra.

## one next mathematical action and independent reviewer

{next_action}
The bottleneck is original mass/compatible-cover compression, not history
account renewal. No additional isolated threshold FEI result is proposed.

## actual persistence receipts or precise save blocker

Four exact-schema protocol files, proofs/reviews, frozen spec, code and
finite certificates saved locally; PACKET_DELTA equals PROGRESS with
packet_ids=[A015]. Three rolling files updated. code/persist.py verifies
source statement hash conventions, exact protocol fields, landed certificate
script hashes and case counts, file sizes, then writes/rereads out/RECEIPTS.json.
No research save blocker. Supervisor-owned remote copying, registry adoption
and mirror verification are unverified; no git/mail/brain write performed.
Brain self-care is degraded/unverified: owner-model90.3h and state-of-mind
74.9h stale; affected personal-context freshness is not used in the mathematics.

**Universal bridge:** C024 history transfer now carries EVERY already-paid
positive original queue subprobability through all adaptive restrictions
with cemetery mass, both FULL child terminals and old debits retained;
C020 consumes A008's central compatible-root closure via independent review.
The supplied full root accounts are107I on A015's rare core (conditional
root review) and256I/5 on A008's central core. What remains is the universal
ORIGINAL compatible-cover/rank influence payment, not a free reference reset.
NEXT targets that nonsymmetric original-mass bottleneck because the transport
account can now be reused once it is paid; another known-class FEI calculation
would not close the missing universal representation line.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text(
 f'STATE: A015 stage8 saved: A008 central251I/5 independently HOLDS; cemetery-aware full-CE projection pays ALL adaptive histories from SAME supplied root; {total} exact checks PASS; FEI OPEN.\n'
 'NEXT: Pay ORIGINAL compatible-prime/rank cost on a nonsymmetric implicant table without borrowing H; retain cemetery projection/old debits. A008/A014/A086/A094 review extension; universal root payment remains open.\n',encoding='utf-8')
work=AGENT/'WORKLOG.md'
if RUN.name not in work.read_text(encoding='utf-8'):
    work.write_text(work.read_text(encoding='utf-8')+f'\n{stamp} | {RUN.name}: Consumed A008 solved central target instead of duplicating it; independent full stated-scope HOLDS using established threshold baseline. Scoped A014(9)-(11) HOLDS; proved strict-subprobability/cemetery extension and all-history full-CE account. {total} exact assertions pass, including real Maj3 denominator fault control. Conditional full roots107I rare and256I/5 central; no universal root payment, FEI OPEN. NEXT: nonsymmetric original compatible-cover/rank influence bound, with same inherited reference.\n',encoding='utf-8')
learn=AGENT/'LEARNED.md'
if RUN.name not in learn.read_text(encoding='utf-8'):
    learn.write_text(learn.read_text(encoding='utf-8')+f'''\n## {stamp} — {RUN.name}\n
- A008-CENTRAL-PRIME-COMPATIBLE-ROOT-AGGREGATION@1 independently HOLDS at stated scope;251I/5 is NONEMPTY cost. Its compatible root labels sum BEFORE logarithms; full-wrapper cost<=256I/5 follows on that family from I>=1. Earlier261I/5 is a valid looser full-wrapper bound, not an inconsistent nonempty value.
- ANY fixed positive nonempty subprobability q survives restrictions by q_i(T)=[q(T)+q(T+i)]/[1-q({{i}})]. Missing mass becomes(1-sum q)/(1-q({{i}})); do not replace denominator by total successful mass or omit conditioning. Exact full-CE decrease is categorical coarsening+binary Jensen+singleton Bernoulli KL+original within-pair phase CE, all nonnegative.
- After queried D: q_D(A)=sum_(B subset D)q(A union B)/(1-e_D), e_D=sum_(nonempty B subset D)q(B). Depends on D, not order or observed values. Every adaptive stopping cut telescopes SAME original root full-CE account with all old debits/both full terminal costs retained. This is inherited projection, NOT the child prime-table queue or true entropy decrement.
- Real fault control: fixed positive smoothed Maj3 spectral subreference makes omission of1-q_i produce NEGATIVE full-cost decrease. Correct denominator passes exact rational power certification.
- A014 normalized full-CE transport(9)-(11) scoped HOLDS; no whole bundled-clique acceptance. A015 rare-tail source root certificate still independently unreviewed. New cemetery extension awaits independent review. Supplied-reference transport never creates the universal original root payment or pays arbitrary genuine resets.\n''',encoding='utf-8')
protocol=read(CAMPAIGN/'EXECUTION_PROTOCOL.json')['required_per_run']
assert set(progress)=={s.split(' (')[0] for s in protocol['progress_fields']}
for c in [claim,imported]:assert set(c)==set(protocol['claim_fields'])
assert read(RUN/'PROGRESS.json')==read(RUN/'PACKET_DELTA.json')
for field in protocol['report_fields']:assert '## '+field in report
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
paths=sorted(p for p in RUN.rglob('*') if p.is_file() and p.name!='RECEIPTS.json')
paths += [AGENT/name for name in ['STATUS.md','WORKLOG.md','LEARNED.md']]
receipts=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in paths]
assert all(x['bytes']<20_000_000 for x in receipts)
dump(RUN/'out/RECEIPTS.json',receipts)
assert all(sha(Path(x['path']))==x['sha256'] for x in read(RUN/'out/RECEIPTS.json'))
print(json.dumps({'status':'SAVED_VERIFIED','assertions':total,'receipts':len(receipts),'new_claim':claim['claim_id'],'hash':claim['statement_sha256']}))
