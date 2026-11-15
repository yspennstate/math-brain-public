"""Check final artifact constraints and source integrity, not the mathematical theorem."""
from pathlib import Path
import hashlib,json,os,re,datetime
root=Path(__file__).resolve().parents[1]
report=(root/'REPORT.md').read_text()
records=[json.loads(l) for l in (root/'data/sources.jsonl').read_text().splitlines()]
checks=[]
for rec in records:
    p=root/'sources'/(rec['name']+'.txt')
    raw=p.read_bytes();body=raw.decode()
    checks.append(dict(name=rec['name'],hash_ok=hashlib.sha256(raw).hexdigest()==rec['text_sha256'],pages_ok=len(re.findall(r'^===== PDF PAGE \d+ =====$',body,re.M))==rec['pages']))
forbidden=[]
for p in root.rglob('*'):
    if not p.is_file(): continue
    if p.suffix.lower() in {'.pdf','.png','.jpg','.jpeg','.gif','.webp','.tiff','.bmp','.svg','.heic'}:forbidden.append(str(p.relative_to(root)))
    elif p.open('rb').read(5)==b'%PDF-':forbidden.append(str(p.relative_to(root)))
result=dict(at=datetime.datetime.now().astimezone().isoformat(),status_line=report.splitlines()[0],sources=checks,forbidden=forbidden,all_source_files_plain_text=all(p.suffix=='.txt' for p in (root/'sources').iterdir() if p.is_file()),display_math_balanced=len(re.findall(r'^\\\[$',report,re.M))==len(re.findall(r'^\\\]$',report,re.M)),priority=os.getpriority(os.PRIO_PROCESS,0),report_sha256=hashlib.sha256(report.encode()).hexdigest())
result['passed']=all(c['hash_ok'] and c['pages_ok'] for c in checks) and not forbidden and result['all_source_files_plain_text'] and result['display_math_balanced'] and result['status_line'] in {'ACCEPT','MINOR','MAJOR','WRONG'} and result['priority']==10
(root/'data/audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='sources'}))
assert result['passed']
