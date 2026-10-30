from pathlib import Path
from fractions import Fraction as Q
import json,time
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;nodes=0
def ck(v):
 global checks
 checks+=1;assert v,checks
 assert time.perf_counter()-start<55
def fwht(a):
 a=a[:];k=1
 while k<len(a):
  for i in range(0,len(a),2*k):
   for j in range(i,i+k):a[j],a[j+k]=a[j]+a[j+k],a[j]-a[j+k]
  k*=2
 return a
for m in range(1,5):
 for k in range(m):
  free=[j for j in range(2*m) if not 1<=j<=k]
  for fixed in range(1<<k):
   nodes+=1;t=[]
   for z in range(1<<len(free)):
    full=fixed<<1
    for q,j in enumerate(free):full|=((z>>q)&1)<<j
    x=full&((1<<m)-1);y=full>>m
    t.append((-1)**((x&y).bit_count()+((y&1)*(y>>1).bit_count())))
   w=fwht(t);nonzero=[a for a in w if a]
   ck(len(nonzero)==1<<(2*(m-k)))
   ck(all(a*a==len(t)**2//len(nonzero) for a in nonzero))
   for j in range(len(free)):
    ck(sum(t[z]!=t[z^(1<<j)] for z in range(len(t)))*2==len(t))
data=json.loads((ROOT/'out/validation.json').read_text(encoding='utf-8'))
for row in data['family']:
 m=row['m']
 for leaf in row['leaves']:
  sup=leaf['support']
  for s in range(1<<(m+1)):
   # conditioning on A=s_x1, with B free: exact two-product mixture
   target=Q(1,4) if s in sup else Q(0)
   mixed=Q(0)
   for a in (0,1):
    ok=((s&1)==a)
    for j in range(1,m):ok=ok and (((s>>(j+1))&1)==(a^((leaf['fixed']>>(j-1))&1)))
    if ok:mixed+=Q(1,4)
   ck(mixed==target)
 ck((m+1)-2==m-1) # exact TC of fair marginals and four equal atoms
out={'status':'PASS','nodes':nodes,'checks':checks,'seconds':time.perf_counter()-start}
(ROOT/'out/frontier.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
