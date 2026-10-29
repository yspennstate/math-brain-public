"""NOTE 'uniform in n', step E[b eta_c^3] = O(d^2): check d * E[b_k (Z_k + W)^3] stays bounded as d -> 0 at large n (agent A).
Model of the NOTE's table: b = 9 on n/10 slots, -1 elsewhere, x = x0-sized. W_p = beta2 (Z_pi(p-1) + W_{p-1})."""
import sys, numpy as np
n = int(sys.argv[1]); C = int(sys.argv[2]); rng = np.random.default_rng(11)
m = n // 10; b = np.array([9.0]*m + [-1.0]*(n - m)); x = 0.02
Z = (x + b)**2; Z -= Z.mean(); EbZ = np.mean(b*Z); s2 = np.mean(Z**2)
for b2 in (0.9, 0.99, 0.999, 0.9999):
    d = 1 - b2; acc = np.zeros(C)
    perm = np.argsort(rng.random((C, n)), axis=1)
    W = np.zeros(C)
    for p in range(n):
        k = perm[:, p]
        if p: W = b2 * (Z[perm[:, p-1]] + W)
        acc += b[k] * (Z[k] + W)**3
    E = acc.mean()/n; se = acc.std(ddof=1)/n/np.sqrt(C)
    A2 = np.mean([np.sum(b2**(2*np.arange(1, p+1))) for p in range(0, n, max(1, n//200))])
    print("n %d beta2 %s: E[b(Z+W)^3] %.4g +- %.2g | d*E %.4g | 3 EbZ s2 A2(avg over p) %.4g" % (n, b2, E, se, d*E, 3*EbZ*s2*A2), flush=True)
