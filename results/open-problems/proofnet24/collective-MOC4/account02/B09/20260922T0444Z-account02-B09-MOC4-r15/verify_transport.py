from fractions import Fraction as F
from itertools import permutations

a=((0,-6),(0,5),(3,5),(1,0))
b=((7,4),(1,7),(1,-5),(-3,0))
eta=(-1,2)
S=list(permutations(range(4)))
e=(0,1,2,3)

def add(z,w): return (z[0]+w[0],z[1]+w[1])
def sub(z,w): return (z[0]-w[0],z[1]-w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def div(z,w):
    d=w[0]*w[0]+w[1]*w[1]
    return (F(z[0]*w[0]+z[1]*w[1],d),F(z[1]*w[0]-z[0]*w[1],d))
def comp(p,q): return tuple(p[q[i]] for i in range(4))
def cycle(*c):
    p=list(range(4))
    for k,x in enumerate(c): p[x]=c[(k+1)%len(c)]
    return tuple(p)
def group(gens):
    H={e}
    while True:
        old=len(H)
        for h in list(H):
            for g in gens:
                H.add(comp(g,h)); H.add(comp(h,g))
        if len(H)==old: return sorted(H)
def h(sig):
    z=(1,0)
    for i,j in enumerate(sig): z=mul(z,add(a[i],b[j]))
    return mul(eta,z)[0]

H={s:F(h(s)) for s in S}
M=max(H.values()); m=sum(H.values(),F(0))/24; d=M-m

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
Q=max(B); Delta=M-Q
kap={s:H[s]-B[rho[s]] for s in S}
K=max(kap.values())
maxs=[s for s in S if kap[s]==K]
assert len(maxs)==1
star=maxs[0]
K2=max(kap[s] for s in S if s!=star)
reserve=K-Delta

def ham(p,q): return sum(x!=y for x,y in zip(p,q))
cstar=min((K-kap[s])/ham(s,star) for s in S if s!=star)

Mij={(i,j):max(H[s] for s in S if s[i]==j) for i in range(4) for j in range(4)}
beta={(i,j):M-Mij[i,j] for i in range(4) for j in range(4)}
betastar=[beta[i,star[i]] for i in range(4)]

trans=[cycle(i,j) for i in range(4) for j in range(i+1,4)]
def pair_gaps(side):
    out=[]
    for t in trans:
        if side=="left":
            roof=max((H[s]+H[comp(t,s)])/2 for s in S)
        else:
            roof=max((H[s]+H[comp(s,t)])/2 for s in S)
        out.append(2*M-2*roof)
    return out
Gleft=sum(pair_gaps("left"),F(0)); Gright=sum(pair_gaps("right"),F(0))
G=max(Gleft,Gright)
bidir=(3*d-Delta-G/2)/4

Hs=[
 group([cycle(0,3),cycle(1,2)]),
 group([cycle(0,1),cycle(0,2,1,3)]),
 group([cycle(1,2),cycle(1,3)]),
 group([cycle(0,1),cycle(2,3)]),
 group([cycle(0,2)]),
 group([cycle(0,3),cycle(0,1,3,2)]),
 group([cycle(0,1),cycle(0,3)]),
]
weights=[F(1,3),F(1,3),F(1,2),F(1,3),F(2,3),F(1,3),F(1,2)]
assert [len(x) for x in Hs]==[4,8,6,4,2,8,6]
def coset_roof(Gp,side):
    unused=set(S); av=[]
    while unused:
        g=next(iter(unused))
        C={comp(x,g) for x in Gp} if side=="left" else {comp(g,x) for x in Gp}
        av.append(sum(H[s] for s in C)/len(C)); unused-=C
    return max(av)
def subgroup_bound(side):
    rr=[coset_roof(Gp,side) for Gp in Hs]
    return sum(w*x for w,x in zip(weights,rr))-2*m,rr
LamL,roofL=subgroup_bound("left")
LamR,roofR=subgroup_bound("right")

def phi(T,r):
    return F(0) if r==0 else 16*T*r/(4*T+r)**2
def Ubar(g): return 3*d+2*g-Delta
def rhs(g):
    T=Ubar(g)
    return cstar*sum((phi(T,g+x) for x in betastar),F(0))
def residual(g): return reserve-g-rhs(g)

assert M==7470
assert m==-108 and d==7578
assert Q==F(7643,2) and Delta==F(7297,2)
assert K==F(7825,2) and K2==Delta and reserve==264
assert star==(1,2,0,3)
assert cstar==132
assert betastar==[7054,7062,0,0]
assert Gleft==35681 and Gright==33406 and bidir==F(1245,4)
assert LamL==8336 and LamR==F(27175,3)
assert residual(F(179))>0
assert residual(F(180))<0
U0=Ubar(F(0))
assert U0==F(38171,2)
assert all(U0>2*x for x in betastar)
pts=[(-z[0],-z[1]) for z in a]+list(b)
z1,z2,z3,z4=pts[0],pts[1],pts[2],pts[4]
cr=div(mul(sub(z1,z3),sub(z2,z4)),mul(sub(z1,z4),sub(z2,z3)))
assert cr==(F(-754,159),F(572,159))
assert cr[1]!=0

print("PASS exact Gaussian-integer endpoint verification")
print("M =",M,"m =",m,"d =",d)
print("Q =",Q,"Delta =",Delta)
print("Kstd =",K,"K2 =",K2,"standard_reserve =",reserve)
print("unique_standard_maximizer =",star,"c_star =",cstar)
print("block_gaps_on_star =",betastar)
print("G_left =",Gleft,"G_right =",Gright,"bidirectional_pair_ceiling =",bidir)
print("subgroup_bounds =",LamL,LamR,"subgroup_gaps =",LamL-M,LamR-M)
print("U(0) =",Ubar(F(0)))
print("residual_at_179 =",residual(F(179)))
print("residual_at_180 =",residual(F(180)))
print("rhs_at_180 =",rhs(F(180)),"lhs_at_180 =",reserve-F(180))
print("cross_ratio =",cr[0],"+",cr[1],"i")
print("CONCLUSION: every hypothetical positive support gap obeying the derived transport/Cartan/Hessian necessary inequality is < 180; prior endpoint ceilings here are 264 (standard), 1245/4 (bidirectional pair), and 866 (subgroup cubature).")
