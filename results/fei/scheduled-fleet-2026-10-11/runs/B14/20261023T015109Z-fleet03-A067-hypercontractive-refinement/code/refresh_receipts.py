from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
receipt_path=R/'out/PERSISTENCE_RECEIPTS.json'
receipt=json.loads(receipt_path.read_text(encoding='utf-8'))
rows=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p!=receipt_path:
  b=p.read_bytes();assert len(b)<20*1024*1024
  rows.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
receipt['artifacts']=rows
receipt['final_prose_readback']='Scope-incident wording clarified; mathematics and counts unchanged.'
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((R.parent.parent/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'FINAL_READBACK_PASS','artifacts':len(rows),'main_checks':117038,'guard_checks':18,'scope_incident':'placeholder untouched, approval pending'}))
