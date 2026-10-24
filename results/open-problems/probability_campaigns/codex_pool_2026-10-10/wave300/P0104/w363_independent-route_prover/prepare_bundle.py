"""Prepare concept drafts and structural receipts; never run integration."""
import json
from pathlib import Path
import re

root = Path(__file__).parent
inbox = Path('~/math-brain-inbox/w363')
inbox.mkdir(parents=True, exist_ok=True)
before = len(list(inbox.glob('bundle_*.json')))
spec = 'mathbrain-draft-v1'
bundle = {'spec': spec, 'author_agent': 'w363',
          'bundle_slug': 'p0104-bernoulli-resampling-harmonic-gap-w363-20261010',
          'entries': [], 'relations': []}

def entry(key, logical, title, statement, assumptions, source_claim):
    bundle['entries'].append({
        'key': key, 'namespace': 'probability.fpp', 'logical_name': logical,
        'kind': 'concept', 'title': 'Research draft: '+title,
        'statement': 'DRAFT; independent mathematical review pending. '+statement,
        'proof_text': None, 'assumptions': assumptions, 'domain': 'probability theory',
        'source': {'source_id': 'owner-probability-campaign:w363:P0104:'+source_claim,
                   'url': 'urn:owner-probability-campaign:w363:P0104:'+source_claim,
                   'revision': 'as-written-2026-10-10',
                   'license': 'owner-own-work; research reconstruction, no novelty or solution claim',
                   'excerpt': None}})

entry('identity', 'finite-bernoulli-passage-variance-resampling-identity',
      'Finite Bernoulli resampling identity',
      'Let f be real on m independent Bernoulli(p) coordinates, 0<p<1. Construct eta^rho by retaining each coordinate with probability rho and otherwise replacing it by an independent Bernoulli(p) bit, independently across coordinates. Define delta_i f=f(eta_-i,1)-f(eta_-i,0) and R_f(rho)=p(1-p) sum_i E[delta_i f(eta) delta_i f(eta^rho)]. Then Var f=integral_0^1 R_f(rho)d rho; in the normalized centered product basis R_f(rho)=sum_{S nonempty}|S|rho^(|S|-1)fhat(S)^2. This is a standard finite special case of Ahlberg-Deijfen-Sfragara arXiv:2302.11367v2 Proposition 6, rederived in this packet.',
      ['finite m', '0<p<1', 'explicit independent-coordinate retention/replacement coupling'], 'C003')
entry('forcing', 'two-point-fpp-forced-edge-minimizer-sandwich',
      'Forced-edge minimizer sandwich',
      'On a finite connected graph, let passage weights be a+Delta eta_e with 0<a, Delta>0, independent Bernoulli(p) eta_e and q=1-p. Choose minimizers with one fixed deterministic tie order. With gamma_e^0 and gamma_e^1 the chosen minimizers after forcing eta_e to 0 or 1, Delta 1_{e in gamma_e^1}<=delta_e T<=Delta 1_{e in gamma_e^0}. Consequently q Delta^2 E H<=D<=p Delta^2 E L for D=pq sum_e E[(delta_e T)^2], where H,L count high/low edges on the chosen unforced minimizer. This selected-minimizer statement does not identify the intersection-of-all-geodesics convention in external overlap theorems.',
      ['finite connected graph and fixed endpoints', 'positive two-point iid weights', 'one deterministic tie order in all forced and unforced environments'], 'C004')
entry('energy', 'rare-cheap-planar-fpp-linear-resampling-energy',
      'Linear resampling energy for rare cheap edges',
      'On nearest-neighbor Z^2 let tau_e=1+eta_e with independent Bernoulli(99/100) eta_e, and T_n=T(0,n e1), integer n>=1. Positive bounded weights localize every minimizer to the deterministic l1 ball of radius 2n. On that finite product let D_n=pq sum_e E[(delta_e T_n)^2], p=99/100, q=1/100. The elementary path-counting and forced-edge argument yields n/600<=D_n<=(99/50)n. This is an energy bound; it supplies no power exponent for Var T_n.',
      ['nearest-neighbor Z^2', 'integer n>=1', 'P(tau_e=1)=1/100; P(tau_e=2)=99/100', 'finite deterministic localization and fixed tie order'], 'C005')
entry('gap', 'rare-cheap-planar-fpp-kpz-harmonic-spectral-gap',
      'Unproved harmonic spectral gap for KPZ variance',
      'For the iid planar two-point law tau_e=1+Bernoulli(99/100), let That_n(S) be the normalized product Fourier coefficients of T_n on the deterministic l1 radius-2n edge graph. Define D_n=sum_{S nonempty}|S|That_n(S)^2 and the probability distribution nu_n(S)=|S|That_n(S)^2/D_n, K=|S|. Exactly Var T_n=D_n E_nu_n[1/K]. Because n/600<=D_n<=(99/50)n, Var T_n=n^(2/3+o(1)) is equivalent to E_nu_n[1/K]=n^(-1/3+o(1)). The harmonic estimate is CONJECTURAL and unproved. The source P0104 question also includes positivity in a suitable dimension, not settled by this draft.',
      ['same bounded planar iid law and deterministic localization', 'normalized product Fourier basis', 'no curvature or generic-flat-edge assertion'], 'C006-C007')
entry('leakage', 'typical-spectral-degree-does-not-control-harmonic-moment',
      'Typical spectral degree misses low-degree leakage',
      'An abstract integer-valued K_n can satisfy K_n/n^(1/3)->1 in probability while E[1/K_n] is not n^(-1/3+o(1)). Put probability n^(-1/4) at K_n=1 and the remaining probability at ceil(n^(1/3)). Then convergence in probability holds but E[1/K_n]>=n^(-1/4). This is an audit counterexample to a typical-scale inference, not an FPP law and not a counterexample to the KPZ conjecture.',
      ['integer n>=2', 'abstract positive spectral-degree distribution', 'no FPP realizability asserted'], 'C008')
bundle['relations'] = [
    {'from_key':'energy','to_key':'forcing','kind':'depends_on','rationale':'The linear energy proof uses the forced-high minimizer lower bound and forced-low upper bound.'},
    {'from_key':'gap','to_key':'identity','kind':'depends_on','rationale':'The exact harmonic variance reduction uses the stated finite Bernoulli spectral identity.'},
    {'from_key':'gap','to_key':'energy','kind':'depends_on','rationale':'Two-sided linear energy makes the harmonic exponent equivalent to the variance exponent.'},
    {'from_key':'leakage','to_key':'gap','kind':'semantic_association','rationale':'The abstract counterexample shows why the unproved harmonic gap needs a weighted small-degree tail estimate; it does not refute the FPP claim.'}]

required = {'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
keys = {entry['key'] for entry in bundle['entries']}
assert len(keys) == len(bundle['entries']) <= 200
for item in bundle['entries']:
    assert required <= item.keys()
    assert item['kind'] == 'concept' and item['proof_text'] is None
    assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', item['logical_name'])
    assert item['source']['license'].startswith('owner-own-work')
    assert item['statement'].startswith('DRAFT;')
edges = {k:[] for k in keys}
for relation in bundle['relations']:
    assert relation['from_key'] in keys and relation['to_key'] in keys
    assert relation['kind'] in {'depends_on','semantic_association'}
    if relation['kind'] == 'depends_on':
        edges[relation['from_key']].append(relation['to_key'])
def check_dag(k, stack):
    assert k not in stack
    for target in edges[k]:
        check_dag(target,stack|{k})
for key in keys:
    check_dag(key,set())
for index in range(1,1000):
    destination = inbox/f'bundle_{index:03d}.json'
    part = destination.with_suffix('.part')
    if not destination.exists() and not part.exists():
        break
else:
    raise RuntimeError('No free own-agent bundle name')
with part.open('x',encoding='utf-8') as stream:
    json.dump(bundle,stream,indent=2)
    stream.write('\n')
part.rename(destination)
receipt = {'spec':spec,'bundle_path':str(destination),'status':'STRUCTURAL_PASS',
           'draft_files_before':before,'draft_files_after':before+1,
           'entries':len(bundle['entries']),'relations':len(bundle['relations']),
           'concept_entries':len(bundle['entries']),'theorem_entries':0,
           'all_supporting_relation_ends_local':True,'depends_on_acyclic':True,
           'cryptographic_ceremony_performed':False,'integration_run':False,
           'states':{'prepared':True,'submitted_for_review':False,
                     'independently_reviewed':False,'ingested':False,'retrievable':False}}
(root/'BUNDLE_VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')

# Correct an ambiguous mathematical typography in the earlier claim row.
claims = [json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
for claim in claims:
    if claim['claim_id'] == 'w363-C005':
        claim['statement'] = claim['statement'].replace('sum_e E(delta_e T(0,n e1))^2','sum_e E[(delta_e T(0,n e1))^2]')
    if claim['claim_id'] == 'w363-C001':
        claim['novelty'] = 'Restates the recorded campaign obstruction at-p0104; elementary, no novelty claim'
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(row)+'\n' for row in claims),encoding='utf-8')
report = (root/'REPORT.md').read_text(encoding='utf-8').replace('weights 1/2 with','weights 1 and 2 with')
(root/'REPORT.md').write_text(report+'\nDraft: '+str(destination)+'. Five concept cards and four supported relations passed local structural validation. Reviewed, ingested and retrievable remain false.\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
