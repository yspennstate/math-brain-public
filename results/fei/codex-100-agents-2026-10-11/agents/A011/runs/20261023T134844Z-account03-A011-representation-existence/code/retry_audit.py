from pathlib import Path
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1]
failure={'scope':'Administrative artifact audit only, not mathematical validation','error':'Assertion expected the literal phrase positive-part-only, whereas REPORT explicitly says does not bound the sum of positive resets alone.','repair':'Check the actual explicit scope sentence; no theorem, model, constants, mathematical cases or source assumptions changed.','checklist':'Reuse the already written CHECKLIST_CLOSURE.json; do not repeat its done action.'}
(R/'out/AUDIT_INITIAL_FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n',encoding='utf-8',newline='')
receiptpath=R/'out/ARTIFACT_RECEIPTS.json';receipt=json.loads(receiptpath.read_text(encoding='utf-8'))
for row in receipt['files']:
 q=Path(row['path']);q=q if q.is_absolute() else R/q;digest=hashlib.sha256(q.read_bytes()).hexdigest()
 if q==(R/'code/audit.py'):row['bytes']=q.stat().st_size;row['sha256']=digest
 else:assert q.stat().st_size==row['bytes'] and digest==row['sha256'],str(q)
receiptpath.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='')
subprocess.run(['python','-X','utf8',str(R/'code/audit.py')],check=True,timeout=60)
