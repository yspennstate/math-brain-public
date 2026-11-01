"""T357, GD: why t_FM - t_OC scatters across seeds. On the late path kappa_hat - kappa(t) = K0 exp(-i_par t), so
exp(-i_par t_X) = (kappa_hat - kappa_X)/K0. If the crossings sit at deterministic kappa positions and only kappa_hat is noisy,
D = exp(-i_par t_OC) - exp(-i_par t_FM) = (kappa_FM - kappa_OC)/K0 is the same on every seed while L = exp(-i_par t_FM) is not,
and the time gap ln(1 + D/L)/i_par inherits the noise of L. Prints D, L and their coefficients of variation per run file.
argv: gd_gap output files"""
import sys, re, math
import numpy as np
IPAR = 0.06053  # beta 2
for f in sys.argv[1:]:
    rows = [tuple(map(float, m)) for m in re.findall(r"t_OC ([\d.]+)\s+t_FM ([\d.]+)", open(f).read())]
    if len(rows) < 2:
        continue
    oc, fm = np.array(rows).T
    D = np.exp(-IPAR * oc) - np.exp(-IPAR * fm); L = np.exp(-IPAR * fm); gap = fm - oc
    cv = lambda a: a.std(ddof=1) / a.mean()
    print(f"{f}: seeds {len(oc)}  gap mean {gap.mean():.3f} median {np.median(gap):.3f} range {gap.min():.3f}..{gap.max():.3f}")
    print(f"   D = e^-i t_OC - e^-i t_FM: mean {D.mean():.5f} cv {cv(D):.3f}   L = e^-i t_FM: mean {L.mean():.5f} cv {cv(L):.3f}"
          f"   corr(gap, t_FM) {np.corrcoef(gap, fm)[0, 1]:+.3f}   gap at mean L: {math.log(1 + D.mean() / L.mean()) / IPAR:.3f}")
