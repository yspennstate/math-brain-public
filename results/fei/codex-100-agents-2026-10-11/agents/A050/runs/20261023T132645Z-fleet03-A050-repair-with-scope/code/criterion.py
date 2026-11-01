from fractions import Fraction as F
from pathlib import Path
import runpy,sys,json,time
# Load definitions only; do not execute the exhaustive check here.
R=Path(__file__).resolve().parents[1];start=time.perf_counter()
d={};src=(R/'code/check.py').read_text(encoding='utf-8');d['__file__']=str(R/'code/check.py')
exec(src.split('cases=0')[0],d)
spec=d['spectrum'];restrict=d['restrict'];marg=d['marg'];mix=d['mixture'];ck=d['ck']
def fresh(p,full,a):
 u=p.get(0,F(0));return mix(p,1-a,[(0,a*u),(full,a*(1-u))])
def channel(t,co,q,i):
 p=spec(t,co);j=co.index(i);cn=tuple(x for x in co if x!=i);mask=sum(1<<x for x in cn)
 pe=marg(p,mask);qe=marg(q,mask);out=[]
 for k in (0,1):
  tt=restrict(t,j,k);pk=spec(tt,cn)
  joint={s:w*pk.get(s,F(0))/(2*pe[s]) for s,w in qe.items()}
  rr=sum(joint.values());ck(rr==F(1,2));out.append((pk,{s:w/rr for s,w in joint.items() if w}))
 return cn,out
cases=[]
for r in ((2,) if '--pilot' in sys.argv else range(2,7)):
 def h(z):return -1 if z==(1<<r)-1 else 1
 t=tuple(h((x>>1)^(x&1)) for x in range(1<<(r+1)))
 co=tuple(range(r+1));p=spec(t,co);full=(1<<(r+1))-1
 ck(p.get(full,F(0))>0)
 # Direct full-vertex pivot count independently checks the rare selector influence.
 ck(F(sum(t[x]!=t[x|1] for x in range(len(t)) if not x&1),len(t)//2)==F(1,1<<(r-1)))
 for a in (F(1,8),F(1,7),F(1,6),F(1,2)):
  q=fresh(p,full,a);cn,kids=channel(t,co,q,0)
  ck(kids[0][0]==kids[1][0])
  for pk,qk in kids:ck(qk==fresh(pk,sum(1<<x for x in cn),a))
  # Either-sign activation lift: zero-data actual atoms, nonempty Q/4 at both copies.
  for sign in (-1,1):
   at=tuple(sign if not x&1 else t[x>>1] for x in range(2*len(t)))
   ac=tuple(range(r+2));ap=spec(at,ac);aq={s:w for s,w in ap.items() if s>>1==0}
   for s,w in q.items():
    if s:
     for z in (0,1):aq[(s<<1)|z]=w/4
   ck(sum(aq.values())==1);an,akids=channel(at,ac,aq,1)
   for k,(pk,qk) in enumerate(akids):
    corepk=kids[k][0];coreq=fresh(corepk,sum(1<<x for x in cn),a)
    wanted={s:w for s,w in pk.items() if s>>1==0}
    for s,w in coreq.items():
     if s:
      for z in (0,1):wanted[(s<<1)|z]=w/4
    ck(qk==wanted)
  cases.append({'r':r,'alpha':str(a),'core_and_both_activations':'inherited equals fresh exactly','selector_influence':str(F(1,1<<(r-1)))})
out={'status':'PASS','cases':cases,'assertions':d['C'],'runtime_seconds':time.perf_counter()-start,'arithmetic':'exact rational atom equality; independent direct Walsh and pivotal edges'}
(R/'out'/('CRITERION_PILOT.json' if '--pilot' in sys.argv else 'CRITERION.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
