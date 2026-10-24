from fractions import Fraction as F
from math import factorial
from itertools import permutations, combinations

# HARD7-03 exact full-centre-pair winner-decomposition certificate.
# This checks the complete conditional centre pair at theta=723/1250,
# integrates all six first-layer order cones exactly, subtracts only the
# increment not already present in the 20260919T1623Z checkpoint, and
# certifies an improved shape/plateau rational.

theta = F(723, 1250)
q = F(1) - theta
a = F(2) - theta
assert F(0) < theta < F(1)
assert q > 0 and a > 0

# Ordered first-layer values: low=u, mid=u+v, high=u+v+w.
LOW = (F(1), F(0), F(0))
MID = (F(1), F(1), F(0))
HIGH = (F(1), F(1), F(1))
ORDER_VECS = (LOW, MID, HIGH)

def vadd(*vs):
    if not vs:
        return (F(0), F(0), F(0))
    return tuple(sum((v[i] for v in vs), F(0)) for i in range(3))

def vscale(c, v):
    return tuple(c*x for x in v)

def subsets(items):
    for k in range(len(items)+1):
        for S in combinations(items, k):
            yield S

def cone_integral(coef, exponent):
    # Multiply by first-layer density exp(-3u-2v-w).
    rates = (F(3)-exponent[0], F(2)-exponent[1], F(1)-exponent[2])
    assert all(r > 0 for r in rates)
    return coef/(rates[0]*rates[1]*rates[2])

def W_terms(i, shifts, universe):
    # E[e^{theta Y_i}; Y_i is maximum] for independent shifted Exp(1)'s.
    # D has the largest shift s_D, so all winner integrals start at s_D.
    sD = shifts["D"]
    others = [j for j in universe if j != i]
    out = []
    for S in subsets(others):
        k = len(S)
        coef = F((-1)**k, 1)/(q+k)
        exponent = vadd(
            shifts[i],
            *(shifts[j] for j in S),
            vscale(-(q+k), sD),
        )
        out.append((coef, exponent))
    return out

def R_terms(i, shifts, universe):
    # E[e^{-q M_i}], M_i=max_{j != i}Y_j, for outer i in {X,Z}.
    # M_i includes D and hence has support starting at s_D.
    sD = shifts["D"]
    others = [j for j in universe if j != i]
    out = []
    for S in subsets(others):
        k = len(S)
        coef = q*F((-1)**k, 1)/(q+k)
        exponent = vadd(
            *(shifts[j] for j in S),
            vscale(-(q+k), sD),
        )
        out.append((coef, exponent))
    return out

# Exact conditional winner formula:
# P_ctr(A)=2/a(W_C+W_D)+(4-theta)/a^2(e^{sX}R_X+e^{sZ}R_Z).
outer_coef = (F(4)-theta)/(a*a)

labels = ("Am", "A0", "A1")
universe = ("X", "Z", "C", "D")
cone_rows = []
P_total = F(0)
Q_total = F(0)

for perm in permutations(labels):
    rank = {lab: r for r, lab in enumerate(perm)}
    avec = {perm[r]: ORDER_VECS[r] for r in range(3)}

    sX = avec["Am"]
    sC = avec["Am"] if rank["Am"] > rank["A0"] else avec["A0"]
    sD = HIGH
    sZ = avec["A0"] if rank["A0"] > rank["A1"] else avec["A1"]
    shifts = {"X": sX, "C": sC, "D": sD, "Z": sZ}

    P_terms = []
    for i in ("C", "D"):
        for coef, exponent in W_terms(i, shifts, universe):
            P_terms.append((F(2)/a*coef, exponent))
    for i in ("X", "Z"):
        for coef, exponent in R_terms(i, shifts, universe):
            P_terms.append((outer_coef*coef, vadd(shifts[i], exponent)))

    # Old common-window centre bound Q_ctr(A)=2/a E exp(theta max(Y_C,Y_D)).
    Q_terms = []
    for i in ("C", "D"):
        for coef, exponent in W_terms(i, shifts, ("C", "D")):
            Q_terms.append((F(2)/a*coef, exponent))

    P_cone = sum((cone_integral(c,e) for c,e in P_terms), F(0))
    Q_cone = sum((cone_integral(c,e) for c,e in Q_terms), F(0))
    gain_cone = P_cone - Q_cone
    assert gain_cone > 0

    cone_rows.append((perm, P_cone, Q_cone, gain_cone))
    P_total += P_cone
    Q_total += Q_cone

delta_full = P_total - Q_total
assert delta_full > 0

# Closed exact totals from the six-cone sum.
P_expected = F(
    11253444786300730080604553222656250000000,
    589014585036522512566911293259319803207,
)
Q_expected = F(
    50552368164062500000000,
    2794229721911833952401,
)
delta_expected = F(
    1133148258990652534484863281250000000,
    1117674734414653724035884806943680841,
)
assert P_total == P_expected
assert Q_total == Q_expected
assert delta_full == delta_expected

# Gain per centre pair already incorporated in the 20260919T1623Z current bound.
delta_prev = F(
    7354736328125000000000,
    16049588934017308109901,
)
assert delta_full > delta_prev
delta_increment = delta_full - delta_prev
DeltaC_increment = F(4)*delta_increment
assert DeltaC_increment > 0

# Immutable current four-step value after the previous two-cone correction.
U4_prev = F(
    462207595847970865379094425847318588877127242915039062500000,
    533551258662847599879934006185557225047638076531060575909,
)
U4_new = U4_prev - DeltaC_increment/q
U4_expected = F(
    21591569424418754612288415153750985225648747506850585937500000,
    25076909157153837194356898290721189577238989596959847067723,
)
assert U4_new == U4_expected
assert U4_new < U4_prev

# Exact Chernoff certificate.
A_prev = F(292367491, 100000000)
A_new = F(29210369, 10000000)
assert A_new < A_prev
x = F(4)*theta*A_new
S32 = sum(x**k / F(factorial(k)) for k in range(33))
margin = S32 - U4_new
assert margin > 0

L_prev = F(1)/(F(4)*A_prev)
L_new = F(1)/(F(4)*A_new)
assert L_prev == F(25000000, 292367491)
assert L_new == F(2500000, 29210369)
assert L_new > L_prev

print("HARD7-03 exact full-centre-pair winner-decomposition certificate")
print(f"theta = {theta}")
print(f"q = {q}")
print(f"a = {a}")
print(f"outer_coef = {outer_coef}")
for perm, P_cone, Q_cone, gain_cone in cone_rows:
    tag = "<".join(perm)
    print(f"cone {tag} P = {P_cone}")
    print(f"cone {tag} Q = {Q_cone}")
    print(f"cone {tag} gain = {gain_cone}")
    print(f"cone {tag} gain_float = {float(gain_cone):.15f}")
print(f"P_total = {P_total}")
print(f"Q_total = {Q_total}")
print(f"delta_full = {delta_full}")
print(f"delta_prev = {delta_prev}")
print(f"delta_increment = {delta_increment}")
print(f"DeltaC_increment = {DeltaC_increment}")
print(f"U4_prev = {U4_prev}")
print(f"U4_new = {U4_new}")
print(f"A_prev = {A_prev}")
print(f"A_new = {A_new}")
print(f"x = {x}")
print(f"S32_minus_U4_new = {margin}")
print(f"L_prev = {L_prev}")
print(f"L_new = {L_new}")
print(f"metric_gain = {L_new-L_prev}")
print(f"P_total_float = {float(P_total):.15f}")
print(f"Q_total_float = {float(Q_total):.15f}")
print(f"delta_full_float = {float(delta_full):.15f}")
print(f"delta_increment_float = {float(delta_increment):.15f}")
print(f"DeltaC_increment_float = {float(DeltaC_increment):.15f}")
print(f"U4_new_float = {float(U4_new):.15f}")
print(f"A_new_float = {float(A_new):.15f}")
print(f"S32_minus_U4_new_float = {float(margin):.15e}")
print(f"L_new_float = {float(L_new):.15f}")
print(f"metric_gain_float = {float(L_new-L_prev):.15e}")
print("ALL_EXACT_CHECKS_PASS = True")