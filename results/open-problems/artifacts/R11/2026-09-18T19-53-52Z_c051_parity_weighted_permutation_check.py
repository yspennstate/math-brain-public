#!/usr/bin/env python3
"""
R11 / I0054 / C051 exact self-check.

Exact finite checks for the parity-weighted permutation / uniform-cycle model
used in U030/C051.  All arithmetic is fractions.Fraction or integer arithmetic.
No floating-point calculation certifies any theorem-sized claim.

This checker verifies:
  * the parity cycle weights and mean-one condition;
  * the exact weighted-permutation EGF recurrence;
  * the closed coefficient formula
        F(z)=1/((1-z)*sqrt(1+z));
  * the reciprocal-cycle pointing identity
        p_{N,m}=(theta_m/m) b_{N-m}/f_N,
    with B(z)=(F(z)-1)/A(z);
  * exact normalization of the selected-cycle law;
  * independent brute-force weighted-permutation enumeration through N=8;
  * exchangeability/uniformity of selected supports conditional on size;
  * exact visible split probabilities against direct brute force;
  * the N=4 finite-law witness used to distinguish C051;
  * the beta identity B(i,j+1)+B(j,i+1)=B(i,j).
"""
from fractions import Fraction
from itertools import permutations, combinations
from math import comb, factorial

checks = 0
def check(cond, msg="assertion failed"):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1

def theta(m):
    return Fraction(3,2) if m % 2 == 0 else Fraction(1,2)

def c(m):
    return theta(m) / m

def falling(n, r):
    out = 1
    for j in range(r):
        out *= n-j
    return out

def beta_int(i,j):
    # i,j positive integers
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

# ---- exact mean-one periodic weights ----
check(theta(1) == Fraction(1,2))
check(theta(2) == Fraction(3,2))
check((theta(1)+theta(2))/2 == 1)
for m in range(1,501):
    check(theta(m+2) == theta(m))
    check(theta(m) > 0)

# ---- F coefficients from recurrence n f_n = sum theta_m f_{n-m} ----
NMAX = 140
f = [Fraction(0)]*(NMAX+2)
f[0] = Fraction(1)
for n in range(1,NMAX+2):
    f[n] = sum(theta(m)*f[n-m] for m in range(1,n+1))/n
    check(f[n] > 0)

# Closed coefficient formula from
# F(z)=(1-z)^(-1)(1+z)^(-1/2).
# [z^r](1+z)^(-1/2)=(-1)^r binom(2r,r)/4^r.
partial = Fraction(0)
for n in range(0,NMAX+2):
    partial += Fraction(((-1)**n)*comb(2*n,n), 4**n)
    check(f[n] == partial, f"closed F coefficient failed at n={n}")

# ---- B=(F-1)/A coefficients by exact formal division ----
# A(z)=sum_{m>=1} c_m z^m and A*B=F-1.
b = [Fraction(0)]*(NMAX+1)
b[0] = f[1]/c(1)
check(b[0] == 1)
for n in range(2,NMAX+2):
    known = sum(c(m)*b[n-m] for m in range(2,n+1))
    b[n-1] = (f[n]-known)/c(1)
    check(b[n-1] > 0)
    check(sum(c(m)*b[n-m] for m in range(1,n+1)) == f[n])

# selected cycle law p_{N,m}=c_m b_{N-m}/f_N
def p_formula(N,m):
    return c(m)*b[N-m]/f[N]

for N in range(1,NMAX+1):
    probs = [p_formula(N,m) for m in range(1,N+1)]
    check(all(x >= 0 for x in probs))
    check(sum(probs, Fraction(0)) == 1, f"p normalization N={N}")

# ---- brute-force weighted permutations ----
def cycle_supports(p):
    n=len(p)
    seen=[False]*n
    out=[]
    for i in range(n):
        if seen[i]:
            continue
        cur=[]
        j=i
        while not seen[j]:
            seen[j]=True
            cur.append(j)
            j=p[j]
        out.append(frozenset(cur))
    return out

def perm_weight(cycles):
    w=Fraction(1)
    for C in cycles:
        w *= theta(len(C))
    return w

def brute_selected_supports(N):
    Z=Fraction(0)
    size_mass={m:Fraction(0) for m in range(1,N+1)}
    support_mass={}
    for p in permutations(range(N)):
        cycs=cycle_supports(p)
        w=perm_weight(cycs)
        Z += w
        K=len(cycs)
        for C in cycs:
            q=w/Fraction(K)
            size_mass[len(C)] += q
            support_mass[C] = support_mass.get(C,Fraction(0))+q
    size_prob={m:x/Z for m,x in size_mass.items() if x}
    supp_prob={S:x/Z for S,x in support_mass.items() if x}
    return Z,size_prob,supp_prob

brute={}
for N in range(1,9):
    Z,p_size,p_supp = brute_selected_supports(N)
    brute[N]=(Z,p_size,p_supp)
    check(Z == factorial(N)*f[N], f"normalizer brute mismatch N={N}")
    for m in range(1,N+1):
        check(p_size.get(m,Fraction(0)) == p_formula(N,m),
              f"selected-size formula mismatch N={N},m={m}")
        # exchangeability: every m-subset has p_m/binom(N,m)
        target=p_formula(N,m)/comb(N,m)
        for S in combinations(range(N),m):
            check(p_supp.get(frozenset(S),Fraction(0)) == target,
                  f"support exchangeability failed N={N},m={m},S={S}")

# ---- visible split formula vs direct brute selected supports ----
def split_formula(N,i,j):
    den=falling(N,i+j)
    ans=Fraction(0)
    for m in range(1,N+1):
        num=(falling(m,i)*falling(N-m,j)
             +falling(m,j)*falling(N-m,i))
        ans += p_formula(N,m)*Fraction(num,den)
    return ans

def split_direct(N,i,j):
    _,_,p_supp=brute[N]
    bvis=i+j
    A=frozenset(range(i))
    C=frozenset(range(i,bvis))
    V=frozenset(range(bvis))
    ans=Fraction(0)
    for S,p in p_supp.items():
        inter=S & V
        if inter == A or inter == C:
            ans += p
    return ans

for N in range(2,8):
    for bvis in range(2,min(N,5)+1):
        for i in range(1,bvis):
            j=bvis-i
            check(split_direct(N,i,j)==split_formula(N,i,j),
                  f"direct split mismatch N={N},i={i},j={j}")

# ---- exact N=4 witness ----
N=4
p4={m:p_formula(4,m) for m in range(1,5)}
expected_p4={
    1:Fraction(41,321),
    2:Fraction(40,107),
    3:Fraction(16,321),
    4:Fraction(48,107),
}
check(p4==expected_p4)

P11=split_formula(4,1,1)
P22=split_formula(4,2,2)
P13=split_formula(4,1,3)
check(P11==Fraction(217,642))
check(P22==Fraction(40,321))
check(P13==Fraction(19,428))
R22=P22/P11
R13=P13/P11
check(R22==Fraction(80,217))
check(R13==Fraction(57,434))

# Compare to a few archived neighboring exact witnesses.
archived_pairs=[
    (Fraction(1,2),Fraction(0)),             # C050 derangement
    (Fraction(4,41),Fraction(33,82)),        # C049 uniform-polynomial-first
    (Fraction(5,61),Fraction(51,122)),       # C048 occurrence-Palm
    (Fraction(11,64),Fraction(21,64)),       # C044 midpoint quadrature
    (Fraction(1,6),Fraction(1,3)),           # C045 exact-on-[4]
]
for pair in archived_pairs:
    check((R22,R13) != pair)

# ---- beta telescoping identity used in limiting generator ----
for i in range(1,41):
    for j in range(1,41):
        check(beta_int(i,j+1)+beta_int(j,i+1)==beta_int(i,j))

print("R11 C051 parity-weighted-permutation exact self-check")
print(f"ASSERTIONS={checks}")
print("F4=",f[4])
print("B_coeffs_0_to_5=",",".join(str(x) for x in b[:6]))
print("selected_cycle_N4=",",".join(f"{m}:{p4[m]}" for m in range(1,5)))
print(f"P4_11={P11}")
print(f"P4_22={P22}")
print(f"P4_13={P13}")
print(f"ratio22={R22}")
print(f"ratio13={R13}")
print("secondary_root_exponent=1/2")
print("ALL_EXACT_CHECKS_PASS")
