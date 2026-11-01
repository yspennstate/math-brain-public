#!/usr/bin/env python3
from fractions import Fraction
from math import factorial

CHECKS = 0

def ck(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def fall(n, r):
    if r < 0:
        raise ValueError
    if r == 0:
        return 1
    if n < r:
        return 0
    out = 1
    for t in range(r):
        out *= n - t
    return out

def B_int(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def w(N,s):
    return Fraction(N, 2*s*(N-s))

def c(N,s):
    return Fraction(N*(N-1), 2*s*(N-s))

def h_support(N,s,i,j):
    b=i+j
    return Fraction(fall(s,i)*fall(N-s,j)+fall(s,j)*fall(N-s,i), fall(N,b))

def p_split(N,s,b):
    return Fraction(fall(N,b)-fall(s,b)-fall(N-s,b), fall(N,b))

# 1) Hypergeometric probabilities and exact harmonic/Vandermonde CTCS identity.
for N in range(4, 41):
    for b in range(2, min(N,10)+1):
        for s in range(1,N):
            ps = p_split(N,s,b)
            ck(Fraction(0) <= ps <= 1, f"invalid split prob N={N},s={s},b={b}")
            support_sum = Fraction(0)
            from math import comb
            for i in range(1,b):
                j=b-i
                if i>j:
                    continue
                mult = comb(b,i) if i<j else comb(b,i)//2
                support_sum += mult*h_support(N,s,i,j)
            ck(support_sum == ps, f"support sum mismatch N={N},s={s},b={b}")
            ck(c(N,s)*ps <= b, f"exit rate bound fails N={N},s={s},b={b}: {c(N,s)*ps}>{b}")

        for i in range(1,b):
            j=b-i
            q = sum((w(N,s)*h_support(N,s,i,j) for s in range(1,N)), Fraction(0))
            ck(q == B_int(i,j), f"exact CTCS rate fails N={N},i={i},j={j}: {q} != {B_int(i,j)}")
            lhs = sum(fall(s-1,i-1)*fall(N-s-1,j-1) for s in range(1,N))
            rhs = factorial(i-1)*factorial(j-1) * (fall(N-1,b-1)//factorial(b-1))
            ck(lhs == rhs, f"Vandermonde fails N={N},i={i},j={j}")

# 2) Activation probabilities for Delta_N = N^-2.
for N in range(3,501):
    D = Fraction(1,N*N)
    for s in range(1,N):
        a = D*c(N,s)
        ck(Fraction(0) < a < 1, f"activation invalid N={N},s={s},a={a}")

# 3) Cycle duration and exact averaged generator scaling.
for N in range(3,501):
    D=Fraction(1,N*N)
    tau=(N-1)*D
    ck(tau == Fraction(N-1,N*N), "tau formula")
    ck(N*D*D < tau*tau, f"raw error not o-cycle-squared at N={N}")

# 4) Exact N=4 root witness starting at rotor phase s=1.
N=4
D=Fraction(1,N*N)
a={s:D*c(N,s) for s in range(1,N)}
ck(a[1]==Fraction(1,8), f"a1 {a[1]}")
ck(a[2]==Fraction(3,32), f"a2 {a[2]}")
ck(a[3]==Fraction(1,8), f"a3 {a[3]}")
h1=a[1]
h2=(1-a[1])*a[2]
h3=(1-a[1])*(1-a[2])*a[3]
S=(1-a[1])*(1-a[2])*(1-a[3])
den=1-S
P13=(h1+h3)/den/Fraction(4,1)
P22=h2/den/Fraction(3,1)
ratio=P13/P22
ck(ratio==Fraction(459,224), f"finite witness ratio {ratio}")
ck(P13>0 and P22>0, "positive finite witness")

prior_binary = [
    Fraction(2,1),
    Fraction(7,5),
    Fraction(2699,1365),
    Fraction(2273,1153),
    Fraction(61381,43765),
    Fraction(166094447739,85563797248),
    Fraction(33,17),
    Fraction(5,3),
    Fraction(597,359),
    Fraction(18,11),
    Fraction(9,5),
    Fraction(5,4),
]
for q in prior_binary:
    ck(ratio != q, f"collision with prior binary witness {q}")

# 5) Exact per-phase N=4 support probabilities.
ck(h_support(4,1,1,3)==Fraction(1,4), "s1 1|3")
ck(h_support(4,2,1,3)==0, "s2 1|3")
ck(h_support(4,3,1,3)==Fraction(1,4), "s3 1|3")
ck(h_support(4,1,2,2)==0, "s1 2|2")
ck(h_support(4,2,2,2)==Fraction(1,3), "s2 2|2")
ck(h_support(4,3,2,2)==0, "s3 2|2")
ck(sum((w(4,s)*h_support(4,s,1,3) for s in range(1,4)),Fraction(0))==Fraction(1,3),"B13")
ck(sum((w(4,s)*h_support(4,s,2,2) for s in range(1,4)),Fraction(0))==Fraction(1,6),"B22")

print("R11 C029 deterministic hypergeometric-rotor exact self-check")
print(f"CHECKS={CHECKS}")
print("Model: Delta_N=N^-2; rotor phases s=1,...,N-1; exactly s occupied sites among N.")
print("At activation, block labels are uniformly injected without replacement into the N sites.")
print("Exact specified-support phase law:")
print("  h_N,s(i,j)=((s)_i (N-s)_j + (s)_j (N-s)_i)/(N)_(i+j).")
print("Harmonic weights w_N,s=N/[2s(N-s)], c_N,s=(N-1)w_N,s.")
print("Exact finite-N identity for every N>=i+j:")
print("  sum_s w_N,s h_N,s(i,j) = B(i,j).")
print("This is Chu/Vandermonde convolution in falling-factorial form; no Riemann approximation is used.")
print("Uniform visible first-order exit bound: c_N,s * P(nonmonochromatic b-sample) <= b.")
print("N=4 finite root witness, starting rotor phase 1:")
print(f"  activation=(1/8,3/32,1/8)")
print(f"  P(particular 1|3 first root)={P13}")
print(f"  P(particular 2|2 first root)={P22}")
print(f"  ratio={ratio} ~= {float(ratio):.12f}")
print("  ratio differs exactly from every retained binary witness through C028.")
print("ALL_EXACT_CHECKS_PASS")
