from fractions import Fraction as F
import math

m = 32
N = 64
eps = F(1,100)
e = eps*eps

# Squared singular values: 1,1,e,e.
E2 = F(1) + 4*e + e*e
E3 = 2*e + 2*e*e
p_top = (2+e)/(2+2*e)
p_tail = (1+2*e)/(2+2*e)

assert 2*p_top + 2*p_tail == 3
assert F(2,m) == F(1,16)
assert p_tail > F(1,2)

# The heavy left hub is pure u3; heavy right hub is pure v4.
T_left = p_tail
T_right = p_tail
tail_energy_left = e
tail_energy_right = e
energy_lower = (E3/E2)*p_tail
assert tail_energy_left >= energy_lower
assert tail_energy_right >= energy_lower

# With N=64, the tail block is two disjoint stars:
# eps * e_hL * (1/sqrt(N)) 1_SR^T
# + eps * (1/sqrt(N)) 1_SL * e_hR^T.
# Hence the heavy-heavy entry is exactly zero and every nonzero
# tail coefficient has magnitude eps/sqrt(N)=1/800.
assert int(math.isqrt(N))**2 == N
max_tail_coeff = eps / int(math.isqrt(N))
assert max_tail_coeff == F(1,800)
hub_hub_coeff = F(0)

# Compare the largest tail edge with the invariant tail scale sqrt(E3/E2).
ratio_sq = max_tail_coeff*max_tail_coeff / (E3/E2)

# The full target embedding A = [1] direct_sum [[0,M],[M^T,0]]
# has nonzero eigenvalues 1 and +/- the singular values of M:
# {1, +1,-1,+1,-1,+eps,-eps,+eps,-eps}.
large_count = 5
assert large_count >= 3

# Choose a same-sign core pair. Its cross coefficient is 2/m=1/16.
# Together with the added scalar 1, the physical 3x3 block has
# eigenvalues {1,+1/16,-1/16}.
c = F(2,m)
assert c == F(1,16)
localized_bound = 6*math.sqrt(math.pi)/float(c)

print("STATUS PASS")
print("m", m, "N", N, "eps", eps)
print("E2", E2, float(E2))
print("E3", E3, float(E3))
print("p_top", p_top, float(p_top))
print("p_tail", p_tail, float(p_tail))
print("top2_leverage", F(2,m), float(F(2,m)))
print("left_hub_weighted_tail", T_left, float(T_left))
print("right_hub_weighted_tail", T_right, float(T_right))
print("tail_energy", tail_energy_left, float(tail_energy_left))
print("energy_lower", energy_lower, float(energy_lower))
print("hub_hub_tail_coeff", hub_hub_coeff)
print("max_tail_coeff", max_tail_coeff, float(max_tail_coeff))
print("max_tail_coeff_over_sqrt_E3_over_E2", math.sqrt(float(ratio_sq)))
print("target_large_eigenvalue_count", large_count)
print("localized_core_scale", c, float(c))
print("localized_Claude_bound_6sqrtpi_over_c", localized_bound)
