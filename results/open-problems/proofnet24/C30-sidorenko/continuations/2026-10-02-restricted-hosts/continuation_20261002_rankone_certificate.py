"""Exact combinatorial and rational-bound certificate for rank-one hosts."""
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

def main():
    edges=[(i,5+j)for i in range(5)for j in range(5)if(j-i)%5 in[0,1,4]]
    counts=Counter()
    for mask in range(1<<15):
        degree=[0]*10
        for k,(x,y)in enumerate(edges):
            if mask>>k&1:degree[x]+=1;degree[y]+=1
        if 1 not in degree:counts[(degree.count(2),degree.count(3))]+=1
    expected={(0,0):1,(4,0):5,(6,0):15,(8,0):30,(10,0):13,(4,2):5,(5,2):10,(6,2):60,(7,2):70,(8,2):95,
              (4,4):15,(5,4):60,(6,4):145,(3,6):10,(4,6):75,(2,8):15,(0,10):1}
    assert dict(counts)==expected
    poly={(n2+n3-4,n3//2):c*(-1)**(n2+3*(n3//2))for(n2,n3),c in counts.items()if n2+n3}
    target={(0,0):5,(2,0):15,(4,0):30,(6,0):13,(2,1):-5,(3,1):10,(4,1):-60,(5,1):70,(6,1):-95,
            (4,2):15,(5,2):-60,(6,2):145,(5,3):10,(6,3):-75,(6,4):15,(6,5):-1}
    assert poly==target
    negative=[(n2,n3,c)for(n2,n3),c in counts.items()if(n2+3*(n3//2))%2]
    assert len(negative)==6
    bounds=[F(5),F(15,4),F(21,10),F(15,16),F(75,256),F(1,256)]
    assert F(1520,729)<F(21,10)
    assert sum(bounds)==F(3867,320)<13
    result={'status':'exact combinatorial and rational-bound PASS','edges':edges,
            'degree_counts':{f'{a},{b}':c for(a,b),c in sorted(counts.items())},'negative_degree_types':negative,
            'F_polynomial_coefficients':{f'z^{a} r^{b}':c for(a,b),c in sorted(poly.items())},'negative_bound_coefficients':[str(b)for b in bounds],
            'sum_negative_bounds':str(sum(bounds)),'remaining_z2_coefficient':str(F(15)-sum(bounds)),
            'theorem':'t(H,1+lambda f tensor f)>=1+5lambda^4+2lambda^6 when mean f=0, second moment1 and kernel nonnegative'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))

if __name__=='__main__':main()
