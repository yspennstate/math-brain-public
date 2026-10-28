from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
SRC=R.parent/'20261023T053904Z-account03-A012-sparse-activation-accounting'
def ck(v):
 global checks
 assert v,checks
 checks+=1
 assert time.perf_counter()-start<50
def fw(v):
 a=list(v);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def spectrum(v):return [F(x*x,len(v)**2) for x in fw(v)]
def influence(v):return F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v)) for j in range((len(v)-1).bit_length())),len(v))
@lru_cache(None)
def factors(n):
 out=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:e+=1;n//=p
  if e:out.append((p,e))
  p+=1
 if n>1:out.append((n,1))
 return out
def logadd(a,w,x):
 if not w:return
 for s,n in ((1,x.numerator),(-1,x.denominator)):
  for p,e in factors(n):a[p]=a.get(p,F(0))+s*w*e
def clean(a):return {k:v for k,v in a.items() if v}
def lin(*args):
 out={}
 for w,a in args:
  for p,v in a.items():out[p]=out.get(p,F(0))+w*v
 return clean(out)
def ce(p,q):
 a={}
 for x,y in zip(p,q):
  if x:ck(y>0);logadd(a,-x,y)
 return clean(a)
def kl(p,q):return lin((1,ce(p,q)),(-1,ce(p,p)))
@lru_cache(None)
def ln(p):
 k=p.bit_length()-1;r=F(p,1<<k)
 def series(x):
  z=(x-1)/(x+1);N=24
  lo=sum((2*z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
  return lo,lo+2*z**(2*N+1)/F(2*N+1)/(1-z*z)
 lo,hi=series(r);l,h=series(F(2));return lo+k*l,hi+k*h
def interval(a,c=F(0)):
 lo=hi=c
 for p,v in a.items():
  l,h=ln(p);lo+=v*(l if v>=0 else h);hi+=v*(h if v>=0 else l)
 return lo,hi
def avg(exprs):return lin(*[(F(1,len(exprs)),v) for v in exprs])
def enc(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [enc(v) for v in x]
 return x
target=json.loads((SRC/'out/NEXT_TARGET.json').read_text(encoding='utf-8'))
truth=target['F'];Q=list(map(F,target['root_Q']));ck(Q==spectrum(truth))
states={}
for state in product((-1,0,1),repeat=3):
 fixed={j:b for j,b in enumerate(state) if b!=-1};free=[j for j in range(6) if j not in fixed]
 def inject(x):return sum(b<<j for j,b in fixed.items())+sum(((x>>k)&1)<<j for k,j in enumerate(free))
 child=[truth[inject(x)] for x in range(1<<len(free))];p=spectrum(child)
 q=[sum(Q[t] for t in range(64) if all(((t>>j)&1)==((x>>k)&1) for k,j in enumerate(free))) for x in range(len(child))]
 profile=(p[0]+q[0])/2
 r=[profile]+[x*(1-profile)/(1-q[0]) for x in q[1:]] if q[0]!=1 else q[:]
 ck(sum(p)==sum(q)==sum(r)==1)
 for i in range(1,len(p)):
  ck((r[i]==0)==(q[i]==0))
  ck(r[i]*(1-q[0])==q[i]*(1-profile))
 old=ce(p,q);new=ce(p,r)
 pp=[p[0],1-p[0]];qq=[q[0],1-q[0]];rr=[r[0],1-r[0]]
 discount=lin((1,kl(pp,qq)),(-1,kl(pp,rr)))
 conversion=kl(r,q);ck(conversion==kl(rr,qq))
 ck(lin((1,old),(-1,new))==discount)
 net=lin((1,discount),(-1,conversion))
 ck(net==lin((1,kl(rr,qq)),(1,kl(qq,rr))))
 # Exact chain rule: full terminal KL remains, only its Bernoulli profile is removed.
 if p[0]!=1:
  cond=kl([x/(1-p[0]) for x in p[1:]],[x/(1-q[0]) for x in q[1:]])
  ck(kl(p,r)==lin((1,kl(pp,rr)),(1-p[0],cond)))
 else:ck(kl(p,r)==kl(pp,rr))
 i=influence(child)
 oldmargin=interval(lin((4*i,{2:F(1)}),(-1,old)),2*i-F(5,4))
 newmargin=interval(lin((4*i,{2:F(1)}),(-1,new)),2*i-F(5,4))
 states[state]={'P':p,'Q_original_marginal':q,'R_profile':r,'I':i,'CE_old':old,'CE_new':new,'profile_discount':discount,'net_rebate':net,'D_R_Q':conversion,'full_terminal_KL':kl(p,r),'margin_old_ln':oldmargin,'margin_new_ln':newmargin,'truth':child}
front=[states[(a,b,-1)] for a,b in product((0,1),repeat=2)]
i=sum(s['I'] for s in front)/4;old=avg([s['CE_old'] for s in front]);new=avg([s['CE_new'] for s in front]);discount=avg([s['profile_discount'] for s in front])
oldm=interval(lin((4*i,{2:F(1)}),(-1,old)),2*i-F(5,4));newm=interval(lin((4*i,{2:F(1)}),(-1,new)),2*i-F(5,4))
conversion=avg([s['D_R_Q'] for s in front]);net=avg([s['net_rebate'] for s in front]);charged=lin((1,new),(1,conversion));ck(lin((1,old),(-1,charged))==net)
chargedm=interval(lin((4*i,{2:F(1)}),(-1,charged)),2*i-F(5,4))
ck(chargedm[0]>0)
out={'status':'PASS','assertions':checks,'seconds':time.perf_counter()-start,'states':{str(k):v for k,v in states.items()},'frontier':{'I':i,'CE_old':old,'CE_new':new,'discount':discount,'margin_old_ln':oldm,'margin_new_ln':newm,'conversion_charge_D_R_Q':conversion,'net_rebate':net,'charged_CE':charged,'charged_margin_ln':chargedm}}
(R/'out/PARTIAL.json').write_text(json.dumps(enc(out),indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','assertions':checks,'seconds':out['seconds'],'frontier_old_margin_nats':list(map(float,oldm)),'frontier_new_margin_nats':list(map(float,newm)),'charged_margin_nats':list(map(float,chargedm)),'net_rebate_nats':list(map(float,interval(net))),'conversion_nats':list(map(float,interval(conversion)))}))
