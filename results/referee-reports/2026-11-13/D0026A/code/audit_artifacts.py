#!/usr/bin/env python3
import csv,hashlib,json,math
from pathlib import Path
r=Path('REPORT.md').read_text();assert r.splitlines()[0]=='PARTIAL';assert 'Work in progress' not in r
for p in Path('.').rglob('*'):
 if p.is_file():assert p.suffix.lower() not in ('.pdf','.png','.jpg','.jpeg','.webp','.tif','.tiff'),str(p)
for p in Path('sources').glob('*'):
 if p.is_file():
  raw=p.read_bytes();assert not raw.startswith(b'%PDF');raw.decode('utf8');assert b'\x00' not in raw,str(p)
summary=list(csv.DictReader(open('data/summary.csv')));assert len(summary)==8
maxz=max(abs(float(row[k+'_z'])) for row in summary for k in ['infect0','infect01','healthy3']);assert maxz<2.10
v=json.load(open('data/verification.json'));assert len(v['checks'])==36
assert all(math.isfinite(c['exact']) for c in v['checks']);assert v['expm_uniformization_max']<1e-13
runs=json.load(open('data/runs.json'));assert len(runs)==8
for x in runs:assert 'nice=10' in x['stdout'] and 'reps=2000' in x['stdout']
paths=[Path('REPORT.md'),Path('LOG.md')]+[p for root in ['sources','code','data'] for p in Path(root).glob('*') if p.is_file() and p.name!='artifact_audit.json']
artifacts={str(p):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths}
Path('data/artifact_audit.json').write_text(json.dumps({'status':'passed','main_paths':16000,'main_events':sum(int(x['stdout'].split('events=')[1].split()[0]) for x in runs),'final_max_abs_z':maxz,'artifacts':artifacts},indent=2)+'\n')
print('audit passed:',len(artifacts),'artifacts; 16000 paths; final max |z|',maxz)
