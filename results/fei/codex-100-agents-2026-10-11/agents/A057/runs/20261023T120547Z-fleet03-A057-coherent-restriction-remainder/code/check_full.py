from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import time,json
ROOT=Path(__file__).resolve().parents[1]
ns={'__file__':str(ROOT/'code/check_mixed.py')}
exec((ROOT/'code/check_mixed.py').read_text(encoding='utf-8').split('for g in cores:')[0],ns)
add,entropy,nonneg,physical,ticket,restrict,phi=[ns[k] for k in ['add','entropy','nonneg','physical','ticket','restrict','phi']]
influence=ns['ns']['influence']
start=time.monotonic();checks=states=xedges=tagedges=rarepartners=deadpartners=0
def ck(b):
 global checks
 assert b;checks+=1
 if time.monotonic()-start>55:raise RuntimeError('frozen55s cap')
def capped(t,q):
 T=ticket(t,q)
 return {2:Q(2)} if nonneg(add((1,T),(-1,{2:2}))) else T
for g in ns['cores']:
 mu=Q(sum(g),len(g));q=mu*mu;full=physical(4,g,2,1)
 def state(xs,ts):
  fix={i:v for i,v in enumerate(xs) if v is not None};fix.update({6+i:v for i,v in enumerate(ts) if v is not None})
  rem=[i for i in range(8) if i not in fix];vals=restrict(full,fix);n=xs.count(None)
  t=Q(1,1<<n) if 0 not in xs else Q(0)
  T=capped(t,q) if None in ts else {};return vals,rem,t,T
 for xs in product([None,0,1],repeat=4):
  for ts in product([None,0,1],repeat=2):
   vals,rem,t,U=state(xs,ts);H=entropy(vals);states+=1;n=xs.count(None)
   for i,v in enumerate(xs):
    if v is not None:continue
    hs=[];us=[]
    for bit in [0,1]:
     xx=list(xs);xx[i]=bit;vv,rr,tt,uu=state(tuple(xx),ts);hs.append(entropy(vv));us.append(uu)
    D=add((1,H),(-Q(1,2),hs[0]),(-Q(1,2),hs[1]));ck(nonneg(D));ck(nonneg(add((1,{2:2}),(-1,D))))
    if None in ts:ck(nonneg(add((1,U),(-Q(1,2),us[0]),(-Q(1,2),us[1]))))
    if xs[i^1] is not None:
     if not t:ck(D=={});deadpartners+=1
     else:
      meanh=Q(0) if None in ts else mu*(-1)**sum(ts)
      e=1-influence(vals,rem.index(i));ck(e==t*(1-meanh))
      if n>=2:
       h2=add((1,phi(e)),(1,phi(1-e)))
       ck(nonneg(add((1,h2),(1,{2:3*e}),(-1,D))))
       ck(nonneg(add((1,{2:2*t*(n+4)}),(-1,D))))
      rarepartners+=1
    xedges+=1
   for j,v in enumerate(ts):
    if v is not None:continue
    hs=[]
    for bit in [0,1]:
     ss=list(ts);ss[j]=bit;vv,rr,tt,uu=state(xs,tuple(ss));hs.append(entropy(vv))
    D=add((1,H),(-Q(1,2),hs[0]),(-Q(1,2),hs[1]))
    if ts.count(None)>1:ck(D=={})
    else:ck(nonneg(add((1,U),(-1,D))))
    tagedges+=1
S=Q(0)
for n in range(2,129):
 S+=Q(n+4,1<<(n-1));tail=Q(n+6,1<<(n-1));ck(S+tail==7)
for m in range(16,257,4):
 c=Q(1,1<<m);bank=2*m-4*m*c
 ck(bank-2*c-m-11>=m/Q(4))
out={'status':'PASS','local_m':4,'states':states,'X_query_edges':xedges,'tag_query_edges':tagedges,'rare_second_partner_edges':rarepartners,'dead_mask_partner_zero_edges':deadpartners,'geometric_tail_cases':127,'full_owner_scalar_cases':61,'exact_assertions':checks,'seconds':time.monotonic()-start,'scope':'full local mixed domain at small m; original full-depth cash theorem asserted only analytically for m>=16; no large truth tables'}
(ROOT/'out/full.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
