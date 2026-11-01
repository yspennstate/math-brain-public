from fractions import Fraction as F
from pathlib import Path
import json
params=[(F(1),F(1,2),F(1),F(1,2)),(F(3,4),F(3,7),F(3,4),F(3,7)),(F(1,2),F(1,3),F(1),F(1,2))]
count=0
for a,b,c,d in params:
    assert a-b-a*b==0 and c-d-c*d==0
    for i in range(11):
      for j in range(11-i):
       for l in range(11-i-j):
        x=[F(i,10),F(j,10),F(l,10),F(10-i-j-l,10)]
        P=x[0]*x[2]; u=x[1]; v=x[3]
        Q=P*(1+a*u-d*v)*(1-b*u+c*v)
        assert Q-P>=min(a*b,c*d)*P*P*(u+v)
        assert Q>=P
        count+=1
out={'status':'PASS','equality_parameter_sets':3,'exact_checks':count,'boundary_and_coefficient_one_included':True}
Path(__file__).with_name('equality_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
