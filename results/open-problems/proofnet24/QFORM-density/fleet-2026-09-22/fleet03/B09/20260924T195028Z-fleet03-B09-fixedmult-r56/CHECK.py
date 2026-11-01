import math, random, itertools
SEED=20260924195028
random.seed(SEED)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm2(a): return dot(a,a)
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def wedge2(a,b): return norm2(a)*norm2(b)-dot(a,b)**2
max_hub_err=max_distinct_err=0.0
for trial in range(300):
    m=random.randint(2,6); n=random.randint(2,6); nh=random.randint(2,6)
    u=[random.uniform(-2,2) for _ in range(m)]
    v=[random.uniform(-2,2) for _ in range(n)]
    cs=[[random.uniform(-2,2) for _ in range(m)] for __ in range(nh)]
    rs=[[random.uniform(-2,2) for _ in range(n)] for __ in range(nh)]
    alpha=[max(0.0,wedge2(u,c)) for c in cs]
    beta=[max(0.0,wedge2(v,r)) for r in rs]
    for h in range(nh):
        a=random.uniform(-3,3); F=0.0
        for P in itertools.combinations(range(m),2):
            for Q in itertools.combinations(range(n),2):
                M=[[u[P[0]]*v[Q[0]],u[P[0]]*v[Q[1]],cs[h][P[0]]],
                   [u[P[1]]*v[Q[0]],u[P[1]]*v[Q[1]],cs[h][P[1]]],
                   [rs[h][Q[0]],rs[h][Q[1]],a]]
                F += det3(M)**2
        target=alpha[h]*beta[h]
        max_hub_err=max(max_hub_err,abs(F-target)/(1+abs(target)))
    A0=sum(alpha); B0=sum(beta); S=sum(x*y for x,y in zip(alpha,beta))
    Omega=A0*B0-S
    direct=sum(beta[g]*alpha[h] for g in range(nh) for h in range(nh) if g!=h)
    max_distinct_err=max(max_distinct_err,abs(Omega-direct)/(1+abs(Omega)))
S0=4322241/61035156250
C3=3*2**(4/3)*math.e**(1/3)
cross=C3*(S0/16)**(-1/6)
common=3*math.e**(2/3)*(4*S0/5)**(-1/6)
partner=(5/3)*2**(6/5)
assert max_hub_err<1e-10
assert max_distinct_err<1e-12
assert cross<83 and common<30 and partner<3.829
print("PASS")
print("seed",SEED)
print("max normalized fixed-hub identity error",max_hub_err)
print("max normalized distinct-hub identity error",max_distinct_err)
print("S0",repr(S0))
print("rank-one disjoint-hub branch bound",repr(cross))
print("rank-one common-hub branch bound",repr(common))
print("partner bound",repr(partner))
