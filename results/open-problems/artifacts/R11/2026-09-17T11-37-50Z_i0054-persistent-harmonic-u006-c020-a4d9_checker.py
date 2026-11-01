from fractions import Fraction as F
from math import factorial

checks = 0

def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)), F(0))

def beta_int(i,j):
    return F(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def weights(N):
    H = harmonic(N-1)
    ws=[]
    pis=[]
    for j in range(1,N):
        x=F(j,N)
        w=F(1, 2*N) / (x*(1-x))
        ws.append(w)
        pis.append(w/H)
    return H, ws, pis

def sprob(x,b,i):
    return x**i*(1-x)**(b-i) + x**(b-i)*(1-x)**i

def solve_linear(A,b):
    # exact Gauss-Jordan
    n=len(A)
    M=[list(A[r])+[b[r]] for r in range(n)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c] != 0)
        M[c],M[p]=M[p],M[c]
        piv=M[c][c]
        M[c]=[z/piv for z in M[c]]
        for r in range(n):
            if r==c: continue
            z=M[r][c]
            if z:
                M[r]=[M[r][q]-z*M[c][q] for q in range(n+1)]
    return [M[r][-1] for r in range(n)]

# 1) exact harmonic normalization and stationary law checks.
for N in range(2,51):
    H,ws,pi=weights(N)
    assert sum(ws,F(0)) == H
    checks += 1
    assert sum(pi,F(0)) == 1
    checks += 1
    rho=F(1,N)
    # K=(1-rho)I+rho Pi; row sums and pi K = pi
    for j in range(N-1):
        rowsum=(1-rho) + rho*sum(pi,F(0))
        assert rowsum==1
        checks += 1
    for ell in range(N-1):
        stat=sum(pi[j]*((1-rho if j==ell else F(0)) + rho*pi[ell]) for j in range(N-1))
        assert stat==pi[ell]
        checks += 1
    # centered eigenfunction identity for f(j)=j^2+3j+1
    vals=[F((j+1)**2+3*(j+1)+1) for j in range(N-1)]
    mean=sum(pi[j]*vals[j] for j in range(N-1))
    cent=[v-mean for v in vals]
    for j in range(N-1):
        Kf=(1-rho)*cent[j] + rho*sum(pi[l]*cent[l] for l in range(N-1))
        assert Kf==(1-rho)*cent[j]
        checks += 1

# 2) exact stationary-average identity with the C001 Riemann generator.
for N in range(2,51):
    H,ws,pi=weights(N)
    for b in range(2,10):
        if b>N+5: # no need, but keep broad hidden-independent algebra grid
            continue
        for i in range(1,b):
            q_env=sum(ws[j-1]*sprob(F(j,N),b,i) for j in range(1,N))
            q_grid=F(1,N)*sum((F(j,N)**(i-1)*F(N-j,N)**(b-i-1) for j in range(1,N)),F(0))
            assert q_env==q_grid
            checks += 1

# 3) exact b=2 averaged rate and second moment bound used in proof.
for N in range(2,151):
    H,ws,pi=weights(N)
    lambdas=[]
    for j in range(1,N):
        x=F(j,N)
        lambdas.append(H*2*x*(1-x))
    mean=sum(pi[j]*lambdas[j] for j in range(N-1))
    assert mean==F(N-1,N)
    checks += 1
    second=sum(pi[j]*lambdas[j]**2 for j in range(N-1))
    # lambda=H*s, s<=1/2 for b=2; crude exact bound second <= H*mean
    assert second <= H*mean
    checks += 1

# 4) polynomial Riemann sums approach CTCS beta rates (exact inequalities at large finite N).
# These are self-checks only, not the asymptotic proof.
for b in range(2,9):
    for i in range(1,b):
        target=beta_int(i,b-i)
        for N in (100,200,500):
            q=F(1,N)*sum((F(j,N)**(i-1)*F(N-j,N)**(b-i-1) for j in range(1,N)),F(0))
            # Endpoint cases converge with O(1/N); this broad tolerance is exact rational.
            assert abs(q-target) <= F(2*b, N)
            checks += 1

# 5) C020 exact N=4 first-root-split law in the persistent environment.
N=4
H,ws,pi=weights(N)
rho=F(1,N)
Delta=F(1,N**3)
a=Delta*H
assert H==F(11,6)
assert pi==[F(4,11),F(3,11),F(4,11)]
assert a==F(11,384)
checks += 3

# total probabilities (conditional on activation) of 1|3 and 2|2 root shapes.
p13=[]; p22=[]; pvis=[]
for j in range(1,N):
    x=F(j,N)
    p13_j=4*(x*(1-x)**3 + x**3*(1-x))  # four singleton supports, each unordered orientation
    # 3 unordered 2|2 supports; each particular support counted with both color orientations
    p22_j=3*(2*x**2*(1-x)**2)
    p13.append(p13_j); p22.append(p22_j); pvis.append(p13_j+p22_j)
assert p13==[F(15,32),F(1,2),F(15,32)]
assert p22==[F(27,128),F(3,8),F(27,128)]
checks += 2

K=[]
for j in range(N-1):
    K.append([((1-rho) if j==l else F(0)) + rho*pi[l] for l in range(N-1)])

# Absorb before environment refresh; if no visible split, refresh K.
A=[]
b13=[]
b22=[]
for j in range(N-1):
    no=1-a*pvis[j]
    A.append([(F(1) if j==l else F(0)) - no*K[j][l] for l in range(N-1)])
    b13.append(a*p13[j]); b22.append(a*p22[j])
u13=solve_linear(A,b13)
u22=solve_linear(A,b22)
P13=sum(pi[j]*u13[j] for j in range(N-1))
P22=sum(pi[j]*u22[j] for j in range(N-1))
assert P13==F(245524,376819)
assert P22==F(131295,376819)
assert P13+P22==1
checks += 3

# Exchangeability: four 1|3 supports, three 2|2 supports.
ratio=(P13/F(4))/(P22/F(3))
assert ratio==F(61381,43765)
checks += 1

# Frozen-equivalence separation from every earlier finite binary class.
old_binary={
    'original_CTCS':F(2,1),
    'C001':F(7,5),
    'C009':F(2699,1365),
    'C010':F(2273,1153),
}
for name,r in old_binary.items():
    assert ratio != r
    checks += 1

# 6) Finite-scale obstruction signature: frozen environment has near-correct annealed
# mean rate but increasingly boundary-heavy stationary environment.
for N in (10,20,50,100,200):
    H,ws,pi=weights(N)
    mean=sum(pi[j-1]*(H*2*F(j,N)*F(N-j,N)) for j in range(1,N))
    assert mean==F(N-1,N)
    checks += 1

print(f'EXACT_CHECKS={checks}')
print(f'N4_H={F(11,6)}')
print(f'N4_activation={a}')
print(f'N4_P_type_1_3={P13}')
print(f'N4_P_type_2_2={P22}')
print(f'N4_particular_ratio={ratio}')
print(f'ratio_minus_C001={ratio-F(7,5)}')
print('ALL_EXACT_CHECKS_PASS')
