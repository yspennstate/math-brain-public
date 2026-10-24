import math
import numpy as np


def sylvester(n: int) -> np.ndarray:
    H = np.array([[1.0]])
    while H.shape[0] < n:
        H = np.block([[H, H], [H, -H]])
    assert H.shape == (n, n)
    return H


def check(N: int):
    assert N >= 8 and (N & (N - 1)) == 0 and N % 4 == 0
    m = N // 4
    H = sylvester(N)
    B = H[:, [0, 1, 2]] / math.sqrt(N)
    assert np.max(np.abs(B.T @ B - np.eye(3))) < 1e-12

    patterns = {}
    for row in H[:, [0, 1, 2]].astype(int):
        patterns[tuple(row)] = patterns.get(tuple(row), 0) + 1
    expected = {(1,1,1):m, (1,1,-1):m, (1,-1,1):m, (1,-1,-1):m}
    assert patterns == expected

    A = np.block([[np.zeros((N, N)), B], [B.T, np.zeros((3, 3))]])
    eig = np.linalg.eigvalsh(A)
    nonzero = eig[np.abs(eig) > 1e-8]
    assert len(nonzero) == 6
    assert np.max(np.abs(np.sort(nonzero) - np.array([-1.,-1.,-1.,1.,1.,1.]))) < 1e-10

    u = np.ones(3)
    P = np.outer(u, u) / 3.0
    light = B[np.any(H[:, [0, 1, 2]].astype(int) != np.array([1,1,1]), axis=1)]
    C = light @ (np.eye(3) - P)

    pos_dets = []
    incid = np.zeros(C.shape[0])
    for i in range(C.shape[0]):
        for j in range(i + 1, C.shape[0]):
            G = C[[i,j]] @ C[[i,j]].T
            d = float(np.linalg.det(G))
            if d > 1e-12:
                pos_dets.append(d)
                incid[i] += 1
                incid[j] += 1

    target_D = 1.0 / (3.0 * m * m)
    assert len(pos_dets) == 3 * m * m
    assert max(abs(d - target_D) for d in pos_dets) < 1e-12
    alpha = incid / len(pos_dets)
    assert np.max(np.abs(alpha - 2.0/(3.0*m))) < 1e-12

    gamma = target_D * math.exp(-np.sum(alpha * np.log(alpha)))
    assert abs(gamma - 0.75) < 1e-12

    new_constant = 4.0 * 3.0**(2.0/3.0)
    peer_constant = 3.0 * (1.0 - 3.0/N)**(-(N-3.0)/6.0)
    assert peer_constant < 3.0 * math.sqrt(math.e)

    return {
        "N": N,
        "m": m,
        "positive_pair_count": len(pos_dets),
        "positive_pair_D": target_D,
        "row_marginal": float(alpha[0]),
        "Gamma_star": gamma,
        "new_projected_crossing_constant": new_constant,
        "peer_exact_marginal_constant": peer_constant,
    }


if __name__ == "__main__":
    for N in (8, 16, 32):
        print(check(N))
