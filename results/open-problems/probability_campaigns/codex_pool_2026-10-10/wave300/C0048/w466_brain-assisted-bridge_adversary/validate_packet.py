"""Packaging validation only; this is not a mathematical proof checker."""
from pathlib import Path
import hashlib
import json
import re
import time

root=Path(__file__).resolve().parent
started=time.perf_counter()
bundle=json.loads((root/'drafts/bundle_001.json').read_text(encoding='utf-8'))
assert bundle['spec']=='mathbrain-draft-v1' and bundle['author_agent']=='w466'
entries=bundle['entries']; assert 0<len(entries)<=200
keys={entry['key']:entry for entry in entries}; assert len(keys)==len(entries)
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
for entry in entries:
    assert required<=entry.keys()
    assert entry['kind']=='concept' and entry['proof_text'] is None
    assert 'DRAFT' in entry['statement'] and 'pending' in entry['statement']
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',entry['logical_name'])
    assert entry['source']['license'].startswith('owner-own-work')
    assert {'source_id','url','revision','license','excerpt'}<=entry['source'].keys()
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
edges=[json.loads(s) for s in (root/'EDGE_EVIDENCE.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
assert len(edges)==len(bundle['relations'])
for relation,edge in zip(bundle['relations'],edges):
    assert relation==edge['relation'] and relation['kind'] in allowed
    assert relation['from_key'] in keys and relation['rationale']
    assert edge['from_statement_quote']==keys[relation['from_key']]['statement']
    if 'to_key' in relation:
        assert edge['to_statement_quote']==keys[relation['to_key']]['statement']
    else:
        assert relation['to_existing_logical'].startswith('math:probability.statmech:open-problem-c0048-')
        assert 'Potts' in edge['to_statement_quote']
claims=[json.loads(s) for s in (root/'CLAIMS.jsonl').read_text(encoding='utf-8-sig').splitlines() if s.strip()]
assert len({row['id'] for row in claims})==len(claims)
for row in claims:
    assert {'statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status'}<=row.keys()
    assert row['status'] in {'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
hook=json.loads((root/'drafts/math-w466.jsonl').read_text(encoding='utf-8'))
assert len(hook['text'])<=300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
for patch_name,target in [('01_C0048_draft_bundle.diff','drafts/bundle_001.json'),('02_C0048_scope_hook.diff','drafts/math-w466.jsonl')]:
    lines=(root/'patches'/patch_name).read_text(encoding='utf-8').splitlines(keepends=True)
    assert lines[0].startswith('--- a/~/') and lines[1].startswith('+++ b/~/')
    reconstructed=''.join(s[1:] for s in lines[2:] if s.startswith('+'))
    assert reconstructed==(root/target).read_text(encoding='utf-8')
arithmetic=json.loads((root/'measurement_arithmetic.json').read_text(encoding='utf-8'))
assert arithmetic['status']=='PASS' and arithmetic['exact_cycle_configurations']==360
retrieval=json.loads((root/'measurement_retrieval.json').read_text(encoding='utf-8'))
assert retrieval['baseline']['spin_glass_cards']==8
assert retrieval['bounded_repair']['live_cards']==2
assert len(retrieval['bounded_repair']['rejected_false_ID_matches'])==1
lifecycle=json.loads((root/'BUNDLE_LIFECYCLE.json').read_text(encoding='utf-8'))
assert lifecycle['staged'] and not any(lifecycle[k] for k in ('submitted','reviewed','ingested','retrievable'))
receipt_path=root/'PEER_REVIEW_RECEIPT.json'
receipt=json.loads(receipt_path.read_text(encoding='utf-8'))
snapshot=Path(receipt['snapshot_path'])
assert receipt['sha256']==hashlib.sha256(snapshot.read_bytes()).hexdigest()
receipt['verdict_scope']='Exact L1-L3 statements and assumptions in PEER_AUDIT.md; any additions to peer snapshot are outside verdict.'
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
for file in root.glob('*.py'):
    compile(file.read_text(encoding='utf-8'),str(file),'exec')
result={'status':'PASS','draft_concepts':len(entries),'edge_rows':len(edges),
        'claim_rows':len(claims),'arithmetic_check':'PASS','logical_ID_scope_check':'PASS',
        'external_mutations':False,'mathematical_referee_gate':'pending',
        'seconds':time.perf_counter()-started,'is_mathematical_proof':False}
(root/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
files=['SOURCE_STATUS.json','ATTEMPT.md','CLAIMS.jsonl','PEER_AUDIT.md','quantitative_obstruction.md',
       'REPORT.md','REVIEW_PACKET.md','drafts/bundle_001.json','EDGE_EVIDENCE.jsonl','drafts/math-w466.jsonl',
       'measurement_arithmetic.json','measurement_retrieval.json','PEER_REVIEW_RECEIPT.json',
       'BUNDLE_LIFECYCLE.json','validation.json','patches/01_C0048_draft_bundle.diff','patches/02_C0048_scope_hook.diff']
hashes={'purpose':'Review content hashes only; not integrator manifests, mathematical proof, store seals or served-model receipts',
        'files':{str(root/file):hashlib.sha256((root/file).read_bytes()).hexdigest() for file in files}}
(root/'ARTIFACT_HASHES.json').write_text(json.dumps(hashes,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
