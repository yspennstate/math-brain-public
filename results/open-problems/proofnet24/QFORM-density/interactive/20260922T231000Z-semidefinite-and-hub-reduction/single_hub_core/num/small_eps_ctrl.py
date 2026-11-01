"""Control for small_eps.py: the same rough hub (cells of length c) with the cross term at eps = c and at eps = 0,
on one fixed frame per row, so that a change along the row can be attributed to the cross term or to the hub law."""
import sys
import numpy as np
import small_eps as se  # the probe in this folder

def peak_fixed(cells, eps, xsFs, lawkind, frame, lam=1.0, nsamp=3_000_000, B=200_000):
    xs, Fs = xsFs
    w, v, p = frame
    delta = 0.002
    ys = np.concatenate([np.linspace(-1.5, 1.5, 121), np.linspace(-0.1, 0.1, 101)])
    acc = np.zeros_like(ys); done = 0
    while done < nsamp:
        X = se.light(lawkind, (B, len(w)))
        L, V, P = X @ w, X @ v, X @ p
        R = lam * V * V + 2 * eps * L * P
        s = 2 * L; s = np.where(np.abs(s) < 1e-12, 1e-12, s)
        for j, y in enumerate(ys):
            x1 = (y - R - delta) / s; x2 = (y - R + delta) / s
            acc[j] += np.abs(np.interp(x2, xs, Fs) - np.interp(x1, xs, Fs)).sum()
        done += B
    dens = acc / done / (2 * delta)
    return dens.max()

if __name__ == "__main__":
    framekind = sys.argv[1]; m = int(sys.argv[2])
    frame = se.frames(framekind, m)
    for lawkind in ("unif", "comb"):
        out = []
        for c in (0.1, 0.03, 0.01, 0.003):
            h = se.hub_cdf("rough", c)
            d1 = peak_fixed(c, c, h, lawkind, frame); d0 = peak_fixed(c, 0.0, h, lawkind, frame)
            out.append(f"c={c}: eps=c {d1:.3f} / eps=0 {d0:.3f}")
        print(f"{framekind} m={m} light={lawkind} rough hub, one frame:  " + "  ".join(out), flush=True)
    print("done", flush=True)
