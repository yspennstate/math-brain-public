from fractions import Fraction

# Exact rational core for R07 I0077 sampled spatial-comb gates.
# Analytic inequalities used on the report page:
#   sup Gaussian density < 1 when s^2=3/4 (because (s*sqrt(2*pi))^2=3*pi/2>1),
#   P(|Z|>=x) <= 2 exp(-x^2/2),
#   exp(5) > 1+5+5^2/2 = 37/2 > 10.

s2 = Fraction(3, 4)
eta0 = Fraction(1, 100)
eta1 = Fraction(3, 200)
eta2 = Fraction(1, 50)
slack01 = eta1 - eta0
slack12 = eta2 - eta1
nearest_tooth_length = 2 * eta2
other_tooth_distance = Fraction(3, 1) - eta2
chernoff_exponent = other_tooth_distance**2 / (2 * s2)
exp5_truncation = Fraction(1, 1) + 5 + Fraction(25, 2)
q_rational_upper = Fraction(1, 25) + Fraction(1, 5)

checks = {
    "s2=3/4": s2 == Fraction(3, 4),
    "eta1-eta0=1/200": slack01 == Fraction(1, 200),
    "eta2-eta1=1/200": slack12 == Fraction(1, 200),
    "nearest tooth length=1/25": nearest_tooth_length == Fraction(1, 25),
    "other tooth distance=149/50": other_tooth_distance == Fraction(149, 50),
    "Chernoff exponent=22201/3750": chernoff_exponent == Fraction(22201, 3750),
    "Chernoff exponent>5": chernoff_exponent > 5,
    "1+5+25/2=37/2": exp5_truncation == Fraction(37, 2),
    "37/2>10": exp5_truncation > 10,
    "rational q upper=6/25": q_rational_upper == Fraction(6, 25),
    "6/25<1/4": q_rational_upper < Fraction(1, 4),
    "25/6>4": Fraction(25, 6) > 4,
}

for label, ok in checks.items():
    print(f"{label}: {'PASS' if ok else 'FAIL'}")

print("s2 =", s2)
print("slacks =", slack01, slack12)
print("nearest_tooth_length =", nearest_tooth_length)
print("other_tooth_distance =", other_tooth_distance)
print("chernoff_exponent =", chernoff_exponent)
print("exp5_truncation =", exp5_truncation)
print("q_rational_upper =", q_rational_upper)

if not all(checks.values()):
    raise SystemExit("FAIL")
print("PASS")
