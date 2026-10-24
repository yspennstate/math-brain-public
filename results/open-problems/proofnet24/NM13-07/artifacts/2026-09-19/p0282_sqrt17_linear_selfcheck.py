from fractions import Fraction

# Exact arithmetic in Q(sqrt(17)); elements are a+b*sqrt(17).
def qa(a=0,b=0): return (Fraction(a),Fraction(b))
def qadd(u,v): return (u[0]+v[0],u[1]+v[1])
def qneg(u): return (-u[0],-u[1])
def qmul(u,v):
    return (u[0]*v[0]+17*u[1]*v[1], u[0]*v[1]+u[1]*v[0])

def padd(P,Q):
    R=dict(P)
    for m,c in Q.items():
        R[m]=qadd(R.get(m,qa()),c)
        if R[m]==qa(): del R[m]
    return R

def pmul(P,Q):
    R={}
    for (ax,aj),u in P.items():
        for (bx,bj),v in Q.items():
            m=(ax+bx,aj+bj)
            R[m]=qadd(R.get(m,qa()),qmul(u,v))
    return {m:c for m,c in R.items() if c!=qa()}

def ppow(P,n):
    R={(0,0):qa(1)}
    while n:
        if n&1:R=pmul(R,P)
        P=pmul(P,P); n//=2
    return R

def pscale(P,c): return {m:qmul(v,c) for m,v in P.items()}

def positive_qsqrt17(u):
    a,b=u
    if b==0:return a>0
    if b>0 and a>=0:return True
    if b<0 and a<=0:return False
    if b>0:return 17*b*b > a*a
    return a*a > 17*b*b

X={(1,0):qa(1)}
J={(0,1):qa(1)}
ONE={(0,0):qa(1)}
alpha=qa(Fraction(-1,2),Fraction(1,2))
D=padd(X,pscale(J,alpha))

jp1=padd(J,ONE)
dp1=padd(D,ONE)
dp3=padd(D,{(0,0):qa(3)})
jpd2=padd(padd(J,D),{(0,0):qa(2)})
jpd=padd(J,D)
E=padd(pmul(pmul(jp1,ppow(dp1,2)),ppow(jpd2,2)),
       pscale(pmul(pmul(J,ppow(dp3,2)),ppow(jpd,2)),qa(-1)))

s=qa(0,1)
expected={
 (4,0):qa(1),
 (3,1):qmul(qa(2),s),(3,0):qa(6),
 (2,2):qa(21),(2,1):qadd(qa(3),qmul(qa(9),s)),(2,0):qa(13),
 (1,3):qmul(qa(4),s),(1,2):qadd(qa(63),qmul(qa(3),s)),
 (1,1):qadd(qa(9),qmul(qa(13),s)),(1,0):qa(12),
 (0,3):qadd(qa(10),qmul(qa(6),s)),
 (0,2):qadd(qa(Fraction(105,2)),qmul(qa(Fraction(9,2)),s)),
 (0,1):qadd(qa(2),qmul(qa(6),s)),(0,0):qa(4)
}
assert E==expected
assert all(positive_qsqrt17(c) for c in expected.values())
assert (0,4) not in E
assert qadd(qadd(qmul(alpha,alpha),alpha),qa(-4))==qa()
print('sqrt17_polynomial_identity=PASS')
print('all_shifted_coefficients_strictly_positive=PASS')
print('j4_coefficient_cancelled=PASS')

def partitions(n, maxpart=None):
    if n==0:
        yield (); return
    if maxpart is None or maxpart>n:maxpart=n
    for first in range(maxpart,0,-1):
        for tail in partitions(n-first,first):
            yield (first,)+tail

def contents(mu):
    return [q-r for r,rowlen in enumerate(mu, start=1) for q in range(1,rowlen+1)]

def addable(mu):
    out=[]; L=list(mu)
    for r in range(len(L)):
        if r==0 or L[r] < L[r-1]:
            new=L.copy(); new[r]+=1
            out.append((tuple(new),new[r]-(r+1)))
    out.append((tuple(L+[1]),1-(len(L)+1)))
    seen=set(); z=[]
    for lam,c in out:
        if lam not in seen: seen.add(lam); z.append((lam,c))
    return z

def edge_ratio(mu,c0,K):
    z=Fraction(1)
    for c in contents(mu):
        z*=Fraction((K-c)*(K-c)-1,(K-c)*(K-c))
    z*=Fraction(K-c0-1,K-c0)
    return z

checked=0
for j in range(2,11):
    d=2*j+1; K=j+d+1
    q=Fraction((d+1)*(j+d+2),(d+3)*(j+d+1))
    vals=[]
    for mu in partitions(j-1):
        for lam,c0 in addable(mu):
            if sum(lam)!=j: continue
            r=edge_ratio(mu,c0,K)
            assert r>=q
            vals.append((r,mu,lam)); checked+=1
    m=min(v[0] for v in vals)
    assert m==q
    assert any(r==q and mu==(j-1,) and lam==(j,) for r,mu,lam in vals)
print(f'exact_growth_edges_checked={checked}')
print('one_row_is_exact_minimum_edge=PASS')
print('ALL_EXACT_CHECKS_PASS')
