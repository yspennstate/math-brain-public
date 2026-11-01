import math

C3 = 3 * 2**(1/6)
assert abs((2*C3)**3 - 216*math.sqrt(2)) < 1e-10
assert abs(C3 - 3.367386144928119) < 1e-12
assert abs(2*C3 - 6.734772289856238) < 1e-12

# Slab enlargement: if |Q-Q0| <= 2*Omega and |J|=L,
# then J enlarged by radius 2*Omega has length L+4*Omega.
L, Omega = 7.0, 1.25
assert abs((L + 2*(2*Omega)) - (L + 4*Omega)) < 1e-15

# Robust graph threshold: three nonedges each contribute <= L/12,
# hence Omega_jkl <= L/4 and the density-factor inflation is at most 2.
assert 3*(L/12) == L/4
assert (L + 4*(L/4))/L == 2

print('QFORM_B13_R25_ROBUST_GRAPH_CHECK_PASS')
print('C3=', repr(C3))
print('2C3=', repr(2*C3))
print('(2C3)^3=', repr((2*C3)**3))
print('216sqrt2=', repr(216*math.sqrt(2)))
