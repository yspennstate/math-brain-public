# Curved marginal U + cV^2 versus the maximal functional M_2 for comb laws on a common lattice.
# Each X_i is uniform on N teeth [j, j + 1/N], 0 <= j < N, i.e. X_i = K_i + W_i/N with K_i uniform on {0..N-1}
# and W_i uniform on [0,1]. The lattice part pi(K) = (<a,K>, <b,K>) is computed exactly by integer convolution;
# the cell part (<u,W>, <v,W>)/N is replaced by its Gaussian limit (mean (sum u_i, sum v_i)/(2N), covariance I/(12 N^2)),
# which is accurate to a bounded factor and does not change growth in N.
import sys, math, time
import numpy as np

def lattice_law(a, b, N):
    a = np.asarray(a); b = np.asarray(b)
    pmin = int(N * a[a < 0].sum()) - 1; pmax = int(N * a[a > 0].sum()) + 1
    qmin = int(N * b[b < 0].sum()) - 1; qmax = int(N * b[b > 0].sum()) + 1
    arr = np.zeros((pmax - pmin + 1, qmax - qmin + 1))
    arr[-pmin, -qmin] = 1.0
    for ai, bi in zip(a, b):
        new = np.zeros_like(arr)
        for j in range(N):
            dp, dq = ai * j, bi * j
            src = arr[max(0, -dp):arr.shape[0] - max(0, dp), max(0, -dq):arr.shape[1] - max(0, dq)]
            new[max(0, dp):max(0, dp) + src.shape[0], max(0, dq):max(0, dq) + src.shape[1]] += src
        arr = new / N
    P, Q = np.nonzero(arr > 0)
    w = arr[P, Q]
    return P + pmin, Q + qmin, w

def curved_max(U, V, w, c, sigma, zstep=None):
    # density of U + cV^2: sum of per-point line integrals of Gaussian bumps along the (locally straight) parabola
    Z = U + c * V * V
    s = sigma * np.sqrt(1.0 + 4.0 * c * c * V * V)
    if zstep is None:
        zstep = sigma / 4.0
    z0, z1 = Z.min() - 6 * s.max(), Z.max() + 6 * s.max()
    nz = int((z1 - z0) / zstep) + 1
    dens = np.zeros(nz)
    order = np.argsort(s)
    for chunk in np.array_split(order, max(1, len(order) // 4000)):
        smax = s[chunk].max()
        half = int(6 * smax / zstep) + 1
        idx = ((Z[chunk] - z0) / zstep).astype(int)
        offs = np.arange(-half, half + 1)
        cols = idx[:, None] + offs[None, :]
        cols = np.clip(cols, 0, nz - 1)
        zz = z0 + cols * zstep
        g = np.exp(-0.5 * ((zz - Z[chunk][:, None]) / s[chunk][:, None]) ** 2) / (math.sqrt(2 * math.pi) * s[chunk][:, None])
        np.add.at(dens, cols.ravel(), (w[chunk][:, None] * g).ravel())
    return dens.max()

def m2_estimate(U, V, w, sigma):
    # M_2 = int sup_u rho(u, v) dv, estimated on a v-grid with the bumps of points near each v, u-profile on a grid
    vstep = sigma / 2.0
    ustep = sigma / 3.0
    order = np.argsort(V)
    Vs, Us, ws = V[order], U[order], w[order]
    vgrid = np.arange(Vs.min() - 4 * sigma, Vs.max() + 4 * sigma, vstep)
    total = 0.0
    lo = 0; hi = 0; n = len(Vs)
    for v in vgrid:
        while lo < n and Vs[lo] < v - 4 * sigma:
            lo += 1
        while hi < n and Vs[hi] <= v + 4 * sigma:
            hi += 1
        if hi <= lo:
            continue
        uu = Us[lo:hi]; vv = Vs[lo:hi]; ww = ws[lo:hi]
        wv = ww * np.exp(-0.5 * ((v - vv) / sigma) ** 2) / (math.sqrt(2 * math.pi) * sigma)
        # the u-profile only matters near the points; evaluate at the points and midpoints of close pairs
        cand = np.concatenate([uu, (uu[:, None] + uu[None, :]).ravel() / 2.0]) if len(uu) < 60 else uu
        prof = (wv[None, :] * np.exp(-0.5 * ((cand[:, None] - uu[None, :]) / sigma) ** 2)).sum(axis=1) / (math.sqrt(2 * math.pi) * sigma)
        total += prof.max() * vstep
    return total

def frame(a, b, tan_theta):
    a = np.asarray(a, float); b = np.asarray(b, float)
    ah = a / np.linalg.norm(a); bh = b / np.linalg.norm(b)
    th = math.atan(tan_theta)
    u = math.cos(th) * ah + math.sin(th) * bh
    v = -math.sin(th) * ah + math.cos(th) * bh
    return u, v

def run(name, a, b, tan_theta, Ns, cs):
    u, v = frame(a, b, tan_theta)
    lev = (u * u + v * v).max()
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    th = math.atan(tan_theta)
    print("== %s  (max leverage %.3f, tan theta = %s)" % (name, lev, tan_theta), flush=True)
    for N in Ns:
        t0 = time.time()
        P, Q, w = lattice_law(a, b, N)
        sigma = 1.0 / (math.sqrt(12.0) * N)
        U = math.cos(th) * P / na + math.sin(th) * Q / nb + u.sum() / (2 * N)
        V = -math.sin(th) * P / na + math.cos(th) * Q / nb + v.sum() / (2 * N)
        row = []
        for c in cs:
            row.append(curved_max(U, V, w, c, sigma))
        m2 = m2_estimate(U, V, w, sigma)
        print("N=%3d points=%6d  sup p_{U+cV^2} for c in %s: %s   M_2 ~ %.2f   (%.0fs)"
              % (N, len(w), cs, " ".join("%.3f" % x for x in row), m2, time.time() - t0), flush=True)

if __name__ == "__main__":
    cs = [0.0, 0.001, 0.003, 0.01, 0.03, 0.1]
    Ns = [int(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else [4, 8, 12, 16]
    run("two-class frame of Example 5.2", [1, 1, 1, 1], [1, 1, -1, -1], math.sqrt(2), Ns, cs)
    A8 = [2, -2, -2, -3, -1, -2, 3, 3]; B8 = [2, -3, 3, 2, -3, 2, 2, -1]
    run("rational plane in R^8, eight directions, irrational basis", A8, B8, math.sqrt(2), Ns, cs)
    run("same plane, rational basis", A8, B8, 0.0, Ns, cs)
