"""Check exact published component bytes against the compilation record."""
from pathlib import Path
import hashlib, json, re
root=Path(__file__).resolve().parents[1]
receipt=json.loads((root/'verification/component_runs.json').read_text(encoding='utf-8'))
for run in receipt['runs']:
    p=root/run['source']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==run['source_sha256'], p.name
    text=p.read_text(encoding='utf-8')
    assert not re.search(r'^\s*(axiom|sorry|admit)\b',text,re.M), p.name
    assert run['returncode']==0
    print(p.name, 'source hash matches successful component run;', run['declarations'], 'declarations')
print('Source correspondence passed. This check does not invoke the Lean compiler.')
