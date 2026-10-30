from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 50

# Exact threshold used in REPORT.md
delta = Fraction(9,16)
D0 = Fraction(13,512)          # proved strict lower bound for |det pair|
k0 = Fraction(1,50)           # proved strict lower bound for sigma_min(pair)

# Diagonal branch: 256 * delta^(-1/4) = 512/sqrt(3).
# Certify it is <296 by squaring positive quantities.
diag_pass = 512**2 < 3 * 296**2

# Pair branch bound in REPORT.md:
# C_pair < 6 * 400^(1/3) * 80000^(1/6).
# Certify it is <291 by raising both positive sides to the sixth power.
pair_lhs6 = 6**6 * 400**2 * 80000
pair_rhs6 = 291**6
pair_pass = pair_lhs6 < pair_rhs6

# Structural exact inequalities used by the rational threshold.
D_pass = Fraction(175,512) - Fraction(81,256) == D0
kappa_pass = Fraction(466,25)**2 < 350  # proves sqrt(350)>466/25, hence (sqrt350-18)/32>1/50

print({
    'delta': str(delta),
    'diag_lt_296': diag_pass,
    'pair_lt_291': pair_pass,
    'D_identity': D_pass,
    'kappa_rational_certificate': kappa_pass,
    'pair_lhs6': pair_lhs6,
    'pair_rhs6_291': pair_rhs6,
    'overall_lt_296': diag_pass and pair_pass and D_pass and kappa_pass,
})
