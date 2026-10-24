"""Structural validation only; this script cannot certify the mathematics."""
import json
from pathlib import Path

base = Path('~/math-brain-inbox/w518')
for name in ('bundle_001.part', 'bundle_002.part'):
    obj = json.loads((base/name).read_text(encoding='utf-8'))
    assert obj['spec'] == 'mathbrain-draft-v1'
    assert obj['author_agent'] == 'w518'
    assert len(obj['entries']) <= 200
    keys = {e['key'] for e in obj['entries']}
    for e in obj['entries']:
        assert e['namespace'] == 'probability.core'
        assert e['source']['license'].startswith('owner-own-work')
        assert e['kind'] in ('concept', 'lemma')
        assert (e['proof_text'] is None) == (e['kind'] == 'concept')
    for r in obj['relations']:
        assert r['from_key'] in keys
        assert (r.get('to_key') in keys) or r.get('to_existing_logical', '').startswith('math:probability.core:')
        assert r['kind'] in ('specializes', 'semantic_association')
    print(name, 'entries', len(keys), 'relations', len(obj['relations']), 'JSON/shape OK')

for name in ('~/brain_workers/w518/CLAIMS.jsonl',
             '~/brain_workers/w518/VERDICTS.jsonl',
             '~/brain_workers/w518/BUNDLE_VERDICTS.jsonl',
             '~/primary_directive/hooks1000/proposals/math-w518.jsonl'):
    rows = [json.loads(line) for line in Path(name).read_text(encoding='utf-8').splitlines() if line.strip()]
    print(Path(name).name, 'rows', len(rows), 'JSONL OK')

for name in ('BUNDLE_STATE.json', 'SOURCE_STATUS.json'):
    json.loads((Path('~/brain_workers/w518')/name).read_text(encoding='utf-8'))
    print(name, 'JSON OK')
