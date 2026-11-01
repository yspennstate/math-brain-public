#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb, isqrt

checks = 0

def rising(x, n):
    y = F(1)
    for r in range(n):
        y *= x + r
    return y

def falling_int(x, n):
    y = 1
    for r in range(n):
        y *= x-r
    return y

def beta_binom(N,a):
    den = rising(2*a,N)
    return [F(comb(N,j))*rising(a,j)*rising(a,N-j)/den for j in range(N+1)]

def predictive_direct(N,a,i,j):
    b=i+j
    den=falling_int(N,b)
    out=F(0)
    for s,ps in enumerate(beta_binom(N,a)):
        t=F(0)
        if s >= i and N-s >= j:
            t += F(falling_int(s,i)*falling_int(N-s,j),den)
        if s >= j and N-s >= i:
            t += F(falling_int(s,j)*falling_int(N-s,i),den)
        out += ps*t
    return out

def predictive_formula(a,i,j):
    return 2*rising(a,i)*rising(a,j)/rising(2*a,i+j)

# 1. Beta-binomial stationary predictive law and CTCS tangent.
for N in range(4,41):
    a=F(1,N*N)
    pi=beta_binom(N,a)
    assert sum(pi,F(0)) == 1
    checks += 1
    for b in range(2,min(N,9)+1):
        for i in range(1,b):
            j=b-i
            d=predictive_direct(N,a,i,j)
            f=predictive_formula(a,i,j)
            assert d==f
            checks += 1

            # Exact tangent ratio p_N / (alpha B(i,j)).
            B=F(1)
            # B(i,j)=(i-1)!(j-1)!/(b-1)!
            import math
            B=F(math.factorial(i-1)*math.factorial(j-1), math.factorial(b-1))
            ratio=f/(a*B)
            prod=F(1)
            for r in range(1,i):
                prod *= 1+a/F(r)
            for r in range(1,j):
                prod *= 1+a/F(r)
            for r in range(1,b):
                prod /= 1+2*a/F(r)
            assert ratio==prod
            checks += 1
            assert ratio > 0
            checks += 1

# 2. Exact CTCS(4) aggregate first-root balanced probability.
# particular rates B(1,3)=1/3, B(2,2)=1/6;
# there are 4 and 3 unordered supports respectively.
ctcs_13_total=4*F(1,3)
ctcs_22_total=3*F(1,6)
assert ctcs_22_total/(ctcs_13_total+ctcs_22_total)==F(3,11)
checks += 1

# 3. Unthinned one-locus Moran no-go finite inequalities.
# At k=1, a b=4 sample splits iff it contains the unique mutant: r=4/N.
# Count leaves k=1 with probability m=2(N-1)/N^2 per raw step.
for N in range(5,501):
    r=F(4,N)
    m=F(2*(N-1),N*N)
    before_exit = r/(r+(1-r)*m)
    assert before_exit >= F(2,3)
    checks += 1

# Green occupation identity E_1 L_k=N/k for mutation-free Moran
# via embedded SSRW expected visits * geometric holding time.
for N in range(5,301):
    for k in range(1,N):
        embedded_visits=F(2*(N-k),N)
        holding=F(N*N,2*k*(N-k))
        assert embedded_visits*holding==F(N,k)
        checks += 1

# Balanced-sample probability and explicit bound s22(k)<=48 k^2/N^2.
for N in range(5,121):
    den=comb(N,4)
    for k in range(1,N):
        s22=F(comb(k,2)*comb(N-k,2),den) if k>=2 and N-k>=2 else F(0)
        assert s22 <= F(48*k*k,N*N)
        checks += 1

# Localized union bound tends to zero with K=floor(N^(1/3)).
# Verify decreasing-to-small behavior on a geometric exact grid.
bounds=[]
for N in (10**3,10**4,10**5,10**6,10**7,10**8,10**9):
    K=max(2,int(round(N**(1/3))))
    # ensure K^3 near N but use an exact valid upper bound expression.
    bound=F(24*K*K,N)+F(1,K)
    bounds.append(bound)
    checks += 1
assert bounds[-1] < F(1,20)
checks += 1

# 4. C022 finite N=4 root-shape witness.
N=4
a=F(1,16)
p13=predictive_formula(a,1,3)
p22=predictive_formula(a,2,2)
assert p13==F(11,600)
assert p22==F(17,1800)
checks += 2
ratio=p13/p22
assert ratio==F(33,17)
checks += 1

old_binary={
    "original_CTCS":F(2,1),
    "C001":F(7,5),
    "C009":F(2699,1365),
    "C010":F(2273,1153),
    "C020":F(61381,43765),
    "C021":F(166094447739,85563797248),
}
for name,r in old_binary.items():
    assert ratio != r
    checks += 1

assert ratio-old_binary["C021"] == F(-17787,85563797248)
checks += 1

# 5. One-step rare-event scales for the fresh-locus model.
# For fixed k, each particular split is O(alpha), two visible blocks splitting
# in the same raw step is O(alpha^2). Check exact total split probabilities
# scale below a crude C_b alpha bound on a broad finite grid.
for N in range(8,101):
    a=F(1,N*N)
    for b in range(2,8):
        # sum each unordered support exactly once by fixing label 1 in A;
        # sum over i counts C(b-1,i-1), each particular split p(i,b-i).
        total=F(0)
        for i in range(1,b):
            total += F(comb(b-1,i-1))*predictive_formula(a,i,b-i)
        # CTCS total rate h_{b-1}; crude uniform bound 4 b alpha for alpha<=1.
        assert total <= 4*b*a
        checks += 1

print(f"EXACT_CHECKS={checks}")
print("NO_GO_CTCS4_BALANCED_CONDITIONAL=3/11")
print(f"UNTHINNED_BOUND_LAST={bounds[-1]}")
print(f"C022_N4_p13={p13}")
print(f"C022_N4_p22={p22}")
print(f"C022_N4_particular_ratio={ratio}")
for name,r in old_binary.items():
    print(f"ratio_minus_{name}={ratio-r}")
print("ALL_EXACT_CHECKS_PASS")
