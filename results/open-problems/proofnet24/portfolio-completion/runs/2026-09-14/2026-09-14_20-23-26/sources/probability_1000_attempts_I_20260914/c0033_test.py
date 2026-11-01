"""C0033 (Lyons, Conjecture 2.6): for positive contractions Q1, Q2 on l^2(E), E finite,
Ent(P_{(Q1+Q2)/2}) >= (Ent(P_{Q1}) + Ent(P_{Q2}))/2, where P_Q is the determinantal probability measure with kernel Q:
P_Q(X = S) = det(Q_S^S) with the (Borodin-Rains) formula P(X = S) = det( K^{(S)} ), K^{(S)} = K with columns j notin S replaced by columns of I - K.
Random search for a violation at |E| = 2..5."""
import numpy as np, itertools, sys
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
def entropy(K):
    n = K.shape[0]; H = 0.0; tot = 0.0
    for r in range(n + 1):
        for S in itertools.combinations(range(n), r):
            M = np.array(K, dtype=float)
            for j in range(n):
                if j not in S: M[:, j] = (np.eye(n)[:, j] - K[:, j])
            p = np.linalg.det(M)
            tot += p
            if p > 1e-15: H -= p * np.log(p)
    assert abs(tot - 1) < 1e-8, tot
    return H
def rand_contraction(n):
    kind = rng.integers(0, 3)
    U, _ = np.linalg.qr(rng.normal(size=(n, n)))
    if kind == 0: ev = rng.uniform(0, 1, n)
    elif kind == 1: ev = rng.choice([0.0, 1.0], n) * rng.uniform(0.9, 1.0, n) + rng.uniform(0, 0.1, n) * 0  # near projections
    else: ev = rng.beta(0.3, 0.3, n)
    return U @ np.diag(np.clip(ev, 0, 1)) @ U.T
worst = (np.inf, None)
for t in range(int(sys.argv[2]) if len(sys.argv) > 2 else 20000):
    n = rng.integers(2, 6)
    Q1 = rand_contraction(n); Q2 = rand_contraction(n)
    gap = entropy((Q1 + Q2) / 2) - (entropy(Q1) + entropy(Q2)) / 2
    if gap < worst[0]: worst = (gap, (Q1.round(5), Q2.round(5)))
print("min midpoint-concavity gap over trials:", worst[0], "(conjecture needs >= 0)")
print(worst[1][0]); print(worst[1][1])

