from fractions import Fraction

checks = 0

def A(cond, msg=""):
    global checks
    checks += 1
    assert cond, msg

def harmonic(n):
    return sum(Fraction(1, j) for j in range(1, n + 1))

def lam(N, s):
    return Fraction(N, 2 * s * (N - s))

def active_indices(N):
    # exact condition 1/2 <= s/N < 4/5
    return [s for s in range(1, N) if 2 * s >= N and 5 * s < 4 * N]

# 1. Harmonic total-rate identity and active-rate sanity checks.
for N in range(3, 80):
    total = sum(lam(N, s) for s in range(1, N))
    A(total == harmonic(N - 1), (N, total, harmonic(N - 1)))
    inds = active_indices(N)
    W = sum(lam(N, s) for s in inds)
    A(W > 0)
    A(W < Fraction(2, 1))
    q = W / total
    A(Fraction(0) < q < 1)

# 2. Geometric waiting time modulo d.  The theorem uses
#    mu(r)=q(1-q)^(r-1)/(1-(1-q)^d), r=1,...,d,
#    and TV(mu,Unif)<=qd/2 whenever qd<=1.
for d in range(2, 25):
    for den in range(2 * d, 8 * d + 1):
        q = Fraction(1, den)
        z = q * d
        A(z <= 1)
        a = 1 - q
        probs = [q * (a ** (r - 1)) / (1 - a ** d) for r in range(1, d + 1)]
        A(sum(probs) == 1)
        u = Fraction(1, d)
        tv = sum(abs(p - u) for p in probs) / 2
        A(tv <= z / 2, (d, den, tv, z / 2))
        for p in probs:
            ratio = p / u
            A(ratio >= 1 - z)
            A(ratio <= Fraction(1, 1) / (1 - z / 2))

# 3. Exact N=4 C091 finite witness by direct Bernoulli-mask enumeration.
# Mark probabilities are lambda_s/H_3 = (4,3,4)/11.
weights = {1: Fraction(4, 11), 2: Fraction(3, 11), 3: Fraction(4, 11)}
A(sum(weights.values()) == 1)

def bias_after_phase(s, phase):
    # d_4=2, b_4=1, rotor increments before applying the active bias.
    # s=1 lies outside the active interval and remains the source bias 1/4.
    if s == 1:
        return Fraction(1, 4)
    if s == 2:
        return Fraction(2, 3) if phase == 1 else Fraction(1, 2)
    if s == 3:
        return Fraction(3, 5) if phase == 1 else Fraction(3, 4)
    raise ValueError

def mask_type_probs(p):
    bal = Fraction(0)
    unb = Fraction(0)
    null = Fraction(0)
    for mask in range(16):
        r = mask.bit_count()
        prob = (p ** r) * ((1 - p) ** (4 - r))
        if r in (0, 4):
            null += prob
        elif r == 2:
            bal += prob
        else:
            unb += prob
    A(bal + unb + null == 1)
    return bal, unb, null

phase_data = {}
for before in (0, 1):
    after = 1 - before
    bal_tot = unb_tot = null_tot = Fraction(0)
    for s, w in weights.items():
        b, u, n = mask_type_probs(bias_after_phase(s, after))
        bal_tot += w * b
        unb_tot += w * u
        null_tot += w * n
    A(bal_tot + unb_tot + null_tot == 1)
    phase_data[before] = (bal_tot, unb_tot, null_tot)

a0, u0, n0 = phase_data[0]
a1, u1, n1 = phase_data[1]
A(a0 == Fraction(560707, 1980000))
A(n0 == Fraction(1367107, 5940000))
A(u0 == Fraction(722693, 1485000))
A(a1 == Fraction(45, 176))
A(n1 == Fraction(47, 176))
A(u1 == Fraction(21, 44))
A(n0 * n1 < 1)

# Eventual balanced absorption probabilities satisfy
# B0=a0+n0 B1, B1=a1+n1 B0.
B0 = (a0 + n0 * a1) / (1 - n0 * n1)
B1 = a1 + n1 * B0
A(B0 == Fraction(357573111, 981185971))
A(B1 == a1 + n1 * B0)
A(B0 != Fraction(3, 11))
A(B0 - Fraction(3, 11) == Fraction(989746308, 10793045681))
C090 = Fraction(3200871, 8926643)
A(B0 != C090)
A(B0 - C090 == Fraction(51277788115632, 8758696879725353))

print("R11 U075/C091 proposal-count rotor exact self-check")
print("CHECKS=", checks)
print("N4_phase0_balanced_one_step=", a0)
print("N4_phase0_null=", n0)
print("N4_phase1_balanced_one_step=", a1)
print("N4_phase1_null=", n1)
print("P_C091_balanced_root=", B0)
print("P_CTCS_balanced_root=", Fraction(3, 11))
print("difference_from_CTCS=", B0 - Fraction(3, 11))
print("P_C090_balanced_root=", C090)
print("difference_from_C090=", B0 - C090)
print("STATUS=ALL_EXACT_CHECKS_PASS")
