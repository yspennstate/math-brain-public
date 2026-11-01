import math
import numpy as np

SEED = 20260922
TRIALS = 1000

def check(seed=SEED, trials=TRIALS):
    rng = np.random.default_rng(seed)
    max_det_err = 0.0
    max_wedge_err = 0.0
    max_q_err = 0.0
    for _ in range(trials):
        n = int(rng.integers(3, 25))
        M = rng.normal(size=(n, 2))
        Q, _ = np.linalg.qr(M)

        ang = float(rng.uniform(0, 2 * np.pi))
        O = np.array([[math.cos(ang), -math.sin(ang)],
                      [math.sin(ang),  math.cos(ang)]])
        vals = np.diag([float(rng.uniform(.1, 4)),
                        -float(rng.uniform(.1, 4))])
        S = O @ vals @ O.T

        norms = np.sum(Q * Q, axis=1)
        i = int(rng.choice(np.where(norms > 1e-10)[0]))
        b = Q[i].copy()
        r = float(np.linalg.norm(b))
        c = np.array([-b[1], b[0]]) / (r * r)
        T = np.column_stack([b, c])
        G = T.T @ S @ T
        max_det_err = max(max_det_err,
                          abs(float(np.linalg.det(G) - np.linalg.det(S))))

        wedges = np.array([
            np.linalg.det(np.stack([b, Q[j]])) for j in range(n)
        ])
        max_wedge_err = max(max_wedge_err,
                            abs(float(np.dot(wedges, wedges) - r * r)))

        x = rng.normal(size=n)
        theta = rng.normal(size=2)
        Z = theta + sum((Q[j] * x[j] for j in range(n) if j != i),
                        np.zeros(2))
        w = float(np.linalg.det(np.stack([b, Z])))
        s = float(np.dot(Z - w * c, b) / (r * r))
        u = float(x[i] + s)
        y = theta + Q.T @ x
        y2 = b * u + c * w
        q1 = float(y @ S @ y)
        q2 = float(y2 @ S @ y2)
        max_q_err = max(max_q_err, abs(q1 - q2))

    C_ind = 8 * 3**(3/4) * 5**(1/4) / math.sqrt(math.e)
    C_heavy = 2**(1/4) * C_ind
    C_eta32 = C_heavy * 32**(1/4)
    C_bank_eta32 = math.sqrt(2) * C_eta32
    C_null_eta32 = 8 * 2**(1/4) * 32**(1/4)
    return {
        "seed": seed,
        "trials": trials,
        "max_det_err": max_det_err,
        "max_wedge_err": max_wedge_err,
        "max_q_err": max_q_err,
        "C_ind": C_ind,
        "C_heavy": C_heavy,
        "C_eta32": C_eta32,
        "C_bank_eta32": C_bank_eta32,
        "C_null_eta32": C_null_eta32,
    }

if __name__ == "__main__":
    out = check()
    for k, v in out.items():
        print(f"{k}={v}")
    assert out["max_det_err"] < 1e-10
    assert out["max_wedge_err"] < 1e-10
    assert out["max_q_err"] < 1e-10
    print("PASS")
