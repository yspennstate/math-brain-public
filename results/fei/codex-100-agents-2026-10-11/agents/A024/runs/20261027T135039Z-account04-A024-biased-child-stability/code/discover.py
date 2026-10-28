from pathlib import Path
from itertools import combinations
import math,json,time
root=Path(__file__).resolve().parents[1];(root/'out').mkdir(exist_ok=True)
start=time.monotonic()
def L(a,b):
 s=a*a+b*b
 return sum(-x*math.log2(x/s) for x in (a*a,b*b) if x) if s else 0.
def spectrum(v):
 a=list(v);k=1
 while k<len(a):
  for j in range(0,len(a),2*k):
   for i in range(j,j+k):a[i],a[i+k]=a[i]+a[i+k],a[i]-a[i+k]
  k*=2
 return [x/len(v) for x in a]
edits=[(i,) for i in range(8)]+list(combinations(range(8),2));count=0;hits=[];best=(-1,None)
for code in range(256):
 g=[1 if code>>x&1 else -1 for x in range(8)];G=spectrum(g)
 for E in edits:
  h=list(g)
  for x in E:h[x]*=-1
  H=spectrum(h);a=(G[0]+H[0])/2;b=(G[0]-H[0])/2;d=len(E)/8
  B=sum(L((x+y)/2,(x-y)/2) for x,y in zip(G,H))
  for j in range(1,16):
   r=j/16
   R=L(1-r+r*a,r*b)+r*(1-r)*L(1-a,b)-r*L(a,b)
   value=(r*B+R)/(r*d)
   if B<=4*d+1e-12 and value>best[0]:best=(value,dict(code=code,edits=E,r=r,a=a,b=b,d=d,B=B,R=R))
   if B<=4*d-1e-10 and value>4+1e-10:hits.append(dict(code=code,edits=E,r=r,a=a,b=b,d=d,B=B,R=R,lift_ratio=value))
   count+=1
assert time.monotonic()-start<55
out=dict(status='DISCOVERY_ONLY',cases=count,hits=len(hits),first_hits=hits[:8],best=best,runtime_seconds=time.monotonic()-start)
(root/'out/DISCOVERY.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
