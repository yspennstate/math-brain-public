"""Sharp prediction: the leading EIGENMEASURE must give (almost) no mass to the octave.

int L^K h = int h e^(S_K phi), and L^K h ~ lambda^K nu(h) g with g the right eigenfunction and nu the
left one (the eigenmeasure). So
    I_K = int_(1/3)^(2/3) e^(S_K phi) ~ lambda^K nu([1/3,2/3]) int g.
I_K is flat at 0.043 to K = 37 while lambda = 1.335 (1.335^37 = 1.5e4), so nu([1/3,2/3]) must be zero or
vanishingly small. Compute the left eigenvector by power-iterating the TRANSPOSE and measure its mass on
the octave. Sized: N = 2^13, 400 iterations.
"""
import numpy as np

N = 1 << 13
y = (np.arange(N) + 0.5) / N
x0 = 2 * y / 3.0
x1 = 2 * (y + 1) / 3.0
w0 = 1.0 + np.cos(2 * np.pi * x0)
w1 = np.where(y < 0.5, 1.0 + np.cos(2 * np.pi * x1), 0.0)
i0 = np.minimum((x0 * N).astype(int), N - 1)
i1 = np.minimum((x1 * N).astype(int), N - 1)

# right eigenfunction
g = np.ones(N)
for _ in range(400):
    g = (2.0/3.0) * (w0 * g[i0] + w1 * g[i1]); g /= g.mean()

# left eigenvector: transpose action, v -> scatter of v * weight back to the preimage cells
v = np.ones(N)
for _ in range(400):
    nv = np.zeros(N)
    np.add.at(nv, i0, (2.0/3.0) * w0 * v)
    np.add.at(nv, i1, (2.0/3.0) * w1 * v)
    v = nv / max(nv.sum(), 1e-300)

print("leading eigenMEASURE nu (left eigenvector, normalised to total mass 1):")
print(f"  concentrated at theta = {y[int(v.argmax())]:.5f}, peak share {v.max():.6f}")
print()
print(f"{'region':>24} {'nu(region)':>14}")
for lo, hi, lab in ((0.0,1.0,'all of [0,1]'), (1/3,2/3,'the octave [1/3,2/3]'),
                    (0.0,1/3,'[0,1/3]'), (2/3,1.0,'[2/3,1]'),
                    (0.0,0.01,'[0,0.01]'), (0.0,0.001,'[0,0.001]')):
    sel = (y >= lo) & (y < hi)
    print(f"{lab:>24} {float(v[sel].sum()):>14.8f}")
print()
print("If nu(octave) is orders below nu([0,1/3]), the localisation is confirmed in the sharpest form.")
