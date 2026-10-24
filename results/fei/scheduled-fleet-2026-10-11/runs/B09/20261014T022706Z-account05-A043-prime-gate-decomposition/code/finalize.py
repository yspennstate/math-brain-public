from pathlib import Path
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1];BASE=AGENT.parents[1]
RUN=ROOT.name;NOW=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
def sha(b):return hashlib.sha256(b).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def claim_hash(c):return sha(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode())
proto=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
requirements=json.loads(proto.read_text(encoding='utf-8'))['required_per_run']
SOURCE42=BASE/'agents/A042/runs/20261014T015254Z-account05-A042-bias-endpoint-certificates'
SOURCE44=BASE/'agents/A044/runs/20261013T235618Z-account05-A044-non-symmetric-gate-classes'
OLD=AGENT/'runs/20261013T233947Z-account05-A043-prime-gate-decomposition'
paths=[BASE/'BOARD.md',BASE/'claude/B09/STREAM_NOTES.md',proto,
 SOURCE42/'REPORT.md',SOURCE42/'CLAIMS.json',SOURCE42/'PROOF.md',SOURCE42/'out/SCOPED_REVIEW.json',
 SOURCE44/'REPORT.md',SOURCE44/'CLAIMS.json',OLD/'CLAIMS.json',OLD/'out/review_records.json']
save(ROOT/'out/source_receipts.json',{'recorded_at':NOW,'sources':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in paths],'all_sources_read_only':True})
source42=json.loads((SOURCE42/'CLAIMS.json').read_text(encoding='utf-8'))[0]
source44=json.loads((SOURCE44/'CLAIMS.json').read_text(encoding='utf-8'))[0]
oldclaim=json.loads((OLD/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert claim_hash(source42)==source42['statement_sha256']
assert claim_hash(source44)==source44['statement_sha256']
accepted_old=json.loads((SOURCE42/'out/SCOPED_REVIEW.json').read_text(encoding='utf-8'))
assert accepted_old['statement_sha256']==oldclaim['statement_sha256']
save(ROOT/'out/consumed_A042_review.json',accepted_old)

review={'reviewer':'A043/account05','at_utc':NOW,'verdict':'HOLDS_FULL_STATED_NARROW_CLAIM',
 'source_claim_id':source42['claim_id'],'version':source42['version'],'statement_sha256':source42['statement_sha256'],
 'accepted_scope':['exact universal retained singleton-slack identity with nonnegative local terms','mask33152 fair-data selector-line spectrum, deficit and sharp absolute margin','fixed-line endpoint expansions and limits'],
 'excluded_scope':['any inference of arbitrary-prime payment from the slack identity','arbitrary four-bias bound attributed to original source','inherited source validation counts'],
 'method':'Independent sign-character spectrum counting; local signed derivatives and exact rational log-dictionary identity; independent analytic margin subtraction and endpoint differentiation; new centered tensor moments',
 'repair_supplied':False,'contributor_to_source_version':False,
 'evidence':['PROOF.md section1','code/check.py','out/checks.json']}
source42['review_records'].append(review)
source42['status']='INDEPENDENTLY_RECONSTRUCTED_LOCALLY_AT_FULL_STATED_NARROW_SCOPE; ORIGINAL_SOURCE_UNCHANGED'
save(ROOT/'out/review_A042.json',review)

deps=[
 {'claim_id':'A042-SHARP-BINARY-PRIME-ENDPOINT','version':1,'statement_sha256':'e163ebefc916767a00214eea2d54e56e53c9666821565f612f15a7ef4f17d5e8','scope':'binary corner bound and genuine disjoint conjunction closure','status':'PREVIOUSLY_SOURCE_READ_AND_RECONSTRUCTED; KNOWN_FORMULA_CONSUMED'},
 {'claim_id':source44['claim_id'],'version':source44['version'],'statement_sha256':source44['statement_sha256'],'scope':'three-input mux bound Cstar only; exact disjoint composition','status':'CURRENT_SOURCE_READ; EARLIER_INDEPENDENT_MUX_RECONSTRUCTION_RETAINED; NO_FULL_PROFILE_ACCEPTANCE'},
 {'claim_id':oldclaim['claim_id'],'version':1,'statement_sha256':oldclaim['statement_sha256'],'scope':'universal signed singleton reserve only','status':'SOURCE_COMPLETE; A042_SCOPED_INDEPENDENT_ACCEPTANCE_CONSUMED; RECONSTRUCTED_LOCALLY'},
 {'claim_id':source42['claim_id'],'version':1,'statement_sha256':source42['statement_sha256'],'scope':'retained-slack identity and selector source review; not an arbitrary-bias premise','status':'INDEPENDENTLY_RECONSTRUCTED_AT_EXACT_STATED_SCOPE'}]
statement=(
 'For every finite Boolean sign whose positive event is the union of two conjunction terms, and every independent interior product input law, corrected entropy in bits obeys Hplus<=K*(I-Var), K=4+12/ln(2); the same K gives ordinary H<=K*I at uniform inputs and applies after deterministic contraction and output negation. '
 'If the two terms have at most one opposing shared literal, exact disjoint factorization gives the sharper Cstar=2+4/ln(2). After removing constants and irrelevant groups, the only essential nonbinary prime root shapes in this two-term class are ternary mux and T_{r,g}, r>=2, g in {0,1,2}, where T is positive at the all-one conflicting-data corner with its first guard and the all-zero corner with its second guard, with absent guards fixed true. Every T_{r,g} is prime and has the uniform all-bias bound K. '
 'The exact labeled census from pairs of consistent conjunctions has 10,52,168 essential primes at n=2,3,4, and 10,80,336 after output negation. In particular the four-input prime mask33152 is bounded over its entire bias continuum, without a sharp-optimum assertion. '
 'The prime mask56067, positive on {Y1=1,Y2=1,Z=1} or {Y1=0,Y3=1,Z=1} or {Y2=0,Y3=0}, has exact constituent deficit loss delta(F)-sum delta(fi)=-2*v1*p2*p3*p4*(1-p4), equal to -1/8 at uniform bias; no all-bias entropy theorem for this three-term prime or full FEI is asserted.')
hypotheses=[
 'Finite Boolean sign functions, normalized product Fourier basis and independent Bernoulli coordinates',
 'v_i=4p_i(1-p_i), corrected Hplus=sum_{S nonempty}P(S)log2(v_S/P(S)); I spectral expected degree, Var=sum_{S nonempty}P(S)',
 'Terms are conjunctions of literals; internally contradictory terms are removed, repeated literals deduplicated, empty groups treated as constants',
 'Prime classification removes irrelevant physical coordinates and uses genuine one-bit block substitution with disjoint supports',
 'The overlap entropy proof uses at least two opposing shared literals; zero/one-conflict cases use the explicitly stated disjoint decomposition',
 'All quotient inequalities use interior laws; degenerate inputs contracted before normalization; zero entropy terms treated continuously',
 'K is a proved nonsharp upper bound; no many-term/arbitrary-prime/all-dimensional claim is made']
claim={'claim_id':'A043-TWO-TERM-PRIME-OVERLAP-PAYMENT','version':1,'exact_statement':statement,'hypotheses':hypotheses,
 'statement_sha256':'','contributors':['A043/account05'],
 'proof_source':{'run_id':RUN,'paths':['PROOF.md','DECOMPOSITION.md','NEXT_FIXTURE.md','out/checks.json','out/decomposition_checks.json','out/next_fixture.json']},
 'proof_dependencies':deps,'review_records':[],
 'status':'SOURCE_COMPLETE_ANALYTIC_ARBITRARY_ARITY_CLASS_AND_EXACT_CENSUS_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A042','A044','A041','A045','A090','A091','B09','B20']}
claim['statement_sha256']=claim_hash(claim)
save(ROOT/'CLAIMS.json',[claim,source42])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':RUN,'stream':'B09','packet_id':'A043',
 'gap_id':'G-A043-CONTINUOUS-PRIME-RATIO','attempt_id':'A043-stage4-separated-overlap-and-disjoint-two-term-factors',
 'method':'independent retained-slack/selector source review; bounded-amplitude entropy collision lemma; derivative-separation influence and deficit ledger; exact disjoint two-term DNF decomposition; unbounded-arity prime proof; exact rational spectra and exhaustive class census',
 'mathematical_delta':'All two-term DNF signs satisfy product-biased Hplus<=(4+12/ln2)delta; zero/one conflict sharp Cstar; irreducible antipodal roots prime at all arities;336 labeled n4 primes closed including all biases of33152. Shared-guard prime56067 loses exactly1/8 of constituent delta at uniform bias. A042 stage4 claim independently reconstructed at exact scope. Full FEI open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT; NEW_CLASS_REVIEW_PENDING; SCOPED_SOURCE_ACCEPTANCE_SAVED',
 'mathematical_status':'TWO_TERM_CLASS_ALL_ARITY_AND_ALL_BIAS_BOUND_PROVED; PRIME_CLASSIFICATION_AND_CENSUS_CERTIFIED; GENERAL_PRIME_PAYMENT_OPEN',
 'claim_versions_used':deps,
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1},
                             {'claim_id':source42['claim_id'],'version':1,'change':'local independent acceptance; source unchanged'},
                             {'claim_id':oldclaim['claim_id'],'version':1,'change':'A042 scoped acceptance consumed; no whole-bundle acceptance'}],
 'source_artifacts':['REPORT.md','PROOF.md','DECOMPOSITION.md','NEXT_FIXTURE.md','out/checks.json','out/decomposition_checks.json','out/next_fixture.json','out/review_A042.json','out/consumed_A042_review.json','out/source_receipts.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Pay the exact shared-guard deficit loss for prime56067 over all biases with actual normalized profiles and one unused singleton/terminal reserve; A042/A091 review scalar and overlap ledger, A044/A090 review prime decomposition and loss identity.',
 'stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A043']}
save(ROOT/'PROGRESS.json',progress)
(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())

cf=set(requirements['claim_fields']);pf={x.split(' (')[0] for x in requirements['progress_fields']}
assert set(progress)==pf
for c in (claim,source42):
 assert set(c)==cf
 assert claim_hash(c)==c['statement_sha256']
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for artifact in ['checks.json','decomposition_checks.json','next_fixture.json']:
 assert json.loads((ROOT/'out'/artifact).read_text(encoding='utf-8'))['all_passed']

(AGENT/'STATUS.md').write_text(
 'STATE: A043 stage4 complete: all two-term DNFs and their antipodal prime roots have all-bias bound K=4+12/ln2;336 labeled n4 primes closed, mask33152 all biases paid; A042 slack/selector claim independently reviewed; new proof review pending; full FEI OPEN.\n'
 'NEXT: Pay shared-guard deficit loss in prime56067 (exact1/8 at uniform bias) with actual normalized profiles and one retained singleton/terminal reserve; A042/A091/A044/A090 review stage4.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n## {NOW} — stage {RUN}\nConsumed A042 scoped review and independently reconstructed its full stated slack/selector claim. Proved scalar collision payment at amplitude cap1/2; derivative-separated overlap delta is superadditive. This closes all two-term DNFs at K=4+12/ln2 after exact genuine disjoint factorization; remaining prime cores are mux/antipodal corners, unbounded arity.159 fixtures/31,728 exact assertions PASS in20.032s; first deterministic-selector dictionary zero-entry failure recorded and repaired without changing domain.7,380 term pairs/118,684 exact assertions PASS in2.072s, yielding168 natural and336 output-negation-closed n4 primes. Certified actual shared-guard prime56067, exact delta loss1/8;35 assertions PASS. Saved all protocol files and proofs locally; full FEI and sharp all-bias optimum of33152 remain open. No heavy job, git, external write or dimension escalation.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('''
## Stage4 durable results (20261014T022706Z)
- A042 retained singleton slack identity and full fair-data selector line independently HOLDS at its stated scope; source hash34db76116f2e3e71acdafec19f3dfa7494ce740480dca6a32187eced16171fbd. Consume its scoped acceptance of own stage3 without declaring the whole bundle reviewed.
- For |a|,|b|<=1/2, h(a+b)<=2h(a)+2h(b), h(t)=t^2 ln(1/t^2). Opposite signs use monotonicity below1/2; equal signs use w=a^2+b^2<=r=(a+b)^2<=2w and log inequalities. Do not extend this proof to singleton amplitudes near1.
- Two conjunction events with >=2 opposing shared literals have disjoint derivative supports; delta(union)=delta(fA)+delta(fB)+8P(A)P(B). Their higher-degree normalized amplitudes are capped1/2. Combined with existing conjunction constant and signed singleton reserve, E<=(12+4ln2)delta, hence bit K=4+12/ln2, arity/bias uniform.
- Exact two-term DNF factorization: disjoint groups of agreeing common literals, opposing common literals, first/second private literals.0 conflicts ->OR,1->mux (constant Cstar=2+4/ln2),>=2->antipodal corner prime T_{r,g}, g=0,1,2 guards (constant K). All such cores are prime; nontrivial conjunction groups supply proper disjoint blocks. No overlapping physical composition is falsely declared disjoint.
- Every two-term DNF sign and its output negation obey the all-bias K bound, and ordinary uniform H<=K I. Mask33152 is now bounded over all four biases; K is not claimed sharp. Exact consistent-term census prime counts n2/3/4:10/52/168; with output negation10/80/336. All other n4 primes remain outside this result.
- Next obstruction: prime56067 positive on A={Y1=1,Y2=1,Z=1},B={Y1=0,Y3=1,Z=1},C={Y2=0,Y3=0}. Net delta loss=-2v1*p2*p3*p4*(1-p4), uniform-1/8; component deltas5/16,5/16,1/4, actual3/4. Agreeing shared guard creates covariance after deleting opposing Y1. Nonzero influence cross terms without that covariance can cancel in delta; price net loss, not raw cross terms.
- Deterministic endpoint checking: remove zero-coefficient entries before comparing rational-log dictionaries. Preserve the true analytic contraction instead of treating a zero dictionary key as mathematical disagreement.
''')
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (ROOT/'REPORT.md').read_text(encoding='utf-8').strip().splitlines()[-1].startswith('**Universal bridge:**')
files=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='persistence_validation.json':
  assert p.stat().st_size<20*1024*1024
  files.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())})
save(ROOT/'out/persistence_validation.json',{'at_utc':NOW,'all_passed':True,
 'checks':['exact claim/progress fields','canonical statement hashes including source claim','byte-identical delta','passed exact outputs','two-line status','final Universal bridge paragraph','all files below20MB'],
 'receipts':files,'external_copy_status':'SUPERVISOR_PENDING; NOT_PERFORMED','new_claim_independent_review':'PENDING'})
print(json.dumps({'saved_run':RUN,'new_claim':claim['claim_id'],'statement_sha256':claim['statement_sha256'],
                  'independent_review':source42['claim_id'],'files_checked':len(files),'all_validation_passed':True}))
