from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
RUN=Path(__file__).resolve().parents[1]; AGENT=RUN.parents[1]
def readj(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def writej(path,obj):path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
v=readj(RUN/'out'/'validation.json');r=readj(RUN/'out'/'review_validation.json');lean=readj(RUN/'out'/'lean_receipt.json')
assert v['status']==r['status']=='PASS'
now=datetime.now(timezone.utc).isoformat()
protocol=readj(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
statement='For every Boolean F(X,Y) on disjoint independent uniform physical cubes, if F=sum_J chi_J(X)u_J(Y), each u_J is the sum of at most two quadratic F2 phases on disjoint affine Y cells, and all row cells partition Y, then H(S_Y|S_X)<=24 I_Y(F) and H(F)<=24 I_Y(F). The class is stable under all Y coordinate restrictions, includes every single X-coordinate restriction of distinct-label quadratic affine partitions, and any fresh Boolean Y tensor factor has F2 degree at most three. No closure under arbitrary further X collisions is asserted.'
claim={
'claim_id':'A034-TWO-CELL-QUADRATIC-COLLISION','version':1,'exact_statement':statement,
'hypotheses':['Boolean signs; uniform independent physical X,Y cubes','At most two disjoint affine quadratic cells per X-frequency row; cells across all rows partition Y','Entropy in bits; influence in original physical coordinates','Optional X degree at most any integer d>=1; no spectral independence assumed'],
'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A034; credit A033 for bounded F2 phase-degree baseline and A079 for earlier full-cube quadratic collision'],
'proof_source':'PROOF.md','proof_dependencies':[], 'review_records':[],
'status':'AUTHOR_PROOF_EXACT_VALIDATION_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],
'first_unproved_line':'For unrestricted further X collisions, no dimension-independent payment is proved for rows with unboundedly many affine components. The coherent entropy factor and simultaneous cancellation remain unpaid.',
'next_consumers':['A032','A033','A079','A088','A094']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
writej(RUN/'CLAIMS.json',[claim])
progress={
'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B07','packet_id':'A034','gap_id':'G-PHASE-COND','attempt_id':'A034-one-collision-two-affine-cells-v1',
'method':'Signed affine-translation energy protection, generic coherent entropy domination, exceptional cubic gluing, exact complete-row ledger; independent reconstruction of A033 all-C no-go',
'mathematical_delta':'One X collision of arbitrary quadratic affine cells now has complete conditional/joint rate24, unequal support allowed; parallel cells retain rate4. Y-restriction stability and degree-three fresh-tensor guard proved. Arbitrary repeated collisions and full FEI remain open.',
'deliverable_status':'COMPLETE_LOCAL_SOURCE_AND_VALIDATION','mathematical_status':'RESTRICTED_AUTHOR_PROOF_PENDING_INDEPENDENT_REVIEW_FULL_FEI_OPEN',
'claim_versions_used':['A034 quadratic-affine baseline reconstructed in PROOF.md section1','A033 bounded-phase-degree baseline reconstructed in PROOF.md section5','A033 stage17 all-C fixed-controller no-go independently reconstructed in REVIEW_A033.md'],
'claims_created_or_changed':['A034-TWO-CELL-QUADRATIC-COLLISION@1'],
'source_artifacts':['PROOF.md','REVIEW_A033.md','FROZEN_SPEC.json','FROZEN_REVIEW_SPEC.json','code/check.py','code/review_check.py','code/formal_check.py','out/validation.json','out/review_validation.json','out/lean_receipt.json','out/source_receipts.json','out/source_extracts.json'],
'next_consumers':['A032','A033','A079','A088','A094'],
'next_action':'A079/A033 independently review the geometric1/3 bound and parallel exception; then price one further X collision of four inherited components using the same physical energy and complete terminals, without renewing the reserve.',
'stagnant_substantive_attempts':0,
'blockers':['Full FEI remains OPEN','No independent acceptance of new theorem or supervisor mirror receipt','Lean key-step attempt held by compute admission; no compiler launched, no formal certificate'],
'packet_ids':['A034']}
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
writej(RUN/'PROGRESS.json',progress);writej(RUN/'PACKET_DELTA.json',progress)
report=f'''# A034: complete entropy after one affine quadratic-row collision

## exact target, quantifiers, hypotheses and units

For every Boolean F on independent uniform physical cubes X,Y, assume its X-frequency rows are unit quadratic F2 signs on at most TWO disjoint affine Y cells each, with the cells across all rows partitioning Y. The X-degree can be bounded by any integer d>=1; constants are independent of d and both dimensions. In bits, H(S_Y|S_X)<=24 I_Y and H(F)<=24 I_Y<=24 I. Every physical Y restriction preserves admission. Every one-coordinate X restriction of the accepted distinct-label quadratic affine partition class is admitted. Fresh Boolean tensor factors must have F2 phase degree<=3; arbitrary factors are excluded. This is an author proof with exact finite validation, pending independent review. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read the complete execution protocol revision {protocol['revision']}; campaign README/CURRENT_STATUS, claim/obstruction/packet/next-action records at A034/B07/G-PHASE-COND, plan phase section and A034 acceptance contract; supplement CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and relevant curated source locators. Thirty-one required files were loaded and hashed by code/sources.py, with selected locators retained in out/source_extracts.json; this does not claim every paper page was reconstructed. Threshold38pp Proposition8.1/Corollary8.2 identify the affine-selector baseline. Both percolation versions' introductions explicitly retain their restricted scope. The four .txt papers decode as cp1252, recorded rather than misreported as corrupted UTF-8. The current owner deadline23October14:49UTC supersedes historical21October metadata, without restarting a clock.

Read BOARD.md supervisor snapshot22October22:17UTC, B07 STREAM_NOTES v2, own rolling files and substantive earlier reports, A033/A079 LEARNED and latest source scopes. A079's independently reconstructed all-product acceptance retires the old bounded-nonfair endpoint. A032's product-branch mass rigidity and A079's arbitrary-seed complement obstruction prohibit reopening the unequal-two-product Boolean split. A033 stage17 NO_GO.md was read in full and independently reconstructed in REVIEW_A033.md. One math-brain search with three wordings supplied only baseline/control context, not a proof premise. Brain wake completed with stale owner-model/state warnings, alerted in conversation; no affected stale note is used as authority.

## complete derivation or exact first unsupported line

PROOF.md gives the complete finite-sum derivation. Each quadratic affine component has flat normalized spectrum and alpha H<=2E, alpha log(1/alpha)<=2E. For disjoint components a,b, P_(a+b)<=2Q for the actual mixture Q, so KL positivity gives mu H(P_(a+b))<=2[alpha H(P_a)+beta H(P_b)+mu h2(alpha/mu)]. The generic inequality is explicitly separated from the Boolean geometric input.

For a physical coordinate crossing two affine supports, both component boundary energies sum to(alpha+beta)/2 and the signed correlation is at most their affine intersection mass gamma. If the supports have unequal dyadic masses, gamma<=(alpha+beta)/3. For equal masses but different directions, gamma<=(alpha+beta)/4. Thus E(a+b)>=(E(a)+E(b))/3 outside the parallel exception. Two parallel cells instead unite into an affine cubic phase; its tangent nonzero influences are>=1/4 by the F2 minimum-weight induction. The exact address+conditional row bill then pays at4.

For other pairs, mu h2(alpha/mu)=alpha log(1/alpha)+beta log(1/beta)-mu log(1/mu). Retaining this signed identity bounds the COMPLETE row bill by8(E(a)+E(b))<=24E(a+b). Summation over actual X-frequency rows is precisely the Fourier entropy chain rule, with I_Y=sum E(row). All conditional entropy, both component terminals and one physical energy account are retained. No generic all-phase Renyi bound or renewed controller bank is used.

Restriction and fresh-factor arguments are proved in sections6--7. Fixing old physical data in a nonzero tensor row leaves a Boolean fresh factor covered by at most two quadratic affine cells. The only two nonempty affine cells partitioning a whole cube are complementary halfcubes, hence the factor is cubic. A quartic monomial phase is excluded. The three-bit point defect is admitted and has nonproduct spectrum, testing vacuous embeddings. The non-Boolean normalized singleton vector psi_N violates24 for N>2^24, and fails the unit-cell/F2 hypotheses.

First unsupported universal line: an unrestricted second or later X collision can create four or more components; the entropy mixture factor and simultaneous cross cancellations have no dimension-independent payment here. The result is a terminal bound after ONE collision, not a reusable universal erasure charge. No full-FEI conclusion follows.

REVIEW_A033.md independently accepts the all-finite-C fixed-controller reserve obstruction at selector-only histories, without supplying a repair: chi-square4/(2^m-1) bounds midpoint entropy loss, Delta_z H-Cdelta>delta(m-C-4/ln2)>0 for even m>=C+6, while H<=3I. Tensor copies make that spend unbounded with all g/h terminals retained. Protected outer-tag scaling requires beta>0; tag queries themselves are outside this review.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the exhaustive checker. Command: python -X utf8 runs/{RUN.name}/code/check.py. The final checker passes {v['checks']} exact assertions in {v['runtime_seconds']:.3f}s. Exhaustive domains n=0,1,2,3 contain signed affine-quadratic row counts2,8,48,480 and disjoint unordered pair counts0,4,168,13776. It checks integer Walsh versus physical-edge energies independently, actual row norms, coherent domination, cancellation protection, complete and conditional entropy bounds, parallel cubic gluing and coordinate-restricted supports. Entropy comparisons use cached rational logarithm enclosures, 18 atanh terms and an explicit positive remainder. No floating comparison establishes a sign. n=4 has only the frozen quartic guard fixture, not an exhaustive claim.

The countertest applying the geometric1/3 estimate to parallel cells FAILS as required (same-sign complementary cells can cancel all energy). The valid unequal/nonparallel bound attains equality1/3 in the frozen finite domain; an actual signed witness is saved. The cubic point defect has squared masses9/16,1/16,... and is checked nonproduct. A second independent representation is physical edge sums versus integer spectral degree sums. An added validation pass broadened checks to this independent energy equality and the explicit full conditional bill; it changed the assertion count from246561 to{v['checks']} without changing the dimension or family.

FROZEN_REVIEW_SPEC.json precedes code/review_check.py. Its four actual bent/flip/splice dimensions2,4,6,8 pass {r['checks']} exact assertions in {r['runtime_seconds']:.3f}s, including chi-square and true influence. This is finite validation of the analytic all-C proof, not evidence of an FEI counterfamily.

The Lean key-step source code/Energy.lean states only the scaled integer cancellation implication3c<=a+b => a+b<=3(a+b-2c). code/formal_check.py requests a named-target/source-hash/axiom receipt through lean_check.check_source, with all scratch inside this run and timeout45s. Compute admission held below its5500MB start floor; no compiler launched and out/lean_receipt.json is RUNTIME_UNVERIFIED. Thus no part is called Lean-certified. memok immediately beforehand exited0 (4.9GB physical free,23.0GB commit free); this is its lower pilot threshold, not a contradictory Lean admission. Small checkers were estimated under90MB; no heavy job/GPU/background process launched.

An attempted cmd-shell one-liner had a quoting SyntaxError and was abandoned; no mathematical result depends on it. A UTF-8 acknowledgment gate held a read-only command; the rerun retained explicit UTF-8 reads. A guessed interventions.jsonl path did not exist; the actual interventions.tsv was subsequently read. These access/runtime errors are not theorem counterexamples or successful certificates.

## proof dependencies and changed downstream conclusions

The new proof is self-contained finite Fourier algebra, binary affine geometry, entropy grouping/KL/subadditivity, and the elementary F2 minimum-weight induction. It reconstructs the earlier quadratic interface and A033 bounded-degree endpoint rather than assuming unreviewed claims. Credit A079 for the earlier sharp common-full-cube two-quadratic collision; this result extends support geometry to arbitrary disjoint unequal cells with a weaker constant, not a new sharp cubic result or novelty assertion. The invalid coupled-gcd clause remains withdrawn and is unused.

A032/A033/A079 can use this as a complete terminal after one affine quadratic-row collision and every subsequent Y restriction. They cannot infer unrestricted X heredity, arbitrary tensor seeds, a constant renewed at every collision, or full FEI. The A033 no-go gets an independent source-bound reconstruction; registry adoption, independent acceptance of the NEW theorem and mirror ingestion remain unverified. No shared registry was changed.

## one next mathematical action and independent reviewer

A079/A033 should reconstruct the1/3 translation estimate, the exceptional parallel cubic gluing and the joint entropy cancellation independently; A088/A094 should audit the row partition and tensor guard. Next mathematical action: price one further X collision of FOUR inherited affine components with complete terminals and the SAME physical energy, identifying which simultaneous cross terms retain protection; do not introduce another fixed controller-only reserve. This directly addresses the first loss of stability of the proved interface.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved, with exact protocol field sets and statement SHA256 verified by code/finalize.py. PROOF.md, REVIEW_A033.md, two frozen specs, code and exact outputs are saved. STATUS.md has exactly two lines; WORKLOG.md and LEARNED.md are appended. out/ARTIFACT_RECEIPTS.json pins file hashes and sizes. Local persistence is checked; supervisor copies, Brain ingestion, GitHub mirroring, independent acceptance and public release are not asserted. All task artifacts remain inside A034. No git, mail, external message, brain write, other-agent mutation, trading action, remote compute or destructive operation occurred. Required brain wake is the session initialization mandated by the developer, not a task artifact save.

## Universal bridge

This stage moves B07's G-PHASE-COND bridge toward C018 by paying the FULL conditional and joint entropy through the first previously unpaid X collision of quadratic affine rows, including unequal supports, at a dimension-independent rate24 and rate4 in the parallel case. It supplies Y stability and a proved cubic-only tensor guard; it does not resolve C018 or full FEI. What remains is the unbounded collision layer: four or more inherited cells can have several simultaneous cancellations. NEXT addresses the very next failure of stability using the same complete row ledger and physical owner, which is closer to a universal restriction mechanism than repeating product-row endpoints or hiding arbitrary seed entropy in a controller reserve.
'''
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
status='STATE: A034 stage17 saved: one affine quadratic-row X collision, unequal cells allowed, FULL H_cond and H<=24I_Y; parallel rate4; exact checks PASS; A033 no-go independently HOLDS; review pending, FEI OPEN.\nNEXT: A079/A033/A088/A094 review geometry/tensor guard; pay one further four-component X collision from SAME physical energy with full terminals; no reserve renewal.\n'
(AGENT/'STATUS.md').write_text(status,encoding='utf-8')
log=f'\n{now} - A034 stage17: read board/lead/protocol and current A033/A079 scopes; proved two-cell complete conditional/joint rate24, parallel4, Y restriction stability and cubic tensor guard. {v["checks"]} exact main assertions and{r["checks"]} independent A033 reconstruction checks PASS. Lean admission HELD; no certificate or compiler. Full FEI OPEN; four-component repeated collision is next. All artifacts local; no background work launched.\n'
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write(log)
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} - ONE-COLLISION EXTENSION (author proof, independent review pending): If actual X-frequency rows are sums of at most two quadratic phases on disjoint affine physical Y cells, and all cells partition Y, then H(S_Y|S_X)<=24I_Y and full H<=24I_Y. Translation overlap gamma protects >=1/3 of component energy for unequal dyadic cells, >=1/2 for equal nonparallel cells. Parallel equal cells MUST be treated separately: union is affine cubic, joint row rate4; generic energy comparison fails at complementary equal signs. Coherent P<=2Q plus exact mu*h(lambda)=alpha*kA+beta*kB-mu*log(1/mu) pays full joint row without discarding terminal entropy. All Y restrictions preserve admission; ONE X restriction of accepted quadratic-affine partition is covered. Fresh Boolean tensor seeds have F2 degree<=3, so quartic phase excluded; spectral product structure is NOT required. {v["checks"]} exact finite checks PASS, including genuine nonproduct cubic and negative parallel control. Arbitrary further X collisions remain unpaid; do not renew rate24 as an erasure bank. A033 all-C fixed-controller no-go independently HOLDS at selector-only histories (REVIEW_A033.md), retaining all terminals; no universal FEI result or new Lean certificate.\n')
receipts=[]
for p in sorted(RUN.rglob('*')):
 if p.is_file() and p.name!='ARTIFACT_RECEIPTS.json':
  data=p.read_bytes(); assert len(data)<20*1024*1024
  receipts.append({'path':str(p.relative_to(RUN)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
assert (RUN/'PACKET_DELTA.json').read_bytes()==(RUN/'PROGRESS.json').read_bytes()
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
writej(RUN/'out'/'ARTIFACT_RECEIPTS.json',{'saved_at_utc':now,'files':receipts,'protocol_field_sets_checked':True,'statement_hash_checked':True,'external_mirror':'UNVERIFIED','lean':'RUNTIME_UNVERIFIED'})
print(json.dumps({'status':'LOCAL_ARTIFACTS_VALIDATED','files':len(receipts),'checks':v['checks'],'review_checks':r['checks'],'run':str(RUN),'saved_at_utc':now}))
