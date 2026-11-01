"""Prepare reviewable concept drafts; optionally submit to the explicitly assigned inbox."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re

root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--submit',action='store_true')
args=parser.parse_args()

def owner_source(locator):
    return {'source_id':'owner:P0297:w522:'+locator,
            'url':'~/brain_workers/w522/ATTEMPT.md',
            'revision':'2026-10-10-author-draft-pending-w524',
            'license':'owner-own-work','excerpt':None}

def concept(key,name,title,statement,assumptions,source):
    return {'key':key,'namespace':'probability.lqg','logical_name':name,
            'kind':'concept','title':title,'statement':statement,
            'proof_text':None,'assumptions':assumptions,
            'domain':'probability and random geometry','source':source}

entries=[
concept('normalization','lqg-metric-dimension-parameter-normalization',
        'LQG metric dimension: parameter normalization',
        'For each fixed gamma in (0,2), the gamma-Liouville quantum gravity metric D_h associated with a whole-plane Gaussian free field h has deterministic almost-sure Hausdorff dimension d_gamma. Its metric Weyl-scaling parameter is xi=gamma/d_gamma, and Q=2/gamma+gamma/2. Hence d_gamma=gamma/xi. These relations parametrize the unknown exponent; they do not evaluate it. The known Brownian-map anchor is d_sqrt(8/3)=4. Gamma=2 is outside this subcritical statement. Current openness on 2026-10-10 is UNKNOWN in this packet; a checked 2026-06-09 primary paper still reports the general value unknown.',
        ['gamma is fixed in (0,2)','h is a whole-plane GFF with fixed additive constant','D_h is the gamma-LQG metric up to deterministic positive scale'],
        {'source_id':'arxiv:1905.00383:problem-7.1','url':'https://arxiv.org/abs/1905.00383',
         'revision':'Problem 7.1, as read 2026-10-10','license':'arxiv-nonexclusive','excerpt':None}),
concept('prior-correction','lqg-prior-attempt-two-q-over-xi-normalization-error',
        'Draft correction: a prior LQG normalization identity is inconsistent',
        'AUTHOR DRAFT, independent review pending w524. A related archived attempt D0049-A001 states d_gamma=2Q/xi. Under 0<gamma<2, D>0, xi=gamma/D and Q=2/gamma+gamma/2, direct substitution gives 2Q/xi=(1+4/gamma^2)D>D. The correct rearrangement is D=gamma/xi. At gamma^2=8/3 and D=4 the archived expression gives 10, whereas the corrected expression gives 4. This is a correction to an auxiliary statement; the original problem of determining the general metric dimension remains unresolved by this draft. The reviewer-only diff retains other archived statements as unaudited.',
        ['0<gamma<2','D>0','xi=gamma/D','Q=2/gamma+gamma/2','only the stated normalization identity is audited'],
        owner_source('C1')),
concept('kpz-barrier','lqg-kpz-thick-point-absolute-dimension-nonidentifiability',
        'Draft guard: KPZ and thick-point dimensions leave an unknown absolute scale',
        'AUTHOR DRAFT, independent review pending w524. Assume 0<gamma<2, xi>0, Q=2/gamma+gamma/2, and 0<=x<=2. The maximum over alpha in [-2,2] of max(x-alpha^2/2,0)/(xi(Q-alpha)) is T(x)=(Q-sqrt(Q^2-2x))/xi. For x>0 the optimizer is uniquely alpha=Q-sqrt(Q^2-2x); for x=0 the expression is identically zero. At x=2, gamma/xi-(2-alpha^2/2)/(xi(Q-alpha))=(alpha-gamma)^2/(2xi(Q-alpha)). If xi=gamma/D for any positive numerical D, then T(x)/D=(Q-sqrt(Q^2-2x))/gamma and every KPZ equation x=xi*Q*T(x)-xi^2*T(x)^2/2 is satisfied. These equations alone do not identify D. This is a numerical nonidentifiability statement, not the existence of multiple LQG metrics. The metric KPZ theorem for a random Borel set requires independence from h; thick points use the dedicated theorem with an independent ambient set. No uncountable union or probability-one intersection is used here.',
        ['0<gamma<2','xi>0','Q=2/gamma+gamma/2','x in [0,2]','numerical equations are distinguished from all metric axioms'],
        owner_source('L1-L3')),
concept('boundary','lqg-thick-point-critical-corner-quadratic-boundary-layer',
        'Draft guard: the thick-point critical corner depends on the approach path',
        'AUTHOR DRAFT, independent review pending w524. For 0<gamma<2, xi>0 and -2<alpha<2, let Q=2/gamma+gamma/2 and F=(2-alpha^2/2)/(xi(Q-alpha)). Set delta=2-gamma and beta=2-alpha. Then xi*F=(2beta-beta^2/2)/(beta+delta^2/(2gamma)). As gamma and alpha approach 2 from below, if beta/delta^2 tends to finite k>=0, xi*F tends to 8k/(4k+1); if the ratio tends to infinity, the limit is 2. Every limit in [0,2] is possible, so there is no unique continuous extension at this corner. This is a deterministic algebraic boundary calculation, not a claim about the critical LQG metric or a coupling over gamma.',
        ['0<gamma<2','xi>0','-2<alpha<2','both parameters approach 2 from below','the limit is of the numerical normalized spectrum xi*F'],
        owner_source('L2')),
concept('inverse','lqg-kpz-inverse-sharp-uniform-square-root-stability',
        'Draft guard: the normalized KPZ inverse has sharp square-root stability',
        'AUTHOR DRAFT, independent review pending w524. For 0<gamma<2, Q=2/gamma+gamma/2 and x in [0,2], define Y_gamma(x)=Q-sqrt(Q^2-2x). Its optimal Lipschitz constant at fixed gamma is 2gamma/(4-gamma^2), which is unbounded as gamma approaches 2. Uniformly in gamma and x,y in [0,2], |Y_gamma(x)-Y_gamma(y)|<=sqrt(2|x-y|). Across this family, the constant sqrt(2) and exponent 1/2 are sharp. Indeed, putting q=(4-gamma^2)/(2gamma), the endpoint deficit gamma-Y_gamma(2-epsilon) equals sqrt(q^2+2epsilon)-q. This inverse-map statement does not supply an absolute metric dimension or assert a critical metric theorem.',
        ['0<gamma<2','Q=2/gamma+gamma/2','x,y in [0,2]','Y is a numerical normalized inverse map'],
        owner_source('L4'))]

relations=[
    {'from_key':'prior-correction','to_key':'normalization','kind':'cites',
     'rationale':'The correction uses the primary normalization xi=gamma/d_gamma and its Brownian-map anchor.'},
    {'from_key':'kpz-barrier','to_key':'normalization','kind':'depends_on',
     'rationale':'Identifying D with a proposed absolute dimension uses xi=gamma/D and Q=2/gamma+gamma/2.'},
    {'from_key':'boundary','to_key':'kpz-barrier','kind':'depends_on',
     'rationale':'The maximum at x=2 bounds the normalized spectrum by gamma, giving the full range of corner limits.'},
    {'from_key':'inverse','to_key':'boundary','kind':'analogous_to',
     'rationale':'The inverse endpoint is controlled by q_gamma^2, and the thick-point corner by delta^2; both degenerate quadratically near gamma=2.'}]

existing=json.loads((root/'EXISTING_P0297_CARDS.json').read_text(encoding='utf-8'))
logical_ids={r['metadata'].get('logical_id') for r in existing}
for target,reason in [
('math:probability.core:open-problem-p0297-exact-hausdorff-dimension-of-liouville-quantum-gravity',
 'The independent metric-normalization exponent is the missing quantity in the original exact-dimension target.'),
('math:probability.core:attempt-p0297-exact-hausdorff-dimension-of-liouville-quantum-gravity',
 'The prior constant-shift attempt already records xi*d=gamma and leaves xi unknown; this draft analyzes KPZ optimization and its critical corner.')]:
    if target in logical_ids:
        relations.append({'from_key':'kpz-barrier','to_existing_logical':target,
                          'kind':'cites','rationale':reason})

bundle={'spec':'mathbrain-draft-v1','author_agent':'w522',
        'bundle_slug':'lqg-normalization-and-critical-boundary-w522-001',
        'entries':entries,'relations':relations}
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
keys={e['key'] for e in entries}
assert len(keys)==len(entries)<=200
for e in entries:
    assert required<=set(e)
    assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
    assert e['kind']=='concept' and e['proof_text'] is None
    assert e['source']['license'].startswith(('arxiv-nonexclusive','owner-own-work'))
    assert e['statement'] and e['assumptions']
for edge in relations:
    assert edge['from_key'] in keys
    assert edge['kind'] in {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
    assert ('to_key' in edge and edge['to_key'] in keys) or ('to_existing_logical' in edge and edge['to_existing_logical'] in logical_ids)
graph={k:[] for k in keys}
for edge in relations:
    if edge['kind']=='depends_on':
        graph[edge['from_key']].append(edge['to_key'])
def visit(node,path):
    assert node not in path, 'Cyclic depends_on relation'
    for target in graph[node]:
        visit(target,path|{node})
for node in keys:
    visit(node,set())

payload=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
local_path=root/'bundle_local_001.json'
local_path.write_text(payload,encoding='utf-8')
now=datetime.now(timezone.utc)
state={'prepared':{'status':'complete','local_path':str(local_path),'entries':len(entries),'relations':len(relations)},
       'submitted':{'status':'not submitted'},
       'reviewed':{'status':'pending','reviewer':'w524','receipt':None},
       'ingested':{'status':'unconfirmed; no integrator invoked by w522','receipt':None},
       'retrievable':{'status':'unverified; no post-ingestion receipt','receipt':None},
       'formal_proof_receipt':None,'original_target_solved':False}
if args.submit:
    receipt=json.loads((root/'MESH_CLAIM_RECEIPT.json').read_text(encoding='utf-8'))
    if receipt.get('released'):
        raise SystemExit('Previous inbox claim was released: acquire a fresh narrow claim before resubmitting')
    claim=receipt['acquired'][0]
    dest=Path('~/math-brain-inbox/w522')
    assert Path(claim['resource']).resolve()==dest.resolve()
    assert claim['mode']=='exclusive' and receipt['agent']=='w522'
    expiry=datetime.fromisoformat(claim['expires_at'].replace('Z','+00:00'))
    if now>=expiry:
        raise SystemExit('Inbox claim expired: acquire a fresh narrow claim first')
    dest.mkdir(parents=True,exist_ok=True)
    for number in range(1,10000):
        final=dest/f'bundle_{number:03d}.json'
        part=dest/f'bundle_{number:03d}.part'
        if not final.exists() and not part.exists():
            break
    else:
        raise SystemExit('No fresh draft name available')
    assert final.parent.resolve()==dest.resolve() and part.parent.resolve()==dest.resolve()
    with part.open('x',encoding='utf-8') as stream:
        stream.write(payload)
    part.rename(final)
    assert json.loads(final.read_text(encoding='utf-8'))==bundle
    state['submitted']={'status':'submitted DRAFT concepts','path':str(final),'at_utc':now.isoformat(),
                        'claim_id':claim['claim_id'],'publication_state':'not a theorem promotion'}
(root/'BRAIN_STATES.json').write_text(json.dumps(state,indent=2),encoding='utf-8')
print(json.dumps(state,indent=2))
