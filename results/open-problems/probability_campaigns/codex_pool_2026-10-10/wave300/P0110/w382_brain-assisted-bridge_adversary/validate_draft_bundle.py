"""Structural checks only; this validator does not verify mathematics or ingest."""
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent
started = time.perf_counter()
bundle = json.loads((ROOT/'draft_bundle'/'bundle_001.json').read_text(encoding='utf-8'))
claims = [json.loads(row) for row in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if row.strip()]
allowed_status = {'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
for claim in claims:
    for field in ('id','status','statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap'):
        assert field in claim, (claim.get('id'),field)
    assert claim['status'] in allowed_status
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w382'
assert len(bundle['entries'])<=200
keys = {entry['key'] for entry in bundle['entries']}
assert len(keys)==len(bundle['entries'])
entries = {entry['key']:entry for entry in bundle['entries']}
for entry in entries.values():
    for field in ('key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'):
        assert field in entry, (entry['key'],field)
    assert entry['kind'] in ('definition','concept'), 'Unreviewed deductions must not be theorem nodes.'
    assert entry['proof_text'] is None
    assert entry['title'].startswith('DRAFT: ')
    assert entry['source']['license'].startswith('owner-own-work')
known = {row['metadata']['logical_id']:row for row in json.loads((ROOT/'BRAIN_SOURCE_REPORT.json').read_text(encoding='utf-8'))['rows'] if row.get('found') and row['metadata'].get('logical_id')}
allowed_relations={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
dependencies={key:[] for key in keys}
edges=[]
for relation in bundle['relations']:
    assert relation['kind'] in allowed_relations
    assert relation['from_key'] in keys
    if 'to_key' in relation:
        assert relation['to_key'] in keys
        target_statement=entries[relation['to_key']]['statement']
        if relation['kind']=='depends_on': dependencies[relation['from_key']].append(relation['to_key'])
    else:
        assert relation['to_existing_logical'] in known
        target_statement=known[relation['to_existing_logical']]['body']
    edges.append({'from_key':relation['from_key'],'to_key':relation.get('to_key'),
        'to_existing_logical':relation.get('to_existing_logical'),'kind':relation['kind'],
        'from_statement_quote':entries[relation['from_key']]['statement'],
        'to_statement_quote':target_statement,'rationale':relation['rationale'],
        'status':'draft; independent mathematical review pending'})
def walk(key,stack):
    assert key not in stack, 'Dependency cycle.'
    for target in dependencies[key]: walk(target,stack|{key})
for key in keys: walk(key,set())
with (ROOT/'EDGE_SUPPORT.jsonl').open('w',encoding='utf-8') as handle:
    for edge in edges: handle.write(json.dumps(edge,ensure_ascii=False)+'\n')
states=json.loads((ROOT/'BUNDLE_STATE.json').read_text(encoding='utf-8'))
assert states['prepared'] is True
assert not any(states[field] for field in ('submitted','reviewed','ingested','retrievable'))
receipt={'command':'python -X utf8 validate_draft_bundle.py','passed':True,
    'claims':len(claims),'entries':len(entries),'relations':len(edges),
    'resolved_existing_targets':sum('to_existing_logical' in relation for relation in bundle['relations']),
    'theorem_nodes':0,'mathematical_proof_checked':False,'ingested':False,
    'elapsed_seconds':round(time.perf_counter()-started,6)}
(ROOT/'BUNDLE_VALIDATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
