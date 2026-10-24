from fractions import Fraction
from math import gcd, log10
import mpmath as mp

# Inherited exact C045 data.
N = 11614187
p = 256717
q = 800000
t = Fraction(p, q)

lam_num = 10114875937111444750637950885399422919832438289108176982868202874026753
lam_den = 29591135160849999997918500618240000000000000000000000000000000000000000
lam = Fraction(lam_num, lam_den)

# Primitive label scaling H=A/t^2 and B=S H.
S = q**6 * (q-p)
a = 1995237757733917147310102692686664915858011319606812684127301
b = 4220452010631561279
R = Fraction(a, b)

# Integer witness construction bound from the frozen witness recipe.
M = 5000000000000000000

assert gcd(a,b) == 1
assert b > 1
assert b <= M < 2*b
assert a > M
assert Fraction(S,1) * lam / (t*t) == R
assert 0 < lam < 1

# New two-step strictification:
# rho(B)^2 <= R^2 - 1/b^2 = (a^2-1)/b^2.
# Since sqrt(a^2-1) < a - 1/(2a),
# rho(A) < lam - eps2, where eps2 = t^2/(2*S*a*b).
eps2 = t*t / Fraction(2*S*a*b,1)
lam2 = lam - eps2
assert 0 < eps2 < lam
assert 0 < lam2 < lam < 1

# Previous primitive-content gap from the prior P02 report:
# eps_prim = t^2 / (2*S*b*(2a)^(N-1)).
# Ratio is exactly 2^(N-1)*a^(N-2), hence >1.
assert N > 2 and a > 1
assert (2*a) > 1

# Public rigorous lower endpoint.
L = Fraction(99083249,125000000)

# Diagnostic high-precision values only; exact strictness is proved above.
mp.mp.dps = 180
tm = mp.mpf(p)/q
lamm = mp.mpf(lam_num)/lam_den
epsm = mp.mpf(eps2.numerator)/eps2.denominator
U0 = mp.log(4*tm*tm)/mp.log(lamm)
U2 = mp.log(4*tm*tm)/mp.log(lamm-epsm)
Ug = U0-U2

print("P02 T02 two-step rational-Collatz strictification checker")
print(f"N={N}")
print(f"t={p}/{q}")
print(f"S={S}")
print(f"a={a}")
print(f"b={b}")
print(f"M={M}")
print(f"gcd(a,b)={gcd(a,b)}")
print(f"b<=M<2b={b <= M < 2*b}")
print(f"a>M={a>M}")
print(f"R_identity={Fraction(S,1)*lam/(t*t) == R}")
print(f"epsilon_two_num={eps2.numerator}")
print(f"epsilon_two_den={eps2.denominator}")
print(f"log10_epsilon_two~={log10(eps2.numerator)-log10(eps2.denominator):.15f}")
print(f"lambda_two_num={lam2.numerator}")
print(f"lambda_two_den={lam2.denominator}")
print("epsilon_two/epsilon_prim = 2^(N-1)*a^(N-2) > 1")
print("U_base~="+mp.nstr(U0, 80))
print("U_two~="+mp.nstr(U2, 80))
print("U_base_minus_U_two~="+mp.nstr(Ug, 50))
print("log10_U_improvement~="+mp.nstr(mp.log10(Ug), 40))
print(f"L={L.numerator}/{L.denominator}")
print("EXACT_TWO_STEP_CONSTANT_CHECKS_PASS")
print("SOURCE_INTERVAL_STRICTLY_SHRINKS_PASS")
print("ALL_EXACT_CHECKS_PASS")
