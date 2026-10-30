from fractions import Fraction as F
from itertools import permutations

# Exact datum from fleet02/B09 r15.
a=((0,-6),(0,5),(3,5),(1,0))
b=((7,4),(1,7),(1,-5),(-3,0))
eta=(-1,2)
S=list(permutations(range(4)))
e=(0,1,2,3)

def add(z,w): return (z[0]+w[0],z[1]+w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def comp(p,q): return tuple(p[q[i]] for i in range(4))
def h(sig):
    z=(1,0)
    for i,j in enumerate(sig):
        z=mul(z,add(a[i],b[j]))
    return mul(eta,z)[0]

H={s:F(h(s)) for s in S}
M=max(H.values())
m=sum(H.values(),F(0))/24
d=M-m

V4=[e,(1,0,3,2),(2,3,0,1),(3,2,1,0)]
unused=set(S); cosets=[]
while unused:
    s=min(unused)
    C={comp(s,v) for v in V4}
    cosets.append(C); unused-=C
B=[]; rho={}
for q,C in enumerate(cosets):
    Bq=sum(H[s] for s in C)/4
    B.append(Bq)
    for s in C: rho[s]=q
Q=max(B)
Delta=M-Q
kap={s:H[s]-B[rho[s]] for s in S}
K=max(kap.values())
stars=[s for s in S if kap[s]==K]
assert len(stars)==1
star=stars[0]
reserve=K-Delta

Mij={(i,j):max(H[s] for s in S if s[i]==j)
     for i in range(4) for j in range(4)}
beta=[M-Mij[i,star[i]] for i in range(4)]

def defect(s): return K-kap[s]
def phi(T,r):
    return F(0) if r==0 else 16*T*r/(4*T+r)**2
def Ubar(g):
    return 3*d+2*g-Delta
def qvec(g):
    T=Ubar(g)
    return [phi(T,g+x) for x in beta]

# Exact feasible point of the assignment-defect LP dual.
y=[F(0),F(264),F(1125,2),F(615,2)]
for s in S:
    lhs=sum(y[i] for i in range(4) if s[i]!=star[i])
    assert lhs <= defect(s), (s,lhs,defect(s))

def ham(p,q): return sum(x!=y for x,y in zip(p,q))
cstar=min(defect(s)/ham(s,star) for s in S if s!=star)
assert cstar==132

U0=Ubar(F(0))
assert U0==F(38171,2)
assert all(U0>2*x for x in beta)

def dual_rhs(g):
    q=qvec(g)
    return sum(y[i]*q[i] for i in range(4))
def residual(g):
    return reserve-g-dual_rhs(g)

assert M==7470
assert m==-108 and d==7578
assert Q==F(7643,2) and Delta==F(7297,2)
assert K==F(7825,2) and reserve==264
assert star==(1,2,0,3)
assert beta==[7054,7062,0,0]

r173=residual(F(173))
r174=residual(F(174))
assert r173==F(44721002882415194611,43802913306687009721)
assert r174==F(-17138174777403444,684723721361319025)
assert r173>0 and r174<0

print("PASS MOC4-STANDARD-DEFECT-LP-DUAL-v1")
print("M =",M,"m =",m,"d =",d)
print("Q =",Q,"Delta =",Delta,"K =",K,"reserve =",reserve)
print("star =",star,"beta =",beta)
print("dual_y =",y)
print("U0 =",U0)
print("residual_173 =",r173)
print("residual_174 =",r174)
print("CONCLUSION: every hypothetical positive support gap on the exact r15 datum satisfying the genuine-unitary Cartan/Hessian collar and standard-channel identities obeys gamma < 174.")
