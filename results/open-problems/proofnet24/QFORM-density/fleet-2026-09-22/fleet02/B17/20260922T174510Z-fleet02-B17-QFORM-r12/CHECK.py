import math
import numpy as np


def main():
    tol = 1e-10
    W = np.array([
        [1, 1, 1],
        [1, -1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
    ], dtype=float) / 2.0
    J = np.diag([1.0, 1.0, -1.0])

    assert np.linalg.norm(W.T @ W - np.eye(3), ord=2) < tol
    assert np.allclose(np.linalg.eigvalsh(W @ J @ W.T), [-1, 0, 1, 1], atol=tol)

    rows = []
    for m in [1, 2, 7, 19]:
        R = np.repeat(W / math.sqrt(m), m, axis=0)
        assert np.linalg.norm(R.T @ R - np.eye(3), ord=2) < 1e-9
        eigs = np.linalg.eigvalsh(R @ J @ R.T)
        nz = eigs[np.abs(eigs) > 1e-8]
        assert np.allclose(nz, [-1, 1, 1], atol=1e-8)

        rng = np.random.default_rng(100 + m)
        q = rng.uniform(0.0, 1.0, R.shape[0])
        p = 1.0 - q
        lhs = np.zeros((3, 3))
        err = np.zeros((3, 3))
        for i in range(R.shape[0]):
            outer = np.outer(R[i], R[i])
            lhs += p[i] ** 3 * outer
            err += q[i] * outer
        rhs = np.eye(3) - 3.0 * err
        assert np.min(np.linalg.eigvalsh(lhs - rhs)) > -1e-9

        delta2 = np.max(np.sum(R * R, axis=1))
        envelope = delta2 * np.sum(q)
        err_op = np.linalg.norm(err, ord=2)
        assert err_op <= envelope + 1e-10
        rows.append((m, delta2, err_op, envelope))

    # Equality cases for the scalar subprobability variance floor:
    # density M on a centered interval of length p/M.
    for p0, M in [(0.37, 5.0), (0.9, 1.7), (1.0, 1.0)]:
        a = p0 / (2.0 * M)
        second = M * 2.0 * a ** 3 / 3.0
        target = p0 ** 3 / (12.0 * M ** 2)
        assert abs(second - target) < 1e-14

    c = 3.0 * math.sqrt(2.0)
    gamma = (63.0 + 6.0 * math.sqrt(38.0)) / 160.0
    assert abs(c - 4.242640687119285) < 2e-15
    assert abs(gamma - 0.6249155251113366) < 2e-15

    print('PASS')
    for m, delta2, err_op, envelope in rows:
        print(f'm={m} delta2={delta2:.12g} err_op={err_op:.12g} envelope={envelope:.12g}')
    print(f'3sqrt2={c:.15f}')
    print(f'gamma*={gamma:.15f}')


if __name__ == '__main__':
    main()
