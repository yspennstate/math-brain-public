import lib as L
from lib import Q,add,phi
from functools import lru_cache
from pathlib import Path
import itertools,time,json
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();assertions=0
def ck(ok):
 global assertions
 assertions+=1
 assert ok,assertions
 assert time.perf_counter()-start<58,'Frozen watchdog'
@lru_cache(None)
def coeff(t):return tuple(L.fw(t))
@lru_cache(None)
def p(t):return tuple(x*x for x in coeff(t))
@lru_cache(None)
def H(t):return L.entropy(p(t))
@lru_cache(None)
def B(t,i):return L.edge(p(t),i)
def I(t):return sum((L.inf(p(t),i) for i in range((len(t)-1).bit_length())),Q(0))
def inf(t,i):return L.inf(p(t),i)
@lru_cache(None)
def sl(t,i,s):
 return tuple(t[(b&((1<<i)-1))|((s<0)<<i)|((b>>i)<<(i+1))] for b in range(len(t)//2))
@lru_cache(None)
def compose(f,h):return tuple(f[2*r+(h[x]<0)] for r in range(len(f)//2) for x in range(len(h)))
def visit(f,h,xlabels,dlabels,order,depth):
 F=compose(f,h);mu=coeff(h)[0];var=1-mu*mu;V=add((var,B(f,0)))
 if not order or not depth:return ({},{},Q(0),Q(0),V,H(F),I(F))
 kind,label=order[0];order=order[1:]
 if kind=='x':
  j=xlabels.index(label);gamma=coeff(h)[1<<j];a=inf(f,0)*inf(h,j)
  ck(inf(F,j)==a)
  q=add((gamma*gamma,B(f,0)));r={}
  children=[visit(f,sl(h,j,s),xlabels[:j]+xlabels[j+1:],dlabels,order,depth-1) for s in [1,-1]]
  se,sd=a,Q(0)
 else:
  j=dlabels.index(label);a=((1+mu)/2)*inf(sl(f,0,1),j)+((1-mu)/2)*inf(sl(f,0,-1),j)
  ck(inf(F,len(xlabels)+j)==a)
  fs=[sl(f,j+1,s) for s in [1,-1]]
  q={};r=add((var,B(f,0)),(-var/2,B(fs[0],0)),(-var/2,B(fs[1],0)))
  children=[visit(fc,h,xlabels,dlabels[:j]+dlabels[j+1:],order,depth-1) for fc in fs]
  se,sd=Q(0),a
 Qall=add((1,q),*( (Q(1,2),c[0]) for c in children))
 Rall=add((1,r),*( (Q(1,2),c[1]) for c in children))
 se+=sum((c[2]/2 for c in children),Q(0));sd+=sum((c[3]/2 for c in children),Q(0))
 vl=add(*[(Q(1,2),c[4]) for c in children]);hl=add(*[(Q(1,2),c[5]) for c in children]);il=sum((c[6]/2 for c in children),Q(0))
 ck(add((1,Qall),(1,Rall))==add((1,V),(-1,vl)))
 ck(I(F)-il==se+sd)
 return Qall,Rall,se,sd,vl,hl,il
trees=0;comps=0
for nf,nh in [(2,2),(3,1)]:
 for a in range(1<<(1<<nf)):
  f=tuple(1 if a&(1<<b) else -1 for b in range(1<<nf))
  for b in range(1<<(1<<nh)):
   h=tuple(1 if b&(1<<x) else -1 for x in range(1<<nh))
   xs=[('x',i) for i in range(nh)];ds=[('d',i) for i in range(nf-1)]
   alt=[]
   for i in range(max(len(xs),len(ds))):
    if i<len(xs):alt.append(xs[i])
    if i<len(ds):alt.append(ds[i])
   for order in [xs+ds,ds+xs,alt]:
    for depth in [0,1,2,3]:
     visit(f,h,tuple(range(nh)),tuple(range(nf-1)),order,depth);trees+=1
   comps+=1
controls=[]
for k in [2,4,6]:
 delta=Q(1,1<<k)
 bent=tuple(1 if sum(((b>>(2*j))&1)*((b>>(2*j+1))&1) for j in range(k//2))%2==0 else -1 for b in range(1<<k))
 g=tuple(bent[y] if s==0 or y else -1 for y in range(1<<k) for s in range(2))
 f=tuple(g[2*y+(z^u)] for y in range(1<<k) for u in range(2) for z in range(2))
 h=tuple(L.majority(3,[]));F=compose(f,h);bstar=B(g,0)
 ck(B(f,0)=={});ck(inf(g,0)==delta);ck(I(g)==Q(k,2)+(k+1)*delta)
 ck(I(F)==Q(k,2)+Q(2*k+5,2)*delta)
 orders=[[('d',0)]+list(perm) for perm in itertools.permutations([('x',0),('x',1),('x',2)])]
 for order in orders:
  qa,ra,se,sd,vl,hl,il=visit(f,h,(0,1,2),tuple(range(k+1)),order,4)
  ck(qa==bstar);ck(ra==add((-1,bstar)));ck(vl=={})
  ck(se==3*delta/2 and sd==delta)
  defect=list(bent);defect[0]=-1
  ck(hl==add((Q(1,2),H(bent)),(Q(1,2),H(tuple(defect)))))
 ck(H(F)==add((1,H(g)),(2*delta,{2:Q(1)})))
 controls.append({'k':k,'delta':str(delta),'I_shadow':str(I(g)),'I_physical':str(I(F)),'spent_unlock_plus_encoder':str(Q(5,2)*delta),'shadow_bank':'B_s(g)','bank_prime_log':{str(q):str(v) for q,v in bstar.items()},'leaf_entropy_prime_log':{str(q):str(v) for q,v in hl.items()}})
 (ROOT/'out/CONTROLS.json').write_text(json.dumps(controls,indent=2)+'\n',encoding='utf-8')
out={'status':'PASS','helper':'A003-interleaved-shadow-v1','assertions':assertions,'compositions':comps,'labelled_prefix_trees':trees,'family_controls':len(controls),'encoder_orders_per_control':6,'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction; integer FWHT; exact prime-log entropy identities'}
(ROOT/'out/VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
