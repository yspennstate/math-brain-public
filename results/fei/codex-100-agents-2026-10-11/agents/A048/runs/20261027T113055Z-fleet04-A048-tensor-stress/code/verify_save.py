from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
files=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE.json':
        raw=p.read_bytes();assert len(raw)<20_000_000
        files.append(dict(path=str(p.relative_to(R)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
out=dict(run_id=R.name,local_verified=True,mirror_verified=False,files=files)
(R/'out/PERSISTENCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for rec in files:
    assert hashlib.sha256((R/rec['path']).read_bytes()).hexdigest()==rec['sha256']
assert json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))==json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))
print('PASS: independently reread all',len(files),'saved artifacts; hashes and packet copy agree')
