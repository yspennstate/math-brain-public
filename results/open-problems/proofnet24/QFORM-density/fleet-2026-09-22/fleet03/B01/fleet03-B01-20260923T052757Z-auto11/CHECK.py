import math


def C_p(p):
    return (4*math.pi*(p-1))**(1/p)*((p-1)/(p-2))**((p-1)/p)


def B_p(p):
    return 2*math.pi*2**(-2/p)*C_p(p)*(2*(p-1))**((p-1)/p)


def K_p(p):
    return (p+1)/math.pi*(B_p(p)/(2*p))**(p/(p+1))

k4 = K_p(4.0)
k4_target = (15/4)*6**(2/5)
assert abs(k4-k4_target) < 1e-12

# The elementary analytic majorant in the report is K_p <= 135 p/32.
for j in range(4001):
    p = 4.0 + j*(196.0/4000.0)
    assert K_p(p) <= (135/32)*p + 1e-12

# Log-receiver prefactor.
log_prefactor = 135*math.e/32

# Endpoint stress-family lower bound coefficient.
lower_log_coefficient = 1/(4*math.sqrt(2))

print(f"K4={k4:.15f}")
print(f"K4_target={k4_target:.15f}")
print(f"coarse_Kp_slope={135/32:.15f}")
print(f"log_prefactor_135e_over_32={log_prefactor:.15f}")
print(f"lower_log_coefficient={lower_log_coefficient:.15f}")
print("STATUS=PASS")
