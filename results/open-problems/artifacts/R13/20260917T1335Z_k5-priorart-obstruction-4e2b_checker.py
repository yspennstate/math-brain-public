#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

D = 142

class Q:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=o if isinstance(o,Q) else Q(o)
        return Q(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,o): return self+(-(o if isinstance(o,Q) else Q(o)))
    def __rsub__(self,o): return Q(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q) else Q(o)
        return Q(self.a*o.a + D*self.b*o.b,
                 self.a*o.b + self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        if isinstance(o,Q):
            den=o.a*o.a-D*o.b*o.b
            return Q((self.a*o.a-D*self.b*o.b)/den,
                     (self.b*o.a-self.a*o.b)/den)
        return Q(self.a/F(o),self.b/F(o))
    def sq(self): return self*self
    def is_zero(self): return self.a==0 and self.b==0
    def sign(self):
        if self.is_zero(): return 0
        a,b=self.a,self.b
        if b==0: return 1 if a>0 else -1
        if a==0: return 1 if b>0 else -1
        if a>0 and b>0: return 1
        if a<0 and b<0: return -1
        cmp=a*a-D*b*b
        if a>0 and b<0: return 1 if cmp>0 else -1
        if a<0 and b>0: return -1 if cmp>0 else 1
        raise AssertionError
    def __repr__(self):
        return f"({self.a})+({self.b})*sqrt({D})"

sqrtD=Q(0,1)
K=(Q(4)+sqrtD)/9
a=K/4
b=K/2-F(1,4)

A=[
    [Q(0), -a, -a, -a, a],
    [Q(F(1,2)), Q(0), Q(0), b, b],
    [Q(F(-1,2)), b, Q(0), Q(0), b],
    [Q(F(-1,2)), -b, b, Q(0), Q(0)],
    [Q(F(-1,2)), Q(0), -b, b, Q(0)],
]

def dot(row,vec):
    z=Q(0)
    for x,e in zip(row,vec):
        z += x*e
    return z

def vec_add(u,v): return [x+y for x,y in zip(u,v)]
def scalar_vec(c,v): return [c*x for x in v]
def vec_equal(u,v): return all((x-y).is_zero() for x,y in zip(u,v))

# 1) Exact column norm checks and exact discrepancy on all antipodal classes.
for j in range(5):
    s=Q(0)
    for i in range(5):
        s += A[i][j].sq()
    assert (s-Q(1)).is_zero(), (j,s)

K2=K.sq()
S=[]
active_by_row=[[] for _ in range(5)]
multiplicities=[]
for tail in product((-1,1), repeat=4):
    eps=(1,)+tail
    idx=len(S)
    S.append(eps)
    vals=[dot(row,eps) for row in A]
    diffs=[v.sq()-K2 for v in vals]
    assert all(d.sign()<=0 for d in diffs), (eps,vals,diffs)
    active=[i for i,d in enumerate(diffs) if d.is_zero()]
    assert active, (eps,vals,diffs)
    for i in active: active_by_row[i].append(idx)
    multiplicities.append(len(active))

assert [len(x) for x in active_by_row]==[2,4,4,4,4]
assert sum(multiplicities)==18
assert multiplicities.count(1)==14
assert multiplicities.count(2)==2

# 2) Fix one exact partition of the 16 projective classes among the five rows.
# Overlap class 4 is assigned to row 2; overlap class 11 to row 3.
blocks=[
    [1,14],
    [3,7,15],
    [0,2,4,6],
    [8,9,10,11],
    [5,12,13],
]
assert sorted(sum(blocks,[]))==list(range(16))

# Normalize rows by K. Orient each assigned sign vector so normalized row dot t = 1.
R=[[x/K for x in row] for row in A]
Tblocks=[]
for i,block in enumerate(blocks):
    Tb=[]
    for j in block:
        eps=S[j]
        z=dot(R[i],eps)
        assert (z.sq()-Q(1)).is_zero()
        sg=z.sign()
        t=tuple(sg*e for e in eps)
        assert (dot(R[i],t)-Q(1)).is_zero()
        Tb.append(t)
    Tblocks.append(Tb)

# 3) Exact diagonal dual weight. This makes the displayed lower construction
# KKT-optimal for this fixed oriented partition.
x=Q(F(-1,7), F(16,497))
y=Q(F(2,7), F(-4,497))
assert (x+4*y-Q(1)).is_zero()
assert x.sign()>0 and y.sign()>0
lam=[x,y,y,y,y]

alpha0=Q(F(1,28),F(-1,994))
C=Q(F(9,98),F(-135,27832))
assert alpha0.sign()>0 and C.sign()>0
alphas=[
    [alpha0,alpha0],
    [C,Q(0),C],
    [Q(0),C,C,Q(0)],
    [Q(0),C,C,Q(0)],
    [C,C,Q(0)],
]

total_cost=Q(0)
for i,(Tb,aa) in enumerate(zip(Tblocks,alphas)):
    # KKT stationarity: Lambda r = sum alpha_t t.
    lhs=[lam[j]*R[i][j] for j in range(5)]
    rhs=[Q(0) for _ in range(5)]
    for alpha,t in zip(aa,Tb):
        rhs=vec_add(rhs, scalar_vec(alpha,t))
    assert vec_equal(lhs,rhs), (i,lhs,rhs)
    assert all(alpha.sign()>=0 for alpha in aa)
    assert all((dot(R[i],t)-Q(1)).sign()>=0 for t in Tb)
    cost=sum(lam[j]*R[i][j].sq() for j in range(5))
    total_cost += cost

c0=Q(1)/K2
assert (total_cost-c0).is_zero(), (total_cost,c0)

print("BELHAOUARI_ALQUDAH_K5_OBSTRUCTION_EXACT_PASS")
print("K=(4+sqrt(142))/9")
print("column_norm_squares=1,1,1,1,1")
print("antipodal_classes_checked=16")
print("all_signings_discrepancy_exactly_K=True")
print("active_incidence_total=18")
print("active_multiplicity_histogram={1:14,2:2}")
print("partition_sizes=2,3,4,4,3")
print("dual_lambda=(x,y,y,y,y)")
print("x=-1/7+16*sqrt(142)/497")
print("y=2/7-4*sqrt(142)/497")
print("fixed_partition_weighted_KKT_sum=1/K^2")
print("conclusion=K5_star >= (4+sqrt(142))/9")
print("scope=lower_obstruction_and_fixed_partition_KKT_only; no_global_K5_upper_claim")
