from fractions import Fraction as F

# Exact arithmetic for the canonical one-sided periodic barrier in R07 run 16.
# Gate data: eta=1/4, gate boundary b=-5, comparison half-line (-infinity,-4],
# gate duty cycle tau/P = 3/5.
eta = F(1, 4)
A = F(4, 1)
tau = F(3, 5)
P = F(1, 1)
b_gate = F(-5, 1)
comparison_boundary = F(-4, 1)

# Ground-state-transform lower bound for the OU Dirichlet eigenvalue on (-infinity,-A]:
# lambda_A >= A^2/8 - 1/4.
lambda_lower = A*A/F(8,1) - F(1,4)
kappa_lower = (tau/P) * lambda_lower
padded_gate_boundary = b_gate + 2*eta

assert lambda_lower == F(7,4)
assert kappa_lower == F(21,20)
assert kappa_lower > 1
assert padded_gate_boundary == F(-9,2)
assert padded_gate_boundary <= comparison_boundary

print('PASS')
print('lambda_lower=', lambda_lower)
print('kappa_lower=', kappa_lower)
print('padded_gate_boundary=', padded_gate_boundary)
print('comparison_boundary=', comparison_boundary)
