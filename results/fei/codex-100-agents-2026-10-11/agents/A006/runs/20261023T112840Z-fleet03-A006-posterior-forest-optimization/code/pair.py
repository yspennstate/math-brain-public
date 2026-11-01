from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time
from check import log2,SCALE
R=Path(__file__).resolve().parent.parent;start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
supports=[3,6,24,48];local=[[x for x in range(64) if x&~s==0] for s in supports]
def mu(x):return F(3,4) if not x else F(1,12)
out={};runs=set();total=F(0)
for masks in product(*local):
 active=[j for j,x in enumerate(masks) if x]
 for j in active:
  key=(j,masks);ck(key not in runs);runs.add(key)
  # Four equal1/4 priors; forced local subset has probability1/3.
  prob=F(1,12)
  for k,x in enumerate(masks):
   if k!=j:prob*=mu(x)
  union=0
  for x in masks:union|=x
  ck(union!=0);out[union]=out.get(union,F(0))+prob;total+=prob
ck(len(runs)==768 and total==1 and sum(out.values())==1)
ck(set(out)==set(range(1,64)))
truth=[1 if all(x&s for s in supports[:2]) and any(x&s==s for s in supports[2:]) else -1 for x in range(64)]
walsh=[sum(truth[x]*(-1 if (x&S).bit_count()%2 else 1) for x in range(64)) for S in range(64)]
I=F(sum(truth[x]!=truth[x^(1<<j)] for x in range(64) for j in range(6)),64)
ck(I==F(5,4));ck(I==F(sum(S.bit_count()*z*z for S,z in enumerate(walsh)),4096))
product_q=F(3,4)**2;product_D=2*F(2,3);surrogate=2*product_q*product_D
ck(surrogate==F(3,2) and surrogate!=I)
lo=hi=0
for S in range(1,64):
 a,b=log2(1/out[S]);lo+=walsh[S]**2*a;hi+=walsh[S]**2*b
cost=[F(lo,4096*SCALE),F(hi,4096*SCALE)]
ck(cost[0]<=cost[1]);ck(time.monotonic()-start<15)
result={'status':'PASS','actual_runs':len(runs),'truth_inputs':64,'assertions':checks,'I':str(I),'invalid_product_influence':str(surrogate),'C_interval':list(map(str,cost)),'C_over_I_interval':[str(x/I) for x in cost],'Q_total_mass':str(total),'seconds':time.monotonic()-start}
(R/'out/PAIR.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
