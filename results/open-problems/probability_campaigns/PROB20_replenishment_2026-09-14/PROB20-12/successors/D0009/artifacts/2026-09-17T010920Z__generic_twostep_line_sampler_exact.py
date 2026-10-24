#!/usr/bin/env python3
from fractions import Fraction as Q

def q(n,d=1): return Q(n,d)

# Target generic source-valid two-step extreme.
a=q(2,5); m=q(2,3); b=q(1)
alpha=(b-m)/(b-a)
beta=(m-a)/(b-a)
tail_mass=m-a
assert alpha==q(5,9)
assert beta==q(4,9)
assert 3*beta==q(4,3)          # previous layer-count architecture is nonintegral
assert 3*tail_mass==q(4,5)     # region-count architecture is also nonintegral
assert m>=q(2,3)               # n=3 source mean condition
mu=m/2
assert mu==q(1,3)

# A boundary-line atom: if one width equals the sum of the other two,
# a single U~Unif[-1/2,1/2] with opposite sign on the largest interval
# makes the sum exactly equal to the sum of interval centers.
branches=[
(q(1,30), [(q(0),q(1,10)),(q(0),q(1,10)),(q(4,5),q(1))]),
(q(1,4),  [(q(0),q(1,5)),(q(0),q(3,10)),(q(1,2),q(1))]),
(q(1,60), [(q(0),q(1,5)),(q(1,10),q(1,5)),(q(7,10),q(4,5))]),
(q(2,5),  [(q(0),q(3,10)),(q(0),q(3,10)),(q(2,5),q(1))]),
(q(1,20), [(q(1,10),q(3,10)),(q(1,5),q(3,10)),(q(2,5),q(7,10))]),
(q(1,20), [(q(1,10),q(3,10)),(q(3,10),q(2,5)),(q(2,5),q(1,2))]),
(q(1,5),  [(q(1,5),q(2,5)),(q(3,10),q(2,5)),(q(3,10),q(2,5))]),
]
assert sum(w for w,_ in branches)==1
for j,(w,ints) in enumerate(branches,1):
    widths=[r-l for l,r in ints]
    centers=[(l+r)/2 for l,r in ints]
    assert all(v>0 for v in widths)
    W=max(widths)
    assert W==sum(widths)-W
    assert sum(centers)==1   # target deterministic sum = 3*mu = 1

# Verify the exchangeable marginal exactly on the common tenth-grid refinement.
density=[]
for k in range(10):
    x=(q(k,10)+q(k+1,10))/2
    d=q(0)
    for w,ints in branches:
        for l,r in ints:
            if l < x < r:
                d += w*q(1,3)/(r-l)
    density.append(d)
assert density[:4]==[q(11,6)]*4
assert density[4:]==[q(4,9)]*6

# Verify this is exactly the two-step extreme F_{a,1}^{(m)}.
low_density=alpha/a + beta/b
high_density=beta/b
assert low_density==q(11,6)
assert high_density==q(4,9)
assert low_density*a + high_density*(1-a)==1
assert low_density*a*a/2 + high_density*(1-a*a)/2==mu

# Exact rank/solution check for the seven-branch breakpoint topology.
# Unknowns: x1,x2,x3,A,x5,x6,x7,S.
# Rows are [coeffs..., rhs].
rows=[
([2,0,0,0,0,0,1,0], 1),                     # B1 width
([2,0,0,0,0,0,1,-2], -1),                   # B1 centers
([0,1,1,0,1,0,0,0], 1),                     # B2 width
([0,1,1,0,1,0,0,-2], -1),                   # B2 centers
([1,0,0,0,0,1,-1,0], 0),                    # B3 width
([1,2,0,0,0,1,1,-2], 0),                    # B3 centers
([0,0,2,1,0,0,0,0], 1),                     # B4 width
([0,0,2,1,0,0,0,-2], -1),                   # B4 centers
([1,1,-2,-1,0,1,0,0], 0),                   # B5 width
([1,1,2,1,0,1,0,-2], 0),                    # B5 centers
([-1,0,2,0,-1,0,0,0], 0),                   # B6 width
([1,0,2,2,1,0,0,-2], 0),                    # B6 centers
([0,-1,2,-1,0,0,0,0], 0),                   # B7 width
([0,1,2,3,0,0,0,-2], 0),                    # B7 centers
]
M=[[q(c) for c in coeff]+[q(rhs)] for coeff,rhs in rows]
nr=len(M); nc=8
pivot_cols=[]
r=0
for c in range(nc):
    piv=next((i for i in range(r,nr) if M[i][c]!=0), None)
    if piv is None:
        continue
    M[r],M[piv]=M[piv],M[r]
    pv=M[r][c]
    M[r]=[z/pv for z in M[r]]
    for i in range(nr):
        if i!=r and M[i][c]!=0:
            fac=M[i][c]
            M[i]=[M[i][j]-fac*M[r][j] for j in range(nc+1)]
    pivot_cols.append(c)
    r+=1
assert len(pivot_cols)==8
for i in range(r,nr):
    assert not all(M[i][c]==0 for c in range(nc)) or M[i][-1]==0
sol=[q(0)]*nc
for i,c in enumerate(pivot_cols):
    sol[c]=M[i][-1]
expected=[q(1,10),q(1,5),q(3,10),q(2,5),q(1,2),q(7,10),q(4,5),q(1)]
assert sol==expected

# B27 continuous arcs: exact identities for region-tail mass q=1/3 and q=2/3.
# q_region=m-a. q_region=1/3 gives two low intervals and one high interval.
# q_region=2/3 gives one low and two high intervals.
for aa in [q(1,3),q(2,5),q(1,2),q(3,5)]:
    mm=aa+q(1,3)
    assert mm>=q(2,3) and mm<1
    widths=[aa,aa,1-aa]
    assert 2*max(widths)<=sum(widths)
    centers=[aa/2,aa/2,(aa+1)/2]
    assert sum(centers)==3*mm/2
for aa in [q(1,10),q(1,5),q(3,10)]:
    mm=aa+q(2,3)
    assert mm>=q(2,3) and mm<1
    widths=[aa,1-aa,1-aa]
    assert 2*max(widths)<=sum(widths)
    centers=[aa/2,(aa+1)/2,(aa+1)/2]
    assert sum(centers)==3*mm/2

print("TARGET a=2/5 m=2/3 b=1")
print("LAYER_WEIGHTS alpha=5/9 beta=4/9; 3beta=4/3 NONINTEGER")
print("REGION_TAIL_MASS q=4/15; 3q=4/5 NONINTEGER")
print("BRANCH_WEIGHTS", " ".join(str(w) for w,_ in branches))
print("MARGINAL_DENSITIES", " ".join(str(x) for x in density))
print("TOPOLOGY_RANK 8")
print("TOPOLOGY_SOLUTION", " ".join(str(x) for x in sol))
print("B27_Q_ONE_THIRD_ARC CHECKED")
print("B27_Q_TWO_THIRDS_ARC CHECKED")
print("ALL EXACT CHECKS PASSED")
