import json,time
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261014T055119Z-account05-A019-orthogonality-extensions/code/check_exposure.py'
src=old.read_text(encoding='utf-8'); ns={'Q':Q,'lru_cache':lru_cache,'checks':0}
exec(src[src.index('def ck(x):'):src.index("transport={'positive'")],ns)
ck=ns['ck'];sp=ns['spectrum'];ce=ns['ce'];add=ns['add'];gate=ns['gate'];psi=ns['psi'];nn=ns['nonnegative'];lf=ns['logform']
start=time.monotonic();rows=[]
for k in range(1,9):
 e=Q(1,1<<k);m=e*e
 a=tuple(1-2*u for v in range(1<<k) for u in range(2))
 b=tuple(1 if v==0 else 1-2*u for v in range(1<<k) for u in range(2))
 ps=[sp(z) for z in (a,b)]; qs=[tuple((p+int(i==0))/2 for i,p in enumerate(pv)) for pv in ps]
 h=tuple(x for pair in zip(a,b) for x in pair);ph=sp(h);qh=[]
 for i in range(len(a)):
  row=ph[2*i]+ph[2*i+1];qr=(qs[0][i]+qs[1][i])/2
  qh.extend((qr*ph[2*i]/row,qr*ph[2*i+1]/row) if row else (qr,Q(0)))
 ck(Q(sum(a),len(a))==0);ck(Q(sum(b),len(b))==e)
 ck(Q(sum(x!=y for x,y in zip(a,b)),len(a))==e/2)
 ck(ph[0]==m/4);ck(ph[1]==m/4);ck(qh[0]==(2+m)/8)
 kl=lambda p,q:add((1,ce(p,q)),(-1,ce(p,p)))
 dc=add((Q(1,2),kl(ps[0],qs[0])),(Q(1,2),kl(ps[1],qs[1])),(-1,kl(ph,qh)))
 ck(dc==add((m/2,lf((2+m)/(1+m)))));ck(nn(dc))
 rt=gate(h,tuple(qh),1);cs=[gate(z,q,1) for z,q in zip((a,b),qs)]
 lam=add((Q(1,2),cs[0][1]),(Q(1,2),cs[1][1]),(-1,rt[1]),(-Q(1,2),dc))
 dh=add((1,ce(ph,ph)),(-Q(1,2),ce(ps[0],ps[0])),(-Q(1,2),ce(ps[1],ps[1])))
 curv=add((1,psi(e/4)),(-Q(1,2),psi(Q(0))),(-Q(1,2),psi(e/2)))
 actual=add((1,rt[0]),(-Q(1,2),cs[0][0]),(-Q(1,2),cs[1][0]))
 ck(actual==add((Q(1,2),dh),(1,curv),(1,lam)))
 banks=[add((4*sum(p*i.bit_count() for i,p in enumerate(pv)),{2:Q(1)}),(-1,ce(pv,q))) for pv,q in zip(ps,qs)]
 rem=add((Q(1,4),banks[0]),(Q(1,4),banks[1]),(-Q(1,8),{2:Q(1)}),(-1,lam))
 ck(nn(lam) if k>=2 else nn(add((-1,lam))))
 ck(nn(add((1,rem),(-Q(3,4) if k>=2 else Q(1,2),{2:Q(1)}))))
 rows.append({'k':k,'d':str(e/2),'Lambda':{str(p):str(v) for p,v in lam.items()},'Dcore':{str(p):str(v) for p,v in dc.items()},'boundary':k==1,'Lambda_sign':'negative' if k==1 else 'positive'})
 assert time.monotonic()-start<60
out={'status':'PASS','cases':len(rows),'checks':ns['checks'],'seconds':time.monotonic()-start,'rows':rows,'full_fei':'OPEN'}
(R/'out/ONE_BIASED_CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
