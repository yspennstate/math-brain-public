from fractions import Fraction
from math import comb
from collections import Counter, defaultdict

# H = K_{5,5} \ C_10 in the cyclic presentation used by C30:
# right vertex R_i is adjacent to left vertices L_i,L_{i+1},L_{i+2} (mod 5).
edges=[]
for i in range(5):
    for d in (0,1,2):
        edges.append(((i+d)%5,5+i))
assert len(edges)==15 and len(set(edges))==15

# Expansion of t_H(1 + lambda f\otimes f).
# Since m_1=0, only edge subsets with no degree-1 vertex survive.
# m_2=1 and m_3=r. Record (number of selected edges, number of degree-3 vertices/2).
counts=Counter()
for mask in range(1<<15):
    deg=[0]*10
    m=0
    for e,(u,v) in enumerate(edges):
        if (mask>>e)&1:
            deg[u]+=1; deg[v]+=1; m+=1
    if 1 in deg:
        continue
    n3=sum(d==3 for d in deg)
    assert n3%2==0
    counts[(m,n3//2)] += 1

expected={
    (0,0):1,
    (4,0):5,
    (6,0):15,
    (7,1):5,
    (8,0):30,
    (8,1):10,
    (9,1):60,
    (10,0):13,
    (10,1):70,
    (10,2):15,
    (11,1):95,
    (11,2):60,
    (12,2):145,
    (12,3):10,
    (13,3):75,
    (14,4):15,
    (15,5):1,
}
assert counts==expected
assert sum(counts.values())==625

# For lambda=-s and x=r^2, Q=P_H(-s,r)-1.
# On the positivity domain 0<s<=1, x <= (1-s)^2/s.
# Parametrize this entire domain by x=(1-a)^2/a and s=a*y,
# with 0<a<=1 and 0<=y<=1. Then Q=a^4 y^4 R(a,y).
# Build R exactly in the ordinary power basis.
R=defaultdict(Fraction)
for (m,k),c in counts.items():
    if (m,k)==(0,0):
        continue
    sign=-1 if m%2 else 1
    # c*sign * a^(m-k) y^m (1-a)^(2k), then divide by a^4 y^4.
    base_a=m-k-4
    base_y=m-4
    assert base_a>=0 and base_y>=0
    for j in range(2*k+1):
        R[(base_a+j,base_y)] += Fraction(c*sign*((-1)**j)*comb(2*k,j),1)

R={mon:coef for mon,coef in R.items() if coef}
na=max(i for i,j in R)
ny=max(j for i,j in R)
assert (na,ny)==(16,11)

# Convert to the tensor-product Bernstein basis of bidegree (16,11).
# If p(a,y)=sum c_kl a^k y^l = sum b_ij B_i^16(a) B_j^11(y), then
# b_ij = sum_{k<=i,l<=j} c_kl C(i,k)/C(16,k) C(j,l)/C(11,l).
bern={}
for i in range(na+1):
    for j in range(ny+1):
        b=Fraction(0,1)
        for k in range(i+1):
            for l in range(j+1):
                c=R.get((k,l),Fraction(0,1))
                if c:
                    b += c*Fraction(comb(i,k),comb(na,k))*Fraction(comb(j,l),comb(ny,l))
        bern[(i,j)]=b

min_b=min(bern.values())
max_b=max(bern.values())
negative=[(ij,b) for ij,b in bern.items() if b<0]
assert not negative
assert min_b==Fraction(5,1)
assert max_b==Fraction(63,1)

# Exact spot checks of Q=a^4 y^4 R after the domain parametrization.
def eval_poly(poly,A,Y):
    z=Fraction(0,1)
    for (i,j),c in poly.items():
        z += c*(A**i)*(Y**j)
    return z

def eval_Q_direct(A,Y):
    s=A*Y
    x=(1-A)*(1-A)/A
    q=Fraction(0,1)
    for (m,k),c in counts.items():
        if (m,k)==(0,0):
            continue
        q += Fraction(c*((-1)**m),1)*(s**m)*(x**k)
    return q

for A,Y in [(Fraction(1,2),Fraction(1,3)),(Fraction(2,3),Fraction(3,5)),(Fraction(5,7),Fraction(7,11)),(Fraction(1,1),Fraction(1,2))]:
    lhs=eval_Q_direct(A,Y)
    rhs=(A**4)*(Y**4)*eval_poly(R,A,Y)
    assert lhs==rhs
    assert rhs>=0

print('H_edges=', len(edges), sep='')
print('surviving_edge_subsets=', sum(counts.values()), sep='')
print('expansion_counts=', sorted(counts.items()), sep='')
print('R_bidegree=', (na,ny), sep='')
print('bernstein_coefficient_count=', len(bern), sep='')
print('bernstein_min=', min_b, sep='')
print('bernstein_max=', max_b, sep='')
print('bernstein_negative_count=', len(negative), sep='')
print('domain_identity_spot_checks=PASS')
print('ALL_EXACT_CHECKS_PASS')
