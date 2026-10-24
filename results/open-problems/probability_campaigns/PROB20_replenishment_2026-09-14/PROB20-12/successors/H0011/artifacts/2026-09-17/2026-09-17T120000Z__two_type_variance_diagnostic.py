from fractions import Fraction as F

# Exact finite-type diagnostic for the H0011 normalization question.
# Mean matrix: a type-1 parent has exactly two type-2 children;
# a type-2 parent has one type-1 child with probability 1/2 and no child otherwise.
M = ((F(0), F(2)), (F(1, 2), F(0)))
h = (F(3, 2), F(3, 4))
pi = (F(1, 3), F(2, 3))

Mh = tuple(sum(M[i][j] * h[j] for j in range(2)) for i in range(2))
piM = tuple(sum(pi[i] * M[i][j] for i in range(2)) for j in range(2))
pi_h = sum(pi[i] * h[i] for i in range(2))
assert Mh == h
assert piM == pi
assert pi_h == 1

# h-tilted stationary type law varpi_*(i) = pi_i h_i.
varpi = tuple(pi[i] * h[i] for i in range(2))
assert varpi == (F(1, 2), F(1, 2))
assert sum(varpi) == 1

# Ordinary child count C under varpi_*.
# Type 1: C=2 surely. Type 2: C~Bernoulli(1/2).
EC = varpi[0] * 2 + varpi[1] * F(1, 2)
EC2 = varpi[0] * 4 + varpi[1] * F(1, 2)
varC = EC2 - EC * EC
assert EC == F(5, 4)
assert varC == F(11, 16)

# Perron pair variance v_i = E_i sum_{r != s} h(type_r) h(type_s).
# Type 1 has two deterministic type-2 children; type 2 has at most one child.
v = (2 * h[1] * h[1], F(0))
pi_v = sum(pi[i] * v[i] for i in range(2))
assert v == (F(9, 8), F(0))
assert pi_v == F(3, 8)

# The standard fixed-mass Brownian-CRT distance coefficient is sqrt(pi(v))/2,
# so its square is pi(v)/4. A naive scalar-count coefficient based on
# Var_{varpi_*}(C) would instead have square varC/4; they are unequal.
intrinsic_scale_sq = pi_v / 4
naive_scalar_scale_sq = varC / 4
assert intrinsic_scale_sq == F(3, 32)
assert naive_scalar_scale_sq == F(11, 64)
assert intrinsic_scale_sq != naive_scalar_scale_sq

print('M h =', Mh)
print('pi M =', piM)
print('pi(h) =', pi_h)
print('varpi_* =', varpi)
print('E_varpi[C] =', EC)
print('Var_varpi(C) =', varC)
print('v =', v)
print('pi(v) =', pi_v)
print('intrinsic scale^2 = pi(v)/4 =', intrinsic_scale_sq)
print('naive scalar scale^2 = Var(C)/4 =', naive_scalar_scale_sq)
print('ALL EXACT CHECKS PASSED')
