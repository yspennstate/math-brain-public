import json,hashlib,datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
BASE=AGENT.parents[1]
RUN=ROOT.name
STAMP=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
def sha(b):return hashlib.sha256(b).hexdigest()
def save(path,obj):path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def canonical(statement,hypotheses):
    return sha(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode())

source_rel=[
 'BOARD.md','claude/B09/STREAM_NOTES.md',
 'agents/A042/runs/20261013T221414Z-account05-A042-bias-endpoint-certificates/REPORT.md',
 'agents/A042/runs/20261013T221414Z-account05-A042-bias-endpoint-certificates/CLAIMS.json',
 'agents/A042/runs/20261012T002547Z-account05-A042-bias-endpoint-certificates/REPORT.md',
 'agents/A044/runs/20261012T040658Z-account05-A044-non-symmetric-gate-classes/out/DERIVATION_CHECKPOINT.md',
 'agents/A043/runs/20261011T221757Z-account05-A043-prime-gate-decomposition/CLAIMS.json',
 'agents/A043/runs/20261012T012726Z-account05-A043-prime-gate-decomposition/PROGRESS.json']
receipt=[]
for rel in source_rel:
    p=BASE/rel
    receipt.append({'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size})
protocol=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
receipt.append({'path':str(protocol),'sha256':sha(protocol.read_bytes()),'bytes':protocol.stat().st_size})
save(ROOT/'out/source_receipts.json',{'recorded_at':STAMP,'sources':receipt,'source_status':'read-only; originals not modified'})

reviews=[{
 'claim_id':'A042-SHARP-MAJORITY3-BIASED-ENDPOINT','version':1,
 'statement_sha256':'396cfaaabff2fa337f7a038ca4380cbede25d84a6ccd96032829a36dbecad11e',
 'reviewer':'A043/account05','verdict':'HOLDS_SCOPED_CORE_UPPER_BOUND_AND_ORBIT',
 'scope':'E <= (4+ln4)delta-(ln4-1)P123 for every interior product law; sharpness reconstructed but not independently accepted because A043 supplied the earlier lower-path input',
 'independence':'sign polynomial and signed rather than monotone derivative reserve; independent truth-table moments',
 'excluded':'explicit 400 corner-error constant, edge remainder formulas, inherited 7783-case counts, independent acceptance of shared lower-bound input',
 'repair_supplied':False,'evidence':['REVIEW_MAJORITY.md','CORE_PROOF.md','out/proof_checks.json']},
 {'source':'A044 stage-2 DERIVATION_CHECKPOINT.md',
 'source_sha256':next(x['sha256'] for x in receipt if 'A044' in x['path']),
 'reviewer':'A043/account05','verdict':'HOLDS_SCOPED_THREE_INPUT_MUX',
 'scope':'explicit spectrum and ratio; fixed-address supremum; global sharp Cstar',
 'independence':'centered-coordinate formula reconstructed and exact independent Fraction moments',
 'excluded':'broader profile-transfer extension and any unprovided completed claim package',
 'repair_supplied':False,'evidence':['REVIEW_MUX.md','out/proof_checks.json']}]
save(ROOT/'out/review_records.json',reviews)

statement=(
 'For every Boolean sign function under an interior product law, its natural corrected singleton entropy obeys E_single<=4delta-2R, where delta=I-Var and R=sum_{|S|>=3}(|S|-2)P(S). '
 'For every essential ternary prime the corrected entropy in bits satisfies Hplus<Cstar*delta in the interior, and each of the five ternary prime symmetry orbits has supremum Hplus/delta=Cstar=2+4/ln(2). '
 'Together with the exact binary bound and disjoint composition, Hplus<=Cstar*delta holds for every Boolean gate on at most three essential inputs and every genuine read-once formula of such gates under arbitrary interior physical product laws, with contraction for deterministic inputs; this implies ordinary uniform-input H<=Cstar*I. '
 'The proposed all-arity prime companion E_ge2<=ln(4)*delta+2R is false: the essential four-input prime positive exactly at binary-index assignments 7,8,15 (mask 33152), at probabilities (1/2,1/2,1/2,1/1024), has companion excess >13/100, while (4+ln(4))*delta-E_total>9/20 at that same law. Full FEI and the all-arity biased-prime constant remain open.')
hypotheses=[
 'Boolean signs on finite cubes, independent Bernoulli coordinates, normalized product Fourier basis',
 'spectral influence I=sum |S|P(S), Var=sum_{S nonempty}P(S), corrected Hplus=sum_{S nonempty}P(S)log2(v_S/P(S))',
 'natural-unit E=(ln2)Hplus; zero terms interpreted continuously; v_i=4p_i(1-p_i)',
 'prime means essential with no proper block of size 2..n-1 having exactly two cofactor rows; constants and literals terminal',
 'no variable reuse in the formula conclusion; deterministic children contracted before normalization',
 'all input biases interior for strict ternary inequality and explicit prime obstruction; sharpness is a supremum of interior ratios, not a boundary ratio at zero deficit',
 'the signed reserve is all-dimensional, the sharp prime bound is restricted to arity three, and no all-dimensional FEI conclusion is asserted']
deps=[
 {'claim_id':'A042-SHARP-BINARY-PRIME-ENDPOINT','version':1,'statement_sha256':'e163ebefc916767a00214eea2d54e56e53c9666821565f612f15a7ef4f17d5e8','scope':'binary sharp inequality via explicit formulas (3),(7)','status':'SOURCE_COMPLETE_EXPLICIT_FORMULAS_RECONSTRUCTED'},
 {'claim_id':'A042-SHARP-MAJORITY3-BIASED-ENDPOINT','version':1,'statement_sha256':reviews[0]['statement_sha256'],'scope':'core bound and orbit only; sharp lower path reconstructed using prior A043 result','status':'SCOPED_UPPER_BOUND_INDEPENDENTLY_RECONSTRUCTED; OTHER_SOURCE_REFINEMENTS_NOT_ASSUMED'},
 {'source':'A044 stage-2 checkpoint','source_sha256':reviews[1]['source_sha256'],'scope':'three-input mux only','status':'SCOPED_CHECKPOINT_INDEPENDENTLY_RECONSTRUCTED'},
 {'claim_id':'A043-DISJOINT-PRIME-ENDPOINT','version':1,'statement_sha256':'bd9d9a2c11b8e82cc302f653748ffe650977e88c429bb63d6ef8cdffb673b4f2','scope':'cofactor criterion and disjoint composition rederived in local CORE_PROOF; earlier n=4 census not needed','status':'ANALYTIC_SCOPE_REDERIVED; NO_ASSUMPTION_OF_WHOLE_BUNDLE_ACCEPTANCE'}]
claim={'claim_id':'A043-TERNARY-PRIME-CLOSURE-AND-RESERVE-OBSTRUCTION','version':1,
 'exact_statement':statement,'hypotheses':hypotheses,'statement_sha256':canonical(statement,hypotheses),
 'contributors':['A043/account05 (three new orbit bounds, signed reserve, prime obstruction, package)',
                 'A042/account05 (source binary and majority bounds)',
                 'A044 (source three-input mux bound)'],
 'proof_source':{'run_id':RUN,'paths':['CORE_PROOF.md','REPORT.md','REVIEW_MAJORITY.md','REVIEW_MUX.md','out/catalogue.json','out/proof_checks.json','out/prime_obstruction.json']},
 'proof_dependencies':deps,'review_records':[],
 'status':'SOURCE_COMPLETE_ANALYTIC_PROOF_AND_EXACT_OBSTRUCTION_PENDING_INDEPENDENT_REVIEW',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A042','A044','A041','A045','A090','A091','B09','B20']}
save(ROOT/'CLAIMS.json',[claim])
progress={
 'protocol_revision':'2026-10-11-execution-v2','run_id':RUN,'stream':'B09','packet_id':'A043',
 'gap_id':'G-A043-CONTINUOUS-PRIME-RATIO','attempt_id':'A043-stage3-ternary-closure-prime-reserve-obstruction',
 'method':'scoped independent source reconstructions; exact 256-table prime orbit catalogue; signed derivative reserve; analytic continuum bounds; independent Fraction spectra and rational logarithm signs; explicit four-input prime obstruction',
 'mathematical_delta':'All 104 ternary primes closed over every interior product law at sharp Cstar=2+4/ln2; universal signed singleton reserve proved; proposed higher-degree reserve companion refuted on prime mask33152 with gap>13/100. All-arity corrected prime bound and FEI open.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT; NEW_CLAIM_REVIEW_PENDING; SOURCE_REVIEWS_SCOPED',
 'mathematical_status':'TERNARY_CONTINUUM_SHARP_CONSTANT_PROVED; COMPANION_REFUTED_ON_QUATERNARY_PRIME; ALL_ARITY_AND_FULL_FEI_OPEN',
 'claim_versions_used':deps,
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1},{'claim_id':reviews[0]['claim_id'],'version':1,'change':'local scoped upper-bound review only; source unchanged'}],
 'source_artifacts':['REPORT.md','CORE_PROOF.md','REVIEW_MAJORITY.md','REVIEW_MUX.md','out/catalogue.json','out/proof_checks.json','out/prime_obstruction.json','out/source_receipts.json','out/review_records.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'Derive or obstruct a cofactor-sensitive higher-degree payment retaining actual unused singleton slack, beginning with the explicit prime mask33152 over all biases; A042/A091 independently review three new orbit bounds and A044/A090 replay prime obstruction.',
 'stagnant_substantive_attempts':0,
 'blockers':[], 'packet_ids':['A043']}
save(ROOT/'PROGRESS.json',progress)
(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())

(AGENT/'STATUS.md').write_text(
 'STATE: A043 stage 3 complete: all 104 ternary primes have sharp all-bias corrected constant 2+4/ln2; signed singleton reserve proved; its higher-degree companion refuted on prime mask33152; new claim review pending; full FEI OPEN.\n'
 'NEXT: Review three new orbit bounds and exact prime obstruction; derive cofactor-sensitive higher-degree payment retaining unused singleton slack, starting with mask33152 over all biases.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n## {STAMP} — stage {RUN}\nRead updated BOARD/lead and originals; scoped majority upper-bound and mux checkpoint reconstructions hold (shared majority lower path excluded from independent acceptance). Exact catalogue: five orbits, 104 ternary primes, 116 assertions. Closed remaining all-equal/exact-one/mask25 orbits at sharp Cstar=2+4/ln2 using signed singleton reserve; Fraction/log checker passed 1,760 cases and 56,661 assertions in 18.612 seconds. Proposed higher-degree companion fails even on explicit prime33152: certified gap>13/100, actual total corrected margin>9/20; 64 final assertions. Saved analytic proofs, scoped reviews, protocol files and rolling state locally; full FEI and all-arity biased-prime optimum open. No heavy job, git or external write.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''
## Stage 3 durable results (20261013T233947Z)
- Signed singleton reserve for every Boolean sign and interior product law: E_single<=4delta-2R, R=sum_{|S|>=3}(|S|-2)P(S). Half-difference D_i in {-1,0,1} gives Var(D_i)>=|E D_i|(1-|E D_i|); h(c)<=2|c|(1-|c|); sum by Parseval. No monotonicity needed.
- All 104 ternary primes form five exact input/output symmetry orbits, masks22,23,24,25,27 with sizes16,8,8,48,24. All have sharp corrected product-bias supremum Cstar=2+4/ln2. Majority/mux sources reconstructed; remaining three closed here.
- Exact-one orbit22: c_ij=(3m_k-1)/4,c123=3/4; each pair excess <=(2/3)T, giving E<=(4+ln4)delta-ln9*T. Path(1-q^3,q,q) reaches Cstar.
- All-equal orbit24: c_ij=1/2,T=0; h(|(a+b)/2|)<=[(1-a^2)+(1-b^2)]/2. All equal rare probabilities reach Cstar.
- Mask25: c12=1-p3/2,c13=-p2/2,c23=-p1/2,c123=-1/4. Distinguished pair pays -2T, others need +2T each; triple ln16*T, singleton reserve -2T cancel. Path(q,q,1-q^3) reaches Cstar. Do not discard the distinguished negative credit.
- Read-once gates of fan-in<=3 close by exact nonnegative-weight corrected entropy/deficit composition; uniform physical inputs give ordinary H<=Cstar I. This ordinary constant is not asserted optimal.
- False even on primes: E_ge2<=ln4*delta+2R. Explicit essential prime33152 positive at7,8,15; p=(1/2,1/2,1/2,1/1024), delta=5257209/16777216,R=262911/4194304; exact log gap>13/100. Its AND3 slice explains the failure. Actual total corrected margin>9/20, so the witness is not an FEI counterexample. Retaining singleton slack is the required new mechanism.
- Review independence: A043 supplied earlier majority lower path, so only reconstructed majority upper bound/orbit counts as independent acceptance; not its bundled corner errors or shared sharpness input. Mux checkpoint review excludes generalized profile-transfer claims.
''')

spec=json.loads(protocol.read_text(encoding='utf-8'))['required_per_run']
claimfields=set(spec['claim_fields'])
progressfields={k.split(' (')[0] for k in spec['progress_fields']}
assert set(claim)==claimfields
assert set(progress)==progressfields
assert claim['statement_sha256']==canonical(claim['exact_statement'],claim['hypotheses'])
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
for required in ['REPORT.md','CORE_PROOF.md','REVIEW_MAJORITY.md','REVIEW_MUX.md','out/catalogue.json','out/proof_checks.json','out/prime_obstruction.json']:
    assert (ROOT/required).is_file()
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (ROOT/'REPORT.md').read_text(encoding='utf-8').strip().splitlines()[-1].startswith('**Universal bridge:**')
assert json.loads((ROOT/'out/proof_checks.json').read_text())['all_passed']
assert json.loads((ROOT/'out/prime_obstruction.json').read_text())['all_passed']
files=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and p.name!='persistence_validation.json':
        assert p.stat().st_size<20*1024*1024
        files.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())})
save(ROOT/'out/persistence_validation.json',{'validated_at':STAMP,'all_passed':True,
 'checks':['exact claim and progress schema fields','canonical statement hash','byte-identical compatibility delta','required proof/output files','two-line STATUS','final Universal bridge paragraph','passed exact checker outputs','every file below20MB'],
 'local_receipts':files,'external_copy_status':'NOT_PERFORMED; supervisor pending','independent_review_of_new_claim':'PENDING'})
print(json.dumps({'saved_run':RUN,'claim':claim['claim_id'],'statement_sha256':claim['statement_sha256'],'files_checked':len(files),'schemas_and_receipts_passed':True}))
