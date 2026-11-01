"""Discovery-only LP conversion; exact_verify.py does not use scipy or this file."""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from core import *

HERE=Path(__file__).resolve().parent
DN=np.array(D,dtype=float);CN=np.array(C,dtype=float)
tables=[];records=[];R=right_inverse()
for p in SEEDS:
    b=contrast(p)
    res=linprog(np.zeros(90),A_eq=DN,b_eq=np.array(b,dtype=float),bounds=(0,None),method='highs')
    assert res.success
    x=[F(float(v)).limit_denominator(1000000) for v in res.x]
    assert min(x)>=0 and matvec(D,x)==b
    stabilizer=[pi for pi in SYMMETRIES if act_point(p,pi)==p]
    xs=[act_weights(x,pi) for pi in stabilizer]
    x=[sum((y[j] for y in xs),F(0))/len(xs) for j in range(90)]
    assert matvec(D,x)==b
    correction=[a-bb for a,bb in zip(x,matvec(R,b))]
    q=flow_coordinates(correction)
    tables.append(x)
    records.append({'point':list(map(str,p)),'weights':list(map(str,x)),
                    'flow_coefficients':list(map(str,q)),'stabilizer_size':len(stabilizer),
                    'positive_atoms':sum(v>0 for v in x)})

# A dual for 9+3(a+b+c)-2t >= 0. The other seven are site symmetries.
p=(F(-1,2),)*3
res=linprog(np.r_[np.zeros(90),-1.0],A_eq=np.column_stack((DN,-CN[:,4])),
            b_eq=CN[:,:4]@np.r_[1,np.array(p,dtype=float)],
            bounds=[(0,None)]*90+[(None,None)],method='highs')
assert res.success
y=[-2*F(float(v)).limit_denominator(10000) for v in res.eqlin.marginals]
assert all(dot(y,column)>=0 for column in zip(*D))
assert [dot(y,column) for column in zip(*C)]==[9,3,3,3,-2]

# Average this dual over group permutations; the target functional is fixed.
def act_dual(y,pi):
    out=[F(0)]*50
    for X,v in zip(SETS,y):out[SIX[tuple(sorted(pi[i] for i in X))]]=v
    return out
pis=[pi for pi in SYMMETRIES if all(pi[2*r]%2==0 for r in range(3))]
ys=[act_dual(y,pi) for pi in pis]
y=[sum((z[j] for z in ys),F(0))/len(ys) for j in range(50)]
assert all(dot(y,column)>=0 for column in zip(*D))
assert [dot(y,column) for column in zip(*C)]==[9,3,3,3,-2]

vtab=vertex_tables(tables)
vertices,count=exact_vertices()
assert set(vertices)==set(vtab)
data={'description':'C039 exact maximal four-coordinate transport polytope',
      'coordinate_order':['a=n0.n1','b=n1.n2','c=n0.n2','t=sqrt(3)*chirality'],
      'seed_tables':records,'transport_cut_dual':list(map(str,y)),
      'vertices':[list(map(str,p)) for p in vertices],
      'nonsingular_four_facet_intersections':count}
(HERE/'certificate.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'seeds':len(tables),'vertices':len(vertices),'nonsingular_intersections':count,
                  'seed_supports':[r['positive_atoms'] for r in records],
                  'dual':list(map(str,y))},indent=2))
