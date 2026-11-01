# One-level vs two-level coarse shares: global joint law of (H, first k ternary digits of Z) for U ~ mu_n = T_2^n mu.
# Coarse lower bound L^(k)_n = sum_c (E[s_c P_c u_c])^2 / E[P_c] over the 3^k classes c of Z, s_c = (-1)^(digit sum);
# compare with the k-level decrement E[u_n^2] - E[u_{n+k}^2].  Density: exact prefix g_D (D=24).
import numpy as np, math, sys
sys.argv = [sys.argv[0], "24", str(3**2 * 2**17)]
exec(open("exact_depth.py", encoding="utf-8").read().split("starts = prefix_starts(D)")[0])
D = int(sys.argv[1]); R = int(sys.argv[2])
starts = prefix_starts(D); L = lam**D
g = density_on_grid(starts, L, R)
def Eu2_of(mass):
    half = mass.size//2; m0 = mass[:half]; m1 = mass[half:]; tot = m0+m1
    u = np.where(tot>0, (m0-m1)/np.maximum(tot,1e-300), 0.0)
    return float(np.sum(tot*u**2))/float(np.sum(tot)), u, tot
levels = []
gg = g
for n in range(0, 8):
    if gg.size % 18: break
    E, u, tot = Eu2_of(gg); levels.append((n, E, u, tot)); gg = gg[:gg.size//2] + gg[gg.size//2:]
print(f"D={D} R={R}: n | Eu2 | 1-level decrement | coarse L1 | share | 2-level decrement | coarse L2 (9 classes) | share")
for i in range(len(levels)-2):
    n, E, u, tot = levels[i]; E1 = levels[i+1][1]; E2 = levels[i+2][1]
    half = u.size; T = float(tot.sum())
    def coarse(k):
        ncls = 3**k; per = half//ncls; Lc = 0.0
        for c in range(ncls):
            digs = [(c//3**d) % 3 for d in range(k)]; s = (-1.0)**sum(digs)
            sl = slice(c*per, (c+1)*per); Pc = float(tot[sl].sum())/T; num = s*float((tot[sl]*u[sl]).sum())/T
            Lc += num**2/max(Pc,1e-300)
        return Lc
    L1 = coarse(1); L2 = coarse(2)
    print(f"n={n}: Eu2={E:.3e}  d1={E-E1:.3e}  L1={L1:.3e} share={L1/(E-E1):.3f}   d2={E-E2:.3e}  L2={L2:.3e} share={L2/(E-E2):.3f}   d2/Eu2={(E-E2)/E:.3f}")
