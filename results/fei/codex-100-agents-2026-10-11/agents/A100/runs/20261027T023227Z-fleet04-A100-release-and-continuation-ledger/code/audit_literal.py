from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];checks=0;t=time.perf_counter()
def ck(v):
 global checks
 checks+=1
 assert v
def spec(tab):
 a=tab.copy();d=1
 while d<len(a):
  for k in range(0,len(a),2*d):
   for j in range(k,k+d):u,v=a[j],a[j+d];a[j],a[j+d]=u+v,u-v
  d*=2
 return [F(x*x,len(a)**2) for x in a]
rows=[]
for b in [12,13]:
 N=2**(b+1);e=F(1,N)
 source=[1 if not i&1 else -1 for i in range(N)]
 full=source+source;full[0]=-1
 pp=spec(full);pg=spec(source);pc=spec(source);pe=spec(full[:N])
 marginal=[pp[i]+pp[i+N] for i in range(N)]
 qr=[(x+3*e*e)/(1+3*e) for x in pg]
 zc=sum(q*x/y for q,x,y in zip(qr,pc,marginal))
 ze=sum(q*x/y for q,x,y in zip(qr,pe,marginal))
 ck(zc+ze==2);ck(zc*ze<1)
 ck(zc==(1+3*e*e)/((1+3*e)*(1-2*e+2*e*e)))
 for i in range(N):
  A=1 if i==1 else 0
  ck(pg[i]==A*A);ck(marginal[i]==(A-e)**2+e*e);ck(pe[i]==(A-2*e)**2)
 # Direct-character audit of selected literal parent coefficients.
 for s in [0,1,2,N-1,N,N+1,2*N-1]:
  w=sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(full))
  ck(pp[s]==F(w*w,(2*N)**2))
 rows.append({'b':b,'literal_parent_dimension':b+2,'actual_parent_atoms':2*N,'Z_clean':str(zc),'strict_product_certificate':str(zc*ze)})
 ck(time.perf_counter()-t<55)
out={'status':'PASS','checks':checks,'cases':rows,'seconds':time.perf_counter()-t,'independence':'literal integer FWHT and selected direct characters; no primary or author helper imported','sign':'exact Fraction product<1'}
(R/'out/INDEPENDENT_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
