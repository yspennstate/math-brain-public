from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib

R=Path(__file__).resolve().parents[1]
S=R.parents[2]/'A012/runs/20261023T140756Z-fleet03-A012-sparse-activation-accounting'
T=time.perf_counter(); checks=0
def check(v):
 global checks
 assert v, checks
 checks+=1
 assert time.perf_counter()-T<55
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def enc(x):
 if isinstance(x,F): return str(x)
 if isinstance(x,dict): return {str(k):enc(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)): return [enc(v) for v in x]
 return x

# Freeze before reading/validating the certificate. No search or source writes.
spec={'helper_version':'A013-review21-v1','family':'fixed A012 six-bit Boolean seed',
 'domain':'all reachable physical restrictions with optional mandatory transaction anchor',
 'case_count':'2229 augmented states expected; 729 raw restrictions; 108 anchors',
 'symmetry':'none','arithmetic':'integer character spectra, Fraction references and 20-term atanh log intervals with geometric tail',
 'memory_estimate_MB':120,'maximum_runtime_seconds':55,'purpose':'source-bound certificate validation, not policy search'}
(R/'FROZEN_REVIEW.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
A=read(S/'out/FULL.json')
D=read(R.parent/'20261023T121800Z-fleet03-A013-representation-stability/out/NEXT_TARGET_U.json')
truth=tuple(D['root_truth']);Q=tuple(map(F,D['original_root_Q']))
def spectrum(v):
 return tuple(F(sum(x*(-1 if (j&m).bit_count()%2 else 1) for j,x in enumerate(v))**2,len(v)**2) for m in range(len(v)))
check(spectrum(truth)==Q)
@lru_cache(None)
def ln(q):
 q=F(q); k=q.numerator.bit_length()-q.denominator.bit_length()
 def scale(k):return q/F(2)**k
 r=scale(k)
 if r<1:k-=1;r=scale(k)
 check(1<=r<2)
 def series(x):
  z=(x-1)/(x+1)
  lo=sum((2*z**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
  return lo,lo+2*z**41/(41*(1-z*z))
 a,b=series(r);c,d=series(F(2))
 return a+k*(c if k>=0 else d),b+k*(d if k>=0 else c)
def KL(p,q):
 lo=hi=F(0)
 for x,y in zip(p,q):
  if x:
   check(y>0);a,b=ln(x/y);lo+=x*a;hi+=x*b
 return lo,hi
@lru_cache(None)
def raw(s):
 free=[i for i,a in enumerate(s) if a==-1]
 v=tuple(truth[x] for x in range(64) if all(a==-1 or (x>>i)&1==a for i,a in enumerate(s)))
 p=spectrum(v);q=[F(0)]*len(p)
 for m,w in enumerate(Q):q[sum(((m>>j)&1)<<k for k,j in enumerate(free))]+=w
 inf=sum((w*m.bit_count() for m,w in enumerate(p)),F(0))
 check(sum(p)==sum(q)==1)
 return p,tuple(q),inf,tuple(free)
def step(s,j,b):
 t=list(s);t[j]=b;return tuple(t)
def marginal(q,k):
 out=[F(0)]*(len(q)//2)
 for m,w in enumerate(q):out[(m&((1<<k)-1))|((m>>(k+1))<<k)]+=w
 return tuple(out)
def due(s,a):return a is None and s[0]!=-1 and s[1]!=-1 and s[2]==-1
W={(tuple(v['state']),None if v['anchor'] is None else tuple(v['anchor'])):F(v['upper_potential_nats']) for v in A['DP_super_solution'].values()}
fees={};betas={}
for v in A['transactions'].values():
 s=tuple(v['anchor']);p,q,_,_=raw(s)
 check(due(s,None));r0=(p[0]+q[0])/2;beta=(1-r0)/(1-q[0]);r=(r0,)+tuple(beta*x for x in q[1:])
 check(beta==F(v['beta']) and r==tuple(map(F,v['R_at_transaction'])))
 check(sum(r)==1 and min(r)>=0)
 cost=KL(r,q);cap=F(v['conversion_nats'][1]);check(cost[1]<=cap)
 fees[s]=(cost,cap);betas[s]=beta
@lru_cache(None)
def current(s,a):
 p,q,i,f=raw(s)
 if a is not None:
  check(all(v==-1 or s[j]==v for j,v in enumerate(a)))
  b=betas[a];q=(1-b*(1-q[0]),)+tuple(b*x for x in q[1:])
 check(sum(q)==1 and min(q)>=0)
 return p,q,i,f
def cap(s,a):return fees[s][1]+W[(s,s)] if due(s,a) else W[(s,a)]
visited=set();edges=0;minimum_slack=None
def visit(s,a):
 global edges,minimum_slack
 if (s,a) in visited:return
 visited.add((s,a))
 if due(s,a):visit(s,s);return
 p,q,inf,free=current(s,a);w=W[(s,a)];check(KL(p,q)[1]<=w)
 for k,j in enumerate(free):
  s0,s1=step(s,j,0),step(s,j,1)
  slack=w-(cap(s0,a)+cap(s1,a))/2;check(slack>=0)
  minimum_slack=slack if minimum_slack is None else min(minimum_slack,slack)
  # Independently check physical marginal transport, before any next mandatory conversion.
  for child in (s0,s1):check(current(child,a)[1]==marginal(q,k))
  e=sum((w for m,w in enumerate(p) if (m>>k)&1),F(0))
  check(inf==e+(raw(s0)[2]+raw(s1)[2])/2)
  # Old shared booking survives private queries; only queried shared owners retire it.
  shared=sum((w*sum((m>>h)&1 for h,jj in enumerate(free) if jj<3) for m,w in enumerate(p)),F(0))
  childshared=[]
  for child in (s0,s1):
   pp,_,_,ff=raw(child);childshared.append(sum((w*sum((m>>h)&1 for h,jj in enumerate(ff) if jj<3) for m,w in enumerate(pp)),F(0)))
  check(shared==sum(childshared)/2+(e if j<3 else 0));edges+=1
  visit(s0,a);visit(s1,a)
root=(-1,)*6;visit(root,None)
check(len(visited)==2229 and len(raw.cache_info().__str__())>0)
check({x for x in visited if not due(*x)}==set(W))
check(len(fees)==108 and raw.cache_info().currsize==729)
elllo,ellhi=ln(F(2));Hlo=Hhi=F(0)
for x in Q:
 if x:a,b=ln(1/x);Hlo+=x*a;Hhi+=x*b
check(raw(root)[2]==F(7,8))
# K*I*ln2 - old_booking*ln2 - H*ln2 = 7/2 ln2 + 1/2 - H_nats.
stocklo=F(7,2)*elllo+F(1,2)-Hhi
marginlo=(stocklo-cap(root,None))/ellhi
check(marginlo>F(19,1024))
feeU=F(0);terminalU=F(0)
for v in A['prescribed_U_full_terminals']:
 s=tuple(v['physical_state']);a=tuple(v['anchor']);p,q,i,_=current(s,a)
 check(p==tuple(map(F,v['P'])) and q==tuple(map(F,v['Q_current'])) and i==F(v['I']))
 terminalU+=KL(p,q)[1]/16;feeU+=fees[a][0][1]/16
Umargin=(stocklo-terminalU-feeU)/ellhi;check(Umargin>F(3,5))
# Mutation control: zero source-root potential is rejected by a physical query inequality.
daughter=(cap(step(root,0,0),None)+cap(step(root,0,1),None))/2
check(daughter>0)
paths=[S/'REPORT.md',S/'DERIVATION.md',S/'CLAIMS.json',S/'out/FULL.json',S/'code/owner21.py',S/'code/replay21.py']
result={'status':'PASS','assertions':checks,'augmented_states':len(visited),'ordinary_states':len(W),'raw_states':raw.cache_info().currsize,'transaction_anchors':len(fees),'physical_query_edges':edges,'all_policy_margin_bits_lower':marginlo,'all_policy_margin_bits_lower_float':float(marginlo),'prescribed_U_margin_bits_lower':Umargin,'prescribed_U_margin_bits_lower_float':float(Umargin),'negative_control':'zero root potential rejected','source_sha256':{str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'seconds':time.perf_counter()-T,'review_scope':'new finite certificate and tensor argument checked; A013 prior contributor recused from independent full-chain acceptance','full_FEI':'OPEN'}
(R/'out/REVIEW.json').write_text(json.dumps(enc(result),indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['source_sha256','all_policy_margin_bits_lower','prescribed_U_margin_bits_lower']}))
