import math


def C_integer(p):
    a = 2 * math.sqrt(2)
    integral = sum(math.comb(p, k) * a ** (p-k) * math.factorial(k)
                   for k in range(p+1))
    cp_power = 4 * integral + 2 ** (2 + 1.5*p) / (p/2 - 1)
    return cp_power ** (1/p), integral, cp_power


def pair_inner_ratio(x):
    # sqrt(kappa)*sqrt(tau)*Psi(tau) on the inner region after x=tau/T.
    return math.sqrt(2*x) * (2*math.sqrt(2) + math.log(1/x))

mx = 0.0
arg = None
for j in range(200001):
    y = 30.0 * j / 200000
    x = math.exp(-y)
    v = pair_inner_ratio(x)
    if v > mx:
        mx, arg = v, x
assert mx <= 4.0 + 1e-12

C8, I8, V8 = C_integer(8)
q8 = 8/7
square_q8 = (2 ** (q8-1) / (2-q8)) ** (1/q8)
K8 = C8 * 2 ** (1-1/8) * square_q8 * (math.sqrt(2)) ** (2/8)

C6, I6, V6 = C_integer(6)
q6 = 6/5
K6 = C6 * q6 * 2 ** (1-1/(2*6))

print(f"pair_inner_ratio_max={mx:.15f} at x={arg:.15f}")
print(f"C8={C8:.15f}")
print(f"I8={I8:.15f}")
print(f"C8^8={V8:.15f}")
print(f"K8_three_bank_square={K8:.15f}")
print(f"C6={C6:.15f}")
print(f"I6={I6:.15f}")
print(f"C6^6={V6:.15f}")
print(f"K6_pair_plus_affine_packet={K6:.15f}")
print(f"pair_E2_composite={4*7.673759290384858:.15f}")
print(f"pair_E3_composite={4*9.840655864922019:.15f}")
print(f"pair_exact_rank2_composite={4*7.270461147134126:.15f}")
print(f"pair_partner_packet={32*math.sqrt(2):.15f}")
print(f"normalized_bank_half_riesz_cascade={32*2**1.25:.15f}")

for m in (1, 2, 5, 10, 100):
    D = 1/(2*m)
    kappa = 1/math.sqrt(2*m)
    aggregate = m*D
    assert abs(aggregate - 0.5) < 1e-15
    print(f"m={m} D={D:.12g} kappa={kappa:.12g} Dkappa={D*kappa:.12g} aggregate={aggregate:.12g}")

print("STATUS=PASS")
