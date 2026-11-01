"""Meaningful read-only fallback boundary checks and draft admission guards."""
import json
import sqlite3
import time
from pathlib import Path
from math_source_fallback import lookup

ROOT = Path(__file__).resolve().parent
database = Path('~/math-brain-build/local/population/brain.sqlite3')
checks = []

def expect_failure(name, callback, error):
    try:
        callback()
    except error:
        checks.append(name)
    else:
        raise AssertionError(name+' did not reject')

card = json.loads((ROOT/'BRIDGE_CARD.json').read_text(encoding='utf-8'))['hits'][0]
result = lookup(database,[],node_id=card['id'])
assert result['hit_count']==1 and result['hits'][0]['body']==card['body']
assert result['hits'][0]['metadata']['claim_kind']=='concept'
assert not result['hits'][0]['source_checked'] and not result['hits'][0]['applicability_checked']
checks.append('exact complete concept card preserved without theorem promotion')
assert lookup(database,[],node_id=card['id']+"' OR 1=1 --")['hit_count']==0
checks.append('node id is literal SQL data, not executable SQL')
expect_failure('unbounded result count rejected',lambda:lookup(database,['percolation'],limit=21),ValueError)
missing = ROOT/'missing_store_should_never_be_created.sqlite3'
assert not missing.exists()
expect_failure('missing store rejected',lambda:lookup(missing,['percolation']),FileNotFoundError)
assert not missing.exists()
checks.append('missing read never creates a SQLite file')
expect_failure('SQL instruction deadline interrupts broad scan',lambda:lookup(database,['percolation'],budget=1e-12),sqlite3.OperationalError)

bundle = json.loads((ROOT/'DRAFT_BUNDLE.json').read_text(encoding='utf-8'))
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w442'
by_key={row['key']:row for row in bundle['entries']}
assert len(by_key)==len(bundle['entries'])<=200
fields={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
for row in bundle['entries']:
    assert fields<=row.keys() and row['statement'] and row['kind'] in {'concept','definition'}
    assert row['proof_text'] is None and row['source']['license'].startswith('owner-own-work')
for row in bundle['relations']:
    assert row['from_key'] in by_key and row['kind'] in {'depends_on','refutes','cites'}
    assert (row.get('to_key') in by_key) or row.get('to_existing_logical')==card['metadata']['logical_id']
checks.append('concept-only bundle, accepted license, exact relation ends')
claims=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(claims)==4 and all(row['review_status']=='pending' and not row['novelty_claim'] for row in claims)
checks.append('own deductions retain pending independent review')
hook=json.loads((ROOT/'hook_proposal.jsonl').read_text(encoding='utf-8'))
assert len(hook['text'])<=300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
checks.append('hook has bounded text and distinct fire and silent cases')
receipt={'passed':len(checks),'checks':checks,'exact_lookup_seconds':result['seconds'],
         'math_proof_receipt':False,'live_store_written':False}
(ROOT/'VALIDATION.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
