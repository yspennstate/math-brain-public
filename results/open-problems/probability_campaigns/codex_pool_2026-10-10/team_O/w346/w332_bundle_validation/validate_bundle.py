import json
from pathlib import Path
import re
import sqlite3
import time

root=Path(__file__).resolve().parent
start=time.perf_counter()
bundle=json.loads((root/'drafts/bundle_001.json').read_text(encoding='utf-8'))
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w332'
entries=bundle['entries'];relations=bundle['relations']
assert 0<len(entries)<=200
keys={e['key']:e for e in entries};assert len(keys)==len(entries)
names=set()
allowed=['cc-by-sa','cc-by','cc0','apache-2.0','gfdl','public-domain','mit','arxiv-nonexclusive','owner-own-work']
for e in entries:
    assert e['kind'] in ['definition','lemma','theorem','concept']
    assert isinstance(e['statement'],str) and len(e['statement'])>30
    assert re.fullmatch('[a-z][a-z0-9-]*',e['logical_name'])
    assert re.fullmatch('[a-z][a-z0-9-]*(?:[.][a-z][a-z0-9-]*)*',e['namespace'])
    logical=(e['namespace'],e['logical_name']);assert logical not in names;names.add(logical)
    assert isinstance(e['assumptions'],list) and e['domain']
    if e['kind'] in ['lemma','theorem']:
        assert isinstance(e['proof_text'],str) and len(e['proof_text'])>60
    else:
        assert e['proof_text'] is None
    assert all(k in e['source'] for k in ['source_id','url','revision','license'])
    assert any(e['source']['license'].lower().startswith(tag) for tag in allowed)

con=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True)
graph={key:[] for key in keys}
external=[];quotes_checked=0
relation_kinds=['depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association']
for r in relations:
    assert r['from_key'] in keys and r['kind'] in relation_kinds
    assert ('to_key' in r) != ('to_existing_logical' in r)
    beginning,quoted=r['rationale'].split(' FROM: "',1)
    from_quote,to_quote=quoted.split('" TO: "',1)
    assert to_quote.endswith('"');to_quote=to_quote[:-1]
    assert from_quote in keys[r['from_key']]['statement']
    if 'to_key' in r:
        assert r['to_key'] in keys
        assert to_quote in keys[r['to_key']]['statement']
        if r['kind']=='depends_on':graph[r['from_key']].append(r['to_key'])
    else:
        target=r['to_existing_logical']
        bodies=con.execute("SELECT id,body FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=?",(target,)).fetchall()
        assert bodies,'Unresolved live target: '+target
        assert any(to_quote in body for _,body in bodies),'Bad target quote: '+target
        external.append({'logical':target,'matching_card_ids':[cid for cid,body in bodies if to_quote in body]})
    quotes_checked+=2
con.close()
visiting=set();finished=set()
def visit(key):
    assert key not in visiting,'Dependency cycle'
    if key in finished:return
    visiting.add(key)
    for target in graph[key]:visit(target)
    visiting.remove(key);finished.add(key)
for key in keys:visit(key)
rows=[json.loads(line) for line in (root/'results.jsonl').read_text(encoding='utf-8').splitlines() if line]
assert len({r['row_id'] for r in rows})==len(rows)
assert {r.get('entry_key') for r in rows if r.get('entry_key')}==set(keys)
result={'command':'python -X utf8 ~/brain_workers/w332/validate_bundle.py',
    'passed':True,'entries':len(entries),'relations':len(relations),'endpoint_quotes_checked':quotes_checked,
    'external_edges_resolved':len(external),'result_rows':len(rows),'depends_on_acyclic':True,
    'source_licenses_accepted_by_local_schema_check':True,'schema_only_not_integrator_or_math_audit':True,
    'live_store_mode':'ro','elapsed_seconds':time.perf_counter()-start,'external_targets':external}
(root/'validation_receipt.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='external_targets'},indent=2))
