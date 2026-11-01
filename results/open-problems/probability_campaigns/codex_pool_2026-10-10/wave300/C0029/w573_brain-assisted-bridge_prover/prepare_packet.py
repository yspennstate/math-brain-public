"""Build only worker-local artifacts. No store writes or global recall changes."""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOC = (ROOT / 'ATTEMPT.md').read_text(encoding='utf-8')

def save(name: str, data: object) -> None:
    p = ROOT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def section(letter: str) -> str:
    text = DOC.split('## Lemma ' + letter + ':', 1)[1]
    return text.split('\n## ', 1)[0].strip()

SOURCE = {'source_id': 'campaign:w573:C0029:2026-10-10',
          'url': None, 'revision': 'w573-author-derived-review-pending-20261010',
          'license': 'owner-own-work', 'excerpt': None}

def entry(key: str, name: str, kind: str, title: str, statement: str,
          assumptions: list[str], proof: str | None) -> dict:
    return {'key': key, 'namespace': 'probability.random-matrices',
            'logical_name': name, 'kind': kind, 'title': title,
            'statement': statement, 'proof_text': proof,
            'assumptions': assumptions, 'domain': 'random matrix theory',
            'source': copy.deepcopy(SOURCE)}

entries = [
 entry('gaussian-limit', 'real-gaussian-hard-edge-limiting-cdf', 'definition',
       'Limiting real Gaussian hard-edge CDF, with finite-n scope warning',
       'Define f(t)=1-exp(-t-t^2/2) for t>=0. For n by n real matrices G_n with independent N(0,1) entries, P(sqrt(n)*s_min(G_n)<=t) tends to f(t) as n tends to infinity for each fixed t>=0 (Tao--Vu, arXiv:0903.0614, Theorem 1.1, after replacing the squared singular-value parameter by t^2). This formula is a limit, not a finite-n identity and not a moving-t error bound. For n=1 the exact CDF is erf(t/sqrt(2)).',
       ['real independent standard normal entries', 'fixed t in the limit'], None),
 entry('cubic-slack', 'cubic-slack-of-real-gaussian-hard-edge-limit', 'lemma',
       'Explicit cubic margin below the coefficient-one envelope',
       'For f(t)=1-exp(-t-t^2/2) and k=exp(-3/2)/3, every t in [0,1] satisfies k*t^3 <= t-f(t) <= t^3/3. Also (t-f(t))/t^3 tends to 1/3 as t decreases to zero. This is an analytic inequality for f, without a finite-n Gaussian assertion.',
       ['0<=t<=1'], section('A')),
 entry('absorption', 'gaussian-cdf-error-absorption-by-cubic-slack', 'lemma',
       'A sufficient coefficient-one error absorption condition',
       'Let 0<=t<=1 and delta,eta,r>=0. Suppose P_n(t)<=(1+delta)*G_n(t)+r and G_n(t)<=1-exp(-t-t^2/2)+eta. Then P_n(t)<=t+r+delta*t+(1+delta)*eta-k*t^3, with k=exp(-3/2)/3. Thus delta*t+(1+delta)*eta<=k*t^3 implies P_n(t)<=t+r. If eta=0, t>=sqrt(delta/k) suffices within [0,1]. A bound on eta for finite n and moving t must be proved separately.',
       ['stated pointwise comparisons', '0<=t<=1', 'delta,eta,r nonnegative'], section('B')),
 entry('cdf-counterexample', 'relative-gaussian-cdf-comparison-does-not-imply-exact-coefficient-one', 'lemma',
       'CDF counterexample to eliminating an uncontrolled relative error',
       'For 0<delta<=1/4 define H_delta(t)=min((1+delta)*(1-exp(-t-t^2/2)),1) for t>=0 and zero for t<0. It is a continuous CDF and H_delta(t)<=(1+delta)*(1-exp(-t-t^2/2)). At t=sqrt(delta), H_delta(t)-t >= delta^(3/2)/2. Therefore a relative comparison with delta_n=min(1/4,(log(n+2))^(-1/16)) does not imply H_delta_n(t)<=t+c^n uniformly in t for any fixed 0<c<1. This disproves an abstract inference, not the Bernoulli conjecture.',
       ['0<delta<=1/4', 'abstract CDF, not claimed to be a matrix CDF'], section('C')),
 entry('row-event', 'exact-schur-event-for-least-singular-value-after-row-append', 'lemma',
       'Exact Schur event for an appended row, including the small-gap branch',
       'Let n>=2, N be any real (n-1) by n matrix, X in R^n, M=[N;X], tau>=0, and mu the second eigenvalue in increasing order of N^T N. If mu<=tau, then s_min(M)^2<=tau for every X. If mu>tau, choose an orthonormal eigenbasis v_0,...,v_(n-1) of N^T N with v_0 in its kernel, positive eigenvalues d_i, and z_i=<X,v_i>. Then s_min(M)^2<=tau if and only if z_0^2<=tau*(1+sum_i z_i^2/(d_i-tau)). For independent random N and X, conditioning on N gives the exact CDF by adding P(mu<=tau) to the expectation of this conditional event on mu>tau. Neither independence of the z_i nor distinct eigenvalues is assumed.',
       ['n>=2', 'N and X real', 'tau>=0'], section('D')),
 entry('denominator', 'controlled-threshold-loss-in-row-append-schur-event', 'lemma',
       'Deterministic threshold loss when removing the spectral parameter',
       'In the full-rank branch of the exact row-append event, with 0<=tau<mu=min_i d_i, set chi_tau^2=1+sum_i z_i^2/(d_i-tau) and chi_0^2=1+sum_i z_i^2/d_i. Then chi_tau^2-chi_0^2=tau*sum_i z_i^2/(d_i*(d_i-tau))>=0 and 1<=chi_tau/chi_0<=(1-tau/mu)^(-1/2). If tau<=mu/2, chi_tau/chi_0<=1+tau/mu. Simply replacing d_i-tau by d_i shrinks the exact event, so it cannot supply an upper bound without compensation.',
       ['0<=tau<mu', 'positive d_i>=mu', 'real z_i'], section('E')),
 entry('scope-correction', 'c0029-prior-attempt-gaussian-finite-n-scope-correction', 'concept',
       'Correction to C0029-A001: Gaussian limit versus finite-n law',
       'The historical C0029-A001 attempt incorrectly calls P(sqrt(n)*s_min(G_n)<=t)=1-exp(-t-t^2/2) an exact finite-n Gaussian law. It is the fixed-t limit as n tends to infinity (Tao--Vu arXiv:0903.0614, Theorem 1.1). At n=1 the exact CDF is erf(t/sqrt(2)) and its slope at zero is sqrt(2/pi)<1, whereas the proposed formula has slope 1. This refutes the finite-n identity. A separate Gaussian stochastic-domination inequality is sufficient for, but stronger than, the Spielman--Teng envelope t+c^n. The prior attempt remains unresolved; correcting this scope does not solve it.',
       ['G_n has independent real N(0,1) entries', 'historical attempt C0029-A001'], None),
 entry('signed-gap', 'c0029-signed-bernoulli-row-comparison-gap', 'concept',
       'Unproved Bernoulli-specific signed row comparison gap',
       'For B_n with independent uniform signs and G_n with independent N(0,1) entries, set F_B,n(t)=P(s_min(B_n)<=t/sqrt(n)) and F_G,n(t)=P(s_min(G_n)<=t/sqrt(n)). An unproved sufficient target is F_B,n(t)-F_G,n(t)<=t-F_G,n(t)+C*exp(-a*n), uniformly for 0<t<1, for fixed a,C>0. The exact row-append event must retain both the small-gap branch and the dependence among the Bernoulli row projections. The published relative error O((log n)^(-1/16)) does not by itself provide this signed estimate. This node states a gap, not a theorem or a claimed resolution.',
       ['independent uniform sign entries in B_n', 'real standard Gaussian entries in G_n', 'uniform 0<t<1'], None),
]

# Other triads independently own the Schur computations. Retain our derivations in
# ATTEMPT.md as shared background, without duplicating their brain-node submissions.
entries = [e for e in entries if e['key'] not in {'row-event', 'denominator'}]
target = 'math:probability.random-matrices:open-problem-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr'
prior = 'math:probability.random-matrices:attempt-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr'
relations = [
 {'from_key':'cubic-slack','to_key':'gaussian-limit','kind':'depends_on','rationale':'The analytic margin is computed for the displayed f(t).'},
 {'from_key':'absorption','to_key':'cubic-slack','kind':'depends_on','rationale':'The bound subtracts k*t^3 using the explicit cubic margin.'},
 {'from_key':'cdf-counterexample','to_key':'cubic-slack','kind':'depends_on','rationale':'The lower bound f(t)>=t-t^3/3 gives the surplus at t=sqrt(delta).'},
 {'from_key':'signed-gap','to_key':'absorption','kind':'cites','rationale':'The absorption condition identifies why a relative error alone leaves a signed small-scale gap.'},
 {'from_key':'scope-correction','to_key':'gaussian-limit','kind':'cites','rationale':'The limiting statement distinguishes fixed-t asymptotics from the finite-n claim.'},
 {'from_key':'scope-correction','to_existing_logical':prior,'kind':'cites','rationale':'Addresses only the historical finite-n exact-law assertion; it does not invalidate or close the remaining small-scale gap.'},
 {'from_key':'signed-gap','to_existing_logical':target,'kind':'cites','rationale':'The unproved signed estimate would establish the exact coefficient-one target.'},
]
bundle = {'spec':'mathbrain-draft-v1','author_agent':'w573',
          'bundle_slug':'c0029-gaussian-scope-and-slack-w573-001',
          'entries':entries,'relations':relations}
save('drafts/bundle_001.json', bundle)

claims_path=ROOT/'CLAIMS.jsonl'
seen={json.loads(line)['id'] for line in claims_path.read_text(encoding='utf-8').splitlines() if line.strip()}
with claims_path.open('a',encoding='utf-8') as out:
    for i,e in enumerate(entries,2):
        claim_id=f'w573-C0029-{i:03}'
        if claim_id in seen:
            continue
        status='proved special case' if e['kind']=='lemma' or e['key']=='scope-correction' else ('conjecture' if e['key']=='signed-gap' else 'sketch')
        out.write(json.dumps({'id':claim_id,'statement':e['statement'],'assumptions':e['assumptions'],
          'source':e['source'],'proof_or_counterexample':e['proof_text'] or e['statement'],
          'independent_reviewer':'w575 pending; served-model identity unverified',
          'remaining_gap':'Signed Bernoulli-specific small-scale CDF bound; no parent solution claim.',
          'status':status,'brain_entry_key':e['key']},ensure_ascii=False)+'\n')

nodes=json.loads((ROOT/'evidence'/'store_retrieval.json').read_text(encoding='utf-8'))['nodes']
edges=[]
bykey={e['key']:e for e in entries}
for rel in relations:
    end=bykey[rel['to_key']]['statement'] if 'to_key' in rel else next(n['body'] for n in nodes if json.loads(n['metadata_json']).get('logical_id')==rel['to_existing_logical'])
    edges.append({'from_key':rel['from_key'],'from_quote':bykey[rel['from_key']]['statement'],
                  'to_key':rel.get('to_key'),'to_existing_logical':rel.get('to_existing_logical'),
                  'to_quote':end,'kind':rel['kind'],'rationale':rel['rationale'],
                  'status':'draft-review-pending','independent_reviewer':'w575 pending'})
(ROOT/'EDGES.jsonl').write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n' for e in edges),encoding='utf-8')

relative='06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl'
live=Path('~/<private-repo>')/relative
with live.open(encoding='utf-8') as stream:
    for lineno,line in enumerate(stream,1):
        if 'C0029' in line:
            old=json.loads(line)
            if old.get('problem_id')=='C0029':
                break
    else:
        raise RuntimeError('Exact C0029 row missing; no patch generated')
new=copy.deepcopy(old)
new['key_identity']='Gaussian limiting law for each fixed t: P(sqrt(n)*s_min(G_n)<=t) -> 1-exp(-t-t^2/2) as n -> infinity; it is not finite-n exact.'
new['result']='For real iid standard Gaussian matrices the fixed-t limiting CDF is f(t)=1-exp(-t-t^2/2), with f(t)~t at zero. At n=1 the finite-n CDF is erf(t/sqrt(2)), so calling f the exact finite-n law is incorrect. Gaussian stochastic domination would suffice but is stronger than the requested envelope t+c^n. Tao--Vu 2010 gives a uniform polynomial absolute comparison error; Sah--Sahasrabudhe--Sawhney arXiv:2405.20308v2 gives a relative error O((log n)^(-1/16)) plus an exponential additive remainder. The exact coefficient-one bound in the small window is not proved by this attempt. No improvement of the parent conjecture is claimed.'
new['correction_note']='DRAFT w573 2026-10-10: finite-n-versus-limit scope correction supported by the n=1 Gaussian CDF and Tao--Vu arXiv:0903.0614 Theorem 1.1; independent review pending. Preserve historical author and attempted-unsolved status.'
new['correction_sources']=['https://arxiv.org/pdf/0903.0614#page=3','https://arxiv.org/html/2405.20308v2#S1']
(ROOT/'patches').mkdir(exist_ok=True)
patch=f'--- a/{relative}\n+++ b/{relative}\n@@ -{lineno},1 +{lineno},1 @@\n-'+line.rstrip('\r\n')+'\n+'+json.dumps(new,ensure_ascii=False)+'\n'
(ROOT/'patches'/'01_c0029_gaussian_scope.diff').write_text(patch,encoding='utf-8')
save('evidence/intake_row_before.json',old)
save('evidence/intake_row_after.json',new)

save('SOURCE_STATUS.json',{
 'target':'C0029','date':'2026-10-10','exact_openness':'UNKNOWN',
 'target_status':'conjecture; no parent solved or novelty claim',
 'primary_sources':[
  {'url':'https://arxiv.org/html/2405.20308v2','version':'v2 2025-01-08','checked':'Eq (2), Theorems 1.1--1.2, Theorem 9.4','finding':'exact sign target differs from relative coefficient 1+O((log n)^(-1/16))'},
  {'url':'https://arxiv.org/pdf/0903.0614','checked':'Theorems 1.1 and 1.3','finding':'real Gaussian fixed-parameter limit; polynomial absolute error; not finite-n exact'}],
 'ranking_locator':'RANKING_2026-09-07.csv:428','prior_attempt_locator':str(live)+f':{lineno}',
 'prior_attempt_id':'C0029-A001','store_reads':'read-only population snapshot; canonical cross-check pending',
 'reviewer':'w575','independent_adversary':'w574','served_model_identity':{'author':None,'referee':None,'status':'UNVERIFIED; requested settings are not response-side evidence'},
 'formal_check':{'performed':False,'theorem':None,'assumptions':None,'trusted_axioms':None},
 'scope':'elementary proved inputs and refuted inference; hardest remaining gap is signed Bernoulli exact-row comparison',
 'history':'H/I named attempt directories returned no exact C0029 match; Lean ranked annotation is not a formal proof receipt'})
save('BUNDLE_STATES.json',{'prepared':True,'submitted':False,'reviewed':False,'ingested':False,'retrievable':False,
 'integrator_run':False,'reason':'Coordinator integrates only after independent review; worker must not write the live store.'})
save('evidence/recall_failure.json',{'command':'python -X utf8 ~/.claude/dreaming/brain.py recall "C0029 Spielman Teng least singular value Bernoulli bridge mistakes"',
 'top_three':['bernoulli_two_thirds_information_methods_2026_09_05','bernoulli_two_thirds_escape_and_long_run_fourier_2026_09_05','reference_phase_retrieval_omega_numerics_2026_05_24'],
 'relevant_to_exact_C0029':0,'evaluated_count':3,
 'proposed_repair':'For an exact problem ID plus random-matrix query, try ID/title-anchored read-only retrieval before semantic expansion. Do not let Bernoulli convolution matches count as matrix theorem support.',
 'live_change':False,'engine_improvement_claim':False})
print(json.dumps({'built_entries':len(entries),'built_relations':len(relations),'patch_line':lineno,'live_store_writes':0}))
