from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

r=Path(__file__).resolve().parents[1]; own=r.parents[1]
b=Path(r'~\brain_workers\FEI100_20261011')
shared=Path(r'math-open-problems/reports\fei-2026-10-11')
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
source=b/'agents/A044/runs/20261026T220625Z-account04-A044-non-symmetric-gate-classes'
now=datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):
    p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')

paths=[shared/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((b/'context').glob('*.txt'))
paths += [b/'BOARD.md',b/'claude/B09/STREAM_NOTES.md',source/'REPORT.md',source/'PROOF.md',source/'CLAIMS.json']
paths += [b/'agents/A041/runs/20261023T135351Z-account03-A041-weighted-threshold-fei/PROOF.md']
save(r/'out/SOURCE_RECEIPTS.json',{'time':now,'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths],
 'reading_scope':'Protocol fully read; current B09 board/stream/rolling/prior claims and full A044/A041 proofs read; background reports and papers consulted at relevant product/composition/prime locators. No percolation theorem used; raw paper texts decode cp1252.',
 'personal_context':'Wake warning: owner model183.4h, state168.0h, dream40.4h stale; not mathematical premises.',
 'compute':'Observed snapshot status ok,9.2GB disk free; small exact jobs60MB estimates; fresh memok exited0,6.6GB physical/18GB commit free for bounded core-Lean attempt; interventions ledger tail read. No other running work changed.'})

claims=json.loads((source/'CLAIMS.json').read_text(encoding='utf-8'))
review=next(x for x in claims if x['claim_id']=='A044-SHARP-RESERVE-EQUALITY-AND-SUPPLIER-OBSTRUCTION')
assert hashlib.sha256(review['exact_statement'].encode('utf-8')).hexdigest()==review['statement_sha256']
assert sha(source/'PROOF.md')==review['proof_source']['sha256']
review['proof_source']={'path':str(source/'PROOF.md'),'sha256':sha(source/'PROOF.md')}
review['review_records'].append({'reviewer':'A045/account04','outcome':'HOLDS_SCOPED','source_statement_sha256':review['statement_sha256'],
 'review_source':str(r/'PROOF.md'),'scope':'A044 new equality, uniform classification, conditional fair-gate corollary and explicit account obstructions. Does not independently reaccept reviewer A045 own earlier prerequisite. No universal supplier.',
 'independent_validation':['out/CHECKS.json','out/INDEPENDENT.json'], 'repair':False})
review['status']='INDEPENDENT_RECONSTRUCTION_HOLDS_SCOPED'
statement=('For every integer n>=3, m=n-2, and 0<epsilon<=1/(8m), the actual Boolean prime gate T_2^n under independent biases (1/2,1/2,epsilon,...,epsilon) has J_hi>=9 ln(4)/64 and 0<Bstar+ln(4)R<=5 ln(4)m epsilon. Thus J_hi/(Bstar+ln(4)R)>=9/(320m epsilon), and no finite universal K pays J_hi from Bstar or Bstar+ln(4)R even after excluding every prime up to any fixed arity cutoff. Bstar is the SAME sharp joint singleton reserve; R is the degree refund; natural units and upper dyadic rounding. These are diminished-account obstructions, not FEI counterexamples. Separately paying all symmetric thresholds is not refuted.')
claim={
 'claim_id':'A045-PRIME-RARE-BOUNDARY-RESERVE-OBSTRUCTION','version':1,
 'exact_statement':statement,
 'hypotheses':['Actual sign T_2^n on n distinct physical inputs, n>=3; genuine independent interior product law',
 'p1=p2=1/2 and remaining biases epsilon in(0,1/[8(n-2)])',
 'P(S)=v_S c_S^2 normalized centered-product spectrum, Delta=I-Var, R=sum_(|S|>=3)(|S|-2)P(S)',
 'J_hi=ln4 sum_high P(S)j_S;1/2<2^j_S|c_S|<=1; Bstar=ln4(2Delta-R)-J1-ln2 L1',
 'Deterministic endpoint contracts physically; no repeated variable or spectral-conditioning substitution',
 'Prior imports/mantissas/low and high carries/S_tree/both full KL terminals retained; no owner renewed'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['A045/account04'],
 'proof_source':{'path':str(r/'PROOF.md'),'sha256':sha(r/'PROOF.md'),'exact_checks':['out/CHECKS.json','out/INDEPENDENT.json']},
 'proof_dependencies':[{'claim_id':'A041-SHARP-JOINT-SINGLETON-SOURCE','version':1,'statement_sha256':'858bf303c4d23127fd913d7bc8c6e670e56b44a2ac6db09f682328ce51ed371f','used_scope':'Bstar>=0 reconstructed directly in PROOF section1'},
 'Direct physical threshold pivotal probabilities, union bounds, centered-product Fourier derivatives, explicit three-row primeness witness'],
 'review_records':[], 'status':'AUTHOR_ANALYTIC_PROOF_EXACT_CHECKS_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],
 'refutes':['Unregistered finite-exception prime-only supplier J_hi<=K Bstar',
 'Unregistered finite-exception prime-only supplier J_hi<=K(Bstar+ln4 R)'],
 'first_unproved_line':'Restricted obstruction has a full analytic proof. A necessary original arbitrary-core high-sector supplier, including rare-core transfer and all previous debits/both full terminals, remains unpaid.',
 'next_consumers':['A041','A042','A043','A044','A090','A091','B09 lead']}
save(r/'CLAIMS.json',[review,claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2', 'run_id':r.name,'stream':'B09','packet_id':'A045',
 'gap_id':'G-B09-ORIGINAL-PRIME-HIGH-SCALE-PAYMENT','attempt_id':'A045-stage11-prime-rare-boundary',
 'method':'Independent A044 reconstruction; actual prime T_2^n rare-input degeneration; analytic physical union bounds with two independent exact spectrum implementations',
 'mathematical_delta':'A044 equality/classification/account theorem HOLDS scoped. Prime-only finite-exception reserve suppliers fail quantitatively at every arity: Jhi>=9ln4/64 but Bstar+ln4R<=5ln4(n-2)epsilon. This closes a finite-known-gate objection, not FEI.',
 'deliverable_status':'COMPLETE_LOCAL_SOURCE_AND_CERTIFICATES',
 'mathematical_status':'FULL_FEI_OPEN;RESTRICTED_OBSTRUCTION_AUTHOR_PROOF_PENDING_REVIEW;A044_SCOPED_REVIEW_HOLDS',
 'claim_versions_used':[{'claim_id':'A044-SHARP-RESERVE-EQUALITY-AND-SUPPLIER-OBSTRUCTION','version':1,'statement_sha256':review['statement_sha256']},
 {'claim_id':'A041-SHARP-JOINT-SINGLETON-SOURCE','version':1,'statement_sha256':'858bf303c4d23127fd913d7bc8c6e670e56b44a2ac6db09f682328ce51ed371f'}],
 'claims_created_or_changed':[{'claim_id':review['claim_id'],'version':1,'change':'Local independent scoped review appended'}, {'claim_id':claim['claim_id'],'version':1,'change':'New quantitative obstruction, pending review'}],
 'source_artifacts':['PROOF.md','out/SOURCE_RECEIPTS.json','out/FROZEN_SPEC.json','out/FROZEN_INDEPENDENT.json','code/check.py','code/independent.py','out/PILOT.json','out/CHECKS.json','out/INDEPENDENT.json','out/LEAN.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A044/A043/A091 independently audit prime boundary; price a NECESSARY complete rare-core/high-sector transfer from SAME original unused influence beyond diminished Bstar, with S_tree/import/carry and both terminal KL retained. Excluding all symmetric thresholds separately remains allowed.',
 'stagnant_substantive_attempts':0,
 'blockers':['Full original arbitrary-prime supplier unpaid','New obstruction independent review pending','Core Lean timed out45s: RUNTIME_UNVERIFIED, not a mathematical disproof','Supervisor mirror/adoption not observed'],
 'packet_ids':['A045']}
save(r/'PROGRESS.json',progress);save(r/'PACKET_DELTA.json',progress)
main=json.loads((r/'out/CHECKS.json').read_text(encoding='utf-8'));other=json.loads((r/'out/INDEPENDENT.json').read_text(encoding='utf-8'))
report=f'''# exact target, quantifiers, hypotheses and units

Independently audit A044's sharp-reserve equality/classification theorem and test the remaining prime-only finite-exception supplier objection. Every n>=3 and every interior epsilon in(0,1/[8(n-2)]) is covered by the new analytic obstruction. Actual Boolean T_2^n, independent physical product law, natural entropy units and upper dyadic rounding. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Execution protocol v2 fully read; current B09 board, lead v2, A045 rolling history/prior sources, current report registries/dispatch and campaign plan A045 contract; supplemental campaign/claim/control/seed mapping and paper background consulted. Full A044 run20261026T220625Z REPORT/CLAIMS/PROOF and A041 sharp-joint-source PROOF read. Exact byte pins are in out/SOURCE_RECEIPTS.json. Threshold/percolation versions decode cp1252; the product-composition/threshold statements are background, no percolation theorem or unverified recall premise is used. One read-only multiwording math recall provided context only. The newer explicit27Oct invocation authorizes this stage without restarting the expired historical campaign clock.

# complete derivation or exact first unsupported line

PROOF.md section1 reconstructs A044's new all-product equality, all-dimensional fair classification and explicit original-account obstructions without repair: HOLDS_SCOPED. The review excludes independent reacceptance of A045's own earlier dependency. Sections2-3 give an actual prime gate in every arity approaching fair AND2 physically: Jhi>=9ln4/64, whereas0<Bstar+ln4 R<=5ln4(n-2)epsilon. The ratio is at least9/[320(n-2)epsilon]. Every proper block has three explicit distinct cofactor rows, so no one-wire disjoint factorization exists. Deleting finitely many known prime gates, or all primes below any fixed arity, cannot rescue either diminished-reserve supplier. These thresholds already have FEI bounds; excluding ALL symmetric thresholds as separately paid gates is not refuted. The exact first unpaid line is an ORIGINAL influence-priced arbitrary-core high-sector supplier surviving deterministic core limits, after actual old commitments and BOTH full terminal KL costs.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs preceded execution. python -X utf8 code/check.py --pilot:1166 exact assertions PASS. python -X utf8 code/check.py: {main['checks']} exact assertions PASS in{main['seconds']}s;24 interior threshold laws n3..6 at six frozen dyadic epsilons,24 deterministic endpoint controls, every proper threshold block, and ALL65,814 labelled Boolean tables n0..4 for the equality census. Uniform zero-reserve counts2,4,14,40,90 agree with the proved formula. Tensor centered-product spectra use Fraction; physical edges and integer Walsh give separate Parseval/influence checks. python -X utf8 code/independent.py: {other['checks']} exact checks PASS in{other['seconds']}s on12 laws, using direct full physical centered moments and explicit three-row witnesses without checker imports. No floating logarithmic sign or finite extrapolation supports the proof; the reserve upper bound is rational after the analytic L1>=0 step. Both research jobs estimated60MB and had55s caps; no automatic arity escalation, GPU or heavy job.

Potential failure checks: product normalization, inverse actual truth table, physical endpoint contraction, nonzero interior variance, strict positive denominator via top coefficient, dyadic1/2 boundary direction, prime admission for EVERY proper block, n=3 and epsilon collar endpoint, and every discarded term's sign. The analytic proof checks the full collar boundary; finite epsilons are prescribed controls. Fresh memok exited0 before core Lean. The reviewed named core-Lean three-row target timed out at45s (receipt46.321s), RUNTIME_UNVERIFIED with no axioms/target verified. Its source/compiler hashes and local receipts are retained. No Lean certification is claimed. Rung: analytic proof plus exact finite certificates, independent mathematical review pending for the new obstruction.

# proof dependencies and changed downstream conclusions

A044's source statement/hash are unchanged; a local scoped review is appended. The new source uses only direct Boolean derivatives/union bounds and the reconstructed Bstar>=0 inequality. No false registered theorem is alleged. The prior caveat about finite-known-gate witnesses is sharpened: even primes of arbitrarily large arity can approach a zero-reserve boundary. An all-symmetric-threshold exception, extra positive entropy slack, or a necessary richer original source remains available. Source references and BOTH full terminal laws are retained, no KL credit or import/carry refund is renewed.

# one next mathematical action and independent reviewer

A044/A043/A091 should reconstruct equations(3)-(8), the top coefficient and three-row module obstruction. Then price one necessary complete rare-core/high-sector transfer from SAME original unused influence, with positive S_tree, prior imports/carries and both full terminals. Gate arity alone cannot prevent the degeneration. This is a saved source-bound handoff; no message or acceptance is assumed.

# actual persistence receipts or precise save blocker

REPORT/CLAIMS/PROGRESS/PACKET_DELTA, full proof, frozen specs, scripts and exact outputs saved in the designated A045 run; progress copies are byte-identical. Rolling STATUS has exactly STATE/NEXT, with WORKLOG and LEARNED appended. out/PERSISTENCE.json checks protocol keys/hashes/source stability and artifact sizes. All research mutations stay inside A045. No git, mail, brain-store write, other-agent edit, remote job, trading access, background helper or worker created. Supervisor mirror/adoption remains unobserved. Wake warned of stale personal-context notes; none is a premise. Compute snapshot was healthy with disk only9.2GB free; existing work was left intact. The bounded core compiler attempt ended on timeout; no new work remains running.

**Universal bridge:** This stage moves C020 whole-set witness cost by closing a precise objection to the original-owner obstruction: requiring prime gates or deleting any finite arity range cannot make diminished Bstar, even plus ln4R, the universal supplier. Actual prime gates in every arity retain an order-one high-sector bill while that account is O((n-2)epsilon). This neither pays the needed bill nor refutes FEI; a complete original arbitrary-core high-sector payment still remains, including its rare-core boundary and both terminal laws. The shortest NEXT is that necessary core-transfer/original-source payment, with every old debit retained, because another singleton refinement or gate census cannot survive this explicit degeneration.
'''
(r/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
status='STATE: Stage11 saved: A044 equality/classification HOLDS scoped; ALL-arity prime rare-boundary reserve supplier obstruction proved;330031+366 exact checks PASS; review pending; FEI OPEN.\nNEXT: A044/A043/A091 audit prime boundary; fund necessary rare-core/high-sector transfer from SAME original unused influence beyond Bstar(+ln4R), with S_tree/import/carries and BOTH full terminals.\n'
(own/'STATUS.md').write_text(status,encoding='utf-8',newline='\n')
with (own/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:
 f.write(f'\n{now} {r.name}: Independently reconstructed A044 reserve equality/classification HOLDS scoped. Actual prime T2^n two-fair/rare-rest laws prove Jhi>=9ln4/64 but Bstar+ln4R<=5ln4(n-2)epsilon in every arity; no finite arity-exception repair. Main330031 exact assertions7.622688s; independent366 checks0.795672s; pilot1166 PASS. Core-Lean45s timeout RUNTIME_UNVERIFIED; no formal certification. All required artifacts saved locally; full FEI and original supplier remain OPEN.\n')
with (own/'LEARNED.md').open('a',encoding='utf-8',newline='') as f:
 f.write('\nStage11: Actual PRIME T2^n with p1=p2=1/2 and remaining m=n-2 biases epsilon<=1/(8m) has Jhi>=9ln4/64 while0<Bstar+ln4R<=5ln4*m*epsilon. All proper blocks have three rows witnessed by block counts0,1,2 against exterior counts0,1. Thus even deleting every prime below a fixed arity cannot salvage a diminished-reserve-only supplier. Physical epsilon0 contracts to AND2; interior gate remains prime. Thresholds are already paid by their class theorem: excluding ALL symmetric thresholds is not refuted, and this is not H/I divergence. A044 equality/classification independently HOLDS scoped; no self-review of own prerequisite. Original positive S_tree/core entropy and BOTH full terminals must survive any rare-core transfer.\n')

protocol=json.loads((shared/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))['required_per_run']
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
for c in [review,claim]:assert set(c)==set(protocol['claim_fields'])
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
assert len((own/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert all(field in report for field in protocol['report_fields'])
files=[p for p in r.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
assert all(p.stat().st_size<20_000_000 for p in files)
save(r/'out/PERSISTENCE.json',{'time':now,'status':'PASS','schema_checks':'exact protocol claim/progress field sets; report fields; identical progress/delta; two-line STATUS; under20MB',
 'files':[{'path':str(p.relative_to(r)),'sha256':sha(p),'bytes':p.stat().st_size} for p in files],
 'source_stability':sha(source/'PROOF.md')==review['proof_source']['sha256'],
 'remote_mirror':'UNOBSERVED','new_independent_review':'PENDING','full_FEI':'OPEN'})
print(json.dumps({'status':'SAVED','run':str(r),'files':len(files)+1,'main_checks':main['checks'],'independent_checks':other['checks']}))
