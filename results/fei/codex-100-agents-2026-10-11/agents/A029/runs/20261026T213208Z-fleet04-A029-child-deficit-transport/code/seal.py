from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1]
p=r/'out/PERSISTENCE.json';o=json.loads(p.read_text(encoding='utf-8'));files=[]
for f in sorted(r.rglob('*')):
 if f.is_file() and f!=p:
  b=f.read_bytes();assert len(b)<20*1024*1024;files.append({'path':str(f.relative_to(r)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
o['files']=files;o['administrative_checklist']='ENTRY_MISSING; see out/CHECKLIST_RECEIPT.json'
p.write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
report=(r/'REPORT.md').read_text(encoding='utf-8');assert report.rstrip().endswith('another isolated floor or reset example.')
status=(r.parents[1]/'STATUS.md').read_text(encoding='utf-8');assert len(status.splitlines())==2
print(status);print(report[report.rfind('## Universal bridge'):]);print('SEALED',len(files),'files; source hashes and local schemas checked; FEI OPEN')
