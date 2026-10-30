import math

# Theorem 2.1 optimization: 8 eps/eta + 4 M eta^2 at eta=(eps/M)^(1/3)
# gives 12 M^(1/3) eps^(2/3).
eps=0.137
M=2.31
eta=(eps/M)**(1/3)
lhs=8*eps/eta+4*M*eta**2
rhs=12*M**(1/3)*eps**(2/3)
assert abs(lhs-rhs) < 1e-12

# Layer cake for alpha=2/3, beta=1/2: crossover s0=H^(3/4),
# integral <= s0 + 3 H s0^(-1/3) = 4 H^(3/4).
H=3.77
s0=H**(3/4)
assert abs((s0+3*H*s0**(-1/3)) - 4*H**(3/4)) < 1e-12

C_scalar=4*12**(3/4)*2**(-1/4)
B_scalar=C_scalar*64**(1/2)*64**(1/4)
C_pair=3*2**(4/3)*12**(1/4)*2**(-1/12)
B_pair=C_pair*64**(1/3)*64**(1/6)*64**(1/12)

print(f"C_scalar={C_scalar:.12f}")
print(f"threshold_scalar={B_scalar:.12f}")
print(f"C_pair={C_pair:.12f}")
print(f"threshold_pair={B_pair:.12f}")
assert C_scalar < 21.687
assert B_scalar < 491
assert C_pair < 13.281
assert B_pair < 151
print("QFORM_B19_R24_TWOGRADIENT_CHECK_PASS")
