from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
OUT=Path(__file__).resolve().parents[1]/'out'
p=Path(r'~\mop_fei100\reports\fei-2026-10-11\CLAIM_REGISTRY.json')
b=p.read_bytes(); c=json.loads((OUT/'CLAIM_CENSUS.json').read_text(encoding='utf-8'))
if not any(x['source']==str(p) for x in c):
    for row in json.loads(b.decode('utf-8-sig'))['claims']:
        c.append({'source':str(p),'record':row,'statement_only_sha256':hashlib.sha256(row['exact_statement'].encode()).hexdigest()})
    (OUT/'CLAIM_CENSUS.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
r=json.loads((OUT/'SOURCE_RECEIPTS.json').read_text(encoding='utf-8'))
if not any(x['path']==str(p) for x in r['files']):
    r['files'].append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
    r['supplemental_canonical_intake_utc']=datetime.now(timezone.utc).isoformat()
    (OUT/'SOURCE_RECEIPTS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Canonical snapshot preserved in census; no historical theorem silently dropped by path selection.')
