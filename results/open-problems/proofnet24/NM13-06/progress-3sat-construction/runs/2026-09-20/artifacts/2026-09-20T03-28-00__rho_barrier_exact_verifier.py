from fractions import Fraction


def state_stats(classes):
    """Exact fluid-state moments.

    classes is [(a,b,c,d,count), ...].  We normalize by the total count so
    x_{a,b,c,d} is a density per original variable in this synthetic state.
    """
    N = sum(n for a, b, c, d, n in classes)
    A = Fraction(sum(a*n for a,b,c,d,n in classes), N)
    B = Fraction(sum(b*n for a,b,c,d,n in classes), N)
    C = Fraction(sum(c*n for a,b,c,d,n in classes), N)
    D = Fraction(sum(d*n for a,b,c,d,n in classes), N)
    m2 = (A+B)/2
    m3 = (C+D)/3
    if m2 <= 0:
        raise ValueError("m2 must be positive")

    S = Fraction(sum(a*b*n for a,b,c,d,n in classes), N)
    rho = S/m2

    R = Fraction(sum((b*c+a*d)*n for a,b,c,d,n in classes), N)
    kappa = Fraction(0) if m3 == 0 else 2*R/(3*m3)

    g2_num = Fraction(sum(
        n*(a*(d-(a+b-1)) + b*(c-(a+b-1)))
        for a,b,c,d,n in classes
    ), N)
    g2 = g2_num/(2*m2)

    g3_num = Fraction(sum(
        n*(a+b)*(c+d) for a,b,c,d,n in classes
    ), N)
    g3 = -g3_num/(2*m2)

    gS_num = Fraction(0)
    for a,b,c,d,n in classes:
        h_plus = -(a-1)*b - Fraction(a+b-1)*rho + d*kappa
        h_minus = -a*(b-1) - Fraction(a+b-1)*rho + c*kappa
        gS_num += Fraction(n, N)*(a*h_plus+b*h_minus)
    gS = gS_num/(2*m2)

    return {
        "N": N, "A": A, "B": B, "C": C, "D": D,
        "m2": m2, "m3": m3, "S": S, "rho": rho,
        "kappa": kappa, "g2": g2, "g3": g3,
        "g1": g2+g3, "gS": gS,
    }


def drifts(q, st):
    a,b,c,d = q
    rho = st["rho"]
    den = 1-rho
    if den <= 0:
        raise ValueError("subcriticality rho<1 required")

    g2, g3, gS = st["g2"], st["g3"], st["gS"]
    kappa, m2 = st["kappa"], st["m2"]

    G2T = Fraction(d-(a+b)) + b*g2/den
    G3T = Fraction(-(c+d)) + b*g3/den
    G2F = Fraction(c-(a+b)) + a*g2/den
    G3F = Fraction(-(c+d)) + a*g3/den
    G1T, G1F = G2T+G3T, G2F+G3F

    sT = -a*b - Fraction(a+b)*rho + d*kappa
    sF = -a*b - Fraction(a+b)*rho + c*kappa
    HST = sT + b*gS/den
    HSF = sF + a*gS/den

    RT = (HST-rho*G2T)/m2
    RF = (HSF-rho*G2F)/m2
    return {
        "G2T":G2T, "G3T":G3T, "G1T":G1T,
        "G2F":G2F, "G3F":G3F, "G1F":G1F,
        "HST":HST, "HSF":HSF, "RT":RT, "RF":RF,
    }


def fs(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


# Example A: V_1 cleanup and rho-safety select opposite polarities.
A_classes = [
    (0,1,0,0,3),
    (1,0,0,0,3),
    (1,1,0,1,3),
    (1,1,1,0,3),
]
A = state_stats(A_classes)
Ad = drifts((0,1,0,0), A)

assert A["m2"] == Fraction(3,4)
assert A["m3"] == Fraction(1,6)
assert A["rho"] == Fraction(2,3)
assert A["kappa"] == 2
assert A["g2"] == Fraction(-1,3)
assert A["g3"] == Fraction(-2,3)
assert A["gS"] == Fraction(2,9)
assert Ad["G1T"] == -4
assert Ad["G1F"] == -1
assert Ad["RT"] == Fraction(16,9)
assert Ad["RF"] == 0

# Example B: near criticality, a modest logarithmic rho barrier overturns
# the aggressive V_1 cleanup choice.  For Phi_beta=V_1-beta*log(1-rho),
# the polarity flip occurs at beta=77/1140 < 0.1.
B_classes = [
    (0,3,3,0,3),
    (3,0,0,3,3),
    (1,3,3,0,3),
    (3,1,0,3,3),
]
B = state_stats(B_classes)
Bd = drifts((0,3,3,0), B)
barrier_slope = (Bd["RT"]-Bd["RF"])/(1-B["rho"])
beta_flip = -(Bd["G1T"]-Bd["G1F"])/barrier_slope

assert B["m2"] == Fraction(7,4)
assert B["m3"] == 1
assert B["rho"] == Fraction(6,7)
assert B["kappa"] == 6
assert B["g2"] == 0
assert B["g3"] == -3
assert B["gS"] == Fraction(606,49)
assert Bd["G1T"] == -69
assert Bd["G1F"] == -3
assert Bd["RT"] == Fraction(7272,49)
assert Bd["RF"] == Fraction(432,49)
assert barrier_slope == Fraction(6840,7)
assert beta_flip == Fraction(77,1140)
assert beta_flip < Fraction(1,10)

print("EXACT VERIFIER: PASS")
print("Example A")
print("  m2,m3,rho,kappa =", fs(A["m2"]), fs(A["m3"]), fs(A["rho"]), fs(A["kappa"]))
print("  g2,g3,gS =", fs(A["g2"]), fs(A["g3"]), fs(A["gS"]))
print("  V1 drift TRUE/FALSE =", fs(Ad["G1T"]), fs(Ad["G1F"]))
print("  rho drift TRUE/FALSE =", fs(Ad["RT"]), fs(Ad["RF"]))
print("  conclusion: V1 prefers TRUE, rho-control prefers FALSE")
print("Example B")
print("  m2,m3,rho =", fs(B["m2"]), fs(B["m3"]), fs(B["rho"]))
print("  V1 drift TRUE/FALSE =", fs(Bd["G1T"]), fs(Bd["G1F"]))
print("  rho drift TRUE/FALSE =", fs(Bd["RT"]), fs(Bd["RF"]))
print("  barrier slope difference =", fs(barrier_slope))
print("  exact beta flip =", fs(beta_flip), "=", float(beta_flip))
print("  conclusion: beta=0.1 barrier reverses the near-critical V1 choice")
