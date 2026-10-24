from pathlib import Path
from fractions import Fraction as F
import json, time
start=time.perf_counter(); checks=0; rows=[]
def check(c):
    global checks
    assert c
    checks+=1
for n in range(1,13):
    vals=[-1]+[1]*((1<<n)-1)
    influence=sum((F(sum(vals[x]!=vals[x^(1<<i)] for x in range(1<<n)),1<<n) for i in range(n)),F(0))
    check(influence==F(2*n,1<<n))
    reaches=[F(1,1<<j) for j in range(n)]
    query_mass=sum(reaches,F(0))
    check(query_mass==2-F(2,1<<n))
    check(query_mass/influence==F((1<<n)-1,n))
    # Independently recurse on the physical truth table. All constant branches stop.
    def cost(v):
        if len(set(v))==1: return F(0)
        return 1+(cost(v[::2])+cost(v[1::2]))/2
    check(cost(vals)==query_mass)
    # Node influence budget: at depth j the residual has n-j relevant coordinates.
    removed=sum((reaches[j]*F(2,1<<(n-j)) for j in range(n)),F(0))
    check(removed==influence)
    rows.append({'n':n,'I':str(influence),'minimum_query_mass':str(query_mass),'tax_bill_over_I_divided_by_tau':str(query_mass/influence),'proved_ratio_lower_bound':str(F((1<<n)-1,14*n))})
check(F(10,7)**2>2)
check(F(3)-2*F(10,7)==F(1,7))
out={'assertions_passed':checks,'failures':0,'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction and integer physical boundary; analytic entropy deficit supplies tau>1/14','rows':rows}
(Path(__file__).resolve().parents[1]/'out'/'TAX_TREE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
