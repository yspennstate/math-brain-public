try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np, time
from famD_spectra import density_spectrum
t0 = time.time()
for h in (4e-4, 1e-4, 2.5e-5):
    c, d = density_spectrum([1, 1, -1], h=h, lo=-3, hi=3); j = int(np.argmax(d))
    print(f"(1,1,-1) h={h:.1e}: max {d[j]:.4f} at s={c[j]:+.5f}   (exact 4.2426 at 0)", flush=True)
for name, lams in {'(1,1,-1)+(.5,-.5,.25,-.25,.125,-.125)': [1, 1, -1, .5, -.5, .25, -.25, .125, -.125],
                   '(1,1,1)+(-.5,-.25,-.125)': [1, 1, 1, -.5, -.25, -.125], '(1,1,-1,-1)': [1, 1, -1, -1],
                   '(1,1,-2)': [1, 1, -2], '(1,2,-1)': [1, 2, -1], '(1,1,1)': [1, 1, 1]}.items():
    c, d = density_spectrum(lams, h=5e-5, lo=-4, hi=4); j = int(np.argmax(d))
    print(f"{name:40s} h=5e-5 max p = {d[j]:.4f} at s = {c[j]:+.4f}  t={time.time()-t0:.0f}", flush=True)
