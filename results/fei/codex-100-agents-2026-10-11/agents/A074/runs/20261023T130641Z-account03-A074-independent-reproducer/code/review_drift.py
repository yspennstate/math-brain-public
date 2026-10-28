from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json, time, sys, hashlib
R=Path(__file__).resolve().parents[1]
checks=0
deadline=None
def ck(v):
 global checks
 checks+=1
 if not v: raise AssertionError(checks)
def plus(*ps):
 d={}
 for p in ps:
  for k,v in p.items(): d[k]=d.get(k,Q(0))+v
 return {k:v for k,v in d.items() if v}
def scale(p,a): return {k:v*a for k,v in p.items() if v*a}
def sub(a,b): return plus(a,scale(b,-1))
def const(v): return {2:Q(v)} if v else {}
def factor(n):
 d={}; p=2
 while p*p<=n:
  while n%p==0: d[p]=d.get(p,0)+1; n//=p
  p+=1
 if n>1: d[n]=d.get(n,0)+1
 return d
def logform(v):
 v=Q(v); return plus(factor(v.numerator),scale(factor(v.denominator),-1))
def ent(ps): return plus(*(scale(logform(p),-p) for p in ps if p))
def phi(a,b): return sub(ent([a,b]),ent([a+b]))
@lru_cache(None)
def logbounds(p):
 if p==2:return Q(1),Q(1)
 # Range reduction: p=2^k*y, 1<=y<2, so z<1/3.
 k=p.bit_length()-1; y=Q(p,2**k); z=(y-1)/(y+1)
 def lnseries(z):
  n=64; s=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(n)),Q(0))
  e=2*z**(2*n+1)/(Q(2*n+1)*(1-z*z))
  return s,s+e
 a,b=lnseries(z); c,d=lnseries(Q(1,3))
 return Q(k)+a/d,Q(k)+b/c
def bounds(p):
 lo=hi=Q(0)
 for k,v in p.items():
  a,b=logbounds(k)
  if v<0:a,b=b,a
  lo+=v*a;hi+=v*b
 return lo,hi
def nonneg(p):
 if not p:return True
 lo,hi=bounds(p)
 if lo>=0:return True
 if hi<0:return False
 raise ArithmeticError('unresolved interval sign; no hull choice permitted')
def restrict(t,i,b):
 return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
@lru_cache(None)
def walsh(t):
 n=len(t); w=tuple(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(n))
 ck(sum(v*v for v in w)==n*sum(v*v for v in t))
 for x,v in enumerate(t):ck(sum(a*(-1 if (x&s).bit_count()%2 else 1) for s,a in enumerate(w))==n*v)
 return tuple(Q(a,n) for a in w)
@lru_cache(None)
def data(t):
 a=walsh(t); n=(len(t)).bit_length()-1
 ds=tuple(Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(n))
 for i,d in enumerate(ds):ck(d==sum(v*v for s,v in enumerate(a) if s>>i&1))
 return ent(v*v for v in a),sum(ds,Q(0)),ds,a
@lru_cache(None)
def erase(t,i):
 H,I,ds,a=data(t); kids=[restrict(t,i,b) for b in (0,1)]
 rows=[(a[s],a[s|1<<i]) for s in range(len(t)) if not s>>i&1]
 B=plus(*(phi(x*x,y*y) for x,y in rows))
 P=ent(x*x+y*y for x,y in rows)
 J=sub(P,scale(plus(*(data(k)[0] for k in kids)),Q(1,2)))
 ck(sub(H,scale(plus(*(data(k)[0] for k in kids)),Q(1,2)))==plus(B,J))
 ck(nonneg(B));ck(nonneg(J));ck(nonneg(sub(const(3*ds[i]),J)))
 return B,J
def composed(h,gs):
 sizes=[len(g).bit_length()-1 for g in gs];N=1<<sum(sizes);t=[]
 for x in range(N):
  off=0;z=0
  for j,(g,n) in enumerate(zip(gs,sizes)):
   if g[(x>>off)&((1<<n)-1)]<0:z|=1<<j
   off+=n
  t.append(h[z])
 return tuple(t)
def pivots(h,gs):
 neg=[Q(g.count(-1),len(g)) for g in gs];qs=[]
 for j in range(len(gs)):
  q=Q(0)
  for z in range(1<<len(gs)):
   if z>>j&1:continue
   p=Q(1)
   for k in range(len(gs)):
    if k!=j:p*=neg[k] if z>>k&1 else 1-neg[k]
   if h[z]!=h[z|1<<j]:q+=p
  qs.append(q)
 return tuple(qs)
def account(h,gs):
 t=composed(h,gs);q=pivots(h,gs);H,I,ds,a=data(t)
 C=sub(H,plus(*(scale(data(g)[0],v) for g,v in zip(gs,q))))
 ck(I==sum(v*data(g)[1] for g,v in zip(gs,q)))
 return t,q,C
@lru_cache(None)
def hull(t,K):
 H,I,ds,a=data(t);base=sub(H,const(K*I))
 best=base if nonneg(base) else {}
 for i in range(len(ds)):
  m=scale(plus(*(hull(restrict(t,i,b),K) for b in (0,1))),Q(1,2))
  if nonneg(sub(m,best)):best=m
 return best
def row(h,gs,j,i,bank=True):
 if deadline is not None and time.monotonic()>deadline:raise TimeoutError('frozen 55-second work cap')
 t,q,C=account(h,gs);off=sum(len(g).bit_length()-1 for g in gs[:j]);pi=off+i
 children=[]
 for b in (0,1):
  child=list(gs);child[j]=restrict(gs[j],i,b);child=tuple(child)
  tt,qq,cc=account(h,child);ck(tt==restrict(t,pi,b));children.append((child,qq,cc))
 for k in range(len(gs)):ck((children[0][1][k]+children[1][1][k])/2==q[k])
 a=data(gs[j])[3];mu=a[0];tau=a[1<<i];d=data(gs[j])[2][i];df=data(t)[2][pi]
 ck(df==q[j]*d)
 # Construct the outside physical A and D functions, allowing values 0.
 other=gs[:j]+gs[j+1:];A=[];D=[]
 for x in range(1<<sum(len(g).bit_length()-1 for g in other)):
  z=0;offset=0;oj=0
  for k in range(len(gs)):
   if k==j:continue
   n=len(gs[k]).bit_length()-1
   if gs[k][(x>>offset)&((1<<n)-1)]<0:z|=1<<k
   offset+=n;oj+=1
  A.append(Q(h[z]+h[z|1<<j],2));D.append(Q(h[z]-h[z|1<<j],2))
 aa,dd=walsh(tuple(A)),walsh(tuple(D));ck(sum(v*v for v in dd)==q[j])
 special=plus(*(phi((x+mu*y)**2,(tau*y)**2) for x,y in zip(aa,dd)))
 Bi,Ji=erase(gs[j],i);Bf,Jf=erase(t,pi);vac=phi(mu*mu,tau*tau)
 ck(Bf==plus(scale(sub(Bi,vac),q[j]),special))
 drift=sub(scale(plus(children[0][2],children[1][2]),Q(1,2)),C)
 ck(drift==sub(scale(plus(vac,Ji),q[j]),plus(special,Jf)))
 ck(nonneg(sub(const(6*df),drift)))
 ck(data(t)[1]-sum(data(composed(h,c[0]))[1] for c in children)/2==df)
 reserve=plus(C,const(6*data(t)[1]));ck(nonneg(reserve))
 if bank:
  for K in (0,1,3):
   parent=plus(reserve,*(scale(hull(g,K),v) for g,v in zip(gs,q)))
   childbanks=[]
   for child,qq,cc in children:
    ft=composed(h,child)
    z=plus(cc,const(6*data(ft)[1]),*(scale(hull(g,K),v) for g,v in zip(child,qq)))
    ck(nonneg(z));ck(nonneg(sub(z,sub(data(ft)[0],const(K*data(ft)[1])))));childbanks.append(z)
   avg=scale(plus(*childbanks),Q(1,2));slack=sub(parent,avg);ck(nonneg(slack))
   credits=[plus(z,slack) for z in childbanks]
   ck(scale(plus(*credits),Q(1,2))==parent)
   for z in credits:ck(nonneg(z))
 return drift,df,C
def serialize(p):return {str(k):str(v) for k,v in p.items()}
def main():
 global deadline
 start=time.monotonic();pilot='--pilot' in sys.argv;rows=0
 deadline=start+55
 h=tuple(1 if z==0 else -1 for z in range(8));gs=tuple(tuple(-1 if x==0 else 1 for x in range(1<<n)) for n in (3,2,2))
 G,d,C=row(h,gs,0,0);rows+=1
 ck(Q(107184,10**6)<bounds(G)[0]<=bounds(G)[1]<Q(107185,10**6));ck(d==Q(9,64))
 expected={2:Q(-37,16),3:Q(-567,512),5:Q(-25,1024),7:Q(3087,2048)};ck(G==expected)
 ck(7**3087>2**4736*3**2268*5**50)
 ck(sub(G,const(Q(1,1000)))!=G) # Deliberate mutation must be rejected.
 if not pilot:
  for j,n in enumerate((3,2,2)):
   for i in range(n):
    if (j,i)!=(0,0):row(h,gs,j,i);rows+=1
  cores=[tuple(-1 if mask>>x&1 else 1 for x in range(2)) for mask in range(4)]
  for mask in range(16):
   hh=tuple(-1 if mask>>x&1 else 1 for x in range(4))
   for g in cores:
    for gg in cores:
     for j in (0,1):row(hh,(g,gg),j,0);rows+=1
  ck(rows==519)
 result={'implementation':'fresh direct character sums; no producer imports','query_rows':rows,'bank_rows':rows*3,'predicates':checks,'elapsed_seconds':time.monotonic()-start,'drift':serialize(G),'drift_bounds':[str(z) for z in bounds(G)],'query_influence':str(d),'reserve_headroom':serialize(sub(const(6*d),G)),'mutation_rejected':True,'status':'PASS','universal_scope':'separate analytic review; finite checks do not prove all dimensions'}
 out=R/'out'/('PILOT.json' if pilot else 'VALIDATION.json');out.parent.mkdir(exist_ok=True)
 if out.exists():
  previous=out.with_name(out.stem+'_BEFORE_SIGN_GUARD.json')
  if not previous.exists():previous.write_bytes(out.read_bytes())
 result['unresolved_sign_policy']='raise ArithmeticError, never choose a hull branch'
 out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:result[k] for k in ('query_rows','bank_rows','predicates','elapsed_seconds','status')}))
if __name__=='__main__':main()
