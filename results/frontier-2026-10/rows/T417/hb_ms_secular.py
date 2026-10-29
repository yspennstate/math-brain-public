"""T417 Target 2 (agent A, 18 Oct 2026): the secular equation of the mean-square map and its stability edge.
Per mode the map is a 3x3 block M_j plus the rank-one coupling (eta^2/B) h h' on the a-coordinates, so an eigenvalue mu of the
whole map that is not an eigenvalue of any M_j solves
    1 = (eta^2/B) sum_j h_j^2 mu (mu + beta) / p_j(mu),   p_j(mu) = det(mu I - M_j),
and at mu = 1 this becomes the exact mean-square stability condition
    S = (eta/B) sum_j (1+beta) h_j / [ (1-beta)(2(1+beta) - eta h_j) - (1+beta) eta h_j / B ]  <  1   (each bracket > 0).
Checks: (1) the leading real eigenvalue of the full map solves the secular equation; (2) S < 1 agrees with rho < 1 on random points.
usage: hb_ms_secular.py trials"""
import sys, numpy as np
from hb_ms_radius import rho


def full(h, eta, beta, B):
    d = len(h); kb = 1 + beta - eta * h
    A = np.zeros((3 * d, 3 * d)); I = np.arange(d)
    A[I, I] = kb ** 2 + eta ** 2 / B * h ** 2
    A[:d, :d] += eta ** 2 / B * np.outer(h, h)
    A[I, d + I] = -2 * beta * kb; A[I, 2 * d + I] = beta ** 2
    A[d + I, I] = kb; A[d + I, d + I] = -beta
    A[2 * d + I, I] = 1.0
    return A


def secular(mu, h, eta, beta, B):
    kb = 1 + beta - eta * h
    p = []
    for k, hj in zip(kb, h):
        M = np.array([[k * k + eta ** 2 / B * hj * hj, -2 * beta * k, beta ** 2], [k, -beta, 0], [1, 0, 0]])
        p.append(np.linalg.det(mu * np.eye(3) - M))
    return 1 - eta ** 2 / B * np.sum(h ** 2 * mu * (mu + beta) / np.array(p))


def S(h, eta, beta, B):
    den = (1 - beta) * (2 * (1 + beta) - eta * h) - (1 + beta) * eta * h / B
    return np.inf if np.any(den <= 0) else eta / B * np.sum((1 + beta) * h / den)


if __name__ == "__main__":
    rng = np.random.default_rng(417); T = int(sys.argv[1]); worst = 0.0; agree = 0; n = 0
    for t in range(T):
        d = rng.integers(2, 12); h = np.sort(rng.uniform(0.01, 1, d))[::-1]; B = int(rng.integers(1, 50))
        beta = rng.uniform(0, 0.99); eta = rng.uniform(0, 2 * (1 + beta) / h[0])
        ev = np.linalg.eigvals(full(h, eta, beta, B)); r = max(abs(ev)); lead = ev[np.argmax(abs(ev))]
        if abs(lead.imag) < 1e-12 and lead.real > 0: worst = max(worst, abs(secular(lead.real, h, eta, beta, B))); n += 1
        agree += ((S(h, eta, beta, B) < 1) == (r < 1))
    print(f"{T} random points: secular residual at the leading real eigenvalue max {worst:.2e} over {n} points; "
          f"S<1 iff rho<1 on {agree}/{T}")
