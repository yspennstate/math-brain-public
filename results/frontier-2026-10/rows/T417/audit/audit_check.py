# Independent check (own code, not hb_ms_*.py) for the T417 audit.
# Heavy ball on Gaussian streaming least squares, H = diag(h), batch B: per mode j the state (a, x, c) =
# (E e_t^2, E e_t e_{t-1}, E e_{t-1}^2) evolves by a' = k^2 a + (eta^2/B)(h^2 a + h (h.a)) - 2 beta k x + beta^2 c, x' = k a - beta x,
# c' = a, k = 1 + beta - eta h.  Checks:
#  (1) AR(2) identity: sum_t g(t)^2 = (1+beta)/((1-beta) eta h (2(1+beta) - eta h)) for the impulse response of r^2-(1+beta-eta h)r+beta.
#  (2) renewal necessity: mean-square stable  =>  S0 = (eta/B) sum_j (1+beta) h_j / ((1-beta)(2(1+beta) - eta h_j)) < 1.
#  (3) the spectral radius of the 3d map is attained by a REAL POSITIVE eigenvalue (Pringsheim).
import numpy as np
rng = np.random.default_rng(41)
def msmap(h, eta, beta, B):
    d = len(h); M = np.zeros((3 * d, 3 * d)); k = 1 + beta - eta * h
    for j in range(d):
        a, x, c = 3 * j, 3 * j + 1, 3 * j + 2
        M[a, a] += k[j] ** 2 + eta ** 2 / B * h[j] ** 2; M[a, x] = -2 * beta * k[j]; M[a, c] = beta ** 2
        for l in range(d): M[a, 3 * l] += eta ** 2 / B * h[j] * h[l]
        M[x, a] = k[j]; M[x, x] = -beta; M[c, a] = 1.0
    return M
e1 = 0
for t in range(300):
    beta = rng.random() * 0.99; s = rng.random() * 2 * (1 + beta)
    k = 1 + beta - s; g = [1.0, k]
    for _ in range(20000): g.append(k * g[-1] - beta * g[-2])
    G = np.sum(np.array(g) ** 2)
    if abs(g[-1]) < 1e-12: e1 = max(e1, abs(G / ((1 + beta) / ((1 - beta) * s * (2 * (1 + beta) - s))) - 1))
print("(1) AR(2) sum g^2 identity: max rel err %.1e" % e1)
n_st = viol2 = viol3 = 0; worst3 = 0
for t in range(4000):
    d = int(rng.integers(1, 12)); h = np.sort(10.0 ** (-3 * rng.random(d)))[::-1]
    B = float(rng.choice([1, 2, 5, 10, 100, 1000])); beta = rng.random() ** 0.3 * 0.999
    eta = rng.random() * 2 * (1 + beta) / h[0]
    ev = np.linalg.eigvals(msmap(h, eta, beta, B)); r = np.abs(ev).max()
    top = ev[np.argmax(np.abs(ev) - 1e-9 * (ev.real > 0))]
    real_pos = ev[(abs(ev.imag) < 1e-9) & (ev.real > 0)]
    gap = r - (real_pos.real.max() if len(real_pos) else -1)
    worst3 = max(worst3, gap / r); viol3 += gap > 1e-7 * r
    if r < 1:
        n_st += 1; br = (1 - beta) * (2 * (1 + beta) - eta * h)
        S0 = np.inf if (br <= 0).any() else eta / B * np.sum((1 + beta) * h / br)
        viol2 += not (S0 < 1)
print("(2) stable points %d, of them with S0 >= 1: %d" % (n_st, viol2))
print("(3) points where the radius is not a real positive eigenvalue: %d of 4000 (max relative gap %.1e)" % (viol3, worst3))
