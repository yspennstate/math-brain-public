"""T250 (agent A, 18 Oct): deterministic step. For 2x2 Grams G = [[r1^2, r1 r2 cos th], [., r2^2]] and Gbar likewise,
test   ||G^(1/2) - Gbar^(1/2)||_F <= A (|r1 - rb1| + |r2 - rb2|) + B sqrt(r1 r2) |th - thb| / sqrt(th + thb)  (candidate)
and the simpler   ||G^(1/2) - Gbar^(1/2)||_F <= |r1 - rb1| + |r2 - rb2| + c sqrt(rb1 rb2) |th - thb|/sqrt(thb)  near thb small.
Find the best constants by random search."""
import numpy as np
rng = np.random.default_rng(0)
def root(r1, r2, th):
    G = np.array([[r1 * r1, r1 * r2 * np.cos(th)], [r1 * r2 * np.cos(th), r2 * r2]])
    w, V = np.linalg.eigh(G); return (V * np.sqrt(np.clip(w, 0, None))) @ V.T
# Exact geometry: G^(1/2) for vectors u1, u2 of lengths r and angle th: Gram root of [u1 u2]. Write X = [u1 u2] (2x2), G = X^T X,
# G^(1/2) = |X|. Polar: ||X^T X^(1/2) - Y^T Y^(1/2)||_F <= sqrt2 ||X - Y||_F^{?}  (Araki-Yamagami: || |X| - |Y| ||_F <= sqrt2 ||X - Y||_F).
worst1 = 0; worst2 = 0
for _ in range(200000):
    rb1, rb2 = np.exp(rng.uniform(-1, 1, 2)); thb = np.exp(rng.uniform(-8, np.log(np.pi / 2)))
    r1 = rb1 * np.exp(rng.normal(0, 0.2)); r2 = rb2 * np.exp(rng.normal(0, 0.2)); th = min(np.pi / 2, thb * np.exp(rng.normal(0, 0.3)))
    lhs = np.linalg.norm(root(r1, r2, th) - root(rb1, rb2, thb))
    # Araki-Yamagami route: X = [[r1, r2 cos th], [0, r2 sin th]], Y likewise; || |X| - |Y| ||_F <= sqrt2 ||X - Y||_F
    X = np.array([[r1, r2 * np.cos(th)], [0, r2 * np.sin(th)]]); Y = np.array([[rb1, rb2 * np.cos(thb)], [0, rb2 * np.sin(thb)]])
    ay = np.sqrt(2) * np.linalg.norm(X - Y)
    worst1 = max(worst1, lhs / ay)
    rhs2 = abs(r1 - rb1) + abs(r2 - rb2) + max(r2, rb2) * abs(th - thb)
    worst2 = max(worst2, lhs / rhs2)
print('max lhs / (sqrt2 ||X - Y||_F) =', worst1, ' (<= 1 is Araki-Yamagami)')
print('max lhs / (|dr1| + |dr2| + rmax |dth|) =', worst2)
