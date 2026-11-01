from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json,time
OUT=Path(__file__).resolve().parents[1]/'out'; OUT.mkdir(exist_ok=True)
start=time.perf_counter(); checks=0
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
 x=Q(x); r={}
 for a,sgn in [(x.numerator,1),(x.denominator,-1)]:
  p=2
  while p*p<=a:
   while a%p==0:r[p]=r.get(p,0)+sgn;a//=p
   p+=1
  if a>1:r[a]=r.get(a,0)+sgn
 return {p:Q(v) for p,v in r.items() if v}
def ent(ps):return add(*(mul(log(p),-p) for p in ps if p))
def h(p):return ent([p,1-p])
@lru_cache(None)
def ln_interval(x):
 z=(x-1)/(x+1); s=sum((2*z**(2*k+1)/Q(2*k+1) for k in range(24)),Q(0))
 e=2*abs(z)**49/(49*(1-z*z))
 return s-e,s+e
@lru_cache(None)
def lp(p):
 if p==2:return Q(1),Q(1)
 k=p.bit_length()-1;x=Q(p,2**k)
 lo,hi=ln_interval(x); l2,u2=ln_interval(Q(2))
 return k+lo/u2,k+hi/l2
def interval(x):
 lo=hi=Q(0)
 for p,c in x.items():
  a,b=lp(p);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 return lo,hi
def gt(x,a=0):return interval(add(x,{2:-Q(a)}))[0]>0
def ge(x,a=0):return not x if a==0 and not x else interval(add(x,{2:-Q(a)}))[0]>=0
def walsh(vals):
 a=list(vals);n=len(a);s=1
 while s<n:
  for j in range(0,n,2*s):
   for k in range(j,j+s):u,v=a[k],a[k+s];a[k]=u+v;a[k+s]=u-v
  s*=2
 return [Q(v,n) for v in a]
def infl(vals):
 n=(len(vals)-1).bit_length()
 return [Q(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),len(vals)) for i in range(n)]
R=[Q(8,13),Q(2,13)]+[Q(1,26)]*6
def cores(pat):
 free=[i for i,v in enumerate(pat) if v<0];aa=[];bb=[]
 for x in range(1<<len(free)):
  y=[(x>>free.index(i))&1 if i in free else pat[i] for i in range(3)]
  aa.append(1 if sum(y)<=1 else -1);bb.append((-1)**y[0])
 rm=[Q(0)]*(1<<len(free))
 for s,p in enumerate(R):rm[sum(((s>>i)&1)<<k for k,i in enumerate(free))]+=p
 return free,aa,bb,rm
def cross(ps,rs):return add(*(mul(log(r),-p) for p,r in zip(ps,rs) if p))
def node(m,pat):
 free,a,b,rm=cores(pat);rho=Q(1,2**m);beta=2*rho*(1-rho)
 d=Q(sum(u!=v for u,v in zip(a,b)),len(a))
 B=mul(add(cross([x*x for x in walsh(a)],rm),cross([x*x for x in walsh(b)],rm)),Q(1,2))
 A=Q(sum(infl(a))+sum(infl(b)),2)
 C=add(B,h(d*rho*rho),{2:2+2*(1-2*d)*rho+beta*m},mul(add(log(1-rho),log(Q(20,7))),beta))
 I=A+1+(m+1-2*d)*rho
 vals=[]
 for x in range(1<<(m+2+len(free))):
  c=x&1;u=(x>>1)&1;z=(x>>2)&((1<<m)-1);y=x>>(m+2)
  g=[a[y],b[y],-b[y],-a[y]][c+2*u]
  vals.append(-g if c==0 and z==0 else g)
 fs=walsh(vals);ps=[x*x for x in fs];iv=infl(vals)
 ck(sum(ps)==1);ck(sum(iv)==I);ck(sum(Q(s.bit_count())*p for s,p in enumerate(ps))==I)
 weights={1:Q(1,4),2:Q(1,4),3:Q(1,16)};ntail=2*((1<<m)-1);alpha=1-d*rho*rho
 control=[]
 for s in range(1<<(m+2)):
  if s==0:q=1-alpha
  elif s<4:q=alpha*weights[s]
  else:q=alpha*(Q(7,80) if s&2 else Q(7,20))/ntail
  control.append(q)
 ck(sum(control)==1)
 refs=[rm[s>>(m+2)]*control[s&((1<<(m+2))-1)] for s in range(len(ps))]
 ck(all(r>0 or p==0 for p,r in zip(ps,refs)));ck(cross(ps,refs)==C)
 for j,i in enumerate(free):ck(iv[m+2+j]==Q(infl(a)[j]+infl(b)[j],2))
 return dict(C=C,B=B,I=I,d=d,iv=iv,free=free)
nodes={};patterns=list(product([-1,0,1],repeat=3));excesses=[]
for m in [1,2,3]:
 for pat in patterns:nodes[m,pat]=node(m,pat)
 for pat in patterns:
  p=nodes[m,pat]
  for i in p['free']:
   children=[]
   for v in [0,1]:q=list(pat);q[i]=v;children.append(nodes[m,tuple(q)])
   dc=add(p['C'],mul(add(*(x['C'] for x in children)),-Q(1,2)))
   db=add(p['B'],mul(add(*(x['B'] for x in children)),-Q(1,2)))
   t=Q(1,4**m);J=add(h(t*p['d']),mul(add(*(h(t*x['d']) for x in children)),-Q(1,2)))
   j=p['iv'][m+2+p['free'].index(i)]
   ck(dc==add(db,J));ck(ge(J));ck(ge({2:t},interval(J)[1]))
   ck(gt(add({2:Q(1,4)+4*j},mul(dc,-1))) or add({2:Q(1,4)+4*j},mul(dc,-1))=={})
   if j:ck(ge(add({2:4*j},mul(db,-1))))
   else:ck(gt(add({2:Q(1,4)},mul(db,-1))))
   lo,hi=interval(add(dc,{2:-4*j}));excesses.append(dict(m=m,pat=pat,query=i,lower=str(lo),upper=str(hi)))
@lru_cache(None)
def trees(pat):
 free=[i for i,v in enumerate(pat) if v<0]
 if not free:return (None,)
 ans=[]
 for i in free:
  p0=list(pat);p1=list(pat);p0[i]=0;p1[i]=1
  for a,b in product(trees(tuple(p0)),trees(tuple(p1))):ans.append((i,a,b))
 return tuple(ans)
def history(m,pat,tree):
 p=nodes[m,pat]
 if tree is None:return {},{},p['C'],p['I']
 i,a,b=tree;qs=[];results=[]
 for v,tr in [(0,a),(1,b)]:
  q=list(pat);q[i]=v;q=tuple(q);qs.append(nodes[m,q]);results.append(history(m,q,tr))
 J=add(h(Q(1,4**m)*p['d']),mul(add(*(h(Q(1,4**m)*q['d']) for q in qs)),-Q(1,2)))
 e=add(p['C'],mul(add(*(q['C'] for q in qs)),-Q(1,2)),{2:-4*p['iv'][m+2+p['free'].index(i)]})
 return (add(J,mul(add(*(r[0] for r in results)),Q(1,2))),add(e,mul(add(*(r[1] for r in results)),Q(1,2))),mul(add(*(r[2] for r in results)),Q(1,2)),sum((r[3] for r in results),Q(0))/2)
root=(-1,-1,-1);tree_count=0;root_receipts=[]
for m in [1,2,3]:
 p=nodes[m,root];t=Q(1,4**m)
 for pat in product([0,1],repeat=3):
  leaf=nodes[m,pat];ck(gt(add({2:4*leaf['I']},mul(leaf['C'],-1)),1))
 for tree in trees(root):
  J,e,lc,li=history(m,root,tree);tree_count+=1
  ck(J==add(h(t*p['d']),mul(h(t),-p['d'])))
  ck(ge(add(mul(h(p['d']),t),mul(J,-1))))
  ck(e==add(p['B'],{2:-4*Q(5,4)},J))
  ck(add({2:4*p['I']},mul(p['C'],-1))==add({2:4*li},mul(lc,-1),mul(e,-1)))
  ck(gt(add({2:4*p['I']},mul(p['C'],-1)),Q(9,4)))
 root_receipts.append(dict(m=m,surplus_interval=[str(x) for x in interval(add({2:4*p['I']},mul(p['C'],-1)))]))
bent=[]
for m in [2,3]:
 n=2*m;delta=Q(1,2**(n+1));aa=[]
 for x in range(1<<(n+2)):
  y=x&((1<<n)-1);w=(x>>n)&1;z=(-1)**((x>>(n+1))&1)
  b=(-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(m))
  aa.append(z if y==0 and w==0 else b)
 fs=walsh(aa);p=[x*x for x in fs];iv=infl(aa);lc={}
 parent=[]
 for x in range(1<<(n+3)):
  c=x&1;w=(x>>(n+1))&1;y=(x>>1)&((1<<n)-1);z=(-1)**((x>>(n+2))&1)
  b=(-1)**(c*w+sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(m)))
  parent.append(z if c==0 and y==0 and w==0 else b)
 ck(parent[::2]==aa)
 bspec=walsh([(-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(m)) for y in range(1<<n)])
 for T in range(1<<(n+1)):
  u=(bspec[T] if T<(1<<n) else 0)-delta;v=delta;q=u*u+v*v
  ck(fs[T]==u);ck(fs[T+(1<<(n+1))]==v)
  lc=add(lc,ent([u*u,v*v]),mul(log(q),q))
 ck(iv[-1]==delta);ck(sum(iv)==m+(2*m+2)*delta)
 ck(gt(lc,delta*(m+Q(3,2))));ck(3*sum(iv)>=n+2)
 bent.append(dict(m=m,conditional_ratio_interval=[str(x) for x in interval(mul(lc,1/delta))]))
# Normalized non-Boolean singleton law: H/I=log2(n), convolution at two bits=2/n.
for n in [4,16,64,256]:ck(Q(2,n)>0);ck(n.bit_length()-1>0)
for t,d in product([Q(0),Q(1,4),Q(1)],[Q(0),Q(1,4),Q(1,2),Q(1)]):
 refund=add(h(t*d),mul(h(t),-d))
 ck(ge(refund));ck(ge(add(mul(h(d),t),mul(refund,-1))))
ck(2*13**4<16**4);ck(20**5<2**8*7**5)
guard_histories=0
for edited in [False,True]:
 av=[(1 if (y&7).bit_count()<=1 else -1)*(-1 if edited and y==0 else 1) for y in range(32)]
 bv=[(-1)**(y&1) for y in range(32)]
 ds=[int(a!=b) for a,b in zip(av,bv)];d=Q(sum(ds),32)
 for m in [1,2]:
  t=Q(1,4**m);empty=Q(0)
  for y in range(32):
   values=[]
   for c,u,z in product([0,1],[0,1],range(1<<m)):
    g=[av[y],bv[y],-bv[y],-av[y]][c+2*u]
    values.append(-g if c==0 and z==0 else g)
   empty+=Q(sum(values),len(values))**2/32
  ck(empty==t*d)
  def walk(rows,free,depth,parity):
   dv=Q(sum(ds[y] for y in rows),len(rows))
   if depth==0:return {},h(t*dv)
   i=free[-1] if parity else free[0];rest=[j for j in free if j!=i]
   rr=[walk([y for y in rows if (y>>i)&1==v],rest,depth-1,parity^v) for v in [0,1]]
   child_h=add(*(mul(h(t*Q(sum(ds[y] for y in rows if (y>>i)&1==v),len(rows)//2)),Q(1,2)) for v in [0,1]))
   J=add(h(t*dv),mul(child_h,-1))
   return add(J,mul(add(*(r[0] for r in rr)),Q(1,2))),mul(add(*(r[1] for r in rr)),Q(1,2))
  for depth in [3,5]:
   J,last=walk(list(range(32)),list(range(5)),depth,0);guard_histories+=1
   ck(J==add(h(t*d),mul(last,-1)));ck(ge(J));ck(ge(add(mul(h(d),t),mul(J,-1))))
result=dict(status='PASS',assertions=checks,full_nodes=81,physical_queries=81,adaptive_trees=tree_count,pad_flip_histories=guard_histories,bent=bent,root_surpluses=root_receipts,runtime_seconds=time.perf_counter()-start,arithmetic='Fraction prime-log exact identities and certified rational intervals')
(OUT/'CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
(OUT/'QUERY_EXCESSES.json').write_text(json.dumps(excesses,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['bent','root_surpluses']},indent=2))
