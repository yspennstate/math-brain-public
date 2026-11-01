"""What the octave position does to the phases - it is simpler than it looks.

Err(k0) = sum_{eps != 0} c_eps e(k0 nu_eps / P) G(nu_eps),  P = 3^(K+1), L = R = (3/2)^K, k0 = round(R).
G(nu) = sum_{j<L} e(j nu/P) is large only for |nu| <~ P/L = 3 * 2^K, so the terms that matter are
exactly the near-origin block - which is why a block carrying 1.2 pct of the weight carries the sum.

Now the phase.  If k0 were exactly (3/2)^K then
    k0 nu / P = (3/2)^K nu / 3^(K+1) = nu / (3 * 2^K),
a LINEAR phase whose slope is exactly the reciprocal of the effective range of nu.  So across the range
that matters the phase makes exactly ONE full turn.  That is the whole cancellation mechanism at the
octave: a single oscillation against the weight, not many - which is why the cancellation is real but
delicate, and why it cannot be got from the modulus.

k0 must be an integer, so the true slope is round((3/2)^K)/3^(K+1); the rounding is itself part of the
arithmetic.  Measure both, and check that replacing the true phase by the idealised nu/(3 2^K) keeps
the answer.
"""
import numpy as np

print(f"{'K':>3} {'k0':>8} {'true slope k0/P':>18} {'1/(3 2^K)':>14} {'ratio':>8} {'turns over |nu|<=3*2^K':>24}")
for K in (6, 8, 10, 12, 14, 16):
    P = 3 ** (K + 1)
    k0 = int(round(1.5 ** K))
    true = k0 / P
    ideal = 1.0 / (3 * 2 ** K)
    print(f"{K:>3} {k0:>8} {true:>18.10e} {ideal:>14.6e} {true/ideal:>8.5f} {2*true*3*2**K:>24.5f}")

print()
print("Now the sum itself: true phase vs the idealised linear phase, on the block.")
print(f"{'K':>3} {'Err/L true':>13} {'Err/L idealised':>17} {'sum |terms| / L':>17}")
for K in (6, 8, 10, 12):
    P = 3 ** (K + 1)
    L = max(1, int(round(1.5 ** K)))
    k0 = L
    n = np.array([(2 ** i) * (3 ** (K - i)) for i in range(K + 1)], dtype=np.int64)
    nu = np.zeros(1, dtype=np.int64); c = np.ones(1)
    for i in range(K + 1):
        nu = np.concatenate([nu - n[i], nu, nu + n[i]])
        c = np.concatenate([c * 0.5, c, c * 0.5])
    nz = nu != 0
    v, cc = nu[nz].astype(float), c[nz]
    z = np.exp(2j * np.pi * v / P)
    den = 1.0 - z
    G = np.where(np.abs(den) < 1e-12, complex(L), (1.0 - np.exp(2j * np.pi * L * v / P)) / den)
    true = float(np.real((cc * np.exp(2j * np.pi * k0 * v / P) * G).sum())) / L
    ideal = float(np.real((cc * np.exp(2j * np.pi * v / (3 * 2.0 ** K)) * G).sum())) / L
    absS = float((cc * np.abs(G)).sum()) / L
    print(f"{K:>3} {true:>13.5f} {ideal:>17.5f} {absS:>17.2f}")
