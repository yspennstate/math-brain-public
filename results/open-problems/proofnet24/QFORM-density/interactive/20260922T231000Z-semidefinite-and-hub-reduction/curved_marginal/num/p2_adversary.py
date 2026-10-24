# Adversarial search for large values of the curved marginal (P2):
#   p(s) = density of U + c (V - b)^2 at s,  (U, V) = sum_i X_i d_i,
# d_i the columns of a 2 x m orthonormal-row frame with |d_i|^2 <= 1/2, X_i independent comb laws
# (N teeth of width 1/N, density 1 on the teeth).  The two-dimensional density of (U, V) is computed
# exactly up to aliasing and grid interpolation, by FFT of the product of the coordinate transforms.
# A (1+1) evolution strategy moves the tooth gaps to maximise F = max over (c, b, s) of p.
# Reported next to F: the flat marginal max rho_U, the largest line density max over slopes a of
# density(U + a V), and the pair bound min_{i,j} 4(|v_i|+|v_j|)/|u_i v_j - u_j v_i| (Prop 5.1(b) of
# single_hub_core), which caps F for every law.
import sys, time, math, json
import numpy as np

def frame(m, rng, tries=20000):
    for _ in range(tries):
        A = rng.standard_normal((m, 2))
        Qm, _ = np.linalg.qr(A)
        D = Qm.T                      # 2 x m, orthonormal rows
        if np.max(np.sum(D**2, axis=0)) <= 0.5:
            return D
    raise RuntimeError("no frame")

def pair_bound(D):
    u, v = D
    best = np.inf
    m = D.shape[1]
    for i in range(m):
        for j in range(i+1, m):
            det = abs(u[i]*v[j] - u[j]*v[i])
            if det > 1e-12:
                best = min(best, 4*(abs(v[i]) + abs(v[j]))/det)
    return best

class Evaluator:
    def __init__(self, D, N, G, delta, cs, nb):
        self.D, self.N, self.G, self.delta = D, N, G, delta
        self.w = 1.0/N
        k = np.fft.fftfreq(G, d=delta)*2*np.pi
        self.xi_u, self.xi_v = np.meshgrid(k, k, indexing='xy')     # rows: v, cols: u
        self.t = [D[0, i]*self.xi_u + D[1, i]*self.xi_v for i in range(D.shape[1])]
        self.cs, self.nb = cs, nb
    def density(self, pos):
        # pos: m x N tooth left ends
        m = self.D.shape[1]
        Psi = np.ones_like(self.xi_u, dtype=complex)
        centre_u = 0.0; centre_v = 0.0
        for i in range(m):
            t = self.t[i]
            half = self.w/2
            sinc = np.sinc(t*half/np.pi)          # sin(t w/2)/(t w/2)
            s = np.zeros_like(t, dtype=complex)
            for a in pos[i]:
                s += np.exp(1j*t*(a + half))
            Psi *= sinc*s/self.N
            mean_i = np.mean(pos[i]) + half
            centre_u += self.D[0, i]*mean_i; centre_v += self.D[1, i]*mean_i
        L = self.G*self.delta
        x0u = centre_u - L/2; x0v = centre_v - L/2
        Psi *= np.exp(-1j*(self.xi_u*x0u + self.xi_v*x0v))
        rho = np.real(np.fft.fft2(Psi))/(L*L)
        self.x0u, self.x0v = x0u, x0v
        return rho
    def score(self, pos):
        rho = self.density(pos)
        G, d = self.G, self.delta
        ugrid = self.x0u + d*np.arange(G); vgrid = self.x0v + d*np.arange(G)
        mass = rho.sum()*d*d
        rhoU = rho.sum(axis=0)*d                     # marginal of U over the u grid
        best = (0.0, None)
        # lines: density of U + a V at s is  int rho(s - a v, v) dv
        lines = rhoU.max()
        for a in np.linspace(-1.0, 1.0, 9):
            if a == 0: continue
            acc = np.zeros(G)
            for j in range(G):
                acc += np.interp(ugrid - a*vgrid[j], ugrid, rho[j], left=0.0, right=0.0)
            lines = max(lines, acc.max()*d/math.sqrt(1 + a*a))
        # parabolas u = s - c (v - b)^2; density of U + c(V - b)^2 at s
        vmean = np.sum(rho.sum(axis=1)*vgrid)/rho.sum()
        vsd = math.sqrt(max(1e-9, np.sum(rho.sum(axis=1)*(vgrid - vmean)**2)/rho.sum()))
        bs = vmean + vsd*np.linspace(-2, 2, self.nb)
        for c in self.cs:
            for b in bs:
                acc = np.zeros(G)
                sh = c*(vgrid - b)**2
                for j in range(G):
                    acc += np.interp(ugrid - sh[j], ugrid, rho[j], left=0.0, right=0.0)
                val = acc.max()*d
                if val > best[0]:
                    best = (val, (float(c), float(b)))
        return best[0], best[1], lines, rhoU.max(), mass

def random_pos(m, N, rng, gapmax):
    gaps = rng.uniform(0, gapmax, size=(m, N))
    return np.cumsum(gaps + 1.0/N, axis=1) - 1.0/N, gaps

def pos_from_gaps(gaps, N):
    return np.cumsum(gaps + 1.0/N, axis=1) - 1.0/N

def run(m, N, seed, minutes, G=512, delta=0.05, gapmax=1.0, out=None):
    rng = np.random.default_rng(seed)
    D = frame(m, rng)
    pb = pair_bound(D)
    ev = Evaluator(D, N, G, delta, cs=[0.003, 0.01, 0.03, 0.1, 0.3], nb=7)
    pos, gaps = random_pos(m, N, rng, gapmax)
    F, arg, lines, rU, mass = ev.score(pos)
    t0 = time.time(); it = 0; sigma = 0.3
    log = [(0, F, lines, rU, mass, arg)]
    while time.time() - t0 < 60*minutes:
        it += 1
        g2 = np.clip(gaps + sigma*rng.standard_normal(gaps.shape)*(rng.random(gaps.shape) < 0.3), 0, 3*gapmax)
        p2 = pos_from_gaps(g2, N)
        F2, arg2, lines2, rU2, mass2 = ev.score(p2)
        if F2 > F:
            gaps, F, arg, lines, rU, mass = g2, F2, arg2, lines2, rU2, mass2
            sigma = min(1.0, sigma*1.2)
            log.append((it, F, lines, rU, mass, arg))
        else:
            sigma = max(0.02, sigma*0.98)
    res = dict(m=m, N=N, seed=seed, iters=it, F=F, lines=lines, rhoU=rU, mass=mass, arg=arg,
               pair_bound=pb, frame=D.tolist(), gaps=gaps.tolist())
    print(json.dumps({k: res[k] for k in ('m','N','seed','iters','F','lines','rhoU','mass','arg','pair_bound')}), flush=True)
    if out:
        with open(out, 'a', encoding='utf-8') as f:
            f.write(json.dumps(res) + "\n")
    return res

if __name__ == "__main__":
    try:
        import psutil
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    m = int(sys.argv[1]); N = int(sys.argv[2]); seed = int(sys.argv[3]); minutes = float(sys.argv[4])
    out = sys.argv[5] if len(sys.argv) > 5 else None
    run(m, N, seed, minutes, out=out)
