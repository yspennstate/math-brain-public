import math

K3 = 2.0 * math.sqrt(2.0)
K1 = math.sqrt(2.0)
J = 2.0 * (2.0*K1)**0.75 + 1.0
M0 = (2.0 * (K3/2.0)**0.75 * J)**(2.0/3.0)
HY = (2.0*math.pi)**(1.0/3.0) * M0
A = math.pi*math.sqrt(2.0)*HY * 4.0**(2.0/3.0)
C0 = (4.0/math.pi) * (A/6.0)**0.75
E2 = 29.0/3072.0
rho = math.sqrt(E2)
application = C0 * (1.0/64.0)**(-0.25) * rho**(-3.0/8.0)
partner = 34.0*math.sqrt(9.0)

# Gram determinant of [[I,c],[c^T,1+|c|^2]] is identically one;
# test a few deterministic c values as a regression check.
def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

max_gram_err = 0.0
for c1,c2 in [(0.0,0.0),(1.0,-2.0),(10.0,0.125),(-3.5,4.25)]:
    G = [[1.0,0.0,c1],[0.0,1.0,c2],[c1,c2,1.0+c1*c1+c2*c2]]
    max_gram_err = max(max_gram_err, abs(det3(G)-1.0))

assert C0 < 12.01
assert application < 82.0
assert partner == 102.0
assert max_gram_err < 1e-12

print(f"K3={K3:.15f}")
print(f"K1={K1:.15f}")
print(f"J={J:.15f}")
print(f"M0={M0:.15f}")
print(f"HY_constant={HY:.15f}")
print(f"tail_A={A:.15f}")
print(f"density_constant={C0:.15f}")
print(f"E2={E2:.15f}")
print(f"rho={rho:.15f}")
print(f"compound_energy_application={application:.15f}")
print(f"partner_e_minus_8_to_1={partner:.15f}")
print(f"max_gram_det_error={max_gram_err:.3e}")
print("QFORM_B19_R26_TRANSVERSE_AGGREGATE_CHECK_PASS")
