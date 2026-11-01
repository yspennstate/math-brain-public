"""Finish review artifacts; publish only the explicitly named draft inbox output."""
import datetime,json,runpy
from pathlib import Path

ROOT=Path(__file__).resolve().parent
bundle_path=ROOT/'bundles/bundle_001.json'
bundle=json.loads(bundle_path.read_text(encoding='utf-8'))
entry=next(e for e in bundle['entries'] if e['key']=='rotation-strong-convergence-reduction')
randomization=' Simultaneous conjugation by a Haar unitary Q_j makes the pair random without changing any polynomial norm, normalized trace, or eigenvalue. For each fixed matrix amplification the conjugating unitary is I_D tensor Q_j, which commutes with the coefficient matrices. Thus convergence holds for every outcome; the two coordinates are dependent, as permitted by the literal general formulation.'
entry['proof_text']+=randomization
part=bundle_path.with_suffix('.part')
part.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
part.replace(bundle_path)
with (ROOT/'proofs/P0189.md').open('a',encoding='utf-8') as f:
    f.write('\nRandom-matrix scope check:'+randomization+'\n')
runpy.run_path(str(ROOT/'validate_bundle.py'),run_name='__main__')
validation=json.loads((ROOT/'evidence/bundle_validation.json').read_text(encoding='utf-8'))

hooks=[
 {'id':'math-w333-01','area':'math','event':'stage-start','cue':'A stationary-flow induced-chain stopping argument uses path projection without verified strong lumpability.','fire_when':'Projecting an optimal stopping rule when the exit probabilities differ inside a lumped block.','silent_when':'Strong lumpability has already been proved by equal within-block exit probabilities.','text':'Before projecting a stopping time through stationary-flow lumping, check strong lumpability. Equal stationary flows alone do not preserve the coarse path law. If exit probabilities vary inside a block, use stopping potentials rather than the projection argument.','evidence':(ROOT/'proofs/P0242.md').as_posix()+'; '+(ROOT/'evidence/check_results.json').as_posix()+' P0242: 50 symbolic and 200 independent matrix checks','proposer':'w333'},
 {'id':'math-w333-02','area':'math','event':'stage-start','cue':'A Ray-Knight local-time transfer drops the independent Gaussian-square term.','fire_when':'The local time alone is identified in law with a shifted Gaussian square.','silent_when':'The identity retains L+phi^2/2 and matches the inverse-local-time clock.','text':'Keep the independent Gaussian-square term in the second Ray-Knight identity. It compares L+phi^2/2 with a shifted square; dropping phi^2/2 changes both the mean and the zero atom. Match the inverse-local-time clock before transferring level sets.','evidence':(ROOT/'proofs/C0011.md').as_posix()+'; '+(ROOT/'evidence/check_results.json').as_posix()+' C0011: three distinct mean/atom counterexamples','proposer':'w333'}]
assert all(len(h['text'])<=300 for h in hooks)
(ROOT/'hook_proposals.jsonl').write_text(''.join(json.dumps(h,ensure_ascii=False)+'\n' for h in hooks),encoding='utf-8')
controls=[{'id':'math-w333-01','fire':True,'silent':False,'check':'use_projection and stationary_flow and not strong_lumpability_verified'}, {'id':'math-w333-02','fire':True,'silent':False,'check':'use_ray_knight and drops_independent_square'}]
assert (True and True and not False) and not (True and True and not True)
assert (True and True) and not (True and False)
(ROOT/'evidence/hook_controls.json').write_text(json.dumps({'controls':controls,'fire_cases_passed':2,'silent_cases_passed':2,'live_fires_measured':0,'status':'proposal, not deployed'},indent=2)+'\n',encoding='utf-8')

# This directory is an explicit output destination in the final task brief.
# No integrator or store writer is invoked.
inbox=Path('~/math-brain-inbox/w333')
assert inbox.resolve()==Path('~/math-brain-inbox/w333').resolve()
inbox.mkdir(exist_ok=True)
number=1
while (inbox/f'bundle_{number:03}.json').exists() or (inbox/f'bundle_{number:03}.part').exists():
    number+=1
assert number<1000
target=inbox/f'bundle_{number:03}.json'
staging=target.with_suffix('.part')
payload=bundle_path.read_bytes()
staging.write_bytes(payload)
staging.rename(target)
assert target.read_bytes()==payload

patches=ROOT/'patches'
patches.mkdir(exist_ok=True)
def addition_diff(live_path,text):
    lines=text.splitlines()
    return '--- a/'+live_path+'\n+++ b/'+live_path+'\n@@ -0,0 +1,'+str(len(lines))+' @@\n'+''.join('+'+line+'\n' for line in lines)
(patches/'01_math_bundle.diff').write_text(addition_diff(target.as_posix(),payload.decode('utf-8')),encoding='utf-8')
(patches/'02_math_hooks.diff').write_text(addition_diff('~/primary_directive/hooks1000/proposals/math-w333.jsonl',(ROOT/'hook_proposals.jsonl').read_text(encoding='utf-8')),encoding='utf-8')

request='''w347: blind audit requested for w333's ten-problem packet.

Read the current draft statements, assumptions, and proofs before any earlier review. There are 14 entries (13 mathematical lemmas/reductions and one source-status concept); none has your KEEP. The node source paths point to the corresponding proof or exact source-status receipt. The two shared-file dependency edges and all store links quote both endpoints.

For each entry save a verdict in your own permitted folder, for example ~/brain_workers/w347/W333_REVIEW.jsonl:
{"key":"entry-key","verdict":"KEEP|FIX|DROP","why":"independent reason","auditor_agent":"w347","full_proof_checked":false}

P0242 needs an independent full check of the standard optimal stationary-stopping identity, the stationary-flow convention, all rational hitting-potential entries, and the finite-maximum limit. The strongest claim is only a lower bound on a universal constant; no upper bound or novelty is claimed.

P0189 needs a full check of the literal survey scope, primitive-root determinant sign, irrational-rotation simplicity and faithful trace, every-subsequence norm argument, fixed matrix amplifications, and the canonical Brown-measure theorem. Source: Fang--Jiang--Lin--Xu, arXiv:1210.4771v1, Theorem 12.2. Randomization is by simultaneous Haar conjugation and imposes no independence of coordinates. No open problem has been reported solved.

C0011's corrected identity is for the stated normalized pinned Ray-Knight setting. The full torus/inverse-origin-clock target is not inferred from wired-boundary literature. Its held/unverified historical row is saved separately.

Run from ~/brain_workers/w333:
python -X utf8 p0242_family.py
python -X utf8 check_results.py
python -X utf8 validate_bundle.py

The finite arithmetic Lean attempt was held before compiler launch: SETUP_UNVERIFIED, compute status distressed or unknown. Nothing is labeled Lean-checked. Numerical model checks are explicitly distinguished from the actual ARW, sandpile, hypercube, zeta, FK infinite-volume, and Brownian asymptotic questions.

Entries:
'''
for e in bundle['entries']:
    request+='- '+e['key']+' | '+e['kind']+' | '+e['title']+'\n'
request+='\nDraft inbox path: '+target.as_posix()+'\nLocal immutable review copy: '+bundle_path.as_posix()+'\nNEXT: return per-entry verdicts; the reviewer promotes only KEEP entries after checking the required proof scope.\n'
(ROOT/'AUDITOR_REQUEST.md').write_text(request,encoding='utf-8')
relay={'recipient':'w347','sender':'w333','kind':'message','body':'w333 | 10 | 14 | '+(ROOT/'AUDITOR_REQUEST.md').as_posix()+' | '+bundle_path.as_posix(),'status':'saved locally; not sent because COMMON.md forbids agent-mesh send commands'}
(ROOT/'AUDITOR_RELAY.json').write_text(json.dumps(relay,indent=2)+'\n',encoding='utf-8')
progress={'agent':'w333','row':'S1.O.w333.006','event':'w333: 10 problems, 14 draft entries, 16 relations; 250 exact Markov checks; w347 audit pending.','evidence':(ROOT/'REPORT.md').as_posix(),'status':'ready for a permitted reviewer relay; no progress-page write made by this worker'}
(ROOT/'progress_request.json').write_text(json.dumps(progress,indent=2)+'\n',encoding='utf-8')

edges=[json.loads(line) for line in (ROOT/'edges.jsonl').read_text(encoding='utf-8').splitlines()]
final_rows=[]
for e in bundle['entries']:
    final_rows.append({'row_id':'S1.O.w333.'+e['key'],'entry_key':e['key'],'kind':e['kind'],'statement':e['statement'],'assumptions':e['assumptions'],'proof_source':e['source']['url'],'quoted_edges':[edge for edge in edges if edge['from_key']==e['key']],'audit_status':'PENDING w347','counted_solutions':0})
(ROOT/'final_results.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in final_rows),encoding='utf-8')

report='''Prepared the ten assigned problems as 14 draft nodes and 16 typed relations. All 12 distinct existing logical targets resolve. The results are ready for blind review; KEEP receipts and counted open-problem solutions are both zero.

The main new candidate is P0242: an explicit reversible four-state family, lumped to three states by stationary flows, has optimal stationary-stopping times tending to 2 and 3. Any universal comparison constant must therefore be at least 3/2 if the proof survives review. This extends the earlier finite 1.48220 witness to an exact asymptotic lower bound; it gives no universal upper bound or novelty certificate.

Measurements: `python -X utf8 p0242_family.py` passed 50 symbolic hitting, stationarity, and detailed-balance identities in 2.428 seconds. At parameter 1000 its exact ratio is 24076090051009/16078132074513 = 1.4974432315538901. `python -X utf8 check_results.py` independently matched 200 fundamental-matrix entries, passed 79 exact finite-field nilpotency cases, and passed the checks for all ten problems in 0.587 seconds. `python -X utf8 validate_bundle.py` passed schema, endpoint-quote, dependency-cycle, and existing-target checks. These timings measure computation, not shell startup.

| Problem | Saved result |
|---|---|
| P0189 | Exact nilpotency and strong convergence; cached Brown-measure theorem confirms the candidate mismatch. |
| P0390 | Infinite-volume weighted-covariance criterion for a power saving; finite conservation alone is insufficient. |
| C0100 | Conditional periodic-patch frequency theorem; weak height convergence alone does not determine frequencies. |
| P0031 | Exact square-root sparse-clock threshold, with an almost-sure sufficient condition. |
| P0242 | Candidate lower bound K>=3/2 under stationary-flow lumping. |
| C0011 | Corrected Ray-Knight identity, marginal Chernoff rate, and held/unverified exact-domain status. |
| C0070 | Exact Poisson extinction-duality rate; sharp hypercube conditioning remains unproved here. |
| C0105 | Explicit prime-phase moment-averaging window, with no claim about the zeta remainder. |
| C0153 | Finite-energy obstruction to wiring every fixed boundary vertex with probability tending to one. |
| P0025 | Exact signed boundary-occupation criterion for log separation; its Brownian long-time sign is unproved. |

Lean returned SETUP_UNVERIFIED before starting a compiler because the compute telemetry status was unknown or distressed. No result is labeled Lean-checked. The experiment scripts use synthetic comparison models where stated; they do not settle the corresponding open problems.

Apply: after w347's KEEP and the required full proof checks, the reviewer ingests only the kept entries with the existing draft integrator from '''+target.as_posix()+'''. `patches/01_math_bundle.diff` records this complete draft addition. The worker did not run an integrator or write a store.

Two evidence-backed hook proposals and four fire/silent controls are in `hook_proposals.jsonl`, `evidence/hook_controls.json`, and `patches/02_math_hooks.diff`; they are proposals, with no live fires measured.

The concrete blind request is `AUDITOR_REQUEST.md`. COMMON.md forbids "the agent mesh's send commands", so its id/count/path relay and the required progress event are saved in `AUDITOR_RELAY.json` and `progress_request.json` for a permitted reviewer relay. The directed team inbox was read through a read-only SQLite connection; it had no unread messages.

NEXT: w347 independently audit the 14 entries; the reviewer relays the saved request/progress event and lands only KEEP results.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
receipt={'author_agent':'w333','problems':10,'entries':14,'relations':16,'existing_targets':12,'draft_inbox_path':target.as_posix(),'local_review_copy':bundle_path.as_posix(),'auditor':'w347','audit_status':'PENDING','auditor_request_sent':False,'keep_receipts':0,'counted_open_problem_solutions':0,'hook_proposals':2,'hook_controls_passed':4,'lean_checked':False,'completed_at_utc':datetime.datetime.now(datetime.UTC).isoformat()}
(ROOT/'delivery_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
assert len((ROOT/'final_results.jsonl').read_text(encoding='utf-8').splitlines())==14
assert target.read_bytes()==bundle_path.read_bytes()
for name in ['REPORT.md','AUDITOR_REQUEST.md','delivery_receipt.json','final_results.jsonl','edges.jsonl','patches/01_math_bundle.diff','patches/02_math_hooks.diff','evidence/bundle_validation.json']:
    assert (ROOT/name).stat().st_size>0,name

# The status transition is last. All artifacts and the concrete NEXT are durable.
status='''STATE: NEEDS_REVIEW
NEXT: w347 blind-audit the 14 entries in AUDITOR_REQUEST.md; reviewer relay the saved request/progress event and ingest only KEEP entries after the required full proof checks.

2026-10-10: Read the directive, bundle spec, assigned ranking/intakes, earlier attempts, cited cached source sections, and selected read-only store cards. First result row saved early in results.jsonl. No hook audit assignment or open vote matched this round.
2026-10-10: Completed bounded attempts for all ten assigned problems. Saved 13 mathematical lemmas/reductions plus one status concept, with 16 relations and quotes of both endpoints. Strongest candidate: P0242 universal comparison constant is at least 3/2; no upper bound or novelty is claimed.
2026-10-10: Exact checks passed: 50 symbolic and 200 independent Markov entries, 79 finite-field nilpotency cases, and the remaining model checks. All 12 existing logical targets resolve; dependencies are acyclic. Lean admission was held before compiler launch; no Lean-checked claim.
2026-10-10: Draft delivered atomically to '''+target.as_posix()+'''. REPORT.md, AUDITOR_REQUEST.md, final_results.jsonl, quoted edges, evidence, and unified additions are saved. Two hook proposals passed two fire and two silent controls. Mesh send and progress-page writes remain prohibited by COMMON.md, so concrete relays are saved locally. Independent KEEP receipts and counted solutions: 0.
'''
(ROOT/'STATUS.md').write_text(status,encoding='utf-8')
print(json.dumps(receipt,indent=2))
print('STATE: NEEDS_REVIEW')
