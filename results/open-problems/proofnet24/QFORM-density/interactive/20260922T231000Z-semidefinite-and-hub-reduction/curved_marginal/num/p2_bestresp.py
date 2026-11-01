# Best-response adversary for the curved marginal (P2).
#   F = density of U + c (V - b)^2 at s,  (U, V) = sum_i X_i a_i,  a_i = (u_i, v_i),
# u, v orthonormal in R^m with u_i^2 + v_i^2 <= 1/2, X_i independent with densities at most 1.
# F is linear in each law f_i: F = int f_i(x) h_i(x) dx, where h_i(x) is the curved marginal of
# Z_{-i} = sum_{j != i} X_j a_j along the parabola moved by -x a_i. Over densities at most 1 the best f_i is the
# indicator of a top level set of h_i of measure 1 (bathtub). Coordinate ascent with these exact best responses
# searches all laws that are unions of cells of width dx, not only laws with a few teeth. Between sweeps the
# parabola is re-chosen: axis direction (8 rotations of the frame), c of both signs, vertex b and level s.
# Restarts from random laws until the time is up; the best law found is then evaluated on the grid, against the
# largest density of a linear form over 360 directions (p2_lines.py; the flat bound is sqrt 2), and by Monte Carlo.
# mode "line" runs the same ascent for the density of a linear form (c = 0, the direction re-chosen each sweep):
# it calibrates the search, since the flat optimum on a given frame is known to be at most sqrt 2.
#
# Densities of partial sums are computed on a 2-D grid by rasterising each law onto its line (linear deposit)
# and convolving by FFT; this is a discretisation at the grid spacing, checked at the end by Monte Carlo.
import sys, time, json, math
import numpy as np
from p2_lines import line_max

def frame(m, rng, tries=20000):
    for _ in range(tries):
        A = rng.standard_normal((m, 2))
        Qm, _ = np.linalg.qr(A)
        D = Qm.T
        if np.max(np.sum(D**2, axis=0)) <= 0.5:
            return D
    raise RuntimeError("no frame")

def named_frame(name):
    # frames from single_hub_core/num (p2_lattice.py): the two-class frame of Example 5.2 and a rational plane in R^8,
    # each rotated by tan theta = sqrt 2
    if name == 'twoclass':
        u0 = np.array([1, 1, 1, 1])/2.0; v0 = np.array([1, 1, -1, -1])/2.0
    elif name == 'rational8':
        a = np.array([2, -2, -2, -3, -1, -2, 3, 3], float); b = np.array([2, -3, 3, 2, -3, 2, 2, -1], float)
        u0 = a/np.linalg.norm(a); v0 = b/np.linalg.norm(b)
    else:
        raise ValueError(name)
    th = math.atan(math.sqrt(2.0))
    return np.vstack([math.cos(th)*u0 + math.sin(th)*v0, -math.sin(th)*u0 + math.cos(th)*v0])

def comb_laws(m, grid, N):
    # N teeth of width 1/N at the integers, centred on 0 (density 1 on the teeth)
    nx = len(grid.x); laws = []
    for i in range(m):
        f = np.zeros(nx)
        for k in range(N):
            left = k - (N - 1)/2.0 - 0.5/N
            f[(grid.x >= left) & (grid.x < left + 1.0/N)] = 1.0
        laws.append(f*(grid.ncell/max(1, int(f.sum())))) if abs(f.sum() - grid.ncell) > 0.5 else laws.append(f)
    return laws

def rot(D, t):
    c, s = math.cos(t), math.sin(t)
    return np.array([[c, s], [-s, c]]) @ D

class Grid:
    def __init__(self, G, delta, xmax, dx):
        self.G, self.d = G, delta
        self.L = G*delta
        self.x = np.arange(-xmax, xmax, dx) + dx/2
        self.dx = dx
        self.ncell = int(round(1.0/dx))
        self.c0 = -self.L/2
        self.g = self.c0 + delta*np.arange(G)

    def raster(self, f, a):
        w = f*self.dx
        keep = w > 0
        xs = self.x[keep]; w = w[keep]
        pu = (xs*a[0] - self.c0)/self.d; pv = (xs*a[1] - self.c0)/self.d
        iu = np.floor(pu).astype(int); iv = np.floor(pv).astype(int)
        fu = pu - iu; fv = pv - iv
        R = np.zeros((self.G, self.G))
        for du, wu in ((0, 1 - fu), (1, fu)):
            for dv, wv in ((0, 1 - fv), (1, fv)):
                ju = iu + du; jv = iv + dv
                ok = (ju >= 0) & (ju < self.G) & (jv >= 0) & (jv < self.G)
                np.add.at(R, (jv[ok], ju[ok]), (w*wu*wv)[ok])
        return R

    def density(self, FTs):
        # grid density (per unit area) of the sum of the rasterised laws whose transforms are FTs
        P = np.ones_like(FTs[0])
        for Fi in FTs:
            P = P*Fi
        p = np.fft.irfft2(P, s=(self.G, self.G))
        # each raster has origin c0; the k-fold circular convolution sits at origin k c0 = -k L/2, i.e. it must
        # be rolled by G/2 when k - 1 is odd
        if (len(FTs) - 1) % 2 == 1:
            p = np.fft.fftshift(p)
        return np.maximum(p, 0.0)/(self.d*self.d)

def curve_vals(rho, grid, c, b, s_vals):
    out = np.zeros(len(s_vals))
    for j in range(grid.G):
        out += np.interp(s_vals - c*(grid.g[j] - b)**2, grid.g, rho[j], left=0.0, right=0.0)
    return out*grid.d

def best_response_h(rho_m, grid, c, b, s, a):
    X = grid.x
    h = np.zeros(len(X))
    for j in range(grid.G):
        uq = s - X*a[0] - c*(grid.g[j] + X*a[1] - b)**2
        h += np.interp(uq, grid.g, rho_m[j], left=0.0, right=0.0)
    return h*grid.d

def random_laws(m, grid, rng):
    nx = len(grid.x)
    laws = []
    for i in range(m):
        f = np.zeros(nx)
        span = int(nx*rng.uniform(0.1, 0.8)); start = rng.integers(0, nx - span + 1)
        k = rng.integers(1, 6)                         # a few clusters of random cells, or scattered cells
        if rng.random() < 0.5:
            idx = start + rng.choice(span, size=grid.ncell, replace=False)
        else:
            centres = start + rng.choice(span, size=k, replace=False)
            idx = np.unique(np.clip(np.concatenate([c + np.arange(grid.ncell//k + 1) for c in centres]), 0, nx - 1))
            if len(idx) < grid.ncell:
                rest = np.setdiff1d(np.arange(nx), idx)
                idx = np.concatenate([idx, rng.choice(rest, size=grid.ncell - len(idx), replace=False)])
            idx = idx[:grid.ncell]
        f[idx] = 1.0
        laws.append(f)
    return laws

def choose_curve(laws, D0, grid, cs, nrot=8):
    best = (0.0, None)
    for t in np.linspace(0, math.pi, nrot, endpoint=False):
        D = rot(D0, t); A = D.T
        rho = grid.density([np.fft.rfft2(grid.raster(laws[i], A[i])) for i in range(len(laws))])
        vm_ = rho.sum(axis=1); vm = float(np.sum(vm_*grid.g)/vm_.sum())
        vs = float(math.sqrt(np.sum(vm_*(grid.g - vm)**2)/vm_.sum()))
        s_vals = grid.g[grid.G//8: 7*grid.G//8]
        for c in list(cs) + [-c for c in cs]:
            for b in vm + vs*np.linspace(-2, 2, 5):
                vals = curve_vals(rho, grid, c, b, s_vals)
                k = int(np.argmax(vals))
                if vals[k] > best[0]:
                    best = (float(vals[k]), (float(t), float(c), float(b), float(s_vals[k])))
    return best

def choose_line(laws, D0, grid):
    A = D0.T
    rho = grid.density([np.fft.rfft2(grid.raster(laws[i], A[i])) for i in range(len(laws))])
    val, t = line_max(rho, grid.c0, grid.d, ndir=90)
    # the level r of the maximum, in the frame rotated so that the line is u' = r
    D = rot(D0, t); Ar = D.T
    rho2 = grid.density([np.fft.rfft2(grid.raster(laws[i], Ar[i])) for i in range(len(laws))])
    s_vals = grid.g[grid.G//8: 7*grid.G//8]
    vals = curve_vals(rho2, grid, 0.0, 0.0, s_vals)
    k = int(np.argmax(vals))
    return float(vals[k]), (float(t), 0.0, 0.0, float(s_vals[k]))

def ascend(laws, D0, grid, cs, mode, rng, deadline, max_sweeps=40, patience=3):
    m = len(laws)
    best = (0.0, None, None); stall = 0; sweeps = 0
    while sweeps < max_sweeps and time.time() < deadline:
        F, par = choose_curve(laws, D0, grid, cs) if mode == 'curve' else choose_line(laws, D0, grid)
        sweeps += 1
        if F > best[0] + 1e-6:
            best = (F, par, [l.copy() for l in laws]); stall = 0
        else:
            stall += 1
            if stall >= patience:
                break
        t, c, b, s = par
        D = rot(D0, t); A = D.T
        FT = [np.fft.rfft2(grid.raster(laws[i], A[i])) for i in range(m)]
        for i in rng.permutation(m):
            rho_m = grid.density([FT[j] for j in range(m) if j != i])
            h = best_response_h(rho_m, grid, c, b, s, A[i])
            top = np.argpartition(-h, grid.ncell)[:grid.ncell]
            f = np.zeros(len(grid.x)); f[top] = 1.0
            laws[i] = f
            FT[i] = np.fft.rfft2(grid.raster(f, A[i]))
    return best, sweeps

def mc_check(D, laws, grid, c, b, s, seed, n=4_000_000, chunk=500_000):
    rng = np.random.default_rng(seed)
    m = D.shape[1]
    cells = [grid.x[laws[i] > 0] - grid.dx/2 for i in range(m)]
    hits = {0.02: 0, 0.01: 0}; done = 0
    while done < n:
        k = min(chunk, n - done)
        X = np.empty((k, m))
        for i in range(m):
            X[:, i] = cells[i][rng.integers(0, len(cells[i]), size=k)] + rng.uniform(0, grid.dx, size=k)
        Y = X @ D[0] + c*(X @ D[1] - b)**2
        for h in hits:
            hits[h] += int(np.sum(np.abs(Y - s) < h))
        done += k
    return [hits[h]/n/(2*h) for h in (0.02, 0.01)]

def run(m, seed, minutes, mode='curve', G=1024, delta=0.05, xmax=6.0, dx=1/64, out=None,
        cs=(0.003, 0.01, 0.03, 0.1, 0.3), frame_name=None, init=None):
    rng = np.random.default_rng(seed)
    D0 = named_frame(frame_name) if frame_name else frame(m, rng)
    m = D0.shape[1]
    grid = Grid(G, delta, xmax, dx)
    t0 = time.time(); deadline = t0 + 60*minutes
    overall = (0.0, None, None); restarts = 0; log = []
    while time.time() < deadline:
        restarts += 1
        if restarts == 1 and init and init.startswith('comb'):
            laws = comb_laws(m, grid, int(init[4:]))
        elif restarts == 1 and init == 'interval':
            laws = comb_laws(m, grid, 1)
        else:
            laws = random_laws(m, grid, rng)
        (F, par, L), sw = ascend(laws, D0, grid, cs, mode, rng, deadline)
        log.append(dict(restart=restarts, F=F, par=par, sweeps=sw, t=round(time.time() - t0)))
        print(json.dumps(log[-1]), flush=True)
        if F > overall[0]:
            overall = (F, par, L)
    F, par, L = overall
    t, c, b, s = par
    D = rot(D0, t); A = D.T
    rho = grid.density([np.fft.rfft2(grid.raster(L[i], A[i])) for i in range(m)])
    s_vals = grid.g[grid.G//8: 7*grid.G//8]
    vals = curve_vals(rho, grid, c, b, s_vals); k = int(np.argmax(vals))
    Fg, sg = float(vals[k]), float(s_vals[k])
    lm, lt = line_max(rho, grid.c0, grid.d, ndir=360)
    mc = mc_check(D, L, grid, c, b, sg, seed + 1000)
    res = dict(m=m, seed=seed, mode=mode, frame_name=frame_name, init=init, restarts=restarts, F_grid=Fg, mc=mc, line_max=lm, line_dir=lt,
               ratio=Fg/lm, rot=t, c=c, b=b, s=sg, mass=float(rho.sum()*grid.d**2), G=G, delta=delta, xmax=xmax,
               dx=dx, frame=D0.tolist(), laws=[np.flatnonzero(l).tolist() for l in L], log=log)
    print(json.dumps({k2: res[k2] for k2 in ('m', 'seed', 'mode', 'restarts', 'F_grid', 'mc', 'line_max', 'ratio',
                                              'rot', 'c', 'b', 's', 'mass')}), flush=True)
    if out:
        with open(out, 'a', encoding='utf-8') as fo:
            fo.write(json.dumps(res) + "\n")
    return res

if __name__ == "__main__":
    try:
        import psutil, os
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        psutil.Process().cpu_affinity(list(range(2, os.cpu_count())))     # off the owner's cores 0 and 1
    except Exception:
        pass
    m = int(sys.argv[1]); seed = int(sys.argv[2]); minutes = float(sys.argv[3]); mode = sys.argv[4]
    out = sys.argv[5] if len(sys.argv) > 5 else None
    G = int(sys.argv[6]) if len(sys.argv) > 6 else 1024
    cs = tuple(float(x) for x in sys.argv[7].split(',')) if len(sys.argv) > 7 and sys.argv[7] != '-' else (0.003, 0.01, 0.03, 0.1, 0.3)
    frame_name = sys.argv[8] if len(sys.argv) > 8 and sys.argv[8] != '-' else None
    init = sys.argv[9] if len(sys.argv) > 9 else None
    run(m, seed, minutes, mode=mode, G=G, out=out, cs=cs, frame_name=frame_name, init=init)
