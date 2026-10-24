from math import pi, sqrt
from itertools import combinations
import random


def det(u,v):
    return u[0]*v[1]-u[1]*v[0]


def matching_identity(vs):
    n=len(vs)
    w={}
    for i in range(n):
        for j in range(i+1,n):
            w[(i,j)]=det(vs[i],vs[j])**2
    D=sum(w.values())
    deg=[sum(x for (i,j),x in w.items() if i==r or j==r) for r in range(n)]
    M4=0.0
    edges=list(w)
    for p in range(len(edges)):
        for q in range(p+1,len(edges)):
            e,f=edges[p],edges[q]
            if len(set(e+f))==4:
                M4 += w[e]*w[f]
    rhs=0.5*(D*D+sum(x*x for x in w.values())-sum(x*x for x in deg))
    return D,M4,rhs

random.seed(230923)
maxerr=0.0
for n in (4,5,7,9):
    for _ in range(200):
        vs=[(random.uniform(-2,2),random.uniform(-2,2)) for _ in range(n)]
        D,M4,rhs=matching_identity(vs)
        maxerr=max(maxerr,abs(M4-rhs)/(1+abs(M4)))

v1=(0.5,1/(2*sqrt(2)))
v3=(0.5,-1/(2*sqrt(2)))
delta=abs(det(v1,v3))
prod=delta*delta
K=sqrt(2)*pi**1.5*prod**-0.5
bound=(3/pi)*K**(2/3)
closed=6*2**(1/3)

print(f"matching_identity_max_relative_error={maxerr:.3e}")
print(f"partner_family_delta={delta:.15f}")
print(f"partner_family_product={prod:.15f}")
print(f"partner_family_K={K:.15f}")
print(f"partner_family_density_bound={bound:.15f}")
print(f"closed_form_6_times_2pow1over3={closed:.15f}")
assert maxerr < 1e-10
assert abs(bound-closed)<1e-12
print("QFORM_B11_FOURROW_MATCHING_CHECK_PASS")
