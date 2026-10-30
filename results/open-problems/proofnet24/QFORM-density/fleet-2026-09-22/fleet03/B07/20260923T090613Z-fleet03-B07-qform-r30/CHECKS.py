from itertools import combinations, product
import random, math

# Algebraic regression for fleet03/B07 r30. Not proof evidence.

def det2(M, u,v,s,t):
    return M[u][s]*M[v][t]-M[u][t]*M[v][s]

def e2(M):
    nr,nc=len(M),len(M[0])
    return sum(det2(M,u,v,s,t)**2
               for u,v in combinations(range(nr),2)
               for s,t in combinations(range(nc),2))

def check_one(nr,nc,rng):
    b=rng.randint(-3,3)
    r=[rng.randint(-3,3) for _ in range(nc)]
    c=[rng.randint(-3,3) for _ in range(nr)]
    D=[[rng.randint(-3,3) for _ in range(nc)] for __ in range(nr)]

    G=0.0; V2=0.0; Smon=0.0
    for u,v in combinations(range(nr),2):
        for s,t in combinations(range(nc),2):
            psi=(r[s]*(c[u]*D[v][t]-c[v]*D[u][t])
                 -r[t]*(c[u]*D[v][s]-c[v]*D[u][s]))
            d=b*det2(D,u,v,s,t)-psi
            G += d*d
            V2 += psi*psi
    for u in range(nr):
        for v in range(nr):
            if u==v: continue
            for s in range(nc):
                for t in range(nc):
                    if s==t: continue
                    Smon += c[u]**2*r[s]**2*D[v][t]**2

    rr=sum(x*x for x in r); cc=sum(x*x for x in c)
    DF=sum(x*x for row in D for x in row)
    Dt_c=[sum(D[u][t]*c[u] for u in range(nr)) for t in range(nc)]
    D_r=[sum(D[u][t]*r[t] for t in range(nc)) for u in range(nr)]
    cDr=sum(c[u]*D_r[u] for u in range(nr))
    exact=rr*cc*DF-rr*sum(x*x for x in Dt_c)-cc*sum(x*x for x in D_r)+cDr*cDr
    assert abs(V2-exact)<1e-9
    assert V2 <= 4*Smon+1e-9
    assert math.sqrt(G) <= abs(b)*math.sqrt(e2(D))+math.sqrt(V2)+1e-9

    best=0.0
    for rowbits in product((0,1), repeat=nr):
        for colbits in product((0,1), repeat=nc):
            c0=sum(c[u]**2 for u in range(nr) if rowbits[u]==0)
            r0=sum(r[s]**2 for s in range(nc) if colbits[s]==0)
            h=sum(D[v][t]**2 for v in range(nr) if rowbits[v]==1
                               for t in range(nc) if colbits[t]==1)
            best=max(best,c0*r0*h)
    if Smon>0:
        assert best+1e-9 >= Smon/16
        trans_ratio=best/(Smon/16)
    else:
        trans_ratio=float('inf')

    E=e2(D); bestp=0.0
    for rowbits in product((0,1), repeat=nr):
        for colbits in product((0,1), repeat=nc):
            for flip in (0,1):
                a=sum(D[u][s]**2 for u in range(nr) if rowbits[u]==0
                                      for s in range(nc) if colbits[s]==flip)
                d=sum(D[v][t]**2 for v in range(nr) if rowbits[v]==1
                                      for t in range(nc) if colbits[t]==1-flip)
                bestp=max(bestp,a*d)
    if E>0:
        assert bestp+1e-9 >= E/16
        e2_ratio=bestp/(E/16)
    else:
        e2_ratio=float('inf')
    return trans_ratio,e2_ratio

rng=random.Random(3007)
mins=[float('inf'),float('inf')]
cases=0
for nr,nc in [(2,2),(2,3),(3,2),(3,3),(3,4),(4,3)]:
    for _ in range(150):
        a,b=check_one(nr,nc,rng)
        mins[0]=min(mins[0],a); mins[1]=min(mins[1],b)
        cases+=1

gamma_den=12824703626379264
sqrt_den=math.isqrt(gamma_den)
assert sqrt_den*sqrt_den==gamma_den
print('cases',cases)
print('min_trans_ratio',mins[0])
print('min_e2_ratio',mins[1])
print('gamma_sqrt_den',sqrt_den)
print('edge_three_link_den',8*sqrt_den)
print('trans_three_link_den',16*sqrt_den)
print('STATUS=PASS')
