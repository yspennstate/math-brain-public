import math

L = 1.0
eta = 1.0/8.0
beta = (3.0/16.0)*math.sqrt(3.0/5.0)*L
tau0 = 1.0/8192.0
eps0 = math.sqrt(tau0 + tau0*tau0)

C_k0 = 6.0*math.sqrt(math.e)/beta
C_k1_tail = (9.0*math.sqrt(3.0)*math.e)/(2.0*beta*eta**(1.0/3.0))
C_k1_volume = 6.0*math.sqrt(math.e)*15.0**(1.0/3.0)/(beta*eta**(1.0/3.0))
C_k2_volume = 6.0*math.sqrt(math.e)/(beta*eta**(2.0/3.0))
hub_support_ratio = beta*beta/(2.0*eps0*eps0)

print(f"beta={beta:.15f}")
print(f"eta_beta={eta*beta:.15f}")
print(f"C_k0={C_k0:.12f}")
print(f"C_k1_tail={C_k1_tail:.12f}")
print(f"C_k1_volume={C_k1_volume:.12f}")
print(f"C_k2_volume={C_k2_volume:.12f}")
print(f"eps0={eps0:.15f}")
print(f"hub_support_ratio={hub_support_ratio:.12f}")
assert C_k0 < 69.0
assert C_k1_tail < 292.0
assert C_k1_volume < 336.0
assert C_k2_volume < 273.0
assert 86.0 < hub_support_ratio < 87.0

# Exact spectral formulas for the two Hadamard hybrid witnesses.
# P has k entries 1-delta and 3-k entries 1/5.
# The 2m x 2m block form [[UPU^T,U(I-P)U^T],[same,UPU^T]]
# has + eigenvalues 1,1,1 and - eigenvalues 2p_j-1.
delta = beta/16.0
for k in (1,2):
    p = [1.0-delta]*k + [1.0/5.0]*(3-k)
    plus = [1.0,1.0,1.0]
    minus = [2.0*x-1.0 for x in p]
    cross = sorted([1.0-x for x in p], reverse=True)
    child = sorted(p, reverse=True)
    count_large = sum(abs(x) >= 1.0-1e-14 for x in plus+minus)
    count_child_gate = sum(abs(x) >= 0.5*math.sqrt(3.0/5.0)-1e-14 for x in child)
    print(f"k={k} plus={plus} minus={minus} child={child} cross={cross} target_large={count_large} child_gate={count_child_gate}")
    assert count_large == 3
    assert count_child_gate == k
    if k == 1:
        assert cross[1] == 0.8 and cross[2] < eta*beta
    if k == 2:
        assert cross[1] < eta*beta and cross[2] < eta*beta

print("QFORM_B08_HYBRID_VOLUME_TAIL_CHECK_PASS")
