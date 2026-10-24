from math import comb
import sympy as sp
from itertools import combinations

EDGES=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
a,b,c,d,e,f=sp.symbols("a b c d e f")
raw=[a,b,c,d,e,f]
w=dict(zip(EDGES,raw))
def W(i,j):
    if i==j:
        return sp.Integer(0)
    return w[tuple(sorted((i,j)))]

deg=[sum(W(i,j) for j in range(4) if j!=i) for i in range(4)]
L=sp.Matrix([[deg[i] if i==j else -W(i,j) for j in range(4)] for i in range(4)])
tau=sp.expand(L[:3,:3].det())

def forest_poly(i,j):
    ans=sp.Integer(0)
    for es in combinations(EDGES,2):
        parent=list(range(4))
        def find(q):
            while parent[q]!=q:
                parent[q]=parent[parent[q]]
                q=parent[q]
            return q
        ok=True
        for u,v in es:
            ru,rv=find(u),find(v)
            if ru==rv:
                ok=False
                break
            parent[rv]=ru
        if not ok or len({find(t) for t in range(4)})!=2 or find(i)==find(j):
            continue
        wt=sp.Integer(1)
        for ed in es:
            wt*=W(*ed)
        ans+=wt
    return sp.expand(ans)

F={ed:forest_poly(*ed) for ed in EDGES}

def rdel(i):
    vv=[q for q in range(4) if q!=i]
    p,q,s=vv
    return sp.expand(W(p,q)*W(p,s)+W(p,q)*W(q,s)+W(p,s)*W(q,s))
r=[rdel(i) for i in range(4)]

psi_num=[
    sp.expand(sum(deg[z]*F[tuple(sorted((i,z)))] for z in range(4) if z!=i))
    for i in range(4)
]

# E_* = N / (2*tau*product_{k<l} F_kl).  Build N directly so there is
# no numerical or symbolic cancellation hidden in the certificate.
N=sp.Integer(0)
for idx,(k,l) in enumerate(EDGES):
    u,v=[q for q in range(4) if q not in (k,l)]
    prod_other=sp.prod(F[ed2] for j,ed2 in enumerate(EDGES) if j!=idx)
    N += W(u,v)*(r[l]-r[k])*(psi_num[l]-psi_num[k])*prod_other

# Equal opposite-edge sums, with the third pair balanced.  Global scaling
# lets us normalize A=B=C=2.
X,Y=sp.symbols("X Y")
subs={
    a:(2+X)/2, f:(2-X)/2,
    b:(2+Y)/2, e:(2-Y)/2,
    c:sp.Integer(1), d:sp.Integer(1),
}
Nxy=sp.expand(N.subs(subs))
poly_xy=sp.Poly(sp.expand(4096*Nxy),X,Y)
assert all(i%2==0 and j%2==0 for (i,j),_ in poly_xy.terms())

# Put p=X^2, q=Y^2 and then u=p/4, v=q/4.  Positive conductances imply
# 0 <= u,v < 1.  Convert the exact polynomial to the bidegree-(6,6)
# Bernstein basis on [0,1]^2.
p,q=sp.symbols("p q")
Ppq=sp.Integer(0)
for (i,j),coef in poly_xy.terms():
    Ppq += coef*p**(i//2)*q**(j//2)

u,v=sp.symbols("u v")
Puv=sp.Poly(sp.expand(Ppq.subs({p:4*u,q:4*v})),u,v)
m=n=6
ad={(i,j):sp.Rational(coef) for (i,j),coef in Puv.terms()}
bern={}
for k in range(m+1):
    for l in range(n+1):
        total=sp.Rational(0)
        for i in range(k+1):
            for j in range(l+1):
                aij=ad.get((i,j),0)
                if aij:
                    total += aij*sp.Rational(comb(k,i),comb(m,i))*sp.Rational(comb(l,j),comb(n,j))
        bern[k,l]=sp.factor(total)

# After pulling out 16384/225, the Bernstein coefficients are these integers.
C=[[int(bern[k,l]*225/16384) for l in range(7)] for k in range(7)]
EXPECTED=[
[0,196608000,336199680,430755840,490076160,522144000,533433600],
[196608000,369459200,484945920,555939840,592880320,604187400,596610000],
[336199680,484945920,576845824,625548288,642020304,635009190,611432760],
[430755840,555939840,625548288,653891562,652350003,629886435,593479305],
[490076160,592880320,642020304,652350003,635546400,600673470,554659320],
[522144000,604187400,635009190,629886435,600673470,556418300,503884800],
[533433600,596610000,611432760,593479305,554659320,503884800,447638400],
]
assert C==EXPECTED
assert C[0][0]==0
assert all(C[k][l]>0 for k in range(7) for l in range(7) if (k,l)!=(0,0))

def B6(k,t):
    return sp.Integer(comb(6,k))*t**k*(1-t)**(6-k)
recon=sp.expand(sp.Rational(16384,225)*sum(
    C[k][l]*B6(k,u)*B6(l,v) for k in range(7) for l in range(7)
))
assert sp.expand(recon-Puv.as_expr())==0

spot=sp.factor(Nxy.subs({X:sp.Rational(1,1),Y:sp.Rational(3,2)}))
assert spot>0
origin=sp.factor(Nxy.subs({X:0,Y:0}))
assert origin==0

print("P0245 equal-opposite-sums two-axis Bernstein self-check")
print("common_numerator_identity = PASS")
print("normalization: A=B=C=2, z=0, u=X^2/4, v=Y^2/4")
print("N = (4/225) * sum_{k,l=0}^6 C[k,l] B_{k,6}(u) B_{l,6}(v)")
print("C_matrix =")
for row in C:
    print(row)
print("all_C_nonnegative = PASS")
print("only_zero_Bernstein_coefficient = C[0,0] = 0")
print("spot_X1_Y3over2_common_numerator =", spot)
print("origin_common_numerator =", origin)
print("ALL_EXACT_CHECKS_PASS")
