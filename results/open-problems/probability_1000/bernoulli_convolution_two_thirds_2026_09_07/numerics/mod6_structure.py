import numpy as np, math, sys
sys.argv = [sys.argv[0], "22", str(3 * 2**18)]
exec(open("exact_depth.py", encoding="utf-8").read().split("starts = prefix_starts(D)")[0])
D = int(sys.argv[1]); R = int(sys.argv[2])
starts = prefix_starts(D); L = lam**D
g = density_on_grid(starts, L, R)
for n in range(0, 4):
    N = n + 2; K = 2**N; per = R // K
    q = g.reshape(K, per); sh = 2**(n+1); M = K + sh
    w = np.zeros((M, per)); w[:K] += 0.5*q; w[sh:sh+K] += 0.5*q
    mass_t = w.sum(axis=0); sign = np.array([(-1.0)**m for m in range(M)])[:, None]
    V = []; P = []
    for r in range(3):
        idx = np.arange(r, M, 3); Pr = w[idx].sum(axis=0)
        V.append((sign[idx]*w[idx]).sum(axis=0)/np.maximum(Pr,1e-300)); P.append(Pr/np.maximum(mass_t,1e-300))
    V = np.array(V); P = np.array(P); wt = mass_t/mass_t.sum()
    Au = (P*V).sum(axis=0)
    cov = lambda x,y: float((wt*x*y).sum() - (wt*x).sum()*(wt*y).sum())
    print(f"n={n}: E[V_r]={[round(float((wt*V[r]).sum()),5) for r in range(3)]}  E[V_r^2]={[round(float((wt*V[r]**2).sum()),6) for r in range(3)]}"
          f"  corr(V0,V2)={cov(V[0],V[2])/math.sqrt(cov(V[0],V[0])*cov(V[2],V[2])):.3f}  corr(V0,V1)={cov(V[0],V[1])/math.sqrt(cov(V[0],V[0])*cov(V[1],V[1])):.3f}"
          f"  corr(V1,V2)={cov(V[1],V[2])/math.sqrt(cov(V[1],V[1])*cov(V[2],V[2])):.3f}  E[P_r]={[round(float((wt*P[r]).sum()),4) for r in range(3)]}")
    # symmetry check t -> 1-t : V_r(t) vs V_{r'}(1-t)
    Vf = V[:, ::-1]
    print(f"      symmetry t->1-t: max|V_r(t)+V_{{s(r)}}(1-t)| for s=identity: {np.abs(V+Vf).max():.3e}, s=reverse(r->2-r): {np.abs(V+Vf[::-1]).max():.3e}, s=id minus: {np.abs(V-Vf).max():.3e}, s=rev minus: {np.abs(V-Vf[::-1]).max():.3e}")
