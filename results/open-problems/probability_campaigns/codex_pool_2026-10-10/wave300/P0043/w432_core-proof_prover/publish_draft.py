"""Publish only this worker's own completed DRAFT; never invoke live integration."""
import json
import os
from pathlib import Path

root = Path(__file__).resolve().parent
inbox = Path('~/math-brain-inbox/w432').resolve()
inbox.mkdir(parents=True, exist_ok=True)
source = root / ('bundle_002.json' if (root / 'bundle_002.json').exists() else 'bundle_001.json')
text = source.read_text(encoding='utf-8')
payload = json.loads(text)
assert payload['author_agent'] == 'w432' and all(entry['kind'] == 'concept' for entry in payload['entries'])
for index in range(1, 1000):
    target = inbox / f'bundle_{index:03d}.json'
    part = inbox / f'bundle_{index:03d}.part'
    assert target.parent.resolve() == inbox and part.parent.resolve() == inbox
    if target.exists():
        if target.read_text(encoding='utf-8') == text:
            break
        continue
    if part.exists():
        continue
    with part.open('x', encoding='utf-8', newline='\n') as stream:
        stream.write(text)
        stream.flush()
        os.fsync(stream.fileno())
    os.rename(part, target)
    break
else:
    raise RuntimeError('No unused worker-owned bundle name; nothing overwritten')
states = json.loads((root / 'BUNDLE_STATES.json').read_text(encoding='utf-8'))
states.update({'submitted': True, 'submission_path': str(target), 'reviewed': False, 'ingested': False, 'retrievable': False})
states.setdefault('submission_history', [])
if str(target) not in states['submission_history']:
    states['submission_history'].append(str(target))
(root / 'BUNDLE_STATES.json').write_text(json.dumps(states, indent=2) + '\n', encoding='utf-8')
print(json.dumps(states))
