from datetime import datetime, timezone
import json
import os
from pathlib import Path

base = Path(__file__).resolve().parent
bundle = json.loads((base / 'DRAFT_BUNDLE.json').read_text(encoding='utf-8'))
assert bundle['author_agent'] == 'w499' and bundle['spec'] == 'mathbrain-draft-v1'
allowed_relations = {'depends_on', 'defines', 'proves', 'refutes', 'generalizes', 'specializes', 'analogous_to', 'cites', 'semantic_association'}
keys = {entry['key'] for entry in bundle['entries']}
required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'}
for entry in bundle['entries']:
    assert required <= entry.keys()
    assert entry['kind'] in {'definition', 'concept'}
    assert entry['proof_text'] is None
    assert entry['source']['license'].startswith('owner-own-work')
for relation in bundle['relations']:
    assert relation['kind'] in allowed_relations
    assert relation['from_key'] in keys and relation['to_key'] in keys
    assert relation['from_key'] != relation['to_key']
# The sole dependency edge cannot make a cycle.
assert len(bundle['relations']) == 1

inbox = Path('~/math-brain-inbox/w499')
inbox.mkdir(parents=True, exist_ok=True)
for number in range(1, 1000):
    target = inbox / f'bundle_{number:03}.json'
    partial = target.with_suffix('.json.part')
    if not target.exists() and not partial.exists():
        break
else:
    raise RuntimeError('No unused worker bundle name')
content = json.dumps(bundle, indent=2, ensure_ascii=False) + '\n'
with partial.open('x', encoding='utf-8') as output:
    output.write(content)
    output.flush()
    os.fsync(output.fileno())
partial.rename(target)

hook = json.loads((base / 'DRAFT_HOOK.jsonl').read_text(encoding='utf-8'))
assert hook['proposer'] == 'w499' and len(hook['text']) <= 300
proposal = Path('~/primary_directive/hooks1000/proposals/math-w499.jsonl')
proposal.parent.mkdir(parents=True, exist_ok=True)
already_present = False
if proposal.exists():
    with proposal.open(encoding='utf-8-sig') as existing:
        already_present = any(json.loads(line).get('id') == hook['id'] for line in existing if line.strip())
if not already_present:
    with proposal.open('a', encoding='utf-8') as output:
        output.write(json.dumps(hook, ensure_ascii=False) + '\n')
        output.flush()
        os.fsync(output.fileno())
receipt = {'at_utc': datetime.now(timezone.utc).isoformat(), 'bundle_path': str(target), 'submitted': True, 'reviewed': False, 'review_state': 'PENDING_REFEREE_AND_PROVENANCE', 'ingested': False, 'retrievable': 'UNKNOWN; no live-store retrieval or integration is claimed', 'entries': len(bundle['entries']), 'relations': len(bundle['relations']), 'hook_path': str(proposal), 'hook_id': hook['id'], 'hook_submission': 'ALREADY_PRESENT' if already_present else 'APPENDED', 'integrator_run': False}
(base / 'SUBMISSION_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
