from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=r/'out/ARTIFACT_MANIFEST.json'
m=json.loads(p.read_text(encoding='utf-8'))
assert all(sha(r/x['path'])==x['sha256'] for x in m['files'])
files=[f for f in r.rglob('*') if f.is_file() and f!=p]
m['files']=[{'path':str(f.relative_to(r)),'bytes':f.stat().st_size,'sha256':sha(f)} for f in files]
m['file_count']=len(files)
m['persisted_hashes_rechecked']=True
p.write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
assert all(sha(r/x['path'])==x['sha256'] for x in json.loads(p.read_text())['files'])
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
assert all(f.stat().st_size<20*1024*1024 for f in files)
print('PASS: persisted hashes, compatibility bytes, size cap;',len(files),'artifacts')
