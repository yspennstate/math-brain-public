"""Read-only structural/provenance checks, not a mathematical proof receipt."""
from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parent
bundle=json.loads((root/'bundle_001.json').read_text(encoding='utf-8'))
packet=json.loads((root/'review_packet.json').read_text(encoding='utf-8'))
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
entries={e['key']:e for e in bundle['entries']}
assert len(entries)==len(bundle['entries'])==6
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w502'
assert all(e['kind'] in {'concept','definition'} and e['proof_text'] is None for e in entries.values())
assert all(e['source']['license'].startswith('owner-own-work') for e in entries.values())
assert all(e['source']['url']==(root/'ATTEMPT.md').as_uri() for e in entries.values())
graph={key:[] for key in entries}
for r in bundle['relations']:
    assert r['kind'] in allowed and r['from_key'] in entries
    assert ('to_key' in r) != ('to_existing_logical' in r)
    if 'to_key' in r:
        assert r['to_key'] in entries
        if r['kind']=='depends_on': graph[r['from_key']].append(r['to_key'])
seen=set()
def visit(key,stack):
    assert key not in stack, 'cyclic depends_on'
    if key in seen:return
    for nxt in graph[key]:visit(nxt,stack|{key})
    seen.add(key)
for key in entries:visit(key,set())
assert (root/'bundle_001.json').read_bytes()==Path(packet['bundle_path']).read_bytes()
assert all(x['match'] for x in packet['source_hash_checks'])
assert hashlib.sha256((root/'REVIEWED_W501_LEMMAS.md').read_bytes()).hexdigest()==packet['proof_snapshot_sha256']
edges=[json.loads(line) for line in (root/'EDGE_EVIDENCE.jsonl').read_text(encoding='utf-8').splitlines()]
assert len(edges)==7 and all(e['from_quote'] and e['to_quote'] for e in edges)
assert packet['lifecycle']=={'prepared':True,'submitted':True,'reviewed':False,'ingested':False,'retrievable':False}
claims=[json.loads(line) for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
assert len({x['id'] for x in claims})==len(claims)==6
assert all(x['status'] in {'conjecture','numerical evidence','sketch','proved special case','independently checked proof'} for x in claims)
assert not any(x['status']=='independently checked proof' for x in claims)
print(json.dumps({'structural_check':'PASS','nodes':len(entries),'exact_quoted_edges':len(edges),'claims':len(claims),'source_hash_matches':2,'theorem_nodes':0,'mathematical_proof_certificate':False,'referee':'PENDING'}))
