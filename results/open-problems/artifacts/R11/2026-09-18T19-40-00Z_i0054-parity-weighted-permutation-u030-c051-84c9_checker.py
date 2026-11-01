from fractions import Fraction
from itertools import permutations
from math import factorial

A = Fraction(1, 2)
ASSERTIONS = 0

def ck(cond, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def theta(m):
    return Fraction(1,1) + (A if m % 2 == 0 else -A)

def cycles(p):
    n = len(p)
    seen = [False]*n
    out = []
    for i in range(n):
        if not seen[i]:
            j=i
            c=[]
            while not seen[j]:
                seen[j]=True
                c.append(j)
                j=p[j]
            out.append(c)
    return out

def brute_selected_law(n):
    Z = Fraction(0)
    mass = {m:Fraction(0) for m in range(1,n+1)}
    for p in permutations(range(n)):
        cs=cycles(p)
        w=Fraction(1)
        for c in cs:
            w *= theta(len(c))
        Z += w
        K=len(cs)
        for c in cs:
            mass[len(c)] += w/Fraction(K)
    return Z, {m:mass[m]/Z for m in mass}

def series_coeffs(N):
    # A(z)=sum c_m z^m, F=exp A, B=(F-1)/A.
    c=[Fraction(0)]*(N+2)
    for m in range(1,N+2):
        c[m]=theta(m)/m
    f=[Fraction(0)]*(N+2)
    f[0]=Fraction(1)
    # F' = A'F: n f_n = sum_{m=1}^n m c_m f_{n-m}
    for n in range(1,N+2):
        f[n]=sum(Fraction(m)*c[m]*f[n-m] for m in range(1,n+1))/n
    b=[Fraction(0)]*(N+1)
    b[0]=Fraction(1)
    # A*B=F-1; coefficient z^(r+1) determines b_r because c1 != 0.
    c1=c[1]
    for r in range(1,N+1):
        coeff=f[r+1]-sum(c[m]*b[r+1-m] for m in range(2,r+2))
        b[r]=coeff/c1
    return c,f,b

def formula_selected_law(n):
    c,f,b=series_coeffs(n)
    law={}
    for m in range(1,n+1):
        law[m]=c[m]*b[n-m]/f[n]
    return factorial(n)*f[n], law

def falling(x,r):
    z=1
    for t in range(r):
        z*=x-t
    return z

def split_prob(n,i,j,law):
    den=falling(n,i+j)
    out=Fraction(0)
    for m,pm in law.items():
        num=falling(m,i)*falling(n-m,j)+falling(m,j)*falling(n-m,i)
        out += pm*Fraction(num,den)
    return out

# positivity and parity weights
for m in range(1,101):
    ck(theta(m) > 0, f"theta positivity m={m}")
    ck(theta(m) == (Fraction(3,2) if m%2==0 else Fraction(1,2)), f"theta parity m={m}")

# exact brute-force selected-cycle formula through n=8
for n in range(1,9):
    Z1, law1 = brute_selected_law(n)
    Z2, law2 = formula_selected_law(n)
    ck(Z1 == Z2, f"partition function n={n}: {Z1} != {Z2}")
    ck(sum(law1.values(), Fraction(0)) == 1, f"brute normalization n={n}")
    ck(sum(law2.values(), Fraction(0)) == 1, f"formula normalization n={n}")
    for m in range(1,n+1):
        ck(law1[m] == law2[m], f"selected law n={n},m={m}")

# exact N=4 witness
Z4, L4 = formula_selected_law(4)
expected_law = {
    1: Fraction(41,321),
    2: Fraction(40,107),
    3: Fraction(16,321),
    4: Fraction(48,107),
}
ck(Z4 == Fraction(321,16), f"Z4={Z4}")
for m,v in expected_law.items():
    ck(L4[m] == v, f"N4 p{m}={L4[m]}")
P11=split_prob(4,1,1,L4)
P22=split_prob(4,2,2,L4)
P13=split_prob(4,1,3,L4)
ck(P11 == Fraction(217,642), f"P11={P11}")
ck(P22 == Fraction(40,321), f"P22={P22}")
ck(P13 == Fraction(19,428), f"P13={P13}")
ck(P22/P11 == Fraction(80,217), "ratio22")
ck(P13/P11 == Fraction(57,434), "ratio13")
ck(P22/P11 != Fraction(1,6), "finite model not CTCS under time rescaling")

# compare a=0 uniform-permutation-first/uniform-cycle finite law at N=4
def theta0(m): return Fraction(1)
def brute_selected_law_custom(n, th):
    Z=Fraction(0); mass={m:Fraction(0) for m in range(1,n+1)}
    for p in permutations(range(n)):
        cs=cycles(p); w=Fraction(1)
        for c in cs: w*=th(len(c))
        Z+=w
        for c in cs: mass[len(c)] += w/Fraction(len(cs))
    return Z,{m:mass[m]/Z for m in mass}
Z0,L0=brute_selected_law_custom(4,theta0)
U11=split_prob(4,1,1,L0); U22=split_prob(4,2,2,L0); U13=split_prob(4,1,3,L0)
ck((P22/P11,P13/P11)!=(U22/U11,U13/U11), "distinct from a=0 model")

# sharp boundary a=1: odd cycles have zero weight, so odd total sizes have zero partition function.
def theta_boundary(m):
    return Fraction(2) if m % 2 == 0 else Fraction(0)
def brute_partition_weight(n, th):
    Z=Fraction(0)
    for p in permutations(range(n)):
        cs=cycles(p); w=Fraction(1)
        for c in cs: w*=th(len(c))
        Z+=w
    return Z
for n in range(1,10,2):
    Zb = brute_partition_weight(n,theta_boundary)
    ck(Zb == 0, f"a=1 odd-size partition function n={n}: {Zb}")
for n in range(2,10,2):
    Zb = brute_partition_weight(n,theta_boundary)
    ck(Zb > 0, f"a=1 even-size partition function n={n}")

# beta decomposition identity: B(i,j+1)+B(j,i+1)=B(i,j)
def Beta(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))
for i in range(1,31):
    for j in range(1,31):
        ck(Beta(i,j+1)+Beta(j,i+1)==Beta(i,j), f"beta identity {i},{j}")

# CTCS total exit rate identity for specified split rates
# sum over unordered set splits = H_{b-1}
for b in range(2,31):
    total=Fraction(0)
    # sum over all nonempty proper subsets A, divide by 2 because A|Ac unordered
    for i in range(1,b):
        total += Fraction(factorial(b), factorial(i)*factorial(b-i)) * Beta(i,b-i) / 2
    H=sum((Fraction(1,r) for r in range(1,b)), Fraction(0))
    ck(total==H, f"exit rate b={b}")

print("R11 I0054 C051 parity-weighted permutation exact self-check")
print("FINITE CLAIMS ONLY; singularity transfer, endpoint estimates, and J1 convergence are proved in the written report.")
print(f"ASSERTIONS={ASSERTIONS}")
print(f"N4_partition_function={Z4}")
print("N4_selected_cycle_law=" + ",".join(f"{m}:{L4[m]}" for m in sorted(L4)))
print(f"N4_P11={P11}")
print(f"N4_P22={P22}")
print(f"N4_P13={P13}")
print(f"N4_ratio_P22_over_P11={P22/P11}")
print(f"N4_ratio_P13_over_P11={P13/P11}")
print(f"uniform_a0_ratios={U22/U11},{U13/U11}")
print("a1_boundary_odd_partition_functions_zero=PASS")
print("ALL_EXACT_CHECKS_PASS")
