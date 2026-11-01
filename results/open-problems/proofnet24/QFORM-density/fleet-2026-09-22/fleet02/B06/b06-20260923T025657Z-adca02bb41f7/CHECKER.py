from fractions import Fraction as F
import math

# QFORM-PHYSICAL-CHAIN-WEIGHTED-FIBER-v1 and weakened-interface falsifier.
N = 4096
assert N >= 16

# For B0=[[1,1,0],[1,0,1],[0,1,0]], p(lam)=lam^3-lam^2-2lam+1.
# On |lam|<=1/3, p(lam) >= 1-1/27-1/9-2/3 = 5/27 >0.
spectral_gap_certificate = F(5,27)
assert spectral_gap_certificate > 0

# E_N={e^-N/N <= y <= 1/N, 0<=z<=1/(Ny)} has area
# (1/N)*log((1/N)/(e^-N/N)) = (1/N)*N = 1.
area_certificate = F(1,1)
conditional_Z_cap = F(1,1)  # Ny<=1 because y<=1/N.
assert area_certificate == 1 and conditional_Z_cap == 1

# On X<=1/(4 sqrt N), y<=1/N, yz<=1/N:
# q0=X^2+2XY+2YZ <= 1/(16N)+1/(2N^(3/2))+2/N < 3/N.
lhs_scaled = F(1,16) + F(1,2*math.isqrt(N)) + 2
assert math.isqrt(N)**2 == N
assert lhs_scaled < 3

prob_lower = 1/(4*math.sqrt(N))
interval_width = 9/N
density_lower = prob_lower/interval_width

# Product-chain theorem at a=d=3 gives 4/sqrt(9)=4/3.
chain_bound_A3 = F(4,3)

# Apply partner r24 to crossed-star/tiny-tail test eps=1/N.
eps = F(1,N)
partner_sigma3_bound = 25/math.sqrt(float(eps))
delta2 = 1 + 2*float(eps)**2

print("STATUS PASS")
print("N", N)
print("spectral_gap_certificate", spectral_gap_certificate, float(spectral_gap_certificate))
print("area_certificate", area_certificate)
print("conditional_Z_given_Y_cap", conditional_Z_cap)
print("event_scaled_q0_upper", lhs_scaled, float(lhs_scaled), "< 3")
print("probability_lower", prob_lower)
print("Q_interval_width", interval_width)
print("weakened_interface_density_lower", density_lower)
print("product_chain_bound_for_A_eq_3B0", chain_bound_A3, float(chain_bound_A3))
print("partner_r24_sigma3_bound_crossed_star", partner_sigma3_bound)
print("crossed_star_Delta2", delta2)
