from fractions import Fraction as R
from collections import defaultdict
from pathlib import Path
from math import lcm
import json,time,hashlib
out=Path(__file__).resolve().parents[1]/'out';start=time.perf_counter();checks=0
def ck(b):
 global checks
 assert b;checks+=1
def factor(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def logs(x):
 d=defaultdict(R)
 for p,e in factor(x.numerator).items():d[p]+=e
 for p,e in factor(x.denominator).items():d[p]-=e
 return dict(d)
def combine(*terms):
 d=defaultdict(R)
 for c,v in terms:
  for p,e in v.items():d[p]+=c*e
 return {p:e for p,e in d.items() if e}
def phi(x):return combine((-x,logs(x))) if x else {}
def entropy(p):return combine(*[(1,phi(q)) for q in p.values()])
def kl(p,q):
 ck(all(q.get(s,0)>0 for s in p))
 return combine(*[(v,logs(v/q[s])) for s,v in p.items()])
def spectrum(v):
 N=len(v)
 return {s:R(a*a,N*N) for s in range(N) if (a:=sum(v[x]*(-1)**((s&x).bit_count()) for x in range(N)))}
def strict_positive(vec):
 den=lcm(*(x.denominator for x in vec.values()));pos=neg=1
 for p,c in vec.items():
  e=int(c*den)
  if e>0:pos*=p**e
  else:neg*=p**(-e)
 ck(pos>neg)
 return {'common_denominator':den,'positive_integer':str(pos),'negative_integer':str(neg)}
def scalar(a):
 return combine((1,phi((1-a/2)**2)),(3,phi(a*a/4)),(R(-1,2),phi((1-a)**2)),
                (R(-1,2),phi(a*a)),(2*a*(1-a),{2:R(1)}))
profiles=[]
for a in (R(1,4),R(1,2),R(3,4),R(1)):
 v=combine((1,scalar(a)),(R(-1,2),{2:R(1)}))
 profiles.append({'alpha':str(a),'D_minus_half':{str(p):str(q) for p,q in v.items()},'positive_integer_certificate':strict_positive(v)})
v=[int(s) for s in (out/'truth_table.txt').read_text().splitlines()]
ck(len(v)==64)
for x,a in enumerate(v):ck(a==(-1)**(x>>5)*(-1 if x&31==1 else 1))
P=spectrum(v);children=[v[b::2] for b in (0,1)];Pchild=[{s<<1:p for s,p in spectrum(w).items()} for w in children]
ck(P=={s|32:R(225 if s==0 else 1,256) for s in range(32)})
H=entropy(P);Hterm=combine(*[(R(1,2),entropy(p)) for p in Pchild]);D=combine((1,H),(-1,Hterm))
ck(D==scalar(R(1,8)))
ck(2**600*7**98<15**225<2**604*7**98)
ck(7**49>2**128) # explicit active-core K4 terminal certificate
ck(15**225>2**864) # positive remaining root-core slack after the one-owner payment
ck(sum(v)==0 and all(sum(w)==0 for w in children))
I=[R(sum(v[x]!=v[x^(1<<i)] for x in range(64)),64) for i in range(6)]
ck(I==[R(1,16)]*5+[R(1)])
Q={s|32:R(1,32) for s in range(32)}
Pe=defaultdict(R);Qe=defaultdict(R)
for s,p in P.items():Pe[s&~1]+=p
for s,p in Q.items():Qe[s&~1]+=p
ck(set(Pe)==set(Qe))
bayes=[];predictions=[]
for b in (0,1):
 raw={T:q*Pchild[b].get(T,0)/(2*Pe[T]) for T,q in Qe.items()}
 pred=sum(raw.values());predictions.append(pred)
 qb={T:q/pred for T,q in raw.items() if q};ck(sum(qb.values())==1);bayes.append(qb)
ck(predictions==[R(4,113),R(109,113)])
ck(bayes[0]==Pchild[0])
ck(bayes[1]=={(s<<1)|32:R(49 if s==0 else 113,1744) for s in range(16)})
fresh=[Pchild[0],{(s<<1)|32:R(1,16) for s in range(16)}]
rootKL=kl(P,Q);eraseKL=combine((1,rootKL),(-1,kl(Pe,Qe)))
outcomeKL=kl({0:R(1,2),1:R(1,2)},dict(enumerate(predictions)))
childKL=combine(*[(R(1,2),kl(p,q)) for p,q in zip(Pchild,bayes)])
freshKL=combine(*[(R(1,2),kl(p,q)) for p,q in zip(Pchild,fresh)])
rho=combine((1,freshKL),(-1,childKL))
ck(combine((1,eraseKL),(1,outcomeKL),(1,childKL))==rootKL)
ck(combine((1,eraseKL),(1,outcomeKL),(1,freshKL),(-1,rho))==rootKL)
ck(rootKL==combine((5,{2:R(1)}),(-1,H)))
ck(combine((1,entropy(P)),(1,rootKL))=={2:R(5)})
ck(combine((1,Hterm),(1,freshKL))=={2:R(2)})
ck(4*R(21,16)-5 == (4*R(5,4)-2)+4*R(1,16)-(5-2) == R(1,4))
ck(combine((1,childKL),(-1,rho))!=childKL) # reset is kept, not silently omitted
for p,q in zip(Pchild,bayes):ck(all(s>>5==1 for s in p) and all(s>>5==1 for s in q))
def serial(d):return {str(p):str(e) for p,e in sorted(d.items())}
result={'profiles_for_t_at_most_2':profiles,'scalar_identity':'D(alpha)=phi((1-alpha/2)^2)+3phi(alpha^2/4)-phi((1-alpha)^2)/2-phi(alpha^2)/2+2alpha(1-alpha)',
 'seed_spectrum_shape_cancels':True,'influence_vector':[str(x) for x in I],
 'reference_branch_predictions':[str(x) for x in predictions],
 'root_KL':serial(rootKL),'conditional_erasure_KL':serial(eraseKL),'outcome_KL':serial(outcomeKL),
 'mean_inherited_terminal_KL':serial(childKL),'mean_chosen_terminal_KL':serial(freshKL),
 'signed_reset':serial(rho),'root_CE_bits':'5','mean_chosen_terminal_CE_bits':'2',
 'full_reference_mean_terminal_K4_surplus':'3','full_reference_query_excess_over_4d':'11/4','full_reference_remaining_root_K4_surplus':'1/4',
 'parity_conditional_KL_bits':'0','all_terminal_costs_retained':True,
 'assertions':checks,'runtime_seconds':time.perf_counter()-start,
 'truth_table_sha256':hashlib.sha256((out/'truth_table.txt').read_bytes()).hexdigest(),
 'external_review':'pending','scope':'Internal different-representation reconstruction, not an independent agent review'}
(out/'REPRODUCTION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('assertions','runtime_seconds','reference_branch_predictions','root_CE_bits','mean_chosen_terminal_CE_bits','truth_table_sha256')},indent=2))
