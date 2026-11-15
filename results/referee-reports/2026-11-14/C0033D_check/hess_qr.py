# Independent check of C0033D Theorem 2: ambient 9-dim entropy Hessian at Q_r, by central finite differences
# in mpmath (60 digits), using only p_S = (-1)^{|S^c|} det(Q - I_{S^c}).
import itertools, sys
import mpmath as mp
mp.mp.dps = 60

def atoms(Q):
    out = []
    for s in itertools.product([0, 1], repeat=3):
        M = Q.copy()
        for i in range(3):
            if not s[i]:
                M[i, i] -= 1
        out.append(((-1) ** (3 - sum(s))) * mp.re(mp.det(M)))
    return out

def H(Q):
    return -sum(p * mp.log(p) for p in atoms(Q))

def basis():
    B = []
    for i in range(3):
        E = mp.zeros(3); E[i, i] = 1; B.append(E)
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        E = mp.zeros(3); E[i, j] = E[j, i] = 1 / mp.sqrt(2); B.append(E)
        E = mp.zeros(3); E[i, j] = 1j / mp.sqrt(2); E[j, i] = -1j / mp.sqrt(2); B.append(E)
    return B

def Qr(r):
    return mp.matrix([[0.5, 1j * r, -1j * r], [-1j * r, 0.5, 1j * r], [1j * r, -1j * r, 0.5]])

B = basis()
h = mp.mpf("1e-15")
for r in [mp.mpf(x) for x in sys.argv[1:]]:
    Q = Qr(r)
    ps = atoms(Q)
    n = 9
    Hm = mp.zeros(n)
    for a in range(n):
        for b in range(a, n):
            f = lambda sa, sb: H(Q + sa * h * B[a] + sb * h * B[b])
            v = (f(1, 1) - f(1, -1) - f(-1, 1) + f(-1, -1)) / (4 * h * h)
            Hm[a, b] = Hm[b, a] = v
    ev = sorted(mp.eig(Hm, left=False, right=False), key=lambda z: mp.re(z))
    k = (1 + 4 * r * r) / (1 - 12 * r * r)
    L = mp.log(k)
    print(f"r={float(r):.6f} L={float(L):.4f} min_atom={float(min(ps)):.3e} sum={float(sum(ps)):.12f} "
          f"eig_max={float(mp.re(ev[-1])):.6e} eig_min={float(mp.re(ev[0])):.4e} 4/(L+4)={float(4/(L+4)):.4f}", flush=True)
