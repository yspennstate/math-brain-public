"""Independent check of T255 section 13 (agent J, 17 Oct 2026).

Written from the paper's Corollary 4.3 (b + b_res, Sigma + Sigma_res, Theorem 3.2 as printed on p. 6) and section 1's
congruence form of Theorem 4.2's noise; no code from lyapY_mlp.py. The generator of a function Y(V) is
    LY = DY[b + b_res] + (1/2) sum_j D^2 Y[E_j, E_j]
with the noise directions E_j = sqrt(c') L B L^T (B over a GOE basis, c' = gamma^2 (2 - gamma^2) + 2 gamma^2) and
E_ij = k L (e_i e_j^T K + K e_j e_i^T) L^T (K = L^T P L, k = gamma^2/(m tau0)). Derivatives are central differences at
200 digits. Reported: max over sampled points of LY / (|W|_F^2 Y), the rate per unit u.

Self-checks first: (s1) at m = 2 the qv of w = tr(PV) is (2c + 4 gamma^2) w^2 + gamma^4 w^4/tau0^2 and its drift is
kappa w^3 - (b_res)_12 (section 14); (s2) the linear part of qv(tr V) is 2 c' |V|_F^2 (section 11).
"""
import json, random, sys
import mpmath as mp

mp.mp.dps = 200
HREL = mp.mpf(10) ** -70


def zeros(m): return mp.matrix(m, m)


def eye(m):
    I = zeros(m)
    for i in range(m): I[i, i] = 1
    return I


def P_of(m):
    P = eye(m)
    for i in range(m):
        for j in range(m): P[i, j] -= mp.mpf(1) / m
    return P


def frob2(A): return mp.fsum(A[i, j] ** 2 for i in range(A.rows) for j in range(A.cols))


def tr(A): return mp.fsum(A[i, i] for i in range(A.rows))


def chol(V):
    m = V.rows; L = zeros(m)
    for i in range(m):
        for j in range(i + 1):
            s = V[i, j] - mp.fsum(L[i, k] * L[j, k] for k in range(j))
            L[i, j] = mp.sqrt(s) if i == j else s / L[j, j]
    return L


class Model:
    def __init__(self, m, g2, tau0, Delta, mlp=True):
        self.m, self.g2, self.tau0, self.Delta, self.mlp = m, mp.mpf(g2), mp.mpf(tau0), mp.mpf(Delta), mlp
        self.P = P_of(m)
        self.c = self.g2 * (2 - self.g2)
        self.cp = self.c + (2 * self.g2 if mlp else 0)
        self.k = self.g2 / (m * self.tau0)

    def nu(self, r):
        r = max(min(r, mp.mpf(1)), mp.mpf(-1))
        return self.Delta / (2 * mp.pi) * (mp.sqrt(1 - r * r) - r * mp.acos(r))

    def drift(self, V):
        m, P = self.m, self.P
        W = P * V * P
        v = mp.matrix([V[i, i] for i in range(m)])
        D = mp.matrix([W[i, i] - tr(W) / m for i in range(m)])
        VD = V * D
        b = V * (frob2(W) / m ** 2) + (v * VD.T + VD * v.T) * (mp.mpf(1) / (2 * m))
        b = b * (self.g2 / self.tau0 ** 2)
        if self.mlp:
            for i in range(m):
                for j in range(m):
                    if i != j:
                        s = mp.sqrt(V[i, i] * V[j, j])
                        b[i, j] += self.g2 * self.nu(V[i, j] / s) * s
        return b

    def noise(self, V):
        m = self.m; L = chol(V); K = L.T * self.P * L; out = []
        for i in range(m):
            for j in range(i, m):
                B = zeros(m)
                if i == j: B[i, i] = mp.sqrt(2)
                else: B[i, j] = 1; B[j, i] = 1
                out.append(L * B * L.T * mp.sqrt(self.cp))
        for i in range(m):
            for j in range(m):
                Eij = zeros(m); Eij[i, j] = 1
                out.append(L * (Eij * K + K * Eij.T) * L.T * self.k)
        return out

    def gen(self, f, V):
        """drift and quadratic-variation rate of f(V), per unit t."""
        B = self.drift(V); f0 = f(V); nV = mp.sqrt(frob2(V))
        def d1(E):
            h = HREL * nV / mp.sqrt(frob2(E)); return (f(V + E * h) - f(V - E * h)) / (2 * h)
        def d2(E):
            h = HREL * nV / mp.sqrt(frob2(E)); return (f(V + E * h) - 2 * f0 + f(V - E * h)) / h ** 2
        dr = d1(B); qv = mp.mpf(0); ito = mp.mpf(0)
        for E in self.noise(V):
            if frob2(E) == 0: continue
            g = d1(E); qv += g * g; ito += d2(E)
        return dr + ito / 2, qv, f0


def coords(V):
    m = V.rows; a = V[0, 0]
    w = [V[i, 0] / a for i in range(1, m)]
    trX = mp.fsum(V[i, i] - V[i, 0] ** 2 / a for i in range(1, m))
    return a, w, trX


def Y_new(q, p, M):
    def f(V):
        a, w, trX = coords(V); return a ** -q + mp.fsum(x * x for x in w) + M * ((trX + 1) / a) ** p
    return f


def Y_old(q, p, M):
    def f(V):
        a, w, trX = coords(V); return a ** -q + mp.fsum(x * x for x in w) + M * (trX / a) ** p
    return f


def build(m, a, w, X):
    """V from (a, w, X): L = [[sqrt a, 0], [sqrt a w, chol X]]."""
    Lx = chol(X); L = zeros(m); L[0, 0] = mp.sqrt(a)
    for i in range(1, m):
        L[i, 0] = mp.sqrt(a) * w[i - 1]
        for j in range(1, i + 1): L[i, j] = Lx[i - 1, j - 1]
    return L * L.T


def rand_shape(rng, n, cond_exp):
    A = mp.matrix([[mp.mpf(rng.gauss(0, 1)) for _ in range(n)] for _ in range(n)])
    Q, _ = mp.qr(A)
    ev = [mp.mpf(10) ** (-rng.uniform(0, cond_exp)) for _ in range(n)]
    X = zeros(n)
    for i in range(n):
        for j in range(n): X[i, j] = mp.fsum(Q[i, k] * ev[k] * Q[j, k] for k in range(n))
    t = tr(X)
    return X * (1 / t)


def selfchecks(rng):
    res = {}
    # s1: m = 2
    worst_q = worst_d = mp.mpf(0)
    for g2 in (0.2, 0.5, 1.0):
        md = Model(2, g2, 1.0, 4.0)
        for _ in range(20):
            x = [mp.mpf(10) ** rng.uniform(-3, 3) for _ in range(2)]; r = mp.mpf(rng.uniform(-0.99, 0.99))
            V = mp.matrix([[x[0], r * mp.sqrt(x[0] * x[1])], [r * mp.sqrt(x[0] * x[1]), x[1]]])
            fw = lambda U: (U[0, 0] + U[1, 1] - 2 * U[0, 1]) / 2
            dr, qv, w = md.gen(fw, V)
            qv_claim = (2 * md.c + 4 * md.g2) * w ** 2 + md.g2 ** 2 * w ** 4 / md.tau0 ** 2
            s = mp.sqrt(V[0, 0] * V[1, 1])
            dr_claim = md.g2 / (4 * md.tau0 ** 2) * w ** 3 - md.g2 * md.nu(V[0, 1] / s) * s
            worst_q = max(worst_q, abs(qv / qv_claim - 1)); worst_d = max(worst_d, abs(dr - dr_claim) / (abs(dr_claim) + w ** 3))
    res["s1_m2_qv_relgap"] = mp.nstr(worst_q, 3); res["s1_m2_drift_relgap"] = mp.nstr(worst_d, 3)
    # s2: linear part of qv(tr V) = 2 c' |V|_F^2 (set k = 0)
    worst = mp.mpf(0)
    for m in (3, 4):
        md = Model(m, 0.7, 1.0, 1.0); md.k = mp.mpf(0)
        for _ in range(5):
            X = rand_shape(rng, m, 3) * mp.mpf(10) ** rng.uniform(-2, 2)
            dr, qv, _ = md.gen(lambda U: tr(U), X)
            worst = max(worst, abs(qv / (2 * md.cp * frob2(X)) - 1))
    res["s2_trV_linear_qv_relgap"] = mp.nstr(worst, 3)
    return res


def run_cell(rng, m, g2, Delta, n, q=0.1, p=0.1, delta=0.05, lam1=100, M=10, adversarial=False):
    md = Model(m, g2, 1.0, Delta)
    Yn, Yo = Y_new(q, p, M), Y_old(q, p, M)
    worst_new = worst_old = None
    for _ in range(n):
        a = mp.mpf(10) ** rng.uniform(mp.log10(lam1), 10)
        if adversarial and rng.random() < 0.5: a = mp.mpf(lam1) * (1 + mp.mpf(rng.random()) / 10)
        r = delta * (rng.random() if rng.random() < 0.5 else 10 ** rng.uniform(-6, 0))
        dirn = [rng.gauss(0, 1) for _ in range(m - 1)]
        if adversarial: dirn = [-abs(x) for x in dirn]            # every tilt anti-aligned: the forcing is largest
        nd = sum(x * x for x in dirn) ** 0.5
        w = [mp.mpf(r * x / nd) * mp.mpf(0.999) for x in dirn]
        phi = delta * mp.mpf(10) ** (-rng.uniform(0, 40))
        X = rand_shape(rng, m - 1, 10) * (phi * a)
        V = build(m, a, w, X)
        W = md.P * V * md.P; W2 = frob2(W)
        for Yf, tag in ((Yn, "new"), (Yo, "old")):
            dr, _, y = md.gen(Yf, V)
            rate = dr / (W2 * y)
            rec = (float(rate), float(a), float(r), float(phi))
            if tag == "new": worst_new = rec if worst_new is None or rec[0] > worst_new[0] else worst_new
            else: worst_old = rec if worst_old is None or rec[0] > worst_old[0] else worst_old
    return worst_new, worst_old


def main():
    rng = random.Random(25917)
    out = {"selfchecks": selfchecks(rng)}
    print("selfchecks", out["selfchecks"], flush=True)
    cells = []
    plan = [(3, 1.0, 1.0), (3, 0.5, 1.0), (3, 1.0, 4.0), (3, 0.1, 4.0), (4, 1.0, 1.0), (4, 0.3, 4.0), (5, 1.0, 1.0)]
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    for m, g2, Dl in plan:
        for adv in (False, True):
            wn, wo = run_cell(rng, m, g2, Dl, n, adversarial=adv)
            row = dict(m=m, g2=g2, Delta=Dl, adversarial=adv, n=n, max_rate_new=wn, max_rate_old=wo)
            cells.append(row); print(json.dumps(row), flush=True)
            json.dump(dict(out, cells=cells), open("lyapY_indep.json", "w"), indent=1)
    print("DONE")


if __name__ == "__main__":
    main()
