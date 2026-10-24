from itertools import combinations
import sympy as sp

# Five partitions of the fixed 3-vertex side.
PARTS = [(0,1,2),(0,0,1),(0,1,0),(0,1,1),(0,0,0)]

def canon(labels):
    mp={}
    out=[]
    nxt=0
    for x in labels:
        if x not in mp:
            mp[x]=nxt
            nxt+=1
        out.append(mp[x])
    return tuple(out)

def transition(part,S):
    labs=[part[i] for i in S]
    if len(labs) != len(set(labs)):
        return None
    if len(S) < 2:
        return part
    chosen=set(labs)
    temp=[999 if x in chosen else x for x in part]
    return canon(temp)

def transfer(predicate=lambda S: True):
    A=sp.zeros(5,5)
    for i,p in enumerate(PARTS):
        for mask in range(8):
            S=tuple(a for a in range(3) if (mask>>a)&1)
            if not predicate(S):
                continue
            q=transition(p,S)
            if q is None:
                continue
            A[i,PARTS.index(q)] += 1
    return A

M=transfer()
E=[transfer(lambda S,a=a: a in S) for a in range(3)]
E2={(a,b):transfer(lambda S,a=a,b=b: a in S and b in S)
    for a in range(3) for b in range(a+1,3)}

M_EXPECT=sp.Matrix([
    [4,1,1,1,1],
    [0,4,0,0,2],
    [0,0,4,0,2],
    [0,0,0,4,2],
    [0,0,0,0,4],
])
assert M == M_EXPECT
N=M-4*sp.eye(5)
assert N**3 == sp.zeros(5,5)
assert N**2 != sp.zeros(5,5)

n=sp.symbols('n', integer=True, positive=True)
v=sp.Matrix([[1,0,0,0,0]])
one=sp.ones(5,1)

def Mpow_apply(k):
    return 4**k*one + k*4**(k-1)*(N*one) + sp.binomial(k,2)*4**(k-2)*(N**2*one)

Z=sp.factor((v*Mpow_apply(n))[0])
Ze=sp.factor((v*E[0]*Mpow_apply(n-1))[0])
ZR=sp.factor((v*E2[(0,1)]*Mpow_apply(n-1))[0])
ZL=sp.factor((v*E[0]*E[0]*Mpow_apply(n-2))[0])
ZD=sp.factor((v*E[0]*E[1]*Mpow_apply(n-2))[0])

Z_expected=4**n*(3*n**2+13*n+16)/16
Ze_expected=4**n*(3*n**2+23*n+38)/64
ZR_expected=4**n*(n+3)/8
ZL_expected=3*4**n*(n**2+11*n+22)/256
ZD_expected=4**n*(3*n**2+33*n+82)/256

for lhs,rhs,name in [
    (Z,Z_expected,"Z"),
    (Ze,Ze_expected,"Ze"),
    (ZR,ZR_expected,"ZR"),
    (ZL,ZL_expected,"ZL"),
    (ZD,ZD_expected,"ZD"),
]:
    assert sp.simplify(lhs-rhs)==0, name

PR=(n-1)*(9*n**3+51*n**2+104*n+92)
PL=2*(41*n**2+181*n+194)
PD=2*(17*n**2+77*n+66)
assert sp.simplify((Ze**2-Z*ZR) - 4**(2*n)*PR/4096)==0
assert sp.simplify((Ze**2-Z*ZL) - 4**(2*n)*PL/4096)==0
assert sp.simplify((Ze**2-Z*ZD) - 4**(2*n)*PD/4096)==0

assert all(c>0 for c in [9,51,104,92])
assert all(c>0 for c in [41,181,194])
assert all(c>0 for c in [17,77,66])

# Direct exact forest enumeration for n=1..4 as an independent finite sanity check.
def is_forest(num_vertices, edges, mask):
    parent=list(range(num_vertices))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra==rb:
            return False
        parent[rb]=ra
        return True
    for j,(a,b) in enumerate(edges):
        if (mask>>j)&1:
            if not union(a,b):
                return False
    return True

def brute(nv):
    # left vertices 0,1,2; right vertices 3,...,3+nv-1.
    edges=[(a,3+i) for i in range(nv) for a in range(3)]
    m=len(edges)
    good=[]
    for mask in range(1<<m):
        if is_forest(3+nv,edges,mask):
            good.append(mask)
    z=len(good)
    z1=sum((mask&1)!=0 for mask in good)
    zr=sum(((mask>>0)&1) and ((mask>>1)&1) for mask in good)
    if nv>=2:
        zl=sum(((mask>>0)&1) and ((mask>>3)&1) for mask in good)
        zd=sum(((mask>>0)&1) and ((mask>>4)&1) for mask in good)
    else:
        zl=zd=None
    return z,z1,zr,zl,zd

def closed(nv):
    z=(4**nv*(3*nv*nv+13*nv+16))//16
    ze=(4**nv*(3*nv*nv+23*nv+38))//64
    zr=(4**nv*(nv+3))//8
    if nv>=2:
        zl=(3*4**nv*(nv*nv+11*nv+22))//256
        zd=(4**nv*(3*nv*nv+33*nv+82))//256
    else:
        zl=zd=None
    return z,ze,zr,zl,zd

for nv in range(1,5):
    assert brute(nv)==closed(nv), (nv,brute(nv),closed(nv))

print("M =", M.tolist())
print("N^3_zero =", N**3 == sp.zeros(5,5))
print("Z_n =", sp.factor(Z_expected))
print("Z_e =", sp.factor(Ze_expected))
print("Z_R =", sp.factor(ZR_expected))
print("Z_L =", sp.factor(ZL_expected))
print("Z_D =", sp.factor(ZD_expected))
print("Rayleigh_factor_R =", sp.factor(PR))
print("Rayleigh_factor_L =", sp.factor(PL))
print("Rayleigh_factor_D =", sp.factor(PD))
for nv in range(1,5):
    print("brute_n",nv,"=",brute(nv))
print("ALL_EXACT_CHECKS_PASS")
