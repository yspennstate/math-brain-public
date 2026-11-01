from fractions import Fraction

# Independent exact-rational certificate for the concrete phase-monotonicity
# sublemma in P20-I0081-LOGUNIFORM-RECTANGLE-03.
# Source report:
# proofnet24/P20-closure-log-unimodality/runs/2026-09-16/
# 2026-09-16_16-08-12__run-report.md
# creation commit 8fa1d9ecf23f1354b8d34a4f5affb7251983c096

# e > sum_{k=0}^8 1/k!.
fact = 1
e_lower = Fraction(0)
for k in range(0, 9):
    if k > 0:
        fact *= k
    e_lower += Fraction(1, fact)

assert e_lower == Fraction(109601, 40320)
assert e_lower**6 > 400

# Therefore for X>=6, a_X=e^{-X}<1/400. The Poisson-kernel minimum is
# (1-a)/(1+a), so it is strictly larger than 399/401.
poisson_lower = Fraction(399, 401)

# For L,M>=6 and csc^2(t)>=1,
# A(theta)=1/2*csc^2(t)*(L P_L + M P_M)-1
# > 1/2*12*(399/401)-1.
phase_lower = Fraction(1, 2) * 12 * poisson_lower - 1
assert phase_lower == Fraction(1993, 401)
assert phase_lower > 0

print('PASS')
print('claim_id=P20-I0081-LOGUNIFORM-RECTANGLE-03')
print('audited_sublemma=uniform unit-circle phase derivative lower bound')
print(f'e_lower=sum_0^8 1/k!={e_lower}')
print(f'e_lower^6={e_lower**6} > 400')
print(f'poisson_kernel_lower={poisson_lower}')
print(f'phase_derivative_lower={phase_lower}')
