from fractions import Fraction
from math import gcd, lcm, log10

# Exact inherited C045 data.
N = 11_614_187
p = 256_717
q = 800_000
r = q - p
lam_num = int("10114875937111444750637950885399422919832438289108176982868202874026753")
lam_den = int("29591135160849999997918500618240000000000000000000000000000000000000000")
lam = Fraction(lam_num, lam_den)
t = Fraction(p, q)

# At x=y=t the C045 label weights are t^(a+2), 0<=a<=6,
# and t^9/(1-t) at |ell|=7.  Extract the common t^2:
# H=A/t^2 has weights 1,t,...,t^6,t^7/(1-t).
weights_H = [t**k for k in range(7)] + [t**7 / (1 - t)]
denoms = [w.denominator for w in weights_H]
S = 1
for d in denoms:
    S = lcm(S, d)

assert gcd(p, q) == 1
assert gcd(q, r) == 1
assert S == q**6 * r

int_coeffs = [int(w * S) for w in weights_H]
assert all(Fraction(c, 1) == w * S for c, w in zip(int_coeffs, weights_H))
primitive_gcd = 0
for c in int_coeffs:
    primitive_gcd = gcd(primitive_gcd, c)
assert primitive_gcd == 1

# Primitive algebraic-integer scaling.
Lam = lam / (t * t)
R = Fraction(S, 1) * Lam
a = R.numerator
b = R.denominator
assert gcd(a, b) == 1 and b > 1

# Previous run's non-primitive integer scaling, for an exact comparison.
C_old = int("50707486515870312693760000000000000000000000000000000000000000")
R_old = Fraction(C_old, 1) * lam
a_old, b_old = R_old.numerator, R_old.denominator
assert b_old == b

K_frac = Fraction(C_old, 1) * t * t / Fraction(S, 1)
assert K_frac.denominator == 1
K = K_frac.numerator
assert K > 1
assert a_old == K * a
assert Fraction(C_old, 1) * t * t == K * S

# If eps_old = 1/(2*C_old*b*(2*a_old)^(N-1)) and
# eps_new = t^2/(2*S*b*(2*a)^(N-1)), then eps_new/eps_old=K^N.
# This symbolic comparison avoids materializing enormous powers.
assert 0 < 4 * t * t < 1
assert 0 < lam < 1

# Diagnostics only; theorem comparisons above are exact integers/rationals.
logeps_new = 2 * log10(p / q) - (
    log10(2) + log10(S) + log10(b) + (N - 1) * log10(2 * a)
)
logeps_old = -(
    log10(2) + log10(C_old) + log10(b_old) + (N - 1) * log10(2 * a_old)
)
logratio = N * log10(K)

print("P02 T02 primitive-content spectral-gap checker")
print(f"N={N}")
print(f"t={p}/{q}")
print(f"r=q-p={r}")
print("H_weights_denominators=" + ",".join(map(str, denoms)))
print(f"S_lcm={S}")
print("primitive_integer_coeff_gcd=1")
print(f"R_primitive_num={a}")
print(f"R_primitive_den={b}")
print(f"R_old_num={a_old}")
print(f"R_old_den={b_old}")
print(f"K={K}")
print("a_old_equals_K_times_a=PASS")
print("epsilon_new_over_epsilon_old=K^N")
print(f"log10_K_to_N~={logratio:.12f}")
print(f"log10_epsilon_old~={logeps_old:.12f}")
print(f"log10_epsilon_new~={logeps_new:.12f}")
print("source_interval_strictly_shrinks_again=PASS")
print("ALL_EXACT_CHECKS_PASS")
