from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();N=0
def ck(x,msg):
 global N
 assert x,msg
 N+=1
 assert time.perf_counter()-start<60,'frozen runtime'
data=json.loads((R/'out/BLOCK_CHECK.json').read_text(encoding='utf-8'))['rows'];states={}
for x in data:states[json.dumps([x['essential'],x['values']])]=x
profiles=0
for row in states.values():
 G=row['values'];s=(len(G)-1).bit_length()
 ig=[F(sum(G[x]!=G[x^(1<<i)] for x in range(len(G))),len(G)) for i in range(s)]
 for kp in [0,1]:
  rho=F(1,1<<kp)
  for phase in [-1,1]:
   nu=phase*F(sum(G),len(G));a=rho*(1-nu)/2
   for qsign in [-1,1]:
    n=1+kp+s+3;vals=[]
    for x in range(1<<n):
     u=1-2*(x&1);pad=(x>>1)&((1<<kp)-1);g=phase*G[(x>>(1+kp))&((1<<s)-1)]
     h=qsign if pad==0 and g==-1 else u
     w=-1 if ((x>>(1+kp+s))&3)==0 else 1
     vals.append(h*w if (x>>(n-1))&1 else 1)
    for i in range(s):
     actual=F(4*sum(vals[x]!=vals[x^(1<<(1+kp+i))] for x in range(len(vals))),len(vals))
     ck(actual==rho*ig[i] and actual<=rho,'literal four-influence source cap, actual shared bits')
    for i in range(kp):
     actual=F(4*sum(vals[x]!=vals[x^(1<<(1+i))] for x in range(len(vals))),len(vals))
     ck(actual==2*a,'literal padding influence, not fresh source credit')
    profiles+=1
for k in [5,6,8,16,32,64,128,256]:
 for r in [0,1,9]:
  cap=F(2*k+r,1<<k);ck(cap<=F(10+r,32),'all-k decreasing occupation cap endpoint')
  if r==9:ck(F(5,8)-cap>=F(1,32),'nine genuinely mixed source queries leave original reserve')
ck(all(F(2*(k+1)+9,2)<2*k+9 for k in [5,6,8,16]),'symbolic monotonicity coefficient')
result={'status':'PASS','profiles':profiles,'assertions':N,'seconds':time.perf_counter()-start,'scope':'direct physical source/padding caps; finite-partition proof gives arbitrary adaptive query selection and at most9 nonzero source queries after admission'}
(R/'out/MIXED_CAP_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
