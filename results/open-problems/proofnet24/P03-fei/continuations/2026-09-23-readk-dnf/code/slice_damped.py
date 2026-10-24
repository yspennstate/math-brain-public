# The damped inequality for slice indicators d = 1[N = s] under a product measure (nats):
#   Psi(d) = sum_{B != 0} (d~(B)^2 / (|B|+1)) ln(sigma_B^2 / d~(B)^2)  <=  C Var(d),
# with d~ the coefficients of the 0/1 function d in the orthonormal basis.  Also checks the identity
#   sum_{|A|>=2} P(A) ln(sigma_A^2/P(A)) = sum_j sigma_j^2 Psi(d_j)      (P for the +-1 threshold T_{t,r})
# which reduces the strengthened biased inequality for thresholds to this one.
import mpmath as mp, random, sys
from isoper3 import biased_P
mp.mp.dps = 40

def psi_slice(n, s, q):
    d = [1 if bin(x).count('1') == s else 0 for x in range(1 << n)]
    P = biased_P(d, q)                       # squared coefficients of the +-1 version
    sig2 = [4 * mp.mpf(v) * (1 - mp.mpf(v)) for v in q]
    U = mp.fsum(P[1:]) / 4
    psi = mp.mpf(0)
    for B in range(1, 1 << n):
        c2 = P[B] / 4
        if c2 > 0:
            k = bin(B).count('1')
            psi += c2 / (k + 1) * mp.log(mp.fprod(sig2[i] for i in range(n) if B >> i & 1) / c2)
    return psi, U

def identity_check(r, t, q):
    f = [1 if bin(x).count('1') >= t else 0 for x in range(1 << r)]
    P = biased_P(f, q)
    sig2 = [4 * mp.mpf(v) * (1 - mp.mpf(v)) for v in q]
    lhs2 = mp.fsum(P[A] * mp.log(mp.fprod(sig2[i] for i in range(r) if A >> i & 1) / P[A])
                   for A in range(1, 1 << r) if bin(A).count('1') >= 2 and P[A] > 0)
    rhs = mp.mpf(0); J = mp.mpf(0)
    for j in range(r):
        qq = [q[i] for i in range(r) if i != j]
        psi, U = psi_slice(r - 1, t - 1, qq)
        rhs += sig2[j] * psi; J += sig2[j] * U
    return lhs2, rhs, J

def rq(rng):
    u = rng.random()
    v = 10 ** -rng.uniform(0, 12) if u < 0.35 else (1 - 10 ** -rng.uniform(0, 12) if u < 0.7 else rng.uniform(0.02, 0.98))
    return min(max(v, 1e-13), 1 - 1e-13)

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); nmax = int(sys.argv[3])
    for (r, t) in [(3, 2), (5, 3), (6, 2)]:
        q = [rq(rng) for _ in range(r)]
        a, b, J = identity_check(r, t, q)
        print('identity', r, t, mp.nstr(a, 15), mp.nstr(b, 15), 'diff', mp.nstr(a - b, 3), flush=True)
    worst = (-1e9, None)
    for trial in range(T):
        n = rng.randint(1, nmax); s = rng.randint(0, n)
        q = [rq(rng) for _ in range(n)]
        psi, U = psi_slice(n, s, q)
        if U <= mp.mpf(10) ** -30: continue
        ratio = float(psi / U)
        if ratio > worst[0]:
            worst = (ratio, n, s, ['%.3g' % v for v in q], float(U))
        if trial % 200 == 0: print(trial, round(worst[0], 4), flush=True)
    print('WORST', worst)
