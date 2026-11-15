# Local log-log slopes of the annealed MSD and the return probability from the exact GPU runs,
# with a bootstrap over environments. Evidence for I0001 (annealed MSD ~ t^{4/3}?), not a proof.
import sys
import numpy as np

for path in sys.argv[1:]:
    z = np.load(path)
    T = int(z["T"]); msd = z["msd"]; t = z["msd_t"]; ret = z["ret"]
    n = msd.shape[0]
    rng = np.random.default_rng(1)
    print(f"{path}: T={T} envs={n}")
    edges = [T // 16, T // 8, T // 4, T // 2, T]
    for a, b in zip(edges[:-1], edges[1:]):
        k = (t >= a) & (t <= b)
        ev = np.arange(2 * (a // 2), b + 1, 2)
        boots_m, boots_p = [], []
        for _ in range(400):
            s = rng.integers(0, n, n)
            boots_m.append(np.polyfit(np.log(t[k]), np.log(msd[s][:, k].mean(0)), 1)[0])
            boots_p.append(np.polyfit(np.log(ev), np.log(ret[s][:, ev].mean(0)), 1)[0])
        m0 = np.polyfit(np.log(t[k]), np.log(msd[:, k].mean(0)), 1)[0]
        p0 = np.polyfit(np.log(ev), np.log(ret[:, ev].mean(0)), 1)[0]
        print(f"  t in [{a},{b}]: msd slope {m0:.4f} (+-{np.std(boots_m):.4f})   p_t(0,0) slope {p0:.4f} (+-{np.std(boots_p):.4f})")
