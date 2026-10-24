"""Validate this worker's review rows and staged source-correction bundle."""
from collections import Counter
import json
from pathlib import Path

root = Path('~/brain_workers/w509')
draft = root / 'BUNDLE_001_DRAFT.json'
staged = Path('~/math-brain-inbox/w509/bundle_001.json')
rows = [json.loads(line) for line in (root / 'REVIEW_VERDICTS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
claims = [json.loads(line) for line in (root / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
bundle = json.loads(staged.read_text(encoding='utf-8'))
assert staged.read_bytes() == draft.read_bytes()
assert len(rows) == len({row['claim'] for row in rows})
assert all(row['verdict'] in {'KEEP', 'FIX', 'DROP'} and row['remaining_gap'] for row in rows)
assert all(row.get('status') and row.get('remaining_gap') for row in claims)
assert bundle['spec'] == 'mathbrain-draft-v1'
assert len(bundle['entries']) == 1 and len(bundle['relations']) == 1
assert bundle['entries'][0]['supersedes_existing'] is True
assert bundle['relations'][0]['kind'] == 'semantic_association'
assert json.loads((root / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))['exact_statement_verified']
assert json.loads((root / 'BUNDLE_STATUS.json').read_text(encoding='utf-8'))['ingested'] is False
packet = (root / 'REVIEW_PACKET.md').read_text(encoding='utf-8-sig')
assert not any(bad in packet for bad in ('â€', 'Ã¡', 'Â²', 'Î”', 'Ïƒ'))
status = (root / 'STATUS.md').read_text(encoding='utf-8').splitlines()
assert status[0] in {'STATE: WORKING', 'STATE: NEEDS_REVIEW'} and any(line.startswith('NEXT: ') for line in status)
print(json.dumps({'verdicts': dict(Counter(row['verdict'] for row in rows)),
                  'claims': len(claims), 'bundle_entries': len(bundle['entries']),
                  'bundle_relations': len(bundle['relations']), 'draft_equals_staged': True,
                  'packet_encoding_check': 'passed', 'bundle_ingested': False}, indent=2))
