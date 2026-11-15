"""Insert generated numerical tables and hash the finished research artifacts."""
import hashlib
import json
from pathlib import Path

report=Path('REPORT.md')
text=report.read_text()
marker='<!-- NUMERICAL_TABLE -->'
if marker in text:
    text=text.replace(marker,Path('data/tables.md').read_text().rstrip())
    report.write_text(text)
assert text.splitlines()[0]=='COUNTEREXAMPLE'
assert marker not in text
for name in ('REPORT.md','LOG.md','requirements.txt','BRAIN_NOTE.md'):
    assert Path(name).is_file()
assert len(json.loads(Path('data/m3_vertices.json').read_text())['vertices'])==222
artifacts=[Path(x) for x in ('REPORT.md','LOG.md','BRAIN_NOTE.md','requirements.txt')]
for folder in ('code','data','sources'):
    artifacts.extend(p for p in Path(folder).rglob('*') if p.is_file()
                     and '__pycache__' not in str(p)
                     and p.name!='manifest.json')
manifest={str(p):dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
          for p in sorted(artifacts)}
Path('data/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Finalised {len(manifest)} research artifacts; report first line COUNTEREXAMPLE.')
