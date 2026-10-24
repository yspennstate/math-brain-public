from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import sys,json,time
ROOT=Path(__file__).resolve().parents[1];START=time.perf_counter();COUNT=0;NODES=0;DEBITS={}
def ck(x):
 global COUNT
 assert x
 COUNT+=1
 if time.perf_counter()-START>55:raise TimeoutError('frozen 55s watchdog')
def save(n,o):(ROOT/'out'/n).write_text(json.dumps(o,indent=2),encoding='utf-8')
GRID=1<<128
def quant(lo,hi):return F((lo*GRID).__floor__(),GRID),F((hi*GRID).__ceil__(),GRID)
def lnraw(x):
 z=(x-1)/(x+1);power=z;s=F(0)
 for j in range(44):s+=power/(2*j+1);power*=z*z
 return 2*s,2*s+2*power/(89*(1-z*z))
LN2=lnraw(F(2))
@lru_cache(None)
def log(x):
 x=F(x);ck(x>0);k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 lo,hi=lnraw(x);return quant(k+lo/LN2[1],k+hi/LN2[0])
def add(*args):
 d={}
 for v in args:
  for k,x in v.items():d[k]=d.get(k,F(0))+x
 return {k:x for k,x in d.items() if x}
def scale(v,a):return {k:a*x for k,x in v.items() if a*x}
@lru_cache(None)
def factors(n):
 d={};i=2
 while i*i<=n and i<=97:
  while n%i==0:d[i]=d.get(i,0)+1;n//=i
  i+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def lv(x):
 d={}
 for n,s in [(x.numerator,1),(x.denominator,-1)]:
  for k,j in factors(n).items():d[k]=d.get(k,F(0))+s*j
 return {k:a for k,a in d.items() if a}
def bounds(v):
 lo=hi=F(0)
 for k,a in v.items():
  x,y=log(k)
  if a<0:x,y=y,x
  lo+=a*x;hi+=a*y
 return quant(lo,hi)
def ent(p):return add(*(scale(lv(w),-w) for w in p.values() if w))
def kl(p,q):
 for s,w in p.items():ck(not w or q.get(s,F(0))>0)
 return add(*(scale(lv(w/q[s]),w) for s,w in p.items() if w))
def nonnegative(v):ck(not v or bounds(v)[0]>=0)
def spec(t):
 n=len(t);a=list(t);k=1
 while k<n:
  for b in range(0,n,2*k):
   for j in range(b,b+k):u,v=a[j],a[j+k];a[j],a[j+k]=u+v,u-v
  k*=2
 p={s:F(x*x,n*n) for s,x in enumerate(a) if x};ck(sum(p.values())==1)
 inf=[sum((w for s,w in p.items() if s>>j&1),F(0)) for j in range(n.bit_length()-1)]
 for j,d in enumerate(inf):ck(d==F(sum(t[x]!=t[x^(1<<j)] for x in range(n)),n))
 return p,sum(inf)
def restrict(t,j,b):return tuple(t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(t)//2))
def drop(s,j):return (s&((1<<j)-1))|((s>>(j+1))<<j)
def marginal(p,j):
 q={}
 for s,w in p.items():u=drop(s,j);q[u]=q.get(u,F(0))+w
 return q
def step(t,coords,q,coord):
 global NODES
 NODES+=1;j=coords.index(coord);cc=tuple(x for x in coords if x!=coord)
 p,_=spec(t);pe=marginal(p,j);qe=marginal(q,j);ts=[restrict(t,j,b) for b in [0,1]];ps=[spec(z)[0] for z in ts]
 ck(sum(q.values())==1)
 for s in set(pe)|set(ps[0])|set(ps[1]):ck(pe.get(s,F(0))==(ps[0].get(s,F(0))+ps[1].get(s,F(0)))/2)
 joints=[{s:w*(ps[b].get(s,F(0))/(2*pe[s]) if pe.get(s,F(0)) else F(1,2)) for s,w in qe.items()} for b in [0,1]]
 qb=[sum(z.values()) for z in joints];ck(sum(qb)==1 and min(qb)>0)
 qs=[{s:w/qb[b] for s,w in joints[b].items() if w} for b in [0,1]]
 for s,pv in p.items():
  u=drop(s,j);er=(pv/pe[u])/(q[s]/qe[u])
  for b in [0,1]:
   if ps[b].get(u,F(0)):ck(pv/q[s]==er*(F(1,2)/qb[b])*(ps[b][u]/qs[b][u]))
 # Exact likelihood products above establish the chain rule, not interval overlap.
 E=add(kl(p,q),scale(kl(pe,qe),-1));O=kl({0:F(1,2),1:F(1,2)},{0:qb[0],1:qb[1]})
 nonnegative(E);nonnegative(O)
 return ts,cc,qs,E,O
def core(z,m,r):
 a=1
 for j in range(m):
  if (z>>(j*r))&((1<<r)-1)==(1<<r)-1:a=-a
 return a
def table(m,r):return tuple(1-2*((u>>1)&1) if not u&1 else core(u>>3,m,r) if u&4 else 1 for u in range(1<<(3+m*r)))
def factor_ref(w,alpha):
 if w==0:return {0:F(1)}
 if w==1:return {1:F(1)}
 d=F(1,1<<w);v=4*d*(1-d);p0=(1-2*d)**2
 return {s:p0 if not s else (1-alpha)*4*d*d+(alpha*v if s==(1<<w)-1 else 0) for s in range(1<<w)}
def fresh_core(t,coords,m,r,alpha):
 # Discover surviving block widths from the actual restricted truth table.
 p,_=spec(t);q={0:F(1)}
 for b in range(m):
  positions=[j for j,c in enumerate(coords) if 3+b*r<=c<3+(b+1)*r]
  blockmask=sum(1<<j for j in positions)
  marginal_p={}
  for s,w in p.items():u=s&blockmask;marginal_p[u]=marginal_p.get(u,F(0))+w
  w=len(positions)
  # An already killed block is constant, detectable by its spectral marginal.
  if marginal_p.get(0,F(0))==1:ref={0:F(1)}
  else:ref={sum(1<<j for k,j in enumerate(positions) if s>>k&1):v for s,v in factor_ref(w,alpha).items()}
  q={s|u:pv*qv for s,pv in q.items() for u,qv in ref.items()}
 ck(sum(q.values())==1)
 return q
def root_ref(m,r):
 n=m*r;delta=F(1,1<<r);mu=(1-2*delta)**m;qcore={0:F(1)}
 for b in range(m):qcore={s|(u<<(b*r)):w*v for s,w in qcore.items() for u,v in factor_ref(r,F(1,8)).items()}
 q={2:F(1,4),3:F(1,4),0:(1+mu)**2/16,1:(1+mu)**2/16,4:(1-mu)**2/16,5:(1-mu)**2/16}
 for s,w in qcore.items():
  if s:
   for control in [0,1,4,5]:q[(s<<3)|control]=w/16
 ck(sum(q.values())==1);return q
def node(t,cc,q,w):return dict(t=t,cc=cc,q=q,w=w)
def query(n,c):
 global DEBITS
 ts,cc,qs,E,O=step(n['t'],n['cc'],n['q'],c)
 DEBITS=add(DEBITS,scale(add(E,O),n['w']))
 return [node(t,cc,q,n['w']/2) for t,q in zip(ts,qs)]
def totals(leaves):
 H={};I=F(0);K={}
 for n in leaves:
  p,i=spec(n['t']);H=add(H,scale(ent(p),n['w']));I+=n['w']*i;K=add(K,scale(kl(p,n['q']),n['w']))
 return H,I,K
def run(m,r,prefix):
 global DEBITS
 DEBITS={}
 t=table(m,r);cc=tuple(range(3+m*r));q=root_ref(m,r);p,I0=spec(t);H0=ent(p);A0=kl(p,q)
 kids=query(node(t,cc,q,F(1)),2);leaves=[kids[0]];active=[kids[1]]
 if prefix:active=query(active[0],3)
 for n in active:
  xp=query(n,0);leaves.extend(xp)
 Kold=totals(leaves)[2]
 # The ACTUAL strong reset from A036 is paid once here.
 for n in leaves:
  if 0 not in n['cc'] and n is not kids[0]:
   pp,_=spec(n['t'])
   if all(c==1 or c>=3 for c in n['cc']):
    # x0 character vs x1 core detected by a influence.
    aj=n['cc'].index(1)
    if any(s>>aj&1 for s in pp):n['q']=pp.copy()
    else:n['q']=fresh_core(n['t'],n['cc'],m,r,F(1,6))
 Kfirst=totals(leaves)[2];sigma1=add(Kfirst,scale(Kold,-1))
 future={};transactions=0;generation=0
 while True:
  new=[];changed=False
  for n in leaves:
   pp,_=spec(n['t']);choices=[c for j,c in enumerate(n['cc']) if c>=3 and any(s>>j&1 for s in pp)]
   # Only x-exposed core descendants, never b0 or x0 character terminals.
   if 0 in n['cc'] or not choices:new.append(n);continue
   changed=True;kk=query(n,choices[0]);old=totals(kk)[2]
   for child in kk:child['q']=fresh_core(child['t'],child['cc'],m,r,F(1,6))
   fresh=totals(kk)[2];sig=add(fresh,scale(old,-1));bb=bounds(sig)
   ck(not sig or bb[1]<=0);future=add(future,sig);transactions+=1;new.extend(kk)
  leaves=new;Hf,If,Kf=totals(leaves)
  edge=add(H0,scale(Hf,-1),{2:-4*(I0-If)})
  net=add(A0,edge,sigma1,future);nb=bounds(net);S=add({2:4*If},scale(Hf,-1));sb=bounds(S)
  remainder=sb[0]-max(F(0),nb[1])-F(1,4)
  ck(remainder>=F(3,4));ck(sb[0]>=2)
  if not changed:break
  generation+=1
 ck(sum(n['w'] for n in leaves)==1)
 difference=add(A0,sigma1,future,scale(DEBITS,-1),scale(Kf,-1));bb=bounds(difference)
 ck(bb[0]<=0<=bb[1] and bb[1]-bb[0]<F(1,1<<80))
 delta=F(1,1<<r);tau=(1-(1-2*delta)**m)/2
 M0=add({2:4*I0},scale(H0,-1),scale(A0,-1))
 ck(bounds(M0)[0]>1+2*tau+F(3,10)*m*delta)
 ck(bounds(sigma1)[1]<F(11,40)*m*delta)
 row={'m':m,'r':r,'prefix':prefix,'first_actual_sigma_interval':list(map(str,bounds(sigma1))),'cumulative_extra_sigma_interval':list(map(str,bounds(future))),'reset_transactions':transactions,'data_generations':generation,'complete_terminal_count':len(leaves),'final_S_interval':list(map(str,sb)),'signed_net_interval':list(map(str,nb)),'old_booking':'1/4','remaining_lower':str(remainder),'all_terminals_retained':True,'full_erasure_outcome_bill_interval':list(map(str,bounds(DEBITS))),'full_terminal_KL_interval':list(map(str,bounds(Kf))),'source_plus_resets_interval':list(map(str,bounds(add(A0,sigma1,future)))),'source_chain_check':'atomwise exact query identities plus algebraic reset telescoping; interval overlap only diagnostic'}
 save(f'CASE_m{m}_r{r}_p{prefix}.json',row);return row
def scalars():
 for w in range(2,33):
  d=F(1,1<<w);E=1-4*d+8*d*d;eta=2*d*d/(3*E);u=(1-4*d)**2;B=d/(1+8*d)
  v=add(scale(lv(1+eta),-1),scale(lv(1-eta),u),scale(lv(1+B),16*d*d))
  if w==2:ck(not v)
  else:ck(bounds(v)[1]<0)
 ck(-F(128,301)-F(1,12)+F(1,2)==-F(31,3612))
 ck(8**5<2*7**5 and 6**40<2**11*5**40 and LN2[0]>F(2,3))
cases=[(1,3,0)] if '--pilot' in sys.argv else [(1,2,0),(1,3,0),(1,4,1),(2,2,1),(2,3,1)]
(ROOT/'out').mkdir(exist_ok=True)
rows=[run(*c) for c in cases];scalars()
result={'status':'PASS','cases':len(rows),'assertions':COUNT,'physical_nodes':NODES,'runtime_seconds':time.perf_counter()-START,'max_dimension':max(3+m*r for m,r,p in cases),'post_reset_transactions':sum(x['reset_transactions'] for x in rows),'rung':'analytic proof with exact checks; independent review pending','rows':rows}
save('PILOT.json' if '--pilot' in sys.argv else 'CHECK.json',result);print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
