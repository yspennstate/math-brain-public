"""Reconstruct the recorded worst row and actually reject a false bound."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
import json,hashlib
H=Path(__file__).resolve().parent;stem='T170_THREE_COMPRESSED_d14_C256'
r=json.loads((H/(stem+'_PYTHON_RECEIPT.json')).read_bytes());v=json.loads((H/(stem+'_BASE.json')).read_bytes());C=v['cap'];S=v['scale'];A0=v['alpha0_units'];base=v['base_bias'];target=r['worst_base'][0]
sigma=[0]*(C+1);f=0
for n in range(1,C+1):f+=(n-1).bit_count();sigma[n]=26*n-2*f
prev=[0]*(C*C);cur=[0]*(C*C)
for a in range(C,target-1,-1):
 for b in range(C,0,-1):
  for c in range(C,0,-1):
   k=(b-1)*C+c-1
   if c==1:cur[k]=base[(a-1)*C+b-1];continue
   ra=sigma[a] if a<C else 0;rb=sigma[b]+max(a-b,0) if b<C else 0;rc=sigma[c]+max(b-c,0) if c<C else 0
   numerator=S+c*(base[k]-A0)
   if ra:numerator+=ra*prev[k]
   if rb:numerator+=rb*cur[k+C]
   if rc:numerator+=rc*cur[k+1]
   cur[k]=-((-numerator)//(ra+rb+rc+c))
 if a==target:break
 prev,cur=cur,prev
b=1;h=base[(target-1)*C];terms=[(sigma[target],base[target*C]),(sigma[1]+target-1,base[(target-1)*C+1]),(sigma[1],cur[1]),(1,base[0])]
actual_required=S+sum(rate*(child-h) for rate,child in terms)
assert actual_required==r['maximum_base_requirement_units']
wrong=actual_required-1
actual_violation=S+sum(rate*child for rate,child in terms)-sum(rate for rate,_ in terms)*h-wrong
assert actual_violation>0
receipt={'at':datetime.now().astimezone().isoformat(),'status':'PASS actual reconstructed row refuses false alpha','state':[target,1,1],'h_units':h,'rate_child_h_units':terms,'wrong_alpha':str(F(wrong,S)),'actual_violation_units':actual_violation,'minimum_required_units':actual_required,'full_replay_receipt_sha256':hashlib.sha256((H/(stem+'_PYTHON_RECEIPT.json')).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Supplements original full replay: its fault boolean used only a scalar inequality; this check recomputes an actual transition row from the compressed construction. Full replay mathematics and original bytes preserved.'}
p=H/'T170_THREE_ACTUAL_FAULT_RECEIPT.json';p.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt))
