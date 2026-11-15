"""Standalone exact check: no numpy/scipy, solver imports or stationary data."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime
import hashlib,json,sys
H=Path(__file__).resolve().parent
out=[]
for cap in [2,128,512]:
 p=H/f'T170_EMBEDDED_d15_C{cap}_BIAS.json';raw=p.read_bytes();v=json.loads(raw)
 r=json.loads((H/f'T170_EMBEDDED_d15_C{cap}_RECEIPT.json').read_bytes())
 assert hashlib.sha256(raw).hexdigest()==r['bias_sha256']
 assert v['dimension']==15 and v['cap']==cap
 z=v['bias'];scale=v['scale'];a=F(v['axis_upper_conditional']);assert len(z)==cap**2 and scale==2**40
 # Count actual edges of the initial segment in Q14 rather than calling popcount.
 edges=[0]*(cap+1)
 for n in range(1,cap+1):
  j=n-1;edges[n]=edges[n-1]+sum((j^(1<<bit))<j for bit in range(14))
 least=None;witness=None
 for x in range(1,cap+1):
  for y in range(1,cap+1):
   k=(x-1)*cap+y-1
   terms=[(y,(y-1)*cap)]
   if x<cap:terms.append((28*x-2*edges[x],x*cap+y-1))
   if y<cap:terms.append((28*y-2*edges[y]+max(x-y,0),(x-1)*cap+y))
   generator=sum(rate*(z[child]-z[k]) for rate,child in terms)
   # Clear both the bias scale and the certificate denominator exactly.
   slack=a.numerator*y*scale-a.denominator*(scale+generator)
   assert slack>=0,(cap,x,y,slack)
   if least is None or slack<least:least=slack;witness=(x,y,generator)
 assert least==0,'Tight maximum row must be present'
 x,y,g=witness
 wrong=a-F(1,2**50)
 assert wrong*y*scale-(scale+g)<0,'Strictly lowered certificate must fail'
 if cap==2:
  assert 0<=a-F(883,1709)<F(1,10**8),'Independent closed-form cycle control'
 out.append({'cap':cap,'states':cap**2,'axis':str(a),'minimum_cleared_slack':least,'lowered_bound_fault_rejected':True,'bias_sha256':hashlib.sha256(raw).hexdigest()})
receipt={'at':datetime.now().astimezone().isoformat(),'status':'PASS standalone exact finite-generator check only; no physical FPP admission','cases':out,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(H/'T170_ROLLING_INDEPENDENT_BIAS_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
