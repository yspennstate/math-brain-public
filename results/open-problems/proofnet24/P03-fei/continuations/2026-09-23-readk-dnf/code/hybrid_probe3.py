import numpy as np, math
import hybrid
hybrid.JCUT = 1e-250
for n in (5, 7):
    for t in range(1, n + 1):
        for side in (-1, 1):
            vals = []
            for e in (1e-3, 1e-6, 1e-9, 1e-12):
                try:
                    r = hybrid.analyse(np.ones(n), 2 * t - n - 1.0, np.full(n, side * (1 - 2 * e)))
                    vals.append(r['ratio'] if r else float('nan'))
                except AssertionError as ex:
                    vals.append(float('nan'))
            print(f"thr {t}/{n} {'p=1-eps' if side > 0 else 'p=eps  '}: " + " ".join(f"{v:6.2f}" for v in vals), flush=True)
