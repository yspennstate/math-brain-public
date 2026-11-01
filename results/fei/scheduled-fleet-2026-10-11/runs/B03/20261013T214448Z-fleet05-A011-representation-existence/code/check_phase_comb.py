import pathlib,json,time,itertools,math,sys
from fractions import Fraction as F
from functools import lru_cache
R=pathlib.Path(__file__).resolve().parents[1]; start=time.monotonic(); checks=0
def ck(v):
 global checks
 checks+=1
 assert v, checks
def fw(v):
 v=list(v); step=1
 while step<len(v):
  for k in range(0,len(v),2*step):
   for j in range(k,k+step): v[j],v[j+step]=v[j]+v[j+step],v[j]-v[j+step]
  step*=2
 return tuple(F(z,len(v)) for z in v)
def spectrum(v): return tuple(z*z for z in fw(v))
@lru_cache(None)
def factors(n):
 ans={}; d=2
 while d*d<=n:
  while n%d==0: ans[d]=ans.get(d,0)+1; n//=d
  d+=1
 if n>1: ans[n]=ans.get(n,0)+1
 return ans
def add(v,w,scale=F(1)):
 for k,z in w.items():
  v[k]=v.get(k,F(0))+scale*z
 return {k:z for k,z in v.items() if z}
@lru_cache(None)
def logvec(z):
 ans={}
 for k,v in factors(z.numerator).items(): ans[k]=F(v)
 for k,v in factors(z.denominator).items(): ans[k]=ans.get(k,0)-v
 return {k:z for k,z in ans.items() if z}
@lru_cache(None)
def ce(p,q):
 ans={}
 for x,y in zip(p,q):
  if x: ck(y>0); ans=add(ans,logvec(y),-x)
 return ans
def entropy(p): return ce(p,p)
def ln_interval(z):
 t=(z-1)/(z+1); acc=F(0); power=t
 for j in range(40): acc+=2*power/(2*j+1); power*=t*t
 return acc,acc+2*power/(81*(1-t*t))
@lru_cache(None)
def log_interval(z):
 z=F(z); k=0
 while z>=2: z/=2; k+=1
 while z<1: z*=2; k-=1
 lo,hi=ln_interval(z); l2,u2=ln_interval(F(2))
 return F(k)+lo/u2,F(k)+hi/l2
def interval(v):
 lo=hi=F(0)
 for z,c in v.items():
  a,b=log_interval(z)
  lo+=c*(a if c>0 else b); hi+=c*(b if c>0 else a)
 return lo,hi
def leaf_index(x,a):
 for j in range(a):
  if not (x>>j)&1: return j
 return a
def weights(a): return tuple(F(1,2**(j+1)) for j in range(a))+(F(1,2**a),)
def scalar(labels):
 a=len(labels)-1; table=tuple(labels[leaf_index(x,a)] for x in range(2**a)); p=spectrum(table)
 inf=sum(F(sum(table[x]!=table[x^(1<<j)] for x in range(len(table))),len(table)) for j in range(a))
 mu=F(labels[-1]); rs=[F(0)]*a
 for j in reversed(range(a)): rs[j]=(1-labels[j]*mu)/2; mu=(labels[j]+mu)/2
 ck(p[0]==mu*mu)
 for u in range(1,2**a):
  j=u.bit_length()-1; ck(p[u]==F(1,2**(2*j))*rs[j]**2)
 vs=[F(1,2**j)*r*r for j,r in enumerate(rs)]
 ck(sum(vs)==1-mu*mu)
 ck(inf==sum(F(1,2**j)*r for j,r in enumerate(rs)))
 ck(inf==sum(F(j+2,2)*v for j,v in enumerate(vs)))
 ck(interval(entropy(p))[1]<=F(41,8)*inf if inf else entropy(p)=={})
 return p,inf
scalar_cache={}
for a in range(1,9):
 for labels in itertools.product((-1,1),repeat=a+1): scalar_cache[labels]=scalar(labels)
cores=[tuple(1 if mask>>x&1 else -1 for x in range(4)) for mask in range(16)]
coeff=[fw(v) for v in cores]; laws=[tuple(z*z for z in v) for v in coeff]
groups={}
for k,p in enumerate(laws): groups.setdefault(p,[]).append(k)
counts={'general':0,'equal_magnitude':0,'additional':0}; examples=[]
def check_comb(ids,a,extra=False):
 ck(time.monotonic()-start<55)
 leaves=[cores[k] for k in ids]; bs=[coeff[k] for k in ids]; w=weights(a)
 table=tuple(leaves[leaf_index(x%(2**a),a)][x>>a] for x in range(2**(a+2)))
 actual_coeff=fw(table); p=tuple(z*z for z in actual_coeff)
 # Coherent closed coefficients for arbitrary shared-data leaves.
 suffix=list(bs[-1]); diffs=[None]*a
 for j in reversed(range(a)):
  diffs[j]=tuple(bs[j][t]-suffix[t] for t in range(4))
  suffix=[(bs[j][t]+suffix[t])/2 for t in range(4)]
 for t in range(4):
  ck(actual_coeff[t<<a]==suffix[t])
  for u in range(1,2**a):
   j=u.bit_length()-1
   ck(actual_coeff[u+(t<<a)]==F((-1)**(u.bit_count()-1),2**(j+1))*diffs[j][t])
 q=tuple(sum(w[l]*bs[l][t]**2 for l in range(a+1)) for t in range(4))
 ck(q==tuple(sum(p[u+(t<<a)] for u in range(2**a)) for t in range(4)))
 selector=sum(F(sum(table[x]!=table[x^(1<<j)] for x in range(len(table))),len(table)) for j in range(a))
 spectral_sel=sum(u.bit_count()*p[u+(t<<a)] for u in range(2**a) for t in range(4))
 ck(selector==spectral_sel)
 ck(sum(t.bit_count()*q[t] for t in range(4))==sum(w[l]*sum(t.bit_count()*laws[ids[l]][t] for t in range(4)) for l in range(a+1)))
 if a<=2:
  # Independent actual leaf posterior, not a rearranged root KL identity.
  js=entropy(q).copy(); kappa={}; avgc={}
  for l in range(a+1):
   js=add(js,entropy(laws[ids[l]]),-w[l])
   avgc=add(avgc,ce(laws[ids[l]],(F(1,4),)*4),w[l])
  for t in range(4):
   if not q[t]: continue
   kp=tuple(w[l]*laws[ids[l]][t]/q[t] for l in range(a+1))
   divergence=add(ce(kp,w).copy(),entropy(kp),-1)
   kappa=add(kappa,divergence,q[t])
  Q=tuple(F(1,4)*p[u+(t<<a)]/q[t] if q[t] else F(1,4)*(u==0) for t in range(4) for u in range(2**a))
  condH=add(entropy(p).copy(),entropy(q),-1)
  ledger=add(add(add(condH,avgc),js),kappa,-1)
  ck(sum(Q)==1); ck(ce(p,Q)==ledger)
 if not all(laws[k]==laws[ids[0]] for k in ids): return
 counts['equal_magnitude']+=1
 P=laws[ids[0]]; cond={}; phase_ent={}; phase_I=F(0)
 for t in range(4):
  if not P[t]: continue
  sig=tuple(1 if bs[l][t]>0 else -1 for l in range(a+1)); pp,jj=scalar_cache[sig]
  phase_ent=add(phase_ent,entropy(pp),P[t]); phase_I+=P[t]*jj; cond[t]=pp
  for u in range(2**a): ck(p[u+(t<<a)]==P[t]*pp[u])
 ck(phase_I==selector)
 ck(entropy(p)==add(entropy(P).copy(),phase_ent))
 for reference in [(F(1,4),)*4,tuple(z/2 for z in P)]:
  Q=tuple(reference[t]*cond.get(t,(F(1),)+(F(0),)*(2**a-1))[u] for t in range(4) for u in range(2**a))
  ck(sum(Q)==sum(reference)); ck(sum(Q)<=1)
  ck(ce(p,Q)==add(ce(P,reference).copy(),phase_ent))
 # The already certified scalar rows imply the positive weighted bound.
 ck(selector>=0); ck(selector!=0 or not phase_ent)
 if len(examples)<8 and selector: examples.append({'ids':ids,'a':a,'selector_I':str(selector),'phase_entropy':{str(k):str(v) for k,v in phase_ent.items()}})
mode=sys.argv[1]
if mode=='general':
 for a in (1,2):
  for ids in itertools.product(range(16),repeat=a+1): check_comb(ids,a); counts['general']+=1
 ck(counts['general']==4352); ck(counts['equal_magnitude']==624)
elif mode=='equal-a3':
 for group in groups.values():
  for ids in itertools.product(group,repeat=4): check_comb(ids,3,True); counts['additional']+=1
 ck(counts['additional']==4160); ck(counts['equal_magnitude']==4160)
else: raise ValueError(mode)
out={'status':'PASS','helper_version':'A011-phase-comb-v1.2','mode':mode,'counts':counts,'scalar_cases':len(scalar_cache),'exact_assertions':checks,'seconds':time.monotonic()-start,'memory':'80 MB estimate; peak not measured','examples':examples,'scope':'Finite reconstruction checks; all-depth proof in PHASE_COMB.md'}
(R/'out'/('EXACT_'+mode+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='examples'}))
