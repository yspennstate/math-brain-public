"""Offline draft and handoff checks; never imports or invokes the live integrator."""
from pathlib import Path
import json,re
from collections import Counter

root=Path(__file__).resolve().parent
bundle=json.loads((root/'bundles/bundle_001.json').read_text(encoding='utf-8'))
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w330'
assert 1<=len(bundle['entries'])<=200
keys=set();claims={}
for e in bundle['entries']:
    assert {'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}<=e.keys()
    assert e['key'] not in keys;keys.add(e['key']);claims[e['key']]=e
    assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
    assert re.fullmatch(r'[a-z0-9-]+(?:\.[a-z0-9-]+)+',e['namespace'])
    assert e['statement'] and e['title']
    assert e['kind'] in {'definition','lemma','theorem','concept'}
    assert bool(e['proof_text']) if e['kind'] in {'lemma','theorem'} else e['proof_text'] is None
    assert e['source']['license'].startswith(('cc-by-sa','cc-by','cc0','apache-2.0','gfdl','public-domain','mit','arxiv-nonexclusive','owner-own-work'))
    assert {'source_id','url','revision','license','excerpt'}<=e['source'].keys()
cards=json.loads((root/'reports/resolved_edge_cards.json').read_text(encoding='utf-8'))
logicals={json.loads(c['metadata']).get('logical_id') for c in cards}
graph={key:[] for key in keys}
for r in bundle['relations']:
    assert r['kind'] in {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
    assert r['from_key'] in keys
    if 'to_key' in r: assert r['to_key'] in keys
    else: assert r['to_existing_logical'] in logicals
    assert 'Source: "' in r['rationale'] and 'Target: "' in r['rationale']
    if r['kind']=='depends_on' and 'to_key' in r: graph[r['from_key']].append(r['to_key'])
visited=set();stack=set()
def visit(key):
    assert key not in stack, 'dependency cycle'
    if key in visited: return
    stack.add(key)
    for nxt in graph[key]:visit(nxt)
    stack.remove(key);visited.add(key)
for key in graph:visit(key)
rows=[json.loads(x) for x in (root/'RESULT_ROWS.jsonl').read_text(encoding='utf-8').splitlines()]
assert {r['bundle_key'] for r in rows if 'bundle_key' in r}==keys
assert all(r.get('audit_status')=='PENDING_w346' for r in rows)
assert {r['problem_id'] for r in rows}=={'P0032','P0347','C0062','P0028','P0220','C0006','C0066','C0097','C0144','P0020'}
edges=[json.loads(x) for x in (root/'EDGE_ROWS.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(edges)==len(bundle['relations']) and all(e['source_quote'] and e['target_quote'] for e in edges)
measurements={}
for p in (root/'measurements').glob('*.json'):
    item=json.loads(p.read_text(encoding='utf-8'))
    if isinstance(item,dict) and 'experiment' in item: measurements[p.stem]=item
assert measurements['filling']['balanced_cases']==160
assert measurements['young']['family_cases']==99 and measurements['young']['boundary_cases']==35
assert measurements['brownian_lengths']['covariance_entries']==800
assert measurements['hammersley']['hook_vs_tableau_comparisons']==271
assert len(measurements)==10
assert len(measurements['folner']['nested_exhaustion_cases'])==3
hook=json.loads((root/'hooks/math-w330.jsonl').read_text(encoding='utf-8'))
assert len(hook['text'])<=300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
for patch,target,original in [
    ('01_mathbrain_bundle.diff','~/math-brain-inbox/w330/bundle_001.json','bundles/bundle_001.json'),
    ('02_provenance_hook.diff','~/primary_directive/hooks1000/proposals/math-w330.jsonl','hooks/math-w330.jsonl')]:
    text=(root/'patches'/patch).read_text(encoding='utf-8')
    assert text.startswith('--- a/'+target+'\n+++ b/'+target+'\n')
    reconstructed=''.join(line[1:] for line in text.splitlines(keepends=True)[3:] if line.startswith('+'))
    assert reconstructed==(root/original).read_text(encoding='utf-8')
request=json.loads((root/'AUDIT_REQUEST.json').read_text(encoding='utf-8'))
assert request['auditor']=='w346' and request['current_keeps']==0
assert {x['key'] for x in request['claims']}==keys
result=dict(command='python -X utf8 validate_packet.py',status='PASS',entries=len(keys),
    kinds=dict(Counter(e['kind'] for e in bundle['entries'])),relations=len(bundle['relations']),
    unresolved_existing_targets=0,dependency_cycles=0,problem_ids=10,result_rows=len(rows),edge_rows=len(edges),
    measured_experiments=len(measurements),audited_keeps=0,patch_reconstruction='exact',
    note='Schema, references and artifact consistency only; does not independently prove the mathematics or run live integration')
(root/'VALIDATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
