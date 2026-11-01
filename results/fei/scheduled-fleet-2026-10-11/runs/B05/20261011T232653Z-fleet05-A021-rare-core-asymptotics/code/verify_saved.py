import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())
p=json.loads((root/'PROGRESS.json').read_text());assert p==json.loads((root/'PACKET_DELTA.json').read_text())
assert set(p)=={x.split(' (',1)[0] for x in protocol['required_per_run']['progress_fields']}
for claim in json.loads((root/'CLAIMS.json').read_text()):
    assert set(claim)==set(protocol['required_per_run']['claim_fields'])
    h=hashlib.sha256(json.dumps({'statement':claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert h==claim['statement_sha256']
report=(root/'REPORT.md').read_text(encoding='utf-8')
for heading in protocol['required_per_run']['report_fields']:assert '## '+heading in report
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
receipt=[]
for file in sorted(root.rglob('*')):
    if file.is_file() and file.name!='artifact_receipt.json':
        data=file.read_bytes();assert len(data)<20_000_000
        receipt.append({'path':str(file.relative_to(root)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(root/'out'/'artifact_receipt.json').write_text(json.dumps({'saved_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'local only; no independent acceptance or mirrors claimed','schemas_checked':True,'artifacts':receipt},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'artifacts':len(receipt),'schemas_and_hashes':'PASS','final_universal_bridge':'PASS'},indent=2))
