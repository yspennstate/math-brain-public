"""Replay an SOS certificate without a floating solver.

Reconstruct the endpoint polynomial from the affine radial coefficients P,Q,R,
not from the ordered-cone expression E used by the certificate generator.
All polynomial and PSD comparisons are exact.
"""
import json,sys
from fractions import Fraction as F
from sympy.polys.rings import ring
from sympy.polys.domains import QQ

def psd(rows):
    mat=[[F(x) for x in row] for row in rows]
    while mat:
        pivot=mat[0][0]
        assert pivot>=0
        if pivot==0:
            assert all(x==0 for x in mat[0])
            mat=[row[1:] for row in mat[1:]]
        else:
            mat=[[mat[i][j]-mat[i][0]*mat[0][j]/pivot for j in range(1,len(mat))] for i in range(1,len(mat))]

filename=sys.argv[1] if len(sys.argv)>1 else 'quartic_ratio_matrices_3_25.json'
data=json.load(open(filename))
assert not data['failed']
rat=F(data['r'])
rho=QQ(rat.numerator,rat.denominator)
ring0,*gens=ring('z0,z1,z2,z3,x0,x1,x2',QQ)
z,x=gens[:4],gens[4:]
u=[sum(((5-j) if i<j else -j)*z[j-1] for j in range(1,5)) for i in range(5)]
span=u[0]-u[4]
w=[sum((u[4]-u[j+1])*x[j] for j in range(3))]+[span*x[j] for j in range(3)]+[sum((u[j+1]-u[0])*x[j] for j in range(3))]
assert sum(u)==0 and sum(w)==0 and sum(ui*wi for ui,wi in zip(u,w))==0
t=sum(ui**2 for ui in u)
n=sum(wi**2 for wi in w)
a4=sum(ui**4 for ui in u)
b4=sum(wi**4 for wi in w)
c4=sum(ui**2*wi**2 for ui,wi in zip(u,w))
d3=sum(ui**3 for ui in u)
e3=sum(ui**2*wi for ui,wi in zip(u,w))
f3=sum(ui*wi**2 for ui,wi in zip(u,w))
h3=sum(wi**3 for wi in w)

# Each expression below has the common denominator t^3 n^2 after
# multiplying by the indicated powers of t and n.
lu=QQ(14,9)*(a4*n+t*c4-t*t*n/5)
lw=QQ(14,9)*(t*b4+c4*n-t*n*n/5)
pnum=QQ(58,45)*t**3*n*n-QQ(40,9)*a4*t*n*n-QQ(34,9)*c4*t*t*n
pnum+=QQ(8,3)*d3*d3*n*n+QQ(2,3)*e3*e3*t*n+2*d3*f3*t*n
qnum=QQ(2,9)*(a4*n*n+t*t*b4-QQ(2,5)*t*t*n*n)-QQ(8,9)*t*c4*n
qnum+=QQ(10,3)*(e3*e3*n+t*f3*f3)+2*d3*f3*n+2*t*h3*e3
rnum=QQ(58,45)*t**3*n*n-QQ(40,9)*t**3*b4-QQ(299,72)*t*t*c4*n
denom=20*(-u[0]*u[4])-t-rho*(7*t-5*(u[0]+u[4])**2)
expected=QQ(9,2)*(denom*(lu*n+rho*t*lw)+2*pnum+2*rho*t*qnum+2*rho*rho*rnum)

actual=ring0.zero
seen=set()
for rec in data['records']:
    mon=tuple(rec['monomial'])
    assert sum(mon)==10 and mon not in seen
    seen.add(mon)
    den=rec['denominator']
    rows=rec['matrix']
    assert den>0 and len(rows)==6 and all(len(row)==6 for row in rows)
    assert all(rows[i][j]==rows[j][i] for i in range(6) for j in range(6))
    psd(rows)
    sc=F(rec['scale'])/den
    assert sc>0
    for i in range(6):
        for j in range(6):
            if rows[i][j]:
                full=mon+tuple(a+b for a,b in zip(data['monomials'][i],data['monomials'][j]))
                value=sc*rows[i][j]
                actual+=ring0.from_dict({full:QQ(value.numerator,value.denominator)})
assert actual==expected
print('PROVED: independent radial construction equals all SOS coefficients exactly.')
print('PROVED: exact symmetric elimination verified',len(seen),'positive semidefinite 6-by-6 Gram matrices.')
print('PROVED: endpoint ratio',rat,'is certified; no SDP solver is needed for this replay.')
