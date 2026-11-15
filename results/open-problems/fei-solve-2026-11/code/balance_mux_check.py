"""Does balancing by a multiplexer keep G = sum_i E_i / I?  h(x, x', z) = psi(x) if z = 0 else -psi(s x') with s = +1
(negated copy) or s = -1 (dual copy, keeps monotone).  Test on agent's n=6 leader (G 3.030964, mean -0.78125)."""
import numpy as np


def wht(v):
    v = v.astype(float).copy(); h = 1; N = len(v)
    while h < N:
        v = v.reshape(-1, 2 * h); a = v[:, :h].copy(); b = v[:, h:].copy()
        v[:, :h] = a + b; v[:, h:] = a - b; v = v.reshape(N); h *= 2
    return v / N


def EI(f, n):
    w2 = wht(f) ** 2; idx = np.arange(1 << n); E = []; I = []
    for i in range(n):
        bit = 1 << i; T = idx[(idx & bit) == 0]
        a = w2[T]; c = w2[T | bit]; s = a + c
        t = np.divide(c, s, out=np.zeros_like(s), where=s > 1e-300)
        with np.errstate(divide="ignore", invalid="ignore"):
            H = -(t * np.log2(np.where(t > 0, t, 1)) + (1 - t) * np.log2(np.where(t < 1, 1 - t, 1)))
        E.append((s * H).sum()); I.append(c.sum())
    return np.array(E), np.array(I)


def G(f, n):
    E, I = EI(f, n)
    return E.sum() / I.sum(), E, I


def from_hex(f1, f0, n=6):
    bits = (int(f1, 16) << 32) | int(f0, 16)
    return np.array([-1.0 if (bits >> k) & 1 else 1.0 for k in range(1 << n)])


n = 6
for name, f1, f0 in [("leader_all", "ffffffee", "fefefeee"), ("leader_bal", "ffccfccc", "a888a888"),
                     ("near_bal", "fffff8a8", "a8a8a8a8")]:
    psi = from_hex(f1, f0)
    g, E, I = G(psi, n)
    print(f"{name}: mean {psi.mean():+.5f}  G {g:.6f}  I {I.sum():.5f}")
    N = 1 << n; neg = np.arange(N) ^ (N - 1)  # index of -x
    for s, lab in [(1, "negated copy"), (-1, "dual copy")]:
        h = np.empty(1 << (2 * n + 1))
        for z in (0, 1):
            for xp in range(N):
                base = (z << (2 * n)) | (xp << n)
                if z == 0:
                    h[base:base + N] = psi
                else:
                    h[base:base + N] = -psi[neg[xp] if s == -1 else xp]
        gh, Eh, Ih = G(h, 2 * n + 1)
        print(f"   mux {lab}: mean {h.mean():+.5f}  G {gh:.6f}  (x part {Eh[:n].sum() / Ih[:n].sum():.6f}, "
              f"x' part {Eh[n:2 * n].sum() / Ih[n:2 * n].sum():.6f}, z: E {Eh[-1]:.5f} Inf {Ih[-1]:.5f})")
