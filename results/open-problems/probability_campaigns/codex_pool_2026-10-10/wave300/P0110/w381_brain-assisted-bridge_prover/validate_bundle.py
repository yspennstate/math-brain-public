"""Local schema/edge checks only; never a mathematical or integration audit."""
import json
from pathlib import Path

root=Path(__file__).resolve().parent
path=root/'drafts'/'bundle_001.json'
bundle=json.loads(path.read_text(encoding='utf-8'))
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w381'
assert len(bundle['entries'])<=200
keys={e['key'] for e in bundle['entries']}
assert len(keys)==len(bundle['entries'])
allowed={'definition','lemma','theorem','concept'}
relation_kinds={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
for e in bundle['entries']:
    assert set(('key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'))<=e.keys()
    assert e['kind'] in allowed and len(e['statement'])>40
    assert bool(e['proof_text']) if e['kind'] in {'lemma','theorem'} else e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
    assert 'independently-unchecked' in e['source']['revision']
deps={k:[] for k in keys}
for r in bundle['relations']:
    assert r['from_key'] in keys and r['kind'] in relation_kinds
    assert ('to_key' in r)!=('to_existing_logical' in r)
    if 'to_key' in r: assert r['to_key'] in keys
    else: assert r['to_existing_logical']=='math:probability.core:open-problem-p0110-an-iid-fpp-law-with-proved-kpz-exponent-relation'
    if r['kind']=='depends_on': deps[r['from_key']].append(r['to_key'])
active=set();finished=set()
def visit(k):
    assert k not in active,'cycle'
    if k in finished:return
    active.add(k)
    for to in deps[k]:visit(to)
    active.remove(k);finished.add(k)
for k in keys:visit(k)
support=[json.loads(s) for s in (root/'EDGE_SUPPORT.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(support)==len(bundle['relations'])
assert all(s['from_statement_quote'] and s['to_statement_quote'] for s in support)
claims=[json.loads(s) for s in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
assert len({c['claim_id'] for c in claims})==len(claims)
assert all(c['assumptions'] and c['remaining_gap'] and c['independent_reviewer'] for c in claims)
assert not any(c['status']=='independently checked proof' for c in claims)
receipt={'command':'python -B -X utf8 ~/brain_workers/w381/validate_bundle.py','entries':len(keys),'relations':len(support),'claim_rows':len(claims),'license_check':True,'depends_on_acyclic':True,'both_edge_ends_quoted':True,'independent_audit':False,'live_ingestion':False,'formal_math_proof_check':False,'failures':0}
(root/'bundle_validation_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
