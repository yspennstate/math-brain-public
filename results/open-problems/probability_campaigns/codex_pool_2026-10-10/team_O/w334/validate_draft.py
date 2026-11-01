"""Validate draft structure and exact endpoint quotations; never ingest."""
from pathlib import Path
from collections import defaultdict
import json
import sqlite3

here=Path(__file__).resolve().parent
bundle=json.loads((here/'bundles/bundle_001.json').read_text(encoding='utf-8'))
entries=bundle['entries']
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w334' and 0<len(entries)<=200
by_key={e['key']:e for e in entries}
assert len(by_key)==len(entries)
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
for e in entries:
    assert required<=e.keys()
    assert e['kind'] in {'definition','lemma','theorem','concept'}
    assert isinstance(e['assumptions'],list) and len(e['statement'])>=40
    assert not any(x in e['statement'] for x in ['preceding wired-box model','preceding normalized integral','see source'])
    if e['kind'] in {'lemma','theorem'}:
        assert isinstance(e['proof_text'],str) and len(e['proof_text'])>=100
    else:
        assert e['proof_text'] is None
    assert {'source_id','url','revision','license','excerpt'}<=e['source'].keys()
    assert e['source']['license'].startswith('owner-own-work')
    assert e['source']['url'].startswith('file:///')
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
deps=defaultdict(list)
for r in bundle['relations']:
    assert r['from_key'] in by_key and r['kind'] in allowed
    assert ('to_key' in r)^('to_existing_logical' in r)
    assert 'From "' in r['rationale'] and '"; to "' in r['rationale'] and '\n' not in r['rationale']
    if 'to_key' in r:
        assert r['to_key'] in by_key
        if r['kind']=='depends_on':
            deps[r['from_key']].append(r['to_key'])
seen=set()
active=set()
def visit(k):
    assert k not in active, 'dependency cycle'
    if k in seen:
        return
    active.add(k)
    for other in deps[k]:
        visit(other)
    active.remove(k)
    seen.add(k)
for k in by_key:
    visit(k)

path=Path('~/math-brain-build/local/population/brain.sqlite3')
db=sqlite3.connect(path.as_uri()+'?mode=ro',uri=True)
db.execute('PRAGMA query_only=ON')
edge_receipts=json.loads((here/'edge_quote_receipts.json').read_text(encoding='utf-8'))
existing_count=0
for q in edge_receipts:
    assert q['from_quote'] in by_key[q['from_key']]['statement']
    if 'target_key' in q:
        assert q['to_quote'] in by_key[q['target_key']]['statement']
    else:
        row=db.execute('SELECT body,metadata_json FROM nodes WHERE id=?',(q['target_id'],)).fetchone()
        assert row and q['to_quote'] in row[0]
        assert json.loads(row[1])['logical_id']==q['target_logical']
        existing_count+=1
before=0
for e in entries:
    logical='math:'+e['namespace']+':'+e['logical_name']
    before+=db.execute("SELECT COUNT(*) FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=?",(logical,)).fetchone()[0]
db.close()
hooks=[json.loads(line) for line in (here/'hook_proposals.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
for hook in hooks:
    assert len(hook['text'])<=300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
audit=json.loads((here/'AUDIT_REQUEST.json').read_text(encoding='utf-8'))
assert audit['claimed_result_count']==sum(e['kind'] in {'lemma','theorem'} for e in entries)
assert audit['accepted_keep_count']==0 and all(r['audit_status']=='PENDING w346' for r in audit['results'])
measure=json.loads((here/'experiments.json').read_text(encoding='utf-8'))
assert measure['passed_check_groups']==10 and len(measure['problem_ids'])==10
receipt={'command':'python -B -X utf8 validate_draft.py','status':'PASS_STRUCTURAL_ONLY','context_nodes':sum(e['kind']=='concept' for e in entries),'result_nodes':audit['claimed_result_count'],'draft_nodes':len(entries),'quoted_relations':len(bundle['relations']),'verified_external_endpoint_quotes':existing_count,'new_logical_ids_currently_in_live_store':before,'drafts_ready_for_blind_audit':1,'independent_keeps':0,'hook_proposals':len(hooks),'live_database_writes':0,'mathematical_correctness_independently_certified':False}
(here/'validation.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
