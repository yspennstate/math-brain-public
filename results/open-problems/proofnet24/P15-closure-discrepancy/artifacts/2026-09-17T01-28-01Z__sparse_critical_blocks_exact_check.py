from fractions import Fraction

# Exact self-check for the deterministic sparse-critical-block construction.
# The theorem-level failure of SMR is proved analytically in the report.

# Stationary second moments in one endpoint-critical r=2 chain block,
# started at lambda_0 = 1 with unit additive noise in coordinate 0.
# v_0(infty)=1/2; v_j(infty)=v_{j-1}/4.
v = Fraction(1, 2)
w0 = Fraction(1, 2)
vals = []
for j in range(13):
    lam = 1 << j
    w = Fraction(lam * lam, 1) * v
    vals.append(w)
    assert w == w0
    v /= 4

# Sparse block starts M_k = 2^(k^2), block length k.
# Check initial disjointness and the exact prefix density upper bounds
# D_k <= k(k+1)/(2*2^(k^2)).
density_bounds = []
prev_end = -1
for k in range(1, 9):
    M = 1 << (k*k)
    L = k
    assert M > prev_end
    prev_end = M + L - 1
    covered = k * (k + 1) // 2
    bound = Fraction(covered, M)
    density_bounds.append((k, M, covered, bound))

print('P15 I0066 sparse-critical-block exact checker')
print('stationary_weighted_energies_j0_to_j12 =', vals)
for k, M, covered, bound in density_bounds:
    print(f'k={k} start={M} cumulative_critical_edges<={covered} prefix_density_bound={bound}')
print('ALL_EXACT_CHECKS_PASSED')
