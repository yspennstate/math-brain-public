from fractions import Fraction as F
from math import comb

def rising(a,n):
    z=F(1)
    for r in range(n):
        z *= a+r
    return z

def falling(n,k):
    z=1
    for r in range(k):
        z *= n-r
    return z

def beta_binom(N,a):
    den=rising(2*a,N)
    return [F(comb(N,j))*rising(a,j)*rising(a,N-j)/den for j in range(N+1)]

def transition(N,a,j):
    den=F(N)*(F(N)+2*a)
    pplus=F(N-j)*(F(j)+a)/den
    pminus=F(j)*(F(N-j)+a)/den
    p0=F(1)-pplus-pminus
    return pminus,p0,pplus

def Kmat(N,a):
    K=[[F(0) for _ in range(N+1)] for __ in range(N+1)]
    for j in range(N+1):
        pm,p0,pp=transition(N,a,j)
        K[j][j]=p0
        if j>0: K[j][j-1]=pm
        if j<N: K[j][j+1]=pp
    return K

def split_given_count(N,s,i,j):
    b=i+j
    den=F(falling(N,b))
    return F(falling(s,i)*falling(N-s,j)+falling(s,j)*falling(N-s,i),1)/den

def solve_linear(A,b):
    n=len(b)
    M=[list(A[i])+[b[i]] for i in range(n)]
    for col in range(n):
        piv=next(r for r in range(col,n) if M[r][col] != 0)
        M[col],M[piv]=M[piv],M[col]
        q=M[col][col]
        M[col]=[x/q for x in M[col]]
        for r in range(n):
            if r==col: continue
            q=M[r][col]
            if q:
                M[r]=[M[r][c]-q*M[col][c] for c in range(n+1)]
    return [M[i][-1] for i in range(n)]

def eventual_shape_N4(a,eps):
    N=4
    K=Kmat(N,a)
    pi=beta_binom(N,a)
    A=[[F(int(r==c)) for c in range(N+1)] for r in range(N+1)]
    b13=[F(0)]*(N+1)
    b22=[F(0)]*(N+1)
    for s in range(N+1):
        kill = eps if 0<s<N else F(0)
        cont=F(1)-kill
        for t in range(N+1):
            A[s][t] -= cont*K[s][t]
        if s in (1,3): b13[s]=eps
        if s==2: b22[s]=eps
    u13=solve_linear(A,b13)
    u22=solve_linear(A,b22)
    return (sum(pi[s]*u13[s] for s in range(N+1)),
            sum(pi[s]*u22[s] for s in range(N+1)))

checks=0

# 1. Mutation parameterization, stochasticity, stationary beta-binomial law,
# detailed balance, affine drift, and monotonicity.
for N in range(2,18):
    for a in (F(1,N*N), F(1,7), F(2,5)):
        mu=a/(F(N)+2*a)
        assert a == F(N)*mu/(1-2*mu)
        checks += 1
        pi=beta_binom(N,a)
        assert sum(pi,F(0)) == 1
        checks += 1
        K=Kmat(N,a)
        gamma=2*a/(F(N)*(F(N)+2*a))
        for j in range(N+1):
            assert sum(K[j],F(0)) == 1
            assert all(x>=0 for x in K[j])
            checks += 2
            mean=sum(F(t)*K[j][t] for t in range(N+1))
            assert mean == (1-gamma)*j + gamma*F(N,2)
            checks += 1
        for j in range(N+1):
            for l in range(N+1):
                assert pi[j]*K[j][l] == pi[l]*K[l][j]
                checks += 1
        # Adjacent-state monotonicity criterion for birth-death kernels.
        for j in range(N):
            pjp=transition(N,a,j)[2]
            pnextm=transition(N,a,j+1)[0]
            assert pjp + pnextm <= 1
            checks += 1

# 2. Exact beta-binomial predictive split identity and O(alpha) beta-kernel ratio.
for N in range(3,15):
    a=F(1,N*N)
    pi=beta_binom(N,a)
    for b in range(2,min(N,8)+1):
        for i in range(1,b):
            j=b-i
            lhs=sum(pi[s]*split_given_count(N,s,i,j) for s in range(N+1))
            rhs=2*rising(a,i)*rising(a,j)/rising(2*a,b)
            assert lhs==rhs
            checks += 1
            physical=rhs/a
            # Beta(i,j)=(i-1)!(j-1)!/(b-1)!
            from math import factorial
            B=F(factorial(i-1)*factorial(j-1),factorial(b-1))
            ratio=physical/B
            expected=F(1)
            for r in range(1,i):
                expected *= 1+a/F(r)
            for r in range(1,j):
                expected *= 1+a/F(r)
            for r in range(1,b):
                expected /= 1+2*a/F(r)
            assert ratio==expected
            checks += 1

# 3. Lipschitz coupling bound for every fixed split observable on a finite grid.
for N in range(3,15):
    for b in range(2,min(N,7)+1):
        for i in range(1,b):
            j=b-i
            for s in range(N):
                d=abs(split_given_count(N,s+1,i,j)-split_given_count(N,s,i,j))
                assert d <= F(b,N)
                checks += 1

# 4. Exact asymptotic scales for the chosen C021 parameters.
for N in (4,5,8,10,20,50):
    a=F(1,N*N)
    Delta=F(1,N**14)
    eps=Delta/a
    gamma=2*a/(F(N)*(F(N)+2*a))
    assert eps == F(1,N**12)
    assert gamma == F(2,N**4+2*N)
    # Martingale averaging, post-jump bias, and multiple-activation errors.
    avg_scale=Delta/(a*a*gamma*gamma)
    bias_scale=Delta/(a*gamma)
    remainder_scale=Delta/(a*a)
    assert avg_scale == F((N**4+2*N)**2,4*N**10)
    assert bias_scale == F(N**4+2*N,2*N**12)
    assert remainder_scale == F(1,N**10)
    checks += 6

# 5. Exact finite N=4 first-root shape witness for C021.
N=4
a=F(1,16)
mu=a/(F(N)+2*a)
Delta=F(1,N**14)
eps=Delta/a
assert mu==F(1,66)
assert Delta==F(1,268435456)
assert eps==F(1,16777216)
checks += 3
pi=beta_binom(N,a)
assert pi == [F(539,1200),F(11,300),F(17,600),F(11,300),F(539,1200)]
checks += 1
P13,P22=eventual_shape_N4(a,eps)
assert P13==F(55364815913,76755765225)
assert P22==F(21390949312,76755765225)
assert P13+P22==1
checks += 3
ratio=(P13/F(4))/(P22/F(3))
assert ratio==F(166094447739,85563797248)
checks += 1

old_binary={
    'original_CTCS':F(2,1),
    'C001':F(7,5),
    'C009':F(2699,1365),
    'C010':F(2273,1153),
    'C020':F(61381,43765),
}
for r in old_binary.values():
    assert ratio != r
    checks += 1

print(f'EXACT_CHECKS={checks}')
print(f'N4_alpha={a}')
print(f'N4_mu={mu}')
print(f'N4_Delta={Delta}')
print(f'N4_activation={eps}')
print('N4_stationary=' + ','.join(str(x) for x in pi))
print(f'N4_P_type_1_3={P13}')
print(f'N4_P_type_2_2={P22}')
print(f'N4_particular_ratio={ratio}')
for name,r in old_binary.items():
    print(f'ratio_minus_{name}={ratio-r}')
print('ALL_EXACT_CHECKS_PASS')
