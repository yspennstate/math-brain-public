try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
np.random.seed(11)
# Theorem H pointwise check: Q = 2 X_h <g, X_I> + lam <r, X_I>^2 + D-twist + a_hh X_h^2, g perp r unit, spread on I.
# Bound: |phi(t)| <= (2|t|)^{-1} (4 pi |t lam|)^{-1/2} (4 pi)^2 det(G~)^{-1/2}, G~ = Gram of rows (r_i, g_i) = I_2.
n = 60
G = np.linalg.qr(np.random.randn(n, 2))[0]
g, r = G[:, 0], G[:, 1]
lev = g**2 + r**2
print(f"max normalised leverage of (r_i, g_i): {lev.max():.3f} (must be <= 1/2)", flush=True)
N = 2_000_000
def comb_sample(N, teeth=5, width=0.2/5):
    # law: uniform on 'teeth' intervals of width 1/teeth spread with gap 1  (density 1)
    k = np.random.randint(0, teeth, N)
    return k * 1.7 + np.random.rand(N) / teeth
lawsets = {"uniform": lambda N: np.random.rand(N) - 0.5, "comb5": comb_sample}
for lawname, sampler in lawsets.items():
    XI = np.column_stack([sampler(N) for _ in range(n)])
    Lg = XI @ g; Lr = XI @ r
    for ahh in [0.0, 3.0]:
        for Dscale in [0.0, 2.0]:
            Dv = Dscale * np.sin(np.arange(n))       # a diagonal twist on I
            quad = (XI**2) @ Dv
            out = []
            for t in [10.0, 20.0, 50.0, 100.0]:
                lam = 1.0
                # E over X_h exactly (uniform or comb): psi_h(2 t Lg) with the X_h^2 term -> numeric for ahh != 0
                if ahh == 0.0:
                    if lawname == "uniform":
                        u = 2 * t * Lg
                        psi = np.where(np.abs(u) < 1e-12, 1.0, np.sin(u / 2) / (u / 2 + 1e-300))
                    else:
                        # comb law: mixture of uniforms on [1.7k, 1.7k + 0.2]
                        u = 2 * t * Lg
                        base = np.where(np.abs(u) < 1e-12, 1.0, np.sin(u * 0.1) / (u * 0.1 + 1e-300)) * np.exp(1j * u * 0.1)
                        psi = base * np.mean([np.exp(1j * u * 1.7 * k) for k in range(5)], axis=0)
                    val = np.mean(psi * np.exp(1j * t * (lam * Lr**2 + quad)))
                else:
                    xh = sampler(N)
                    val = np.mean(np.exp(1j * t * (2 * xh * Lg + ahh * xh**2 + lam * Lr**2 + quad)))
                bound = (2 * t)**-1 * (4 * np.pi * t * lam)**-0.5 * (4 * np.pi)**2
                out.append(f"t={t:5.0f}: |phi|={abs(val):.4f} bound {bound:.4f}")
            print(f"  law={lawname:8s} a_hh={ahh:3.1f} Dscale={Dscale:3.1f}  " + " | ".join(out), flush=True)
print(f"  (Monte Carlo noise ~ {1/np.sqrt(N):.4f})", flush=True)
