from pathlib import Path
from fractions import Fraction as Q
import json,time
RUN=Path(__file__).resolve().parents[1]; start=time.monotonic(); checks=0; rows=[]
def need(x):
 global checks
 checks+=1
 assert x
def W(v):
 a=list(v); k=1
 while k<len(a):
  for j in range(0,len(a),2*k):
   for i in range(j,j+k):a[i],a[i+k]=a[i]+a[i+k],a[i]-a[i+k]
  k*=2
 return a
for m in (2,4,6,8):
 M=1<<m; delta=Q(1,M)
 g=[1-2*(sum(((x>>i)&1)*((x>>(i+1))&1) for i in range(0,m,2))%2) for x in range(M)]
 h=g.copy();h[0]*=-1; a=g.copy();a[0]-=1
 wg,wh,wa=W(g),W(h),W(a)
 need(all(w*w==M for w in wg));need(sum(wg)==M)
 need(all(x in (-1,1) for x in g+h))
 norm=Q(sum(x*x for x in a),M); need(norm==1-delta)
 pa=[Q(x*x,M*M)/norm for x in wa]
 chisq=sum((p-delta)**2/delta for p in pa)
 need(chisq==Q(4,M-1))
 infg=Q(sum(g[x]!=g[x^(1<<i)] for x in range(M) for i in range(m)),M)
 infh=Q(sum(h[x]!=h[x^(1<<i)] for x in range(M) for i in range(m)),M)
 need(infg==Q(m,2));need(infh==Q(m,2)+2*m*delta)
 F=g+h; wf=W(F)
 influence=Q(sum(i.bit_count()*x*x for i,x in enumerate(wf)),4*M*M)
 need(influence==Q(m,2)+(m+1)*delta)
 rows.append({'m':m,'chi_square':str(chisq),'influence':str(influence),'selector_influence':str(delta)})
out={'status':'PASS','checks':checks,'rows':rows,'runtime_seconds':time.monotonic()-start,'scope':'finite exact identities supporting the analytic all-C no-go; no new universal FEI conclusion'}
(RUN/'out'/'review_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
