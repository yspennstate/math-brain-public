"""Frozen stage19 exact local-edge certificate. No floating-point sign decisions."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json,time,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261023T015026Z-account03-A057-coherent-restriction-remainder/code/check_nonflat.py'
ns={'__file__':str(OLD)}
exec(OLD.read_text(encoding='utf-8').split('worst_lower=None')[0],ns)
add,entropy,phi,nonneg,influence,interval=[ns[k] for k in ['add','entropy','phi','nonneg','influence','interval']]
entropy=lru_cache(maxsize=4096)(entropy)
start=time.monotonic();pilot='--pilot' in sys.argv;limit=55 if pilot else 180
checks=states=internal_edges=exterior_edges=source_states=positive_old=0
def ck(x):
 global checks
 assert x;checks+=1
def cap():
 if time.monotonic()-start>limit:raise RuntimeError('frozen runtime cap')
def restrict(vals,s):
 rem=[i for i,x in enumerate(s) if x is None]
 return tuple(vals[sum(x<<i for i,x in enumerate(s) if x is not None)+sum(((a>>j)&1)<<i for j,i in enumerate(rem))] for a in range(1<<len(rem))),rem
def bent(x,m):return (-1)**sum(((x>>i)&1)*((x>>(i+1))&1) for i in range(0,m,2))
def make(g,zs):
 ext,rem=restrict(tuple(bent(x,4) for x in range(16)),zs)
 active=1 not in zs;t=Q(1,1<<len(rem)) if active else Q(0)
 vals=tuple(g[y] if active and x==0 else ext[x] for y in range(len(g)) for x in range(len(ext)))
 return vals,rem,t
def block(vals,indices):return sum((influence(vals,i) for i in indices),Q(0))
def profile(u,v,ys,t):
 p=Q(1,2) if ys[0] is None else Q(ys[0]==0)
 ur,_=restrict(u,ys[1:]);U={};R={};Vbar=Q(0)
 for p0,h in [(p,ur),(1-p,(v,))]:
  mu=Q(sum(h),len(h));var=1-mu*mu
  U=add((1,U),(t*p0,add((1,entropy(h)),(-1,phi(mu*mu)))))
  R=add((1,R),(var,phi(t*p0)));Vbar+=p0*var
 return U,R,Vbar
def accounts(g,yr,u,v,ys,zs):
 vals,zr,t=make(g,zs);nz=len(zr);U,R,Vbar=profile(u,v,ys,t)
 ctrl=sum((influence(g,j) for j,i in enumerate(yr) if i==0),Q(0))
 data=sum((influence(g,j) for j,i in enumerate(yr) if i==1),Q(0))
 q=t*(21*ctrl+5*data);mu=Q(sum(g),len(g));var=1-mu*mu
 S=add((var,phi(t)));E=4*block(vals,range(nz))
 P=add((1,U),(1,R),(1,S),(1,{2:q+E}))
 return vals,zr,t,P,(U,R,q,S,E,Vbar,var)
zs_all=[s for s in product([None,0,1],repeat=4) if 1 in s or all(not(s[i] is not None and s[i+1] is not None) for i in [0,2])]
ck(len(zs_all)==74)
fixtures=list(product(range(4),[-1,1]));fixtures=fixtures[:2] if pilot else fixtures
for ut,v in fixtures:
 u=tuple(1 if ut>>x&1 else -1 for x in range(2))
 full=tuple(u[(x>>1)&1] if x&1==0 else v for x in range(4))
 for ys in product([None,0,1],repeat=2):
  cap();g,yr=restrict(full,ys);mu=Q(sum(g),len(g));a=Q(17,32)
  vals,zr,t,P,ac=accounts(g,yr,u,v,ys,(None,)*4)
  rare=vals;frequent=tuple(g[y] for y in range(len(g)) for _ in range(16));W=frequent+rare
  DX=add((1,entropy(W)),(-Q(1,2),entropy(frequent)),(-Q(1,2),entropy(rare)))
  dX=(1-Q(1,16)-mu*(Q(1,4)-Q(1,16)))/2
  ck(influence(W,len(W).bit_length()-2)==dX)
  Z=Q(1,4)*(1-mu*mu)
  ck(nonneg(add((1,{2:6*dX-Z/2} ),(-1,DX))))
  ck(4*block(W,range(4))==ac[4]/2);source_states+=1
  for zs in zs_all:
   cap();vals,zr,t,P,ac=accounts(g,yr,u,v,ys,zs);states+=1;H=entropy(vals)
   U,R,q,S,E,Vbar,var=ac
   for j,orig in enumerate(yr):
    children=[];Ps=[];Es=[]
    for b0 in [0,1]:
     yy=list(ys);yy[orig]=b0;gc,rc=restrict(full,yy)
     vc,_,_,pc,acc=accounts(gc,rc,u,v,tuple(yy),zs)
     children.append(entropy(vc));Ps.append(pc);Es.append(acc[4])
    D=add((1,H),(-Q(1,2),children[0]),(-Q(1,2),children[1]))
    drop=add((1,P),(-Q(1,2),Ps[0]),(-Q(1,2),Ps[1]))
    ck(nonneg(add((1,drop),(-1,D))))
    ck(E==sum(Es)/2);internal_edges+=1
    if nonneg(add((1,D),(-1,{2:Q(1,1000)}))):positive_old+=1
   for j,orig in enumerate(zr):
    if t and zs[orig^1] is not None:continue
    cs=[];pps=[];acs=[]
    for b0 in [0,1]:
     zz=list(zs);zz[orig]=b0
     vc,_,_,pc,acc=accounts(g,yr,u,v,ys,tuple(zz));cs.append(entropy(vc));pps.append(pc);acs.append(acc)
    d=influence(vals,j);D=add((1,H),(-Q(1,2),cs[0]),(-Q(1,2),cs[1]))
    ck(nonneg(add((1,{2:4*d}),(-1,D))))
    ck(E-(acs[0][4]+acs[1][4])/2==4*d)
    ck(nonneg(add((1,P),(-Q(1,2),pps[0]),(-Q(1,2),pps[1]),(-1,D))))
    if t:
     ck(d==Q(1,2)+t*(1-mu))
     ck(add((1,U),(-Q(1,2),acs[0][0]),(-Q(1,2),acs[1][0]))=={})
     ck(q==(acs[0][2]+acs[1][2])/2)
     ck(add((1,R),(-Q(1,2),acs[0][1]),(-Q(1,2),acs[1][1]))=={2:t*Vbar} if Vbar else add((1,R),(-Q(1,2),acs[0][1]),(-Q(1,2),acs[1][1]))=={})
     ck(add((1,S),(-Q(1,2),acs[0][3]),(-Q(1,2),acs[1][3]))=={2:t*var} if var else add((1,S),(-Q(1,2),acs[0][3]),(-Q(1,2),acs[1][3]))=={})
    else:ck(d in [0,Q(1,2),1])
    exterior_edges+=1
controls=[]
for m in [4,6,8,10,12]:
 cap();N=1<<(m-1)
 # First bit is0: original coordinate1 is now an isolated partner, coordinate0 of this actual table.
 vals=tuple(-1 if x==0 else bent(x<<1,m) for x in range(N))
 d=influence(vals,0);H=entropy(vals)
 cs=[entropy(tuple(vals[x] for x in range(N) if x&1==b0)) for b0 in [0,1]]
 D=add((1,H),(-Q(1,2),cs[0]),(-Q(1,2),cs[1]))
 gap=add((1,D),(-1,{2:4*d}));lo,hi=interval(gap)
 ck(d==Q(4,1<<m));controls.append({'m':m,'d':str(d),'gap_lower':str(lo),'gap_upper':str(hi),'E4_local_extension_fails':lo>0})
out={'status':'PASS','pilot':pilot,'states':states,'source_states':source_states,'internal_edges':internal_edges,'exterior_edges':exterior_edges,'positive_internal_debit_edges':positive_old,'exact_assertions':checks,'seconds':time.monotonic()-start,'negative_controls':controls,'helper_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest(),'scope':'local edges exhaustive in frozen domain; arbitrary-policy conclusion by analytic telescope'}
(ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='negative_controls'}));print('partner controls',[(x['m'],x['E4_local_extension_fails']) for x in controls])
