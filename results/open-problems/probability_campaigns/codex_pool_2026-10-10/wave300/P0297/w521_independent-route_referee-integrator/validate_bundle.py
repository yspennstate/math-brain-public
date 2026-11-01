import json
import sys
from pathlib import Path

root = Path(__file__).parent
draft = root / (sys.argv[1] if len(sys.argv) > 1 else 'bundle_001.json')
submitted = Path('~/math-brain-inbox/w521') / draft.name
obj = json.loads(draft.read_text(encoding='utf-8'))
assert obj['spec'] == 'mathbrain-draft-v1'
assert obj['author_agent'] == 'w521'
keys = {entry['key'] for entry in obj['entries']}
assert len(keys) == len(obj['entries'])
for entry in obj['entries']:
    for field in ('key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'):
        assert field in entry, (entry['key'], field)
    assert entry['kind'] in {'definition', 'lemma', 'theorem', 'concept'}
    assert entry['proof_text'] is None if entry['kind'] in {'definition', 'concept'} else bool(entry['proof_text'])
    assert entry['source']['license'].lower().startswith(('cc-by-', 'cc-by-sa-', 'cc0', 'apache-2.0', 'gfdl', 'public-domain', 'mit', 'arxiv-nonexclusive', 'owner-own-work'))
for relation in obj['relations']:
    assert relation['from_key'] in keys
    assert ('to_key' in relation) != ('to_existing_logical' in relation)
    if 'to_key' in relation:
        assert relation['to_key'] in keys
    assert relation['kind'] in {'depends_on', 'defines', 'proves', 'refutes', 'generalizes', 'specializes', 'analogous_to', 'cites', 'semantic_association'}
    assert relation['rationale']
assert draft.read_bytes() == submitted.read_bytes()
json.loads((root / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
claims = [json.loads(line) for line in (root / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
verdicts = [json.loads(line) for line in (root / 'VERDICTS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
print(f'VALID: draft={draft.name} entries={len(obj["entries"])} relations={len(obj["relations"])} claims={len(claims)} verdicts={len(verdicts)} submitted_bytes={submitted.stat().st_size}')
