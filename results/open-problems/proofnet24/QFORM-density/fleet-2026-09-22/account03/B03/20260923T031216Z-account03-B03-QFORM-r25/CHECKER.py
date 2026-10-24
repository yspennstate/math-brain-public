import math

Cpar = 4 * (1 + math.sqrt(3))
Cquarter = 2 * math.sqrt(Cpar) * 2 ** (-1/8)
Criesz = 2 * math.gamma(1/4) * math.cos(math.pi/8) * Cquarter
Cpair = 3 * 2 ** (5/4) * Cpar ** (1/3)
Ccollision = 2 * Cpair

# For r=|a|M in [0,1], the proof chooses K-1=1/r.  The normalized
# near+far bracket is sqrt(1+2r)+1, maximized at r=1.
assert math.sqrt(1 + 2*1.0) + 1 <= 1 + math.sqrt(3) + 1e-15

# Scaling checks: projection cap M scales as ||m||^{-1}; quarter potential
# therefore scales as ||m||^{-1/4}; the pair transducer raises its
# quarter-small-ball coefficient to 2/3, hence ||m||^{-1/6}.
assert abs((-1/4) * (2/3) - (-1/6)) < 1e-15

# Target-family block H_a has determinant -1, so its two real eigenvalues
# have product -1; at least one has absolute value >=1 for every a.
for a in [-100, -3, -1, -1e-9, 0, 1e-9, 1, 3, 100]:
    disc = math.sqrt(a*a + 4)
    l1 = (a + disc)/2
    l2 = (a - disc)/2
    assert abs(l1*l2 + 1) < 1e-10
    assert max(abs(l1), abs(l2)) >= 1 - 1e-12

print('QFORM_B03_R25_CHECK_PASS')
print(f'C_par={Cpar:.15f}')
print(f'C_quarter={Cquarter:.15f}')
print(f'C_riesz={Criesz:.15f}')
print(f'C_pair={Cpair:.15f}')
print(f'C_collision={Ccollision:.15f}')
print(f'max_simple_near_far_factor={1+math.sqrt(3):.15f}')
