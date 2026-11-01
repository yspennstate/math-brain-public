from fractions import Fraction as F
from pathlib import Path
import json,time
import exact as E
import validate as V
R=Path(__file__).resolve().parents[1];start=time.perf_counter();v=V.point(3);u=[1,-1];p=E.law(v);alpha=F(1,6)
q=[p[0]]+[(1-alpha)*x for x in p[1:]];q[1]+=alpha*(1-p[0]);t,r=V.lift(v,u,1,q,E.law(u))
ts,ps,old,outs,loss,out=V.step(t,r,1);sigma=E.iv(0)
for y in [0,1]:
 vy=E.restrict(v,0,y);tt,new=V.lift(vy,u,1,V.qfactor(vy,alpha),E.law(u));V.ck(tt==ts[y]);sigma=E.add(sigma,E.scale(F(1,2),E.sub(V.KL(ps[y],new),V.KL(ps[y],old[y]))))
ratio=F(6875,6561)*F(99,100)**4*F(400,399)**8;expected=E.scale(F(1,16),E.logpoint(ratio));V.ck(E.overlaps(sigma,expected));V.ck(sigma[0]>0);V.ck(outs!=[F(1,2)]*2);V.ck(ratio>1);V.ck(outs==[F(21,40),F(19,40)])
receipt={'status':'PASS','cases':1,'signed_reset':E.enc(sigma),'exact_expression':'log2((6875/6561)*(99/100)^4*(400/399)^8)/16','outcomes':list(map(str,outs)),'assertions':V.checks,'primitive_assertions':E.checks,'seconds':time.perf_counter()-start,'scope':'counterexample ONLY when old full-spike hypothesis is removed; no FEI counterexample'}
(R/'out/CONTROL.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8');print(json.dumps(receipt))
