"""lim_{eta->0} lambda/eta at the symmetric plateau for K = M erf committees (orthonormal teachers, output weights 1).
All students equal r * sum_n v_n on the plateau; r solves d eps/dr = 0; lambda/eta = -(smallest Hessian eigenvalue)
of eps in the K^2 coordinates w_i . v_n. usage: python lam_closed_K.py Kmax"""
import sys
import sympy as sp

for K in range(int(sys.argv[2]) if len(sys.argv) > 2 else 2, int(sys.argv[1]) + 1):
    X = sp.Matrix(K, K, lambda i, n: sp.Symbol('x%d_%d' % (i, n), real=True))
    def G(u, w):
        return sp.asin(u.dot(w) / sp.sqrt((1 + u.dot(u)) * (1 + w.dot(w))))
    rows = [X.row(i) for i in range(K)]
    eye = [sp.eye(K).row(n) for n in range(K)]
    eps = (sum(G(rows[i], rows[k]) for i in range(K) for k in range(K)) + K * sp.pi / 2
           - 2 * sum(G(rows[i], eye[n]) for i in range(K) for n in range(K))) / sp.pi
    r = sp.Symbol('r', positive=True)
    sym = {X[i, n]: r for i in range(K) for n in range(K)}
    er = sp.simplify(eps.subs(sym))
    sols = [s for s in sp.solve(sp.diff(er, r), r) if s.is_real and s > 0]
    xs = list(X)
    for r0 in sols:
        H = sp.Matrix(len(xs), len(xs), lambda i, j: sp.diff(eps, xs[i], xs[j]).subs(sym).subs(r, r0))
        import numpy as np
        Hn = np.array(H.evalf(20).tolist(), dtype=float)
        lo = float(np.linalg.eigvalsh((Hn + Hn.T) / 2)[0])
        exact = None
        try:
            # the antisymmetric mode: student 1 along v1 - v2, student 2 along v2 - v1
            u = sp.zeros(K, K); u[0, 0] = 1; u[0, 1] = -1; u[1, 0] = -1; u[1, 1] = 1
            uv = sp.Matrix(list(u)) / 2
            exact = sp.nsimplify(sp.simplify(-(uv.T * H.subs(r, r0) * uv)[0]))
        except Exception as e:
            exact = repr(e)
        print("K %d r %s (Q = %s) eps %s  lambda/eta = %.12f ; antisym (1,2) mode: %s = %s"
              % (K, sp.nsimplify(r0), sp.nsimplify(K * r0 ** 2), sp.N(er.subs(r, r0), 8), -lo,
                 exact, sp.N(exact, 12) if not isinstance(exact, str) else ''), flush=True)
