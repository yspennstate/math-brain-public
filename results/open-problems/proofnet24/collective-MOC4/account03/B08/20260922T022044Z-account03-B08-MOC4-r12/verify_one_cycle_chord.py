#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import permutations

def zadd(x,y): return (x[0]+y[0],x[1]+y[1])
def zsub(x,y): return (x[0]-y[0],x[1]-y[1])
def zmul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def zscale(q,x): return (q*x[0],q*x[1])
def zprod(xs):
    z=(F(1),F(0))
    for x in xs: z=zmul(z,x)
    return z
def zsum(xs):
    z=(F(0),F(0))
    for x in xs: z=zadd(z,x)
    return z
def psign(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1
def zdet(M):
    out=(F(0),F(0))
    for p in permutations(range(len(M))):
        out=zadd(out,zscale(F(psign(p)),zprod([M[i][p[i]] for i in range(len(M))])))
    return out

def eye(n=4):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def tr(A): return [list(r) for r in zip(*A)]
def givens(u,v,c,s):
    G=eye()
    G[u][u]=c; G[u][v]=-s
    G[v][u]=s; G[v][v]=c
    return G

c1=c2=c3=c4=F(3,5)
s1=s2=s3=s4=F(4,5)
U0=eye()
for e,c,s in [((0,1),c1,s1),((1,2),c2,s2),((2,3),c3,s3)]:
    U0=mm(U0,givens(e[0],e[1],c,s))
U=mm(U0,givens(0,3,c4,s4))
U1=mm(U0,givens(0,3,F(0),F(1)))
assert mm(U,tr(U))==eye()
assert mm(U0,tr(U0))==eye()
assert mm(U1,tr(U1))==eye()

a=[(F(-4),F(5)),(F(3),F(-8)),(F(-3),F(0)),(F(3),F(-5))]
b=[(F(-1),F(8)),(F(7),F(-3)),(F(5),F(-6)),(F(6),F(-4))]
eta=(F(-1),F(-1))

def vertex(p):
    return zprod([zadd(a[i],b[p[i]]) for i in range(4)])
def support(z): return zmul(eta,z)[0]

verts={p:vertex(p) for p in permutations(range(4))}
assert len(set(verts.values()))==24
vals={p:support(z) for p,z in verts.items()}
pmax=max(vals,key=vals.get)
M=vals[pmax]
assert pmax==(2,0,3,1)
assert M==8
assert sorted(vals.values(),reverse=True)[:4]==[F(8),F(0),F(-36),F(-80)]

def det_for(Ux):
    B=[[zsum(zscale(Ux[i][k]*Ux[j][k],b[k]) for k in range(4))
        for j in range(4)] for i in range(4)]
    C=[[zadd(a[i] if i==j else (F(0),F(0)),B[i][j])
        for j in range(4)] for i in range(4)]
    return zdet(C)

D=det_for(U); D0=det_for(U0); D1=det_for(U1)
gap=M-support(D)
delta0=M-support(D0)
delta1=M-support(D1)
assert D==(F(292022244,390625),F(49307748,390625))
assert gap==F(245839496,390625)>0
assert delta0==F(23525352,3125)>0
assert delta1==F(87756716,15625)>0

p4123=(3,0,1,2)
p1423=(0,3,1,2)
chord=zsub(verts[p4123],verts[p1423])
chord_support=support(chord)
assert chord_support==19244

k=c1*s1*s2*s3
rhs=zadd(zadd(zscale(c4*c4,D0),zscale(s4*s4,D1)),
         zscale(2*c4*s4*k,chord))
assert D==rhs

cross=2*c4*s4*k*chord_support
base=c4*c4*delta0+s4*s4*delta1
assert cross==F(88676352,15625)
assert base==F(2462748296,390625)
assert base-cross==gap
assert cross/base==F(277113600,307843537)

def mu(Ux,p):
    q=F(psign(p))
    for i,j in enumerate(p): q*=Ux[i][j]
    return q
for name,Ux in [("tree_endpoint_0",U0),("tree_endpoint_1",U1)]:
    mus0={p:mu(Ux,p) for p in permutations(range(4))}
    assert all(x>=0 for x in mus0.values())
    assert sum(mus0.values(),F(0))==1
    assert sum(1 for x in mus0.values() if x)==8

mus={p:mu(U,p) for p in permutations(range(4))}
assert sum(mus.values(),F(0))==1
assert min(mus.values())==F(-186624,9765625)<0

# Exact target-level membership certificate for this selected adversary.
# D = l1*v_1234 + l2*v_2134 + l3*v_2314.
l1=F(28480049,10030078125)
l2=F(572818676,668671875)
l3=F(1409317936,10030078125)
assert l1>=0 and l2>=0 and l3>=0 and l1+l2+l3==1
combo=zadd(zadd(zscale(l1,verts[(0,1,2,3)]),zscale(l2,verts[(1,0,2,3)])),
           zscale(l3,verts[(1,2,0,3)]))
assert combo==D

print("orthogonal_true_unitary=True")
print("24_vertices_distinct=True")
print("unique_support_max_perm_1based=3142")
print("support_max=",M)
print("determinant=",D)
print("target_support_gap=",gap)
print("endpoint_deficits=",delta0,delta1)
print("chord_support_4123_minus_1423=",chord_support)
print("cross_chord_payment=",cross)
print("endpoint_base_payment=",base)
print("cross_fraction_of_base=",cross/base)
print("one_cycle_chord_identity=True")
print("tree_endpoints_nonnegative_lifts=True")
print("cyclic_min_formal_mu=",min(mus.values()))
print("exact_hull_certificate_perms=1234,2134,2314")
print("exact_hull_certificate_weights=",l1,l2,l3)
print("exact_hull_membership=True")
print("PASS")
