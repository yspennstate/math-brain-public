import numpy as np
rng = np.random.default_rng(5)
def nuhat(eta, w, A, s):   # one partner: (2pi)^-1 int |E e^{i z L + i eta R}|^2 dz, X' ~ N(0, s^2 I)
    m = A.shape[0]
    K = np.eye(m) - 2j * eta * s**2 * A
    Kinv = np.linalg.inv(K)
    detfac = abs(np.linalg.det(K)) ** (-1.0)
    g = (w @ Kinv @ w)
    return (2*np.pi)**-1 * detfac * np.sqrt(np.pi / (s**2 * g.real))
worst = 0; n = 0
for trial in range(400):
    m = rng.integers(5, 11); nJ = rng.integers(2, m - 1)
    J = np.arange(nJ); I = np.arange(nJ, m)
    w = rng.standard_normal(m) * rng.random()
    A = rng.standard_normal((m, m)) * rng.random() * 2; A = (A + A.T) / 2
    s = 1/np.sqrt(2*np.pi) * (1 + 2 * rng.random())
    wJ = w[J]; P = np.outer(wJ, wJ) / (wJ @ wJ)
    C = A[np.ix_(I, J)] @ (np.eye(nJ) - P)
    F = np.linalg.norm(C)
    if (np.linalg.norm(C, axis=1)**2).max() > F**2 / 2: continue
    n += 1
    for eta in [0.5, 1, 2, 5, 10, 30, 100, 300]:
        b = 4 * np.pi / (np.linalg.norm(wJ) * F * eta)
        worst = max(worst, nuhat(eta, w, A, s) / b)
print(n, "cases; max nu^/bound:", round(worst, 4))
