"""Initial staging receipt. After the L4 repair use fix_tilt_domain.py and validate_packet.py; do not reinitialize the corrected handoff. No live database is opened for writing."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
from math import comb

ROOT=Path(__file__).resolve().parent
BASE=Path('~')
now=datetime.now(timezone.utc).isoformat()
for name in ['drafts','patches','reviews','measurements']:(ROOT/name).mkdir(exist_ok=True)

def write_json(path,data):
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def append_unique(path,rows):
    old=[]
    if path.exists():old=[json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    known={r.get('id') for r in old}
    with path.open('a',encoding='utf-8') as f:
        for row in rows:
            if row['id'] not in known:f.write(json.dumps(row,ensure_ascii=False)+'\n');known.add(row['id'])

late=[
 {'id':'w350-R349-W1','subject':'w349 WEIGHTED_GAP.md posterior factorization counterexample','verdict':'KEEP','reviewer':'w350','exact_scope':'X=Exp(1)-1, s>0, Y=sX+sqrt(s)Z, independent standard Gaussian Z, fixed f(x)=x. Mathematical strictness only; the reported quadrature value is not independently certified by w350.','independent_reproduction':'The posterior is N((y-1)/s,1/s) truncated at -1. At y=1-s its variance is (1-2/pi)/s; as y tends to positive infinity it tends to 1/s. The variance A(y) is continuous, so it is nonconstant. Y has positive density everywhere and 0<A<=1/s, hence Var(A(Y))>0. The proposed bound reduces to E A^2 <= (E A)^2 and is strictly false.','remaining_gap':'Does not refute the correctly weighted bound or KLS.'},
 {'id':'w350-R349-W2','subject':'w349 WEIGHTED_GAP.md conditional Gronwall reduction','verdict':'KEEP','reviewer':'w350','exact_scope':'Full-dimensional compactly supported isotropic log-concave prior; smooth f; assumed uniform T>0 and K>=0 with E|Cov_mu_t(f,X)|^2 <= K E Var_mu_t(f) for almost every t<T.','independent_reproduction':'Innovation Y_t-integral a_r dr has zero conditional drift and bracket tI; compact support gives integrability, so Levy identifies a Brownian motion. Bayes/Ito gives d(mu_t f)=Cov_mu_t(f,X).dW_t. Ito isometry and total variance give V(t)=V(0)-integral E|Cov|^2. The assumed inequality implies V(T)>=exp(-KT)V(0). Posterior curvature T gives V(T)<=energy/T by generalized strong-log-concavity Poincare. For extension, truncate an arbitrary prior on expanding balls and whiten. Its means converge to 0 and covariance matrices Sigma_j converge to I; transfer the bound to the unwhitened conditional laws with factor ||Sigma_j||, then pass compact smooth tests to the limit.','remaining_gap':'The weighted all-function input and the generalized strong-log-concavity Poincare inequality are explicit external inputs; no parent proof is claimed.'}
]
append_unique(ROOT/'reviews'/'w349_verdicts.jsonl',late)
peer_reviews=[]
for filename in ['w348_verdicts.jsonl','w349_verdicts.jsonl']:
    peer_reviews.extend(json.loads(s) for s in (ROOT/'reviews'/filename).read_text(encoding='utf-8').splitlines() if s.strip())
assert len(peer_reviews)==11 and all(r['verdict']=='KEEP' for r in peer_reviews)

status=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status['exact_poincare_target']='There is a universal C<infinity such that, for every n>=1 and every isotropic log-concave probability measure mu on R^n, Var_mu(f)<=C integral |grad f|^2 dmu for all locally Lipschitz f in L^2(mu) with finite Dirichlet energy. Isotropy means mean 0 and Cov=I_n; extended convex potentials and convex supports are included.'
status['original_primary_source']={'title':'Randomstrasse101: Open Problems of 2025','url':'https://arxiv.org/html/2603.29571v1','location':'Conjecture 30, Entry 13 as named by the intake','statement_in_own_words':'The Euclidean Cheeger constant is bounded below by c/sqrt(||Cov(mu)||_op) for log-concave mu; in isotropic position this is a universal positive lower bound.','notation_warning':'This source uses psi_mu for the Cheeger constant itself. Klartag 2303.14938 uses psi_mu for its reciprocal. The direction must be translated before comparing bounds.'}
status['recent_primary_claims']=[
 {'authors':['Pierre Bizeul','Boaz Klartag','Joseph Lehec'],'url':'https://arxiv.org/html/2610.05474v1','posted':'2026-10-04','location':'Theorem 1.1','claim':'Universal dimension-free C_P for every isotropic log-concave law','full_proof_independently_checked':False},
 {'authors':['Z. Song','X. Zhang'],'url':'https://arxiv.org/abs/2610.01447v2','revision':'2026-10-04','claim':'An O(1) bound for the KLS constant','full_proof_independently_checked':False},
 status['recent_primary_claim']
]
status['reported_resolution']='YES: multiple October primary preprints claim the full target'
status['current_openness']='UNKNOWN'
status['current_status_detail']='Reported full resolution is verified as a primary-source claim. Complete mathematical proof validity has not been independently checked in this packet. Do not label the target currently open on the September ranking alone.'
status['prior_owner_solved_retired_status']={'historical_status':'attempted_unsolved','verified_evidence':'Intake op-p0017 and at-p0017; the latter is a Gaussian special case and explicitly leaves general log-concavity unresolved.','later_owner_status':'UNKNOWN; no P0017 solved/retired result appeared in the named H/I attempt folders under targeted ID search. This is not an exhaustive absence claim.'}
status['read_only_store_probe']='context/store_probe.json: two historical P0017 nodes; no matches for the four recorded distinctive-word probes. This is a limited deduplication probe, not proof of global absence.'
status['formal_check_receipt']=None
write_json(ROOT/'SOURCE_STATUS.json',status)

snapshots=[]
for rel in ['w348/ATTEMPT.md','w348/STATEMENT_FIRST.md','w349/INDEPENDENT.md','w349/WEIGHTED_GAP.md','w349/CLAIMS.jsonl']:
    p=BASE/'brain_workers'/rel
    if not p.exists():continue
    data=p.read_bytes()
    target=ROOT/'reviews'/('snapshot_'+rel.replace('/','_'))
    target.write_bytes(data)
    snapshots.append({'source':str(p),'snapshot':str(target),'sha256':hashlib.sha256(data).hexdigest(),'scope':'Only the named reviewed claims are covered; a source hash itself is not proof.'})
write_json(ROOT/'reviews'/'snapshot_provenance.json',snapshots)

channel_source={'source_id':'owner-probability-campaign-w350-20261010:gaussian-retention','url':'urn:owner-probability-campaign:P0017:w350:gaussian-retention','revision':'2026-10-10-draft-v1','license':'owner-own-work; campaign derivation; independent review requested from w353','excerpt':None}

def entry(key,logical,kind,title,statement,proof=None,assumptions=None,source=None):
    return {'key':key,'namespace':'probability.core','logical_name':logical,'kind':kind,'title':title,'statement':statement,'proof_text':proof,'assumptions':assumptions or [],'domain':'probability theory','source':source or channel_source}

own_entries=[
 entry('retention-definition','gaussian-observation-variance-retention-coefficient','definition','Gaussian observation variance retention','Let X have a full-dimensional probability law mu on R^n, let G be an independent N(0,I_n) vector, and let t>0. For Y=sqrt(t)X+G define R_mu(t)=inf E[Var(f(X)|Y)]/Var_mu(f), where the infimum is over all f in L^2(mu) with positive variance. The conditioning is on the Gaussian observation; no independence between coordinates of X is assumed.'),
 entry('forward-bridge','poincare-to-gaussian-observation-variance-retention','concept','Poincare implies Gaussian observation variance retention','DRAFT REDUCTION; independent review pending. If a probability law mu satisfies its Sobolev Poincare inequality with finite constant C, then R_mu(t)>=1/(1+Ct) for every t>0, with R defined using Y=sqrt(t)X+G and all L^2 functions. The constant C is an assumption in this direction. The proof in w350 ATTEMPT.md uses Gaussian Bessel inequality, prior Poincare, total variance and the adjoint of conditional expectation.',assumptions=['Finite prior Sobolev Poincare constant C','Independent standard Gaussian observation noise']),
 entry('reverse-bridge','gaussian-observation-variance-retention-to-poincare','concept','Gaussian observation variance retention implies Poincare','DRAFT REDUCTION; independent review pending. For a full-dimensional log-concave law mu, suppose deterministic t0>0 and eta>0 satisfy R_mu(t0)>=eta, with the infimum over all nonconstant L^2 functions. Then C_P(mu)<=1/(eta*t0). The posterior potential is V(x)+t0|x|^2/2-sqrt(t0)y.x, so its generalized strong-log-concavity Poincare bound is 1/t0. Average the posterior variance bound by the tower property, then combine with the assumed retention. The retention hypothesis is not proved in this packet.',assumptions=['Full-dimensional log-concave law on convex support','All-function retention R_mu(t0)>=eta>0','Generalized uniformly-log-concave Poincare input, Klartag 2303.14938v2 (1.7)']),
 entry('uniform-input','uniform-log-concave-gaussian-observation-variance-retention-input','concept','Uniform variance retention input for log-concave Poincare','UNPROVED INPUT IN THIS PACKET. Universal deterministic constants t0>0 and eta>0 are sought such that R_mu(t0)>=eta for every isotropic log-concave probability law in every dimension, where R takes an infimum over all L^2 test functions. Together with the recorded reductions this is equivalent, up to explicit constants, to a uniform Poincare bound. Linear or quadratic tests alone do not discharge this all-function hypothesis. Recent primary preprints claim the parent target; this packet has not audited their complete proofs.',assumptions=['Mean zero and covariance I_n','Log-concavity','All dimensions and all L^2 functions']),
 entry('gaussian-benchmark','standard-gaussian-observation-variance-retention-benchmark','concept','Exact Gaussian variance retention benchmark','GAUSSIAN SPECIAL CASE; independent review of the new bridge pending. For mu=N(0,I_n) and independent G=N(0,I_n), the channel Y=sqrt(t)X+G has R_mu(t)=1/(1+t). Sharp Gaussian C_P=1 gives the lower bound through the forward bridge; a unit linear function and posterior covariance I_n/(1+t) give equality. This checks channel normalization. The reverse bridge yields only C_P<=(1+t)/t, while the prior Hermite proof gives exact C_P=1.'),
 entry('source-status','p0017-october-2026-primary-resolution-claim-status','concept','P0017 primary-source status on 10 October 2026','SOURCE AUDIT, 2026-10-10. The September P0017 ranking records attempted_unsolved and its old attempt proves only the Gaussian special case. Randomstrasse101 2603.29571v1 Conjecture 30 states the log-concave Cheeger target. Bizeul-Klartag-Lehec 2610.05474v1 Theorem 1.1, Song-Zhang 2610.01447v2, and Balasubramanian-Kasiviswanathan 2610.07728v2 report dimension-free bounds. The existence of these claims is checked; their full proofs are not independently certified here. Current openness is UNKNOWN in this packet, with reported resolution YES. Randomstrasse psi is the Cheeger constant; Klartag 2303.14938 psi is its reciprocal.',source={'source_id':'owner-probability-campaign-w350-20261010:source-audit','url':'https://arxiv.org/html/2603.29571v1','revision':'as-read-2026-10-10','license':'owner-own-work; primary-source audit in own words','excerpt':None})
]
parent='math:probability.core:open-problem-p0017-dimension-free-log-concave-poincare-or-cheeger-constant'
attempt='math:probability.core:attempt-p0017-dimension-free-log-concave-poincare-or-cheeger-constant'
own_relations=[
 {'from_key':k,'to_key':'retention-definition','kind':'depends_on','rationale':'The statement uses the all-function coefficient R_mu(t) defined for the normalized Gaussian channel.'} for k in ['forward-bridge','reverse-bridge','uniform-input','gaussian-benchmark']
]+[
 {'from_key':'gaussian-benchmark','to_key':'forward-bridge','kind':'specializes','rationale':'The Gaussian law has sharp C_P=1 and attains the forward retention bound with a linear function.'},
 {'from_key':'uniform-input','to_key':'reverse-bridge','kind':'semantic_association','rationale':'A universal version of the retention hypothesis supplies the reverse bridge in every dimension; the input remains unproved here.'},
 {'from_key':'source-status','to_existing_logical':parent,'kind':'cites','rationale':'The historical P0017 target is the subject of the dated source-status audit.'},
 {'from_key':'gaussian-benchmark','to_existing_logical':attempt,'kind':'cites','rationale':'The existing at-p0017 Hermite special case supplies the exact Gaussian Poincare normalization.'}
]
own_bundle={'spec':'mathbrain-draft-v1','author_agent':'w350','bundle_slug':'p0017-gaussian-retention-and-source-status-w350-001','entries':own_entries,'relations':own_relations}
write_json(ROOT/'drafts'/'bundle_001.json',own_bundle)

peer_source=lambda worker,label:{'source_id':f'owner-probability-campaign-{worker}-20261010:{label}','url':f'urn:owner-probability-campaign:P0017:{worker}:{label}','revision':'2026-10-10-reviewed-by-w350','license':'owner-own-work; peer campaign result, independently reproduced by w350; additional account audit pending','excerpt':None}
peer_entries=[
 entry('tensor-recovery','sharp-symmetric-block-tensor-recovery','lemma','Sharp recovery from two tensor block symmetries','Let H,W be finite-dimensional real Hilbert spaces and 1<=p<=q. If T in H^(tensor(p+q)) tensor W is invariant under permutations of its first p positions and, separately, of its next q positions, and P_q averages permutations of the first q positions, then ||T||<=binom(q,p)||P_qT||. The constant is optimal for dim H>=2 and W nonzero. Norms are the induced Hilbert tensor norms.',proof='Associate to each p-subset F a permuted tensor T_F. Double expansion and Vandermonde give sum_{|E|=q}||sum_{F subset E}T_F||^2=sum_{s=0}^p binom(q-p,p-s)sum_{|S|=s}||sum_{F superset S}T_F||^2. The s=p term is sum_F||T_F||^2; all terms are nonnegative. Each left sum is binom(q,p) times a permutation of P_qT, proving the bound. For sharpness, in a two-dimensional orthonormal basis set the tensor component with p total ones and r ones in the first block to (-1)^r/binom(q,p-r), and all others to zero. A kth alternating binomial difference shows P_qT=(-1)^p RT/binom(q,p) for a block reversal R. Thus equality is attained. A separate disjointness-operator proof is saved in w350 reviews/w348_independent.md.',source=peer_source('w348','L1')),
 entry('exponential-tilt','centered-exponential-product-normalized-tilt-derivative-norm','lemma','Exact normalized tilt norm for exponential products','Let X_i=Y_i-1 for independent rate-one exponential Y_i, 1<=i<=n, and let mu be their joint law. For F_f(z)=E[f(X)e^(z.X)]/E[e^(z.X)] and T_d f=(1/d!)D^dF_f(0), using the ordered-index Hilbert-Schmidt norm, the operator norm from L^2(mu) to HS tensors is sqrt(binom(2d-2,d-1)) for every d>=1 and n>=1. The smallest base R valid in ||T_d f||<=R^d||f||_2 for all degrees is 2.',proof='The tilt kernel is product_i(1-z_i)e^(z_iY_i). Its coefficients P_0=1 and P_j=y^j/j!-y^(j-1)/(j-1)! are centered for j>=1 and satisfy E[P_jP_k]=binom(j+k-2,j-1). Ordered multiplicities give ||T_df||^2=sum_{|alpha|=d}(alpha!/d!)|<f,product P_alpha_i>|^2. Distinct coordinate supports are orthogonal by independence and centering. For one support of size s, the frame norm is at most its trace, bounded by binom(2(d-s),d-s)sum alpha!/d!. The factorial/composition bound sum alpha!/d!<=(d-s+1)/(d(s-1)!)<=1, so every block norm is <=binom(2d-2,d-1). Orthogonality means the maximum of block norms, with no support-count factor. The test f=P_d(Y_1)/sqrt(binom(2d-2,d-1)) attains equality. Central binomial bounds between 4^(d-1)/(2d-1) and 4^(d-1) give optimal base 2. This is a product special case, not general log-concavity.',source=peer_source('w348','L3')),
 entry('quadratic-duality','second-tilt-derivative-quadratic-variance-duality','lemma','Degree-two tilt norm and quadratic variance','Let mu be centered and isotropic in R^n with finite fourth moments. With T_2f=(1/2)D^2F_f(0), its L^2-to-Hilbert-Schmidt operator norm equals (1/2)sup_{A=A^T,||A||_HS=1}sqrt(Var_mu(X^TAX)).',proof='Twice differentiating the normalized tilt quotient gives T_2f=(1/2)E[f(XX^T-I)]. Pair with an HS-unit symmetric A. The functional is one half of the covariance with X^TAX, whose L2 norm is one half of the standard deviation. Interchanging the two suprema yields the identity, and the centered normalized quadratic attains each nonzero-variance functional norm. Antisymmetric matrices pair to zero.',source=peer_source('w348','L4')),
 entry('factorization-counterexample','shifted-exponential-posterior-variance-factorization-counterexample','lemma','Posterior variances cannot be factored in expectation','Let X=Exp(1)-1, s>0, and Y=sX+sqrt(s)Z for independent standard Gaussian Z. Write A(Y)=Var(X|Y). Then E[A(Y)^2]>(E[A(Y)])^2. In particular, for fixed f(x)=x, the bound E|Cov(f(X),X|Y)|^2<=(E||Cov(X|Y)||_op)(E Var(f(X)|Y)) is false, even for this isotropic log-concave prior and genuine Gaussian observation.',proof='The posterior density is proportional to exp((y-1)x-sx^2/2) on x>=-1, a truncated Gaussian with variance A(y). At y=1-s it is a half-normal translated to -1, with variance (1-2/pi)/s. As y tends to positive infinity the truncation disappears and A(y) tends to 1/s. The variance is continuous, so it is nonconstant; Y has positive density everywhere. Strong log-concavity gives 0<A(y)<=1/s, so A(Y) is square integrable and Var(A(Y))>0. The proposed inequality is exactly the reverse of this strict variance identity. No assertion about a correctly weighted estimate or a full KLS proof follows.',source=peer_source('w349','weighted-gap-counterexample'))
]
peer_bundle={'spec':'mathbrain-draft-v1','author_agent':'w350','bundle_slug':'p0017-peer-lemmas-reviewed-w350-002','entries':peer_entries,'relations':[
 {'from_key':'exponential-tilt','to_key':'quadratic-duality','kind':'specializes','rationale':'The exponential product laws are centered and isotropic with finite fourth moments; at d=2 the exact tilt norm is sqrt(2), the quadratic-duality instance.'},
 *[{'from_key':e['key'],'to_existing_logical':parent,'kind':'semantic_association','rationale':'This is a scoped lemma or obstruction for a proof route to the recorded P0017 target; it does not prove or refute the full target.'} for e in peer_entries]
]}
write_json(ROOT/'drafts'/'bundle_002.json',peer_bundle)

inbox=BASE/'math-brain-inbox'/'w350'
assert inbox.resolve()==Path('~/math-brain-inbox/w350').resolve()
inbox.mkdir(exist_ok=True)
part=inbox/'bundle_001.part'
queued=inbox/'bundle_001.json'
if queued.exists():
    assert json.loads(queued.read_text(encoding='utf-8'))==own_bundle,'Existing queue file differs; use a new filename rather than overwrite'
else:
    write_json(part,own_bundle)
    part.rename(queued)
# Complete reviewed peer bundle is held as .part, so duplicate author submissions and
# the missing second-account audit can be settled before any integrator consumes it.
held=inbox/'bundle_002.part'
write_json(held,peer_bundle)

prior=json.loads((ROOT/'context'/'intake_records.json').read_text(encoding='utf-8'))
existing={x['record']['logical_name']:x['record']['statement'] for x in prior if isinstance(x.get('record'),dict) and 'logical_name' in x['record']}
edges=[]
for bundle in [own_bundle,peer_bundle]:
    items={e['key']:e for e in bundle['entries']}
    for rel in bundle['relations']:
        end=items[rel['to_key']]['statement'] if 'to_key' in rel else existing.get(rel['to_existing_logical'].split(':')[-1])
        assert end is not None,'Relation endpoint evidence absent'
        edges.append({'bundle_slug':bundle['bundle_slug'],**rel,'from_statement_quote':items[rel['from_key']]['statement'],'to_statement_quote':end,'status':'prepared relation; not ingested'})
(ROOT/'RELATIONS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in edges),encoding='utf-8')

extra=[]
for e in peer_entries:
    extra.append({'id':'w350-reviewed-'+e['key'],'statement':e['statement'],'assumptions':e['assumptions'] or ['Exact mathematical hypotheses are fully specified in the statement.'],'source':e['source'],'proof_or_counterexample':e['proof_text'],'independent_reviewer':'w350','remaining_gap':'No parent solution; one independent worker review recorded. Additional account audit and coordinator integration pending.','status':'independently checked proof','parent_problem_solved':False})
append_unique(ROOT/'CLAIMS.jsonl',extra)

hook={'id':'math-w350-01','area':'math','event':'stage-start','cue':'(?i)(?:dated|historical|September).{0,100}(?:ranking|open.problem)|attempted_un','fire_when':'A new proof attempt treats the September P0017 attempted_un ranking as current evidence of openness despite October primary resolution claims.','silent_when':'A scoped Gaussian-channel lemma has already recorded the exact current sources and expressly makes no parent novelty or resolution claim.','text':'Before claiming a ranked major problem remains open or solved, recover its exact primary statement and check current versions. Separate reported resolution from an independently checked proof; a dated ranking or source hash certifies neither.','evidence':'SOURCE_STATUS.json; recall slug open_problem_repo_survey_famous_tracks_all_open_af449ii_now_refuted_with_two_audits_2026_09_18; three primary October claims measured in this packet.','proposer':'w350'}
assert len(hook['text'])<=300
hook_line=json.dumps(hook,ensure_ascii=False)
(ROOT/'drafts'/'math-w350.jsonl').write_text(hook_line+'\n',encoding='utf-8')
(ROOT/'patches'/'01_stale_status_hook.diff').write_text('--- a/~/primary_directive/hooks1000/proposals/math-w350.jsonl\n+++ b/~/primary_directive/hooks1000/proposals/math-w350.jsonl\n@@ -0,0 +1 @@\n+'+hook_line+'\n',encoding='utf-8')

checks=json.loads((ROOT/'measurements'/'math_checks.json').read_text(encoding='utf-8'))
optional=json.loads((ROOT/'measurements'/'exponential_frame.json').read_text(encoding='utf-8'))
comparison=[{'d':d,'published_loose_bound':4**d,'sharp_bound':comb(2*d,d),'ratio':4**d/comb(2*d,d)} for d in range(1,6)]
write_json(ROOT/'measurements'/'before_after.json',{'command':'python -X utf8 finalize_packet.py; exact arithmetic from python -X utf8 check_math.py','source':'BKL 2610.05474v1 Lemma 2.2; its proof already yields the binomial bound. No novelty claim.','tensor_constants':comparison,'store_before':'Two historical P0017 cards found in read-only store','after':'Six concept/definition entries queued; four reviewed lemma entries prepared and held. No ingestion or recall gain measured.','peer_KEEP_count':11,'initial_exact_check':checks,'optional_Gram_check':optional})

workflow={'prepared_at':now,'bundle_001':{'path':str(queued),'prepared':True,'submitted':True,'reviewed':'Own reduction independent reviewer w353 requested, pending. All new reductions are typed concept, not theorem.','ingested':False,'retrievable':False},'bundle_002':{'path':str(held),'prepared':True,'submitted':False,'reviewed':'Four included peer lemmas independently reproduced by w350; second-account audit and author-deduplication pending.','ingested':False,'retrievable':False},'live_store_written':False,'formal_check_receipt':None,'parent_problem_solved_by_this_packet':False}
write_json(ROOT/'BUNDLE_STATES.json',workflow)

packet={'worker':'w350','target':'P0017','date':now,'verdicts':peer_reviews,'source_status':'SOURCE_STATUS.json','own_attempt':'ATTEMPT.md','own_reviewer':'w353','own_review_status':'PENDING','reviewer_request_receipt':'msg-f94cc18b0d','hardest_unproved_input':'Universal all-function Gaussian-channel variance retention for all isotropic log-concave laws. It is quantitatively equivalent to the Poincare target, not a proved input.','peer_hardest_unproved_inputs':['w348: universal all-degree normalized Taylor tensor bound beyond exponential products','w349: uniform variance-weighted covariance bound (W)'],'reproductions':['reviews/w348_independent.md','reviews/w348_verdicts.jsonl','reviews/w349_verdicts.jsonl'],'snapshots':'reviews/snapshot_provenance.json','measurements':['measurements/math_checks.json','measurements/before_after.json','measurements/fresh_host_gate.json','measurements/exponential_frame.json'],'bundle_states':workflow,'open_votes':json.loads((BASE/'primary_directive/democracy/OPEN_VOTES.json').read_text(encoding='utf-8-sig')),'NEXT':'Independently audit Claims A-B adjoint and Sobolev-domain steps; retain VR as the explicit full-target input, then finish second-account review of the peer lemma bundle.'}
write_json(ROOT/'REVIEW_PACKET.json',packet)
(ROOT/'REVIEW_PACKET.md').write_text('P0017 review packet, w350, 2026-10-10\n\nEleven scoped KEEP verdicts are in reviews/w348_verdicts.jsonl and reviews/w349_verdicts.jsonl. They cover w348 L1-L4, w349 C001-C005, the exact posterior factorization counterexample, and the conditional weighted reduction. The optional small-drift extension of w349 C005 and the posterior quadrature number are outside these KEEP scopes.\n\nThe hardest tensor step was independently derived before reading w348 ATTEMPT.md. The exponential support-direct-sum step was independently checked: distinct supports are orthogonal because the law is a product and each positive-degree coordinate coefficient is centered. This argument has no correlated-law conclusion. The posterior counterexample was checked without repeating the peers quadrature: one observation gives a half-normal variance, while the positive-observation tail tends to untruncated Gaussian variance.\n\nOwn Claims A-B have complete written derivations in ATTEMPT.md; w353 was asked to audit the adjoint, L2-domain and normalization steps. Their brain cards remain concepts pending that review. A uniform all-function retention input is not proved. Recent primary sources report full KLS resolution; this packet certifies their claim statements and only the scoped peer lemmas above.\n\nREVIEW_PACKET.json pins artifacts and lists every verdict, input and submission state. Source hashes identify snapshots and are not mathematical or formal-check receipts.\n\nNEXT: Check Claims A-B independently, then authorize the already reviewed peer entries after the second-account and duplicate-author checks.\n',encoding='utf-8')

(ROOT/'REPORT.md').write_text('P0017 now has October primary papers reporting full KLS resolution, while the read-only brain probe found two historical September cards. SOURCE_STATUS.json recovers Randomstrasse101 Conjecture 30 and records the three current claims, their versions, isotropy, the L2 domain and the opposite psi conventions. Complete current proof validity remains unverified in this packet.\n\nI returned eleven scoped KEEP verdicts, independently reproduced the sharp tensor bound, and proved the Gaussian-observation retention bridge conditionally. For p=d,q=2d, the checked recovery constant is binom(2d,d), versus the displayed 4^d bound: at d=5, 1024 becomes 252 (4.06349 times smaller). The source proof already supports this sharpening; novelty is not claimed.\n\nMeasurement: python -X utf8 check_math.py passed 35 sharpness pairs, 925 components, 140 arbitrary block-symmetric fixtures, 9 coordinate enumerations, 100 Gaussian calibrations, 16 Wick dimensions and one negative control in 0.116479 seconds. python -X utf8 check_exponential_frame.py skipped its optional Gram test at the fresh 85% CPU gate (measured 86.7257%). The general product proof was checked mathematically, with no numerical Gram certification claimed.\n\nSix concept/definition entries are submitted as math-brain-inbox/w350/bundle_001.json. Four peer lemma entries are complete in bundle_002.part and held for duplicate-author and second-account review. BUNDLE_STATES.json separates prepared, submitted, reviewed, ingested and retrievable. No live store was written and no recall gain is claimed. w353s own-result audit is requested, pending.\n\nApply: the validating coordinator reviews and integrates the accepted inbox entries; the staged hook is patches/01_stale_status_hook.diff. The worker folder restriction leaves the global hook proposal and progress post staged locally in drafts/math-w350.jsonl and PROGRESS_PENDING.json.\n\nThe remaining mathematical risk is the all-function input: tensor symmetry, Gaussian/product examples and unweighted covariance means do not establish it. NEXT: independently audit the adjoint/domain steps of Claims A-B, then the universal variance-retention or weighted-covariance input.\n',encoding='utf-8')
write_json(ROOT/'PROGRESS_PENDING.json',{'agent':'w350','row':'S1.P0017.350','event':'P0017: 11 scoped KEEP verdicts; sharp tensor recovery and exact product tilt norm checked; Gaussian-retention draft queued; full-target input remains explicit.','evidence':str(ROOT/'REVIEW_PACKET.json'),'state':'STAGED_FOR_REVIEWER_POST','reason':'Worker writes only its folder except the explicitly named math-brain inbox and named-peer mesh.','command_template':'python -X utf8 ~/primary_directive/pd_progress.py --event <event> --agent w350 --row S1.P0017.350 --evidence ~/brain_workers/w350/REVIEW_PACKET.json'})

print(json.dumps({'status':'PREPARED','peer_KEEPs':len(peer_reviews),'queued_entries':len(own_entries),'reviewed_held_entries':len(peer_entries),'relations':len(edges),'submitted':str(queued),'held':str(held),'ingested':False,'own_review':'PENDING'}),flush=True)
