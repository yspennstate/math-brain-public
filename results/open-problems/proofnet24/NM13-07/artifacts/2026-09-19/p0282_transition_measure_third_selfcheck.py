from fractions import Fraction
from math import factorial


def partitions(n, maxp=None):
    if n == 0:
        yield ()
        return
    if maxp is None or maxp > n:
        maxp = n
    for a in range(maxp, 0, -1):
        for rest in partitions(n-a, a):
            yield (a,) + rest


def dim(part):
    n = sum(part)
    hook = 1
    for r, row in enumerate(part):
        for c in range(row):
            below = sum(1 for rr in range(r+1, len(part)) if part[rr] > c)
            hook *= (row-c) + below
    return factorial(n) // hook


def contents(part):
    return [(c+1)-(r+1) for r,row in enumerate(part) for c in range(row)]


def children(part):
    L = list(part)
    out = []
    for r in range(len(L)+1):
        if r == len(L):
            if not L or L[-1] >= 1:
                lam = tuple(L+[1])
                out.append((lam, -r))
        else:
            new = L[r]+1
            if r == 0 or new <= L[r-1]:
                M = L.copy(); M[r] = new
                out.append((tuple(M), new-(r+1)))
    seen = set(); ans=[]
    for x in out:
        if x[0] not in seen:
            seen.add(x[0]); ans.append(x)
    return ans


def trans(mu):
    s = sum(mu); fm = dim(mu)
    arr=[]
    for lam,c in children(mu):
        p = Fraction(dim(lam), (s+1)*fm)
        arr.append((lam,c,p))
    return arr


def B(mu,K):
    z=Fraction(1)
    for c in contents(mu):
        z *= Fraction((K-c)**2-1,(K-c)**2)
    return z


def G(mu,K):
    return sum((p*Fraction(1,K-c) for _,c,p in trans(mu)), Fraction(0))


def H(mu,K):
    b=B(mu,K)
    return b*b*sum((p*Fraction(K-c-1,K-c)**2 for _,c,p in trans(mu)), Fraction(0))

count_shapes=0
count_K=0
for s in range(1,10):
    for mu in partitions(s):
        T=trans(mu)
        assert sum((p for _,_,p in T), Fraction(0)) == 1
        assert sum((p*c for _,c,p in T), Fraction(0)) == 0
        assert sum((p*c*c for _,c,p in T), Fraction(0)) == s
        for K in range(s+2, 4*s+11):
            g=G(mu,K)
            assert B(mu,K) * K * g == 1
            U = Fraction(1,K) + Fraction(s, K*K*(K-s))
            assert g <= U
            lower = ((1-U)/(K*U))**2
            assert H(mu,K) >= lower
            count_K += 1
        count_shapes += 1

poly = [1,7,35,93,144,44]
assert all(a>0 for a in poly)

def P(j):
    return sum(a*(j**i) for i,a in enumerate(poly))

for j in range(1,5001):
    delta0 = Fraction(j-1, (2*j+1)*(j+2))
    r0 = (1 - delta0/Fraction(2*j,1))/(1+delta0)
    q = Fraction(j+1,j)*r0*r0
    rhs = Fraction(P(j), 4*j**3*(2*j*j+6*j+1)**2)
    assert q-1 == rhs
    assert q > 1

for j in range(1,300):
    for extra in (0,1,2,5,20,100):
        n=3*j+extra
        s=j-1; K=n-j+1
        delta=Fraction(s, K*(K-s))
        U=Fraction(1+delta,K)
        L=((1-U)/(K*U))**2
        Q=Fraction(j+1,j)*Fraction(K,K-1)**2*L
        assert Q>1

print('P0282 transition-measure one-third self-check')
print('partition_shapes_checked=',count_shapes)
print('shape_K_instances_checked=',count_K)
print('verified: Plancherel transition mass, E[C]=0, E[C^2]=s')
print('verified: B_mu(K) * K * G_mu(K) = 1')
print('verified: G upper bound and conditional Jensen lower bound')
print('boundary_polynomial_coeffs_ascending=',poly)
print('verified_exact_boundary_identity_j=1..5000')
print('verified_full_Q_lower_grid_j=1..299 extras={0,1,2,5,20,100}')
print('ALL_EXACT_CHECKS_PASS')
