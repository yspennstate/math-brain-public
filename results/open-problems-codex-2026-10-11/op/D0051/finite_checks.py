import math,json,random,pathlib
from fractions import Fraction as F
R=pathlib.Path(__file__).resolve().parent
x=1/math.sqrt(6);Q=5/math.sqrt(6);C=(4+math.sqrt(15))/6;c=x*(Q-2)
rows=[]
for a in [-2,-1.99,-1.9,-1,-x,0,0.5,1,1.9,1.99,2]:
 ambient=2-a*a/2;annulus=x*(Q-a);B=max(0,min(ambient,annulus,C))
 rows.append({'alpha':a,'ambient_upper':ambient,'annulus_upper':annulus,'Euclidean_combined_upper':B,'metric_combined_upper':min(1,B/c)})
rng=random.Random(51);checked=0
for i in range(10000):
 ellJ=F(rng.randint(1,1000),100);ellI=ellJ*F(rng.randint(1,2000),1000)
 gap=(ellI+ellJ)/2*F(rng.randint(-999,999),1000)
 assert abs(gap)+ellI/2<F(5,2)*ellJ
 checked+=1
# Exact rational arithmetic for KPZ control.
assert F(5,6)-F(1,6)/2==F(3,4)
assert F(5,6)+F(1,6)==1
result={'purpose':'Finite referee checks, not an LFPP simulation or spectrum estimate','interval_containment_checks':checked,'exact_rational_kpz_value':'3/4','Brownian_geodesic_upper':C,'Brownian_forward_Holder_supremum':c,'table':rows}
(R/'numerical_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='table'},indent=2))
