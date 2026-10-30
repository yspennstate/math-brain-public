import check as C
from fractions import Fraction as F
import json,time
rows=[];positive=[]
for a in [2,3,4]:
 for b in [0,1]:
  for r in [1,2,3]:
   for j in range(a):
    Pg=C.spec(C.source(a,b));v=1-Pg[0];N=len(Pg)
    R=[Pg[0]]+[v/F(16*(N-2))]*(N-1);R[1<<j]=F(15,16)*v
    C.ck(sum(R)==1)
    vals,P,Q=C.floor(a,b,r,R);old=C.marginal(Q,j);V=C.marginal(R,j)
    debt=C.sub(C.mul(-1,C.lg(old[0])),C.mul(-1,C.lg(V[0])))
    C.one(a,b,r,R,j)
    row={'a':a,'b':b,'r':r,'j':j,'complementary_debt_interval':[str(x) for x in debt]}
    rows.append(row)
    if debt[0]>0:positive.append(row)
C.ck(len(rows)==54);C.ck(len(positive)>0)
result={'status':'PASS','cases':len(rows),'positive_complementary_debts':len(positive),'positive_reset_calls':C.POSITIVE,'assertions':C.COUNT,'runtime_seconds':time.perf_counter()-C.START,'first_positive_complement':positive[0],'rows':rows}
C.dump('ADVERSARIAL_VALIDATION.json',result)
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
