from fractions import Fraction as F
from decimal import Decimal, getcontext

# Exact inherited C045 certificate.
x = F(256717, 800000)
lam = F(
    int("10114875937111444750637950885399422919832438289108176982868202874026753"),
    int("29591135160849999997918500618240000000000000000000000000000000000000000"),
)
# Strict rational endpoint proposed in this run.
Q = F(8262759427622826251, 10**19)
A = 4 * x * x


def neglog_interval(z: F, M: int = 250):
    """Return exact rational [lo,hi] containing -log(z), for 0<z<1.

    Uses -log z = 2 sum_{m>=0} t^(2m+1)/(2m+1),
    t=(1-z)/(1+z), and bounds the positive tail geometrically.
    """
    assert 0 < z < 1
    t = (1 - z) / (1 + z)
    s = F(0, 1)
    p = t
    for m in range(M):
        s += 2 * p / F(2 * m + 1, 1)
        p *= t * t
    first = t ** (2 * M + 1)
    rem = 2 * first / F(2 * M + 1, 1) / (1 - t * t)
    return s, s + rem


LA_lo, LA_hi = neglog_interval(A)
LL_lo, LL_hi = neglog_interval(lam)

# alpha = log(A)/log(lam) = (-log A)/(-log lam).
alpha_lo = LA_lo / LL_hi
alpha_hi = LA_hi / LL_lo

# A sufficient exact inequality for alpha < Q is
# upper(-log A) < Q * lower(-log lambda).
gap = Q * LL_lo - LA_hi
assert gap > 0

L = F(792665992, 10**9)
U_old = F(826275942762282626, 10**18)
W_old = U_old - L
W_new = Q - L
improvement = W_old - W_new
assert improvement > 0

getcontext().prec = 90

def dec(q: F):
    return Decimal(q.numerator) / Decimal(q.denominator)

print("A=4*x^2 =", A)
print("lambda =", lam)
print("candidate_U =", Q)
print("alpha_lower =", dec(alpha_lo))
print("alpha_upper =", dec(alpha_hi))
print("gap_lower_Qloglambda_minus_logA =", dec(gap))
print("CERTIFY_ALPHA_LT_Q =", gap > 0)
print("old_width =", dec(W_old))
print("new_width =", dec(W_new))
print("width_decrease =", dec(improvement))
