from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb
import sys,json,time

ROOT=Path(__file__).resolve().parents[1]
checks=0;nodes=0
def ck(x):
 global checks
 assert x
 checks+=1
def prod(xs):
 y=F(1)
 for x in xs:y*=x
 return y
def bern(p):
 return tuple(prod(p[i] if x>>i&1 else 1-p[i] for i in range(len(p))) for x in range(1<<len(p)))
def component(kind,p):
 n=len(p)
 if kind=='single':return tuple(F(0) if x==0 or x&(x-1) else p[x.bit_length()-1] for x in range(1<<n))
 a=bern(p);z=1-a[0];assert z>0
 return (F(0),)+tuple(x/z for x in a[1:])
def law(model,n):
 v,comps=model;out=[F(0)]*(1<<n);out[0]=v
 for mass,kind,p in comps:
  for x,z in enumerate(component(kind,p)):out[x]+=mass*z
 return tuple(out)
def model(v,comps):return (v,tuple((w,k,tuple(p)) for w,k,p in comps if w))
def marginal(m,n,remaining):
 v,comps=m;out=[]
 for mass,kind,p in comps:
  pp=tuple(p[i] for i in remaining)
  a=sum(pp) if kind=='single' else (1-prod(1-x for x in pp))/(1-prod(1-x for x in p))
  v+=mass*(1-a)
  if a:out.append((mass*a,kind,tuple(x/a for x in pp) if kind=='single' else pp))
 return model(v,out)
def tilt(m,n,t,v):
 if v==1:return model(F(1),[])
 out=[]
 for mass,kind,p in m[1]:
  if kind=='single':
   z=sum(x*y for x,y in zip(p,t));pp=tuple(x*y/z for x,y in zip(p,t))
  else:
   empty=prod(1-x for x in p);z=(prod(1-x+x*y for x,y in zip(p,t))-empty)/(1-empty)
   pp=tuple(x*y/(1-x+x*y) for x,y in zip(p,t))
  out.append((mass*z,kind,pp))
 z=sum(w for w,_,_ in out);assert z>0
 return model(v,[(w*(1-v)/z,k,p) for w,k,p in out])
def project_vac(m,n,p0):return tilt(m,n,(F(1),)*n,p0) if n else model(F(1),[])
def project_vector(p,remaining):
 out=[F(0)]*(1<<len(remaining))
 for x,z in enumerate(p):
  key=sum(((x>>i)&1)<<j for j,i in enumerate(remaining));out[key]+=z
 return tuple(out)

@lru_cache(None)
def factor(n):
 out=[];d=2
 while d*d<=n:
  k=0
  while n%d==0:n//=d;k+=1
  if k:out.append((d,k))
  d+=1
 if n>1:out.append((n,1))
 return tuple(out)
def add(a,b,k=F(1)):
 out=dict(a)
 for x,y in b.items():
  out[x]=out.get(x,F(0))+k*y
  if not out[x]:del out[x]
 return out
@lru_cache(None)
def log(v):
 assert v>0
 return add(dict(factor(v.numerator)),dict(factor(v.denominator)),F(-1))
def ce(p,q):
 out={}
 for x,y in zip(p,q):
  if x:out=add(out,log(y),-x)
 return out
@lru_cache(None)
def entropy(p):return ce(p,p)
def kl(p,q):return add(ce(p,q),entropy(p),F(-1))
def walsh(truth):
 out=list(truth);step=1
 while step<len(out):
  for base in range(0,len(out),step*2):
   for j in range(base,base+step):a,b=out[j],out[j+step];out[j]=a+b;out[j+step]=a-b
  step*=2
 return tuple(F(x,len(out)) for x in out)
@lru_cache(None)
def spec(truth):return tuple(x*x for x in walsh(truth))
def restrict(truth,i,b):return tuple(truth[(x&((1<<i)-1))|(b<<i)|((x>>i)<<(i+1))] for x in range(len(truth)//2))
def energy(p):return sum((x*s.bit_count() for s,x in enumerate(p)),F(0))
def fixtures(n,v):
 p=tuple(F(1+(i%3),4) for i in range(n));q=tuple(1-x for x in p)
 alpha=tuple(F(i+1,n*(n+1)//2) for i in range(n))
 fixed=tuple(F(i==0) for i in range(n))
 w=1-v
 return [model(v,[(w,'product',p)]),model(v,[(w/2,'product',p),(w/2,'product',q)]),model(v,[(w,'single',alpha)]),model(v,[(w/2,'product',fixed),(w/2,'single',alpha)])]
def closure():
 cases=0
 for n in range(1,6):
  for v in (F(0),F(1,4),F(1)):
   for m in fixtures(n,v):
    p=law(m,n);ck(sum(p)==1)
    for mask in range(1<<n):
     rem=tuple(i for i in range(n) if mask>>i&1);child=marginal(m,n,rem)
     ck(law(child,len(rem))==project_vector(p,rem));ck(len(child[1])<=len(m[1]));cases+=1
    if v<1:
     t=tuple(F(2) if i%2 else F(1,2) for i in range(n))
     for nv in (F(0),F(1,3),F(1)):
      u=tilt(m,n,t,nv);up=law(u,n);raw=[p[x]*prod(t[i] for i in range(n) if x>>i&1) for x in range(1<<n)];z=sum(raw[1:])
      expected=(nv,)+tuple((1-nv)*x/z for x in raw[1:])
      ck(up==expected);ck(len(u[1])<=len(m[1]));cases+=1
 return cases

def walk(truth,m,depth=0):
 global nodes
 nodes+=1;n=(len(truth)-1).bit_length();p=spec(truth);q=law(m,n)
 ck(sum(q)==1);ck(all(y>0 for x,y in zip(p,q) if x));ck(len(m[1])<=2)
 if not n:return [({}, {}, {}, ce(p,q))]*2
 selected=[sum(i for i,x in enumerate(truth) if x<0)%n,n-1]
 result=[None,None]
 for i in range(n):
  rem=tuple(j for j in range(n) if j!=i);pm=project_vector(p,rem);mm=marginal(m,n,rem);qm=law(mm,n-1)
  ck(qm==project_vector(q,rem));B=add(entropy(p),entropy(pm),F(-1));K=add(kl(p,q),kl(pm,qm),F(-1))
  children=[];costs=[];projs=[];childp=[]
  for bit in (0,1):
   tt=restrict(truth,i,bit);pp=spec(tt);uu=project_vac(mm,n-1,pp[0]);qu=law(uu,n-1)
   ck(all(y>0 for x,y in zip(pp,qm) if x));ck(len(uu[1])<=len(m[1]));ck(qu[0]==pp[0])
   delta=add(ce(pp,qu),ce(pp,qm),F(-1));release=kl(qu,qm)
   ck(add(delta,release)=={})
   children.append(walk(tt,uu,depth+1));costs.append(ce(pp,qu));projs.append(release);childp.append(pp)
  ck(tuple((a+b)/2 for a,b in zip(*childp))==pm)
  inf=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(len(truth))),len(truth))
  ck(energy(p)==inf+(energy(childp[0])+energy(childp[1]))/2)
  rhs=add(add(B,K),add(projs[0],projs[1]),F(1,2));rhs=add(rhs,add(costs[0],costs[1]),F(1,2));ck(rhs==ce(p,q))
  # Conditional entropy is recomputed from the true full law, never from latent labels.
  ck(add(entropy(p),entropy(pm),F(-1))==B)
  for policy in range(2):
   if selected[policy]==i:
    aggregate=[]
    for k in range(4):aggregate.append(add(children[0][policy][k],children[1][policy][k],F(1)))
    aggregate=[{p:v/2 for p,v in x.items()} for x in aggregate]
    aggregate[0]=add(aggregate[0],B);aggregate[1]=add(aggregate[1],K);aggregate[2]=add(aggregate[2],add(projs[0],projs[1]),F(1,2));result[policy]=tuple(aggregate)
 return result

def boolean_domain(maxn):
 roots=0
 for n in range(maxn+1):
  for table in range(1<<(1<<n)):
   truth=tuple(-1 if table>>x&1 else 1 for x in range(1<<n));p=spec(truth)
   initial=model(F(1,3),[(F(1,3),'product',(F(1,3),)*n),(F(1,3),'product',(F(2,3),)*n)]) if n else model(F(1),[])
   q0=law(initial,n);m=project_vac(initial,n,p[0]);q=law(m,n)
   ck(add(add(ce(p,q),ce(p,q0),F(-1)),kl(q,q0))=={})
   paths=walk(truth,m)
   for account in paths:
    total={}
    for e in account:total=add(total,e)
    ck(total==ce(p,q))
   roots+=1
 return roots

def and_fixtures():
 out=[]
 for n in (4,6,8):
  N=1<<n;r=F(1,N)
  root=model(F(1,2*N),[(F(N-1,2*N),'product',(F(1,2),)*n),(F(1,2),'product',(F(1),)*n)])
  q=law(root,n);expected=tuple(F(1,2*N)+(F(1,2) if x==N-1 else 0) for x in range(N));ck(q==expected)
  v=project_vac(root,n,r);ck(len(v[1])==2)
  def mean_sign(x):
   Z=(1+x)**n-1+N*x**n;der=n*(1+x)**(n-1)+N*n*x**(n-1)
   return 2*(N-1)*x*der-n*N*Z
  lo,hi=F(1,N+1),F(1);ck(mean_sign(lo)<0<mean_sign(hi))
  for _ in range(40):
   mid=(lo+hi)/2
   if mean_sign(mid)<0:lo=mid
   else:hi=mid
  u=tilt(v,n,(F(1,2),)*n,r);ck(len(u[1])==2);uv=law(u,n)
  Z=F(3,2)**n-1+N*F(1,2)**n
  explicit=(r,)+tuple(F(N-1,N)*F(1,2)**x.bit_count()*(N+1 if x==N-1 else 1)/Z for x in range(1,N))
  ck(uv==explicit)
  out.append({'n':n,'minimum_individual_atoms':N-n,'nonempty_components_after_calibration':2,'tilt_root_interval':[str(lo),str(hi)],'bracket_signs':[-1,1],'note':'Exact tilted model at x1/2; actual matched-influence projection is at the uniquely bracketed algebraic root'})
 return out

def flat_review():
 out=[]
 for m in range(1,5):
  truth=tuple((-1)**(((x&((1<<m)-1))&(x>>m)).bit_count()+(((x>>m)&1)*((x>>(m+1)).bit_count()))) for x in range(1<<(2*m)))
  p=spec(truth);ck(all(x==F(1,len(p)) for x in p));ck(energy(p)==m)
  for t in range(1<<(m-1)):
   child=[]
   for z in range(1<<(m+1)):
    x1=z&1;y=z>>1;x=x1|(t<<1);child.append(truth[x|(y<<m)])
   pc=spec(tuple(child));expected=[F(0)]*len(pc)
   for aa,bb in product((0,1),repeat=2):
    key=aa|(bb<<1)
    for j in range(1,m):key|=(aa^((t>>(j-1))&1))<<(j+1)
    expected[key]=F(1,4)
   ck(pc==tuple(expected));ck(energy(pc)==F(m+1,2))
   # The posterior conditioned on copied bit A=1 attains contraction exactly m.
   rr=tuple(2*z if x&1 else F(0) for x,z in enumerate(pc))
   numerator={}
   for i in range(m+1):numerator=add(numerator,kl(project_vector(rr,(i,)),project_vector(pc,(i,))))
   ck(numerator=={p:m*v for p,v in kl(rr,pc).items()})
  out.append({'m':m,'full_terminals':1<<(m-1),'optimal_contraction':m})
 return out

def main():
 mode=sys.argv[1];start=time.perf_counter()
 closures=closure();roots=boolean_domain(2 if mode=='pilot' else 3)
 af=and_fixtures();flat=flat_review()
 result={'status':'PASS','mode':mode,'exact_assertions':checks,'seconds':time.perf_counter()-start,'boolean_roots':roots,'all_query_path_nodes':nodes,'full_adaptive_policy_accounts':2*roots,'closure_fixtures':closures,'and2_reference_fixtures':af,'flat_parent_review':flat,'arithmetic':'integers, Fractions, exact prime-log identities; algebraic tilt root brackets by exact polynomial signs','peak_memory':'unmeasured; estimated under90MB'}
 (ROOT/'out').mkdir(exist_ok=True)
 (ROOT/f'out/{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ('and2_reference_fixtures','flat_parent_review')}))
if __name__=='__main__':main()
