from itertools import permutations, combinations
from fractions import Fraction

G = list(permutations(range(4)))
e = (0,1,2,3)

def comp(g,h):
    return tuple(g[h[i]] for i in range(4))

def inv(g):
    q=[0]*4
    for i,j in enumerate(g):
        q[j]=i
    return tuple(q)

def generated(gens):
    H={e}
    changed=True
    while changed:
        changed=False
        for a in list(H):
            for b in list(H)+list(gens):
                for c in (comp(a,b),comp(b,a)):
                    if c not in H:
                        H.add(c); changed=True
    return frozenset(H)

def t(i,j):
    p=list(e); p[i],p[j]=p[j],p[i]; return tuple(p)

def cyc4(a,b,c,d):
    p=list(e)
    p[a]=b;p[b]=c;p[c]=d;p[d]=a
    return tuple(p)

def left_cosets(H):
    unused=set(G); out=[]
    while unused:
        x=next(iter(unused))
        C=frozenset(comp(h,x) for h in H)
        out.append(C); unused-=C
    return out

def right_cosets(H):
    unused=set(G); out=[]
    while unused:
        x=next(iter(unused))
        C=frozenset(comp(x,h) for h in H)
        out.append(C); unused-=C
    return out

# Gaussian integer operations.
def zmul(x,y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def zadd(x,y):
    return (x[0]+y[0],x[1]+y[1])

a=[(-4,4),(0,-1),(-3,2),(-4,-4)]
b=[(-4,-4),(2,-1),(2,-4),(4,-1)]

def endpoint(sig):
    z=(1,0)
    for i in range(4):
        z=zmul(z,zadd(a[i],b[sig[i]]))
    return z
Hval={g:endpoint(g)[0] for g in G}
M=max(Hval.values())

# Seven subgroups in the exact cubature identity.
H1=generated([t(0,3),t(1,2)])
H2=generated([t(0,1),cyc4(0,2,1,3)])
H3=generated([t(1,2),t(1,3)])
H4=generated([t(0,1),t(2,3)])
H5=generated([t(0,2)])
H6=generated([t(0,3),cyc4(0,1,3,2)])
H7=generated([t(0,1),t(0,3)])
Hs=[H1,H2,H3,H4,H5,H6,H7]
weights=[Fraction(1,3),Fraction(1,3),Fraction(1,2),Fraction(1,3),
         Fraction(2,3),Fraction(1,3),Fraction(1,2)]
expected_sizes=[4,8,6,4,2,8,6]
assert [len(H) for H in Hs]==expected_sizes
assert all(any(sum(g[i]!=i for i in range(4))==2 for g in H) for H in Hs)

def subgroup_avg(f,H):
    return sum(Fraction(f[g]) for g in H)/len(H)

# The cubature identity is exact on constants, every singleton assignment
# indicator, and every unordered 2-subset assignment indicator. Those
# generators contain the k=0,1,2,3,4 Cauchy-Binet orbit functions in n=4.
basis=[]
basis.append({g:1 for g in G})
for i in range(4):
    for j in range(4):
        basis.append({g:int(g[i]==j) for g in G})
subs=list(combinations(range(4),2))
for I in subs:
    for J in subs:
        SJ=frozenset(J)
        basis.append({g:int(frozenset(g[i] for i in I)==SJ) for g in G})

for f in basis:
    rhs=sum(w*subgroup_avg(f,H) for w,H in zip(weights,Hs))
    rhs -= 2*sum(Fraction(f[g]) for g in G)/24
    assert rhs == f[e], (rhs,f[e])

def roof_for_values(H,values,side):
    Cs = left_cosets(H) if side=="left" else right_cosets(H)
    return max(sum(Fraction(values[g]) for g in C)/len(C) for C in Cs)

def cubature_bound(values,side):
    mean=sum(Fraction(values[g]) for g in G)/24
    roofs=[roof_for_values(H,values,side) for H in Hs]
    return sum(w*r for w,r in zip(weights,roofs))-2*mean, mean, roofs

bound_left,m_left,roofs_left=cubature_bound(Hval,"left")
assert roofs_left==[Fraction(-47,2),Fraction(-7,2),Fraction(32),Fraction(58),
                    Fraction(231),Fraction(-68),Fraction(-134,3)]
assert M==256
assert m_left==Fraction(-217,2)
assert bound_left==Fraction(1057,3)
assert bound_left-M==Fraction(289,3)

# The prior real-spectrum lead datum is exactly closed by the opposite
# coset orientation of the same cubature identity.
ar=[-1,2,1,0]
br=[-1,1,-2,2]
Hreal={g:__import__("math").prod(ar[i]+br[g[i]] for i in range(4)) for g in G}
real_bound_right,real_mean,real_roofs_right=cubature_bound(Hreal,"right")
assert max(Hreal.values())==36
assert real_mean==Fraction(29,6)
assert real_bound_right==36

print("PASS MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1")
print("basis_generators =",len(basis))
print("subgroup_sizes =",expected_sizes)
print("hard_left_coset_roofs =",[str(x) for x in roofs_left])
print("hard_endpoint_M =",M)
print("hard_endpoint_mean =",m_left)
print("hard_support_upper_bound =",bound_left)
print("hard_gap_upper_bound =",bound_left-M)
print("real_right_coset_roofs =",[str(x) for x in real_roofs_right])
print("real_support_upper_bound =",real_bound_right)
