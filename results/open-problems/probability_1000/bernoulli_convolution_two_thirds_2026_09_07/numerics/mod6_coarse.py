import numpy as np, math, sys
sys.argv = [sys.argv[0], "24", str(3 * 2**18)]
exec(open("exact_depth.py", encoding="utf-8").read().split("starts = prefix_starts(D)")[0])
D = int(sys.argv[1]); R = int(sys.argv[2])
starts = prefix_starts(D); L = lam**D
g = density_on_grid(starts, L, R)
print(f"D={D}: n | mod-6 law of m=floor(2^(n+2)Y)+2^(n+1)B (s=0..5) | Eu2 | Em2 | coarse lower bound Lc=sum_r (E[P_r V_r])^2/E[P_r] | Lc/Eu2 | E[Var_r]=Eu2-Em2 | Lc/(Eu2-Em2)")
for n in range(0, 7):
    N = n + 2; K = 2**N; per = R // K
    if per < 3: break
    q = g.reshape(K, per); sh = 2**(n+1); M = K + sh
    w = np.zeros((M, per)); w[:K] += 0.5*q; w[sh:sh+K] += 0.5*q
    mass_t = w.sum(axis=0); tot = mass_t.sum()
    sign = np.array([(-1.0)**m for m in range(M)])[:, None]
    Au = (sign*w).sum(axis=0)/np.maximum(mass_t,1e-300); Em2 = float((mass_t*Au**2).sum()/tot)
    Eu2 = 0.0; Lc = 0.0; law6 = [float(w[np.arange(s, M, 6)].sum()/tot) for s in range(6)]
    for r in range(3):
        idx = np.arange(r, M, 3); Pr = w[idx].sum(axis=0); Vr = (sign[idx]*w[idx]).sum(axis=0)/np.maximum(Pr,1e-300)
        Eu2 += float((Pr*Vr**2).sum()/tot)
        EPV = float((Pr*Vr).sum()/tot); EP = float(Pr.sum()/tot); Lc += EPV**2/EP
    print(f"n={n}: law6={np.round(law6,4)}  Eu2={Eu2:.3e} Em2={Em2:.3e}  Lc={Lc:.3e}  Lc/Eu2={Lc/Eu2:.3f}  EVar={Eu2-Em2:.3e}  Lc/EVar={Lc/(Eu2-Em2):.3f}")
