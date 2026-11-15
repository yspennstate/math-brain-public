# Independent check of P0347 means/variances for the critical beta-splitting tree.
# Split of a clade of size m into (i, m-i) with prob m/(2 h_{m-1} i (m-i)), 1<=i<=m-1.
# Tolls: Sackin m, Colless |2i-m|, quadratic Colless (2i-m)^2. Variance by total variance.
import numpy as np, math, sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
mu = {k: np.zeros(N + 1) for k in 'SCQ'}
va = {k: np.zeros(N + 1) for k in 'SCQ'}
h = 0.0
for m in range(2, N + 1):
    h += 1.0 / (m - 1)
    i = np.arange(1, m)
    p = m / (2 * h * i * (m - i))
    t = {'S': np.full(m - 1, float(m)), 'C': np.abs(2.0 * i - m), 'Q': (2.0 * i - m) ** 2}
    for k in 'SCQ':
        a = t[k] + mu[k][i] + mu[k][m - i]
        e = p @ a
        mu[k][m] = e
        va[k][m] = p @ (va[k][i] + va[k][m - i]) + p @ (a - e) ** 2
z = math.pi ** 2 / 6; g = 0.5772156649015329; z3 = 1.2020569031595942
b = g / z + z3 / z ** 2; kap = (2 * z3 - z) / z ** 2
for n in [500, 1000, 2000, N]:
    L = math.log(n)
    rS = (mu['S'][n] - n * L * L / (2 * z) - b * n * L) / n
    rC = (mu['C'][n] - n * L * L / (2 * z) - (b - 2 * math.log(2) / z) * n * L) / n
    print(n, 'ES', mu['S'][n], 'O(n)remS', round(rS, 4), 'remC', round(rC, 4),
          'EQ/n2L', mu['Q'][n] / (n * n * L),
          'VS/kn2L2', va['S'][n] / (kap * n * n * L * L), 'VC/kn2L2', va['C'][n] / (kap * n * n * L * L),
          'VQ/(2/11 n4L2)', va['Q'][n] / (2 / 11 * n ** 4 * L * L))
print('n=%d means' % N, mu['S'][N], mu['C'][N], mu['Q'][N])
print('n=%d vars ' % N, va['S'][N], va['C'][N], va['Q'][N])
