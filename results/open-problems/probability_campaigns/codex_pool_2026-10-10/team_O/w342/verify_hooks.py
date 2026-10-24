import json
from pathlib import Path
import re

root=Path(__file__).resolve().parent
rows=[json.loads(s) for s in (root/'hooks/math-w342.jsonl').read_text(encoding='utf-8').splitlines() if s]
for row in rows:
    assert len(row['text'])<=300
    cue=re.compile(row['cue'])
    assert cue.search(row['fire_when']),row['id']
    assert not cue.search(row['silent_when']),row['id']
receipt={'command':'python -X utf8 verify_hooks.py','proposals':len(rows),'fire_controls_passed':len(rows),'silent_controls_passed':len(rows),'live_activated':0}
(root/'hook_measurements.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
