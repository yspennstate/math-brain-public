from pathlib import Path
from fractions import Fraction
import json
import re

base = Path(__file__).resolve().parent
namespace = 'probability.functional'
source = {
    'source_id':'owner:w348:p0017-core-proof-20261010',
    'url':'urn:owner-work:w348:P0017:20261010',
    'revision':'2026-10-10; prover-written, independent review pending',
    'license':'owner-own-work; campaign proof and refuted-route packet, review pending',
    'excerpt':None}


def entry(key, logical, title, statement, assumptions):
    return {'key':key,'namespace':namespace,'logical_name':logical,
            'kind':'concept','title':title,'statement':statement,
            'proof_text':None,'assumptions':assumptions,
            'domain':'probability theory and Hilbert tensor algebra','source':dict(source)}


pending = 'Prover-written mathematical claim; independent review pending. '
entries = [
entry('p0017-status','kls-p0017-reported-resolution-audit-status',
      'P0017 KLS: October proof claims and prior Gaussian-only attempt',
      'Source-status draft, not a full-proof verdict. P0017 asks for a universal C with Var_mu(f)<=C integral |grad f|^2 dmu for every isotropic log-concave probability mu in every dimension. Isotropic means mean zero and covariance I. The older owner campaign attempt established only the standard Gaussian case using Hermite expansion and explicitly left the general log-concave case unresolved. Bizeul, Klartag and Lehec arXiv:2610.05474v1 Theorem 1.1 and Song, Zhang arXiv:2610.01447v2 report a full KLS resolution on 2026-10-04. These primary claims have not received a complete independent audit in this packet. Current openness is UNKNOWN pending audit; no new full-KLS proof or novelty is claimed by w348.',
      ['Status checked on 2026-10-10','Dated September ranking is not current proof-status evidence']),
entry('tilt-tensor','normalized-ordered-tilt-taylor-tensor',
      'Normalized ordered Taylor tensor of an exponential tilt average',
      'For a centered probability mu on R^n with exponential moments in a neighborhood of zero and f in L2(mu), define F_f(z)=integral f(x)exp(<z,x>) dmu(x)/integral exp(<z,x>) dmu(x) near zero. The degree-d Taylor tensor is T_d f=(1/d!)D^d F_f(0). Its Hilbert--Schmidt norm sums the squares of all n^d ordered-index entries. For a multi-index alpha of total degree d, if c_alpha is the coefficient of z^alpha in F_f, those entries equal (alpha!/d!)c_alpha, and their multiplicity is d!/alpha!. Thus ||T_df||^2=sum_{|alpha|=d}(alpha!/d!)|c_alpha|^2.',
      ['d>=1 integer','f in L2(mu)','Local exponential integrability; choose a smaller neighborhood for the L2 tilt kernel']),
entry('block-recovery','sharp-binomial-block-symmetric-tensor-recovery-draft',
      'Sharp block-symmetric tensor recovery, review pending',
      pending+'Let H,W be finite-dimensional real Hilbert spaces, 1<=p<=q, and T in H^(tensor(p+q)) tensor W. Assume T is symmetric in its first p positions and separately its next q positions. If P_q averages permutations of the first q positions, leaving all others fixed, then ||T||<=binom(q,p)||P_qT|| in the Hilbert tensor norm. The factor is optimal when dim H>=2 and W is nonzero. The case p=d,q=2d has factor binom(2d,d); BKL Lemma 2.2 already obtains this factor in its proof before stating the coarser 4^d bound. Complete incidence-identity and explicit sharpness proofs are in w348/ATTEMPT.md L1; this is not a full KLS proof.',
      ['Both specified block symmetries','Ordered Hilbert tensor norm','Optimality requires dim H>=2 and W nonzero']),
entry('robust-recovery','approximate-block-symmetry-tensor-recovery-draft',
      'Approximate block symmetry and a recovery-kernel counterexample',
      pending+'Let 1<=p<=q and T in H^(tensor(p+q)) tensor W be symmetric in the first p positions. Let Q average the next q positions, P_q average the first q positions, delta=||T-QT||, and b=binom(q,p). Then ||T||<=b||P_qT||+(b+1)delta. The two original block projections commute, so the sharp two-block bound applies to QT. Without the second block symmetry, a zero-error recovery estimate fails: for p=1,q=2,H=R^2, T=(e0 tensor e1-e1 tensor e0) tensor e0 is nonzero but P_2T=0. The error coefficient b+1 is a valid bound whose optimality is not claimed.',
      ['Finite-dimensional real Hilbert spaces','First p block symmetry','Projection averages have the indicated positions']),
entry('universal-input','kls-universal-tilt-taylor-input-review-gap',
      'KLS route: universal all-degree tilt input remains unaudited here',
      'Unproved input in the w348 packet. The full analytic statement sought is one universal R>=1 such that every centered full-dimensional log-concave probability mu with Cov(mu)<=I, every f in L2(mu), and every d>=1 satisfy ||T_df||_HS<=R^d||f||_2 for the normalized ordered tilt Taylor tensor. On the regular subclass used by BKL, Theorem 3.1 of arXiv:2610.05474v1 states that this input implies C_P(mu)<=C R^2 with a numerical C. That reduction, its general-measure approximation, and the Cheeger comparison are externally supplied steps here. The general all-degree input is not established or independently audited by this packet; published authors claim to establish it through cumulants and suspension.',
      ['Centered log-concave mu with Cov<=I','All degrees and all L2 functions, in Hilbert--Schmidt norm','BKL criterion application requires its regularity assumptions']),
entry('exp-product','exact-exponential-product-tilt-taylor-operator-norm-draft',
      'Exact all-degree tilt norm for centered exponential products',
      pending+'Let Y_1,...,Y_n be independent Exp(1) variables, X_i=Y_i-1, and mu the law of X. For every n>=1 and d>=1, the operator f -> T_df=(1/d!)D^dF_f(0), from L2(mu) to the ordered-index Hilbert--Schmidt tensor space, has norm exactly sqrt(binom(2d-2,d-1)). Thus ||T_df||<=2^(d-1)||f||_2 and R=2 is the smallest base valid in ||T_df||<=R^d||f||_2 for all degrees in this family. Equality is attained by the normalized one-coordinate polynomial P_d(Y_1), where P_d(y)=y^d/d!-y^(d-1)/(d-1)!. The proof separates orthogonal coordinate supports before bounding each positive frame-operator trace. The law is isotropic and log-concave but nonsmooth, so this direct calculation does not invoke the regularity-dependent BKL criterion. It does not supply the input for arbitrary log-concave laws.',
      ['Independent centered Exp(1) product law','f in L2(mu)','Ordered-index tensor normalization includes 1/d!','All d>=1']),
entry('degree-two','tilt-degree-two-quadratic-variance-duality-draft',
      'Degree-two tilt bound is a quadratic-form variance bound',
      pending+'For a centered isotropic probability mu on R^n with finite fourth moments, define U_2f=(1/2)E[f(X)(X tensor X-I)]. Then ||U_2||_(L2->HS)=(1/2)sup_{A=A^T,||A||_HS=1}sqrt(Var_mu(<AX,X>)). If local exponential moments exist, U_2 equals the actual normalized tilt Taylor tensor operator T_2. Thus even degree two of a universal tilt bound requires a dimension-free quadratic-form variance estimate. Isotropy alone is insufficient: the non-log-concave law with mass 1/(2M) at each of +/-sqrt(M) and remaining mass at zero has Var(X)=1 but ||U_2||^2=(M-1)/4. Finite fourth moments alone do not define exponential tilts near zero.',
      ['Centered isotropic mu','Finite fourth moments','Local exponential integrability additionally required to identify U_2 with a tilt derivative'])]

relations = [
 {'from_key':'robust-recovery','to_key':'block-recovery','kind':'depends_on',
  'rationale':'The robust card says "the sharp two-block bound applies to QT"; the block card assumes the first p and next q block symmetries, which QT has.'},
 {'from_key':'exp-product','to_key':'tilt-tensor','kind':'depends_on',
  'rationale':'The exponential-product statement uses "T_df=(1/d!)D^dF_f(0)" and the definition supplies the ordered multiplicity weights alpha!/d!.'},
 {'from_key':'degree-two','to_key':'tilt-tensor','kind':'depends_on',
  'rationale':'The quadratic card identifies U_2 with the normalized Taylor tensor only "if local exponential moments exist"; the definition requires that same local integrability.'},
 {'from_key':'universal-input','to_key':'tilt-tensor','kind':'depends_on',
  'rationale':'The input quantifies over "the normalized ordered tilt Taylor tensor"; the definition gives its normalization and Hilbert--Schmidt norm.'},
 {'from_key':'exp-product','to_key':'universal-input','kind':'specializes',
  'rationale':'The input quantifies over every centered log-concave covariance<=I law. The exponential-product card states its law is isotropic and log-concave and proves the same all-degree inequality for that family only.'},
 {'from_key':'p0017-status','to_existing_logical':'math:probability.core:open-problem-p0017-dimension-free-log-concave-poincare-or-cheeger-constant','kind':'cites',
  'rationale':'Read-only recovery of the existing P0017 card quotes "current status unverified; result status attempted_unsolved". The new status card attributes October primary proof claims and explicitly keeps independent audit pending.'}]

bundle = {'spec':'mathbrain-draft-v1','author_agent':'w348',
          'bundle_slug':'p0017-sharp-tensor-recovery-exponential-tilts-001',
          'entries':entries,'relations':relations}
keys={e['key'] for e in entries}
assert len(keys)==len(entries)<=200
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
for e in entries:
    assert e['kind']=='concept' and e['proof_text'] is None
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
    assert e['source']['license'].startswith('owner-own-work')
    assert len(e['statement'])>100 and e['assumptions']
for r in relations:
    assert r['from_key'] in keys and r['kind'] in allowed and r['rationale']
    assert ('to_key' in r) != ('to_existing_logical' in r)
    if 'to_key' in r: assert r['to_key'] in keys
graph={k:[] for k in keys}
for r in relations:
    if r['kind']=='depends_on' and 'to_key' in r: graph[r['from_key']].append(r['to_key'])
def visit(k,trail):
    assert k not in trail, 'dependency cycle'
    for target in graph[k]: visit(target,trail|{k})
for k in keys: visit(k,set())

draft_dir=base/'drafts'
draft_dir.mkdir(exist_ok=True)
draft_file=draft_dir/'bundle_001.json'
draft_file.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
status=json.loads((base/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status['brain_states']['prepared']=True
status['original_primary_source']={
 'id':'arxiv:2603.29571v1','url':'https://arxiv.org/html/2603.29571v1',
 'locator':'Entry 13, Conjecture 30','license':'CC-BY-4.0',
 'statement_recovered':'h(mu)>=c/sqrt(||Cov(mu)||_op); in isotropic position h(mu)>=c',
 'notation_note':'The printed halfspace display mixes H and S; the adjacent covariance-normalized formulation is explicit and is used here.'}
status['owner_prior_work_check']={
 'result':'GAUSSIAN_ONLY_ATTEMPT_RECOVERED; NO FULL OWNER PROOF FOUND IN TARGETED NAMED RECORDS',
 'prior_problem_node':'claim_d2e9e3d859a16e515c09803220b9b26608e8a6b5a6ce584d2e99cf6613f89694',
 'prior_attempt_node':'claim_fbc7554cdcce8efc8484f98a5982f7add13464aa5d5d53dfb9ca2710fc43e19f',
 'database_mode':'ro','record_file':'checks/prior_records.json',
 'coverage':'Named intake records, H/I attempt directories, Lean annotated ranking, two owner solved registers, and targeted population-store P0017 cards. Not an exhaustive owner-work or novelty audit.'}
status['compute_check']={'receipt':'checks/compute_gate.json','results':'checks/exact_results.json'}
status['submission']={'draft_file':'drafts/bundle_001.json','intended_path':'~/math-brain-inbox/w348/bundle_001.json','entry_kind':'concept','theorem_promotion_allowed':False}
(base/'SOURCE_STATUS.json').write_text(json.dumps(status,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

claim_file=base/'CLAIMS.jsonl'
claims=[json.loads(line) for line in claim_file.read_text(encoding='utf-8').splitlines() if line.strip()]
for c in claims:
    if c['claim_id']=='w348-L4':
        c['statement']='For a centered isotropic law with finite fourth moments, U_2f=(1/2)E[f(X)(X tensor X-I)] has operator norm (1/2)sup_(A=A^T,||A||_HS=1)sqrt(Var(<AX,X>)). With exponential moments near zero, U_2 is the actual tilt Taylor operator T_2.'
    if c['claim_id'].startswith('w348-L'):
        c['validation_receipt']='checks/exact_results.json; finite arithmetic only, independent review pending'
claim_file.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')

results=json.loads((base/'checks'/'exact_results.json').read_text(encoding='utf-8'))
assert results['status']=='PASS'
validation={'status':'PASS','entries':len(entries),'relations':len(relations),
            'claim_rows':len(claims),'all_entries_review_pending_concepts':True,
            'allowed_relations':True,'acyclic_depends_on':True,
            'source_license_prefixes_accepted':True,'structural_check_only':True,
            'independent_mathematical_review':'PENDING','full_KLS_proof':False}
(base/'checks'/'bundle_validation.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')

hook={
 'id':'tensor-recovery-w348-01','area':'math','event':'stage-start',
 'cue':'A proof recovers an unsymmetrized tensor norm from a partial-symmetrization norm.',
 'fire_when':'A partial-symmetry recovery bound is asserted with only one block symmetry; p=1,q=2 has a nonzero tensor in the projection kernel.',
 'silent_when':'Both original block symmetries are explicit and verified, or no recovery inequality is asserted.',
 'text':'Before recovering a tensor from partial symmetrization, check both block symmetries and the ordered-index norm. One block alone leaves a nonzero kernel; carry the approximate-symmetry error explicitly.',
 'evidence':'w348/ATTEMPT.md L2; checks/exact_results.json missing_symmetry_control: norm_squared=2, projected_norm_squared=0; scar perceptron_proof_open_gaps_fleet_2026_07_12',
 'proposer':'w348'}
assert len(hook['text'])<=300
(base/'HOOK_PROPOSAL.jsonl').write_text(json.dumps(hook)+'\n',encoding='utf-8')
metrics={'status':'PASS','before':'Old P0017 brain attempt: Gaussian Hermite special case only; published stated recovery bound 4^d.',
 'after':'Prepared prover-written all-degree exponential-product proof and sharp general tensor recovery, with an explicit full-target gap.',
 'finite_exact_checks':{k:v for k,v in results['checks'].items() if k.endswith('_cases')},
 'elapsed_compute_seconds':results['elapsed_compute_seconds'],
 'd8_recovery':{'stated_bound':65536,'sharp_bound':12870,
                'ratio':str(Fraction(65536,12870)),
                'note':'The binomial upper bound is already in BKL proof; no novelty or algorithm-runtime claim.'},
 'draft_entries':len(entries),'draft_relations':len(relations),
 'independently_accepted_results':0,'live_store_writes_by_w348':0,
 'submitted':False,'reviewed':False,'ingested':False,'retrievable':False}
(base/'METRICS.json').write_text(json.dumps(metrics,indent=2)+'\n',encoding='utf-8')
print(json.dumps(validation))
