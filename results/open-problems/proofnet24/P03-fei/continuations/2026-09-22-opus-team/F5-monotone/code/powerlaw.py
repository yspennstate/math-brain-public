"""H/I for power-law weights w_i = i^-a, several thresholds, n up to 24."""
import sys, numpy as np, time
from ltf_core import ltf_table, spectrum, HI, linform
ns = [int(a) for a in sys.argv[1].split(',')]
for a in [0.3, 0.5, 0.7, 1.0]:
    for n in ns:
        w = np.arange(1, n+1, dtype=np.float64)**(-a)
        w = w + 1e-9*np.sin(np.arange(n)*1.7)  # generic
        v = linform(w); sd = np.linalg.norm(w)
        row = []
        for t in [0.0, 1.0, 2.0, 3.0]:
            th = t*sd + 1e-7
            f = ltf_table(w, th); c = spectrum(f); H, I = HI(c)
            row.append("t=%.0f p=%.3g H/I=%.4f I=%.3f" % (t, (1-c[0])/2, H/I, I))
        print("a=%.1f n=%d | %s" % (a, n, " | ".join(row)), flush=True)
