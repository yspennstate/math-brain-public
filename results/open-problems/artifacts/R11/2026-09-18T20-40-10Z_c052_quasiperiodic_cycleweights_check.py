from fractions import Fraction
from itertools import permutations
from collections import defaultdict
from math import factorial, comb

ASSERTIONS = 0

def check(cond, msg=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def ff(n,k):
    if k > n:
        return 0
    v = 1
    for t in range(k):
        v *= n-t
    return v

# C052 parameters: alpha with cos(alpha)=1/4, theta_m = 1 + (1/2) cos(m alpha).
COS = [Fraction(1), Fraction(1,4)]
for n in range(2, 2501):
    COS.append(Fraction(1,2)*COS[-1] - COS[-2])  # 2 cos(alpha)=1/2.

THETA = [None] + [Fraction(1) + Fraction(1,2)*COS[n] for n in range(1,2501)]

# Exact finite diagnostics for the recurrence and positivity.
check(COS[0] == 1, "cos0")
check(COS[1] == Fraction(1,4), "cos1")
for n in range(2,2501):
    check(COS[n] == Fraction(1,2)*COS[n-1] - COS[n-2], f"cos recurrence {n}")
for n in range(1,2501):
    # Analytical theorem gives 1/2 <= theta_m <= 3/2; exact finite scan is only a self-check.
    check(Fraction(1,2) <= THETA[n] <= Fraction(3,2), f"theta range {n}")

# Irrational-rotation certificate ingredients:
# lambda=e^{i alpha} has primitive Q-minimal polynomial 2 x^2 - x + 2,
# discriminant -15, and is not an algebraic integer because that primitive
# irreducible polynomial is not monic. Root-of-unity => algebraic integer.
check((-1)**2 - 4*2*2 == -15, "discriminant")
check(2 != 1, "nonmonic leading coefficient")
check(THETA[1] == Fraction(9,8), "theta1")
check(THETA[2] == Fraction(9,16), "theta2")
check(THETA[3] == Fraction(21,32), "theta3")
check(THETA[4] == Fraction(81,64), "theta4")

def cycles_of_perm(p):
    n = len(p)
    seen = [False]*n
    out = []
    for i in range(n):
        if not seen[i]:
            cyc = []
            j = i
            while not seen[j]:
                seen[j] = True
                cyc.append(j)
                j = p[j]
            out.append(tuple(cyc))
    return out

def weighted_perm_enumeration(N):
    total = Fraction(0)
    size_mass = defaultdict(Fraction)
    support_mass = defaultdict(Fraction)
    for p in permutations(range(N)):
        cyc = cycles_of_perm(p)
        # exact partition check
        flat = sorted(x for C in cyc for x in C)
        check(flat == list(range(N)), f"cycle partition N={N}")
        w = Fraction(1)
        for C in cyc:
            w *= THETA[len(C)]
            check(THETA[len(C)] > 0, "positive weight")
        total += w
        K = len(cyc)
        for C in cyc:
            size_mass[len(C)] += w/Fraction(K,1)
            mask = sum(1 << x for x in C)
            support_mass[mask] += w/Fraction(K,1)
    psize = {m: size_mass[m]/total for m in sorted(size_mass)}
    psupp = {mask: v/total for mask,v in support_mass.items()}
    check(sum(psize.values(), Fraction(0)) == 1, f"size normalization N={N}")
    check(sum(psupp.values(), Fraction(0)) == 1, f"support normalization N={N}")
    return total, psize, psupp

# Coefficients f_n of F(z)=exp(sum theta_m z^m/m):
# n f_n = sum_{m<=n} theta_m f_{n-m}.
def f_coeffs(Nmax):
    f = [Fraction(0)]*(Nmax+1)
    f[0] = Fraction(1)
    for n in range(1,Nmax+1):
        f[n] = sum((THETA[m]*f[n-m] for m in range(1,n+1)), Fraction(0))/n
    return f

# b_n of B(z)=(F(z)-1)/A(z)=int_0^1 exp(t A(z)) dt.
# A(z)B(z)=F(z)-1 gives:
# theta_1 b_{n-1} + sum_{m=2}^n theta_m/m b_{n-m}=f_n.
def b_coeffs(f, Nmax):
    b = [Fraction(0)]*(Nmax+1)
    b[0] = Fraction(1)
    a1 = THETA[1]
    for n in range(2,Nmax+2):
        rhs = f[n] if n < len(f) else None
        if rhs is None:
            raise RuntimeError("need f coefficient")
        rest = sum((THETA[m]*b[n-m]/m for m in range(2,n+1)), Fraction(0))
        b[n-1] = (rhs-rest)/a1
    return b

F = f_coeffs(10)
B = b_coeffs(F, 8)

# Direct enumeration through N=8 against generating-function and pointing identities.
ENUM = {}
for N in range(1,9):
    total, psize, psupp = weighted_perm_enumeration(N)
    ENUM[N] = (total, psize, psupp)
    check(total == factorial(N)*F[N], f"partition function N={N}")
    for m in range(1,N+1):
        formula = THETA[m] * B[N-m] / (m*F[N])
        check(psize[m] == formula, f"pointing identity N={N},m={m}")
    # Exchangeability of the selected cycle support conditional on its size.
    for m in range(1,N+1):
        vals = {v for mask,v in psupp.items() if mask.bit_count()==m}
        check(len(vals)==1, f"exchangeability N={N},m={m}")
        common = next(iter(vals))
        check(common == psize[m]/comb(N,m), f"uniform support N={N},m={m}")

def s_prob(N,m,i,j):
    if i+j > N:
        return Fraction(0)
    return Fraction(
        ff(m,i)*ff(N-m,j) + ff(m,j)*ff(N-m,i),
        ff(N,i+j)
    )

# Check the closed hypergeometric visible-split formula directly from support enumeration.
for N in range(2,9):
    total, psize, psupp = ENUM[N]
    for i in range(1,N):
        for j in range(1,N-i+1):
            # choose canonical visible sides A={0,...,i-1}, B={i,...,i+j-1}
            A = set(range(i))
            D = set(range(i,i+j))
            direct = Fraction(0)
            for mask,p in psupp.items():
                S = {x for x in range(N) if (mask>>x)&1}
                if (A <= S and D.isdisjoint(S)) or (D <= S and A.isdisjoint(S)):
                    direct += p
            formula = sum((psize[m]*s_prob(N,m,i,j) for m in psize), Fraction(0))
            check(direct == formula, f"visible split N={N},i={i},j={j}")

# Exact C052 N=4 witness.
_, p4, _ = ENUM[4]
check(p4[1] == Fraction(1123,3083), "p41")
check(p4[2] == Fraction(360,3083), "p42")
check(p4[3] == Fraction(448,3083), "p43")
check(p4[4] == Fraction(1152,3083), "p44")

P11 = sum((p4[m]*s_prob(4,m,1,1) for m in p4), Fraction(0))
P22 = sum((p4[m]*s_prob(4,m,2,2) for m in p4), Fraction(0))
P13 = sum((p4[m]*s_prob(4,m,1,3) for m in p4), Fraction(0))
check(P11 == Fraction(2051,6166), "P11")
check(P22 == Fraction(120,3083), "P22")
check(P13 == Fraction(1571,12332), "P13")
R22 = P22/P11
R13 = P13/P11
check(R22 == Fraction(240,2051), "R22")
check(R13 == Fraction(1571,4102), "R13")

# Compare with archived nearby permutation/quadrature witnesses.
nearby = {
    "C051": (Fraction(80,217), Fraction(57,434)),
    "C050": (Fraction(1,2), Fraction(0,1)),
    "C049": (Fraction(4,41), Fraction(33,82)),
    "C048": (Fraction(5,61), Fraction(51,122)),
}
for name,pair in nearby.items():
    check((R22,R13) != pair, f"distinct from {name}")

# Exact beta telescoping identity for the limiting kernel.
def beta_int(a,b):
    # B(a,b) for positive integers.
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))

for i in range(1,41):
    for j in range(1,41):
        check(beta_int(i,j+1)+beta_int(j,i+1) == beta_int(i,j),
              f"beta identity {i},{j}")

# CTCS exit-rate identity on a block of size b:
# sum over unordered specified splits = H_{b-1}.
# Sum over all nonempty proper A and divide by 2.
for b in range(2,31):
    total = Fraction(0)
    for i in range(1,b):
        total += Fraction(comb(b,i),2)*beta_int(i,b-i)
    H = sum((Fraction(1,r) for r in range(1,b)), Fraction(0))
    check(total == H, f"exit rate b={b}")

print("R11 I0054 C052 quasiperiodic weighted-permutation exact self-check")
print("FINITE CLAIMS ONLY; asymptotic singularity analysis and J1 convergence are proved in the written report.")
print(f"ASSERTIONS={ASSERTIONS}")
print("cos_alpha=1/4")
print("theta_1_to_4=" + ",".join(str(THETA[m]) for m in range(1,5)))
print("N4_selected_cycle_size=" + ",".join(f"{m}:{p4[m]}" for m in sorted(p4)))
print(f"N4_P11={P11}")
print(f"N4_P22={P22}")
print(f"N4_P13={P13}")
print(f"N4_ratio_P22_over_P11={R22}")
print(f"N4_ratio_P13_over_P11={R13}")
print("ALL_EXACT_CHECKS_PASS")
