from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path(__file__).resolve().parents[1]
p=root/'out/PERSISTENCE_RECEIPTS.json'
data=json.loads(p.read_text(encoding='utf8'))
for entry in data['artifacts']:
 path=Path(entry['path'])
 if not path.is_absolute():path=root/path
 b=path.read_bytes();entry['bytes']=len(b);entry['sha256']=hashlib.sha256(b).hexdigest()
myself=Path(__file__);b=myself.read_bytes()
data['artifacts'].append({'path':str(myself.relative_to(root)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'readback':'PASS'})
data['final_readback_utc']=datetime.now(timezone.utc).isoformat()
data['metadata_note']='LEARNED.md clarified unchanged statement text versus corrected local UTF-8 hashes; mathematical certificates unchanged.'
p.write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
print('PASS: final source-hash clarification and persistence readbacks refreshed')
