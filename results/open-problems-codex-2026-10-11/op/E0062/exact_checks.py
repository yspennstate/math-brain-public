from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
count=0; parameter_sets=0
for a,b,c,d in product([F(1,2),F(3,4),F(1)], [F(1,20),F(1,10),F(1,4)], [F(1,2),F(3,4),F(1)], [F(1,20),F(1,10),F(1,4)]):
    k=min(a-b-a*b,c-d-c*d)
    if k<=0: continue
    parameter_sets+=1
    A=[[0,a,0,-d],[-a,0,b,0],[0,-b,0,c],[d,0,-c,0]]
    for i in range(11):
      for j in range(11-i):
       for l in range(11-i-j):
        x=[F(i,10),F(j,10),F(l,10),F(10-i-j-l,10)]
        y=[x[r]*(1+sum(A[r][s]*x[s] for s in range(4))) for r in range(4)]
        P=x[0]*x[2]; Q=y[0]*y[2]; u=x[1]; v=x[3]
        bracket=(a-b-a*b)*u+(c-d-c*d)*v+a*b*u*(1-u)+c*d*v*(1-v)+(a*c+b*d)*u*v
        assert sum(y)==1 and min(y)>=0
        assert Q-P == P*bracket
        assert Q-P >= k*P*(u+v)
        assert abs(y[0]-x[0])<=u+v and abs(y[2]-x[2])<=u+v
        assert P<=F(1,4)
        count+=1
out={'status':'PASS','parameter_sets':parameter_sets,'simplex_points_per_set':286,'exact_rational_checks':count,'boundary_points_included':True,'coefficient_one_included':True,'example_gap':str(F(9,10)-F(1,10)-F(9,10)*F(1,10))}
Path(__file__).with_name('exact_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
