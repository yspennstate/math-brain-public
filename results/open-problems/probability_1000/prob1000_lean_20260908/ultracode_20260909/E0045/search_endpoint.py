# Search for a counterexample to the endpoint case (d = p-1) of the Mallat-Zeitouni conjecture:
#   E min_i (T Y)_i^2  >=  E min_i Y_i^2   for Y ~ N(0, diag(sigma)), T orthogonal.
# Method: common-random-numbers Monte Carlo objective, minimised over T by gradient descent on
# a skew-symmetric parametrisation T = expm(A) (Cayley/expm), soft-min smoothing, many restarts.
import numpy as np, sys, time
from scipy.linalg import expm
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv)>1 else 0)

def emin(C, Z):
    # Z: (n, N) standard normals; C covariance; returns E min_i X_i^2 estimate
    L = np.linalg.cholesky(C + 1e-14*np.eye(len(C)))
    X = Z @ L.T
    return np.min(X**2, axis=1).mean()

def objective_and_grad(A, sig, Z, beta):
    # T = expm(A), X = T Y, Y = sqrt(sig) * Z.  soft-min via -log-sum-exp(-beta x^2)/beta
    N = len(sig)
    T = expm(A)
    Y = Z * np.sqrt(sig)
    X = Y @ T.T            # (n, N)
    Q = X**2
    m = Q.min(axis=1, keepdims=True)
    w = np.exp(-beta*(Q - m)); w /= w.sum(axis=1, keepdims=True)   # softmin weights
    val = (m[:,0] - np.log(np.exp(-beta*(Q-m)).sum(axis=1))/beta).mean()
    # d val / d X = 2 w X / n ; d val/dT = (dval/dX)^T Y
    G = (2*w*X).T @ Y / len(Z)   # (N,N) gradient wrt T
    # gradient wrt A through expm: use first-order T ~ (I + A) near solution -> project: dA = skew(T^T G)... use Riemannian gradient
    R = T.T @ G
    dA = (R - R.T)/2
    return val, T, dA

def riemann_descent(sig, Z, steps=300, lr=0.05, beta=30.0, A0=None):
    N = len(sig)
    T = np.eye(N) if A0 is None else expm(A0)
    best = (np.inf, None)
    for k in range(steps):
        Y = Z*np.sqrt(sig); X = Y @ T.T; Q = X**2
        m = Q.min(axis=1, keepdims=True)
        E = np.exp(-beta*(Q-m)); w = E/E.sum(axis=1, keepdims=True)
        val = (m[:,0] - np.log(E.sum(axis=1))/beta).mean()
        G = (2*w*X).T @ Y / len(Z)
        R = T.T @ G; S = (R - R.T)/2       # skew part = Riemannian gradient in Lie algebra
        T = T @ expm(-lr*S)
        hard = np.min(Q,axis=1).mean()
        if hard < best[0]: best = (hard, T.copy())
    return best

N = int(sys.argv[2]) if len(sys.argv)>2 else 6
n = 20000
Z = rng.standard_normal((n, N))
results = []
t0=time.time()
for trial in range(40):
    kind = trial % 4
    if kind==0: sig = np.sort(rng.uniform(0.05,1,N))[::-1]
    elif kind==1: sig = np.array([1.0]*(N-1)+[rng.uniform(0.01,0.9)])
    elif kind==2: sig = np.array([rng.uniform(1.5,10)]+[1.0]*(N-1))
    else: sig = np.exp(-rng.uniform(0,3)*np.arange(N))
    sig = sig/sig.max()
    base = np.min((Z*np.sqrt(sig))**2,axis=1).mean()
    A0 = rng.standard_normal((N,N)); A0 = (A0-A0.T)*rng.uniform(0.1,1.5)
    val, T = riemann_descent(sig, Z, A0=A0)
    # also start from identity with a small kick
    A1 = rng.standard_normal((N,N)); A1=(A1-A1.T)*0.1
    val1, T1 = riemann_descent(sig, Z, A0=A1)
    if val1 < val: val, T = val1, T1
    ratio = val/base
    results.append((ratio, sig, T))
    print(f"trial {trial:2d} kind {kind} sig={np.round(sig,3)} base={base:.5f} best={val:.5f} ratio={ratio:.4f}", flush=True)
print("min ratio over trials:", min(r[0] for r in results), "time", time.time()-t0)
i = int(np.argmin([r[0] for r in results]))
np.save("worst_T_N%d.npy"%N, results[i][2]); np.save("worst_sig_N%d.npy"%N, results[i][1])
