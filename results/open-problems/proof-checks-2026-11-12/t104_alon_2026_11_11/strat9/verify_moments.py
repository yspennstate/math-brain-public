"""Exact replay of the lower moment certificates, without a solver."""
import json
from fractions import Fraction
from sympy.polys.rings import ring
from sympy.polys.domains import QQ

def psd(mat):
    mat=[[Fraction(x) for x in row] for row in mat]
    while mat:
        p=mat[0][0]
        assert p>=0
        if p==0:
            assert all(x==0 for x in mat[0])
            mat=[row[1:] for row in mat[1:]]
        else:
            mat=[[mat[i][j]-mat[i][0]*mat[0][j]/p for j in range(1,len(mat))] for i in range(1,len(mat))]

ring0,*gen=ring('z0,z1,z2,z3,x0,x1,x2',QQ)
z,x=gen[:4],gen[4:]
u=[sum(((5-j) if i<j else -j)*z[j-1] for j in range(1,5)) for i in range(5)]
delta=u[0]-u[4]
w=[sum((u[4]-u[j+1])*x[j] for j in range(3))]+[delta*x[j] for j in range(3)]+[sum((u[j+1]-u[0])*x[j] for j in range(3))]
t=sum(ui**2 for ui in u)
q=sum(ui**4 for ui in u)
n=sum(wi**2 for wi in w)
c=sum(ui**2*wi**2 for ui,wi in zip(u,w))
scalar=q-QQ(7,30)*t*t
assert all(v>=0 for v in scalar.values())
actual=ring0.zero
records=json.load(open('moment_lower_matrices.json'))
for rec in records:
    mat=rec['matrix']
    psd(mat)
    for i in range(3):
        for j in range(3):
            ex=[0,0,0]
            ex[i]+=1
            ex[j]+=1
            actual+=ring0.from_dict({tuple(rec['monomial'])+tuple(ex):QQ(mat[i][j],rec['denominator'])})
assert actual==(q-t*t/4)*n+t*c
print('PROVED: A>=7/30 by nonnegative exact ordered-cone coefficients.')
print('PROVED: A+C>=1/4 by',len(records),'exact PSD coefficient matrices and exact coefficient matching.')
