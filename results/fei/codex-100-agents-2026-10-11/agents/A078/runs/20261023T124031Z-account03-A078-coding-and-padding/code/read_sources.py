from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];O=R/'out'
A=Path('agents/A076/runs/20261023T114019Z-account03-A076-threshold-and-tribes-controls')
claims=json.loads((A/'CLAIMS.json').read_text(encoding='utf-8'))
print('SOURCE_CLAIMS',[(c['claim_id'],c['version']) for c in claims])
context=Path('context')
papers=sorted(context.glob('*threshold*38pp*.txt'))
receipt=[]
for p in papers:
 raw=p.read_bytes();encoding='utf-8'
 try:s=raw.decode(encoding)
 except UnicodeDecodeError:
  encoding='cp1252';s=raw.decode(encoding)
 lines=s.splitlines();selected=[]
 for j,l in enumerate(lines[:300]):
  if 'Theorem A' in l or 'Creg' in l or 'C_reg' in l or 'regular' in l.lower() or '8.937' in l:
   selected.extend(lines[max(0,j-1):min(len(lines),j+3)])
 receipt.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'source_encoding_used':encoding,'source_not_modified':True,'header_locators':selected[:45]})
 print('PAPER',p.name,'\n'+'\n'.join(selected[:45]))
(O/'THRESHOLD_DEPENDENCY_READBACK.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8',newline='\n')
