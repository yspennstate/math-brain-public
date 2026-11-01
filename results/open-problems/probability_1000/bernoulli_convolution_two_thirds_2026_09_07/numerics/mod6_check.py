# Machine check of the mod-6 reformulation of the contraction, against the direct fibre statistics.
# Level N = n+2: a = floor(2^N Y), t = frac(2^N Y), q_a(t) fibre weights; m = a + 2^(n+1) B, B fair.
# Claim: u_{n+1}(t) = E[(-1)^m | t]  and  E[u_n^2] = E_t sum_r P(r|t) E[(-1)^m | m=r mod 3, t]^2,
#        E[(Au_n)^2] = E_t (E[(-1)^m | t])^2.  Compare with exact_depth.fibre_stats on the same density.
import numpy as np, math, sys
sys.argv = [sys.argv[0]] + (sys.argv[1:] or ["20", str(3 * 2**18)])
exec(open("exact_depth.py").read().split("starts = prefix_starts(D)")[0])   # defs only
D = int(sys.argv[1]); R = int(sys.argv[2])
starts = prefix_starts(D); L = lam**D
g = density_on_grid(starts, L, R)
print(f"D={D} R={R} cells/interval={L*R:.1f}")
gg = g
for n in range(0, 5):
    # direct (exact_depth) statistics of u_n on the current folded density gg (law of frac(2^n Y))
    j, EVar, Eu2, Em2 = fibre_stats(gg)
    # mod-6 form from the ORIGINAL density g at level N = n+2
    N = n + 2; K = 2**N; per = R // K            # t-cells per preimage
    q = g.reshape(K, per)                          # q[a, t] masses
    sh = 2**(n+1)
    M = K + sh
    w = np.zeros((M, per)); w[:K] += 0.5 * q; w[sh:sh+K] += 0.5 * q
    mass_t = w.sum(axis=0)
    sign = np.array([(-1.0)**m for m in range(M)])[:, None]
    Au = (sign * w).sum(axis=0) / np.maximum(mass_t, 1e-300)
    Em2_mod6 = float((mass_t * Au**2).sum() / mass_t.sum())
    Eu2_mod6 = 0.0
    for r in range(3):
        idx = np.arange(r, M, 3)
        Pr = w[idx].sum(axis=0); Vr = (sign[idx] * w[idx]).sum(axis=0) / np.maximum(Pr, 1e-300)
        Eu2_mod6 += float((Pr * Vr**2).sum() / mass_t.sum())
    print(f"n={n}: direct Eu2={Eu2:.6e} Em2={Em2:.6e}   mod6 Eu2={Eu2_mod6:.6e} Em2={Em2_mod6:.6e}   "
          f"ratio Em2/Eu2={Em2/Eu2:.4f} (mod6 {Em2_mod6/Eu2_mod6:.4f})   j_n={j:.6f}")
    gg = gg[:gg.size//2] + gg[gg.size//2:]
