try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np
exec(open('n1_obstruction.py').read().split("for sigma in")[0])
lam=1.0
for sigma in [0.1, 0.02]:
    for t0 in [2560, 10240, 40960, 163840]:
        xmax = 8*sigma*np.sqrt(1+ (2*t0*sigma*s2)**2)/max(1.0, 2*t0*sigma*s2) + 8/(t0*np.sqrt(s2))
        b, x, f = adversarial(t0, sigma, lam, xmax, N=800001)
        # predicted plateau: (1/pi)*int|Psi| ~ (1/pi) * (2 t sigma s2)^-1/2 (2 t lam s2)^-1/2 * sigma*sqrt(2 pi s2)... compute directly
        xx=np.linspace(-xmax,xmax,800001); I=np.abs(Psi(t0,2*t0*xx,sigma,lam)).sum()*(xx[1]-xx[0])
        print(f"sigma={sigma} t0={t0:7d} t0*adv={t0*b:.4f}  t0*int|Psi(2t0x)|dx={t0*I:.4f}  ratio={b/I:.3f}  t0^1.5*adv={t0**1.5*b:.1f}",flush=True)
