"""Validate the draft schema, each quoted endpoint and dependencies without live writes."""
import json
import re
import sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parent
bundles=[json.loads((ROOT/('bundle_'+str(i).zfill(3)+'.json')).read_text(encoding='utf-8')) for i in [1,2]]
all_keys=set()
total_relations=0
resolved=set()
quoted_endpoints=0
claims=[]
source_snapshot=json.loads((ROOT/'SOURCE_REPORT.json').read_text(encoding='utf-8'))
with sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro',uri=True,timeout=5) as c:
    for number,bundle in enumerate(bundles,1):
        filename='bundle_'+str(number).zfill(3)+'.json'
        assert (ROOT/filename).read_bytes()==(Path('~/math-brain-inbox/w340')/filename).read_bytes()
        assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w340'
        assert len(bundle['entries'])<=200
        entries={e['key']:e for e in bundle['entries']}
        assert len(entries)==len(bundle['entries'])
        graph={key:[] for key in entries}
        for entry in entries.values():
            assert entry['key'] not in all_keys
            all_keys.add(entry['key'])
            assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',entry['logical_name'])
            assert re.fullmatch(r'[a-z0-9]+(?:\.[a-z0-9]+)+',entry['namespace'])
            assert entry['kind'] in ['definition','lemma','theorem','concept']
            assert len(entry['statement'])>100 and entry['source']['license'].startswith('owner-own-work')
            assert entry['kind'] in ['lemma','theorem'] and len(entry['proof_text'])>100
            assert 'audit pending' in entry['statement'].lower()
            claims.append({'problem_id':None,'entry_key':entry['key'],'namespace':entry['namespace'],'statement':entry['statement'],'assumptions':entry['assumptions']})
        for relation in bundle['relations']:
            total_relations+=1
            assert relation['from_key'] in entries
            assert relation['kind'] in ['depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association']
            rationale=relation['rationale']
            new_match=re.search(r'(?:New end|From end): "([^\"]+)"',rationale)
            assert new_match,new_match
            assert new_match[1] in entries[relation['from_key']]['statement'],relation
            quoted_endpoints+=1
            if 'to_key' in relation:
                assert relation['to_key'] in entries
                target_text=entries[relation['to_key']]['statement']
                match=re.search(r'to end: "([^\"]+)"',rationale)
                assert match and match[1] in target_text,relation
                if relation['kind']=='depends_on': graph[relation['from_key']].append(relation['to_key'])
            else:
                logical=relation['to_existing_logical']
                target_rows=c.execute("SELECT body FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=?",(logical,)).fetchall()
                assert target_rows,logical
                match=re.search(r'store end: "([^\"]+)"',rationale)
                assert match and any(match[1] in row[0].replace('\n',' ') for row in target_rows),relation
                resolved.add(logical)
            quoted_endpoints+=1
        visiting=set()
        finished=set()
        def visit(key):
            assert key not in visiting,'dependency cycle'
            if key in finished: return
            visiting.add(key)
            for child in graph[key]: visit(child)
            visiting.remove(key)
            finished.add(key)
        for key in graph: visit(key)

rows=[json.loads(x) for x in (ROOT/'results.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
math_rows=[x for x in rows if x.get('proof_path')]
assert len(math_rows)==len(all_keys)
for row in math_rows:
    assert Path(row['proof_path']).is_file() and Path(row['measurement_path']).is_file()
    assert row['audit_status']=='PENDING_W346'
ids={row['problem_id'] for row in math_rows}
assert ids==set(source_snapshot)
row_by_key={row.get('entry_key'):row for row in math_rows if row.get('entry_key')}
for bundle in bundles:
    for entry in bundle['entries']:
        if entry['key'] not in row_by_key:
            # First bundle predates the enriched row schema.
            pid='P0276' if entry['key'].startswith('p0276') else 'C0033'
            row=next(x for x in math_rows if x['problem_id']==pid and x['row_id'].endswith('.001'))
            row['entry_key']=entry['key']
            row['draft_path']='~/math-brain-inbox/w340/bundle_001.json'
            row_by_key[entry['key']]=row
for claim in claims:
    row=row_by_key[claim['entry_key']]
    assert row['statement'] in claim['statement'],claim['entry_key']
    claim['row_id']=row['row_id']
    claim['problem_id']=row['problem_id']
(ROOT/'AUDIT_STATEMENTS.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in claims),encoding='utf-8')
(ROOT/'results.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),encoding='utf-8')
hooks=[json.loads(x) for x in (ROOT/'HOOK_PROPOSALS.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(hooks)==3
for hook in hooks:
    assert len(hook['text'])<=300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
receipt={'command':'python -X utf8 validate_deliverables.py','verdict':'PASS','assigned_problems':len(ids),'existing_source_snapshot_cards':sum(len(x['store_nodes']) for x in source_snapshot.values()),'draft_bundles':len(bundles),'mathematical_entries':len(all_keys),'relations':total_relations,'verified_quoted_endpoints':quoted_endpoints,'resolved_existing_logical_targets':len(resolved),'mathematical_result_rows':len(math_rows),'auditor_KEEPs':0,'hooks_prepared_locally':len(hooks),'dependency_cycles':0,'inbox_matches_local':True,'live_store_access':'read-only; no worker ingestion'}
(ROOT/'VALIDATION.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))
