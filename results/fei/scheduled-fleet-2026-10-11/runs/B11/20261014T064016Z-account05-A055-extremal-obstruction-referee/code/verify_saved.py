from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1];m=json.loads((r/'out/ARTIFACT_MANIFEST.json').read_text(encoding='utf-8'))
assert all(hashlib.sha256((r/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in m['files'])
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
assert all((r/x['path']).stat().st_size<20*1024*1024 for x in m['files'])
print('PASS:',len(m['files']),'persisted hashes, compatibility bytes, size cap')
