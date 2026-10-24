import json,re,sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parent
bundle=json.loads((ROOT/'bundles/bundle_001.json').read_text(encoding='utf-8'))
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w333'
entries={e['key']:e for e in bundle['entries']}
assert len(entries)==len(bundle['entries'])<=200
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
for entry in entries.values():
    assert required<=entry.keys()
    assert re.fullmatch(r'[a-z][a-z0-9]*(\.[a-z][a-z0-9]*)*',entry['namespace'])
    assert re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*',entry['logical_name'])
    assert entry['kind'] in ['lemma','theorem','concept','definition']
    assert isinstance(entry['statement'],str) and entry['statement'].strip()
    assert isinstance(entry['assumptions'],list)
    if entry['kind'] in ['lemma','theorem']:
        assert entry['proof_text'] and entry['proof_text'].strip()
    else:
        assert entry['proof_text'] is None
    source=entry['source']
    assert {'source_id','url','revision','license'}<=source.keys()
    assert source['license'].startswith('owner-own-work')
deps={key:[] for key in entries}
targets=set()
for edge in bundle['relations']:
    assert edge['from_key'] in entries
    assert ('to_key' in edge) != ('to_existing_logical' in edge)
    assert edge['kind'] in ['depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association']
    assert 'New end:' in edge['rationale']
    assert entries[edge['from_key']]['statement'] in edge['rationale']
    if 'to_key' in edge:
        assert edge['to_key'] in entries
        assert entries[edge['to_key']]['statement'] in edge['rationale']
        if edge['kind']=='depends_on': deps[edge['from_key']].append(edge['to_key'])
    else:
        targets.add(edge['to_existing_logical'])
seen=set(); active=set()
def visit(key):
    assert key not in active,'cyclic dependency'
    if key in seen: return
    active.add(key)
    for child in deps[key]: visit(child)
    active.remove(key); seen.add(key)
for key in entries: visit(key)
conn=sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True)
conn.execute('PRAGMA query_only=ON')
found={row[0] for row in conn.execute("SELECT json_extract(metadata_json,'$.logical_id') FROM nodes WHERE json_extract(metadata_json,'$.logical_id') IN ("+','.join('?' for _ in targets)+')',tuple(targets))}
assert targets<=found,targets-found
checks=json.loads((ROOT/'evidence/check_results.json').read_text(encoding='utf-8'))
assert all(checks[pid]['all_passed'] for pid in ['P0189','P0390','C0100','P0031','P0242','C0011','C0070','C0105','C0153','P0025'])
receipt={'entries':len(entries),'relations':len(bundle['relations']),'existing_logical_targets':len(targets),'unresolved_targets':0,'acyclic_dependencies':True,'all_ten_problem_checks_passed':True,'live_store_opened_read_only':True,'audit_status':'PENDING w347','lean_status':json.loads((ROOT/'evidence/lean_arithmetic_receipt.json').read_text(encoding='utf-8'))}
(ROOT/'evidence/bundle_validation.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
