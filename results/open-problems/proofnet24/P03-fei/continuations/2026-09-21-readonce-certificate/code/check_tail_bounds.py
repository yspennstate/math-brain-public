"""numerical sanity checks of the two analytic tail bounds used by the certificate (90-digit mpmath):
   (T1)  E(p,q) - b* <= (16K + 19) 2^-K  for p, q <= 2^-K
   (T2)  E(p,q) - e(q) <= p [8(1-q) L(p) + 12/ln2]  for p <= 2^-K, q <= 1/2,  e(q) = 8 q L(q) + 8(1-q) - Psi(q)"""
import mpmath as mp, random
mp.mp.dps = 90
def psi(z):
    w = (1 - 2 * z) ** 2
    return -w * mp.log(w, 2) / z if w > 0 else mp.mpf(0)
def L(z): return mp.log(1 / z, 2)
def E(p, q): return 8 * p * (1 - q) * L(p) + 8 * q * (1 - p) * L(q) + 8 * (1 - p) * (1 - q) + psi(p * q) - psi(p) - psi(q)
def e(q): return 8 * q * L(q) + 8 * (1 - q) - psi(q)
bstar = 8 - 4 / mp.log(2)
random.seed(1); worst1 = -mp.inf; worst2 = -mp.inf
for K in (10, 14, 20, 30, 40, 60):
    K = mp.mpf(K)
    for _ in range(300):
        p = mp.mpf(2) ** (-(K + 30 * random.random())); q = mp.mpf(2) ** (-(K + 30 * random.random()))
        ratio = (E(p, q) - bstar) / ((16 * K + 19) * mp.mpf(2) ** (-K))
        worst1 = max(worst1, ratio)
    for _ in range(300):
        p = mp.mpf(2) ** (-(K + 30 * random.random())); q = mp.mpf(2) ** (-(1 + (K - 1) * random.random()))
        bound = p * (8 * (1 - q) * L(p) + 12 / mp.log(2))
        ratio = (E(p, q) - e(q)) / bound
        worst2 = max(worst2, ratio)
print("(T1) max of (E - b*) / ((16K+19) 2^-K) over samples: %s  (must be <= 1)" % mp.nstr(worst1, 6))
print("(T2) max of (E - e(q)) / (p[8(1-q)L(p) + 12/ln2]) over samples: %s  (must be <= 1)" % mp.nstr(worst2, 6))
# corner limit check
print("E(2^-60, 2^-60) - b* = %s ; e(1/2) = %s" % (mp.nstr(E(mp.mpf(2) ** -60, mp.mpf(2) ** -60) - bstar, 5), mp.nstr(e(mp.mpf(1) / 2), 12)))
