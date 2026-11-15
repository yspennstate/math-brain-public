# Independent check of C0033D (11)-(13): entropy Hessian at Q_r on the subspace T = alpha I + beta (J3 - I), by central
# finite differences from the atom formula alone, against -(F + diag(3L, 6L)) + kappa * tau tau^T with tau = (3, 0).
import itertools, sys
import mpmath as mp
mp.mp.dps = 80

def H(Q):
    s = 0
    for sub in itertools.product([0, 1], repeat=3):
        M = Q.copy()
        for i in range(3):
            if not sub[i]:
                M[i, i] -= 1
        p = ((-1) ** (3 - sum(sub))) * mp.re(mp.det(M))
        s -= p * mp.log(p)
    return s

I3 = mp.eye(3)
Joff = mp.matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
dirs = [I3, Joff]
h = mp.mpf("1e-20")
for r in [mp.mpf(x) for x in sys.argv[1:]]:
    Q = mp.matrix([[0.5, 1j * r, -1j * r], [-1j * r, 0.5, 1j * r], [1j * r, -1j * r, 0.5]])
    Hs = mp.zeros(2)
    for a in range(2):
        for b in range(2):
            f = lambda sa, sb: H(Q + sa * h * dirs[a] + sb * h * dirs[b])
            Hs[a, b] = (f(1, 1) - f(1, -1) - f(-1, 1) + f(-1, -1)) / (4 * h * h)
    k = (1 + 4 * r * r) / (1 - 12 * r * r)
    L = mp.log(k)
    den = k * (3 * k + 1)
    f11 = 3 * (3 * k**3 + 15 * k**2 - 3 * k + 1) / den
    f12 = -9 * (k - 1) ** 3 / den
    f22 = 9 * (k - 1) ** 2 * (k + 3) / den
    J = mp.matrix([[f11 + 3 * L, f12], [f12, f22 + 6 * L]])
    G = Hs + J  # should be kappa * diag(9, 0)
    kappa = G[0, 0] / 9
    Jinv = J ** -1
    theta_num = kappa * 9 * Jinv[0, 0]
    D = 36 * (-L**2 + (6 * k**2 + 6 * k - 4) / den * L + 3 * (k - 1) ** 2 / k)
    s = D / (f22 + 6 * L)
    theta_rep = 9 * L / (9 * L + s)
    print(f"r={float(r):.5f} L={float(L):.4f} off-diag resid={mp.nstr(G[0,1],3)} bb resid={mp.nstr(G[1,1],3)} "
          f"kappa={mp.nstr(kappa,10)} kappa/L={mp.nstr(kappa/L,10)} theta_num={mp.nstr(theta_num,12)} theta_rep={mp.nstr(theta_rep,12)} "
          f"m={mp.nstr(1-theta_rep,6)} 4/(L+4)={mp.nstr(4/(L+4),6)}", flush=True)
