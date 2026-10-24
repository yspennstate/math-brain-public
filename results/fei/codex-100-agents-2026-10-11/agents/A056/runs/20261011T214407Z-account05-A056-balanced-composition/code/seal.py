from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
r=Path(__file__).resolve().parents[1]
files=[]
for p in sorted(r.rglob('*')):
    if p.is_file() and p.name!='receipts.json' and '__pycache__' not in p.parts:
        b=p.read_bytes()
        assert len(b)<20_000_000
        files.append({'path':str(p.relative_to(r)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(r/'out/receipts.json').write_text(json.dumps({'saved_at_utc':datetime.now(timezone.utc).isoformat(),'local_only':True,'files':files},indent=2)+'\n',encoding='utf-8')
print('Final local receipts:',len(files),'files; every file below 20 MB')
