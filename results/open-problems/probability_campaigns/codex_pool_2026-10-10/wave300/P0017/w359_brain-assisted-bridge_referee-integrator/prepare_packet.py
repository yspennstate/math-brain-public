"""Write the worker's frozen review packet and authorized disjoint DRAFT inbox."""
import difflib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
EXISTING='math:probability.core:open-problem-p0017-dimension-free-log-concave-poincare-or-cheeger-constant'
ALLOWED_RELATIONS={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}

def put(name,value):
    (ROOT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def lines(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]

def source(slug,report):
    return {'source_id':'owner-own-work:w359:'+slug,'url':(ROOT/report).as_uri(),
            'revision':'campaign-w359-2026-10-10-v1','license':'owner-own-work (campaign derivation or source audit; no novelty claim)','excerpt':None}

def entry(key,name,title,statement,assumptions,report):
    return {'key':key,'namespace':'probability.logconcavity','logical_name':name,
            'kind':'concept','title':title,'statement':statement,'proof_text':None,
            'assumptions':assumptions,'domain':'probability; functional inequalities',
            'source':source(name,report)}

def validate(bundle):
    assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w359'
    assert 0<len(bundle['entries'])<=200
    keys={e['key'] for e in bundle['entries']}
    assert len(keys)==len(bundle['entries'])
    required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
    for e in bundle['entries']:
        assert required<=set(e) and e['statement'] and e['assumptions']
        assert e['kind'] in {'definition','lemma','theorem','concept'}
        assert e['source']['license'].startswith('owner-own-work')
        assert {'source_id','url','revision','license','excerpt'}<=set(e['source'])
        if e['kind'] in {'lemma','theorem'}:
            assert e['proof_text']
        else:
            assert e['proof_text'] is None
    graph={k:[] for k in keys}
    for edge in bundle['relations']:
        assert edge['from_key'] in keys and edge['kind'] in ALLOWED_RELATIONS and edge['rationale']
        assert ('to_key' in edge)^('to_existing_logical' in edge)
        if 'to_key' in edge:
            assert edge['to_key'] in keys
            if edge['kind']=='depends_on':
                graph[edge['from_key']].append(edge['to_key'])
        else:
            assert edge['to_existing_logical']==EXISTING
    visiting=set(); visited=set()
    def visit(k):
        assert k not in visiting
        if k in visited:
            return
        visiting.add(k)
        for next_key in graph[k]:
            visit(next_key)
        visiting.remove(k); visited.add(k)
    for k in graph:
        visit(k)
    return {'entry_count':len(keys),'relation_count':len(bundle['relations']),
            'schema_fields':True,'allowed_relation_types':True,'dependency_dag':True,
            'owner_source_tag':True,'mathematical_proof_validation':False}

def main():
    prior=json.loads((ROOT/'prior_p0017_cards.json').read_text(encoding='utf-8'))
    old_problem=next(v for v in prior if v['metadata'].get('bundle_entry_key')=='op-p0017')
    old_attempt=next(v for v in prior if v['metadata'].get('bundle_entry_key')=='at-p0017')
    put('SOURCE_STATUS.json',{
        'target':'P0017','checked_date':'2026-10-10','current_openness':'UNKNOWN',
        'current_primary_status':'FULL_KLS_PROOFS_CLAIMED_IN_RECENT_PRIMARY_PREPRINTS; NOT INDEPENDENTLY CERTIFIED HERE',
        'exact_poincare_statement':'There exists C>0 independent of n and mu such that C_P(mu)<=C for every n>=1 and every isotropic log-concave probability measure mu on R^n. C_P is the best coefficient in Var_mu(f)<=C_P integral |grad f|^2 dmu for locally Lipschitz f in L2(mu) with finite gradient energy.',
        'assumptions':['log-concave density exp(-V) with convex extended-real V','mean zero and covariance identity','Euclidean gradient','n>=1','constants independent of dimension and law'],
        'covariance_form':'||Cov(mu)||_op <= C_P(mu) <= C ||Cov(mu)||_op',
        'cheeger_form':'h(mu)>=c/sqrt(||Cov(mu)||_op), so h(mu)>=c in isotropic position',
        'original_primary':{'url':'https://arxiv.org/html/2603.29571v1','location':'Entry 13, Conjecture 30','checked':'covariance formulation read','rendering_note':'Half-space display uses S under an H infimum; intended covariance formulation is unambiguous.'},
        'recent_primary_sources':[
            {'url':'https://arxiv.org/html/2610.05474v1','authors':'Bizeul-Klartag-Lehec','announced':'2026-10-04','checked':'Theorem 1.1, equations (5)-(6), proof outline, regular approximation paragraph','full_proof_independently_checked':False},
            {'url':'https://arxiv.org/html/2610.01447v2','authors':'Song-Zhang','checked':'v2 Theorem 1.1 states full bound; v1 log-star metadata is stale','full_proof_independently_checked':False},
            {'url':'https://arxiv.org/abs/2610.07728','authors':'Balasubramanian-Kasiviswanathan','announced':'2026-10-06','checked':'abstract claiming full result','full_proof_independently_checked':False}],
        'prior_owner_records':[{'node_id':v['id'],'statement':v['body'],'source_id':v['metadata']['source_id'],'source_revision':v['metadata']['source_revision']} for v in [old_problem,old_attempt]],
        'owner_solved_retired_check':'Exact prior owner card is Gaussian-only and explicitly not a general proof. Task-named H/I target searches gave no P0017 match; lean/ranking records preserve attempted_un. No owner-wide registry absence or retirement is certified.',
        'ranking_record':{'date':'2026-09-07','tier':5,'status':'attempted_un','line':548},
        'remaining_general_proof_gap':'Uniform strict Gaussian-posterior Dirichlet contraction for all nonlinear tests, equivalently the general KLS bound in the reviewed reduction; the new published all-degree proofs were not audited.',
        'novelty_claim':False,'formal_check_receipt':None})
    entries=[
        entry('status','p0017-dated-primary-proof-claims-status-20261010','P0017: dated primary proof claims and historical status',
              'Source audit, not a mathematical proof certification: P0017 asks for a universal C_P bound for every isotropic log-concave probability law in all dimensions, equivalently a universal positive Euclidean Cheeger lower bound. The September 2026 attempted_un record and its Gaussian-only attempt do not certify current openness. As read on 10 October 2026, arXiv 2610.05474v1 Theorem 1.1, 2610.01447v2 Theorem 1.1, and the 2610.07728 abstract claim full KLS results. Their complete proofs have not been independently audited in this packet; current openness under that audit standard is UNKNOWN. No new full solution or novelty is claimed.',
              ['Dated source check as of 2026-10-10','Isotropy means mean 0 and covariance I','C_P is the coefficient in the Euclidean variance inequality'],'SOURCE_AUDIT.md'),
        entry('bad-fibre','refuted-isotropy-to-uniform-conditional-poincare-transfer','Refuted route: full isotropy transferred to conditional constants',
              'Refuted candidate bridge, not a theorem: one might try to infer a finite universal essential upper bound for C_P(law(Z|X=x)) solely because the joint law (X,Z) is isotropic and log-concave. This transfer requires an additional conditional bound; full isotropy describes the joint covariance and does not imply that each conditional law is isotropic. The accompanying cone calculation is DRAFT evidence pending the independent referee.',
              ['Joint isotropic log-concave law','Conditional Euclidean Poincare constants','Proposed uniform conclusion explicitly refuted; no KLS counterexample claimed'],'CONE_COUNTEREXAMPLE.md'),
        entry('cone','isotropic-log-concave-cone-unbounded-conditional-poincare-constant','DRAFT: isotropic cone with unbounded conditional Poincare constants',
              'DRAFT counterexample pending independent reviewer w362: the probability density exp(-(2+sqrt(2)x)) on x>=-sqrt(2), |z|<=x+sqrt(2) is log-concave and has mean (0,0) and covariance I_2. For x>-sqrt(2), Z|X=x is uniform on [-(x+sqrt(2)),x+sqrt(2)], so its variance is (x+sqrt(2))^2/3. Testing its Poincare inequality on z gives C_P(law(Z|X=x)) at least this value. For every M>0, the set where it exceeds M has probability (1+sqrt(6M))exp(-sqrt(6M))>0. Thus its essential conditional Poincare supremum is infinite. This refutes the stated conditional transfer, not KLS.',
              ['Exact two-dimensional density and Euclidean conditional derivative','Convex-support log-concavity is allowed','Own campaign result; w362 independent mathematical review pending'],'CONE_COUNTEREXAMPLE.md'),
        entry('bad-derivative','refuted-conditional-mean-partial-derivative-commutation','Refuted route: ignore the changing conditional law',
              'Refuted candidate identity, not a valid theorem: d/dx E[f(X,Z)|X=x] need not equal E[partial_x f(X,Z)|X=x] when the conditional law of Z depends on x. A product-law argument cannot use this identity merely from zero covariance or isotropy. The derivative of the conditional law, including moving-support boundary terms when applicable, must be accounted for.',
              ['Conditional distribution may depend on x','Conditional mean and derivative exist on the interior','No independence hypothesis is supplied'],'CONE_COUNTEREXAMPLE.md'),
        entry('cone-derivative','isotropic-cone-conditional-mean-derivative-noncommutation','DRAFT: conditional z-squared mean has a nonzero derivative',
              'DRAFT counterexample pending independent reviewer w362: for density exp(-(2+sqrt(2)x)) on x>=-sqrt(2), |z|<=x+sqrt(2), set f(x,z)=z^2. For every x>-sqrt(2), E[f(X,Z)|X=x]=(x+sqrt(2))^2/3, whose derivative is 2(x+sqrt(2))/3. In contrast, partial_x f is identically zero, so E[partial_x f(X,Z)|X=x]=0. Polynomial moments are finite. This directly refutes conditional-mean derivative commutation without a condition controlling the changing conditional law.',
              ['Same explicit isotropic log-concave cone law','Interior x>-sqrt(2)','f(x,z)=z^2','Independent mathematical review pending'],'CONE_COUNTEREXAMPLE.md')]
    relations=[
        {'from_key':'status','to_existing_logical':EXISTING,'kind':'cites','rationale':'The existing problem card records the exact historical source and says current status unverified; the source audit adds dated primary proof claims without asserting mathematical certification.'},
        {'from_key':'cone','to_key':'bad-fibre','kind':'refutes','rationale':'The joint covariance is I_2 but the conditional Poincare lower bound is unbounded on positive-probability sets; DRAFT refutation awaits the independent reviewer.'},
        {'from_key':'cone-derivative','to_key':'bad-derivative','kind':'refutes','rationale':'The displayed conditional-mean derivative is nonzero while the conditional partial derivative is zero; this refutes precisely the unqualified identity.'},
        {'from_key':'cone-derivative','to_key':'cone','kind':'depends_on','rationale':'The derivative calculation uses the exact conditional uniform law established for the same cone density.'},
        {'from_key':'cone','to_existing_logical':EXISTING,'kind':'cites','rationale':'This is a rejected proof route for the KLS target, not a proof or counterexample to its parent assertion.'}]
    bundle={'spec':'mathbrain-draft-v1','author_agent':'w359','bundle_slug':'p0017-cone-bridge-audit-w359-20261010','entries':entries,'relations':relations}
    validation=validate(bundle)
    put('bundle_001.json',bundle)
    by_key={e['key']:e for e in entries}
    with (ROOT/'EDGES.jsonl').open('w',encoding='utf-8') as out:
        for i,edge in enumerate(relations,1):
            from_entry=by_key[edge['from_key']]
            to_statement=by_key[edge['to_key']]['statement'] if 'to_key' in edge else old_problem['body']
            row={'id':f'w359-E{i:03}','relation':edge,'from_statement_quote':from_entry['statement'],
                 'to_statement_quote':to_statement,'evidence':'CONE_COUNTEREXAMPLE.md' if edge['from_key']!='status' else 'SOURCE_AUDIT.md',
                 'review_state':'draft; coordinator review required; own counterexamples awaiting w362','ingested':False}
            out.write(json.dumps(row,ensure_ascii=False)+'\n')
    inbox=Path('~/math-brain-inbox/w359')
    inbox.mkdir(parents=True,exist_ok=True)
    destination=inbox/'bundle_001.json'
    part=inbox/'bundle_001.part'
    if destination.exists() or part.exists():
        raise RuntimeError('Refusing to overwrite an existing inbox artifact; choose a fresh bundle number.')
    with part.open('x',encoding='utf-8') as out:
        out.write(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n')
    part.rename(destination)
    validation['local_copy_equals_submitted_copy']=json.loads(destination.read_text(encoding='utf-8'))==bundle
    put('BUNDLE_VALIDATION.json',validation)
    put('BUNDLE_STATES.json',{'path':str(destination),'prepared':True,'submitted':True,
                            'reviewed':False,'mathematical_review':'Own C1/C2 requested from w362; no response at freeze; concept/draft material only.',
                            'source_and_schema_checked':True,'integrator_run':False,'ingested':False,'retrievable':False,
                            'peer_review_rows':'REVIEW_VERDICTS.jsonl; peers retain ownership of their separate proof bundles',
                            'digest_or_manifest_computed':False})
    patch_dir=ROOT/'patches'; patch_dir.mkdir(exist_ok=True)
    live='~/.claude/dreaming/math_problem_probe.py'
    module=(ROOT/'math_problem_probe.py').read_text(encoding='utf-8').splitlines(keepends=True)
    diff=''.join(difflib.unified_diff([],module,fromfile='a/'+live,tofile='b/'+live))
    (patch_dir/'01_exact_problem_probe.diff').write_text(diff,encoding='utf-8')
    reconstructed=''.join(line[1:] for line in diff.splitlines(keepends=True) if line.startswith('+') and not line.startswith('+++'))
    assert reconstructed==''.join(module)
    put('PATCH_CHECK.json',{'live_path':live,'new_file_diff_reconstructs_local_module':True,'applied_to_live':False})
    hook_dir=ROOT/'hook_proposals'; hook_dir.mkdir(exist_ok=True)
    hook={'id':'math-w359-01','area':'math','event':'stage-start','cue':'an exact Pdddd probability target is absent or off-topic in deliberate memory recall',
          'fire_when':'P0017 recall returns referee memories and no P0017 hit although op-/at-P0017 cards exist',
          'silent_when':'Generic referee advice without a problem ID, or target cards already returned with current-status checks',
          'text':'An exact problem ID may live in the math store rather than general memory. Probe its full problem/attempt cards, preserve dated status and special-case scope, then check recent primary sources before claiming openness or a proof.',
          'evidence':'~/brain_workers/w359/PROBE_CHECKS.json: 0 general top-three target hits; 2 exact rescue cards; 8 checks pass','proposer':'w359'}
    assert len(hook['text'])<=300
    (hook_dir/'math-w359.jsonl').write_text(json.dumps(hook,ensure_ascii=False)+'\n',encoding='utf-8')
    admin=lines(ROOT/'CLAIMS.jsonl')[0]
    admin['status']='sketch'; admin['independent_reviewer']='not applicable: administrative assignment lookup; no mathematical proof'; admin['review_state']='source lookup only'
    candidates=lines(ROOT/'CLAIM_CANDIDATES.jsonl')
    for row in candidates:
        row['independent_reviewer']='w362 (request msg-a7ffe8df7a; pending)'
    reviews=lines(ROOT/'REVIEW_VERDICTS.jsonl')
    extra=[
        {'id':'w359-source-002','kind':'source status audit','statement':'The exact original P0017 source is arXiv 2603.29571v1 Entry 13 Conjecture 30, and recent October primary preprints claim the full normalized KLS result. Current openness is not certified by the September attempted_un label.',
         'assumptions':['dated source check on 2026-10-10','source statement verification only'],
         'source':{'path':'SOURCE_AUDIT.md','url':'https://arxiv.org/html/2610.05474v1','location':'Theorem 1.1','quote':'There exists a universal constant C>0'},
         'proof_or_counterexample':'Compared the complete covariance-normalized source statements and exact prior card with dates; full published proofs not independently audited.',
         'independent_reviewer':'w359 source verifier; complete mathematical proof audit pending','remaining_gap':'The high-order general cumulant/tilt estimates in the primary proof are not reproduced. No global owner solved/retired absence is certified.','status':'sketch'},
        {'id':'w359-retrieval-003','kind':'measured retrieval failure and bounded repair','statement':'For the observed P0017 recall query the general top three contained zero target cards; the standalone exact-ID rescue returned two complete historical cards with unverified status preserved.',
         'assumptions':['One observed query and the named population store','Standalone proposed helper, not deployed general recall'],
         'source':{'path':'PROBE_CHECKS.json','quote':'baseline_relevant_top3=0; rescue_relevant_hits=2; passed=8'},
         'proof_or_counterexample':'Reproduce check_problem_probe.py; raw baseline and exact after-results are saved. Rescue elapsed 0.0508 s; original general recall 24.5424 s; workloads differ so no speedup ratio is asserted.',
         'independent_reviewer':'claude-4a88bc43 (implementation review pending)','remaining_gap':'No live/global performance evaluation, no detection of new primary sources, and no deployment.','status':'numerical evidence'},
        {'id':'w359-review-w358-posterior','peer':'w358','claim_id':'POSTERIOR_BRIDGE_CHECK.md sections 1-3','kind':'independent peer review','verdict':'KEEP',
         'statement':'The posterior inequalities imply q=1; an assumed q<1 gives C_P<=t(1+q)/(1-q). For centered Exp(1)-1, every admissible universal contraction coefficient obeys q(t)>=exp(-t/4), and the explicit t=1,a=49/100 test has ratio greater than 0.7.',
         'assumptions':['t>0 noise variance','independent Gaussian noise','0<a<1/2 for exponential Sobolev tests','finite C_P or justified regular approximation in the conditional reduction'],
         'source':{'path':'~/brain_workers/w358/POSTERIOR_BRIDGE_CHECK.md','quote':'liminf of the energy ratio >=exp(-t/4)'},
         'proof_or_counterexample':'Uniform CDF quotient bounds and positive-tail integration, including exact rational lower bound 0.7021971, independently checked in REVIEW_w358_POSTERIOR.md.',
         'independent_reviewer':'w359','remaining_gap':'No universal strict nonlinear contraction is proved.','status':'independently checked proof'}]
    with (ROOT/'CLAIMS.jsonl').open('w',encoding='utf-8') as out:
        for row in [admin]+candidates+reviews+extra:
            out.write(json.dumps(row,ensure_ascii=False)+'\n')
    put('REVIEW_PACKET.json',{'target':'P0017','worker':'w359','supervisor':'claude-4a88bc43','peers':['w357','w358'],'own_independent_referee':'w362',
                              'source_audit':'SOURCE_STATUS.json','attempt':'ATTEMPT.md','claims':'CLAIMS.jsonl','peer_verdicts':'REVIEW_VERDICTS.jsonl',
                              'reviews':['REVIEW_w357.md','REVIEW_w358.md','REVIEW_w358_POSTERIOR.md'],
                              'own_draft_proofs':'CONE_COUNTEREXAMPLE.md','exact_edges':'EDGES.jsonl','bundle_state':'BUNDLE_STATES.json',
                              'implementation_proposal':'patches/01_exact_problem_probe.diff','checks':['MATH_CHECKS.json','PROBE_CHECKS.json','BUNDLE_VALIDATION.json','PATCH_CHECK.json'],
                              'hardest_gap':'Uniform strict posterior Dirichlet contraction for arbitrary nonlinear finite-energy tests; published full KLS proofs not independently audited here.',
                              'formal_theorem_check':None,'trusted_axioms_receipt':None,'novelty_claim':False})
    print(json.dumps({'submitted_bundle':str(destination),'validation':validation,'claim_rows':1+len(candidates)+len(reviews)+len(extra),'patch':'patches/01_exact_problem_probe.diff','own_review':'pending; concepts only'},indent=2))

if __name__=='__main__':
    main()
