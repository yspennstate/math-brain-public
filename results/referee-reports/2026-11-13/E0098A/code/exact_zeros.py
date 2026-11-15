"""Exact exhaustive small-n Bernoulli check, using rational polynomial gcds."""
import csv
import itertools
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
x=sp.Symbol('x')
rows=[]
for diagonal, sizes in [('rademacher',(2,3,4)), ('zero',(2,3,4,5))]:
    for n in sizes:
        positions=[(i,j) for i in range(n) for j in range(i,n) if i!=j or diagonal!='zero']
        total=simple=any_zero=zero_pairs=0
        for bits in itertools.product((-1,1),repeat=len(positions)):
            a=sp.zeros(n)
            for (i,j), value in zip(positions,bits):
                a[i,j]=a[j,i]=value
            p=sp.Poly(a.charpoly(x).as_expr(),x,domain=sp.QQ)
            total+=1
            if sp.gcd(p,p.diff()).degree()>0:
                continue
            simple+=1
            found=False
            for i in range(n):
                minor=a.minor_submatrix(i,i)
                q=sp.Poly(minor.charpoly(x).as_expr(),x,domain=sp.QQ)
                degree=sp.gcd(p,q).degree()
                zero_pairs+=degree
                found=found or degree>0
            any_zero+=found
        row=dict(diagonal=diagonal,n=n,total=total,simple_spectrum=simple,
                 repeated_spectrum=total-simple,simple_with_zero_coordinate=any_zero,
                 zero_coordinate_eigenpair_count_on_simple_matrices=zero_pairs)
        rows.append(row)
        print(json.dumps(row),flush=True)

out=ROOT/'data'/'exact_zeros.csv'
with out.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

example=sp.Matrix([[1,1,1],[1,1,1],[1,1,-1]])
result={'matrix':list(map(list,example.tolist())),
        'characteristic_polynomial':str(example.charpoly(x).as_expr()),
        'unnormalized_zero_eigenvector':[1,-1,0],
        'matrix_times_vector':list(example*sp.Matrix([1,-1,0])),
        'simple_spectrum':sp.gcd(example.charpoly(x).as_poly(),example.charpoly(x).as_poly().diff()).degree()==0}
(ROOT/'data'/'exact_zero_witness.json').write_text(json.dumps(result,indent=2,default=str))
