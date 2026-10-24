"""Validate draft shape and review-state separation, without integrating."""
import json
import pathlib

root=pathlib.Path(__file__).resolve().parent
bundle=json.loads((root/'bundle_001.json').read_text(encoding='utf-8'))
assert bundle['spec']=='mathbrain-draft-v1'
assert bundle['author_agent']=='w513'
entries={e['key']:e for e in bundle['entries']}
assert len(entries)==len(bundle['entries'])<=200
fields={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
for e in entries.values():
    assert fields<=e.keys()
    assert e['kind'] in {'definition','lemma','theorem','concept'}
    assert e['statement'] and e['assumptions']
    if e['kind'] in {'lemma','theorem'}:
        assert isinstance(e['proof_text'],str) and len(e['proof_text'])>100
        assert 'admit' not in e['proof_text'].lower()
        assert 'sorry' not in e['proof_text'].lower()
    else:
        assert e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
    assert e['novelty_claim'] is False
    assert 'independent mathematical audit pending' in e['review_status']
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
graph={key:[] for key in entries}
for r in bundle['relations']:
    assert r['from_key'] in entries and r['kind'] in allowed and r['rationale']
    assert ('to_key' in r)!=('to_existing_logical' in r)
    if 'to_key' in r:
        assert r['to_key'] in entries
        if r['kind']=='depends_on': graph[r['from_key']].append(r['to_key'])
    else:
        assert r['to_existing_logical'].startswith('math:')
def visit(key,stack,done):
    assert key not in stack,'cyclic dependency'
    if key in done:return
    for other in graph[key]:visit(other,stack|{key},done)
    done.add(key)
done=set()
for key in graph:visit(key,set(),done)
receipt=json.loads((root/'INBOX_RECEIPT.json').read_text(encoding='utf-8'))
assert receipt['prepared'] and not any(receipt[x] for x in ('submitted','reviewed','ingested','retrievable'))
assert pathlib.Path(receipt['path']).read_bytes()==(root/'bundle_001.json').read_bytes()
claim=json.loads((root/'CLAIM_RECEIPT.json').read_text(encoding='utf-8'))
assert claim['acquired'] and claim['resource'].replace('\\','/')==receipt['path'].replace('\\','/')
claims=[json.loads(x) for x in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if x]
assert len({x['id'] for x in claims})==len(claims)
for c in claims:
    assert {'statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status'}<=c.keys()
    assert c['status'] in {'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
    assert c['status']!='independently checked proof'
source=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
assert source['statement_verified'] and source['current_openness']=='UNKNOWN'
assert source['formal_check']['performed'] is False
patch=(root/'patches/01_p0162_bridge_bundle.diff').read_text(encoding='utf-8')
assert patch.startswith('--- a/~/math-brain-inbox/w513/bundle_001.json\n+++ b/~/math-brain-inbox/w513/bundle_001.json\n')
assert ''.join(line[1:] for line in patch.splitlines(keepends=True) if line.startswith('+') and not line.startswith('+++'))==(root/'bundle_001.json').read_text(encoding='utf-8')
result=dict(entries=len(entries),relations=len(bundle['relations']),claims=len(claims),acyclic=True,
            exact_patch=True,staged_bytes_match=True,independent_audit=False,live_integration=False)
(root/'packet_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
