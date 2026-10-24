from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
agent=root.parents[1]
base=Path(r'~\mop_fei100')
workers=Path(r'~\brain_workers\FEI100_20261011')
protocol=json.loads((base/'reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(root/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
baseline=base/'research_pushes/2026-10-11-full-fei-100-agents/baseline/current-threshold-paper.tex'
sources=[
    (base/'reports/fei-2026-10-11/EXECUTION_PROTOCOL.json','protocol revision 2026-10-11-execution-v2'),
    (workers/'claude/B09/STREAM_NOTES.md','lead v1: two-weight target and prime bridge'),
    (workers/'BOARD.md','coordination read at stage intake; latest local snapshot hash'),
    (baseline,'bias:strong, bias:eq-5-1, coefficient inequality (62)'),
    (workers/'context/threshold_paper_38pp.txt','Theorem 6.6 and equation (62); cp1252 text'),
    (base/'reports/fei-2026-10-11/source_material/reductions/paper/biased.tex','biasfull:weightedcounter, creditremark, localTC, composition'),
    (workers/'agents/A043/runs/20261011T221757Z-account05-A043-prime-gate-decomposition/REPORT.md','cofactor criterion, inherited-bias prime endpoint')]
save('out/SOURCE_RECEIPTS.json',[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'locator':loc} for p,loc in sources])

ln2_lower=2*sum(F(1,(2*k+1)*3**(2*k+1)) for k in range(4))
assert ln2_lower>F(3715,5360)
e_lower=sum(F(1,d) for d in (1,1,2,6))
assert e_lower==F(8,3)
constant_upper=F(320)+(1856+4/e_lower)/ln2_lower
assert constant_upper<3000
save('out/CONSTANT_CERTIFICATE.json',{'ln2_strict_lower_bound':str(ln2_lower),
    'e_strict_lower_bound':str(e_lower),'C_bits_strict_upper_bound':str(constant_upper),
    'verified': '320+(1856+4/e)/ln2 < 3000',
    'arithmetic':'Exact Fraction; omitted positive series terms supply strictness'})

statement=(
    'Let X~Ber(p) be independent of arbitrary product-biased bits Y_1,...,Y_n and '
    'F=2*1{w X+sum_j Y_j>=t}-1, with arbitrary n>=0, real w>0,t, and all interior biases. '
    'With v_i=4q_i(1-q_i), P(S)=fhat_mu(S)^2 in the orthonormal product basis, '
    'Delta=I_mu-Var_mu and c=460+80 ln 2, the higher-degree corrected entropy in nats '
    'E_ge2=sum_{|S|>=2}P(S)ln(v_S/P(S)) satisfies E_ge2(F)<=(4c+12+4/e)Delta(F); '
    'corrected FEI+ in bits satisfies Hplus_mu(F)<=[(4c+16+4/e)/ln 2]Delta(F), with that '
    'constant strictly below 3000. Endpoints are contracted. This includes the '
    'essential disjoint-composition-prime family 2*1{2X+sum_{j=1}^n Y_j>=3}-1 for every n>=3. '
    'For arbitrary two-weight groups, merge identical B slices f_s into probabilities pi_s. '
    'Their deficit Gram matrix has diagonal Delta(f_s) and off-diagonal -Cov(f_s,f_u), is PSD, '
    'and yields 2 sum_{s<u}pi_s pi_u Cov(f_s,f_u)<=sum_s pi_s^2 Delta(f_s). '
    'Mixed spectral B-energy is exactly sum_s pi_s(1-pi_s)I(f_s)<=Delta(F), and '
    'Delta(F)=sum_s pi_s Delta(f_s)+[I_A(F)-Var_A(E_B F)] with a nonnegative bracket. '
    'Those overlapping energy ledgers do not assert entropy control for arbitrary |A|. '
    'The full two-weight, all-prime and full FEI targets remain open.')
hypotheses=['actual Boolean thresholds on independent product inputs',
    'one exceptional physical input for the entropy theorem; arbitrary finite groups for the Gram/energy interface',
    'arbitrary real positive weight and threshold; zero/signed/deterministic inputs reduced by contraction/orientation',
    'orthonormal product Fourier basis; natural logarithms for E and bits for Hplus',
    'source-complete symmetric-threshold baseline E<=c Delta at bias:strong']
claim={'claim_id':'A041-COHERENT-TWO-WEIGHT-SLICE-APPLICATION','version':1,
    'exact_statement':statement,'hypotheses':hypotheses,
    'statement_sha256':hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
    'contributors':['account05/A041'],
    'proof_source':{'path':str(root/'SLICE_DEFICIT_PAYMENT.tex'),'sha256':sha(root/'SLICE_DEFICIT_PAYMENT.tex')},
    'proof_dependencies':[{'source':str(baseline),'sha256':sha(baseline),'locator':'bias:strong',
        'exact_statement':'E(g)<=(460+80 ln 2)Delta(g) for every symmetric threshold at every product bias',
        'status':'PROVED_BASELINE; source theorem application'}],
    'review_records':[],'status':'AUTHOR_PROVED_SCOPED_APPLICATION_PENDING_INDEPENDENT_REVIEW',
    'supersedes':[],'refutes':[],'first_unproved_line':None,
    'next_consumers':['A042','A044','A045','A084','A090','A091','B09','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save('CLAIMS.json',[claim])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':root.name,'stream':'B09','packet_id':'A041',
    'gap_id':'G-BIASED-LTF','attempt_id':'A041-BIASED-LTF-02-COHERENT-SLICE-DEFICIT',
    'method':'Disjoint pivotal-boundary cross-Dirichlet cancellation; PSD deficit Gram matrix; coherent coefficient entropy with overhead restricted to high-degree mass',
    'mathematical_delta':'Proved E_ge2<=K Delta and corrected FEI+ constant <3000 for one exceptional weighted input, arbitrary arity/real weight/all biases; proved unbounded prime-family admission; exact full two-group covariance and mixed-energy ledger. General multi-slice entropy normalization remains unpaid.',
    'deliverable_status':'COMPLETE_LOCAL_SCOPED_APPLICATION_REVIEW_PENDING',
    'mathematical_status':'ONE_EXCEPTIONAL_INPUT_TARGET_PROVED; FULL_TWO_WEIGHT_AND_UNIVERSAL_PRIME_FEIPLUS_OPEN',
    'claim_versions_used':[{'source':str(baseline),'sha256':sha(baseline),'locator':'bias:strong','status':'PROVED_BASELINE'}],
    'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1}],
    'source_artifacts':['REPORT.md','SLICE_DEFICIT_PAYMENT.tex','WEIGHTED_GUARD_LEDGER.md',
        'out/EXACT_SLICES.json','out/PRIME_FIXTURE.json','out/CONSTANT_CERTIFICATE.json','out/SOURCE_RECEIPTS.json'],
    'next_consumers':['A042','A044','A045','A084','A090','A091','B09','B20'],
    'next_action':'A091/A090 independently review; construct one normalized coherent multi-slice spectral reference paid by the exact root deficit ledger, keeping the pure-heavy sector and no double spending.',
    'stagnant_substantive_attempts':0,'blockers':[],'packet_ids':['A041']}
assert set(progress)=={s.split(' (',1)[0] for s in protocol['required_per_run']['progress_fields']}
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()

(agent/'STATUS.md').write_text(
    'STATE: Stage 2 complete locally: one-exceptional-weight all-bias FEI+ C<3000 and unbounded prime family proved; full two-group deficit Gram/mixed-energy identities; 436 cases/27,188 exact assertions; review pending; full FEI OPEN.\n'
    'NEXT: A091/A090 review; pay the coherent multi-slice spectral-set entropy plus pure-heavy sector using one normalized reference and the nonreused root deficit, instead of enlarging isolated classes.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-11 23:28Z stage 2 completed: Followed B09 two-weight direction. Distinct symmetric tails have zero cross Dirichlet form and covariance <=sqrt(Delta0 Delta1). Their band deficit <=2(sum tail deficits), sharp on AND2/OR2. Proved one-exceptional real-weight corrected FEI+ C<3000 at all arities/biases; proved family weights (2,1,...,1), threshold 3, prime for all n_light>=3. Full two-weight PSD slice Gram and mixed-energy ledgers are exact; entropy interference remains open. Pilot v1 had a serialization digit-cap failure; v1.1 exact outward fixed-grid compression passed 436 cases, 27,188 assertions in 1.670s. Ten-block prime fixture and rational constant certificate PASS. No endpoint/rank work repeated. Saved complete stage package; independent review pending.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\n## Stage 2: coherent two-weight slices\n\n'
    '* Distinct symmetric count tails have disjoint pivotal boundaries per coordinate at every product bias. Their cross Dirichlet form is zero, so positive covariance equals minus their high-degree deficit inner product and is <=sqrt(Delta0 Delta1).\n'
    '* The band sign g=f1-f0-1 satisfies Delta(g)=Delta0+Delta1+2Cov<=2(Delta0+Delta1); factor two is sharp on uniform AND2/OR2. Apply coherent scalar entropy only to high degree so its norm overhead costs deficit, not raw variance.\n'
    '* Singleton corrected entropy <=4 Delta nats for EVERY Boolean sign, not just monotone: signed derivative mean has magnitude at most pivotal probability.\n'
    '* For F=2*1{wX+sum Y>=t}-1 with ONE exceptional physical input, all arities/real w/all biases: E_ge2<=(4c+12+4/e)Delta and Hplus<=[(4c+16+4/e)/ln2]Delta<3000Delta, c=460+80ln2. This uses the symmetric-threshold baseline, not conditional-input TC or an assumed weighted gate theorem.\n'
    '* Family weights (2,1,...,1), threshold 3, n_light>=3 is composition-prime: every proper substituted block of size >=2 has >=3 cofactor rows. Thus the theorem covers an unbounded nonsymmetric prime family, without closing all primes.\n'
    '* For arbitrary two-weight groups, merge identical B slices. Deficit Gram G has diagonal Delta_s and off-diagonal -Cov_su and is PSD; 2sum pi_s pi_u Cov_su<=sum pi_s^2 Delta_s. Mixed B-energy=sum pi_s(1-pi_s)I_s<=Delta(F).\n'
    '* Full ledger: Delta(F)=sum pi_s Delta_s+delta_A, delta_A=I_A-Var_A(E_B F)>=0. Mixed-energy and averaged-slice bounds overlap; never add them as extra reserves. A mixed set gets exactly (|S_A|+|S_B|-1)P(S) in the root deficit.\n'
    '* Exact remaining gap: normalized logarithmic cost of coherent sum sum_s chat_s(S_A)fhat_s(S_B), including pure-heavy high degree. Binary induction multiplies constants and does not prove arity-uniform full two-weight FEI+.\n'
    '* When exact entropy Fraction endpoints exceed serialization digit limits, outward projection onto a fixed rational grid preserves certification without modifying internal arithmetic or escalating precision.\n')
receipts=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in (agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md'):
    receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
save('out/PERSISTENCE_RECEIPTS.json',{'saved_at_utc':datetime.now(timezone.utc).isoformat(),
    'protocol_fields_checked':True,'claim_count':1,'progress_delta_identical':True,
    'local_only':True,'artifacts':receipts})
print(json.dumps({'status':'PASS','claim_count':1,'claim_fields':len(claim),'progress_fields':len(progress),
    'receipt_count':len(receipts),'largest_bytes':max(r['bytes'] for r in receipts),
    'C_bits_certified_less_than':3000},indent=2))
