from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
import helper as h
from fractions import Fraction as F
from itertools import product
R=Path(__file__).resolve().parents[1]
start=time.perf_counter(); N=0
def ck(x,msg):
 global N
 assert x,msg
 N+=1
 assert time.perf_counter()-start<60,'frozen runtime'
def E(x):
 return (-1 if x&7==0 else 1)*(-1 if (x&1)==0 and (x&24)==0 else 1)
truth=[E(x) for x in range(32)]
orig=h.walsh(truth)
ck(sum(F(x,32) for x in truth)==F(5,8),'shared E mean')
inf=[F(sum(truth[x]!=truth[x^(1<<i)] for x in range(32)),32) for i in range(5)]
ck(inf==[F(3,8)]+[F(1,4)]*4,'actual overlap influence')
rows=[]; seen={}; failures=[]
pilot='--pilot' in sys.argv
domain=product([-1,0,1],repeat=3 if pilot else 5)
for raw in domain:
 if pilot:raw=tuple(raw)+(-1,-1)
 fixed={i:v for i,v in enumerate(raw) if v!=-1}
 rem=[i for i in range(5) if i not in fixed]
 def restrict(keep):
  ans=[]
  for y in range(1<<len(keep)):
   x=sum(v<<i for i,v in fixed.items())+sum(((y>>j)&1)<<i for j,i in enumerate(keep))
   ans.append(truth[x])
  return ans
 vals=restrict(rem)
 essential=[i for j,i in enumerate(rem) if any(vals[x]!=vals[x^(1<<j)] for x in range(len(vals)))]
 ghosts=[i for i in rem if i not in essential]
 for i in ghosts:fixed[i]=0
 vals=restrict(essential)
 P=h.walsh(vals); Q=h.project(orig,essential)
 nu=F(sum(vals),len(vals)); I=sum(t.bit_count()*p for t,p in P.items())
 edges=F(sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals)) for j in range(len(essential))),len(vals))
 ck(I==edges,'Walsh vs actual edges after cleanup')
 ck(sum(Q.values())==1,'full original reference marginal normalization')
 ck(all(Q.get(t,F(0))>0 for t,p in P.items() if p),'no discarded support')
 C=h.cehist([(1,P.get(t,F(0)),Q.get(t,F(0))) for t in range(1<<len(essential))])
 slack=h.sub(h.val(4*I),C)
 ck(slack[0]>=0,'cleaned interacting E seed code <=4 actual influence')
 den=len(vals)**2
 exp=4*I*den
 ck(exp.denominator==1,'integer certificate clearing factor')
 lhs=1<<int(exp);rhs=1
 for t,pp in P.items():
  power=pp*den;ck(power.denominator==1,'integer spectral multiplicity')
  qq=Q[t];lhs*=qq.numerator**int(power);rhs*=qq.denominator**int(power)
 ck(lhs>=rhs,'portable exact integer product certificate of full seed CE<=4I')
 ck(not I or abs(nu)<=F(3,4),'nonconstant mean bound')
 if not I:ck(Q=={0:F(1)} and C==h.val(0),'constant cleanup removes ALL reference ghosts')
 key=json.dumps([essential,vals],separators=(',',':'))
 item={'assignment':raw,'essential':essential,'ghosts':ghosts,'values':vals,'mean':str(nu),'I':str(I),'Q':[str(Q.get(t,F(0))) for t in range(1<<len(essential))],'P':[str(P.get(t,F(0))) for t in range(1<<len(essential))],'CE_interval':h.pack(C),'margin_interval':h.pack(slack),'R0_minus_mean_squared':str(Q.get(0,F(0))-nu*nu),'integer_certificate':{'clearing_denominator':den,'lhs':str(lhs),'rhs':str(rhs)}}
 rows.append(item);seen[key]=item
result={'status':'PASS','cases':len(rows),'distinct_cleaned_states':len(seen),'assertions':N,'helper_assertions':h.N,'seconds':time.perf_counter()-start,'R0_counterexamples':[x for x in rows if F(x['R0_minus_mean_squared'])<0],'rows':rows}
(R/'out'/('BLOCK_PILOT.json' if pilot else 'BLOCK_CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','cases','distinct_cleaned_states','assertions','helper_assertions','seconds']}))
