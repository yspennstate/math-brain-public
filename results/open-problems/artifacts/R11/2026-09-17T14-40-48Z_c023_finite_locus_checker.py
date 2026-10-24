from fractions import Fraction
from math import comb, ceil

checks = 0

def rising(a, n):
    out = Fraction(1)
    for r in range(n):
        out *= a + r
    return out

def falling(n, r):
    out = 1
    for j in range(r):
        out *= n-j
    return out

def beta_int(i,j):
    # integer beta B(i,j) for positive integer arguments
    from math import factorial
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

def count_stationary(N, alpha):
    den = rising(2*alpha, N)
    return [Fraction(comb(N,s))*rising(alpha,s)*rising(alpha,N-s)/den for s in range(N+1)]

def config_weight(N, alpha, s):
    return rising(alpha,s)*rising(alpha,N-s)/rising(2*alpha,N)

def mu_of(N, alpha):
    return alpha/(N+2*alpha)

# 1. Exact fixed-victim detailed balance and count-law normalization over a grid.
for N in range(2, 21):
    for aden in range(2, 13):
        alpha = Fraction(1, aden)
        mu = mu_of(N, alpha)
        pis = count_stationary(N, alpha)
        assert sum(pis, Fraction()) == 1
        checks += 1
        for s in range(N):
            p_up = mu + (1-2*mu)*Fraction(s,N)
            p_dn = mu + (1-2*mu)*Fraction(N-s-1,N)
            assert p_up == Fraction(alpha+s, N+2*alpha)
            assert p_dn == Fraction(alpha+N-s-1, N+2*alpha)
            lhs = config_weight(N,alpha,s)*p_up
            rhs = config_weight(N,alpha,s+1)*p_dn
            assert lhs == rhs
            checks += 3

# 2. Predictive unordered split identity for fixed b and parameter grid.
for N in range(4, 21):
    for aden in range(2, 11):
        alpha = Fraction(1, aden)
        pis = count_stationary(N, alpha)
        for b in range(2, min(N,8)+1):
            den_sample = falling(N,b)
            for i in range(1,b):
                j=b-i
                ave = Fraction()
                for s,pis_s in enumerate(pis):
                    orient = Fraction(falling(s,i)*falling(N-s,j) + falling(s,j)*falling(N-s,i), den_sample)
                    ave += pis_s*orient
                closed = 2*rising(alpha,i)*rising(alpha,j)/rising(2*alpha,b)
                assert ave == closed
                checks += 1

# 3. Product-ratio identity p/(alpha B(i,j)).
for aden in range(2,31):
    alpha=Fraction(1,aden)
    for b in range(2,9):
        for i in range(1,b):
            j=b-i
            p=2*rising(alpha,i)*rising(alpha,j)/rising(2*alpha,b)
            ratio = p/(alpha*beta_int(i,j))
            prod = Fraction(1)
            for r in range(1,i):
                prod *= 1 + alpha/Fraction(r)
            for r in range(1,j):
                prod *= 1 + alpha/Fraction(r)
            for r in range(1,b):
                prod /= 1 + 2*alpha/Fraction(r)
            assert ratio == prod
            checks += 1

# 4. Finite-pool scale L_N Delta_N^2 for perfect fourth powers.
scale_rows=[]
for q in range(2,21):
    N=q**4
    m=q
    delta=Fraction(1,m)
    L=N
    val=L*delta*delta
    assert val == q*q
    scale_rows.append((N,delta,val))
    checks += 1

# 5. N=4 exact C023 witness.
N=4
m=2
alpha=Fraction(1,m)
delta=alpha
L=4
mu=mu_of(N,alpha)
assert mu == Fraction(1,10)
checks += 1
pis=count_stationary(N,alpha)
expected=[Fraction(35,128),Fraction(5,32),Fraction(9,64),Fraction(5,32),Fraction(35,128)]
assert pis == expected
checks += len(pis)

def p_split(i,j):
    return 2*rising(alpha,i)*rising(alpha,j)/rising(2*alpha,i+j)
p13=p_split(1,3)
p22=p_split(2,2)
assert p13 == Fraction(5,64)
assert p22 == Fraction(3,64)
ratio=p13/p22
assert ratio == Fraction(5,3)
checks += 3

# Prior retained binary-class exact witnesses from immutable R11 history.
prior = {
    "original_CTCS_finite": Fraction(2,1),
    "C001": Fraction(7,5),
    "C009": Fraction(2699,1365),
    "C010": Fraction(2273,1153),
    "C020": Fraction(61381,43765),
    "C021": Fraction(166094447739,85563797248),
    "C022": Fraction(33,17),
}
for name,r in prior.items():
    assert ratio != r
    checks += 1

# 6. Same-locus reuse witness for a two-label block at N=4.
def g_no_split(s):
    return Fraction(s*(s-1)+(N-s)*(N-s-1), N*(N-1))
q=sum((pis[s]*g_no_split(s) for s in range(N+1)), Fraction())
Eg2=sum((pis[s]*g_no_split(s)**2 for s in range(N+1)), Fraction())
var_g=Eg2-q*q
lam = 1-Fraction(4*alpha+2, N*(N+2*alpha))
assert q == Fraction(3,4)
assert var_g == Fraction(5,64)
assert lam == Fraction(4,5)
checks += 3

# Directly verify the centered no-split observable is a one-step eigenfunction
# for the ordinary Moran count kernel (uniform victim), which is the single-locus marginal.
def count_transition_row(s):
    mu=mu_of(N,alpha)
    parent_one = mu + (1-2*mu)*Fraction(s,N)
    up = Fraction(N-s,N)*parent_one
    down = Fraction(s,N)*(1-parent_one)
    stay=1-up-down
    return down,stay,up

for s in range(N+1):
    down,stay,up=count_transition_row(s)
    lhs=stay*(g_no_split(s)-q)
    if s>0: lhs += down*(g_no_split(s-1)-q)
    if s<N: lhs += up*(g_no_split(s+1)-q)
    assert lhs == lam*(g_no_split(s)-q)
    checks += 1

p_no2 = q*q + Fraction(1,L)*lam*var_g
xi = p_no2/(q*q)
assert p_no2 == Fraction(37,64)
assert xi == Fraction(37,36)
checks += 2

print("claim=R11-I0054-C023")
print("checker=self-check exact rational arithmetic")
print(f"checks={checks}")
print(f"N4_alpha={alpha}")
print("N4_stationary_counts="+",".join(str(x) for x in pis))
print(f"N4_two_label_q={q}")
print(f"N4_var_g={var_g}")
print(f"N4_lambda2={lam}")
print(f"N4_P_no_split_first_two={p_no2}")
print(f"N4_survival_ratio_Xi={xi}")
print(f"N4_p_1|3={p13}")
print(f"N4_p_2|2={p22}")
print(f"N4_support_ratio={ratio}")
for name,r in prior.items():
    print(f"N4_ratio_minus_{name}={ratio-r}")
print("scale_fourth_powers="+";".join(f"{N}:{d}:{v}" for N,d,v in scale_rows))
print("ALL_EXACT_CHECKS_PASS")
