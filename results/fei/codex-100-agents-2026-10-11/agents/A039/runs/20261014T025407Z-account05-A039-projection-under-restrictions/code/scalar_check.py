from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('scalar_primitive',R/'code/pilot.py');V=importlib.util.module_from_spec(s);s.loader.exec_module(V)
def ex(x):return x,x
def add(*xs):return V.sumiv(xs)
def scale(x,a):return V.mul(x,ex(a))
def bern(p,q):return V.kl([p,1-p],[q,V.sub(ex(F(1)),q)])
def fmt(x):
    d=10**12;return {'lower':str(F((x[0]*d).__floor__(),d)),'upper':str(F((x[1]*d).__ceil__(),d))}
start=time.perf_counter();lo,hi=F(3,4),F(1)
g=lambda c:1-c-(1-F(32,55)*c)**2*(1-F(8,55)*c)**3
assert g(lo)>0>g(hi)
for _ in range(48):
    m=(lo+hi)/2
    if g(m)>0:lo=m
    else:hi=m
c=(lo,hi);t=scale(c,F(32,55));z=V.sub(ex(F(1)),scale(c,F(8,55)))
cube=V.mul(V.mul(z,z),z);h=scale(V.mul(V.sub(ex(F(1)),t),cube),F(1,2))
b0=V.div(h,add(ex(F(9,64)),h))
release=add(scale(bern(F(16,25),b0),F(25,64)),scale(bern(F(16,25),t),F(25,64)),scale(V.log(V.div(ex(F(1)),V.sub(ex(F(1)),t))),F(7,32)))
rho=add(ex(F(2)),scale(V.log(ex(F(7))),F(21,32)),scale(V.log(ex(F(5))),F(-25,16)))
v=F(55,64);r=[F(32,55)]*2+[F(8,55)]*3
HM=V.log(c)
for a in r:
    theta=scale(c,a)
    HM=V.sub(HM,add(scale(V.log(theta),a),scale(V.log(V.sub(ex(F(1)),theta)),1-a)))
hv=V.L.evalformal(V.L.h(v))
Hparent=add(ex(F(4)),scale(V.log(ex(F(3))),F(-9,16)))
root=V.sub(add(hv,scale(HM,v)),Hparent)
q0=add(ex(F(1,2)),scale(V.sub(ex(F(9,64)),scale(V.mul(t,cube),F(1,2))),F(12,25)))
O=bern(F(1,2),q0)
Hchild=add(ex(F(6)),scale(V.log(ex(F(7))),F(-49,32)))
TCchild=V.sub(scale(V.L.evalformal(V.L.h(F(1,8))),4),Hchild)
margin=V.sub(root,add(O,TCchild))
assert V.sub(release,rho)[0]>F(1,40)
assert margin[0]>F(1,25)
main=json.loads((R/'out/TRANSPORT.json').read_text())
for iv,key in [(release,'first_erasure_release'),(root,'root_occupancy_KL'),(margin,'release_minus_actual_conversion_reset')]:
    prev=main[key];assert iv[0]<=F(prev['upper']) and iv[1]>=F(prev['lower'])
out={'status':'PASS','assertions':6,'representation':'Three scalar conditional fibers for release; matched-moment maximum entropy formula for root KL, independent of enumerating reference atoms',
'c_bracket':[str(lo),str(hi)],'release':fmt(release),'release_minus_rho':fmt(V.sub(release,rho)),'actual_conversion_margin':fmt(margin),
'strict_certificates':{'release_minus_rho_lower':'1/40','root_KL_minus_outcome_KL_minus_mean_child_TC_lower':'1/25'},'runtime_seconds':time.perf_counter()-start}
assert out['runtime_seconds']<60
(R/'out/SCALAR_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
