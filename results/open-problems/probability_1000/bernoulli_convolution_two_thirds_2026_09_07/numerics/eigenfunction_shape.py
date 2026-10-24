"""Where does the leading eigenfunction of the tilted operator live?

The eigenvalue 1.335073 governs growth over all of [0,1] while the octave [1/3,2/3] stays flat, so the
eigenfunction should be concentrated away from the octave - near the alignment spike at theta = 0.
Extract it from the power iteration and measure how its mass is distributed.
Sized deliberately: N = 2^14, 400 iterations, one pass, prints flushed.
"""
import numpy as np, sys

N = 1 << 14
y = (np.arange(N) + 0.5) / N
x0 = 2 * y / 3.0
x1 = 2 * (y + 1) / 3.0
w0 = 1.0 + np.cos(2 * np.pi * x0)
w1 = np.where(y < 0.5, 1.0 + np.cos(2 * np.pi * x1), 0.0)
i0 = np.minimum((x0 * N).astype(int), N - 1)
i1 = np.minimum((x1 * N).astype(int), N - 1)

g = np.ones(N)
for it in range(400):
    g = (2.0 / 3.0) * (w0 * g[i0] + w1 * g[i1])
    g /= g.mean()

print(f"leading eigenfunction, normalised to mean 1 on [0,1]")
print(f"  min {g.min():.6f}   max {g.max():.6f}   at theta = {y[int(g.argmax())]:.5f}")
print()
print(f"{'region':>22} {'width':>8} {'mass':>10} {'mass/width':>12}")
for lo, hi, lab in ((0.0,1.0,'all of [0,1]'), (1/3,2/3,'the octave [1/3,2/3]'),
                    (0.0,1/3,'[0,1/3]'), (2/3,1.0,'[2/3,1]'),
                    (0.0,0.05,'[0,0.05] near spike'), (0.0,0.01,'[0,0.01] near spike')):
    sel = (y >= lo) & (y < hi)
    mass = float(g[sel].sum()) / N
    print(f"{lab:>22} {hi-lo:>8.3f} {mass:>10.5f} {mass/(hi-lo):>12.4f}", flush=True)
print()
print("mass/width is the average height: compare the octave against the interval near 0.")
