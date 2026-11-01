# Independent method: iterate the stationary equation Y = (2Y' + B)/3 on a cell grid (piecewise-linear cumulative
# interpolation), then compute the fibre statistics at levels n = 0..NMAX. Cross-checks exact_depth (prefix densities).
import numpy as np, math, sys, time
R = int(sys.argv[1]) if len(sys.argv) > 1 else 3 * 2**20
ITERS = int(sys.argv[2]) if len(sys.argv) > 2 else 90
NMAX = int(sys.argv[3]) if len(sys.argv) > 3 else 9
t0 = time.time()
c = np.full(R, 1.0 / R)                      # start uniform
edges = np.arange(R + 1) / R
for it in range(ITERS):
    F = np.concatenate([[0.0], np.cumsum(c)])   # cumulative at cell edges
    new = np.zeros(R)
    for B in (0, 1):
        a = (3 * edges[:-1] - B) / 2; b = (3 * edges[1:] - B) / 2
        Fa = np.interp(a, edges, F, left=0.0, right=1.0); Fb = np.interp(b, edges, F, left=0.0, right=1.0)
        new += 0.5 * (Fb - Fa)
    delta = float(np.abs(new - c).sum()); c = new / new.sum()
print(f"R={R} iters={ITERS} last L1 step={delta:.2e}  mass={c.sum():.12f}  {time.time()-t0:.1f}s")
np.save(f"stationary_density_R{R}.npy", c)
# density L2 and shape
print(f"int f^2 (grid) = {float(np.sum((c*R)**2)/R):.6f}   max f = {float((c*R).max()):.4f}")
def fibre_stats(mass):
    Rr = mass.size; half = Rr // 2
    m0 = mass[:half]; m1 = mass[half:]; tot = m0 + m1
    p1 = np.where(tot > 0, m1 / np.maximum(tot, 1e-300), 0.5)
    with np.errstate(divide='ignore', invalid='ignore'):
        h = -(p1*np.log(p1) + (1-p1)*np.log(1-p1)); h = np.nan_to_num(h)
    j = math.log(2) - float(np.sum(tot*h)) / float(np.sum(tot))
    u = np.where(tot > 0, (m0 - m1)/np.maximum(tot, 1e-300), 0.0)
    q = half // 3; tz = tot.reshape(3, q); uz = u.reshape(3, q)
    V = np.array([1.0, -1.0, 1.0])[:, None] * uz
    massw = tz.sum(axis=0); p = tz/np.maximum(massw, 1e-300)
    Em2 = float(np.sum(massw*((p*V).sum(axis=0))**2))/float(np.sum(massw))
    Eu2 = float(np.sum(tot*u**2))/float(np.sum(tot))
    return j, Eu2, Em2
g = c; rows = []
for n in range(NMAX + 1):
    if (g.size // 2) % 3 or g.size < 96: break
    j, Eu2, Em2 = fibre_stats(g); rows.append((n, j, Eu2, Em2))
    print(f"n={n}: j={j:.6e}  Eu2={Eu2:.4e}  Em2={Em2:.4e}  one-step ratio={Em2/Eu2:.4f}")
    g = g[:g.size//2] + g[g.size//2:]
print("sum j =", sum(r[1] for r in rows))
print("two-step products:", [round(rows[i][3]/rows[i][2] * rows[i+1][3]/rows[i+1][2], 4) for i in range(len(rows)-1)])
