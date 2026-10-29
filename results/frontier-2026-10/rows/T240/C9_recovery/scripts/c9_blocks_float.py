"""Float preview of the block tube (no intervals): v' = A(t) v along the float path from the exit face."""
import numpy as np, fdrive, math
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from scipy.optimize import fsolve
x0 = np.array([0.3677, 0.3254, 0.3677, 0.4144, 0.4144, 0.4144, 0.4144])
xs = fsolve(lambda z: fdrive.f(z, 0.5), x0, xtol=1e-14)
J = fdrive.jac(xs, 0.5); w, V = np.linalg.eig(J); o = np.argsort(-w.real); V = np.real(V[:, o]); V /= np.linalg.norm(V, axis=0)
for U, kap in [(2e-4, 0.1), (1e-4, 0.05)]:
    p0 = xs + U * V[:, 0]
    sol = solve_ivp(lambda t, y: fdrive.f(y, 0.5), (0, 900), p0, method='DOP853', rtol=1e-12, atol=1e-14, dense_output=True)
    v = np.array([1e-9] + [kap * U] * 6); r = np.linalg.norm(v); h = 1.0
    P = V; Pi = np.linalg.inv(P)
    for k in range(900):
        x = sol.sol(k * h)
        Jx = fdrive.jac(x, 0.5)
        w2, V2 = np.linalg.eig(Jx)
        if np.max(np.abs(w2.imag)) > 1e-9: print('complex at t', k); break
        o2 = np.argsort(-w2.real); P2 = np.real(V2[:, o2]); P2 /= np.linalg.norm(P2, axis=0); Pi2 = np.linalg.inv(P2)
        T = np.abs(Pi2 @ P); v = T @ v; P, Pi = P2, Pi2          # frame switch
        M = Pi @ Jx @ P; A = np.abs(M); np.fill_diagonal(A, np.diag(M)); v = expm(A * h) @ v
        Ms = (M + M.T) / 2; r = r * np.linalg.norm(Pi2 @ P) if False else r
        r = r * math.exp(np.linalg.eigvalsh(Ms).max() * h)
        if k % 75 == 0 or k == 899: print(U, kap, 't', k, 'dist_teacher %.2e' % np.linalg.norm(x - np.array([1, 0, 1, 1, 0, 0, 1])), 'block |v| %.2e' % np.linalg.norm(v), 'ball %.2e' % r, 'v_u %.1e' % v[0])
