from pathlib import Path
from itertools import combinations
import json, sys, time
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0;cases=0;budgets=0;inherited=0;examples={};profiles={}
def ck(x):
 global checks
 assert x
 checks+=1
 if time.perf_counter()-start>55:raise RuntimeError('frozen runtime cap')
def rank(vs):
 b={}
 for v in vs:
  while v:
   k=v.bit_length()
   if k in b:v^=b[k]
   else:b[k]=v;break
 return len(b)
def labels_for(n,U):
 left=set(U);labels={};j=0
 while left:
  stack=[left.pop()]
  while stack:
   x=stack.pop();labels[x]=j
   for i in range(n):
    y=x^(1<<i)
    if y in left:left.remove(y);stack.append(y)
  j+=1
 return labels
cache={}
def test(n,labels,source):
 global cases,budgets,inherited
 N=1<<n;U=set(labels);vs=list(range(1,N));mass=len(U)
 if n not in cache:cache[n]=[b for b in combinations(vs,n) if rank(b)==n]
 bases=cache[n]
 w={v:sum((x in U)!=((x^v) in U) for x in range(N)) for v in vs}
 gamma={v:sum((x^v) in U and labels[x]!=labels[x^v] for x in U) for v in vs}
 ell={v:w[v]+2*gamma[v] for v in vs}
 ck(all(0<=ell[v]<=2*mass for v in vs))
 ck(all(gamma[1<<i]==0 for i in range(n)))
 I0=sum(w[1<<i] for i in range(n));cost={b:sum(ell[v] for v in b) for b in bases};M=min(cost.values())
 ck(M<=I0)
 levels=sorted(set(ell.values()));lam={}
 for v in vs:
  lam[v]=next(t for t in levels if rank([z for z in vs if ell[z]<=t]+[v])==rank([z for z in vs if ell[z]<=t]))
  forced=min(c for b,c in cost.items() if v in b)
  ck(forced==M+ell[v]-lam[v]);ck(0<=lam[v]<=ell[v])
 T=[v for v in vs if ell[v]>=mass]
 tau=min((ell[v]-lam[v] for v in T),default=None)
 paid=[b for b in bases if any(v in T for v in b)]
 F=min((cost[b] for b in paid),default=None)
 ck((F is None)==(tau is None))
 if F is not None:ck(F==M+tau)
 ck((tau==0)==(rank([v for v in vs if ell[v]<mass])<n))
 ordinary={b:sum(w[v] for v in b) for b in bases};M0=min(ordinary.values());lam0={}
 for v in vs:
  lam0[v]=next(t for t in sorted(set(w.values())) if rank([z for z in vs if w[z]<=t]+[v])==rank([z for z in vs if w[z]<=t]))
  ck(min(c for b,c in ordinary.items() if v in b)==M0+w[v]-lam0[v])
 marked=[(ordinary[b]+2*gamma[v],b,v) for b in bases for v in b if v in T]
 best0=min(marked,default=None);tau0=min((ell[v]-lam0[v] for v in T),default=None)
 ck((best0 is None)==(tau0 is None))
 if best0 is not None:
  ck(best0[0]==M0+tau0);ck(best0[0]<=F)
 # Exhaust every half-grid historical debit; formula is analytic for all real u.
 for twice_u in range(2*I0+1):
  eligible=[b for b in paid if 2*cost[b]<=2*I0-twice_u]
  predicted=F is not None and 2*F<=2*I0-twice_u
  ck(bool(eligible)==predicted);budgets+=1
  admitted0=best0 is not None and 2*best0[0]<=2*I0-twice_u
  ck(admitted0==(tau0 is not None and 2*(M0+tau0)<=2*I0-twice_u))
  if admitted0:
   _,b0,v0=best0;rho0=I0-ordinary[b0]
   ck(2*rho0-twice_u>=4*gamma[v0]);ck(ell[v0]>=mass)
  if eligible:
   b=min(eligible,key=lambda b:cost[b]);v=next(v for v in b if v in T)
   rho=I0-sum(w[z] for z in b);G=sum(gamma[z] for z in b)
   ck(2*rho==2*(I0-cost[b])+4*G)
   ck(2*rho-twice_u>=4*gamma[v]);ck(ell[v]>=mass)
 cases+=1;inherited+=int(source['kind']=='inherited')
 key='empty_high' if tau is None else ('zero_surcharge' if tau==0 else ('positive_surcharge_paid' if F<=I0 else 'positive_surcharge_unpaid'))
 profiles[key]=profiles.get(key,0)+1
 detail={'n':n,'labels':{str(x):l for x,l in labels.items()},'source':source,'I0':I0,'M':M,'tau':tau,'forced_cost':F,'mass_count':mass,'normalizer':N,'best_qualifying_basis':min(paid,key=lambda b:cost[b]) if paid else None,'ell':ell,'lambda':lam}
 detail.update({'M0':M0,'tau0':tau0,'lambda0':lam0,'best_singleton':best0})
 if key not in examples:examples[key]=detail
 if F is not None and F<I0 and 'debit_changes_admission' not in examples:examples['debit_changes_admission']=detail
 if paid:
  b=min(paid,key=lambda b:cost[b]);G=sum(gamma[z] for z in b)
  if G and F<=I0 and 'positive_flux_paid' not in examples:examples['positive_flux_paid']=detail
 if best0 is not None and best0[0]<F and 'singleton_strict_improvement' not in examples:examples['singleton_strict_improvement']=detail
 if best0 is not None and best0[0]<=I0<F and 'singleton_only_paid' not in examples:examples['singleton_only_paid']=detail
pilot='--pilot' in sys.argv
four='--four' in sys.argv
roots=0
for n in ([4] if four else range(1,3 if pilot else 4)):
 N=1<<n
 masks=sorted({(1103515245*j+12345)&65535 for j in range(64)}) if four else range(1,1<<N)
 for mask in masks:
  if mask==0:continue
  labs=labels_for(n,{x for x in range(N) if mask>>x&1});roots+=1
  test(n,labs,{'kind':'root','mask':mask})
  if n>=2:
   for i in range(n):
    rem=[j for j in range(n) if j!=i]
    for bit in range(2):
     child={y:labs[x] for y in range(1<<(n-1)) if (x:=((bit<<i)|sum(((y>>j)&1)<<r for j,r in enumerate(rem)))) in labs}
     if child:test(n-1,child,{'kind':'inherited','root_n':n,'root_mask':mask,'coordinate':i,'bit':bit})
out={'status':'PASS','pilot':pilot,'assertions':checks,'root_count':roots,'cases':cases,'inherited_cases':inherited,'old_debit_tests':budgets,'profiles':profiles,'seconds':time.perf_counter()-start,'arithmetic':'integer counts and doubled integer debit, exact'}
(R/'out'/('N4_CHECK.json' if four else 'PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
if not pilot:(R/'out'/('N4_EXAMPLES.json' if four else 'EXAMPLES.json')).write_text(json.dumps(examples,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
