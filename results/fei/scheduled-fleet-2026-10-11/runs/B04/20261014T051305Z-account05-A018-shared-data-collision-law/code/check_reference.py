from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import time,json,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261012T010436Z-account05-A018-shared-data-collision-law/code/check_lead.py'
ns={'__file__':str(OLD),'__name__':'arithmetic_only'}
exec(compile(OLD.read_text(encoding='utf8').split("\nresult={'helper_version'")[0],str(OLD),'exec'),ns)
start=time.perf_counter();checks=0
def ck(v):
 global checks
 checks+=1;assert v;assert time.perf_counter()-start<60
def W(v):
 if len(v)==1:return v[:]
 k=len(v)//2;a=W(v[:k]);b=W(v[k:])
 return [x+y for x,y in zip(a,b)]+[x-y for x,y in zip(a,b)]
def data(v):
 w=W(v);L=len(v);p=[Q(x*x,L*L) for x in w];I=Q(0)
 for bit in range((L-1).bit_length()):
  edge=Q(sum(v[x]!=v[x^(1<<bit)] for x in range(L)),L)
  ck(edge==sum(p[s] for s in range(L) if s&(1<<bit)));I+=edge
 return p,ns['ent'](p),I,Q(sum(v),L)
def phi(mu):
 p=[(1+mu)**2/4,(1-mu)**2/4]
 return ns['add']((1,ns['ent'](p)),(1-mu*mu,{2:1}),(-Q(1,2),ns['ent']([mu*mu])))
def CE(p,q):
 ck(sum(q)==1)
 return ns['add'](*[(-x,ns['logq'](y)) for x,y in zip(p,q) if x])
def core(n,mask):return [1-2*((mask>>x)&1) for x in range(1<<n)]
fixtures=[[(1,m)] for m in range(4)]+[[(2,a),(2,b)] for a,b in ((0,0),(1,1),(1,6),(7,15))] if '--pilot' in sys.argv else [[(n,m)] for n in range(4) for m in range(1<<(1<<n))]+[[(2,a),(2,b)] for a in range(16) for b in range(16)]
rows=[];admitted=0;nonflat=0
for spec in fixtures:
 vs=[core(n,m) for n,m in spec];ds=[data(v) for v in vs]
 g=[1]
 for v in vs:g=[a*b for b in v for a in g]
 vp=[x for val in g for x in (val,1)]
 P,H,I,muparent=data(vp);mu=Q(sum(g),len(g));G,HG,IG,_=data(g)
 ck(HG==ns['add'](*[(1,d[1]) for d in ds]))
 ck(IG==sum(d[2] for d in ds))
 shared=(1-mu)/2;ck(I==IG/2+shared)
 profile=phi(mu);ck(H==ns['add']((Q(1,2),HG),(1,profile)))
 fold=(1-abs(mu))/2
 ck(ns['grid'](ns['add']((4*fold,{2:1}),(-1,profile)),constant=Q(5,8)*fold)[0]>=0)
 R=[P[2*t]+P[2*t+1] for t in range(len(g))]
 ck(R==[(p+int(t==0))/2 for t,p in enumerate(G)])
 costs=[]
 for flavor in ('actual','uniform'):
  qs=[d[0] if flavor=='actual' else [Q(1,len(v))]*len(v) for d,v in zip(ds,vs)]
  cj=[CE(d[0],q) for d,q in zip(ds,qs)]
  qprod=[Q(1)]
  for q in qs:qprod=[a*b for b in q for a in qprod]
  qjoint=[(q+int(t==0))/2 for t,q in enumerate(qprod)]
  full=[]
  for t,q in enumerate(qjoint):
   cond=[P[2*t]/R[t],P[2*t+1]/R[t]] if R[t] else [Q(1,2)]*2
   full.extend(q*x for x in cond)
  rootcost=CE(P,full)
  bound=ns['add'](*[(Q(1,2),c) for c in cj],(1,profile))
  ck(ns['grid'](ns['add']((1,bound),(-1,rootcost)))[0]>=0)
  if flavor=='actual':ck(rootcost==H)
  eligible=all(ns['grid'](ns['add']((6*d[2],{2:1}),(-1,c)))[0]>=0 for d,c in zip(ds,cj))
  if eligible:
   ck(ns['grid'](ns['add']((6*I,{2:1}),(-1,rootcost)))[0]>=0);admitted+=1
  costs.append({'reference':flavor,'normalized':'1','rate6_hypothesis_satisfied':eligible,'CE_prime_log':{str(p):str(c) for p,c in rootcost.items()}})
 nonflat+=int(any(len({p for p in d[0] if p})>1 for d in ds))
 rows.append({'core_specs':spec,'mu_product':str(mu),'I_parent':str(I),'folded_selector_influence':str(fold),'reference_checks':costs,'status':'PASS'})
 (ROOT/'out/REFERENCE_PARTIAL.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf8')
out={'status':'PASS','cases':len(rows),'checks':checks,'nonflat_cases':nonflat,'admitted_reference_cases':admitted,'elapsed_seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest(),'cases_details':rows}
(ROOT/'out'/('REFERENCE_PILOT.json' if '--pilot' in sys.argv else 'REFERENCE_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ('status','cases','checks','nonflat_cases','admitted_reference_cases','elapsed_seconds')}))
