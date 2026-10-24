import math
from fractions import Fraction

tau = Fraction(1, 2**20)
beta = (Fraction(1,12800) - tau - 2*tau*tau)/2
E0 = (1-tau)**2/4
top4 = Fraction(63,64)*E0
rho_star = Fraction(63,16384)*(1-tau)**2

assert beta > 40*tau
assert Fraction(1,12800) == Fraction(2048,25)*tau
assert Fraction(48,25)*tau - 41*tau*tau > tau
assert top4 > Fraction(246,1000)

# STAR4 rank-one tube algebra.
# If s2<=s1/16 and tail_{>=5}<E/64 then R=sum_{>=2}s_r^2 <= s1^2/36.
coef = (Fraction(3,256) + Fraction(1,64))*Fraction(64,63)
assert coef == Fraction(1,36)

C_d5 = 5*math.sqrt(2*math.e)*(120/((1/64)**4*float(E0)**5))**0.1
C_window = 5400*math.sqrt(math.e)/(29*math.sqrt(2))

print(f"tau={float(tau):.16g}")
print(f"beta={float(beta):.15f}")
print(f"beta_over_tau={float(beta/tau):.12f}")
print(f"E0={float(E0):.15f}")
print(f"top4_lower={float(top4):.15f}")
print(f"rho_star={float(rho_star):.15f}")
print(f"D5_bound={C_d5:.12f}")
print(f"window_bound={C_window:.12f}")
print(f"rank1_tail_coefficient={float(coef):.15f}")
print("QFORM_B19_TINYTAU_STAR4_CHECK_PASS")
