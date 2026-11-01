from pathlib import Path
from fractions import Fraction as R
from math import log2
import json,time
RUN=Path(__file__).resolve().parents[1];start=time.monotonic()
rows=[]
for m in range(1,13):
 N=1<<m;rho=R(1,N);t=rho*rho
 for d in (0,1):
  A=(1+3*t*d)/4;B=5*(1-t*d)/16;r=7*(1-t*d)/R(32*(N-1))
  P0,P1=((1-rho)**2,t) if d==0 else (t,(1-rho)**2)
  delta=float(P0)*log2(1+float(r/A))+float(P1)*log2(1+float(r/B))+float(t)*log2(float((1+A/r)*(1+B/r)))+float(2*(N-2)*t)
  row={'m':m,'d':d,'first_excess':delta-float(4*rho),'second':[]}
  if m>=2:
   for z in (0,1):
    a,b,s=A+r,B+r,2*r
    if z==1:p0,p1=(R(1),R(0)) if d==0 else (R(0),R(1));tail=R(0);inf=R(0)
    else:
     rho2=2*rho;p0,p1=((1-rho2)**2,rho2*rho2) if d==0 else (rho2*rho2,(1-rho2)**2)
     tail=rho2*rho2;inf=rho2
    price=float(p0)*log2(1+float(s/a))+float(p1)*log2(1+float(s/b))+float(tail)*log2(float((1+a/s)*(1+b/s)))+float(2*((N//2)-2)*tail)
    row['second'].append({'z':z,'excess':price-float(4*inf)})
  rows.append(row)
  assert time.monotonic()-start<55
out={'status':'DISCOVERY_ONLY','rows':rows,'elapsed_seconds':time.monotonic()-start}
(RUN/'out/PILOT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
