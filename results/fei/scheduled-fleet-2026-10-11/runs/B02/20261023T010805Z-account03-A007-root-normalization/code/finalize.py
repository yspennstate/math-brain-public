"""Persist only inside A007; verify protocol fields and every generated receipt."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

RUN = Path(__file__).resolve().parents[1]
HOME = RUN.parents[1]
assert HOME.name == 'A007'
SHARED = HOME.parents[1]
BASE = Path('~/mop_fei100/reports/fei-2026-10-11')
def read(path): return path.read_text(encoding='utf-8')
def load(path): return json.loads(read(path))
def write(path, text):
    assert path.resolve().is_relative_to(HOME.resolve())
    path.write_text(text,encoding='utf-8')
def save(path, data): write(path,json.dumps(data,indent=2,ensure_ascii=False)+'\n')
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

main = load(RUN/'out/checks.json')
other = load(RUN/'out/retuning.json')
assert main['status'] == other['status'] == 'PASS'
assert main['assertions'] == 45580 and other['assertions'] == 56
assert main['source_sha256'] == digest(RUN/'code/check.py')
assert other['source_sha256'] == digest(RUN/'code/check_retuning.py')
# Check actual artifacts, rather than a checkpoint's assertion of their existence.
assert main['counts']['functions'] == 270
assert main['counts']['scalar_pairs'] == 819
assert main['counts']['boolean_pairs'] == 1350
assert {'positive','negative'} <= set(main['signed_witnesses'])
protocol = load(BASE/'EXECUTION_PROTOCOL.json')
now = datetime.now(timezone.utc).isoformat()
sources = [BASE/'EXECUTION_PROTOCOL.json', SHARED/'BOARD.md', SHARED/'claude/B02/STREAM_NOTES.md',
 SHARED/'agents/A008/runs/20261021T234312Z-account03-A008-gate-label-compression/ROOT_PAYMENT.md',
 SHARED/'agents/A008/runs/20261021T234312Z-account03-A008-gate-label-compression/CLAIMS.json',
 SHARED/'agents/A008/runs/20261021T234312Z-account03-A008-gate-label-compression/REPORT.md',
 SHARED/'agents/A015/runs/20261022T231544Z-account03-A015-minterm-barrier-analysis/REPORT.md',
 SHARED/'agents/A015/runs/20261022T231544Z-account03-A015-minterm-barrier-analysis/RARE_CORE_PAYMENT.md',
 SHARED/'agents/A015/runs/20261022T231544Z-account03-A015-minterm-barrier-analysis/FRONTIER.md',
 BASE/'source_material/reductions/paper/forests.tex']
save(RUN/'out/source_pins.json',{'recorded_utc':now,
 'note':'Hashes of source bytes at final save; BOARD is a mutable coordination view, not a proof premise.',
 'sources':[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in sources]})

next_action = ('Against one fixed original prime-table reference, bound the occupation-weighted '
 'singleton-name and output-ambiguity terms of actual compatible prime forests in central-band '
 'threshold products; do not substitute the nonempty root prior for the Fourier-set posterior. '
 'Use A015 FRONTIER.md to avoid its refuted whole-variable dimension budget.')
statement1 = ('For every finite nonempty positive vector x (dimension N>=1) and coordinatewise thinning 0<y<=x, put '
 'A_x=sum x_i, D_x=prod(1+x_i)-1, Q_x(R)=prod_{i in R}x_i/D_x for nonempty R, '
 'r_x(i)=x_i/A_x and L=sum(x_i-y_i). Then -L<=ln(D_y/D_x)-ln(A_y/A_x)<=0 '
 'and |KL_nats(Q_y||Q_x)-KL_nats(r_y||r_x)|<=L. For activities '
 'x_e=lambda_e 2^-w_e, y_e=lambda_prime_e 2^-w_e from any finite nonempty '
 'signed-conjunction implicant table of a nonconstant uniform sign Boolean f, '
 'positive packing-feasible lambda and 0<lambda_prime<=lambda, q=Pr(f=-1), '
 'v=4q(1-q), k=min w_e>=1, a_w=(1-2^-w)/w and '
 'd_i=sum_{e:i in R_e}(lambda_e-lambda_prime_e)a_w_e, '
 'vL<=2(1-q)sum_i Inf_i(f)d_i<=2a_k(1-q)I(f). Thus either root remainder '
 'above, in bits and weighted by v, is bounded by '
 '2(1-q)sum_i Inf_i(f)d_i/ln2. These are alternative component bounds, not an added budget.')
statement2 = ('For the fixed three-bit sign Boolean f=2[x2 AND (x1 OR x3)]-1, '
 'the complete positive prime table is R1={x1,x2}, R2={x2,x3}, pi1=pi2=1/4, '
 'v=15/16 and I=5/4. For every integer j>=1 and delta=2^-j, '
 'lambda=(delta/2,delta^2/2) and lambda_prime=(delta^3/2,delta^2/2) '
 'are positive, fixed before sampling, packing-feasible ordered references on this same table. '
 'Their nonempty conditioned root priors satisfy '
 'v KL_bits(Q_lambda_prime||Q_lambda)/I > 3j/4-1 and equal 3j/4+o(1). '
 'All root activities tend to zero. Hence no universal K pays this KL for EVERY '
 'feasible thinning pair. This does not refute optimized reference existence or FEI.')
gap = ('The complete fixed-reference occupation, gate-name and output-ambiguity payment for '
 'actual Fourier-set forest posteriors remains unproved; the prior Q_y cannot be substituted '
 'for such a posterior. No full FEI claim is made.')

def claim(identifier, statement, hypotheses, source, dependencies, refutes):
    return {'claim_id':identifier,'version':1,'exact_statement':statement,'hypotheses':hypotheses,
      'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
      'contributors':['A007'],'proof_source':source,'proof_dependencies':dependencies,
      'review_records':[{'reviewer':'A007','role':'author audit, not independent acceptance',
        'verdict':'analytic derivation and independent representations checked; exact certificates PASS',
        'evidence':['out/checks.json','out/retuning.json']}],
      'status':'PROVED_LOCALLY_PENDING_INDEPENDENT_REVIEW','supersedes':[], 'refutes':refutes,
      'first_unproved_line':None,'next_consumers':['A008','A015','A086','A094','B02','B20']}
claims = [claim('A007-NONUNIFORM-ROOT-THINNING-AND-PHYSICAL-PAYMENT',statement1,
 ['Finite positive activities; no zero support changes','Only coordinatewise thinning is allowed',
  'For physical corollary: genuine signed implicants, actual rarity, original feasible packing',
  'KL compares the stated priors, not arbitrary witness posteriors'],
 ['ROOT_THINNING.md','REVIEW_A008.md','out/checks.json'],
 ['A008-ALL-BOOLEAN-IMPLICANT-ROOT-NORMALIZER-PAYMENT@1: local fiber/packing core independently reconstructed; private-leaf corollary not used'],[]),
 claim('A007-OVERLAPPING-PRIME-RARE-RETUNING-KL-OBSTRUCTION',statement2,
 ['The actual fixed three-bit function and references specified in the statement',
  'j is an integer at least one; KL is in bits; gate table remains fixed'],
 ['RETUNING_OBSTRUCTION.md','ROOT_THINNING.md','out/retuning.json'],
 ['A007-NONUNIFORM-ROOT-THINNING-AND-PHYSICAL-PAYMENT@1'],
 ['Unregistered helper: for every feasible coordinatewise thinning, v KL_bits(Q_new||Q_old)<=K I with universal K'])]
fields = protocol['required_per_run']['claim_fields']
assert all(set(c)==set(fields) for c in claims)
save(RUN/'CLAIMS.json',claims)
progress = {'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B02','packet_id':'A007',
 'gap_id':'G-J-COST','attempt_id':'A007-substantive-root-thinning-after-A008-universal-payment',
 'method':'Independent physical-fiber review; exact differential normalization; conditioned-prior KL identity; overlapping-prime obstruction; frozen rational certificates',
 'mathematical_delta':'Universal coordinatewise root thinning has a signed lost-activity remainder and a paid multi-root KL correction; the singleton-name KL survives and is unbounded on feasible rare references of one overlapping-prime function. A008 universal root core independently reconstructed.',
 'deliverable_status':'COMPLETE_LOCAL_PENDING_REVIEW_AND_SUPERVISOR_COPY',
 'mathematical_status':'TWO_SCOPED_LOCAL_PROOFS; INDEPENDENT_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':['A008-ALL-BOOLEAN-IMPLICANT-ROOT-NORMALIZER-PAYMENT@1, universal root core only; independently reconstructed without repair'],
 'claims_created_or_changed':[c['claim_id']+'@1' for c in claims],
 'source_artifacts':['ROOT_THINNING.md','RETUNING_OBSTRUCTION.md','REVIEW_A008.md',
  'FROZEN_SPEC.json','FROZEN_SPEC_RETUNING.json','out/pilot.json','out/checks.json',
  'out/retuning.json','out/retuning_precision_attempt.md','out/source_pins.json'],
 'next_consumers':['A008','A015','A006','A086','A094','B02','B20'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':[gap,'New claims await independent review; supervisor mirror copying is not observed',
  'Stored owner-model/state-of-mind freshness is degraded; brain self-care is unverified'],
 'packet_ids':['A007']}
expected = {p.split(' (')[0] for p in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
save(RUN/'PROGRESS.json',progress)
save(RUN/'PACKET_DELTA.json',progress)

report = f'''# A007 B02: root normalization under nonuniform thinning

## exact target, quantifiers, hypotheses and units

Continue the 2026-10-23 01:08 UTC root-normalization packet, retaining the negative normalization term. The owner deadline is 2026-10-23 14:49 UTC; the earlier baseline protocol deadline is superseded. The local targets are the two exact all-parameter statements in CLAIMS.json. Natural logarithms and nats are used in the analytic identities, then divided by ln2 for bit costs. The physical corollary uses q=Pr(f=-1), actual signed implicants, pi=2^-width and the same packing rows. It does not require monotonicity, private leaves or minimal primes. The refuted helper concerns EVERY feasible reference-thinning pair, not existence of a favorable reference or full FEI.

## sources actually read, revisions and theorem locators

Read the complete execution protocol, fresh BOARD snapshot (2026-10-23 01:01 UTC), B02 STREAM_NOTES.md v2, own prior STATUS and stage7 result. The lead's original A009/tribes review direction was already consumed in earlier stages. The previous rare-leafless NEXT was overtaken by A015's 20261022T231544Z REPORT.md, RARE_CORE_PAYMENT.md and FRONTIER.md; these were read to avoid duplicating its complete queue payment and failed central-band dimension budget.

Read A008's 20261021T234312Z ROOT_PAYMENT.md, CLAIMS.json and REPORT.md. REVIEW_A008.md reconstructs the universal fiber/packing/root theorem independently, without a repair. Its source claim is A008-ALL-BOOLEAN-IMPLICANT-ROOT-NORMALIZER-PAYMENT@1, declared canonical statement SHA256 140a7ef8246f415477ef68edd58fccc9b135b13e4f5c896fa370a988504067cd. This review does not certify the compound private-leaf corollary: A009's complete upstream theorem was not newly reviewed. Also read the original forests.tex root-reference definitions and queue construction (first 95 lines), and A006's latest class report for orientation. Prior campaign/paper readings are continuation context, not a claim of fresh all-paper review here. out/source_pins.json records exact source bytes at final save; mutable BOARD hashes are not proof premises.

## complete derivation or exact first unsupported line

The full derivations are in ROOT_THINNING.md and RETUNING_OBSTRUCTION.md. For A=sum x and D=prod(1+x)-1, define Delta=ln(D/A). The exact derivative is (AE-D)/(AD). A finite union bound proves AE-D>=0; E[1+(A+1)a]>=A+1 proves AE-D<=AD. Thus every derivative lies in [0,1], giving -(A_x-A_y)<=ln(D_y/D_x)-ln(A_y/A_x)<=0 under coordinatewise thinning. This retains both the total-mass logarithm and the negative multi-root correction.

The exact KL difference between the nonempty root laws and their singleton gate laws is Delta(x)-Delta(y)+sum_i(mu_i-r_i)ln(y_i/x_i). Here 0<=mu_i-r_i<=y_i. The first summand is in [0,L]; the remaining sum is in [-L,0] by t ln(1/t)<=1-t. Therefore the absolute difference is at most L. Both signs occur in exact fixtures. A008's independently reconstructed local physical inequality pays vL<=2(1-q)sum_i Inf_i d_i<=2a_k(1-q)I. The two resulting component estimates are alternatives, not an additive use of the same influence budget.

For f=2[x2 AND (x1 OR x3)]-1, the exact positive primes overlap and have rarity 1/4; v/I=3/4. With delta=2^-j and old/new feasible weights (delta/2,delta^2/2), (delta^3/2,delta^2/2), the singleton laws swap and have bit KL j(1-delta)/(1+delta). The nonempty-root KL differs by at most (delta-delta^3)/(8 ln2). Consequently v KL/I>3j/4-1 and equals 3j/4+o(1), though all root activities tend to zero. The signed normalization has Ay/Ax=delta and remainder in [-L,0]. This is an actual overlapping-prime reference obstruction on one fixed Boolean function, not a Boolean unbounded H/I family.

First unsupported line toward the universal target: {gap} Neither a fixed-reference posterior payment nor any surviving name payment follows from an estimate comparing the priors Q_y and Q_x. The obstruction rules out paying arbitrary reference retuning by influence alone.

## executed validation with domain, arithmetic, commands and outputs

The search specifications were saved before their jobs in FROZEN_SPEC.json and FROZEN_SPEC_RETUNING.json. No dimension was raised. All Python used -X utf8; outputs use explicit UTF-8. The main pilot took 0.599 seconds and passed 2544 assertions. The full command `python -X utf8 code/check.py`, from this run directory, passed {main['assertions']} assertions in {main['seconds']:.3f} seconds. Equivalent invocation from A007 used the run-relative script path.

Its frozen domain was all {main['counts']['functions']} labelled nonconstant functions for n=1,2,3, every signed implicant and actual outside false fiber: {main['counts']['implicants']} implicants, {main['counts']['fibers']} fibers. It also checked 120 positive activity vectors, 819 scalar thinning pairs, 1350 physical-table thinning pairs and sharp AND-width endpoints through 128. Arithmetic was integer/Fraction, with 32-term atanh log intervals and a proved rational tail. Invalid implication, packing, rarity and reverse-thinning fixtures prevent dropping hypotheses. The inherited forced-two-root posterior fixture is a scope guard, not new mathematics.

The independent command `python -X utf8 code/check_retuning.py` passed {other['assertions']} assertions in {other['seconds']:.3f} seconds. It constructed the complete actual eight-entry truth table, all Walsh coefficients, physical influences and all signed prime faces; then directly summed all three nonempty root-set likelihood ratios at j in {{1,2,8,32,128}}. This second representation does not import the first checker. Its 96-term rational atanh enclosures are outward-rounded to dyadic output bounds and rechecked exactly. out/retuning.json contains the certificates. The infinite-j conclusion uses the analytic argument, not finite extrapolation.

Two failed validation attempts are retained in out/retuning_precision_attempt.md: 40-term intervals were too wide at the extreme rarity, then giant exact-Fraction string serialization hit Python's digit limit. Precision and output representation were repaired without changing the frozen case list or accepting either failed attempt as a certificate. No floating-point sign is used. No compiler, GPU, heavy job, background worker or other-agent intervention was launched. Both scripts were estimated at 80 MB and observed below their 55-second limits; therefore the >300 MB admission threshold was not invoked. Lean formal verification was not performed and is not claimed.

## proof dependencies and changed downstream conclusions

The first new claim depends only on the independently reconstructed A008 local physical core and elementary finite products/calculus/KL identities proved in ROOT_THINNING.md. The second depends on the first and an exact physical truth-table calculation. This is an acyclic chain. The universal root bound has no prime/private-leaf dependence. A008's sharper private-leaf composite remains conditional on upstream review and is not used. No existing registered claim is asserted refuted; the precise unregistered all-reference KL helper is refuted. A015 already closed the previous NEXT; the stage consumes that new dependency instead of repeating its class proof.

This closes the signed multi-root normalization component under general coordinatewise thinning. It does not close complete occupation, source-dependent ambiguity or witness cost. New local claims require independent review; the author's own exact checks do not count as independent acceptance. The canonical statement hash convention for new claims is SHA256 of the exact UTF-8 statement; A008's declared canonical source hash is retained with its original convention.

## one next mathematical action and independent reviewer

{next_action} The requested reviewers/consumers are A008 and A015 for the physical/reference interface, and A086/A094 for the new thinning proof and actual counterfamily. This is an on-disk handoff, not an assertion that a message was sent or review accepted. Review-first priority applies before opening another broad candidate.

## actual persistence receipts or precise save blocker

All four required files, full proofs, frozen specifications, scripts and exact outputs are saved under this run. STATUS.md, WORKLOG.md and LEARNED.md are updated only in A007. out/persistence_receipt.json records generated-file hashes and byte counts after schema/content verification. PROGRESS.json and PACKET_DELTA.json are identical and packet_ids is ["A007"]. No file reaches 20 MB. Shared registries, other agents, brain data and source trees were not modified. Supervisor copy/mirror acceptance is unobserved; no git or external write was attempted.

Brain self-care remains degraded/unverified: stored owner-model and state-of-mind sources were stale at wake. Their freshness and personalization based on them remain unverified; current explicit instructions and checked mathematical sources govern this run. This is separate from the local exact certificates. No authorized mathematical work is blocked on refreshing those views.

## Universal bridge

This stage moves C020 whole-set witness cost, at the root-normalization interface: the exact signed multi-root correction under every finite positive coordinatewise thinning is bounded by the lost physical activity and paid by the same implicant packing; A008's universal root core is independently reconstructed. The amount still unpaid is the singleton gate-name/occupation and ambiguity bill for actual Fourier-set forest posteriors. An overlapping-prime fixed-function example proves that arbitrary reference retuning cannot universally pay that bill. NEXT attacks precisely that unpaid fixed-reference interface using actual compatible forests and A015's central-band obstruction; it avoids repeating a known threshold FEI class and avoids another normalization-only bound. Full FEI remains OPEN.
'''
for heading in protocol['required_per_run']['report_fields']:
    assert '## '+heading+'\n' in report
write(RUN/'REPORT.md',report)
write(RUN/'CHECKPOINT.md','COMPLETE_LOCAL '+now+'\n45580 main exact assertions and 56 independent retuning assertions PASS. Proofs and four protocol files saved. New claims await independent review; FEI OPEN.\nNEXT: '+next_action+'\n')
write(HOME/'STATUS.md','STATE: A007 root-thinning stage locally complete: signed lost-activity and multi-root KL bounds; rare overlapping-prime retuning obstruction; 45636 exact assertions PASS; independent review pending; FEI OPEN.\nNEXT: '+next_action+'\n')
entry = f'\n## {now} | {RUN.name}\nConsumed A015 completion of prior rare-leafless NEXT and independently reconstructed A008 universal local root core. Proved coordinatewise thinning signed normalization/KL remainder and physical lost-activity payment. Constructed an actual overlapping-prime, all-roots-rare feasible retuning family with v KL/I>3j/4-1. Main 45580 + independent 56 exact assertions PASS. Retained interval-width and Fraction-serialization audit failures, repaired without domain expansion. Independent review/mirror receipt pending; no jobs left by these checkers; full FEI OPEN. Brain self-care degraded/stored owner context stale. NEXT: {next_action}\n'
old = read(HOME/'WORKLOG.md') if (HOME/'WORKLOG.md').exists() else ''
if RUN.name not in old: write(HOME/'WORKLOG.md',old+entry)
lesson = f'''\n## {RUN.name}: root thinning is paid; arbitrary name retuning is not

For finite x>0 and 0<y<=x, Delta=ln((prod(1+x)-1)/sum x) has every derivative in [0,1]. Consequently the signed normalization remainder lies in [-sum(x-y),0], and the nonempty-root prior KL differs from singleton-name KL by at most sum(x-y) nats. Both signs of this KL difference occur. These are actual conditioned-product priors, never arbitrary Fourier-set forest posteriors.

With genuine signed implicants and actual rarity 2^-w, FALSE probability q, and the same feasible packing, v sum((lambda-lambda_prime)pi)<=2(1-q)sum Inf_i d_i<=2a_k(1-q)I. The two component bounds are alternatives, not an additive influence debit. A008's local core was independently reconstructed without repair; its private-leaf corollary was not accepted here.

The fixed f=2[x2 AND (x1 OR x3)]-1 has exactly two overlapping positive primes, v/I=3/4. At delta=2^-j, weights (delta/2,delta^2/2) thinned to (delta^3/2,delta^2/2) are positive, feasible and all rare; nevertheless v KL_bits(Q_new||Q_old)/I>3j/4-1. This refutes universal payment of EVERY reference reset, not optimized existence and not FEI. Keep the singleton-name cost and the actual posterior occupation separate.

Exact audit lesson: at j=128, fixed low-order log intervals can be wider than the root correction even when the leading KL is large; increase certified precision only as needed. Serialize exact intervals by checked outward dyadic rounding instead of enormous rational decimal strings. No proof conclusion may use a failed certificate. Prior rare-leafless NEXT is already paid by A015; use its central-band actual-forest frontier rather than a repeated class calculation.
'''
old = read(HOME/'LEARNED.md') if (HOME/'LEARNED.md').exists() else ''
if RUN.name not in old: write(HOME/'LEARNED.md',old+lesson)

assert load(RUN/'PROGRESS.json') == load(RUN/'PACKET_DELTA.json')
assert len(read(HOME/'STATUS.md').splitlines()) == 2
files = sorted(p for p in RUN.rglob('*') if p.is_file() and p.name != 'persistence_receipt.json')
assert all(p.stat().st_size<20_000_000 for p in files)
save(RUN/'out/persistence_receipt.json',{'saved_utc':now,'run_id':RUN.name,
 'schema_validation':'PASS','exact_assertions':45636,'independent_review':'PENDING',
 'mirror_verification':'UNOBSERVED','formal_Lean_verification':'NOT_PERFORMED',
 'files':[{'relative_path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files],
 'rolling_files':[{'path':str(HOME/n),'sha256':digest(HOME/n)} for n in ['STATUS.md','WORKLOG.md','LEARNED.md']]})
print(json.dumps({'saved':str(RUN),'assertions':45636,'files':len(files)+1,'protocol_fields':'PASS',
 'packet_delta_identical':True,'largest_file_bytes':max(p.stat().st_size for p in files)}))
