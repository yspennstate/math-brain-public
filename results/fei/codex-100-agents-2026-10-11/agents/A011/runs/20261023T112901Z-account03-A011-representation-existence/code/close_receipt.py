from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];A=R.parents[1]
receipt=json.loads((R/'out/ARTIFACT_RECEIPTS.json').read_text(encoding='utf-8'))
report=R/'REPORT.md';text=report.read_text(encoding='utf-8')
assert 'Checklist entry T-20261023-380 closed' not in text
report.write_text(text.rstrip()+' Checklist entry T-20261023-380 closed for this completed local stage; universal research remains open.\n',encoding='utf-8',newline='')
status=A/'STATUS.md';lines=status.read_text(encoding='utf-8').splitlines();assert len(lines)==2
lines[1]='NEXT: A086/A094 reconstruct v4; replace fixed-ambient positive-sum admission (parity obstruction) by cancellation-aware whole-set supplier.'
status.write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='')
log=A/'WORKLOG.md'
with log.open('a',encoding='utf-8',newline='') as f:f.write('\nChecklist T-20261023-380 closed by the dated task command (exit0); NEXT remains v4 independent reconstruction and cancellation-aware whole-set admission.\n')
closure=R/'out/CHECKLIST_CLOSURE.json';closure.write_text(json.dumps({'entry_id':'T-20261023-380','action':'done','command_exit_code':0,'scope':'Completed local A011 stage; full FEI, independent v4 review and remote mirror remain open.'},indent=2)+'\n',encoding='utf-8',newline='')
changed=[report,status,log,Path(__file__).resolve(),closure]
for q in changed:
 rel=str(q.relative_to(R)) if q.is_relative_to(R) else str(q)
 item={'path':rel,'bytes':q.stat().st_size,'sha256':hashlib.sha256(q.read_bytes()).hexdigest()}
 found=False
 for i,old in enumerate(receipt['files']):
  if old['path']==rel:receipt['files'][i]=item;found=True;break
 if not found:receipt['files'].append(item)
(R/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='')
print('checklist closure receipt and NEXT saved; local artifact hashes refreshed')
