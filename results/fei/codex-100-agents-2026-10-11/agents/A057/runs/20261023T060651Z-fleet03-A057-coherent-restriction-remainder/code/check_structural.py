from pathlib import Path
from itertools import product
import time,json
start=time.monotonic();checks=slices=amps=0
def ck(b):
 global checks
 assert b;checks+=1
for code in range(16):
 def P(x):
  bits=[x>>i&1 for i in range(3)]
  mon=[bits[0]*bits[1],bits[0]*bits[2],bits[1]*bits[2],bits[0]*bits[1]*bits[2]]
  return sum(v*(code>>j&1) for j,v in enumerate(mon))%2
 vals=[]
 for z in range(64):
  x=sum((z>>(2*j)&1)<<j for j in range(3))
  vals.append((-1)**(sum((z>>(2*j)&1)*(z>>(2*j+1)&1) for j in range(3))+P(x)))
 ck(vals[0]==1)
 for j in range(6):ck(vals[1<<j]==1)
 ck(sum(vals)==8)
 for j in range(3):
  outside=[i for i in range(6) if i not in [2*j,2*j+1]]
  for bits in product([0,1],repeat=4):
   z=sum(v<<i for i,v in zip(outside,bits));sgn=1
   for a,b in product([0,1],repeat=2):sgn*=vals[z+(a<<(2*j))+(b<<(2*j+1))]
   ck(sgn==-1);slices+=1
 for s in range(64):
  w=sum(v*(-1 if (s&z).bit_count()%2 else 1) for z,v in enumerate(vals));ck(abs(w)==8);amps+=1
 ck(time.monotonic()-start<55)
out={'status':'PASS','functions':16,'pair_slices':slices,'direct_Fourier_amplitudes':amps,'exact_assertions':checks,'seconds':time.monotonic()-start,'arithmetic':'integer physical slice signs and independent direct character sums'}
p=Path(__file__).resolve().parents[1]/'out/structural.json';p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
