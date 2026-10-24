try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
"""Counterexample N2: J(kappa v v^T) grows linearly in N for Gaussian-bump product laws with densities <= 1.

Laws: coordinate i is (1/N) sum_p N(a_ip, s0^2), s0 = 1/(N sqrt(2 pi)) (each bump has height exactly 1), positions
a_ip = p N^{i-1} D / v_i (base-N digits), so L = <v, X> has N^n bumps, all of variance s0^2 (sum v_i^2 = 1), with
distinct centres D * {0, ..., N^n - 1}.  D = C N / |kappa|.
(a) exact grid computation of J (all components, windows of +-9 sd) - n = 2, kappa = 1;
(b) the rigorous lower bound  J >= sum_c w_c (||G_c||_1 - 2 int_{U_c^c} G_c)  (disjoint windows U_c around the
    centres, G_c = modulus of component c, an explicit Gaussian in u), any kappa, n = 2 and n = 4;
(c) the untwisted value: J(0) <= sqrt(2) * 2 pi ||f_1||_2 ||f_2||_2 (n = 2), computed.
"""
import numpy as np, sys, math, time
sys.path.insert(0, '.')
from gmix import components, J_k1_windowed

def laws_for(n, N, D, v):
    s0 = 1.0 / (N * math.sqrt(2 * math.pi))
    laws = []
    for i in range(n):
        a = np.array([p * N ** i * D / v[i] for p in range(N)], float)
        laws.append((np.full(N, 1.0 / N), a, np.full(N, s0)))
    return laws, s0

def max_density(law):
    w, a, s = law
    # bumps separated by >= D/v_i >> s0: the max is attained at a bump centre up to exp(-(sep/s0)^2/2) corrections
    grid = np.concatenate([a_ + np.linspace(-4 * s[0], 4 * s[0], 801) for a_ in a[:3]])
    f = np.zeros_like(grid)
    for p in range(len(w)):
        f += w[p] * np.exp(-(grid - a[p]) ** 2 / (2 * s[p] ** 2)) / math.sqrt(2 * math.pi * s[p] ** 2)
    return f.max()

def envelope_lower_bound(n, N, kappa, C):
    """Rigorous lower bound (b) using the exact modulus of each component (a Gaussian in u)."""
    v = np.full(n, 1 / math.sqrt(n)); D = C * N / abs(kappa)
    s0 = 1.0 / (N * math.sqrt(2 * math.pi))
    alpha = 1 / (2 * s0 ** 2)
    # every component: L-bump N(y_c, s0^2), weight N^{-n}; modulus (alpha/sqrt(alpha^2+kappa^2))^{1/2}
    # * exp(-(u + 2 kappa y_c)^2 / (2 tau^2)), tau^2 = 2 (alpha^2 + kappa^2)/alpha
    h = math.sqrt(alpha / math.sqrt(alpha ** 2 + kappa ** 2)); tau = math.sqrt(2 * (alpha ** 2 + kappa ** 2) / alpha)
    L1 = h * math.sqrt(2 * math.pi) * tau
    sep = 2 * abs(kappa) * D          # centres -2 kappa y_c, y_c in D*Z, all distinct
    tail = math.erfc((sep / 2) / (tau * math.sqrt(2)))   # P(|g| > sep/(2 tau))
    return L1 * (1 - 2 * tail), L1, sep / tau

if __name__ == '__main__':
    t0 = time.time()
    print("(a) exact grid computation, n = 2, v = (1,1)/sqrt2, kappa = 1", flush=True)
    v = np.array([1.0, 1.0]) / math.sqrt(2)
    for C in [4.0, 8.0]:
        for N in [2, 4, 6, 8, 12]:
            kappa = 1.0; D = C * N / kappa
            laws, s0 = laws_for(2, N, D, v)
            W, MU, S = components(laws)
            E = kappa * np.outer(v, v)
            du = min(0.02, 0.1 / (D / math.sqrt(2)))     # resolve neighbour interference
            J = J_k1_windowed(v, E, W, MU, S, du)
            f2 = [ (1.0 / N) / (2 * s0 * math.sqrt(math.pi)) for _ in range(2)]   # ||f||_2^2 for separated bumps
            J0_cs = math.sqrt(2) * 2 * math.pi * math.sqrt(f2[0] * f2[1])
            md = max(max_density(l) for l in laws)
            lb, L1, r = envelope_lower_bound(2, N, kappa, C)
            print(f"  C={C:3.0f} N={N:3d}  J(kappa vv^T) = {J:9.3f}   J/(2 pi N) = {J/(2*math.pi*N):.3f}   "
                  f"rigorous LB = {lb:8.3f}   J(0) <= {J0_cs:.3f}   max density = {md:.6f}   [{time.time()-t0:.0f}s]", flush=True)
    print("(b) rigorous lower bound, any kappa (the bound depends on kappa only through alpha^2 + kappa^2)", flush=True)
    for n in [2, 4]:
        for kappa in [1.0, 0.1, 0.01]:
            row = []
            for N in [5, 10, 20, 40]:
                lb, L1, r = envelope_lower_bound(n, N, kappa, 8.0)
                row.append(f"N={N}: {lb:7.2f}")
            print(f"  n={n} kappa={kappa:5.2f}  " + "   ".join(row), flush=True)
    # (a') n = 4 exact grid, small leverages 1/4
    print("(a') exact grid computation, n = 4, v = (1,1,1,1)/2 (leverages 1/4), kappa = 1, C = 8", flush=True)
    v4 = np.full(4, 0.5)
    for N in [2, 3, 4]:
        kappa = 1.0; D = 8.0 * N
        laws, s0 = laws_for(4, N, D, v4)
        W, MU, S = components(laws)
        E = kappa * np.outer(v4, v4)
        du = min(0.02, 0.1 / D)
        J = J_k1_windowed(v4, E, W, MU, S, du)
        lb, L1, r = envelope_lower_bound(4, N, kappa, 8.0)
        md = max(max_density(l) for l in laws)
        print(f"  N={N}  components={len(W)}  J = {J:8.3f}  J/(2 pi N) = {J/(2*math.pi*N):.3f}  rigorous LB = {lb:7.3f}  max density = {md:.6f}  [{time.time()-t0:.0f}s]", flush=True)
