from pathlib import Path
from fractions import Fraction as F
import json,sys,time,hashlib
import exact_utils as x
from functools import lru_cache
raw_logprime=x.logprime
@lru_cache(None)
def rounded_logprime(p):
 a,b=raw_logprime(p);B=1<<96
 return F((a*B).numerator//(a*B).denominator,B),F(-((-b*B).numerator//(-b*B).denominator),B)
x.logprime=rounded_logprime # rigorously outward dyadic bounds, not float estimates
R=Path(__file__).resolve().parents[1];START=time.monotonic();PILOT='--pilot' in sys.argv;C=0
def ck(z):
 global C
 C+=1;assert z,C
 if time.monotonic()-START>(55 if PILOT else 180):raise RuntimeError('frozen pilot55/full180s cap')
def le(a,b):return x.nonneg(x.sub(b,a))
def policy(f,mode):
 nodes=[];leaves=[]
 def go(g,dep,w):
  s=x.stats(g);n=s['n']
  if n==0 or (mode==1 and len(set(g))==1) or (mode==2 and dep>=1):leaves.append((w,s));return
  i=min(range(n),key=lambda j:(s['p'][j],j)) if mode==3 else 0
  raw=[x.stats(x.child(g,(i,),b)) for b in [0,1]]
  nxt=[x.stats(z['canonical']) if mode in [1,2] or(mode==3 and b) else z for b,z in enumerate(raw)]
  for old,new in zip(raw,nxt):ck(new['H']==old['H'] and new['I']<=old['I'])
  c=s['p'][i]+sum((old['I']-new['I'] for old,new in zip(raw,nxt)),F(0))/2
  L=x.sub(s['H'],x.plus(*(x.scale(F(1,2),z['H']) for z in nxt)))
  nodes.append((w,c,L,s['I']));ck(c>=0)
  # Carry actual tables explicitly; no identification through a statistics record.
  for b,z in enumerate(raw):
   h=z['canonical'] if mode in [1,2] or(mode==3 and b) else x.child(g,(i,),b)
   go(h,dep+1,w/2)
 go(f,0,F(1));return nodes,leaves
roots=[x.table(n,t) for n in range(3 if PILOT else 4) for t in range(1<<(1<<n))]
policies=certs=failures=0;nodecount=leafcount=0
stored=[]
for f in roots:
 s=x.stats(f)
 for mode in range(4):
  nodes,leaves=policy(f,mode);policies+=1;nodecount+=len(nodes);leafcount+=len(leaves)
  spend=sum((w*c for w,c,_,_ in nodes),F(0));leafI=sum((w*z['I'] for w,z in leaves),F(0))
  ck(spend+leafI==s['I'])
  LH=x.plus(*(x.scale(w,z['H']) for w,z in leaves));L=x.sub(s['H'],LH)
  ck(L==x.plus(*(x.scale(w,l) for w,_,l,_ in nodes)))
  for K in [0,1,2,4]:
   D=x.sub(s['H'],x.const(K*s['I']))
   bills=[(w,c,x.sub(l,x.const(K*c))) for w,c,l,_ in nodes]
   debts=[(w,z['I'],x.sub(z['H'],x.const(K*z['I']))) for w,z in leaves]
   ck(D==x.plus(*(x.scale(w,b) for w,_,b in bills+debts)))
   # Group the complete actual policy into one macro reduction.
   ck(x.sub(L,x.const(K*spend))==x.plus(*(x.scale(w,b) for w,_,b in bills)))
   for eps in [F(0),F(1,8),F(1,2),F(1),F(2)]:
    shifted=x.sub(D,x.const(eps*s['I']))
    ck(shifted==x.plus(*(x.scale(w,x.sub(b,x.const(eps*c))) for w,c,b in bills+debts)))
    ck(sum((w*eps*c for w,c,_ in bills+debts),F(0))==eps*s['I'])
    good=all(le(b,x.const(eps*c)) for _,c,b in bills+debts)
    if good:ck(le(D,x.const(eps*s['I'])));certs+=1
    else:failures+=1
  stored.append((f,nodes,leaves))
# Exact least-dimensional shifted-threshold selectors on the frozen domain.
critical=0
for threshold in [F(1),F(2)]:
 candidates=[f for f in roots if x.positive(x.sub(x.stats(f)['H'],x.const(threshold*x.stats(f)['I'])))]
 if not candidates:continue
 n=min(x.stats(f)['n'] for f in candidates);small=[f for f in roots if x.stats(f)['n']<n]
 ck(all(le(x.stats(f)['H'],x.const(threshold*x.stats(f)['I'])) for f in small))
 group=[f for f in candidates if x.stats(f)['n']==n];best=group[0]
 for f in group[1:]:
  a=x.sub(x.stats(f)['H'],x.const(threshold*x.stats(f)['I']));b=x.sub(x.stats(best)['H'],x.const(threshold*x.stats(best)['I']))
  if x.positive(x.sub(a,b)):best=f
 s=x.stats(best);ck(s['I']==s['amin'])
 for eps in [F(0),F(1,2)]:
  K=threshold-eps
  for mode in range(4):
   nodes,leaves=policy(best,mode)
   ck(all(le(x.sub(z['H'],x.const(K*z['I'])),x.const(eps*z['I'])) for _,z in leaves if z['n']<n))
   if all(z['n']<n for _,z in leaves):
    ck(any(not le(x.sub(L,x.const(K*c)),x.const(eps*c)) for _,c,L,_ in nodes));critical+=1
r={'status':'PASS','pilot':PILOT,'root_tables':len(roots),'complete_policies':policies,'internal_nodes':nodecount,'complete_leaves':leafcount,'successful_tolerance_certificates':certs,'rejected_local_tolerance_conditions':failures,'critical_shifted_threshold_guards':critical,'assertions':C+x.COUNT,'own_assertions':C,'utility_assertions':x.COUNT,'runtime_seconds':time.monotonic()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'utility_sha256':hashlib.sha256(Path(x.__file__).read_bytes()).hexdigest(),'arithmetic':'integer Walsh, actual physical restrictions, Fraction, prime-log identities and rational32-term atanh enclosures','scope':'four fixed policy rules, not all policy trees; general tolerance theorem is analytic'}
(R/'out'/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r))
