from pathlib import Path
from fractions import Fraction as R
from itertools import product
from functools import lru_cache
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(t):
 global checks
 checks+=1
 assert t,checks
 assert time.monotonic()-start<55,'55s guard'
def fw(a):
 a=list(a);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for i in range(j,j+h):
    x,y=a[i],a[i+h];a[i],a[i+h]=x+y,x-y
  h*=2
 return a
def fac(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def add(*terms):
 d={}
 for a,b in terms:
  for p,v in b.items():d[p]=d.get(p,R(0))+a*v
 return {p:v for p,v in d.items() if v}
def log(q):
 q=R(q);assert q>0
 return add((1,fac(q.numerator)),(-1,fac(q.denominator)))
def h2(q):
 return add(*[(-v,log(v)) for v in (q,1-q) if v])
def ln_unit(q):
 z=(q-1)/(q+1)
 lo=2*sum((z**(2*j+1)/R(2*j+1) for j in range(24)),R(0))
 return lo,lo+2*z**49/(49*(1-z*z))
LN2=ln_unit(R(2))
@lru_cache(None)
def interval_log(q):
 q=R(q);k=0
 while q<1:q*=2;k-=1
 while q>=2:q/=2;k+=1
 lo,hi=ln_unit(q)
 return R(k)+lo/LN2[1],R(k)+hi/LN2[0]
def interval(expr):
 lo=hi=R(0)
 for p,w in expr.items():
  a,b=interval_log(p)
  lo+=w*(a if w>=0 else b);hi+=w*(b if w>=0 else a)
 return lo,hi
def fmt(x):return str(x)
BASE=[R(8,13),R(2,13)]+[R(1,26)]*6
@lru_cache(None)
def coredata(pat):
 free=[i for i,v in enumerate(pat) if v==2]
 aa=[];bb=[]
 for x in range(1<<len(free)):
  y=[pat[i] if pat[i]!=2 else ((x>>free.index(i))&1) for i in range(3)]
  s=[2*v-1 for v in y];aa.append(1 if sum(s)>0 else -1);bb.append(s[0])
 n=len(aa);P=[[R(v*v,n*n) for v in fw(a)] for a in [aa,bb]]
 ry=[R(0)]*n
 for s,r in enumerate(BASE):ry[sum(((s>>i)&1)<<j for j,i in enumerate(free))]+=r
 B=add(*[(-p/2,log(ry[t])) for ps in P for t,p in enumerate(ps) if p])
 inf=[sum(p for ps in P for t,p in enumerate(ps) if (t>>j)&1)/2 for j in range(len(free))]
 d=R(sum(a!=b for a,b in zip(aa,bb)),n)
 return {'free':free,'a':aa,'b':bb,'B':B,'inf':inf,'A':sum(inf),'d':d,'R':ry}
def formula(pat,m):
 d=coredata(pat);r=R(1,1<<m);beta=2*r*(1-r)
 I=d['A']+1+(m+1-2*d['d'])*r
 C=add((1,d['B']),(1,h2(d['d']*r*r)),(2+2*(1-2*d['d'])*r,log(2)),(beta,log((1-r)/r*R(20,7))))
 return I,C
patterns=list(product(range(3),repeat=3));queryrows=[];fullnodes=fullqueries=0
for pat in patterns:
 p=coredata(pat);ck(sum(p['R'])==1)
 for j,i in enumerate(p['free']):
  cs=[]
  for b in (0,1):
   q=list(pat);q[i]=b;cs.append(coredata(tuple(q)))
  delta=add((1,p['B']),(-R(1,2),cs[0]['B']),(-R(1,2),cs[1]['B']))
  lo,hi=interval(delta);inf=p['inf'][j]
  ck(p['d']==(cs[0]['d']+cs[1]['d'])/2)
  if inf:ck(hi<=4*inf)
  else:ck(hi<R(1,4));ck(cs[0]['d']==p['d']==cs[1]['d'])
  queryrows.append({'pattern':pat,'query':i,'Inf':str(inf),'delta_core_interval':[str(lo),str(hi)]})
 for m in (1,2,3):
  free=p['free'];D=m+2;tab=[]
  for x in range(1<<(D+len(free))):
   c=x&1;u=(x>>1)&1;z=(x>>2)&((1<<m)-1);y=x>>D
   v=[p['a'][y],p['b'][y],-p['b'][y],-p['a'][y]][c+2*u]
   tab.append(v*(-1 if c==0 and z==0 else 1))
  N=len(tab);P=[R(v*v,N*N) for v in fw(tab)];mask=(1<<D)-1
  inf=[sum(q for s,q in enumerate(P) if (s>>i)&1) for i in range(D+len(free))]
  # Independently compare pivotal counts with every spectral influence.
  for i,ii in enumerate(inf):ck(ii==R(sum(tab[x]!=tab[x^(1<<i)] for x in range(N)),N))
  alpha=sum(q for s,q in enumerate(P) if s&mask);r=R(1,1<<m)
  ck(alpha==1-p['d']*r*r);ck(sum(inf[2:D])==m*r)
  ck(sum(inf[:2])==1+(1-2*p['d'])*r)
  tail=[R(0)]*(1<<D);tail[1]=tail[2]=R(1,4);tail[3]=R(1,16)
  cellsz=2*((1<<m)-1)
  for s in range(4,1<<D):tail[s]=(R(7,80) if s&2 else R(7,20))/cellsz
  ck(sum(tail)==1)
  ce={}
  for s,q in enumerate(P):
   if q:
    ss=s&mask;rd=(1-alpha) if not ss else alpha*tail[ss]
    ce=add((1,ce),(-q,log(p['R'][s>>D]*rd)))
  I,C=formula(pat,m);ck(I==sum(inf));ck(C==ce);fullnodes+=1
  for j,i in enumerate(free):
   cis=[];ccs=[]
   for b in (0,1):
    ch=list(pat);ch[i]=b;ic,cc=formula(tuple(ch),m);cis.append(ic);ccs.append(cc)
   ck(I==p['inf'][j]+sum(cis)/2)
   delta=add((1,C),(-R(1,2),ccs[0]),(-R(1,2),ccs[1]))
   lo,hi=interval(delta);ck(hi-4*p['inf'][j]<R(1,4))
   fullqueries+=1
boundary=[]
for d in (0,1):
 pat=(0,0,0) if d==0 else (1,0,0)
 ck(coredata(pat)['d']==d)
 for m in (1,2):
  I,C=formula(pat,m);lo,hi=interval(C);ck(4*I-hi>1)
  boundary.append({'d':d,'m':m,'surplus_lower':str(4*I-hi)})
ck(20**5<2**8*7**5)
# Relevant second query after Y1=0: both core terminal pairs nonconstant.
pat=(2,0,2);p=coredata(pat);I,C=formula(pat,1);cs=[]
for b in (0,1):
 q=(2,0,b);ck(coredata(q)['A']>0);cs.append(formula(q,1)[1])
delta=add((1,C),(-R(1,2),cs[0]),(-R(1,2),cs[1]))
lo,hi=interval(delta);j=p['free'].index(2);exlo=lo-4*p['inf'][j];exhi=hi-4*p['inf'][j]
ck(exlo>R(1,100));ck(exhi<R(1,40))
ck(len(queryrows)==27 and fullnodes==81 and fullqueries==81)
out={'status':'PASS','exact_assertions':checks,'core_nodes':27,'core_queries':27,'full_nodes':fullnodes,'full_queries':fullqueries,'leaf_boundary_types':boundary,'negative_relevant_example':{'pattern':pat,'query':2,'m':1,'excess_interval':[str(exlo),str(exhi)],'bounds':'1/100 < DeltaC-4Inf < 1/40'},'query_certificates':queryrows,'elapsed_seconds':time.monotonic()-start,'spec_sha256':hashlib.sha256((RUN/'FROZEN_CERTIFICATE_SPEC.json').read_bytes()).hexdigest(),'arithmetic':'Fraction; exact prime-log identities; rigorous 24-term atanh bounds'}
(RUN/'out/CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['query_certificates','leaf_boundary_types','negative_relevant_example']}))
