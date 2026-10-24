# F0019: exact-in-environment test of  d/dbeta E[OV_n] = 2 beta n E< R12^2 + 3 R12 R34 - 4 R13 R23 >
# and of p_n' = beta(1 - E OV_n), by enumerating all 2^n paths in d=1 and averaging over M Gaussian environments.
import numpy as np, itertools, json
rng = np.random.default_rng(11)
def paths(n):
    P = np.array(list(itertools.product([-1,1], repeat=n))).cumsum(axis=1)  # (2^n, n) positions X_1..X_n
    return P
def stats(n, beta, M, h=1e-3):
    P = paths(n); K = P.shape[0]
    R = (P[:,None,:] == P[None,:,:]).mean(axis=2)          # overlap fraction matrix (K,K)
    # site index for (k, x): x in [-n, n] -> x+n
    idx = (np.arange(n)[None,:]*(2*n+1) + (P+n))            # (K, n) flat site ids
    W = rng.standard_normal((M, n*(2*n+1)))
    H = W[:, idx].sum(axis=2)                                 # (M, K) path energies
    def q_and_logZ(b):
        w = np.exp(b*(H - H.max(axis=1, keepdims=True)))
        nu = w/w.sum(axis=1, keepdims=True)
        logZ = np.log(w.sum(axis=1)) + b*H.max(axis=1) - n*np.log(2)
        r12 = np.einsum('mp,mq,pq->m', nu, nu, R)
        return nu, r12, logZ
    nu, r12, logZ = q_and_logZ(beta)
    r12sq = np.einsum('mp,mq,pq->m', nu, nu, R**2)
    t = nu @ R                                                # (M,K): sum_p nu_p R(p,q)
    r1323 = np.einsum('mq,mq->m', nu, t**2)
    formula = 2*beta*n*(r12sq + 3*r12**2 - 4*r1323).mean()
    _, r12p, lp = q_and_logZ(beta+h); _, r12m, lm = q_and_logZ(beta-h)
    fd = ((r12p - r12m)/(2*h)).mean()
    pprime = ((lp-lm)/(2*h)/n).mean(); ident = beta*(1-r12.mean())
    return fd, formula, pprime, ident
out={}
for n in [2,3,4,6]:
    for beta in [0.5,1.0,2.0]:
        M = 200000 if n<=4 else 60000
        fd, fo, pp, idn = stats(n,beta,M)
        out[f"n{n}_b{beta}"]=(fd,fo,pp,idn)
        print(f"n={n} beta={beta} M={M}:  FD dq/dbeta={fd:.4f}  formula={fo:.4f}  |  FD p_n'={pp:.4f}  beta(1-E OV)={idn:.4f}")
json.dump(out,open('gg_defect_exact_small_n.json','w',encoding='utf-8'),indent=1)
