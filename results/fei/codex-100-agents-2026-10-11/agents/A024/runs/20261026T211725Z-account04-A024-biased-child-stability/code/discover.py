from pathlib import Path
import math,json,time
root=Path(__file__).resolve().parents[1]
start=time.monotonic()
def L(a,b):
 s=a*a+b*b
 return sum(-x*math.log2(x/s) for x in (a*a,b*b) if x) if s else 0.
best=(-1,None);count=0
for j in range(1,33):
 r=j/32
 for k in range(1,33):
  b=k/32
  for l in range(-32+k,33-k):
   a=l/32
   R=L(1-r+r*a,r*b)+r*(1-r)*L(1-a,b)-r*L(a,b)
   val=R/(r*b)
   if val>best[0]:best=(val,(r,a,b,R))
   count+=1
assert time.monotonic()-start<45
out=dict(status='NUMERICAL_EVIDENCE_ONLY',cases=count,maximum=best,runtime_seconds=time.monotonic()-start)
(root/'out').mkdir(exist_ok=True)
(root/'out/DISCOVERY.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
