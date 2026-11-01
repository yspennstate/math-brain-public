"""Write review artifacts and a local draft; this is not an experiment or integrator."""
from pathlib import Path
import difflib
import json

ROOT = Path(__file__).parent
OWNER = Path('~')
EXISTING_TARGET = 'math:probability.core:open-problem-p0017-dimension-free-log-concave-poincare-or-cheeger-constant'
EXISTING_GAUSSIAN = 'math:probability.core:attempt-p0017-dimension-free-log-concave-poincare-or-cheeger-constant'


def entry(key, name, title, statement, assumptions, proof_path, review_status):
    return {
        'key': key, 'namespace': 'probability.functional', 'logical_name': name,
        'kind': 'concept', 'title': title, 'statement': statement,
        'proof_text': None, 'assumptions': assumptions, 'domain': 'probability theory',
        'source': {
            'source_id': 'owner-primary-directive-w358-p0017:' + key,
            'url': 'urn:owner-primary-directive:w358:p0017:' + key,
            'revision': '2026-10-10-draft-v1',
            'license': 'owner-own-work; campaign derivation or audit, DRAFT only',
            'excerpt': None,
        },
        'review_note': review_status + '; derivation: ~/brain_workers/w358/' + proof_path,
    }


def make_bundle():
    entries = [
        entry('status', 'p0017-primary-source-status-october-2026',
              'DRAFT: P0017 dated primary-source status',
              'DRAFT source audit as of 2026-10-10. P0017 asks for one universal C such that CP(mu)<=C for every dimension and every isotropic log-concave probability law. Isotropy means mean zero and covariance identity; CP is the variance-to-Euclidean-gradient-energy coefficient. Randomstrasse101 arXiv:2603.29571v1 Entry 13 Conjecture 30 gives the equivalent Cheeger bound c/sqrt(||Cov||op). arXiv:2610.05474v1 (4 October) and 2610.07728v1 (6 October) claim complete bounds. These source claims have not been fully independently audited here; current openness is UNKNOWN and the September attempted_unsolved label is historical.',
              ['Full-dimensional log-concave probability laws', 'Dated source status is distinct from proof verification'],
              'SOURCE_STATUS.json', 'Source-read audit; mathematical completeness not certified'),
        entry('parseval-route', 'refuted-gaussian-to-appell-diagonal-parseval-route',
              'DRAFT refuted route: Gaussian diagonal Parseval for Appell polynomials',
              'REFUTED DRAFT ROUTE, not an available identity: replacing Gaussian Hermite polynomials by centered Appell polynomials of a general isotropic log-concave law does not preserve diagonal Parseval. In particular the proposed equality Var(q1+q2)=E q1^2+E q2^2 fails for X=Exp(1)-1, q1=X and q2=(X^2-1)/2. The full variance requires their cross Gram term.',
              ['The proposed extrapolation is false', 'Appell polynomials need not be orthogonal'],
              'INDEPENDENT_DERIVATION.md', 'Gram corollary pending independent referee check'),
        entry('appell-calibration', 'centered-exponential-appell-coefficient-calibration',
              'DRAFT: exact exponential Appell coefficient norms and Gram obstruction',
              'DRAFT exact special case. For X=Y-1 with Y~Exp(1), the normalized tilt coefficient T_d f=F_f^(d)(0)/d! is E[f(X)q_d(Y)], where q_d(y)=y^d/d!-y^(d-1)/(d-1)! for d>=1. Its squared L2 operator norm is binomial(2d-2,d-1), attained by the normalized representer; its all-degree exponential rate is 2. Scalar cumulants of order m>=2 equal (m-1)!. Moreover q1=X, q2=(X^2-1)/2 have Gram entries 1, 2 and cross entry 1. Thus Var(q1+q2)=5, a diagonal sum gives 3, and E|(q1+q2)prime|^2=2. This does not prove a tensor bound for general laws.',
              ['d>=1 integer', 'f in L2(mu)', 'Factorial-normalized scalar Taylor coefficient', 'mu is not a regular smooth strongly log-concave law'],
              'INDEPENDENT_DERIVATION.md', 'w359 KEEP S1.5 for coefficient norm and factorial calibration; extra Gram corollary pending'),
        entry('tilt-route', 'refuted-initial-covariance-bound-under-arbitrary-tilts',
              'DRAFT refuted route: arbitrary tilts inherit initial isotropy',
              'REFUTED DRAFT ROUTE: original isotropy of a log-concave law does not bound the covariance or Poincare constant of every normalized linear or Gaussian-damped tilt by a universal multiple of the original covariance. Log-concavity persists while covariance changes. A bound on the covariance of the current law, or a process-specific averaged estimate with its probability law and time range, is needed.',
              ['Original covariance is identity', 'Arbitrary deterministic tilt parameters', 'No assertion about a specific localization process average'],
              'INDEPENDENT_DERIVATION.md', 'w359 KEEP S1.3-S1.4'),
        entry('tilt-calibration', 'centered-exponential-linear-and-gaussian-tilt-covariance',
              'DRAFT: exact exponential tilted covariance obstruction',
              'DRAFT independently checked special case. For X=Exp(1)-1, the normalized linear tilt exp(sx), s<1, has mean s/(1-s), variance (1-s)^(-2), and CP at least that variance by the linear test. For t>0, the normalized tilt exp((1-t)x-tx^2/2) has variance (1-2/pi)/t: X+1 becomes half-normal with precision t. These laws are log-concave, and both variances can be arbitrarily large compared with the original variance 1. These deterministic examples do not refute KLS normalized with the current covariance, or an averaged localization estimate.',
              ['Dimension one', 's<1 for the linear tilt', 't>0 for the quadratic tilt', 'Normalized deterministic tilt family'],
              'INDEPENDENT_DERIVATION.md', 'w359 independent KEEP S1.3-S1.4; REVIEW_w358.md'),
        entry('posterior-nonstrict', 'log-concave-gaussian-posterior-nonstrict-dirichlet-contraction',
              'DRAFT: posterior curvature yields non-strict Dirichlet contraction',
              'DRAFT conditional deduction. Let X~mu be log-concave, G~N(0,I) independent, t>0, Y=X+sqrt(t)G, nu_t=Law(Y), and T_t f=E[f(X)|Y]. For regular mu and finite-energy f, grad_y T_t f=Cov(f,X|Y=y)/t. The posterior curvature is at least 1/t, giving Cov(X|Y=y)<=tI and Var(f|Y=y)<=t E[|grad f|^2|Y=y]. Cauchy-Schwarz and averaging imply D_nu_t(T_t f)<=D_mu(f). Extension beyond regular laws needs the appropriate Sobolev approximation. This argument gives coefficient 1 and supplies no uniform strict margin.',
              ['t>0 is NOISE variance', 'Independent Gaussian observation', 'Begin with regular smooth log-concave mu', 'Finite gradient energy and justified conditional differentiation'],
              'POSTERIOR_BRIDGE_CHECK.md', 'Independently rederived by w358; w359 status reports the same q=1 derivation'),
        entry('strict-gap', 'uniform-strict-gaussian-posterior-contraction-kls-gap',
              'DRAFT: the strict averaged posterior bridge retains the KLS gap',
              'DRAFT conditional equivalence, attributed to w357 and independently audited by w358. For log-concave mu with finite K=CP(mu), fixed t>0 and Q_t(mu)<=q<1 for every Sobolev f imply K<=t(1+q)/(1-q), by total variance and CP(mu*Gaussian_t)<=K+t. Conversely K<=C gives D(T_t f)<=Var_mu(f)/t<=C D_mu(f)/t; t=2C gives q=1/2. Thus a dimension-uniform strict posterior Dirichlet contraction at some fixed noise level is equivalent to a dimension-free KLS bound. Its nonlinear averaged gap remains unproved in this campaign packet. The unweighted MMSE covariance average cannot be substituted into an energy-weighted expectation.',
              ['K<infinity before rearrangement', 'One fixed numerical t and q uniform over dimensions and laws', 'All Sobolev test functions', 'Uniform regular approximation for the full target'],
              'PEER_AUDIT.md', 'w358 KEEP w357 L4; w359 also reports independently checking L4; full strict bound unproved'),
        entry('posterior-tail', 'exponential-gaussian-posterior-dirichlet-contraction-lower-bound',
              'DRAFT: exponential tail constrains a posterior contraction coefficient',
              'DRAFT special-case derivation awaiting independent referee check. For centered isotropic X=Exp(1)-1 observed through independent Gaussian noise of variance t>0, test f_a(x)=exp(a x), 0<a<1/2. A positive-tail calculation gives liminf as a increases to 1/2 of D_nu_t(T_t f_a)/D_mu(f_a)>=exp(-t/4). Hence any all-function coefficient q(t) must be at least exp(-t/4). At t=1 the explicit a=49/100 test has ratio greater than 7/10, using only the tail y>=5 in the untranslated observation coordinates. The exact Gaussian affine coefficient 1/4 at t=1 cannot hold for this law. This does not refute existence of some q<1.',
              ['t>0 fixed noise variance', '0<a<1/2 ensures L2 and finite energy', 'Translation to centered X preserves the ratio', 'Sobolev approximation needed if the initial test class is bounded'],
              'POSTERIOR_BRIDGE_CHECK.md', 'w359 independent review requested; not theorem material'),
    ]
    relations = [
        {'from_key':'status', 'to_existing_logical':EXISTING_TARGET, 'kind':'cites',
         'rationale':'Attach dated primary verification to the exact historical P0017 problem, preserving its unverified current-status caveat.'},
        {'from_key':'parseval-route', 'to_existing_logical':EXISTING_GAUSSIAN, 'kind':'analogous_to',
         'rationale':'The historical card proves only Gaussian Hermite Parseval; this explicitly refuted extrapolation records the missing orthogonality premise.'},
        {'from_key':'appell-calibration', 'to_key':'parseval-route', 'kind':'refutes',
         'rationale':'At X=Exp(1)-1 the exact cross Gram term is 1: actual variance 5 differs from the proposed diagonal variance 3.'},
        {'from_key':'tilt-calibration', 'to_key':'tilt-route', 'kind':'refutes',
         'rationale':'The initial isotropic variance is 1 but linear-tilt variance (1-s)^(-2) and quadratic-tilt variance (1-2/pi)/t diverge.'},
        {'from_key':'strict-gap', 'to_key':'posterior-nonstrict', 'kind':'depends_on',
         'rationale':'The conditional variance and covariance inequalities support the variance reduction; obtaining q<1 is an additional unproved premise.'},
        {'from_key':'posterior-tail', 'to_key':'strict-gap', 'kind':'semantic_association',
         'rationale':'This specific isotropic law imposes q(t)>=exp(-t/4) on any constants proposed for the full nonlinear bridge.'},
        {'from_key':'appell-calibration', 'to_existing_logical':EXISTING_GAUSSIAN, 'kind':'analogous_to',
         'rationale':'Exact exponential Appell Gram entries show why the Gaussian diagonal generator cannot be assumed for other log-concave laws.'},
    ]
    return {'spec':'mathbrain-draft-v1','author_agent':'w358',
            'bundle_slug':'p0017-exponential-boundaries-w358-001',
            'entries':entries,'relations':relations}


def validate(bundle, lookup):
    allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
    keys={e['key'] for e in bundle['entries']}
    assert len(keys)==len(bundle['entries']) and len(keys)<=200
    existing={json.loads(r['metadata_json'])['logical_id'] for s in lookup for r in s.get('rows',[])}
    required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
    for e in bundle['entries']:
        assert required.issubset(e) and e['kind']=='concept' and e['proof_text'] is None
        assert e['source']['license'].startswith('owner-own-work')
        assert 'DRAFT' in e['statement'] and len(e['statement'])>80
    for r in bundle['relations']:
        assert r['from_key'] in keys and r['kind'] in allowed
        if 'to_key' in r: assert r['to_key'] in keys
        else: assert r['to_existing_logical'] in existing
    graph={k:[] for k in keys}
    for r in bundle['relations']:
        if r['kind']=='depends_on' and 'to_key' in r:graph[r['from_key']].append(r['to_key'])
    def visit(k, active, seen):
        assert k not in active, 'depends_on cycle'
        if k in seen:return
        for v in graph[k]:visit(v,active|{k},seen)
        seen.add(k)
    seen=set()
    for k in keys:visit(k,set(),seen)
    return {'schema_checks':'PASS','entries':len(keys),'relations':len(bundle['relations']),
            'cross_targets_resolved':True,'depends_on_acyclic':True,
            'mathematical_proof':'not established by this structural validation',
            'experiment_status':'HELD: no exact-polynomial experiment executed by w358'}


def main():
    source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    source['primary_sources'].insert(0,{'url':'https://arxiv.org/html/2603.29571v1',
        'arxiv':'2603.29571v1','location':'Entry 13, Conjecture 30',
        'license':'cc-by-4.0','statement':'Cheeger(mu)>=c/sqrt(||Cov(mu)||op) uniformly over log-concave laws',
        'source_status':'dated problem statement, not a current openness certificate'})
    source['owner_prior_work_check']={
        'ranking':'2026-09-07 P0017 row 548: attempted_un',
        'exact_problem_record':'brain_bundle_C006p01.json entry op-p0017',
        'exact_attempt_record':'brain_bundle_C006a04.json entry at-p0017: Gaussian-only Hermite expansion, author-checked, no full solution',
        'H_I_attempts':'Targeted P0017/KLS/Kannan/Poincare search found no P0017 full-proof record in the named H/I attempt folders',
        'lean_prior':'Targeted reads locate dated ranked list only for this target; no actual formal theorem receipt identified',
        'team_O':'TEAM_BOARD.md line 553 has historical listing; named triad claims are disjoint',
        'canonical_repository':'No SQLite file was found by the targeted filename lookup in the named canonical repository. Its local directory has named subdirectories but no immediate files. Canonical store location remains unresolved; benchmark/evaluation subdirectories were not opened.',
        'retirement_certification':'No owner full-solution or retirement certificate found in these narrowly named records; not an exhaustive claim',
    }
    source['independent_derivation_before_peer_proof']='INDEPENDENT_DERIVATION.md saved before any paired proof; POSTERIOR_BRIDGE_CHECK.md saved after statement-only packet and before w357/ATTEMPT.md'
    source['paired_proof_read']='w357/ATTEMPT.md: L1-L6 independently audited KEEP at stated scope; strict nonlinear gap remains'
    (ROOT/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

    claims=[json.loads(s) for s in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
    for c in claims:
        if c['id'] in {'w358-S1.3','w358-S1.4','w358-S1.5'}:
            c['status']='independently checked proof'
            c['independent_reviewer']='w359; KEEP, ~/brain_workers/w359/REVIEW_w358.md'
            c['remaining_gap']='No full KLS proof or process-specific covariance estimate; review covers the original scalar claim, not later added corollaries'
    claims += [
        {'id':'w358-S1.6','kind':'refuted_route','statement':'For centered Exp(1)-1, q1=X and q2=(X^2-1)/2 have cross Gram entry 1, Var(q1+q2)=5 and Dirichlet energy 2. Gaussian diagonal Parseval predicts 3 and cannot be transferred to these Appell coefficients.',
         'assumptions':['Centered isotropic scalar exponential law','q1 and q2 are centered normalized Appell coefficients'],
         'source':{'path':'INDEPENDENT_DERIVATION.md','source_tag':'owner-own-work','quote':'Var(q1+q2)=5'},
         'proof_or_counterexample':'Use exponential centered moments E X^2=1, E X^3=2, E X^4=9 to compute the full 2x2 Gram matrix.',
         'independent_reviewer':'w359 requested; pending for this later corollary','remaining_gap':'Independent check; not a counterexample to KLS with unspecified C','status':'proved special case'},
        {'id':'w358-S1.7','kind':'peer_audit','statement':'KEEP w357 L1-L6 at their stated scopes; strict contraction Q_t<=q<1 for all functions, laws and dimensions remains the hardest missing premise.',
         'assumptions':['Finite CP before rearrangement','Independent Gaussian observation','t denotes noise variance','No independence between posterior covariance and conditional energy'],
         'source':{'path':'~/brain_workers/w357/ATTEMPT.md','quote':'Only the uniform strict bound Q_t<=q<1 remains unproved here.'},
         'proof_or_counterexample':'Independent derivations and quantified scope checks in PEER_AUDIT.md, including the Laplace energy-weighted ratio tending to 1.',
         'independent_reviewer':'w358 audits original w357 argument; source receipts also name w359','remaining_gap':'Full strict bound still unproved; audit is not admission under a two-login protocol','status':'independently checked proof'},
        {'id':'w358-S1.8','kind':'derived_obstruction','statement':'For centered Exp(1)-1 with independent Gaussian noise t>0, exp(a x) tests as a increases to 1/2 imply q(t)>=exp(-t/4). At t=1, a=49/100 gives posterior Dirichlet ratio greater than 7/10.',
         'assumptions':['0<a<1/2','t>0 fixed noise variance','L2 and finite energy','Sobolev closure if the starting test class is bounded'],
         'source':{'path':'POSTERIOR_BRIDGE_CHECK.md','source_tag':'owner-own-work','quote':'q(t)>=exp(-t/4)'},
         'proof_or_counterexample':'Complete the Gaussian square, differentiate the CDF ratio, then integrate only y>=R; the explicit t=1 bound uses R=5 and elementary Mills inequalities.',
         'independent_reviewer':'w359 requested; pending','remaining_gap':'Referee check of tail lower bound and Sobolev approximation; strict contraction may still exist','status':'sketch'},
        {'id':'w358-S1.9','kind':'retrieval_failure','statement':'General memory recall returned no result before a configured 60-second timeout (68.668 seconds observed). A bounded read-only P0017 math-store lookup took 0.099 seconds and recovered two historical cards, neither mentioning the October proof claims.',
         'assumptions':['Different retrieval tasks; no apples-to-apples latency gain claimed','Only the named target cards were read','Live SQLite opened mode=ro'],
         'source':{'path':'recall_probe.json; brain_target_lookup.json','quote':'elapsed_seconds: 68.668; timed_out: true'},
         'proof_or_counterexample':'Saved tool-run receipts; repair stages dated status and exact boundary cases on the existing logical IDs.',
         'independent_reviewer':'claude-4a88bc43 review pending','remaining_gap':'Proposed attachment is not ingested or globally evaluated; compute-gated math experiment held','status':'numerical evidence'},
    ]
    (ROOT/'CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')

    lookup=json.loads((ROOT/'brain_target_lookup.json').read_text(encoding='utf-8'))
    bundle=make_bundle();receipt=validate(bundle,lookup)
    payload=json.dumps(bundle,indent=2,ensure_ascii=False)+'\n'
    (ROOT/'bundle_001.json').write_text(payload,encoding='utf-8')
    (ROOT/'STRUCTURAL_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    key_map={e['key']:e for e in bundle['entries']}
    old={json.loads(r['metadata_json'])['logical_id']:r['body'] for s in lookup for r in s.get('rows',[])}
    edges=[]
    for n,r in enumerate(bundle['relations'],1):
        end=key_map[r['to_key']]['statement'] if 'to_key' in r else old[r['to_existing_logical']]
        edges.append({'id':f'w358-edge-{n:02d}',**r,'from_quote':key_map[r['from_key']]['statement'],
                      'to_quote':end,'verdict':'DRAFT; independent edge review pending'})
    (ROOT/'EDGE_REVIEW.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in edges),encoding='utf-8')
    (ROOT/'patches').mkdir(exist_ok=True)
    target='math-brain-inbox/w358/bundle_001.json'
    diff=''.join(difflib.unified_diff([],payload.splitlines(True),fromfile='a/'+target,tofile='b/'+target))
    (ROOT/'patches/01_p0017_boundary_bundle.diff').write_text(diff,encoding='utf-8')
    lifecycle={'prepared':True,'submitted':False,'submission_path':'~/math-brain-inbox/w358/bundle_001.json',
               'reviewed':False,'reviewed_claims':['w358-S1.3','w358-S1.4','w358-S1.5'],
               'review_receipt':'~/brain_workers/w359/REVIEW_w358.md',
               'ingested':False,'retrievable':False,'integration':'validating coordinator only',
               'local_schema_validation':receipt,'new_concepts':'remain DRAFT; no theorem promotion'}
    (ROOT/'BUNDLE_LIFECYCLE.json').write_text(json.dumps(lifecycle,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt))


if __name__=='__main__':
    main()
