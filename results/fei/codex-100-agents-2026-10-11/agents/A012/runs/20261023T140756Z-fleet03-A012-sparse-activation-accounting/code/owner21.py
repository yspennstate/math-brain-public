from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,time,sys
R=Path(__file__).resolve().parents[1];BASE=R.parents[1];T=time.perf_counter();checks=0
mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert mode in ('pilot','full')
def ck(v):
 global checks
 assert v,checks;checks+=1
 assert time.perf_counter()-T<50
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
def factor(n):
 a=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e+=1
  if e:a.append((p,e))
  p+=1
 if n>1:a.append((n,1))
 return a
def logadd(a,w,x):
 for sign,n in ((1,x.numerator),(-1,x.denominator)):
  for p,e in factor(n):a[p]=a.get(p,F(0))+sign*w*e
def kl(p,q):
 a={}
 for x,y in zip(p,q):
  if x:ck(y>0);logadd(a,x,x/y)
 return {p:v for p,v in a.items() if v}
def ce(p,q):
 a={}
 for x,y in zip(p,q):
  if x:ck(y>0);logadd(a,-x,y)
 return {p:v for p,v in a.items() if v}
@lru_cache(None)
def ln(p):
 k=p.bit_length()-1;r=F(p,1<<k)
 def series(x):
  z=(x-1)/(x+1);N=24
  lo=sum((2*z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
  return lo,lo+2*z**(2*N+1)/F(2*N+1)/(1-z*z)
 l,h=series(r);a,b=series(F(2));return l+k*a,h+k*b
DEN=1<<36
EPS=F(1,4096) if mode=='full' else F(0)
transactions={}
def outward(a,c=F(0)):
 lo=hi=c
 for p,v in a.items():
  l,h=ln(p);lo+=v*(l if v>=0 else h);hi+=v*(h if v>=0 else l)
 return F((lo*DEN).__floor__(),DEN),F((hi*DEN).__ceil__(),DEN)
target=json.loads((BASE/'runs/20261023T053904Z-fleet03-A012-sparse-activation-accounting/out/NEXT_TARGET.json').read_text(encoding='utf-8'))
truth=target['F'];Q=list(map(F,target['root_Q']));ck(Q==spectrum(truth));ck(influence(truth)==F(7,8))
@lru_cache(None)
def raw(s):
 free=[j for j,a in enumerate(s) if a==-1]
 vals=[truth[x] for x in range(64) if all(a==-1 or ((x>>j)&1)==a for j,a in enumerate(s))]
 p=spectrum(vals);q=[F(0)]*len(p)
 for t,v in enumerate(Q):q[sum(((t>>j)&1)<<k for k,j in enumerate(free))]+=v
 ck(sum(p)==sum(q)==1)
 return p,q,influence(vals),vals
def step(s,j,b):
 v=list(s);v[j]=b;return tuple(v)
@lru_cache(None)
def transaction(s):
 p,q,_,_=raw(s);r0=(p[0]+q[0])/2;beta=(1-r0)/(1-q[0]);r=[r0]+[beta*x for x in q[1:]]
 ck(sum(r)==1);l,h=outward(kl(r,q));c=(l,h+EPS)
 transactions[str(s)]={'anchor':s,'beta':beta,'conversion_nats':c,'R_at_transaction':r}
 return beta,c
@lru_cache(None)
def current(s,anchor):
 p,q,i,v=raw(s)
 if anchor is not None:
  beta,_=transaction(anchor);q=[1-beta*(1-q[0])]+[beta*x for x in q[1:]]
 ck(sum(q)==1 and min(q)>=0)
 return p,q,i
records={}
@lru_cache(None)
def dp(s,anchor):
 if anchor is None and s[0]!=-1 and s[1]!=-1 and s[2]==-1:
  _,c=transaction(s);l,h=dp(s,s);return l+c[0],h+c[1]
 p,q,_=current(s,anchor);l,h=outward(kl(p,q));terminal=(l,h+EPS);opts=[terminal]
 for j,a in enumerate(s):
  if a==-1:
   a0=dp(step(s,j,0),anchor);a1=dp(step(s,j,1),anchor)
   opts.append(((a0[0]+a1[0])/2,(a0[1]+a1[1])/2))
 ans=max(x[0] for x in opts),max(x[1] for x in opts)
 key=str((s,anchor));records[key]={'state':s,'anchor':anchor,'terminal_KL_nats':terminal,'upper_potential_nats':ans[1],'lower_optimum_nats':ans[0],'number_query_options':len(opts)-1}
 return ans
root=(-1,)*6;hr=ce(Q,Q)
# Correctly combine the log2 coefficient with -H, including H's log2 term.
sig={p:-v for p,v in hr.items()};sig[2]=sig.get(2,F(0))+F(7,2);stock=outward(sig,F(1,2))
if mode=='pilot':
 roots=[]
 for a,b in product((0,1),repeat=2):
  s=(a,b,-1,-1,-1,-1);c=transaction(s)[1];v=dp(s,s);roots.append((v[0]+c[0],v[1]+c[1]))
 bill=sum(x[0] for x in roots)/4,sum(x[1] for x in roots)/4
else:bill=dp(root,None)
margin=stock[0]-bill[1],stock[1]-bill[0]
# Prescribed original U query after fixed s0,s1,profile,s2 history, retaining its actual fee.
u_bills=[];u_detail=[]
for a,b,c in product((0,1),repeat=3):
 anchor=(a,b,-1,-1,-1,-1);s=(a,b,c,-1,-1,-1);fee=transaction(anchor)[1];costs=[]
 for u in (0,1):
  t=step(s,3,u);p,q,i=current(t,anchor);k=outward(kl(p,q));costs.append(k)
  u_detail.append({'physical_state':t,'anchor':anchor,'P':p,'Q_current':q,'I':i,'KL_nats':k,'truth':raw(t)[3]})
 u_bills.append((fee[0]+sum(x[0] for x in costs)/2,fee[1]+sum(x[1] for x in costs)/2))
ub=sum(x[0] for x in u_bills)/8,sum(x[1] for x in u_bills)/8;um=stock[0]-ub[1],stock[1]-ub[0]
count=[1]
for k in range(1,7):count.append(1+k*count[-1]**2)
def enc(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [enc(x) for x in v]
 return v
out={'status':'PAID' if margin[0]>0 else 'NOT_CERTIFIED','assertions':checks,'seconds':time.perf_counter()-T,'mode':mode,'raw_states':raw.cache_info().currsize,'DP_states':dp.cache_info().currsize,'paid_transaction_states':transaction.cache_info().currsize,'original_source_spare_nats':stock,'worst_terminal_KL_plus_all_fees_nats':bill,'margin_nats':margin,'policy_counts':count,'DP_super_solution':records,'transactions':transactions,'prescribed_U_margin_nats':um,'prescribed_U_full_terminals':u_detail}
(R/'out').mkdir(exist_ok=True)
(R/f'out/{mode.upper()}.json').write_bytes((json.dumps(enc(out),indent=2)+'\n').encode('utf-8'))
print(json.dumps({k:([float(x) for x in v] if k in ('margin_nats','prescribed_U_margin_nats') else v) for k,v in out.items() if k in ('status','assertions','seconds','mode','raw_states','DP_states','paid_transaction_states','margin_nats','prescribed_U_margin_nats')}))
