import math

c_holder = 6 * math.sqrt(2 * math.pi)
family_holder = 24 * math.sqrt(math.pi)
mhalf = 2**0.25 * math.gamma(0.75) / math.sqrt(math.pi)
c_heat = 6 * 2**0.75 * math.gamma(0.75)
family_heat = family_holder * mhalf
family_height = 6 * 2**(1/3)

assert abs(c_holder - 15.039769647786002) < 1e-12
assert abs(family_holder - 42.538892421732385) < 1e-12
assert abs(mhalf - 0.8221789586624588) < 1e-12
assert abs(c_heat - 12.365382147539949) < 1e-12
assert abs(family_heat - 34.97458227395429) < 1e-12
assert abs(family_height - 7.559526299369239) < 1e-12

# Algebraic consistency of the six-coordinate specialization:
# K = sqrt(2)*pi^(3/2)*(1/8)^(-1/2) = 4*pi^(3/2),
# so 6K/pi = 24*sqrt(pi), and (2/3)*(6K/pi)=16*sqrt(pi).
K_family = math.sqrt(2) * math.pi**1.5 * (1/8)**(-0.5)
assert abs(K_family - 4 * math.pi**1.5) < 1e-12
assert abs(6 * K_family / math.pi - family_holder) < 1e-12
assert abs((2/3) * family_holder - 16 * math.sqrt(math.pi)) < 1e-12
assert abs(family_holder * mhalf - family_heat) < 1e-12

print('QFORM_B15_T32_ENDPOINT_HOLDER_CONSTANT_CHECK_PASS')
print(f'c_holder={c_holder:.15f}')
print(f'family_holder={family_holder:.15f}')
print(f'mhalf={mhalf:.15f}')
print(f'c_heat={c_heat:.15f}')
print(f'family_heat={family_heat:.15f}')
print(f'family_height={family_height:.15f}')
