"""Build local claim rows and an authorized concept-only DRAFT inbox bundle."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w480')
OWN_SOURCE = {
    'source_id': 'owner-own-work:probability300-c0056-w480-20261010',
    'url': 'file:///~/brain_workers/w480/ATTEMPT.md',
    'revision': '2026-10-10-author-draft',
    'license': 'owner-own-work',
    'excerpt': None,
}
text = (ROOT / 'ATTEMPT.md').read_text(encoding='utf-8')
sections = {}
for block in text.split('\n## ')[1:]:
    heading, _, body = block.partition('\n')
    sections[heading.split(':')[0]] = '## ' + heading + '\n' + body.strip()

items = [
    ('L1', 'anderson-single-site-poisson-entropy-identity', 'Exact conditional single-site entropy bound',
     'For real a, b>0 and lambda>0, let y(v)=b/[pi*((lambda*v-a)^2+b^2)] and Phi(t)=t*log(1+t). Then integral_R Phi(y(v)) dv=(2/lambda)*log((1+sqrt(1+1/(pi*b)))/2)<=log(1+1/(pi*b))/lambda. If V has an independent density bounded by R, E Phi(y(V))<=R*log(1+1/(pi*b))/lambda, conditionally on the cavity.',
     ['b>0', 'lambda>0', 'For the conditional extension, V is independent of a,b and has Lebesgue density bounded by R.']),
    ('L2', 'anderson-logarithmic-cavity-entropy-purity-criterion', 'Conditional logarithmic cavity criterion for spectral purity',
     'Let H_lambda=-A+lambda*V on l2(Z^3), with nearest-neighbor adjacency A, fixed lambda>0 and iid uniform V_x on [-1,1]. Delete site x; write Sigma_x(z)=<h_x,(H_lambda^(x)-z)^(-1)h_x> and b_x(E,eta)=eta+Im Sigma_x(E+i*eta). If J is bounded and open and sup_{0<eta<=1} E integral_J log(1+1/b_0(E,eta)) dE is finite, then almost surely the spectral restriction of H_lambda to J is purely absolutely continuous. This implication assumes the logarithmic bound and does not establish it.',
     ['Fixed lambda>0 before eta->0', 'Infinite-volume cavity operator', 'Uniform-in-eta logarithmic bound on J', 'iid uniform site law; in particular own-site independence and bounded density']),
    ('L3', 'finite-cavity-logarithmic-resolvent-bound-divergence', 'Finite cavities cannot supply a uniform logarithmic bound',
     'Let B be any finite-dimensional self-adjoint matrix, h a vector, J a nonempty bounded interval, and b(E,eta)=eta+Im<h,(B-E-i*eta)^(-1)h>. As eta->0, [integral_J log(1+1/b(E,eta)) dE]/log(1/eta)->|J|. The same limit holds with expectation for arbitrary random finite cavities. Thus the infinite-volume logarithmic criterion cannot be verified by taking eta->0 at a fixed finite volume.',
     ['Finite-dimensional self-adjoint B', 'Finite vector h', 'J nonempty bounded interval', 'For the annealed extension the random matrix and vector are measurable and finite almost surely']),
    ('C1', 'annealed-spectral-density-does-not-imply-sample-purity', 'Bounded annealed density can coexist with atomic sample spectra',
     'For the scalar random operator H=lambda*V with fixed lambda>0 and V uniform on [-1,1], every sample spectral measure is the atom delta_(lambda*V), but the expected spectral measure has bounded density 1/(2*lambda) on [-lambda,lambda]. The averaged Poisson-smoothed density has the same bound. Hence a bounded averaged density alone does not imply almost-sure absolutely continuous spectrum. This is an implication counterexample, not a counterexample to lattice delocalization.',
     ['Scalar toy operator, no hopping', 'lambda>0', 'Uniform scalar V']),
    ('L4', 'anderson-cavity-perturbation-regulator-cutoff', 'Cavity perturbation controls only positive regulators',
     'For nearest-neighbor Anderson cavities on Z^3 with |V_x|<=M, |Sigma_lambda(E+i*eta)-Sigma_free(E+i*eta)|<=6*lambda*M/eta^2. If b_free(E,eta)>=b_*>0 on J and 0<eta<=1, then b_lambda>=b_*/2 whenever eta^2>=12*lambda*M/b_*. This gives integral_J log(1+1/b_lambda)<=|J|*log(1+2/b_*) only above that cutoff; it supplies no fixed-positive-lambda eta->0 bound.',
     ['Bounded potential |V_x|<=M', 'lambda>0', 'eta>0', '||h_x||^2=6', 'For the lower-bound consequence assume the displayed uniform free-cavity lower bound']),
    ('L5', 'anderson-bounded-disorder-nonzero-window-mass', 'Small bounded disorder preserves some window mass',
     'Let H_0=-A be nearest-neighbor hopping on l2(Z^3), and J any nonempty open interval contained in (-6,6). For any M<infinity, there is lambda_J,M>0 such that for every diagonal potential with |V_x|<=M and 0<lambda<lambda_J,M, the spectral projection of H_0+lambda*V onto J is nonzero. This follows from norm continuity of continuous functional calculus and positive free spectral weight, and says nothing about purity.',
     ['Nearest-neighbor hopping on Z^3', 'J nonempty open subinterval of the free band', 'Uniform bound |V_x|<=M<infinity', 'lambda sufficiently small depending on J,M']),
]

claims_path = ROOT / 'CLAIMS.jsonl'
existing = [json.loads(line) for line in claims_path.read_text(encoding='utf-8').splitlines() if line.strip()]
known = {row['claim_id'] for row in existing}
new = []
for short, slug, title, statement, assumptions in items:
    key = f'C0056-W480-{short}'
    if key in known:
        continue
    new.append({
        'claim_id': key, 'kind': 'conditional_lemma' if short == 'L2' else ('counterexample' if short == 'C1' else 'scoped_lemma'),
        'statement': statement, 'assumptions': assumptions,
        'source': dict(OWN_SOURCE, path=str(ROOT / 'ATTEMPT.md'), section=short),
        'proof_or_counterexample': sections[short],
        'independent_reviewer': 'w482 (requested; verdict pending)',
        'independent_adversary': 'w481 (statement sent before proof)',
        'remaining_gap': 'LG is unproved; GOE is outside this route. This lemma still needs independent review.',
        'status': 'proved special case',
        'status_detail': 'Complete author proof of the exact scoped statement; not independently checked.',
        'parent_problem_solved': False,
        'served_model_evidence': {'author': 'UNAVAILABLE', 'referee': 'PENDING'},
    })
gap_key = 'C0056-W480-LG'
if gap_key not in known:
    new.append({
        'claim_id': gap_key, 'kind': 'missing_input',
        'statement': 'For the infinite-volume nearest-neighbor Anderson operator on Z^3 with iid uniform potentials in [-1,1], there exist a fixed nonempty bounded open J inside (-6,6) and lambda_0>0 such that for every fixed 0<lambda<lambda_0, sup_{0<eta<=1} E integral_J log(1+1/[eta+Im<h_0,(H_lambda^(0)-E-i*eta)^(-1)h_0>]) dE is finite.',
        'assumptions': ['Infinite volume before eta->0', 'Fixed positive lambda', 'iid bounded-density uniform law'],
        'source': dict(OWN_SOURCE, path=str(ROOT / 'ATTEMPT.md'), section='Notation and the single hardest input'),
        'proof_or_counterexample': 'Not proved. Resolvent identity gives only a regulator cutoff of order sqrt(lambda); finite-volume limits and averaged density cannot fill the gap.',
        'independent_reviewer': 'w482 (requested; verdict pending)',
        'remaining_gap': 'The claimed fixed-lambda uniform logarithmic control is itself the missing input; no GOE implication is known here.',
        'status': 'conjecture', 'parent_problem_solved': False,
    })
with claims_path.open('a', encoding='utf-8') as handle:
    for row in new:
        handle.write(json.dumps(row, ensure_ascii=False) + '\n')

entries = []
for short, slug, title, statement, assumptions in items:
    entries.append({
        'key': short.lower(), 'namespace': 'probability.random-operators', 'logical_name': slug,
        'kind': 'concept', 'title': 'DRAFT: ' + title,
        'statement': 'UNREVIEWED CAMPAIGN DRAFT; author proof saved, independent review pending. ' + statement,
        'proof_text': None, 'assumptions': assumptions,
        'domain': 'probability / random Schrodinger operators', 'source': OWN_SOURCE,
    })
entries.append({
    'key': 'lg', 'namespace': 'probability.random-operators',
    'logical_name': 'anderson-infinite-volume-logarithmic-cavity-missing-input',
    'kind': 'concept', 'title': 'UNPROVED: infinite-volume logarithmic cavity bound',
    'statement': next(r['statement'] for r in existing + new if r['claim_id'] == gap_key) + ' This is an unproved input, not a theorem or a solved-parent claim. The associated conditional reduction does not address GOE statistics.',
    'proof_text': None, 'assumptions': ['Infinite-volume cavity', 'Fixed positive lambda', 'Uniform control for all 0<eta<=1'],
    'domain': 'probability / random Schrodinger operators', 'source': OWN_SOURCE,
})
relations = [
    {'from_key': 'l2', 'to_key': 'l1', 'kind': 'depends_on', 'rationale': 'The conditional reduction first converts logarithmic cavity control into the single-site Phi entropy bound by the exact L1 identity.'},
    {'from_key': 'l2', 'to_key': 'lg', 'kind': 'depends_on', 'rationale': 'The L2 conclusion explicitly assumes LG, which is separately labeled unproved.'},
    {'from_key': 'l3', 'to_key': 'lg', 'kind': 'semantic_association', 'rationale': 'L3 concerns finite matrices and warns against replacing the explicitly infinite-volume LG input by a fixed finite cavity.'},
    {'from_key': 'c1', 'to_key': 'l2', 'kind': 'semantic_association', 'rationale': 'C1 refutes a weaker first-moment-only implication, while L2 adds a uniform entropy hypothesis.'},
    {'from_key': 'l4', 'to_key': 'lg', 'kind': 'semantic_association', 'rationale': 'The deterministic L4 comparison reaches only positive regulator cutoffs and leaves the all-eta LG bound open.'},
    {'from_key': 'l5', 'to_key': 'l2', 'kind': 'semantic_association', 'rationale': 'L5 supplies nonzero mass for small bounded disorder; L2 supplies purity only conditional on LG.'},
]
bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w480', 'bundle_slug': 'probability300-c0056-log-cavity-w480-001', 'entries': entries, 'relations': relations}
local = ROOT / 'bundle_001.json'
local.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
INBOX.mkdir(exist_ok=True)
final = INBOX / 'bundle_001.json'
if not final.exists():
    part = INBOX / 'bundle_001.part'
    part.write_bytes(local.read_bytes())
    part.rename(final)
else:
    assert final.read_bytes() == local.read_bytes(), 'Never overwrite an existing different peer/inbox artifact'

allowed = {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
keys = {e['key'] for e in entries}
assert len(keys) == len(entries)
assert all(e['kind'] == 'concept' and e['proof_text'] is None and e['source']['license'] == 'owner-own-work' for e in entries)
assert all(r['from_key'] in keys and r['to_key'] in keys and r['kind'] in allowed for r in relations)
graph = {key: [] for key in keys}
for r in relations:
    if r['kind'] == 'depends_on':
        graph[r['from_key']].append(r['to_key'])
def visit(node, path):
    assert node not in path, 'Cyclic depends_on'
    for child in graph[node]:
        visit(child, path | {node})
for key in keys:
    visit(key, set())

support = []
for r in relations:
    support.append(dict(r, from_statement=next(e['statement'] for e in entries if e['key']==r['from_key']), to_statement=next(e['statement'] for e in entries if e['key']==r['to_key']), status='DRAFT; independent review pending'))
(ROOT / 'RELATION_SUPPORT.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in support), encoding='utf-8')
(ROOT / 'BUNDLE_VALIDATION.json').write_text(json.dumps({'status':'LOCAL_SCHEMA_PASS', 'entries':len(entries), 'relations':len(relations), 'all_entries_concept':True, 'depends_on_acyclic':True, 'integration_run':False, 'reviewed':False, 'ingested':False, 'retrievable':False}, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'new_claim_rows':len(new), 'draft_entries':len(entries), 'relations':len(relations), 'inbox_path':str(final), 'live_store_mutated':False}))
