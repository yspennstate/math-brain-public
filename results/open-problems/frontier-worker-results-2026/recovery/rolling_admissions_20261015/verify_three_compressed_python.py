from pathlib import Path
from datetime import datetime
from fractions import Fraction as F
import json,hashlib,time,sys
H=Path(__file__).resolve().parent;C=int(sys.argv[1]);stem=f'T170_THREE_COMPRESSED_d14_C{C}'
r=json.loads((H/(stem+'_RECEIPT.json')).read_bytes());v=json.loads((H/(stem+'_BASE.json')).read_bytes());S=v['scale'];A0=v['alpha0_units'];base=v['base_bias'];assert len(base)==C*C and S==2**40
for name,h in r['files_sha256'].items():assert hashlib.sha256((H/name).read_bytes()).hexdigest()==h,name
t=time.monotonic();sigma=[];edges=0
for n in range(C+1):
 if n:edges+=sum(((n-1)^(1<<j))<n-1 for j in range(14))
 sigma.append(26*n-2*edges)
prev=[0]*(C*C);cur=[0]*(C*C);A=A0;minimum=None;numstates=0;maxbase=-10**100;worst=None
for a in range(C,0,-1):
 ra=sigma[a] if a<C else 0
 for b in range(C,0,-1):
  rb=sigma[b]+max(a-b,0) if b<C else 0
  for c in range(C,0,-1):
   k=(b-1)*C+c-1;rc=sigma[c]+max(b-c,0) if c<C else 0;total=ra+rb+rc+c
   # Child values absent at caps have zero rates; no stale slice is read.
   u=prev[k] if ra else 0;w=cur[k+C] if rb else 0;z=cur[k+1] if rc else 0;drop=base[k]
   if c==1:
    h=base[(a-1)*C+b-1];needed=S+ra*(u-h)+rb*(w-h)+rc*(z-h)+drop-h
    if needed>maxbase:maxbase=needed;worst=[a,b,1]
    A=max(A,needed)
   else:
    numerator=S+ra*u+rb*w+rc*z+c*(drop-A0)
    h=-((-numerator)//total)
    slack=total*h-numerator;assert 0<=slack<total
    minimum=slack if minimum is None else min(minimum,slack)
   assert -S<=h<=S
   cur[k]=h;numstates+=1
 prev,cur=cur,prev
assert A==r['alpha_units'] and A>=A0 and numstates==C**3
assert maxbase>0
# An actual base inequality fails below its recomputed requirement, even if
# this certificate deliberately retained surplus from alpha0.
assert (maxbase-1)-maxbase<0
receipt={'at':datetime.now().astimezone().isoformat(),'status':'PASS independent unbounded integer constructive replay; no physical admission','cap':C,'states':numstates,'axis':str(F(A,S)),'alpha0_units':A0,'alpha_units':A,'maximum_base_requirement_units':maxbase,'worst_base':worst,'minimum_interior_slack':minimum,'seconds':time.monotonic()-t,'base_sha256':hashlib.sha256((H/(stem+'_BASE.json')).read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'lowered_base_fault_rejected':True}
(H/(stem+'_PYTHON_RECEIPT.json')).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt))
