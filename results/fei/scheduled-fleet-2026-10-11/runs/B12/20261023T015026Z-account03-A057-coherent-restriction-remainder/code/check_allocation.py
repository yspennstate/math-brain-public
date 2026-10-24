"""v1 fine-profile edge audit; shares exact log helper, not an independent implementation."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as Q
import itertools,time,json
ROOT=Path(__file__).resolve().parents[1]
ns={'__file__':str(ROOT/'code/check_nonflat.py')}
exec((ROOT/'code/check_nonflat.py').read_text(encoding='utf-8').split('worst_lower=None')[0],ns)
add,entropy,phi,nonneg,influence=[ns[x] for x in ['add','entropy','phi','nonneg','influence']]
entropy=lru_cache(None)(entropy)
start=time.monotonic();checks=states=edges=sources=positive_sources=0
c=Q(1,16);a=(1+c)/2;b=tuple((-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16))
def ck(v):
 global checks
 assert v;checks+=1
def table(n,t):return tuple(1 if(t>>x)&1 else -1 for x in range(1<<n))
def restrict(vals,state):
 rem=[i for i,z in enumerate(state) if z is None];out=[]
 for x in range(1<<len(rem)):
  full=sum(z<<i for i,z in enumerate(state) if z is not None)
  full+=sum(((x>>j)&1)<<i for j,i in enumerate(rem));out.append(vals[full])
 return tuple(out),rem
@lru_cache(None)
def hphase(g,phase):
 if phase==0:return entropy(g)
 rare=tuple(g[y] if x==0 else b[x] for y in range(len(g)) for x in range(16))
 if phase==1:return entropy(rare)
 frequent=tuple(g[y] for y in range(len(g)) for x in range(16))
 return entropy(frequent+rare)
def profile(u,v,s,t):
 pu=Q(1,2) if s[0] is None else Q(s[0]==0);pv=1-pu
 ur,_=restrict(u,s[1:3]);vr,_=restrict(v,s[3:4])
 U={};R={}
 for p,h in [(pu,ur),(pv,vr)]:
  mean=Q(sum(h),len(h));V=1-mean*mean
  U=add((1,U),(t*p,add((1,entropy(h)),(-1,phi(mean*mean)))))
  R=add((1,R),(V,phi(t*p)))
 return U,R
def capacity(g,rem,t,K):
 ctrl=sum(influence(g,j) for j,i in enumerate(rem) if i==0)
 data=sum(influence(g,j) for j,i in enumerate(rem) if i!=0)
 return t*(K*ctrl+5*data),ctrl
for ut,vt in itertools.product(range(16),range(4)):
 u,v=table(2,ut),table(1,vt)
 gfull=tuple(u[(x>>1)&3] if not x&1 else v[(x>>3)&1] for x in range(16))
 for state in itertools.product([None,0,1],repeat=4):
  if time.monotonic()-start>55:raise RuntimeError('frozen55-second cap')
  g,rem=restrict(gfull,state);H=[hphase(g,p) for p in [-1,0,1]]
  Upre,Rpre=profile(u,v,state,a)
  D=add((1,H[0]),(-Q(1,2),H[1]),(-Q(1,2),H[2]))
  mu=Q(sum(g),len(g));dX=(1-c-mu*(Q(1,4)-c))/2
  ck(nonneg(add((1,{2:6*dX}),(-1,D))));sources+=1
  qh,ctrl=capacity(g,rem,a,21);q0,_=capacity(g,rem,Q(1),20);q1,_=capacity(g,rem,c,24)
  ck(qh-(q0+q1)/2==Q(13,32)*ctrl);positive_sources+=ctrl>0
  for phase,t,K in [(-1,a,21),(0,Q(1),20),(1,c,24)]:
   U,R=profile(u,v,state,t);UR=add((1,U),(1,R));qp,_=capacity(g,rem,t,K);states+=1
   hp=hphase(g,phase)
   for j,orig in enumerate(rem):
    child=[];URchild=[];qc=[]
    for value in [0,1]:
     sc=list(state);sc[orig]=value;gc,rc=restrict(gfull,tuple(sc))
     child.append(hphase(gc,phase));uc,rr=profile(u,v,tuple(sc),t)
     URchild.append(add((1,uc),(1,rr)));qc.append(capacity(gc,rc,t,K)[0])
    decrement=add((1,hp),(-Q(1,2),child[0]),(-Q(1,2),child[1]))
    drop=add((1,UR),(-Q(1,2),URchild[0]),(-Q(1,2),URchild[1]))
    rate=K if orig==0 else 5
    own=t*influence(g,j);credit=rate*own
    ck(qp-sum(qc)/2==credit)
    ck(nonneg(add((1,{2:credit}),(1,drop),(-1,decrement))))
    edges+=1
for m in range(4,129):
 cc=Q(1,1<<m);aa=(1+cc)/2
 ck(21*aa-(20+cc*(20+m))/2==aa-m*cc/2)
 ck(aa-m*cc/2>=Q(13,32))
out={'status':'PASS','source_cylinders':sources,'positive_controller_ticket_refunds':positive_sources,
 'phase_states':states,'internal_query_edges':edges,'exact_assertions':checks,
 'elapsed_seconds':time.monotonic()-start,'scope':'all local edges of frozen fine representations; all-policy conclusion is by proved induction, not enumerating policies'}
(ROOT/'out/allocation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
