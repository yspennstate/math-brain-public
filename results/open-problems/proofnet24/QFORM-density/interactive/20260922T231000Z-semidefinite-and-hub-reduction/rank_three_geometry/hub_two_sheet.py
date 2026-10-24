try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Exact conditional estimator for rank-3 forms with one heavy coordinate h:
#   Q = (Y - y0)^T L (Y - y0),  Y = R^T X,  X_h integrated exactly given X_{-h}:
#   Q = a x^2 + 2 M x + C,   p(s) = E[ sum_roots f_h(x) / |2 a x + 2 M| ].
# Hub normal form (frame T, V, U): row h = (sqrt(l), 0, 0), light rows (eps*zeta_i, nu_i, mu_i),
# Ltilde = [[L11, 1, 0], [1, 0, 0], [0, 0, 1]]  (eigenvalues ~ +-1, 1; exactly for L11 = 0).
import numpy as np, sys, time
rng = np.random.default_rng(12345)

def spread_law(K, Lhalf, rng):
    # union of K intervals of length 1/K inside [-Lhalf, Lhalf], total length 1, density 1 on it
    slot = 2 * Lhalf / K
    starts = -Lhalf + slot * np.arange(K) + rng.uniform(0, slot - 1.0 / K, size=K)
    return starts, 1.0 / K

def sample_law(law, size, rng):
    if law[0] == 'unif':
        return rng.uniform(-0.5, 0.5, size=size)
    starts, w = law[1], law[2]
    k = rng.integers(0, len(starts), size=size)
    return starts[k] + rng.uniform(0, w, size=size)

def f_law(law, x):
    if law[0] == 'unif':
        return ((x >= -0.5) & (x <= 0.5)).astype(float)
    starts, w = law[1], law[2]
    out = np.zeros_like(x)
    for st in starts:
        out += ((x >= st) & (x <= st + w))
    return out

def density_heavy(r_h, Rrest, Lt, y0, law_h, laws_rest, svals, N, rng):
    m = Rrest.shape[0]
    X = np.empty((N, m))
    for i in range(m):
        X[:, i] = sample_law(laws_rest[i], N, rng)
    D = X @ Rrest - y0                     # Y' - y0, N x 3
    LD = D @ Lt
    a = r_h @ Lt @ r_h
    M = LD @ r_h
    C = np.einsum('ij,ij->i', D, LD)
    out = []
    for s in svals:
        c = C - s
        if abs(a) < 1e-14:
            with np.errstate(divide='ignore', invalid='ignore'):
                x = -c / (2 * M)
                w = f_law(law_h, x) / np.abs(2 * M)
            w[~np.isfinite(w)] = 0
            vals = w
        else:
            disc = M * M - a * c
            ok = disc > 0
            sq = np.sqrt(np.where(ok, disc, 0.0))
            # stable roots of a x^2 + 2 M x + c = 0
            q = -(M + np.sign(M + (M == 0)) * sq)
            with np.errstate(divide='ignore', invalid='ignore'):
                x1 = q / a
                x2 = c / q
            vals = np.zeros(N)
            for x in (x1, x2):
                with np.errstate(invalid='ignore'):
                    g = np.abs(2 * a * x + 2 * M)
                    w = np.where(ok & np.isfinite(x) & (g > 0), f_law(law_h, np.nan_to_num(x)) / np.where(g > 0, g, 1), 0.0)
                vals += w
        out.append((vals.mean(), vals.std() / np.sqrt(N), vals.max()))
    return np.array(out)

def orth_cols(G):
    Qm, _ = np.linalg.qr(G)
    return Qm

def family(name, m, rng, a=0.0):
    # returns zeta, nu, mu orthonormal in R^m
    if name == 'rand':
        B = orth_cols(rng.standard_normal((m, 3)))
        return B[:, 0], B[:, 1], B[:, 2]
    if name == 'shared':   # zeta, nu share coordinates 0,1 with weight a (hyperbolic Z0*V component)
        G = orth_cols(rng.standard_normal((m - 2, 3)))
        z = np.zeros(m); v = np.zeros(m); u = np.zeros(m)
        z[0] = z[1] = a / np.sqrt(2); v[0] = a / np.sqrt(2); v[1] = -a / np.sqrt(2)
        z[2:] = np.sqrt(1 - a * a) * G[:, 0]; v[2:] = np.sqrt(1 - a * a) * G[:, 1]; u[2:] = G[:, 2]
        return z, v, u
    if name == 'sharedU':  # additionally U and Z0 share coordinate 2 with weight a
        G = orth_cols(rng.standard_normal((m - 4, 3)))
        z = np.zeros(m); v = np.zeros(m); u = np.zeros(m)
        z[0] = z[1] = a / np.sqrt(2); v[0] = a / np.sqrt(2); v[1] = -a / np.sqrt(2)
        z[2] = a / np.sqrt(2); z[3] = 0.0
        u[2] = a / np.sqrt(2); u[3] = a / np.sqrt(2)
        # make z orthogonal to u: z uses e2, u uses e2+e3 -> <z,u> = a^2/2; fix with e3 in z
        z[3] = -a / np.sqrt(2)   # now <z,u> = a^2/2 - a^2/2 = 0, |z part| = a^2 (from 0,1) + a^2 (2,3)
        nz = np.sqrt(1 - 2 * a * a / 2 - 2 * a * a / 2) if a < 0.7 else 0.0
        z[4:] = nz * G[:, 0]; v[4:] = np.sqrt(1 - a * a) * G[:, 1]; u[4:] = np.sqrt(1 - a * a) * G[:, 2]
        # renormalise (keeps orthogonality because supports of the corrections are orthogonal)
        z /= np.linalg.norm(z); v /= np.linalg.norm(v); u /= np.linalg.norm(u)
        return z, v, u
    raise ValueError(name)

def run(fam, a, lval, L11, law_h_name, law_rest_name, m=40, N=300000, seed=1):
    rng = np.random.default_rng(seed)
    z, v, u = family(fam, m, rng, a)
    eps = np.sqrt(max(0.0, 1 - lval))
    r_h = np.array([np.sqrt(lval), 0.0, 0.0])
    Rrest = np.stack([eps * z, v, u], axis=1)
    # sanity: columns of full R orthonormal
    Rfull = np.vstack([r_h, Rrest])
    err = np.abs(Rfull.T @ Rfull - np.eye(3)).max()
    Lt = np.array([[L11, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    y0 = np.zeros(3)
    def mk(nm):
        if nm == 'unif':
            return ('unif',)
        st, w = spread_law(6, 5.0, rng)
        return ('spread', st, w)
    law_h = mk(law_h_name)
    laws_rest = [mk(law_rest_name) for _ in range(m)]
    s_neg = -np.concatenate([np.geomspace(1e-3, 0.05, 8), np.linspace(0.08, 1.5, 18)])
    s_pos = -s_neg
    rn = density_heavy(r_h, Rrest, Lt, y0, law_h, laws_rest, s_neg, N, rng)
    rp = density_heavy(r_h, Rrest, Lt, y0, law_h, laws_rest, s_pos, N, rng)
    kn = np.argmax(rn[:, 0]); kp = np.argmax(rp[:, 0])
    print(f"{fam:8s} a={a:4.2f} l={lval:8.6f} eps={eps:7.4f} L11={L11:+5.2f} h={law_h_name:6s} rest={law_rest_name:6s} "
          f"| two-sheet sup {rn[kn,0]:6.3f} +- {rn[kn,1]:5.3f} at s={s_neg[kn]:+7.4f} "
          f"| one-sheet sup {rp[kp,0]:6.3f} +- {rp[kp,1]:5.3f} at s={s_pos[kp]:+7.4f} | orth err {err:.1e}", flush=True)
    return rn, rp

if __name__ == '__main__':
    t0 = time.time()
    ls = [0.5, 0.9, 0.99, 0.999, 0.9999, 1.0]
    for fam, a in [('rand', 0.0), ('shared', 0.6), ('shared', 0.9)]:
        for law in [('unif', 'unif'), ('spread', 'spread'), ('unif', 'spread')]:
            for lval in ls:
                run(fam, a, lval, 0.0, law[0], law[1])
            print(f"   elapsed {time.time()-t0:6.1f}s", flush=True)
    for L11 in [0.05, -0.05, 0.2]:
        for lval in [0.9, 0.999, 1.0]:
            run('shared', 0.6, lval, L11, 'unif', 'unif')
    print(f"total {time.time()-t0:6.1f}s", flush=True)
