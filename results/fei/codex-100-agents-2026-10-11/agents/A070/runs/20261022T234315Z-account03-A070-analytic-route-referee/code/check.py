from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json,time
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';OUT.mkdir(exist_ok=True)
start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
def add(*xs):
 r={}
 for x in xs:
  for p,c in x.items():r[p]=r.get(p,Q(0))+c
 return {p:c for p,c in r.items() if c}
def mul(x,c):return {p:v*c for p,v in x.items() if v*c}
@lru_cache(None)
def log(x):
 x=Q(x);r={}
 for a,sgn in [(x.numerator,1),(x.denominator,-1)]:
  p=2
  while p*p<=a:
   while a%p==0:r[p]=r.get(p,0)+sgn;a//=p
   p+=1
  if a>1:r[a]=r.get(a,0)+sgn
 return {p:Q(c) for p,c in r.items() if c}
def h(p):return add(*(mul(log(q),-q) for q in [p,1-p] if q))
def ce(ps,rs):return add(*(mul(log(r),-p) for p,r in zip(ps,rs) if p))
def ln(x):
 z=(x-1)/(x+1);s=sum((2*z**(2*k+1)/Q(2*k+1) for k in range(24)),Q(0));e=2*abs(z)**49/(49*(1-z*z))
 return s-e,s+e
def floor(x):return x.numerator//x.denominator
@lru_cache(None)
def lp(p):
 if p==2:return Q(1),Q(1)
 k=p.bit_length()-1;a,b=ln(Q(p,2**k));l,u=ln(Q(2));scale=2**90
 lo=k+a/u;hi=k+b/l
 return Q(floor(lo*scale),scale),Q(-floor(-hi*scale),scale)
def iv(x):
 lo=hi=Q(0)
 for p,c in x.items():
  a,b=lp(p);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 return lo,hi
def gt(x,a=0):return iv(add(x,{2:-Q(a)}))[0]>0
def ge(x):return not x or iv(x)[0]>=0
def pos(x):
 if not x:return {}
 lo,hi=iv(x);ck(lo>0 or hi<0)
 return x if lo>0 else {}
def walsh(vals):
 a=list(vals);s=1;n=len(a)
 while s<n:
  for j in range(0,n,2*s):
   for k in range(j,j+s):u,v=a[k],a[k+s];a[k]=u+v;a[k+s]=u-v
  s*=2
 return [Q(v,n) for v in a]
def influence(vals):
 return [Q(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),len(vals)) for i in range((len(vals)-1).bit_length())]
def majority(bits):return 1 if sum(bits)>0 else -1
aa=[]
for y in range(512):aa.append(majority([majority([(-1)**((y>>i)&1) for i in range(j,j+3)]) for j in [0,3,6]]))
bb=list(aa);bb[0]*=-1
R=[]
for s in range(512):
 L=1+3*(int(s!=0)+sum(bool(s&(7<<j)) for j in [0,3,6]))
 R.append(Q(1,2**L))
Z=sum(R);ck(Z==Q(6959,8192));R=[r/Z for r in R]
refs={d:[sum((R[(s<<d)|v] for v in range(1<<d)),Q(0)) for s in range(1<<(9-d))] for d in range(10)}
nodes={}
for depth in range(10):
 for prefix in range(1<<depth):
  a=[aa[prefix+(y<<depth)] for y in range(1<<(9-depth))];b=[bb[prefix+(y<<depth)] for y in range(1<<(9-depth))]
  fa=walsh(a);fb=walsh(b);ps=[(u*u+v*v)/2 for u,v in zip(fa,fb)]
  ia,ib=influence(a),influence(b);A=sum((Q(x+y,2) for x,y in zip(ia,ib)),Q(0))
  ck(sum(ps)==1);ck(sum((s.bit_count()*p for s,p in enumerate(ps)),Q(0))==A)
  B=ce(ps,refs[depth]);dv=Q(sum(x!=y for x,y in zip(a,b)),len(a))
  nodes[depth,prefix]=dict(A=A,B=B,d=dv,j=Q(ia[0]+ib[0],2) if depth<9 else 0)
P={};signed={};queries=[]
for depth in range(9):
 for prefix in range(1<<depth):
  p=nodes[depth,prefix];cs=[nodes[depth+1,prefix+(v<<depth)] for v in [0,1]]
  ck(p['A']==p['j']+(cs[0]['A']+cs[1]['A'])/2);ck(p['d']==(cs[0]['d']+cs[1]['d'])/2)
  db=add(p['B'],mul(add(*(c['B'] for c in cs)),-Q(1,2)))
  e=add(db,{2:-4*p['j']});positive=pos(e);weight=Q(1,2**depth)
  P=add(P,mul(positive,weight));signed=add(signed,mul(e,weight))
  queries.append(dict(depth=depth,prefix=prefix,j=str(p['j']),e_interval=[str(x) for x in iv(e)],child_A=[str(c['A']) for c in cs]))
ck(gt(add({2:Q(7,12)},mul(P,-1))));ck(gt(add({2:Q(1,32)},mul(h(Q(1,512)),-1))))
ck(signed==add(nodes[0,0]['B'],{2:-4*nodes[0,0]['A']}))
for v in [0,1]:ck(gt(add({2:4*nodes[1,v]['A']},mul(nodes[1,v]['B'],-1)),Q(1,2)))
for depth in [0,2,5]:
 row=next(r for r in queries if r['depth']==depth and r['prefix']==0)
 ck(Q(row['e_interval'][0])>0);ck(Q(row['j'])>0)
 if depth<5:ck(all(Q(x)>0 for x in row['child_A']))
(OUT/'CORE_CHECKPOINT.json').write_text(json.dumps(dict(status='CORE_PASS',P_core_interval=[str(x) for x in iv(P)],core_assertions=checks),indent=2),encoding='utf-8')
# Terminal full-control reference. Q is marginalized, never reconstructed,
# after either actual physical c/u query.
control=[];l=log(Q(5,4));extra_u={};extra_c={}
for m,d in product(range(1,7),[0,1]):
 rho=Q(1,2**m);t=rho*rho;beta=2*rho*(1-rho);alpha=1-t*d;N=2*((1<<m)-1)
 qr=[]
 for s in range(1<<(m+2)):
  if s==0:q=1-alpha
  elif s<4:q=alpha*{1:Q(1,4),2:Q(1,4),3:Q(1,16)}[s]
  else:q=alpha*(Q(7,80) if s&2 else Q(7,20))/N
  qr.append(q)
 vals=[]
 for x in range(1<<(m+2)):
  c=x&1;u=(x>>1)&1;z=x>>2
  g=(-1)**(c if d else u)
  vals.append(-g if c==0 and z==0 else g)
 f=walsh(vals);ps=[x*x for x in f];inf=influence(vals);C=ce(ps,qr)
 ck(sum(qr)==1);ck(all(q>0 or p==0 for p,q in zip(ps,qr)))
 I=1+(m+1-2*d)*rho;ck(sum(inf)==I)
 formula=add(h(t*d),{2:2+2*(1-2*d)*rho+beta*m},mul(add(log(1-rho),log(Q(20,7))),beta))
 ck(C==formula);ck(gt(add({2:4*I},mul(C,-1)),1))
 for bit,name in [(0,'c'),(1,'u')]:
  def omit(x):return (x&((1<<bit)-1))|((x>>(bit+1))<<bit)
  rchild=[Q(0)]*(len(qr)//2)
  for s,q in enumerate(qr):rchild[omit(s)]+=q
  children=[[v for x,v in enumerate(vals) if (x>>bit)&1==j] for j in [0,1]]
  pcs=[[v*v for v in walsh(a)] for a in children]
  cc=mul(add(*(ce(p,rchild) for p in pcs)),Q(1,2));dc=add(C,mul(cc,-1));e=add(dc,{2:-4*inf[bit]})
  ck(sum(rchild)==1);ck(sum(inf)==inf[bit]+sum((sum(influence(a)) for a in children),Q(0))/2)
  if name=='u':ck(all(sum(influence(a))>0 for a in children))
  if name=='u':
   expected=mul(log(Q(5)),2*rho-t) if d==0 else add(mul(log((1+3*t)/(4*t)),t),mul(l,1-t))
   if d==0:ck(gt(mul(e,-1)))
   else:ck(gt({2:1},iv(e)[1]))
  else:
   expected=add(mul(l,1-2*rho+2*t),{2:2*rho}) if d==0 else add(mul(log((1+3*t)/(4*t)),t),mul(log((1+3*t)/(1-t)),(1-rho)**2),{2:beta})
   if d==1:ck(gt(mul(e,-1)))
  ck(dc==expected)
  (extra_u if name=='u' else extra_c)[m,d]=pos(e)
 control.append(dict(m=m,d=d))
continuation=[]
for m in range(1,7):
 t=Q(1,4**m);old_bound=add(P,mul(h(Q(1,512)),t))
 pu=add(*(mul(extra_u[m,d],Q(511 if d==0 else 1,512)) for d in [0,1]))
 pc=add(*(mul(extra_c[m,d],Q(511 if d==0 else 1,512)) for d in [0,1]))
 # Exact flag increments along this fixed tree, not an upper refund reset.
 pcomplete={}
 for depth in range(9):
  for prefix in range(1<<depth):
   p=nodes[depth,prefix];cs=[nodes[depth+1,prefix+(v<<depth)] for v in [0,1]]
   J=add(h(t*p['d']),mul(add(*(h(t*c['d']) for c in cs)),-Q(1,2)))
   db=add(p['B'],mul(add(*(c['B'] for c in cs)),-Q(1,2)))
   pcomplete=add(pcomplete,mul(pos(add(db,J,{2:-4*p['j']})),Q(1,2**depth)))
 ck(gt(add({2:Q(3,5)},mul(pcomplete,-1))))
 ck(gt(add({2:Q(5,8)},mul(add(pcomplete,pu),-1)),Q(59,2560)))
 continuation.append(dict(m=m,core_and_flag_interval=[str(x) for x in iv(pcomplete)],u_total_interval=[str(x) for x in iv(add(pcomplete,pu))],c_total_interval=[str(x) for x in iv(add(pcomplete,pc))]))
ck(Q(5,8)-Q(3,5)-Q(1,512)==Q(59,2560))
# Actual cost P alone gives a lower bound on old complete query spending.
obstruction=add(P,mul(l,Q(511,512)),{2:-Q(5,8)})
ck(gt(obstruction))
ck(25<32) # log2(5/4)<1/2
res=dict(status='PASS',assertions=checks,core_nodes=1023,core_queries=511,control_functions=12,control_queries=24,P_core_interval=[str(x) for x in iv(P)],limiting_c_bank_excess_interval=[str(x) for x in iv(obstruction)],continuation=continuation,runtime_seconds=time.perf_counter()-start,arithmetic='Integer Walsh/direct pivots; Fraction prime-log identities and certified24-term atanh intervals')
(OUT/'CHECK.json').write_text(json.dumps(res,indent=2),encoding='utf-8')
(OUT/'QUERY_ROWS.json').write_text(json.dumps(queries,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in res.items() if k not in ['continuation','P_core_interval','limiting_c_bank_excess_interval']},indent=2))
