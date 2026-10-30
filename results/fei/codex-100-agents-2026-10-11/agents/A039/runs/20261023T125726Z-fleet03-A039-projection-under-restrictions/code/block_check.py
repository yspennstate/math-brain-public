from pathlib import Path
from fractions import Fraction as F
import importlib.util,time,json
R=Path(__file__).resolve().parents[1];OWN=R.parents[1]
p=OWN/'runs/20261023T105639Z-fleet03-A039-projection-under-restrictions/code/check.py'
s=importlib.util.spec_from_file_location('prior',p);M=importlib.util.module_from_spec(s);s.loader.exec_module(M);H=M.H
START=time.monotonic();N=0
def ck(a,label):
 global N
 N+=1
 assert a,label
 assert time.monotonic()-START<55,'frozen55s'
def local(r,eps,sgn):
 d=F(1,1<<r)
 v=[-1 if (x>>1)==0 or (x&1 and (x>>1)==3) else 1 for x in range(1<<(r+1))]
 p=H.spectrum(v);q=M.qlaw(v);u=[1,-1];qu=H.spectrum(u)
 ck(sum(v)==len(v)*(1-3*d),'parent actual mean')
 ck(p[-1]==d*d,'parent nonzero full mass')
 ck(sum(H.restrict(v,0,0))==len(v)//2*(1-2*d),'child0 actual mean')
 ck(sum(H.restrict(v,0,1))==len(v)//2*(1-4*d),'child1 actual mean')
 t=M.selector(M.signed(M.makecore([v,u]),sgn),eps);Q=H.lift(t,H.tensor([q,qu]))
 ch,rr,pb,qb,ks=H.channel(t,Q,1);sigma=H.IV();fresh=H.IV()
 for y,(ct,cp,old) in enumerate(ch):
  vy=H.restrict(v,0,y);py=H.spectrum(vy);qy=M.qlaw(vy);new=H.lift(ct,H.tensor([qy,qu]))
  ck(py[-1]==(4 if y==0 else 16)*d*d,'child source full mass')
  ck(1-py[0]<=8*d,'actual child variance bound')
  sigma+=(H.KL(cp,new)-H.KL(cp,old))*F(1,2);fresh+=H.KL(py,qy)*F(1,4)
 ck(sigma.hi<=fresh.hi,'generic compensated DP gross factor bill bound')
 ck(fresh.hi<(H.log2(F(6,5))*(4*d)).hi,'local vanishing block bill')
 ck(H.KL(p,q).hi<(H.log2(F(6,5))*(6*d)).hi,'original block KL variance cap')
 return {'r':r,'epsilon':eps,'sign':sgn,'sigma':sigma.json(),'fresh_factor_bill':fresh.json(),'outcomes':list(map(str,rr))}
rows=[]
for r in range(3,7):
 for eps in [1,-1]:
  for sgn in [1,-1]:rows.append(local(r,eps,sgn))
scalars=[]
for s in range(12,21):
 k=1<<s;r=s*s;kd=F(k,1<<r)
 ck(kd<F(1,4096),'tiny summed private density')
 ck(16*r*kd<F(1,2048),'all full-core entropy cap')
 ck(F(1,4)-F(13,4096)>F(1,5),'whole reference KL lower cap')
 ck(6*kd*F(11,40)<F(1,1000),'actual block conversion is a refund')
 ck(F(7,2)*F(11,40)<1,'combined original and later variance bank')
 ck(F((s+1)**2,s*s)*F(1,1<<(2*s))<1,'entropy bound decreases analytically')
 scalars.append({'s':s,'k':k,'r':r,'kd':str(kd)})
out={'status':'PASS','local_cases':len(rows),'scalar_cases':len(scalars),'checks':N+M.EXTRA+H.CHECKS,'new_checks':N,'runtime_seconds':time.monotonic()-START,'local':rows,'scalars':scalars,'external_review':'PENDING','full_FEI':'OPEN'}
(R/'out/BLOCK_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['local','scalars']}))
