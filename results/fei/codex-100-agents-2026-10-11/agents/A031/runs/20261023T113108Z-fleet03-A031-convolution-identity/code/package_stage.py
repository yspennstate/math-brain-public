"""Persist the current stage only; no shared-tree writes, no search."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

RUN=Path(__file__).resolve().parent.parent
AGENT=RUN.parent.parent
ROOT=AGENT.parent.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def read(p): return p.read_text(encoding='utf-8')
def save(p,s): p.write_text(s,encoding='utf-8')
def jsave(p,o): save(p,json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def jread(p): return json.loads(read(p))
stamp=datetime.now(timezone.utc).isoformat()
run_id=RUN.name
claim_id='A031-SHARP-COMPATIBLE-PROFILE-GHOST-CAPACITY'
statement=(
'Let p,q be complete finite probability laws with CE(p,q)<infinity, pi a partition, '
'and prescribed child profiles r+,r- with mean pi(q). Among complete references R+,R- '
'with pi(Rtau)=rtau and (R++R-)/2=q, the mean CE increase is minimized by minimizing '
'-(1/2) sum_{p(s)>0} p(s) log2(1-t(s)^2), subject to Rtau(s)=q(s)(1+tau*t(s)) '
'and sum_{pi(s)=z}q(s)t(s)=Delta(z)=(r+(z)-r-(z))/2. Its minimum is zero iff '
'|Delta(z)|<=g(z)=sum_{pi(s)=z,p(s)=0}q(s) for every block. Beyond that capacity, '
'ghost tilts saturate at sign Delta and the unique occupied minimizer satisfies '
'p(s)t(s)/(1-t(s)^2)=lambda(z)q(s), with lambda fixed by the block constraint; '
'fully one-sided occupied boundaries have infinite cost. If p,q have matching '
'conditionals in each occupied block, the minimum equals -(1/2)sum_z pi(p)(z) '
'log2(1-((r+(z)-r-(z))/(2*pi(q)(z)))^2). For every coherent Boolean controller '
'G=a+sigma*(1-a^2)*parity4 on disjoint variables, the explicit complete references '
'of DERIVATION section4a achieve a prescribed nonempty profile change, proper only if E(1-a^2)>0, '
'at zero CE increment after querying the fourth seed bit, with zero erasure, JS, '
'occupancy refund and phase products. The incoming source is supplied; no initial '
'source admission or necessity of the prescribed class for universal FEI is claimed.')
first=('A universal proof must supply its mathematically necessary admissible reference '
'class and pay its minimum full-KL price from an actual unused source, or provide '
'influence-priced initial reference admission for arbitrary signed Boolean cores.')
check=jread(RUN/'out/CHECK.json')
repro=jread(RUN/'out/REPRODUCE.json')
ghost=jread(RUN/'out/GHOST_CHECK.json')
indep=jread(RUN/'out/GHOST_REPRODUCE.json')
review=jread(RUN/'out/REVIEW_A035.json')
claim={
'claim_id':claim_id,'version':1,'exact_statement':statement,
'hypotheses':['Finite complete reference laws and finite parent CE; all ghosts and both children retained.',
'The prescribed branch profiles and full-mean compatibility are explicit additional obligations.',
'The simple block logarithm requires matching occupied-block conditionals; the general ghost-capacity solution does not.',
'Coherent controller a takes values in {-1,0,1}, b=1-a^2, seed and controller variables disjoint, sigma in {-1,1}.',
'No universal necessity of these reference obligations and no initial Boolean source bound are assumed proved.'],
'statement_sha256':sha(statement.encode('utf-8')),'contributors':['A031'],
'proof_source':['DERIVATION.md sections2-6','code/check_calibration.py','code/reproduce.py','code/check_ghost.py','code/reproduce_ghost.py'],
'proof_dependencies':['Elementary CE/KL chain rule and convexity, proved in DERIVATION.',
'Signed physical Boolean child amplitudes u+/-v; actual witnesses checked by full Walsh convolution.',
'A035-ALL-QUERY-TERMINAL-KL-ENVELOPE v1 is consumed as a separate reviewed frontier, not required for the variational theorem.'],
'review_records':[{'reviewer':'A031 author self-check','verdict':'ANALYTIC_PROOF_AND_EXACT_CERTIFICATES_PASS_EXTERNAL_REVIEW_PENDING','artifact':'out/GHOST_REPRODUCE.json','scope':'Independent implementation, same author; not independent peer review.'}],
'status':'PROVED_BY_AUTHOR_WITH_EXACT_CERTIFICATES_PENDING_INDEPENDENT_REVIEW',
'supersedes':[],'refutes':['An unrestricted claim that positive prescribed block-profile change forces positive conversion cost even when reference-only capacity suffices.'],
'first_unproved_line':first,'next_consumers':['B07 Claude lead','A035','A096','A097','C019/C024 universal bridge reviewers']}
jsave(RUN/'CLAIMS.json',[claim])
sources=[
Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'),
ROOT/'BOARD.md',ROOT/'claude/B07/STREAM_NOTES.md',AGENT/'LEARNED.md',
ROOT/'agents/A035/runs/20261023T110610Z-fleet03-A035-signed-cancellation-countersearch/DERIVATION.md',
ROOT/'agents/A035/runs/20261023T110610Z-fleet03-A035-signed-cancellation-countersearch/REPORT.md',
ROOT/'agents/A035/runs/20261023T110610Z-fleet03-A035-signed-cancellation-countersearch/CLAIMS.json',
ROOT/'agents/A097/runs/20261023T062140Z-fleet03-A097-cross-route-transfer/DERIVATION.md',
AGENT/'runs/20261023T045953Z-fleet03-A031-convolution-identity/code/reproduce.py']
source_receipts=[{'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sources]
jsave(RUN/'out/SOURCE_RECEIPTS.json',source_receipts)
progress={
'protocol_revision':'2026-10-11-execution-v2','run_id':run_id,'stream':'B07','packet_id':'A031',
'gap_id':'C024-isospectral-compatible-reference-constraints','attempt_id':'A031-stage20-sharp-ghost-capacity',
'method':'Analytic finite convex optimization with explicit minimizer, exact rational primal/dual certificates, independent exact-power reproduction, full signed Boolean witnesses.',
'mathematical_delta':'Sharp zero-price iff reference-only capacity suffices; explicit optimizer beyond capacity; all coherent Boolean controllers inherit the free profile change; consumed A035 all-query endpoint envelope rather than repeating marker cycles.',
'deliverable_status':'COMPLETE_LOCAL_ARTIFACTS_SAVED_PENDING_SUPERVISOR_COPY',
'mathematical_status':'SCOPED_THEOREM_PROVED_BY_AUTHOR_EXACTLY_CHECKED; FULL_FEI_OPEN; INDEPENDENT_PEER_REVIEW_PENDING',
'claim_versions_used':[{'claim_id':'A035-ALL-QUERY-TERMINAL-KL-ENVELOPE','version':1}, {'claim_id':'A031-RETAINED-MARKER-EXPOSURE-SAME-ORIGINAL-BANK','version':1}],
'claims_created_or_changed':[{'claim_id':claim_id,'version':1}],
'source_artifacts':['DERIVATION.md','CLAIMS.json','out/CHECK.json','out/REPRODUCE.json','out/GHOST_CHECK.json','out/GHOST_REPRODUCE.json','out/REVIEW_A035.json','out/SOURCE_RECEIPTS.json'],
'next_consumers':['B07 Claude lead','A035','A096','A097'],
'next_action':'Obtain a reference class actually forced by the surviving universal route; apply the sharp full-law minimum, including ghost capacity, and compare its cumulative price to one unused original source budget.',
'stagnant_substantive_attempts':0,
'blockers':['Universal mandatory admissible class and arbitrary-core initial source remain unproved.', 'Same-author independent implementation is not external peer review.', 'Personal brain self-care degraded/unverified: model98h, state82.6h, dream33.3h stale at wake; not mathematical premises.'],
'packet_ids':['A031']}
jsave(RUN/'PROGRESS.json',progress)
jsave(RUN/'PACKET_DELTA.json',progress)
report=f'''# A031 stage20: sharp compatible-reference ghost capacity

## exact target, quantifiers, hypotheses and units

For arbitrary finite retained laws, solve the compatible full-reference profile-conversion problem exactly; then apply its zero-cost sector to actual signed Boolean queries. Logs and entropy are in bits, Walsh coefficients use the uniform cube. Both children, every reference-only atom, original reaches and source debits are retained. This is a reference-transfer theorem, not initial Boolean source admission. Full FEI remains OPEN. The exact theorem and hypotheses are in CLAIMS.json and DERIVATION sections4-4a.

## sources actually read, revisions and theorem locators

Current BOARD header 2026-10-23 11:24 UTC; B07 STREAM_NOTES v2; own stage19 STATUS/LEARNED and exact helper; execution protocol v2. Consumed A035 run20261023T110610Z DERIVATION/REPORT/CLAIMS: ALL-QUERY-TERMINAL-KL-ENVELOPE v1 already closes our prior NEXT. Read A097 run20261023T062140Z DERIVATION on calibrated coherent wrappers and the isospectral nullspace. Current source hashes are in out/SOURCE_RECEIPTS.json; no new theorem is attributed to the older threshold/percolation papers. Earlier source orientation is inherited, not claimed a fresh paper audit.

## complete derivation or exact first unsupported line

DERIVATION sections1-6 give the complete proof. Parameterize compatible children as q(s)(1+/-t(s)); their average CE increment is -(1/2) sum p(s)log2(1-t(s)^2). Within block z the required shift is Delta_z. Reference-only cells carry g_z mass at zero objective. Hence the minimum is zero exactly when |Delta_z|<=g_z in every block. Beyond capacity, ghost tilts saturate; strict convexity and an explicit multiplier solve the occupied part. A supporting-hyperplane certificate proves global optimality. Matching occupied-block conditionals gives the closed block logarithm; an exact negative control shows that assumption cannot be dropped. Formulae are generic probability geometry, not a new Boolean-admission inequality.

The explicit parity4 example has a proper nonempty profile change at zero complete CE cost. Its full signed convolution is checked. The proof extends to every coherent controller a+sigma*(1-a^2)*parity4, arbitrary controller dimension, with a supplied complete inherited reference. An opposite prescribed-profile example has arbitrarily large necessary conditional cost on the same fixed Boolean function; that class is explicitly imposed, not asserted necessary for FEI. No FEI counterexample is claimed.

First unsupported universal line: {first}

## executed validation with domain, arithmetic, commands and outputs

All commands below run from this run directory using python -X utf8. Frozen specs were saved before each search. No automatic dimension increase, no floating proof, no GPU, no heavy job. Peak estimates below100 MB; the fresh memok receipt permitted memory but no Lean/heavy job was started.

* code/check_calibration.py pilot:87 matched-profile cases,2780 checks,1.636s. Main:285 cases,8922 checks,1.641s; exact Fraction log intervals with28-term atanh and outward2^-256 rounding. out/PILOT.json and out/CHECK.json.
* code/reproduce.py:285 exact rational cleared-log product cases plus1080 retained-marker complete query/stop policy states;15167 checks,3.705s. Also reconstructs original-source endpoint comparison and actual L64 five-bit uniform-reference obstruction. out/REPRODUCE.json and out/REVIEW_A035.json.
* code/check_ghost.py pilot:8 exact KKT certificates,233 checks. Main:75 rational primal/dual certificates,15 exact zero-capacity boundaries and actual parity reference normalization;1238 checks,0.569s. out/GHOST_PILOT.json and out/GHOST_CHECK.json.
* code/reproduce_ghost.py:25126 checks,1.565s;75 exact rational dual fixtures,15 zero-capacity fixtures, all162 ternary two-controller-bit/sign wrappers (130 active seed queries), direct truth-table Walsh transforms and signed convolution, full ghost normalization and the negative control for mismatched conditionals. out/GHOST_REPRODUCE.json. This independent implementation is by the same author, not independent peer review.

Two attempted read commands and one reproduction launch initially used the agent root as cwd and failed before accessing run-local inputs; corrected commands explicitly used this run directory. No failed launch is counted as validation. No formal Lean check is claimed; the logarithmic convexity proof is analytic and its finite certificates are exact.

## proof dependencies and changed downstream conclusions

The sharp optimizer depends on elementary CE/KL and convexity, proved locally. Actual Boolean examples depend on full signed Walsh child identities, checked directly. Preserve signs through actual-child cancellation: isospectrality makes every u_T*v_T zero before concluding zero phase energy; reference-only mass then pays the normalization shift. New result closes the supplied-reference ghost-capacity sector of C024, including arbitrary coherent controllers. It does not supply initial CE. A035's all-query full-terminal-KL envelope is accepted at its stated supplied-source scope, independently reconstructing the endpoint comparison and finite policies; its strengthened source itself was originally A031's, so this is not relabeled full-chain independent review. Its unbounded terminal-KL limitation remains.

## one next mathematical action and independent reviewer

Ask B07/A096/A097 to instantiate the actual admissible reference constraints of their surviving universal route. Compute this theorem's infimum with all reference-only capacities, then pay only any unavoidable occupied cost from the single unused source budget. Independent reviewer requested: B07 Claude lead or A035; none has reviewed the new claim yet. Another expensive arbitrary profile or bounded marker cycle does not address necessity.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, DERIVATION.md, scripts, frozen specs and exact receipts saved locally. out/MANIFEST.json records artifact hashes; out/READBACK.json records actual final validation. STATUS.md has two lines, WORKLOG.md appended, LEARNED.md updated. Supervisor copy/publication is outside this packet and remains pending. No shared tree, brain store, other agent folder or git state was mutated. Personal brain self-care is degraded/unverified: fresh wake reported model98h, state82.6h and dream33.3h stale; personal continuity/context freshness is affected and is not used as a mathematical premise. Compute-governor state was stale and not restarted; all actual finite jobs completed within their frozen low-memory limits.

**Universal bridge:** C024 moves from an undifferentiated isospectral conversion obstruction to an exact zero-cost iff reference-only-capacity criterion and an explicit occupied-cell optimizer, with a zero-cost construction for every coherent Boolean controller. C019 retains the same-ancestor rule: cumulative conversion is a full-KL endpoint difference and cannot renew the source. What remains is a reference class forced by a universal proof and an actual initial or unused source paying its occupied minimum. Obtaining that class is the shortest route to full FEI because it tests necessary universal expenditure directly, rather than collecting another isolated class or arbitrary expensive reference.
'''
save(RUN/'REPORT.md',report)
save(RUN/'out/CHECKPOINT.md',f'''Stage20 finished locally {stamp}. Sharp generic reference optimization proved; exact zero iff |Delta_z|<=reference-only capacity g_z, explicit unique occupied optimizer beyond. Matching-conditionals corollary and negative control checked. Actual free profile change extends to all coherent controllers. Exact checks:8922 primary,15167 reproduction,1238 ghost,25126 independent ghost. A035 all-query terminal-KL envelope consumed and reviewed at supplied-source scope. Full FEI, universal mandatory class and initial source remain open; new theorem pending peer review. NEXT: instantiate mandatory constraints from B07/A096/A097 and charge only their exact minimum against one original source.\n''')
save(AGENT/'STATUS.md', 'STATE: Stage20 sharp compatible-reference ghost-capacity theorem proved and exactly checked; all coherent controllers inherit zero-cost sector; full FEI open, peer review pending.\nNEXT: Obtain the universal route\'s mandatory reference class from B07/A096/A097; compare its exact occupied minimum to one unused original source budget.\n')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n2026-10-23 11:31 UTC stage20 ({stamp} saved): consumed A035 all-query full-KL envelope and A097 matching nullspace. Proved sharp general full-mean compatible-profile optimizer and zero iff ghost capacity suffices; matched-conditionals logarithm needs its hypothesis (exact negative control). Proved actual free nonempty profile change for all coherent controllers. Exact independent reproduction25126 checks includes162 wrappers; primary8922, first reproduction15167 and ghost1238 pass. Full FEI/initial source and mandatory universal constraints remain open. Saved {run_id}; no shared mutation; peer review and supervisor copy pending.\n')
learned=read(AGENT/'LEARNED.md')
learned+='''\n## Stage20 (2026-10-23): sharp compatible-profile conversion with ghosts
For finite p,q and prescribed profiles r+/r- averaging pi(q), compatible complete references have Rtau(s)=q(s)(1+tau*t(s)), block constraint sum_z q*t=Delta_z. Mean CE increment is -(1/2)sum_{p>0}p log2(1-t^2). Minimum zero iff |Delta_z|<=g_z=sum_{p=0,in z}q. Ghosts are the exact capacity; deleting them loses the result. Beyond capacity saturate ghost tilts and solve p*t/(1-t^2)=lambda*q on occupied cells; strict convexity plus supporting hyperplane proves optimality. Simple block formula -(1/2)sum P_z log2(1-eta_z^2) requires matching p/q conditionals in occupied blocks; counterexample without match is exact. In parity4, qbar(1,2,7)=(1/2,1/4,1/4), bins{1},{2,7}, R+=(5/8,1/8,1/4), R-=(3/8,3/8,1/4) have changed nonempty profiles but zero cost and full compatibility. Extends algebraically to every a+sigma*(1-a^2)*parity4 coherent controller; requires a supplied initial reference. No necessary universal positive price follows from one expensive arbitrary target. NEXT must specify the universal route's actual admissible class and pay its infimum from one original source, not renew bank. Source: stage20 DERIVATION; independent exact implementation25126 checks/162 wrappers, external peer review pending.\n'''
save(AGENT/'LEARNED.md',learned)
manifest=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name not in ('MANIFEST.json','READBACK.json') and '__pycache__' not in p.parts:
  assert p.stat().st_size<20_000_000
  manifest.append({'path':p.relative_to(RUN).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())})
jsave(RUN/'out/MANIFEST.json',{'created_utc':stamp,'artifacts':manifest})
print(json.dumps({'saved':run_id,'claim':claim_id,'artifacts':len(manifest),'pending':'Run independent readback; external peer review and supervisor copy.'}))
