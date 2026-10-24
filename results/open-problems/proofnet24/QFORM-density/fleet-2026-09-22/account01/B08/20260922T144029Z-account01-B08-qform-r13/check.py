import math


def kappa(m):
    return math.sqrt(m*(m+1)/8.0)


def q1_threshold(m):
    k = kappa(m)
    return 1.0/(2.0*(2.0+k))


def qstar_threshold(m):
    k = kappa(m)
    return 3.0/(2.0*(4.0+3.0*k))


def floating_alpha(m, delta):
    return 0.5-kappa(m)*delta

print('finite-rank floating thresholds')
for m in range(4, 19):
    print(m, f'kappa={kappa(m):.12f}', f'q1={q1_threshold(m):.12f}', f'qstar={qstar_threshold(m):.12f}')

m = 4
delta = 1.0/8.0
alpha = floating_alpha(m, delta)
leverage_ratio = delta/alpha
C = 3.0*math.e/(math.sqrt(2.0)*alpha)
print('rank4 delta=1/8')
print(f'alpha={alpha:.15f}')
print(f'delta/alpha={leverage_ratio:.15f}')
print(f'q=1 density constant={C:.15f}')

assert alpha > 0
assert leverage_ratio < 0.5
assert abs(alpha - (8.0-math.sqrt(10.0))/16.0) < 1e-15
assert qstar_threshold(4) > 1.0/8.0

# At delta=1/16, q=1 remains available through rank 16.
for m in range(4, 17):
    a = floating_alpha(m, 1.0/16.0)
    assert (1.0/16.0)/a <= 0.5 + 1e-14

# Rank 18 still lies in the general q<3/2 floating regime at delta=1/16.
assert 1.0/16.0 < qstar_threshold(18)
print('all checks passed')
