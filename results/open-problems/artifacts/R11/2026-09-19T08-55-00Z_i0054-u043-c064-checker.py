from fractions import Fraction
from itertools import permutations

ASSERTIONS = 0

def ck(cond, msg='assertion failed'):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def fall(n,r):
    if r < 0 or r > n:
        return 0
    z=1
    for a in range(r):
        z *= n-a
    return z

def math_factorial(n):
    z=1
    for r in range(2,n+1):
        z*=r
    return z

def beta_int(i,j):
    return Fraction(math_factorial(i-1)*math_factorial(j-1), math_factorial(i+j-1))

def weight(N,s,eps=Fraction(1,2)):
    return Fraction(1,1) + eps*((-1)**s)

def sym_weight(N,s,eps=Fraction(1,2)):
    return (weight(N,s,eps)+weight(N,N-s,eps))/2

def intensity(N,s,eps=Fraction(1,2)):
    return Fraction(N,2*s*(N-s))*weight(N,s,eps)

def split_prob_type(N,s,i,j):
    k=i+j
    return Fraction(fall(s,i)*fall(N-s,j)+fall(s,j)*fall(N-s,i), fall(N,k))

def rate_direct(N,i,j,eps=Fraction(1,2)):
    return sum((intensity(N,s,eps)*split_prob_type(N,s,i,j) for s in range(1,N)), Fraction())

def rate_sym_formula(N,i,j,eps=Fraction(1,2)):
    k=i+j
    return Fraction(N,fall(N,k))*sum((sym_weight(N,s,eps)*fall(s-1,i-1)*fall(N-s-1,j-1) for s in range(1,N)), Fraction())

def rate_base(N,i,j):
    k=i+j
    return Fraction(N,fall(N,k))*sum((Fraction(fall(s-1,i-1)*fall(N-s-1,j-1),1) for s in range(1,N)), Fraction())

def parity_discrepancy(N):
    eps=Fraction(1,2)
    vals=[]
    H=Fraction(0)
    for s in range(1,N):
        h=sym_weight(N,s,eps)-1
        H += h
        vals.append(abs(H))
    return max(vals,default=Fraction())

# Positivity and symmetrization identity.
for N in range(2,101):
    for s in range(1,N):
        ck(weight(N,s)>0)
        ck(intensity(N,s)>0)
        ck(sym_weight(N,s)==sym_weight(N,N-s))
        if N%2:
            ck(sym_weight(N,s)==1)
        else:
            ck(sym_weight(N,s)==1+Fraction(1,2)*((-1)**s))

# Marginal of a uniform injection does not depend on hidden block size.
for N in range(2,41):
    for b in range(1,N+1):
        for k in range(1,b+1):
            lhs=Fraction(fall(N-k,b-k), fall(N,b))
            rhs=Fraction(1, fall(N,k))
            ck(lhs==rhs, (N,b,k,lhs,rhs))

# Direct vs symmetrized rate formula and exact baseline Vandermonde identity.
for N in range(2,81):
    for k in range(2,min(N,12)+1):
        for i in range(1,k):
            j=k-i
            qd=rate_direct(N,i,j)
            qs=rate_sym_formula(N,i,j)
            ck(qd==qs, ('sym',N,i,j,qd,qs))
            qb=rate_base(N,i,j)
            B=beta_int(i,j)
            ck(qb==B, ('vandermonde',N,i,j,qb,B))
            if N%2:
                ck(qd==B, ('odd exact',N,i,j,qd,B))

# Explicit discrepancy bound from Abel summation for N >= 2k.
eps=Fraction(1,2)
for N in range(4,201):
    D=parity_discrepancy(N)
    ck(D <= eps)
    for k in range(2,min(10,N//2)+1):
        bound=Fraction((k-1)*(2**k),1)*D/Fraction(N,1)
        for i in range(1,k):
            j=k-i
            err=abs(rate_direct(N,i,j)-beta_int(i,j))
            ck(err <= bound, ('bound',N,i,j,err,bound,D))

# Direct injection+arc enumeration for small N and specified labeled splits.
# Labels are 0..k-1; target split is first i vs last j, unordered.
for N in range(2,8):
    for k in range(2,min(N,5)+1):
        inj=list(permutations(range(N),k))
        den=len(inj)*N
        for s in range(1,N):
            for i in range(1,k):
                j=k-i
                good=0
                for phi in inj:
                    for R in range(N):
                        arc={(R+d)%N for d in range(s)}
                        bits=[phi[t] in arc for t in range(k)]
                        orient=all(bits[t] for t in range(i)) and all(not bits[t] for t in range(i,k))
                        rev=all(not bits[t] for t in range(i)) and all(bits[t] for t in range(i,k))
                        if orient or rev:
                            good += 1
                p=Fraction(good,den)
                pf=split_prob_type(N,s,i,j)
                ck(p==pf, ('enum',N,k,s,i,j,p,pf))

# N=4 exact finite witness.
N=4
q11=rate_direct(N,1,1)
q13=rate_direct(N,1,3)
q22=rate_direct(N,2,2)
root_total=4*q13+3*q22
root_bal=3*q22/root_total
ck(q11==Fraction(5,6),q11)
ck(q13==Fraction(1,6),q13)
ck(q22==Fraction(1,4),q22)
ck(root_total==Fraction(17,12),root_total)
ck(root_bal==Fraction(9,17),root_bal)
ck(root_bal!=Fraction(3,11))
# Pair-normalized witness survives global time rescaling.
ck(q13/q11==Fraction(1,5))
ck(q22/q11==Fraction(3,10))

# Finite-state target samples: errors shrink and odd N are exact.
for N in [11,20,21,40,41,80,81,160]:
    for i,j in [(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]:
        if i+j<=N:
            q=rate_direct(N,i,j)
            B=beta_int(i,j)
            if N%2:
                ck(q==B)
            else:
                ck(abs(q-B) <= Fraction((i+j-1)*(2**(i+j)),1)*eps/Fraction(N,1))

print('R11-I0054-U043/C064 exact self-check')
print('assertions =',ASSERTIONS)
print('N4_q11 =',q11)
print('N4_q13 =',q13)
print('N4_q22 =',q22)
print('N4_root_total =',root_total)
print('N4_root_P_2v2 =',root_bal)
print('source_root_P_2v2 = 3/11')
print('pair_normalized_witness =',q13/q11,q22/q11)
for N in [8,9,20,21,100,101]:
    vals=[]
    for i,j in [(1,1),(1,3),(2,2),(2,3)]:
        if i+j<=N:
            vals.append(f'{i},{j}:{rate_direct(N,i,j)}')
    print('N',N,'Delta',parity_discrepancy(N),'rates',' '.join(vals))
print('ALL_EXACT_CHECKS_PASS')
