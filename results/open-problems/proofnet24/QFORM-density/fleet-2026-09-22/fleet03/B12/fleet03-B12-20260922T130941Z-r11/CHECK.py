import math

pi = math.pi
C3 = 2*pi + 3*math.sqrt(3)
C = C3 + math.sqrt(C3*C3 + 3*pi*pi)
a = (pi/C)**2
b = C3/C
old_pair = pi*math.sqrt(1000/17)
old_triple = (2000/949)*C3
old = max(old_pair, old_triple)

assert abs((3*a + 2*b)-1) < 2e-15
assert abs(pi/math.sqrt(a)-C) < 2e-13
assert abs(C3/b-C) < 2e-13
assert 0 < a < 1/3
assert 0 < b < 1
assert C < old

print(f'C3={C3:.15f}')
print(f'C_star={C:.15f}')
print(f'a_star={a:.15f}')
print(f'b_star={b:.15f}')
print(f'frontier={3*a+2*b:.15f}')
print(f'pair_cost={pi/math.sqrt(a):.15f}')
print(f'triple_cost={C3/b:.15f}')
print(f'old_pair={old_pair:.15f}')
print(f'old_triple={old_triple:.15f}')
print(f'old_max={old:.15f}')
print(f'improvement={old-C:.15f}')
print('QFORM_OPTIMAL_SWITCH_CHECK_PASS')
