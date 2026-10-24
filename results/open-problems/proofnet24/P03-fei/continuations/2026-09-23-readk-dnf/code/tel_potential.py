# Gate inequality with the potential Phi(f) = Var ln(1/Var) (nats), for thresholds T_{t,r} under product measures:
#   LHS <= C (I - V) + K [ sum_i Inf_i ln(1/sigma_i^2) - V ln(1/V) ].
# Reports, for each K, the worst (LHS - K*B)/(I - V), and the worst (LHS - K*B)/J with J = sum_{|A|>=2}|A|P(A).
import mpmath as mp, random, sys
from isoper3 import biased_P
from slice_damped import rq
mp.mp.dps = 50
KS = [0, 0.25, 0.5, 1, 2, 4]
def quant(r, t, q):
    f = [1 if bin(x).count('1') >= t else 0 for x in range(1 << r)]
    P = biased_P(f, q); sig2 = [4 * mp.mpf(v) * (1 - mp.mpf(v)) for v in q]
    V = mp.fsum(P[1:]); I = mp.fsum(bin(A).count('1') * P[A] for A in range(1, 1 << r))
    J = mp.fsum(bin(A).count('1') * P[A] for A in range(1, 1 << r) if bin(A).count('1') >= 2)
    Inf = [mp.fsum(P[A] for A in range(1 << r) if A >> i & 1) for i in range(r)]
    lhs = mp.fsum(P[A] * mp.log(mp.fprod(sig2[i] for i in range(r) if A >> i & 1) / P[A]) for A in range(1, 1 << r) if P[A] > 0)
    B = mp.fsum(Inf[i] * mp.log(1 / sig2[i]) for i in range(r)) - V * mp.log(1 / V)
    rho = [Inf[i] / sig2[i] for i in range(r)]
    return lhs, I, V, J, B, max(rho)
if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); rmax = int(sys.argv[3])
    worst = {}; negB = [0, 0]
    for trial in range(T):
        r = rng.randint(2, rmax); t = rng.randint(1, r); q = [rq(rng) for _ in range(r)]
        lhs, I, V, J, B, rmx = quant(r, t, q)
        if I - V <= mp.mpf(10) ** -40: continue
        negB[0] += 1; negB[1] += 1 if B < 0 else 0
        for K in KS:
            v1 = float((lhs - K * B) / (I - V)); key = 'K%s' % K
            if key not in worst or v1 > worst[key][0]:
                worst[key] = (v1, r, t, ['%.3g' % x for x in q], float(B / (I - V)), rmx)
        if trial % 300 == 0: print(trial, {k: round(v[0], 3) for k, v in worst.items()}, flush=True)
    print('B<0 in', negB[1], 'of', negB[0])
    for k, v in worst.items(): print('WORST', k, v)
