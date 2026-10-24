from pathlib import Path
from fractions import Fraction as Q
from math import comb
from collections import Counter
from functools import lru_cache
import json,time,hashlib
R=Path(__file__).resolve().parents[1]
spec=json.loads((R/'out/FROZEN_SPEC.json').read_text());start=time.perf_counter();checks=0
def check(ok):
 global checks
 assert ok
 checks+=1
 if time.perf_counter()-start>60:raise RuntimeError('frozen time exceeded')
def fourier(vals):
 v=list(vals);n=len(v).bit_length()-1
 for i in range(n):
  for x in range(len(v)):
   if not x&(1<<i):
    y=x|(1<<i);a,b=v[x],v[y];v[x]=a+b;v[y]=b-a
 return tuple(Q(a,len(v)) for a in v)
@lru_cache(None)
def logform(q):
 ans={}
 for v,sgn in ((q.numerator,1),(q.denominator,-1)):
  p=2
  while p*p<=v:
   while v%p==0:ans[p]=ans.get(p,0)+sgn;v//=p
   p+=1
  if v>1:ans[v]=ans.get(v,0)+sgn
 return {p:Q(v) for p,v in ans.items() if v}
def add(*terms):
 ans={}
 for scale,d in terms:
  for p,v in d.items():ans[p]=ans.get(p,Q(0))+scale*v
 return {p:v for p,v in ans.items() if v}
def entropy(probs):return add(*[(-q,logform(q)) for q in probs if q])
def H(c):return entropy(tuple(a*a for a in c))
def h(t):return entropy((t,1-t))
def I(c):return sum((s.bit_count()*a*a for s,a in enumerate(c)),Q(0))
def mono(v):
 n=len(v).bit_length()-1
 return all(v[x]<=v[x|(1<<i)] for x in range(len(v)) for i in range(n) if not x&(1<<i))
def bins(k):
 hist=Counter();moment=0
 for j in range(k):
  N=comb(k,j)*7**(k-j)
  S=7*(comb(k-1,j) if j<=k-1 else 0)-(comb(k-1,j-1) if j else 0)
  check((N+S)%2==0 and (N-S)%2==0 and abs(S)<=N)
  hist[2*7**j-1]+=(N+S)//2
  hist[2*7**j+1]+=(N-S)//2
  moment+=j*N
 t0=abs(8**k-2*7**k-1);hist[t0]+=1
 return hist,moment
direct=[]
for k in (1,2,3):
 n=3*k;eps=Q(1,8**k);y=7<<(3*(k-1))
 f=tuple(1 if any((x>>(3*j))&7==7 for j in range(k)) else -1 for x in range(1<<n))
 g=tuple(-1 if x==y else v for x,v in enumerate(f));root=g+f
 check(f[y]==1 and mono(f) and mono(g) and mono(root))
 a,b,p=map(fourier,(f,g,root));c=tuple((x+y)/2 for x,y in zip(a,b));d=tuple((x-y)/2 for x,y in zip(a,b))
 check(p==c+d)
 check(sum((x*x for x in d),Q(0))==eps)
 check(I(a)==Q(3*k,4)*Q(7,8)**(k-1))
 check(I(b)-I(a)==2*eps*(3*k-6))
 check(I(p)==I(a)+eps*(3*k-5))
 hist=Counter(abs(x/eps) for x in c);expected,moment=bins(k)
 check(hist==expected)
 for T in range(1,1<<n):
  r=sum(bool((T>>(3*j))&7) for j in range(k));j=k-r
  check(abs(a[T])==2*eps*7**j and abs(c[T])>=eps*7**j)
 B={};refund={}
 for x,y in zip(c,d):
  q=x*x+y*y
  B=add((1,B),(q,h(y*y/q)))
  refund=add((1,refund),(q,add((1,{2:Q(1)}),(-1,h((x+y)**2/(2*q))))))
 delta=add((1,H(p)),(Q(-1,2),H(a)),(Q(-1,2),H(b)))
 check(delta==add((1,B),(1,refund)))
 V=sum((abs(x*x-y*y) for x,y in zip(a,b)),Q(0));D=4*eps
 check(V==4*eps*sum(map(abs,c)))
 l1=sum(map(abs,a));check(l1==abs(1-2*Q(7,8)**k)+2*(Q(7,4)**k-Q(7,8)**k))
 check(V/D>=l1-1)
 # Terminal-inclusive alternative tree: query the final AND3 block.
 m=3*(k-1);hv=[];gv=[]
 for x in range(1<<(m+1)):
  hv.append(1 if any((x>>(3*j))&7==7 for j in range(k-1)) else -1)
  gv.append(1 if x else -1)
 hc,gc=map(fourier,(hv,gv))
 def kernel(r):return fourier(tuple(gv[x&((1<<(m+1))-1)] if x>>(m+1)==(1<<r)-1 else hv[x&((1<<(m+1))-1)] for x in range(1<<(m+1+r))))
 check(H(kernel(3))==H(p) and I(kernel(3))==I(p))
 paidH={};paidI=Q(0)
 for depth in range(3):
  r=3-depth;parent=kernel(r);child=kernel(r-1)
  local=add((1,H(parent)),(Q(-1,2),H(child)),(Q(-1,2),H(hc)))
  paidH=add((1,paidH),(Q(1,2**depth),local))
  ci=I(parent)-(I(child)+I(hc))/2
  check(ci>=0);paidI+=Q(1,2**depth)*ci
 terminalH=add((Q(7,8),H(hc)),(Q(1,8),H(gc)))
 terminalI=Q(7,8)*I(hc)+Q(1,8)*I(gc)
 check(H(p)==add((1,paidH),(1,terminalH)))
 check(I(p)==paidI+terminalI)
 direct.append({'k':k,'n':n,'I_selector':str(eps),'I_root':str(I(p)),'V_over_D':str(V/D),'l1_child':str(l1),
  'Delta_over_I_form':{str(p):str(v/eps) for p,v in delta.items()},
  'terminal_entropy_form':{str(p):str(v) for p,v in terminalH.items()},'terminal_influence':str(terminalI)})
compressed=[]
for k in range(1,13):
 hist,moment=bins(k);eps=Q(1,8**k)
 check(sum(hist.values())==8**k)
 check(eps**2*sum(t*t*v for t,v in hist.items())==1-eps)
 check(moment==k*8**(k-1)-k)
 VoverD=eps*sum(t*v for t,v in hist.items())
 l1=abs(1-2*Q(7,8)**k)+2*(Q(7,4)**k-Q(7,8)**k)
 check(VoverD>=l1-1 and VoverD>=2*Q(7,4)**k-3)
 compressed.append({'k':k,'packet_types':len(hist),'packet_count':8**k,'missed_block_moment_nonempty':moment,'V_over_D':str(VoverD),'lower_coefficient_of_log2_7':str(Q(k,4)-Q(2*k,8**k))})
k=9;lower=Q(k,2)-Q(4*k,8**k);check(7>4 and lower>4)
out={'status':'PASS','exact_assertions':checks,'seconds':time.perf_counter()-start,'direct_roots':direct,
 'compressed_laws':compressed,'k9_certificate':{'log2_7_lower_bound':'strictly greater than 2 because 7>4','Delta_over_I_lower_bound_strict':str(lower),'threshold':'4'},
 'counts':spec['case_count'],'all_logarithm_signs':'Proved analytically; no floating-point sign checks',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out/VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':out['status'],'exact_assertions':checks,'seconds':out['seconds'],'k9_bound':str(lower),'direct_roots':3,'compressed_laws':12}))
