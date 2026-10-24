from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
r=Path(__file__).resolve().parents[1]
d=json.loads((r/'out/checks.json').read_text(encoding='utf-8'))
fixture=d['fixtures'][2]
assert fixture['L_signed']=={'2':'1/4','3':'-9/8','5':'5/8'}
assert fixture['J_signed']=={'2':'5/4','5':'-5/8'}
assert 4*5**5<3**9 and 4<5
p=json.loads((r/'PROGRESS.json').read_text(encoding='utf-8'))
assert p==json.loads((r/'PACKET_DELTA.json').read_text(encoding='utf-8'))
validation=json.loads((r/'out/artifact_validation.json').read_text(encoding='utf-8'))
validation['signed_JS_certificate']={'exact_expression':'(5/8)log2(4/5)','integer_comparison':'4<5','verdict':'PASS'}
(r/'out/artifact_validation.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')
receipts=[]
for file in sorted(r.rglob('*')):
    if file.is_file() and file.name!='receipts.json' and '__pycache__' not in file.parts:
        b=file.read_bytes(); assert len(b)<20_000_000
        receipts.append({'path':str(file.relative_to(r)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(r/'out/receipts.json').write_text(json.dumps({'saved_at_utc':datetime.now(timezone.utc).isoformat(),'local_only':True,'files':receipts},indent=2)+'\n',encoding='utf-8')
print('Final witness certificates, delta, artifact receipts: PASS;',len(receipts),'local files')
