import itertools
import numpy as np

rng = np.random.default_rng(0)
m = 6
S = rng.normal(size=(m, m))
S = (S + S.T) / 2
pairs = list(itertools.combinations(range(m), 2))

# Ordered disjoint 2x2-minor volume.
D = 0.0
for P in pairs:
    for T in pairs:
        if set(P).isdisjoint(T):
            D += np.linalg.det(S[np.ix_(P, T)]) ** 2

# Exact average over all Bernoulli physical cuts.
zs = []
for mask in range(1 << m):
    I = [j for j in range(m) if (mask >> j) & 1]
    J = [j for j in range(m) if not ((mask >> j) & 1)]
    z = 0.0
    if len(I) >= 2 and len(J) >= 2:
        M = S[np.ix_(I, J)]
        for P0 in itertools.combinations(range(len(I)), 2):
            for T0 in itertools.combinations(range(len(J)), 2):
                z += np.linalg.det(M[np.ix_(P0, T0)]) ** 2
    zs.append(z)

print("D", D)
print("mean_cut_Z2", np.mean(zs))
print("D_over_16", D / 16)
print("cut_identity_error", abs(np.mean(zs) - D / 16))

# Bordered determinant identity det A[{i}U P,{i}U T] = d det S[P,T].
d = 1.7
a = rng.normal(size=m)
A = np.empty((m + 1, m + 1))
A[0, 0] = d
A[0, 1:] = a
A[1:, 0] = a
A[1:, 1:] = S + np.outer(a, a) / d

maxerr = 0.0
W = 0.0
for P0 in pairs:
    for T0 in pairs:
        if set(P0).isdisjoint(T0):
            P = [x + 1 for x in P0]
            T = [x + 1 for x in T0]
            detA = np.linalg.det(A[np.ix_([0] + P, [0] + T)])
            detS = np.linalg.det(S[np.ix_(P0, T0)])
            maxerr = max(maxerr, abs(detA - d * detS))
            W += detA ** 2

print("border_max_abs_error", maxerr)
print("W", W)
print("d2D", d * d * D)
print("volume_identity_error", abs(W - d * d * D))

Cstar = 16 * np.e ** 0.25
print("Cstar", Cstar)
print("Cstar_sqrt2", Cstar * np.sqrt(2))
print("low_branch_universal_factor", 16 * Cstar ** 8)
