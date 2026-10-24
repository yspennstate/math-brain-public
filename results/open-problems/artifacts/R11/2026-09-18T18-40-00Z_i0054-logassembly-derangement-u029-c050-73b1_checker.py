from fractions import Fraction
from math import factorial, comb
from itertools import permutations, combinations

ASSERTIONS = 0
def ck(cond, msg="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

# d[n][k] = number of derangements of [n] having exactly k cycles.
MAXN = 60
d = [[0]*(MAXN+1) for _ in range(MAXN+1)]
d[0][0] = 1
for n in range(1, MAXN+1):
    for k in range(1, n+1):
        s = 0
        for m in range(2, n+1):
            if n-m >= 0:
                # choose the other m-1 labels in the cycle containing 1,
                # and arrange that cycle: C(n-1,m-1)*(m-1)! = (n-1)!/(n-m)!
                coeff = factorial(n-1)//factorial(n-m)
                s += coeff * d[n-m][k-1]
        d[n][k] = s

def derangement_number(n):
    return factorial(n) * sum(Fraction((-1)**j, factorial(j)) for j in range(n+1))

D = [sum(d[n]) for n in range(MAXN+1)]
for n in range(MAXN+1):
    ck(D[n] == derangement_number(n), f"D recurrence mismatch n={n}")

# J_n = sum_k d_{n,k}/(k+1), exact reciprocal-cycle-count remainder weight.
J = [sum((Fraction(d[n][k], k+1) for k in range(MAXN+1)), Fraction(0))
     for n in range(MAXN+1)]

def p_selected_cycle(N,m):
    # Uniform derangement first; then uniform cycle.
    if m < 2 or m > N or D[N] == 0:
        return Fraction(0)
    return Fraction(comb(N,m)*factorial(m-1), D[N]) * J[N-m]

for N in range(2, MAXN+1):
    probs = [p_selected_cycle(N,m) for m in range(2,N+1)]
    ck(sum(probs, Fraction(0)) == 1, f"selected-cycle law not normalized N={N}")
    for p in probs:
        ck(p >= 0, "negative p")

# direct brute-force selected-cycle law for N <= 8
def cycles_of_perm(p):
    n=len(p)
    seen=[False]*n
    cyc=[]
    for i in range(n):
        if not seen[i]:
            c=[]
            j=i
            while not seen[j]:
                seen[j]=True
                c.append(j+1)
                j=p[j]-1
            cyc.append(tuple(c))
    return cyc

def brute_p(N):
    ders=[]
    for p in permutations(range(1,N+1)):
        if all(p[i] != i+1 for i in range(N)):
            ders.append(p)
    acc={m:Fraction(0) for m in range(2,N+1)}
    for p in ders:
        cs=cycles_of_perm(p)
        for c in cs:
            acc[len(c)] += Fraction(1, len(ders)*len(cs))
    return acc, len(ders)

for N in range(2,9):
    acc, count = brute_p(N)
    ck(count == D[N], f"brute derangement count N={N}")
    for m in range(2,N+1):
        ck(acc[m] == p_selected_cycle(N,m), f"brute p mismatch N={N},m={m}")

def falling(n,r):
    if r < 0 or r > n:
        return 0
    z=1
    for j in range(r):
        z *= n-j
    return z

def specified_split_prob_given_m(N,m,i,j):
    b=i+j
    if b > N:
        return Fraction(0)
    return Fraction(falling(m,i)*falling(N-m,j) + falling(m,j)*falling(N-m,i),
                    falling(N,b))

def proposal_rate(N,i,j):
    return sum((p_selected_cycle(N,m)*specified_split_prob_given_m(N,m,i,j)
                for m in range(2,N+1)), Fraction(0))

# Brute direct visible specified split probabilities for all N <= 8, b <= 5.
# Use A={1,...,i}, C={i+1,...,b}; event selected cycle intersects visible set
# in exactly A or exactly C.
def brute_proposal_rate(N,i,j):
    b=i+j
    A=set(range(1,i+1))
    C=set(range(i+1,b+1))
    ders=[]
    for p in permutations(range(1,N+1)):
        if all(p[t] != t+1 for t in range(N)):
            ders.append(p)
    ans=Fraction(0)
    for p in ders:
        cs=cycles_of_perm(p)
        for c in cs:
            S=set(c) & set(range(1,b+1))
            if S==A or S==C:
                ans += Fraction(1, len(ders)*len(cs))
    return ans

for N in range(2,9):
    for b in range(2,min(N,5)+1):
        for i in range(1,b):
            j=b-i
            ck(proposal_rate(N,i,j) == brute_proposal_rate(N,i,j),
               f"visible split mismatch N={N},i={i},j={j}")

# Exact N=4 witness.
ck(p_selected_cycle(4,2) == Fraction(1,3))
ck(p_selected_cycle(4,4) == Fraction(2,3))
p11 = proposal_rate(4,1,1)
p22 = proposal_rate(4,2,2)
p13 = proposal_rate(4,1,3)
ck(p11 == Fraction(2,9), f"p11={p11}")
ck(p22 == Fraction(1,9), f"p22={p22}")
ck(p13 == 0, f"p13={p13}")
ck(p22/p11 == Fraction(1,2))
ck(p13/p11 == 0)

# Compare explicitly with archived C049 N=4 invariant ratios.
c049_r22 = Fraction(4,41)
c049_r13 = Fraction(33,82)
ck(p22/p11 != c049_r22)
ck(p13/p11 != c049_r13)

# General theta obstruction: normalized balanced 2|2 rate.
# Q_theta(2,2)=(theta+1)/((theta+2)(theta+3));
# CTCS B(2,2)=1/6 iff theta=1 (theta>0).
for theta in range(1,501):
    q22 = Fraction(theta+1, (theta+2)*(theta+3))
    ck((q22 == Fraction(1,6)) == (theta == 1), f"theta obstruction {theta}")

# Exact beta identity at theta=1 for finite integer i,j range.
def beta_int(a,b):
    # B(a,b) for positive integers
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))

for i in range(1,31):
    for j in range(1,31):
        lhs = beta_int(i,j+1) + beta_int(j,i+1)
        rhs = beta_int(i,j)
        ck(lhs == rhs, f"beta identity i={i},j={j}")

# Exact total CTCS exit-rate identity for b through 35:
# 1/2 sum_i C(b,i) B(i,b-i) = H_{b-1}.
for b in range(2,36):
    total = Fraction(1,2)*sum((Fraction(comb(b,i))*beta_int(i,b-i)
                              for i in range(1,b)), Fraction(0))
    H = sum((Fraction(1,r) for r in range(1,b)), Fraction(0))
    ck(total == H, f"exit identity b={b}")

print("R11 I0054 C050 derangement/logarithmic-assembly exact self-check")
print("FINITE CLAIMS ONLY; asymptotic singularity-transfer and J1 convergence are proved in the written report.")
print(f"ASSERTIONS={ASSERTIONS}")
print(f"N4_selected_cycle_p2={p_selected_cycle(4,2)}")
print(f"N4_selected_cycle_p4={p_selected_cycle(4,4)}")
print(f"N4_P11={p11}")
print(f"N4_P22={p22}")
print(f"N4_P13={p13}")
print(f"N4_ratios=({p22/p11},{p13/p11})")
print("THETA_OBSTRUCTION=PASS integer theta 1..500; written proof solves theta(theta-1)=0 for all theta>0")
print("ALL_EXACT_CHECKS_PASS")
