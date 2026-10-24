from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from math import comb
import json,time
RUN=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0
def check(b):
 global checks
 checks+=1
 if time.perf_counter()-start>50:raise RuntimeError('50-second internal cutoff')
 if not b:raise AssertionError(checks)
def fwht(t):
 a=list(t);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):
    u,v=a[k],a[k+h];a[k]=u+v;a[k+h]=u-v
  h*=2
 return [F(x,len(a)) for x in a]
def inf(t,n):return [F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in range(n)]
@lru_cache(None)
def factor(n):
 a=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e+=1
  if e:a.append((p,e))
  p+=1
 if n>1:a.append((n,1))
 return tuple(a)
def add(a,b,c=F(1)):
 a=dict(a)
 for p,v in b.items():
  a[p]=a.get(p,F(0))+c*v
  if not a[p]:del a[p]
 return a
def scale(a,c):return {p:v*c for p,v in a.items() if v*c}
def logv(x):
 x=F(x);assert x>0;v={}
 for p,e in factor(x.numerator):v[p]=F(e)
 for p,e in factor(x.denominator):v[p]=v.get(p,F(0))-e
 return {p:e for p,e in v.items() if e}
def entropy(p):
 v={}
 for x in p:
  if x:v=add(v,logv(1/x),x)
 return v
def cross(p,q):
 v={}
 for x,y in zip(p,q):
  if x:
   check(y>0);v=add(v,logv(1/y),x)
 return v
@lru_cache(None)
def factlog(n):
 v={}
 for j in range(2,n+1):v=add(v,logv(j))
 return v
def ln_iv(z):
 u=(z-1)/(z+1);a=sum((2*u**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
 return a,a+2*u**41/(41*(1-u*u))
lnlo,lnhi=ln_iv(F(2))
@lru_cache(None)
def log_iv(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 lo,hi=ln_iv(x);return F(k)+lo/lnhi,F(k)+hi/lnlo
def enclose(v):
 lo=hi=F(0)
 for p,c in v.items():
  a,b=log_iv(F(p))
  lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
 return lo,hi
def binlaw(m):return [F(comb(m,b),1<<m) for b in range(m+1)]
def rank_formula(m,d):
 v=scale(add(factlog(d),factlog(d+m)),F(1,2))
 for b,w in enumerate(binlaw(m)):v=add(v,factlog(d+b),-w)
 return scale(v,F(6,5))
def rarity(m,d):return sum((w*(m+d)*(d+b) for b,w in enumerate(binlaw(m)) if 120*(d+b)<11*(m+d)),F(0))

# Independent reference review: labelled balanced tables n<=3, no author code.
activation_cases=0
for n in [1,2,3]:
 for mask in range(1<<(1<<n)):
  g=[1 if mask>>x&1 else -1 for x in range(1<<n)]
  if sum(g):continue
  pg=[v*v for v in fwht(g)];hg=entropy(pg)
  refs=[pg,[F(0)]+[F(1,(1<<n)-1)]*((1<<n)-1),[F(0)]+[F(1,2*((1<<n)-1))]*((1<<n)-1)]
  for r in [1,2,3]:
   p=F(1,1<<r);zmask=(1<<r)-1
   table=[g[x>>r] if x&zmask==0 else 1 for x in range(1<<(n+r))]
   pf=[v*v for v in fwht(table)];ar=add(logv(1/(1-p)**2),{},F(0))
   ar=add(scale(ar,(1-p)**2),logv(2),2*r*p*(2-p))
   for rg in refs:
    q=[]
    for s in range(len(pf)):
     u,t=s&zmask,s>>r
     q.append((1-p)**2 if s==0 else p*p*(rg[t] if t else 1))
     check(pf[s]==((1-p)**2 if s==0 else p*p*(pg[t] if t else 1)))
    check(sum(q)==1-p+p*sum(rg))
    cg=cross(pg,rg);ce=cross(pf,q)
    check(ce==add(scale(cg,p),ar))
    check(add(ce,entropy(pf),F(-1))==scale(add(cg,hg,F(-1)),p))
    activation_cases+=1

# Reconstruct true (J,S) coupling for literal core directly from children.
def joint_literal(r):
 def rec(k,depth):
  if k==0:return {('core',1):F(1)}
  active=rec(k-1,depth+1);inactive={(depth,0):F(1)}
  children=[]
  for tablesign in [0,1]:
   if tablesign==1:t=[1]*(1<<k)
   else:t=[(-1)**(x>>(k-1)) if x&((1<<(k-1))-1)==0 else 1 for x in range(1<<k)]
   children.append(fwht(t))
  u,v=children;out={}
  for child in [active,inactive]:
   for (j,s),w in child.items():
    theta=(u[s]-v[s])**2/(2*(u[s]**2+v[s]**2))
    for bit,prob in [(0,1-theta),(1,theta)]:
     key=(j,(s<<1)|bit);out[key]=out.get(key,F(0))+w*prob/2
  return {k:v for k,v in out.items() if v}
 return rec(r,1)
posterior_cases=[]
for r in [1,2,3,4]:
 p=F(1,1<<r);law=joint_literal(r);spectrum={}
 for (j,s),w in law.items():spectrum[s]=spectrum.get(s,F(0))+w
 eps=[];bsum={}
 for k in range(1,r+1):
  mk=1-F(1,1<<(k-1));qk=(1+mk*mk)/2;ek=(1-mk)**2/(2*(1+mk*mk))
  eps.insert(0,ek)
  bk=add(scale(entropy([ek,1-ek]),qk),logv(2),(1-mk*mk)/2)
  bsum=add(bsum,bk,F(1,1<<(r-k)))
 for s in range(1<<r):
  check(spectrum.get(s,0)==((1-p)**2 if s==0 else p*p))
  for j in range(1,r+1):
   if s==0:
    expected=F(1,1<<j)
    for i in range(j):expected*=1-eps[i]
   elif j>=s.bit_length():
    m=s.bit_length();expected=F(1,1<<j)*eps[m-1]*F(1,1<<(m-1))
    for i in range(m,j):expected*=1-eps[i]
   else:expected=0
   check(law.get((j,s),0)==expected)
 for s in range(1<<r):check(law.get(('core',(1<<r)|s),0)==p*p)
 check(sum(law.values())==1)
 for j in range(1,r+1):check(sum(w for (jj,s),w in law.items() if jj==j)==F(1,1<<j))
 hw=entropy(law.values());check(hw==add(bsum,logv(2),2*(1-p)))
 ar=add(scale(logv(1/(1-p)**2),(1-p)**2),logv(2),2*r*p*(2-p))
 check(add(hw,entropy(spectrum.values()),F(-1))==add(add(bsum,logv(2),2*(1-p)),ar,F(-1)))
 posterior_cases.append({'r':r,'joint_atoms':len(law),'exact_posterior_prime_log':{str(q):str(v) for q,v in add(hw,entropy(spectrum.values()),F(-1)).items()}})

# Sharp coefficient certified at five finite r and proved analytic tail.
cs=[]
for r in [1,2,3,4,5]:
 p=F(1,1<<r)
 c=add(scale(logv(1/(1-p)**2),(1-p)**2/(r*p)),logv(2),2*(2-p))
 cs.append(c)
cstar=add(logv(2),logv(F(8,7)),F(49,12));cstar=add(cstar,logv(2),F(11,4))
check(cs[2]==cstar);check(enclose(cstar)[0]>F(4536,1000));check(enclose(cstar)[1]<F(4537,1000))
for j in [0,1,3,4]:check(enclose(add(cstar,cs[j],F(-1)))[0]>0)
check(lnlo>F(2,3));check(enclose(cstar)[0]>F(9,2))

result={'helper':'A013-A012-review-v2','status':'PASS','exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'activation_reference_cases':activation_cases,'posterior_joint_cases':posterior_cases,'sharp_coefficient_interval':[str(x) for x in enclose(cstar)],'failures':0}
(RUN/'out/REVIEW_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['posterior_joint_cases','sharp_coefficient_interval']},indent=2))
