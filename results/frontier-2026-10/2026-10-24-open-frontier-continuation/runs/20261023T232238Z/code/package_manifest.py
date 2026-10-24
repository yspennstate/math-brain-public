from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
excluded = {'MANIFEST.json', 'VERIFIED_READBACK.json', 'COORDINATOR_HANDOFF.json'}
files=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name not in excluded and '__pycache__' not in p.parts:
        data=p.read_bytes()
        data.decode('utf-8')
        files.append({'path':str(p.relative_to(root)), 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest()})
manifest={'run':root.name,'files':files,'excluded_supplements':sorted(excluded), 'all_utf8':True}
(root/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'files_without_manifest':len(files),'bytes':sum(x['bytes'] for x in files)}))
