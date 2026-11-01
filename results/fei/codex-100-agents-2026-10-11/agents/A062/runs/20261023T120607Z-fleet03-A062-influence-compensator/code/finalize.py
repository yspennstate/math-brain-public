from pathlib import Path
import json, hashlib, datetime

run=Path(__file__).resolve().parents[1]
agent=run.parents[1]
proto=json.loads(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
checks=json.loads((run/'out/checks.json').read_text(encoding='utf-8'))
assert checks['status']=='PASS'
statement=('For every finite subset law p with all actual coordinate marginals strictly between zero and one, actual marginal product Q, and partition into nonempty blocks with p_j(empty)>=Q_j(empty), let Z record occupied blocks. If R(S)=r(Z) times the product, over occupied blocks, of Q_j conditional on nonempty tilted by lambda_j^rank and normalized, where 0<lambda_j<=1 and r supports p_Z, then TC(p)-KL(p||R)<=TC(p_Z)+log2(e)I(p)-KL(p_Z||r). The occupancy correction cannot be bounded by c I from local eligibility alone: for every k>=2 the actual 2k-bit point-function spectrum with consecutive pair blocks admits the supporting reference R(S)=p_Z(Z)Q(S|Z), all lambda_j=1, all blocks eligible, and both C_p(R)/I and [TC(p)-KL(p||R)]_+/I exceed 3k/2-9/2-1/(2k). These references are constructed, not certified descendants of an original product reference.')
claim={
 'claim_id':'A062-OCCUPANCY-COUPLING-OBSTRUCTION','version':1,'exact_statement':statement,
 'hypotheses':['Bits; finite distributions; 0<d_i<1; supporting references; occupied-block rank tilts independent given Z; stated empty dominance. The obstruction has strictly positive probabilities throughout.','No original-product-root reachability asserted. No full-FEI claim.'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A062'],
 'proof_source':str(run/'PROOF.md'),'proof_dependencies':['Elementary entropy/KL chain rule','A062-SPARSE-SIGNED-REFERENCE-ENVELOPE@2, local rank-mean mechanism independently restated in this proof'],
 'review_records':[],'status':'PROVED_PENDING_INDEPENDENT_REVIEW','supersedes':[],
 'refutes':['Unregistered extension of block-product projection to arbitrary coupled references based only on eligible block marginals'],
 'first_unproved_line':'Hereditary control of occupancy/reference coupling for references actually transported from the original product root, paid by the SAME unused original owner after query charges and old debits.',
 'next_consumers':['A061','A064','A065','A087','A094','B13']}
(run/'CLAIMS.json').write_text(json.dumps([claim],indent=2)+'\n',encoding='utf-8')
progress={
 'protocol_revision':proto['revision'],'run_id':run.name,'stream':'B13','packet_id':'A062',
 'gap_id':'C019-HEREDITARY-SIGNED-REFERENCE-COUPLING','attempt_id':'A062-stage20-sector-occupancy',
 'method':'Exact sector likelihood decomposition, rank exponential-family monotonicity, all-dimensional actual point-source obstruction; independent direct Walsh/Fraction checks and rigorous logarithm intervals.',
 'mathematical_delta':'Separates coupling failure from local eligibility loss: every two-coordinate block is eligible at lambda=1 yet the coupling/reset liability divided by influence is unbounded. Proves the corrected occupancy-divergence projection inequality; product-reference theorem survives. Independently reconstructs A061 stage20 section0 for core-prefix-then-pivot immediate stops only.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'NARROW_INTERFACE_OBSTRUCTION_PROVED; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A062-SPARSE-SIGNED-REFERENCE-ENVELOPE@2','A061 stage20 PROOF section0 scoped reconstruction; field bundle not accepted','A065 stage19 PROOF fixed-root mixture obstruction consumed; not independently accepted'],
 'claims_created_or_changed':['A062-OCCUPANCY-COUPLING-OBSTRUCTION@1'],
 'source_artifacts':['PROOF.md','FROZEN_SPEC.json','code/check.py','out/checks.json','out/receipts.json'],
 'next_consumers':['A061','A064','A065','A087','A094','B13'],
 'next_action':'On A065 actual fixed two-module product-root history, query one ordinary coordinate after a selector and compute the occupancy law and conditional-within-sector reference defect; bound or refute their combined change against the SAME original unused owner. Do not test arbitrary supplied references again.',
 'stagnant_substantive_attempts':0,
 'blockers':['General inherited-reference admissibility and coupling funding remain open. Constructed R is not an actual root-history certificate.','Independent review by A087/A094 pending.','Brain self-care degraded/unverified: stale owner-model, state-of-mind and latest dream; personalized guidance and recent consolidation not used as proof premises.'],
 'packet_ids':['A062']}
for name in ['PROGRESS.json','PACKET_DELTA.json']:
    (run/name).write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')
head=proto['required_per_run']['report_fields']
texts=[
 'Target: C019 signed inherited-reference payment, in bits. This stage proves a general occupancy-corrected projection inequality and refutes the stronger current-local-eligibility-only extension by actual Boolean point spectra for all k>=2. The reference is constructed. Its original-root reachability is NOT claimed. The assignment finite-tree influence telescope, randomized stopping, and qualified Fatou passage remain as already saved in earlier stages; no limiting argument is invoked here.',
 'Read current EXECUTION_PROTOCOL.json (2026-10-11-execution-v2), machine AGENTS.md applicable rules, own STATUS/LEARNED and prior stage19 proof mechanism, BOARD 2026-10-23 12:16 UTC in bounded sections, and B13 STREAM_NOTES v2. New mathematical sources actually consumed: A061 runs/20261023T113614Z-fleet03-A061-entropy-process/PROOF.md, especially section0 and the ordinary-prefix obstruction; A065 runs/20261023T112150Z-fleet03-A065-stopping-rule-falsifier/PROOF.md, especially sections3-7; A087 runs/20261023T061410Z-fleet03-A087-restriction-referee/PROOF.md. Baseline papers and campaign material were consumed in prior stages, not newly reread. Source revisions are recorded by hashes below. The lead direction is followed: retain full terminal entropy and the original owner.',
 'Complete derivation is in PROOF.md sections1-4: sector factorization, corrected inequality TC-K<=TC(p_Z)+aI-KL(p_Z||r), actual point-family spectrum, every local lambda=1 eligibility, and linear lower bound (TC-K)/I >= C_p(R)/I >3k/2-9/2-1/(2k). Section5 independently reconstructs only A061 core-prefix/pivot/immediate-stop reduction, including source-zero reference mass. First unsupported universal line: the same costs for ACTUALLY REACHABLE original-root references are payable by the original still-unused owner. No terminal entropy payment, second reset, arbitrary post-pivot equivalence, or FEI conclusion is inferred.',
 f'Frozen spec precedes computation. Executed python -B -X utf8 {run / "code/check.py"}. Output: PASS, {checks["assertions"]} exact assertions in {checks["runtime_seconds"]:.3f} seconds measured inside the job. Full independent Walsh truth tables n=4,6,8; six explicitly frozen compressed cases k=2,3,4,8,16,32. Rational probabilities, exact physical influences, reference normalization and block eligibility; entropy/KL identities enclosed by atanh-series rational log intervals with proved remainder and outward dyadic rounding. Falsification controls replace R by product of its actual block marginals: coupling must disappear and the influence bound return; the old R=p shortcut must fail the lambda=1 condition. Jobs estimated below45MB, so no >300MB job or memok requirement was triggered. No floating-point result is used as proof. out/checks.json contains certificates.',
 'Dependencies are elementary finite entropy algebra and the previous local rank monotonicity argument, fully restated here. The prior block-product theorem is unchanged. A087 arbitrary-reference obstruction is sharpened to simultaneous eligibility of every nontrivial block. A061 scoped reduction is independently accepted by a different factor/zero-row reconstruction; its complete field-family theorem is not accepted here. New theorem and obstruction await external review. Owner funding for arbitrary coupled references is now ruled out under local eligibility alone; original-root/history restrictions are essential.',
 progress['next_action']+' Independent reviewers: A087 and A094. This is a mathematical handoff in local artifacts; no messages sent or shared indices modified.',
 'Saved in this immutable run: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, PROOF.md, FROZEN_SPEC.json, code/check.py, out/checks.json and out/receipts.json. Rolling STATUS.md, WORKLOG.md and LEARNED.md updated locally. Receipts record file SHA256 and byte counts. No GitHub/mirror persistence is claimed; supervisor copies completed runs. Did: proved corrected projection and all-k local-eligibility obstruction. Stopped: this finite declared stage after checks. Left running: no research job.'
]
texts[3]+=' The first pilot emitted no success certificate: its 56-bit mantissa enclosure could not certify the compressed bound. out/pilot_failure.json preserves that failure; the successful rerun retained 128 bits without changing any family or dimension. Freshly read compute-state data were a timestamped snapshot, not a new health guarantee; no running work was stopped or throttled.'
report='# A062 stage20: occupancy coupling survives local eligibility\n\n'
for h,t in zip(head,texts): report+='## '+h+'\n\n'+t+'\n\n'
report+='**Universal bridge:** C019 stopping-tree payment moves by isolating a necessary missing cost: reference-sector coupling can be unbounded per influence even while every block projection remains eligible; the exact occupancy-divergence correction is retained. What remains is its hereditary payment or avoidance for references actually reached from one original product root, with old debits, query influence, K/E/O and full terminal H retained. The NEXT ordinary query on A065\'s fixed root is the shortest route because it tests the surviving history restriction rather than another arbitrary-reference family or isolated FEI class.\n'
(run/'REPORT.md').write_text(report,encoding='utf-8')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(agent/'STATUS.md').write_text('STATE: A062 stage20: all-block eligibility does NOT fund coupling; actual point family C/I>3k/2-9/2-1/(2k); corrected occupancy projection proved; '+str(checks['assertions'])+' checks PASS; review pending; FEI OPEN.\nNEXT: Measure occupancy plus within-sector defect after A065 ordinary post-selector query at SAME original product root; retain old owner/debits/full H; A087/A094 review.\n',encoding='utf-8')
for name,content in [
 ('WORKLOG.md',f'\n{now} stage20: consumed A061 prefix and A065 fixed-root coupling; changed mechanism to occupancy sectors. Proved corrected TC-K inequality; actual point spectra with eligible two-bit blocks refute local-only coupling price for all k. Checked {checks["assertions"]} exact assertions, including product-reference and R=p falsification controls. Arbitrary constructed references do not establish root-history reachability. Scoped A061 core-prefix/pivot reduction independently reconstructed. Saved complete run; FEI open.\n'),
 ('LEARNED.md','\nStage20: For a block-sector reference R=r(Z) times independent occupied-block rank tilts of actual Q_j with lambda_j<=1 and source empty dominance, TC(p)-KL(p||R)<=TC(p_Z)+log2(e)I-KL(p_Z||r). At lambda1 and r=p_Z, T=KL(p_Z||q_Z), coupling=TC(p_Z), localT_j=binaryKL. Actual point on2k bits, pair blocks, d=2^(1-2k), P(Zj=1)=3d/2, pZ(0)=(1-d)^2, pZ(z)=d^2*3^rank, has EVERY local block eligible but C/I>3k/2-9/2-1/(2k). Thus loss of local eligibility is not needed for coupling failure; product reference cancels occupancyTC via KL, arbitrary coupling can remove that cancellation. Constructed R is not certified inherited from its point-product root. Root-history eligibility is the surviving target. Full H/I of this source remains bounded; no FEI counterexample.\n')]:
    with (agent/name).open('a',encoding='utf-8') as f: f.write(content)
assert set(claim)==set(proto['required_per_run']['claim_fields'])
expected={x.split(' (')[0] for x in proto['required_per_run']['progress_fields']}
assert set(progress)==expected
assert json.loads((run/'PACKET_DELTA.json').read_text())==progress
assert len((agent/'STATUS.md').read_text().splitlines())==2
assert all('## '+h in report for h in head)
receipts={}
for p in sorted(run.rglob('*')):
    if p.is_file() and p.name!='receipts.json':
        data=p.read_bytes(); assert len(data)<20_000_000
        receipts[str(p.relative_to(run))]={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
source_paths=[Path(r'BOARD.md'),Path(r'claude\B13\STREAM_NOTES.md')]
sources={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}
(run/'out/receipts.json').write_text(json.dumps({'saved_at_utc':now,'files':receipts,'source_hashes_at_persistence':sources,'protocol_field_validation':'PASS','mirror':'NOT_VERIFIED'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'saved':str(run),'assertions':checks['assertions'],'protocol_fields':'PASS','files_hashed':len(receipts),'rolling':'UPDATED'}))
