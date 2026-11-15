"""Independent switching-reduced audit via determinants and resultants."""
import csv
import itertools
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
x=sp.Symbol('x')
results=[]
for row in csv.DictReader((ROOT/'data/exact_zeros.csv').open()):
    n=int(row['n'])
    diagonal=row['diagonal']
    positions=[(i,j) for i in range(1,n) for j in range(i+1,n)]
    if diagonal=='rademacher':
        positions += [(i,i) for i in range(n)]
    simple=zero=total=0
    for bits in itertools.product((-1,1),repeat=len(positions)):
        a=sp.zeros(n)
        for j in range(1,n):
            a[0,j]=a[j,0]=1
        for (i,j),value in zip(positions,bits):
            a[i,j]=a[j,i]=value
        # Determinants and resultants, rather than the main script's charpoly and gcd.
        p=(x*sp.eye(n)-a).det(method='domain-ge')
        total+=1
        if sp.resultant(p,sp.diff(p,x),x)==0:
            continue
        simple+=1
        zero+=any(sp.resultant(p,(x*sp.eye(n-1)-a.minor_submatrix(i,i)).det(method='domain-ge'),x)==0
                  for i in range(n))
    factor=2**(n-1)
    result=dict(n=n,diagonal=diagonal,switching_orbits=total,multiplicity=factor,
                total=total*factor,simple=simple*factor,zero=zero*factor)
    result['matches_main']=all((result[key]==int(row[column])) for key,column in
                              [('total','total'),('simple','simple_spectrum'),('zero','simple_with_zero_coordinate')])
    assert result['matches_main'],result
    results.append(result)
    print(result,flush=True)
(ROOT/'data/exact_zero_audit.json').write_text(json.dumps(results,indent=2))
