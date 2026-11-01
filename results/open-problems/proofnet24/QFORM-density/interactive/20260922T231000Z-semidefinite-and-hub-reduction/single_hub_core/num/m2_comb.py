"""The maximal functional M_2 = int sup_u rho_{V,B}(u, s) ds for two orthonormal projections V = <v,X>, B = <b,X>.

Each X_i is a comb: N teeth of width 1/N at the points 0, K, 2K, ..., (N-1)K (density exactly 1 on the teeth), or,
as the control, uniform on [0, N K] (density 1/(NK), same spread, no fine structure).  The law of (V, B) is the
convolution of the m laws of X_i (v_i, b_i), each supported on a line; it is computed on a grid by rasterising each
line measure and multiplying 2D FFTs.  Printed: M_2 for the comb and for the control, as N grows.
"""
import sys
import numpy as np


def line_measure(grid_n, h, lo, direction, law, N, K, sub=64):
    """Rasterise the law of X_i * direction onto a (grid_n x grid_n) grid with spacing h and lower corner lo."""
    img = np.zeros((grid_n, grid_n))
    if law == "comb":
        t = (np.arange(N)[:, None] * K + (np.arange(sub)[None, :] + 0.5) / (sub * N)).ravel()
        w = np.full(t.size, 1.0 / t.size)
    else:
        t = (np.arange(N * sub * 4) + 0.5) / (N * sub * 4) * (N * K)
        w = np.full(t.size, 1.0 / t.size)
    pts = (t[:, None] * direction[None, :] - lo) / h - 0.5      # cloud-in-cell (bilinear) deposition
    i0 = np.floor(pts).astype(int)
    fr = pts - i0
    for di in (0, 1):
        for dj in (0, 1):
            wt = w * (fr[:, 0] if di else 1 - fr[:, 0]) * (fr[:, 1] if dj else 1 - fr[:, 1])
            ii, jj = i0[:, 0] + di, i0[:, 1] + dj
            ok = (ii >= 0) & (ii < grid_n) & (jj >= 0) & (jj < grid_n)
            np.add.at(img, (ii[ok], jj[ok]), wt[ok])
    return img


def m2(vecs_v, vecs_b, law, N, K, h, cap=4096):
    m = len(vecs_v)
    D = np.stack([vecs_v, vecs_b], 1)                       # m x 2, rows (v_i, b_i)
    span = (np.abs(D).sum(0) * N * K).max() + 4 * h * m
    grid_n = int(2 ** np.ceil(np.log2(span / h + 8)))
    if grid_n > cap:
        return None
    F = None
    for i in range(m):
        lo_i = np.minimum(0, D[i]) * N * K - h              # each line measure gets its own origin
        img = line_measure(grid_n, h, lo_i, D[i], law, N, K)
        G = np.fft.rfft2(img)
        F = G if F is None else F * G
    dens = np.maximum(np.fft.irfft2(F, s=(grid_n, grid_n)), 0) / (h * h)
    total = dens.sum() * h * h
    M2 = dens.max(axis=0).sum() * h                         # sup over u (axis 0 = V), integrate over s (axis 1 = B)
    return M2, total, dens.max(), grid_n


def frames(m, kind, rng):
    if kind == "walsh" and m in (2, 4, 8):
        H = np.array([[1.0]])
        while H.shape[0] < m:
            H = np.block([[H, H], [H, -H]])
        H /= np.sqrt(m)
        return H[1], H[2 % m] if m > 2 else H[0]
    Q, _ = np.linalg.qr(rng.standard_normal((m, 2)))
    return Q[:, 0], Q[:, 1]


if __name__ == "__main__":
    try:
        import psutil
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    rng = np.random.default_rng(1)
    K = 1.0
    cases = [(2, "diag"), (2, "irrat"), (4, "walsh"), (4, "random"), (6, "random"), (8, "random")]
    if len(sys.argv) > 1:
        cases = [c for c in cases if c[1] + str(c[0]) in sys.argv[1:]]
    for m, kind in cases:
        v, b = frames(m, kind, rng)
        if kind == "diag":
            v, b = np.array([1, -1]) / np.sqrt(2), np.array([1, 1]) / np.sqrt(2)
        if kind == "irrat":
            a0 = 0.5 * (np.sqrt(5) - 1)
            v, b = np.array([np.cos(a0), -np.sin(a0)]), np.array([np.sin(a0), np.cos(a0)])
        for N in (4, 8, 16):
            h = 1.0 / (6 * N)
            rc = m2(v, b, "comb", N, K, h)
            if rc is None:
                print(f"m={m} {kind} N={N}: grid too large, skipped", flush=True); continue
            Mc, tc, pc, gn = rc
            Mu, tu, pu, _ = m2(v, b, "unif", N, K, h)
            print(f"m={m} {kind:6s} N={N:2d} grid={gn}  comb: M2={Mc:.3f} peak={pc:.3f} mass={tc:.3f}   "
                  f"uniform[0,NK]: M2={Mu:.4f} peak={pu:.4f}", flush=True)
