from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
import json,sys,time
import entropy_tools as E
ROOT=Path(__file__).resolve().parents[1];START=time.perf_counter();COUNT=0
def ck(x):
 global COUNT
 COUNT+=1
 if not x:raise AssertionError(COUNT)
def save(n,x):(ROOT/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def ser(v):return {str(p):str(c) for p,c in v.items()}
def entropy(p):return E.H(tuple(v for v in p.values() if v))
@lru_cache(None)
def logvec(x):
 ck(x>0)
 ans={}
 for p,c in E.factors(x.numerator).items():ans[p]=F(c)
 for p,c in E.factors(x.denominator).items():ans[p]=ans.get(p,F(0))-c
 return {p:c for p,c in ans.items() if c}
def kl(p,q):
 ck(sum(p.values())==sum(q.values())==1)
 return E.add(*(E.mul(logvec(v/q.get(s,F(0))),v) for s,v in p.items() if v))
def project(p,mask):
 out=defaultdict(F)
 for s,v in p.items():out[s&mask]+=v
 return dict(out)
def product(p,labels):
 ds={i:sum(v for s,v in p.items() if s>>i&1) for i in labels};out={}
 for x in range(1<<len(labels)):
  s=sum(1<<i for j,i in enumerate(labels) if x>>j&1);v=F(1)
  for i in labels:v*=ds[i] if s>>i&1 else 1-ds[i]
  if v:out[s]=v
 ck(sum(out.values())==1);return out
def spectrum(t,labels):
 vals=list(t);N=len(t);step=1
 while step<N:
  for j in range(0,N,2*step):
   for k in range(step):
    a,b=vals[j+k],vals[j+k+step];vals[j+k],vals[j+k+step]=a+b,a-b
  step*=2
 p={sum(1<<i for j,i in enumerate(labels) if s>>j&1):F(a*a,N*N) for s,a in enumerate(vals) if a}
 ck(sum(p.values())==1);return p
def restrict(t,i,b):return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
def condkl(p,q,mask):return E.sub(kl(p,q),kl(project(p,mask),project(q,mask)))
def sign(v):
 if not v:return 0
 lo,hi=E.interval(v)
 if lo>0:return 1
 if hi<0:return -1
 raise AssertionError('Undecided sign '+str(v))
def audit(t,i,Z,name,q=None,matched_fresh=False):
 n=len(t).bit_length()-1;labels=tuple(range(n));allmask=(1<<n)-1
 p=spectrum(t,labels);remain=tuple(j for j in labels if j!=i);erased=allmask&~(1<<i)
 children=[spectrum(restrict(t,i,b),remain) for b in [0,1]]
 pe=project(p,erased);q=product(p,labels) if q is None else q;qe=project(q,erased)
 ck(all(pe.get(s,F(0))==(children[0].get(s,F(0))+children[1].get(s,F(0)))/2 for s in set(pe)|set(children[0])|set(children[1])))
 transported=[defaultdict(F),defaultdict(F)]
 for s,v in qe.items():
  ks=[children[b].get(s,F(0))/(2*pe[s]) if pe.get(s,F(0)) else F(1,2) for b in [0,1]]
  ck(sum(ks)==1)
  for b in [0,1]:transported[b][s]+=v*ks[b]
 qout=[sum(x.values()) for x in transported];ck(sum(qout)==1 and min(qout)>0)
 bayes=[{s:v/qout[b] for s,v in transported[b].items() if v} for b in [0,1]]
 fresh=[product(c,remain) for c in children]
 if matched_fresh:
  fresh=[]
  for c in children:
   cmask=erased&~Z;cp=project(c,cmask);cq=product(cp,tuple(j for j in remain if not Z>>j&1))
   fresh.append({s:cq[s&cmask]*v/cp[s&cmask] for s,v in c.items()})
  for ref in fresh:ck(sum(ref.values())==1)
 outcome=kl({0:F(1,2),1:F(1,2)},{0:qout[0],1:qout[1]})
 source=kl(p,q);eraseKL=E.sub(source,kl(pe,qe))
 inherited=E.mul(E.add(*(kl(children[b],bayes[b]) for b in [0,1])),F(1,2))
 ck(source==E.add(eraseKL,outcome,inherited))
 fullreset=E.mul(E.add(*(E.sub(kl(children[b],fresh[b]),kl(children[b],bayes[b])) for b in [0,1])),F(1,2))
 resetquot=E.mul(E.add(*(E.sub(kl(project(children[b],erased&~Z),project(fresh[b],erased&~Z)),kl(project(children[b],erased&~Z),project(bayes[b],erased&~Z))) for b in [0,1])),F(1,2))
 cb=E.mul(E.add(*(condkl(children[b],bayes[b],erased&~Z) for b in [0,1])),F(1,2))
 cf=E.mul(E.add(*(condkl(children[b],fresh[b],erased&~Z) for b in [0,1])),F(1,2))
 extra=E.sub(cf,cb);ck(extra==E.sub(fullreset,resetquot))
 L=E.sub(entropy(p),entropy(project(p,allmask&~Z)))
 Lleaf=E.mul(E.add(*(E.sub(entropy(c),entropy(project(c,erased&~Z))) for c in children)),F(1,2))
 drift=E.sub(L,Lleaf)
 joint_account={}
 if q==product(p,labels) and not matched_fresh:
  root_cond=condkl(p,q,allmask&~Z);erased_cond=condkl(pe,qe,erased&~Z)
  gamma={}
  for j in labels:
   if Z>>j&1:
    d=sum(v for s,v in p.items() if s>>j&1)
    gamma=E.add(gamma,E.sub(E.hb(d),E.mul(E.add(*(E.hb(sum(v for s,v in c.items() if s>>j&1)) for c in children)),F(1,2))))
  debit=E.sub(cf,root_cond)
  ck(debit==E.sub(drift,gamma));ck(sign(gamma)>=0)
  release=E.sub(erased_cond,cb);ck(sign(release)>=0)
  erasure_cond=E.sub(root_cond,erased_cond)
  ck(E.sub(E.add(erasure_cond,release),extra)==E.sub(root_cond,cf))
  joint_account={'conditional_root_KL':ser(root_cond),'conditional_erased_KL':ser(erased_cond),'conditional_erasure_release':ser(erasure_cond),'conditional_branch_release':ser(release),'spectator_marginal_JS':ser(gamma),'joint_conditional_debit':ser(debit)}
 M=E.sub(entropy(p),entropy(pe));Mq=E.sub(entropy(project(p,allmask&~Z)),entropy(project(pe,erased&~Z)))
 J=E.sub(entropy(pe),E.mul(E.add(*(entropy(c) for c in children)),F(1,2)))
 Jq=E.sub(entropy(project(pe,erased&~Z)),E.mul(E.add(*(entropy(project(c,erased&~Z)) for c in children)),F(1,2)))
 rootcorr=E.sub(Mq,M);branchcorr=E.sub(J,Jq)
 ck(drift==E.sub(branchcorr,rootcorr))
 for v in [rootcorr,branchcorr,cf,cb]:ck(sign(v)>=0)
 inf=F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
 infl=sum(F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)) for j in labels)
 childinfl=sum(F(sum(restrict(t,i,b)[x]!=restrict(t,i,b)[x^(1<<j)] for x in range(len(t)//2)),len(t)//2) for j in range(n-1) for b in [0,1])/2
 ck(infl==inf+childinfl)
 if sign(drift)>0:
  _,ln2hi=E.ln_unit(F(2));ck(E.interval(drift)[1]<=2*inf/ln2hi)
 # Likelihood sufficiency is tested on reference-positive rows too.
 ratios={};sufficient=True
 for s,v in q.items():
  T=s&erased&~Z;r=p.get(s,F(0))/v
  if r<=0:sufficient=False
  if T in ratios and ratios[T]!=r:sufficient=False
  ratios[T]=r
 if sufficient:ck(not cb)
 result={'name':name,'n':n,'query':i,'spectator_mask':Z,'truth_table':list(t),'influence':str(inf),'total_I':str(infl),'terminal_I':str(childinfl),
  'source_law':{str(s):str(v) for s,v in p.items()},'source_reference':{str(s):str(v) for s,v in q.items()},
  'children':[{'law':{str(s):str(v) for s,v in children[b].items()},'inherited_reference':{str(s):str(v) for s,v in bayes[b].items()},'fresh_product_reference':{str(s):str(v) for s,v in fresh[b].items()}} for b in [0,1]],
  'branch_reference_predictions':list(map(str,qout)),'entropy_drift':ser(drift),'entropy_drift_sign':sign(drift),
  'conditional_inherited_KL':ser(cb),'conditional_fresh_KL':ser(cf),'conditional_reset':ser(extra),'conditional_reset_sign':sign(extra),
  'conditional_reset_interval':E.outward(E.interval(extra),80),'full_signed_reset':ser(fullreset),'quotient_signed_reset':ser(resetquot),
  'terminal_H':ser(E.mul(E.add(*(entropy(c) for c in children)),F(1,2))),'L_root':ser(L),'L_terminal':ser(Lleaf),'sufficient_retained_likelihood':sufficient}
 result.update(joint_account)
 return result
def main():
 pilot='--pilot' in sys.argv;cases=0;witnesses=[];counts=defaultdict(int)
 for mask in range(16 if pilot else 256):
  t=tuple(1-2*(mask>>x&1) for x in range(8));r=audit(t,0,1<<2,'mask_'+str(mask));cases+=1
  counts[str((r['entropy_drift_sign'],r['conditional_reset_sign']))]+=1
  if F(r['influence']) and r['entropy_drift_sign']<=0 and r['conditional_reset_sign']>0:
   witnesses.append(r);save('WITNESSES.json',witnesses)
 for n in ([1,2] if pilot else [1,2,3,4]):
  # Reached A038 gate: x=0 -> (-1)^a, x=1 -> +1 unless b and v negative.
  t=[]
  for z in range(1<<(n+3)):
   x,a,b=z&1,z>>1&1,z>>2&1;y=z>>3;v=-1 if y==0 else 1
   t.append((-1)**a if x==0 else v if b else 1)
  r=audit(tuple(t),1,((1<<(n+3))-1)^7,'EXPOSED_v'+str(n));cases+=1;save(r['name']+'.json',r)
  ck(r['branch_reference_predictions']==['1/2','1/2'])
 # Actual matched likelihood example h2(C)*h3(U,Z), query U.
 t=tuple((-1 if x&3==3 else 1)*(-1 if x>>2==7 else 1) for x in range(32))
 pc=spectrum((1,1,1,-1),(0,1));pd=spectrum((1,1,1,1,1,1,1,-1),(2,3,4))
 for kind,refc in [('flat',{s:F(1,4) for s in range(4)}),('nonflat',{0:F(1,2),1:F(1,4),2:F(1,8),3:F(1,8)})]:
  q={s|z:p*v for s,p in refc.items() for z,v in pd.items()}
  r=audit(t,2,(1<<3)|(1<<4),'MATCHED_'+kind,q);cases+=1;save(r['name']+'.json',r)
  ck(r['sufficient_retained_likelihood'] and not r['conditional_inherited_KL'])
  ck(r['entropy_drift']=={'2':'1','3':'-3/8'})
 ck(cases==(20 if pilot else 262));ck(time.perf_counter()-START<(60 if pilot else 120))
 result={'status':'PASS','cases':cases,'primary_assertions':COUNT,'entropy_helper_assertions':E.ASSERTIONS,'runtime_seconds':time.perf_counter()-START,'pilot':pilot,'nonpositive_entropy_positive_KL_witnesses':len(witnesses),'three_bit_sign_counts':dict(counts),'float_used':False}
 save('PILOT.json' if pilot else 'RESULT.json',result);print(json.dumps(result))
if __name__=='__main__':main()
