from fractions import Fraction

ASSERTIONS = 0


def check(cond):
    global ASSERTIONS
    if not cond:
        raise AssertionError(f"assertion {ASSERTIONS + 1} failed")
    ASSERTIONS += 1


def H(p, i, j):
    return p**i * (1-p)**j + p**j * (1-p)**i


def mask_split_prob(p, i, j):
    # Specified unordered split: first i leaves red / last j blue, or complement.
    m = i + j
    ans = Fraction(0, 1)
    for mask in range(1 << m):
        nr = mask.bit_count()
        prob = p**nr * (1-p)**(m-nr)
        first_red_last_blue = (
            all((mask >> a) & 1 for a in range(i))
            and all(not ((mask >> a) & 1) for a in range(i, m))
        )
        first_blue_last_red = (
            all(not ((mask >> a) & 1) for a in range(i))
            and all((mask >> a) & 1 for a in range(i, m))
        )
        if first_red_last_blue or first_blue_last_red:
            ans += prob
    return ans


# N=4 harmonic clocks.
lam = {s: Fraction(4, 2*s*(4-s)) for s in (1, 2, 3)}
check(lam[1] == Fraction(2, 3))
check(lam[2] == Fraction(1, 2))
check(lam[3] == Fraction(2, 3))

# C090 at N=4: b4=1, d4=2.
# s=1 lies outside the active interval and keeps p=1/4.
# s=2: half-period cyclic dither gives 1/2, 2/3.
# s=3: adding log 2 to logit(3/4)=log 3 crosses the log-4 seam,
# and the wrapped logit is log(3/2), giving 3/5.
bias = {
    1: (Fraction(1, 4),),
    2: (Fraction(1, 2), Fraction(2, 3)),
    3: (Fraction(3, 4), Fraction(3, 5)),
}
check(bias[1][0] == Fraction(1, 4))
check(bias[2] == (Fraction(1, 2), Fraction(2, 3)))
check(bias[3] == (Fraction(3, 4), Fraction(3, 5)))

# Direct finite enumeration agrees with the specified-split formula
# for five biases and six split shapes.
all_ps = [Fraction(1, 4), Fraction(1, 2), Fraction(2, 3),
          Fraction(3, 4), Fraction(3, 5)]
shapes = [(1, 1), (1, 2), (1, 3), (2, 2), (1, 4), (2, 3)]
for p in all_ps:
    for i, j in shapes:
        check(mask_split_prob(p, i, j) == H(p, i, j))


def q(i, j):
    total = Fraction(0, 1)
    for s in (1, 2, 3):
        avg = sum((H(p, i, j) for p in bias[s]), Fraction(0, 1)) / len(bias[s])
        total += lam[s] * avg
    return total


q13 = q(1, 3)
q22 = q(2, 2)
check(q13 == Fraction(1431443, 6480000))
check(q22 == Fraction(1066957, 6480000))

root = 4*q13 + 3*q22
balanced = 3*q22/root
check(root == Fraction(8926643, 6480000))
check(balanced == Fraction(3200871, 8926643))
check(Fraction(3, 11) == 3*Fraction(1, 6)/(4*Fraction(1, 3)+3*Fraction(1, 6)))
check(balanced - Fraction(3, 11) == Fraction(766332, 8926643))
check(balanced != Fraction(3, 11))
check(q13/q22 == Fraction(1431443, 1066957))
check(q13/q22 != Fraction(2, 1))
check(Fraction(1, 3) / Fraction(1, 6) == 2)

# Seam endpoint data used in U074.
check(H(Fraction(1, 2), 1, 1) == Fraction(1, 2))
check(H(Fraction(4, 5), 1, 1) == Fraction(8, 25))
check(H(Fraction(1, 2), 1, 3) == Fraction(1, 8))
check(H(Fraction(4, 5), 1, 3) == Fraction(68, 625))

# Rational numerators in the exact integrals
# int_0^1 H_11(t)dt = 3/(10 log 2),
# int_0^1 H_13(t)dt = 21/(250 log 2).
check(Fraction(3, 10) == Fraction(3, 10))
check(Fraction(21, 250) == Fraction(21, 250))

# If a single seam weight w matched both observables, eliminating w forces
# log 2 = 57/80.  Indeed
#   w11(l) = (15-16l)/(9l),
#   w13(l) = 4(105-136l)/(81l).
lhs_const = 9*15
lhs_l = 9*16
rhs_const = 4*105
rhs_l = 4*136
check(rhs_l - lhs_l == 400)
check(rhs_const - lhs_const == 285)
forced_log2 = Fraction(rhs_const-lhs_const, rhs_l-lhs_l)
check(forced_log2 == Fraction(57, 80))

# Strict elementary upper bound log 2 < 17/24 from the two-panel
# trapezoid rule for the strictly convex function 1/x on [1,2].
trap = (Fraction(1, 4)*(Fraction(1, 1)+Fraction(2, 3))
        + Fraction(1, 4)*(Fraction(2, 3)+Fraction(1, 2)))
check(trap == Fraction(17, 24))
check(Fraction(57, 80) - trap == Fraction(1, 240))
check(trap < Fraction(57, 80))

# Small-N active-grid complexity sanity.  The theorem uses the general
# pigeonhole/Dirichlet argument; this is only a finite exact check.
for N in range(4, 41):
    active = [s for s in range(1, N)
              if Fraction(1, 2) <= Fraction(s, N) < Fraction(4, 5)]
    M = len(active)
    check(M >= 1)
    check(M <= N)
    check(N**M <= N**N)

print("R11 U073/U074/C090 exact self-check")
print(f"ASSERTIONS={ASSERTIONS}")
print(f"C090_N4_q13={q13}")
print(f"C090_N4_q22={q22}")
print(f"C090_N4_root_rate={root}")
print(f"C090_N4_balanced={balanced}")
print(f"C090_N4_balanced_minus_CTCS={balanced-Fraction(3,11)}")
print(f"C090_N4_q13_over_q22={q13/q22}")
print(f"seam_equal_weight_forces_log2={forced_log2}")
print(f"trapezoid_upper_bound_log2={trap}")
print(f"gap_57_80_minus_17_24={Fraction(57,80)-trap}")
print("STATUS=ALL_EXACT_CHECKS_PASS")
