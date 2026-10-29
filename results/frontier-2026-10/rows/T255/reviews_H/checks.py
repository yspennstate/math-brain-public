"""T255 audit checks (agent H): sections 4 and 9 of M2_EXACT.md against gen_b1e.py."""
import random, sys
import mpmath as mp
from gen_b1e import generator, P_of, W2_of, drift_b
mp.mp.dps = 100
random.seed(7)
tau0 = mp.mpf("0.7")

def rand_pd(m, scale=1):
    A = mp.matrix([[mp.mpf(random.gauss(0, 1)) for _ in range(m)] for _ in range(m)])
    return (A * A.T + mp.eye(m) * mp.mpf("0.1")) * scale

def sec4():
    worst = [0, 0, 0]
    for g2 in map(mp.mpf, ["0.2", "0.5", "0.9", "1"]):
        c = g2 * (2 - g2); kap = g2 / (4 * tau0 ** 2); k2 = g2 ** 2 / tau0 ** 2
        for _ in range(6):
            V = rand_pd(2, mp.mpf(random.choice([0.3, 1, 5])))
            P = P_of(2)
            wf = lambda X: sum((P * X)[i, i] for i in range(2))
            w = wf(V)
            dr, qv = generator(wf, V, g2, tau0)
            worst[0] = max(worst[0], abs(dr / (kap * w ** 3) - 1), abs(qv / (2 * c * w ** 2 + k2 * w ** 4) - 1))
            Sf = lambda X: sum(X[i, j] for i in range(2) for j in range(2))
            S = Sf(V); dS, qS = generator(Sf, V, g2, tau0)
            worst[1] = max(worst[1], abs(dS / (g2 * w ** 2 / (4 * tau0 ** 2) * S) - 1))
            worst[2] = max(worst[2], qS / (S ** 2 * (1 + w) ** 2))
    print("sec4: max rel err drift/qv of w %.2e; drift of S rel err %.2e; max qv(S)/(S(1+w))^2 %.3f" % tuple(map(float, worst)))

def schur(V):
    a = V[0, 0]; m = V.rows
    p1 = mp.matrix([V[i, 0] for i in range(1, m)])
    X = mp.matrix([[V[i, j] for j in range(1, m)] for i in range(1, m)]) - p1 * p1.T / a
    return a, p1 / a, X

def corner(m, a, wv, Xs):
    """V with V11 = a, tilt wv (list), Schur complement Xs."""
    V = mp.zeros(m, m); V[0, 0] = a
    for i in range(1, m):
        V[i, 0] = V[0, i] = a * wv[i - 1]
    for i in range(1, m):
        for j in range(1, m):
            V[i, j] = Xs[i - 1, j - 1] + a * wv[i - 1] * wv[j - 1]
    return V

def logPhi(V):
    a, w, X = schur(V)
    return mp.log(sum(X[i, i] for i in range(X.rows)) / a)

def sec9(m, g2, shapes, wsize, a=mp.mpf(10) ** 6, eps=mp.mpf(10) ** -12, with_c=False, cond=None):
    mu = g2 / m ** 2 * (g2 - mp.mpf(m * (m - 2)) / (m - 1))
    out = []
    for _ in range(shapes):
        n = m - 1
        Q = mp.matrix([[mp.mpf(random.gauss(0, 1)) for _ in range(n)] for _ in range(n)])
        Q, _r = mp.qr(Q)
        ev = [mp.mpf(10) ** (-random.uniform(0, cond)) if cond else mp.mpf(random.uniform(0.1, 1)) for _ in range(n)]
        Xs = Q * mp.diag(ev) * Q.T
        Xs = Xs * (eps * a / sum(Xs[i, i] for i in range(n)))
        wv = [mp.mpf(random.gauss(0, 1)) for _ in range(n)]
        nrm = mp.sqrt(sum(x * x for x in wv)); wv = [x * wsize / nrm for x in wv]
        V = corner(m, a, wv, Xs)
        dr, qv = generator(logPhi, V, g2, tau0, with_c=with_c)
        W2 = W2_of(V) / tau0 ** 2
        out.append((dr / W2, qv / W2))
    drs = [float(x[0]) for x in out]; qvs = [float(x[1]) for x in out]
    return float(mu), min(drs), max(drs), max(qvs)

def alpha_check(m, g2):
    a = mp.mpf(10) ** 6
    V = corner(m, a, [0] * (m - 1), mp.eye(m - 1) * a * mp.mpf(10) ** -12)
    dr, qv = generator(lambda X: mp.log(X[0, 0]), V, g2, tau0, with_c=False)
    W2 = W2_of(V) / tau0 ** 2
    f = g2 * ((mp.mpf(m - 1) / m) ** 2 / m ** 2 + mp.mpf((m - 1) * (m - 2)) / m ** 2 / m)
    B = 2 * g2 * (mp.mpf(m - 1) / m) / m
    alpha = (f - B ** 2 / 2) * m ** 2 / (m - 1) ** 2
    return float(dr / W2), float(alpha), float(2 * f / B ** 2), float((m * m - m - 1) / (2 * g2 * (m - 1)))

if __name__ == "__main__":
    which = sys.argv[1]
    if which == "sec4":
        sec4()
    elif which == "alpha":
        for m in (3, 4, 5):
            for g2 in map(mp.mpf, ["0.5", "1"]):
                print("alpha m%d g2 %s: generator %.10f  formula %.10f  2f/B^2 %.6f vs %.6f" % ((m, float(g2)) + alpha_check(m, g2)))
    elif which == "mu":
        for m in (3, 4, 5):
            for g2 in map(mp.mpf, ["0.3", "0.5", "1"]):
                for ws, cond in ((0, None), (mp.mpf("1e-6"), None), (0, 8), (mp.mpf("1e-3"), 8)):
                    mu, lo, hi, q = sec9(m, g2, 6, ws, cond=cond)
                    print("mu m%d g2 %.1f |w| %.0e cond %s: formula %.8f  generator [%.8f, %.8f]  max qv %.4f" % (m, float(g2), float(ws), cond, mu, lo, hi, q), flush=True)
    elif which == "muc":
        for m in (3, 4):
            g2 = mp.mpf(1)
            for a in (mp.mpf(10) ** 3, mp.mpf(10) ** 6):
                mu, lo, hi, q = sec9(m, g2, 4, 0, a=a, with_c=True, cond=6)
                print("with c-noise m%d a %.0e: formula %.8f  generator [%.8f, %.8f]" % (m, float(a), mu, lo, hi), flush=True)
