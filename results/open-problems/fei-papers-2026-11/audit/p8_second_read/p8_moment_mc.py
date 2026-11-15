"""Independent Monte Carlo of the Toeplitz and Hankel limit moments m_2k (Bryc-Dembo-Jiang volumes),
to check paper 8's inputs m_6, m_8 (Hankel 11/2, 281/15) and u_4 (Toeplitz 2724/5, i.e. m_8 = 2724/45)."""
import numpy as np

def pairings(pts):
    if not pts:
        yield []
        return
    a = pts[0]
    for i in range(1, len(pts)):
        rest = pts[1:i] + pts[i + 1:]
        for p in pairings(rest):
            yield [(a, pts[i])] + p

def vol(pairs, n2, kind, N, rng):
    mate = {}
    for a, b in pairs:
        mate[a] = b; mate[b] = a
    if kind == "H" and any((a - b) % 2 == 0 for a, b in pairs):
        return 0.0, 0.0
    x = rng.random(N)            # x_0
    ok = np.ones(N, bool)
    store = {}
    prev = x
    for i in range(1, n2 + 1):
        j = mate[i]
        if j > i:                # first visit: x_i free
            xi = rng.random(N)
            store[i] = (xi - prev) if kind == "T" else (xi + prev)
        else:
            s = store[j]
            xi = (prev - s) if kind == "T" else (s - prev)
            ok &= (xi >= 0) & (xi <= 1)
        prev = xi
    p = ok.mean()
    return p, np.sqrt(p * (1 - p) / N)

if __name__ == "__main__":
  rng = np.random.default_rng(12)
  N = 2_000_000
  for k in (2, 3, 4):
      for kind in ("T", "H"):
          tot = 0.0; var = 0.0
          for pr in pairings(list(range(1, 2 * k + 1))):
              p, se = vol(pr, 2 * k, kind, N, rng)
              tot += p; var += se * se
          print(f"k={k} {kind}: m_{2*k} = {tot:.4f} +- {np.sqrt(var):.4f}")
  print("targets: T m4 8/3=2.6667 m6 11 m8 2724/45=%.4f (1435/24=%.4f); H m4 2 m6 5.5 m8 281/15=%.4f"
        % (2724 / 45, 1435 / 24, 281 / 15))
