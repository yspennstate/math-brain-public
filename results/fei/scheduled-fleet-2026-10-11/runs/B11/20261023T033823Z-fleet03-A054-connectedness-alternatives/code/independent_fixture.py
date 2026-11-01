from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];count=0;t=time.perf_counter()
def ck(x):
 global count
 assert x;count+=1
def coeff(f):
 N=len(f)
 return [sum(y*(-1 if (s&x).bit_count()%2 else 1) for x,y in enumerate(f)) for s in range(N)]
rows=[]
for k in [0,2,3,4]:
 n=k+4;N=1<<n;q=F(1,1<<k)
 original=[];reset=[];labels=[]
 for x in range(N):
  a,b,c,d=[(x>>j)&1 for j in range(4)];active=(x>>4)==0
  v=(-1 if active and (a*b+c*d)%2==0 else 1)
  ar=a^c;vnew=(-1 if active and (ar*b+c*d)%2==0 else 1)
  original.append(v);reset.append(vnew)
  labels.append((-1 if not active or vnew==1 else int(ar*b==1)))
 ck(sorted(abs(z) for z in coeff(original))==sorted(abs(z) for z in coeff(reset)))
 costs=[]
 for v in range(1,N):
  cost=F(sum(reset[x]!=reset[x^v] for x in range(N)),N);costs.append(cost)
  ck(cost==(F(5,4)*q if v>>4 else q/2))
  ck(cost<=F(1,2))
  ck(cost>=max((F(5,4)*q if j>=4 else q/2) for j in range(n) if v>>j&1))
 gam=F(sum(labels[x]>=0 and labels[x^4]>=0 and labels[x]!=labels[x^4] for x in range(N)),N)
 ck(gam==q/8);ck(F(sum(x==-1 for x in original),N)==5*q/8)
 ck([x for x in range(N) if labels[x]>=0 and labels[x^4]>=0 and labels[x]!=labels[x^4]]==[10,14])
 rows.append({'k':k,'gamma_c':str(gam),'parities':N-1,'rho':0})
out={'status':'PASS','assertions':count,'seconds':time.perf_counter()-t,'fixtures':rows,'method':'independent direct character sums, explicit labels and all physical translations; no imported checker helper'}
(R/'out/INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
