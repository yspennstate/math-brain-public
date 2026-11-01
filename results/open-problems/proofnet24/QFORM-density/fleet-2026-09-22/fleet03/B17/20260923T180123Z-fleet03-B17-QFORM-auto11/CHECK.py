from fractions import Fraction
from decimal import Decimal, getcontext
import itertools, math

# Householder bank-core q(d)=|d|^2-(2/3)(sum d)^2 on partner cell-center patterns.
vals=[]
for d in itertools.product(range(3), repeat=3):
    if d == (0,0,0):
        continue
    q = Fraction(sum(x*x for x in d),1) - Fraction(2,3)*sum(d)**2
    vals.append((d,q))
assert all(q != 0 for _, q in vals)
assert min(abs(q) for _, q in vals) == Fraction(1,3)

# Uniform support-box separation for R>=50.  C=(R+eta/2)/sqrt(2)>=R/sqrt(2).
R=50.0
C=R/math.sqrt(2)
margin = C*C/3 - 6*math.sqrt(2)*C - 1.5
assert margin > 0

# Partner exact cone-tip constant and the strengthened equality values.
getcontext().prec=60
pstar=Decimal("4.06307061680603726012548442259349995675296534606391429208671")
eta=Decimal("0.001")
pexact=(Decimal(1)-eta)**4*pstar
pbalanced=(Decimal("0.5")**4)*pstar
assert pexact > Decimal(4)
assert pbalanced == pstar/Decimal(16)

print("PASS QFORM_DENSE_REMOTE_FRAGMENT_SEPARATION")
print("min_abs_q_integer_pattern =", min(abs(q) for _,q in vals))
print("R50_cone_separation_margin_lower =", margin)
print("eta_1e-3_exact_conetip =", pexact)
print("eta_1/2_exact_conetip =", pbalanced)
print("gap_base_minus_eta_1e-3 =", pstar-pexact)
