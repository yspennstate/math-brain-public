from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]; A=R.parent.parent
O=R/'out'; O.mkdir(exist_ok=True)
prev=A/'runs/20261023T134050Z-fleet03-A100-release-and-continuation-ledger'
for name in ['intake.py','ledger.py','exact.py']:
 s=(prev/'code'/name).read_text(encoding='utf-8')
 if name=='intake.py':
  s=s.replace("20261023T112759Z-fleet03-A100-release-and-continuation-ledger",prev.name)
 if name=='ledger.py':
  s=s.replace("20261023T112759Z-fleet03-A100-release-and-continuation-ledger",prev.name)
  s=s.replace("A097-NECESSARY-FLOOR-ADMISSION-SAME-ORIGINAL-OWNER",'A094-A011-V5-PHYSICAL-QUERY-KL-LEDGER-GAP')
 (R/'code'/name).write_text(s,encoding='utf-8',newline='\n')
(A/'STATUS.md').write_text('STATE: A100 stage21 active: checking A094 physical-query KL accounting objection to A011v5; full FEI OPEN.\nNEXT: Reconstruct actual normalizers and full signed-tree identity; propagate exact scoped objection and refresh release ledger.\n',encoding='utf-8')
p=Path(r'agents\A094\runs\20261026T232939Z-fleet04-A094-proof-chain-challenger')
files=[p/'CLAIMS.json',p/'DERIVATION.md',Path(r'agents\A011\runs\20261023T134844Z-fleet03-A011-representation-existence\DERIVATION.md'),Path(r'agents\A011\runs\20261023T134844Z-fleet03-A011-representation-existence\CLAIMS.json')]
receipts=[{'path':str(f),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in files]
(O/'REVIEW_SOURCE_RECEIPTS.json').write_text(json.dumps({'files':receipts},indent=2)+'\n',encoding='utf-8')
print('Saved active status, source receipts, and own helper copies; no search executed.')
