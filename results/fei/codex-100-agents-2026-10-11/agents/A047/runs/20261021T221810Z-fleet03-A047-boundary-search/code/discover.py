import math,json,time
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def h(p):return -sum(x*math.log2(x) for x in [p,1-p] if x)
def hp(r):
 if r<=1:return 0.
 d=2.**-r
 return h((1-2*d)**2)+(1-(1-2*d)**2)*math.log2((1<<r)-1)
def calc(m,r):
 d=2.**-r;t=(1-(1-2*d)**m)/2;p0=(1-t)**2/4;v=1-p0
 ds=[.5,.5,t/2]+[d/2]*(m*r)
 lo=1e-12;hi=1.
 for _ in range(65):
  c=(lo+hi)/2
  if 1-c-math.prod(1-c*x/v for x in ds)>0:lo=c
  else:hi=c
 c=(lo+hi)/2;th=[c*x/v for x in ds]
 ce=-p0*math.log2(p0)-v*math.log2(v/c)-sum(x*math.log2(z)+(v-x)*math.log2(1-z) for x,z in zip(ds,th))
 # Core entropy via tensor additivity. Root H is calculated from its exact profile.
 # F has two a-atoms of mass1/4; empty,x of mass(1-t)^2/4;
 # b,xb mass t^2/4; four copies of each nonempty core atom /16.
 mu=(1-2*d)**m;he=m*hp(r);core_nonempty=1-mu*mu
 H0=1-2*(p0*math.log2(p0)+(t*t/4)*math.log2(t*t/4))+(he+(mu*mu*math.log2(mu*mu) if mu else 0))/4+core_nonempty
 Hf=2+(m-1)*hp(r)/4+hp(r-1)/8
 If=1+((m*r*2*d)-2*d)/4
 rem=t/2+d/2;S=4*If-Hf;A=ce-H0;e=H0-Hf-4*rem
 G=sum(h(x) for x in ds)-2
 return dict(m=m,r=r,G=G,CE=ce,H0=H0,Hf=Hf,S=S,A=A,edge=e,L=A+max(e,0),exact_floor=ce-2)
start=time.perf_counter();rows=[calc(m,r) for m in range(2,13) for r in range(2,13)]
passing=[x for x in rows if x['G']>=x['S'] and x['L']<x['S']]
obj={'rung':'numerical evidence','rows':rows,'marginal_fails_exact_passes':passing,'runtime_seconds':time.perf_counter()-start,'note':'parity controls deferred; point-product rows=121; frozen count133 is upper bound'}
(R/'out').mkdir(exist_ok=True)
(R/'out/DISCOVERY.json').write_text(json.dumps(obj,indent=2),encoding='utf-8')
print(json.dumps({'candidates':passing[:12],'runtime_seconds':obj['runtime_seconds']}))
