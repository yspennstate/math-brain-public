from fractions import Fraction as F
from pathlib import Path
import sys,time,json
import exact as E
import channel as C
R=Path(__file__).resolve().parents[1];start=time.perf_counter();N=0
if '--scalar' in sys.argv:
 E.GRID=1<<256
 def precise_ln_series(x):
  z=(x-1)/(x+1);s=F(0);power=z
  for j in range(64):s+=power/F(2*j+1);power*=z*z
  return (2*s,2*s+2*power/(129*(1-z*z)))
 E.ln_series=precise_ln_series;E.LN2=E.ln_series(F(2));E.logpoint.cache_clear()

def ck(b):
 global N
 N+=1;assert b,N
 assert time.perf_counter()-start<(240 if "--scalar" in sys.argv else 55)

def formula(k):
 d=F(1,2**k);e=d*d;a=F(1,6)
 As=[(1-2*c*d+2*e)/4 for c in [1,-1]]
 V=E.total(E.scale(A,E.logpoint(1-a*e/(4*A))) for A in As)
 ratio=F(8192,3125)*(1+49*e)**5/((1+80*e)**4*(1+16*e))
 eta=a*(F(3,10)-F(4,5)*e-e*(1+2*e)/(2*(1+4*e*e)))
 O=E.scale(F(-1,2),E.logpoint(1-eta*eta));full=E.scale(e,E.logpoint(ratio));sigma=E.add(E.add(V,full),O)
 return sigma,[(1+eta)/2,(1-eta)/2],V,full,O,ratio,eta

def family(k):
 g=[(-1)**(z&1)*(-1 if z in [2,3] else 1) for z in range(1<<k)]
 v=[g[z>>1]*(-1 if z==1 else 1) for z in range(1<<(k+1))]
 return v,g,C.E.restrict(v,0,1)

def spectral_certificate(k,v):
 d=F(1,2**k);coef=[]
 for mask in range(len(v)):
  S=mask>>1
  gg=(F(1) if S==1 else F(0))- (4*d*(-1)**((S>>1)&1) if S&1 else 0)
  coef.append(d if mask&1 else gg-d)
 ck(E.law(v)==[a*a for a in coef]);ck(sum(v)==-d*len(v));ck(coef[1]==d);ck(coef[-1]==d);ck(coef[-2]==3*d);ck(coef[2]==1-5*d)

def physical():
 rows=[]
 for k in ([3] if '--pilot' in sys.argv else range(3,9)):
  v,g,gp=family(k);spectral_certificate(k,v);d=F(1,2**k)
  ck(F(sum(v[z]!=v[z^1] for z in range(len(v))),len(v))==d)
  ck(E.fwht(g)[-1]/F(len(g))==4*d);ck(E.fwht(gp)[-1]/F(len(gp))==2*d)
  for eps in [1,-1]:
   t,q=C.lift(v,[1],eps,C.qfactor(v,F(1,6)),[F(1)])
   ts,ps,old,outs,loss,out=C.step(t,q,1);sigma=E.iv(0);newbill=E.iv(0);oldbill=E.iv(0)
   for y,vy in enumerate([g,gp]):
    tt,new=C.lift(vy,[1],eps,C.qfactor(vy,F(1,6)),[F(1)]);ck(tt==ts[y]);ck(all((p==0)==(q==0) for p,q in zip(ps[y],new)))
    nk=C.KL(ps[y],new);ok=C.KL(ps[y],old[y]);newbill=E.add(newbill,E.scale(F(1,2),nk));oldbill=E.add(oldbill,E.scale(F(1,2),ok));sigma=E.add(sigma,E.scale(F(1,2),E.sub(nk,ok)))
   ss,oo,V,full,O,ratio,eta=formula(k);ck(E.overlaps(sigma,ss));ck(outs==oo);ck(sigma[0]>0);ck(out[0]>0)
   ck(E.overlaps(E.add(C.KL(E.law(t),q),sigma),E.add(E.add(loss,out),newbill)))
   if k>=5:ck(sigma[0]>E.div(E.iv(F(1,2048)),E.LN2)[1])
   rows.append({'k':k,'epsilon':eps,'Inf_j':str(d),'sigma':E.enc(sigma),'sigma_over_Inf':E.enc(E.scale(1/d,sigma)),'outcomes':list(map(str,outs)),'old_inherited_KL':E.enc(oldbill),'fresh_KL':E.enc(newbill),'erasure_KL':E.enc(loss),'outcome_KL':E.enc(out),'same_support':True})
 return rows

def scalar():
 rows=[]
 progress=(R/"out/SCALAR_PROGRESS.jsonl").open("w",encoding="utf-8")
 ck(F(8192,3125)>(F(9,8)**4)*F(33,32));ck(F(13,18432)>F(1,2048));ck(F(9053,2560)>F(7,2))
 for k in range(5,65):
  d=F(1,2**k);e=d*d;ss,outs,V,full,O,ratio,eta=formula(k)
  ck(ratio>1);ck(eta>=F(1,24));ck(V[0]>=-e/F(6)/E.LN2[0]);ck(ss[0]>E.div(E.iv(F(1,2048)),E.LN2)[1]);ck(O[0]>0)
  if k>=10:
   ck(4*(1-10*d)-10*d*(2*k+3)-F(1,5)>F(7,2));ck(4*(1-12*d)-12*d*(2*k+2)>F(7,2))
  rows.append({'k':k,'Inf_j':str(d),'sigma':E.enc(ss),'normalized_outcome':E.enc(O),'ratio_R':str(ratio),'eta':str(eta)})
  progress.write(json.dumps(rows[-1])+"\n");progress.flush()
 progress.close()
 return rows
rows=scalar() if '--scalar' in sys.argv else physical()
receipt={'status':'PASS','cases':len(rows),'assertions':N,'channel_assertions':C.checks,'primitive_assertions':E.checks,'seconds':time.perf_counter()-start,'rows':rows}
name='SCALAR' if '--scalar' in sys.argv else ('PILOT' if '--pilot' in sys.argv else 'PHYSICAL')
(R/'out'/f'{name}.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in receipt.items() if k!='rows'}))
