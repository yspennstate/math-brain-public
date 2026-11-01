from fractions import Fraction as Q
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import json,time,hashlib,sys
OUT=Path(__file__).resolve().parents[1]/'out';pilot='--pilot' in sys.argv
start=time.perf_counter();checks=0
def ck(b):
 global checks
 assert b
 checks+=1
def walsh(v):
 a=list(v);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):
    x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
  h*=2
 return a
def law(v,shift=0):return {s<<shift:Q(a*a,len(v)**2) for s,a in enumerate(walsh(v)) if a}
def fac(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def entropy(p):
 d=defaultdict(Q)
 for q in p.values():
  for a,e in fac(q.denominator).items():d[a]+=q*e
  for a,e in fac(q.numerator).items():d[a]-=q*e
 return {a:b for a,b in d.items() if b}
def add(*terms):
 d=defaultdict(Q)
 for k,v in terms:
  for a,b in v.items():d[a]+=k*b
 return {a:b for a,b in d.items() if b}
def ln(x):
 z=(x-1)/(x+1);lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(16)),Q(0))
 return lo,lo+2*z**33/(33*(1-z*z))
@lru_cache(None)
def log2(p):
 k=p.bit_length()-1;lo,hi=ln(Q(p,1<<k));a,b=ln(Q(2))
 return Q(k)+lo/b,Q(k)+hi/a
def bound(v):
 lo=hi=Q(0)
 for a,b in v.items():
  x,y=log2(a);lo+=b*(x if b>0 else y);hi+=b*(y if b>0 else x)
 # Outward rational rounding makes persisted bounds small and readable.
 D=10**9
 return Q(lo.numerator*D//lo.denominator,D),Q(-((-hi.numerator*D)//hi.denominator),D)
def vec(v):return {str(a):str(b) for a,b in sorted(v.items())}
def influences(v):
 n=len(v).bit_length()-1
 return [Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v)) for i in range(n)]
results=[];witness=None
cases=[(t,k) for t in range(4) for k in range(1<<(1<<t))]
if pilot:cases=[(t,k) for t,k in cases if t<=1]+[(3,1)]
for t,code in cases:
 seed=[1-2*((code>>w)&1) for w in range(1<<t)]
 alpha=Q(seed.count(-1),len(seed));n=t+3
 core=[1+((x&1)*(1-(x>>1&1)))*(seed[x>>2]-1) for x in range(1<<(t+2))]
 full=[core[x&((1<<(t+2))-1)]*(-1)**(x>>(t+2)) for x in range(1<<n)]
 P=law(full);Pcore=law(core);children=[full[b::2] for b in (0,1)];Pb=[law(v,1) for v in children]
 H=entropy(P);Hc=add(*[(Q(1,2),entropy(d)) for d in Pb]);D=add((1,H),(-1,Hc))
 er=defaultdict(Q)
 for s,p in P.items():er[s&~1]+=p
 He=entropy(er);M=add((1,H),(-1,He));J=add((1,He),(-1,Hc))
 ck(add((1,M),(1,J))==D)
 ck(sum(P.values())==1);ck(H==entropy(Pcore))
 for b in (0,1):
  qbranch=Q(0);bayes={}
  for T,q in er.items():
   K=Pb[b].get(T,Q(0))/(2*q)
   ck(0<=K<=1);qbranch+=q*K
   if K:bayes[T]=q*K
  ck(qbranch==Q(1,2));bayes={s:p/qbranch for s,p in bayes.items()}
  ck(bayes==Pb[b]);ck(sum(bayes.values())==1)
  ck(sum(children[b])==0) # common parity remains at both physical terminals
 I= sum(influences(full));Ichild=sum((sum(influences(v))/2 for v in children),Q(0))
 ck(I-Ichild==alpha/2)
 ck(I==1+alpha+sum(influences(seed))/4)
 ck(Ichild==1+alpha/2+sum(influences(seed))/4)
 lab=Q(1) if alpha else Q(0);labchild=lab/2;kappa=lab-labchild
 pre=alpha-alpha*alpha/2;prechild=alpha*(1-alpha);prekap=pre-prechild
 ck(prekap==alpha*alpha/2);ck(kappa-prekap==(1-alpha*alpha)/2 if alpha else kappa==0)
 residual=add((1,D),(-kappa,{2:Q(1)}));blo,bhi=bound(residual)
 if residual:ck(not (blo<=0<=bhi))
 essential_seed=all(d>0 for d in influences(seed));all_essential=bool(alpha and essential_seed)
 if alpha:
  ck(kappa/(alpha/2)==1/alpha)
  if t<=2:ck(blo>=0)
 row={'t':t,'seed_code':code,'alpha':str(alpha),'n_nominal':n,'all_root_variables_essential':all_essential,
      'I_root':str(I),'I_terminal_mean':str(Ichild),'removed_influence':str(alpha/2),
      'labelled_release':str(kappa),'pre_factor_release':str(prekap),
      'H_root':vec(H),'H_terminal_mean':vec(Hc),'M':vec(M),'J':vec(J),'D':vec(D),
      'signed_residual':vec(residual),'residual_bounds':[str(blo),str(bhi)],
      'negative_residual':bhi<0,'strict_rate4_release_failure':kappa>4*(alpha/2),
      'normalized_reference':'Q_root=P_root; identical actual physical reveal kernel; Bayes children Q_b=P_b; all source/erasure/outcome/child KL zero'}
 results.append(row)
 if (t,code)==(3,1):
  ck(alpha==Q(1,8));ck(all_essential);ck(I==Q(21,16));ck(Ichild==Q(5,4))
  ck(kappa==Q(1,2));ck(prekap==Q(1,128));ck(D=={2:Q(5),7:Q(49,64),3:Q(-225,128),5:Q(-225,128)})
  # Exact integer product sandwich: 9/32 < actual decrement < 5/16.
  B=15**225;A=7**98
  ck((2**600)*A<B<(2**604)*A)
  ck(bhi<Q(-3,16));ck(kappa-4*(alpha/2)==Q(1,4))
  active_slack=add((Q(2),{2:Q(1)}),(-1,entropy(Pb[1])))
  average_core_slack=add((Q(1),{2:Q(1)}),(-1,Hc))
  true_excess=add((1,D),(Q(-1,4),{2:Q(1)}))
  root_core_slack=add((Q(5,4),{2:Q(1)}),(-1,H))
  ck(add((1,average_core_slack),(-1,true_excess))==root_core_slack)
  ck(bound(root_core_slack)[0]>0);ck(bound(active_slack)[0]>0)
  row.update({'active_core_K4_slack':vec(active_slack),'mean_core_K4_slack':vec(average_core_slack),
    'true_rate4_excess':vec(true_excess),'root_core_K4_slack':vec(root_core_slack),
    'truth_table':full,'coordinate_order':'LSB a,z,w0,w1,w2,y; cube sign=(-1)^bit',
    'integer_sign_certificate':'2^600 * 7^98 < 15^225 < 2^604 * 7^98',
    'pre_factor_root_reserve':'15/128','post_factor_root_reserve':'1',
    'pre_factor_mean_terminal_reserve':'7/64','post_factor_mean_terminal_reserve':'1/2',
    'common_factor_release_boost':'63/128','signed_residual_shift':'-63/128'})
  witness=row
  (OUT/'WITNESS.json').write_text(json.dumps(row,indent=2)+'\n',encoding='utf-8')
  (OUT/'truth_table.txt').write_text(''.join(str(v)+'\n' for v in full),encoding='ascii')
suffix='PILOT' if pilot else 'FULL'
negative=[r for r in results if r['negative_residual']]
rate=[r for r in results if r['strict_rate4_release_failure']]
summary={'helper_version':'A049-contracted-core-reveal-v1','cases':len(cases),'assertions':checks,
 'negative_residual_cases':len(negative),'strict_rate4_release_failures':len(rate),
 'minimum_nominal_n_negative_residual':min(r['n_nominal'] for r in negative),
 'minimum_nominal_n_rate4_release_failure':min(r['n_nominal'] for r in rate),
 'runtime_seconds':time.perf_counter()-start,'all_checks':'PASS','external_review':'pending','FEI':'OPEN'}
(OUT/(suffix+'_CASES.json')).write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
(OUT/(suffix+'_CHECK.json')).write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
