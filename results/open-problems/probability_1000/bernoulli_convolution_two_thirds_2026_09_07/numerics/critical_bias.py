"""The auxiliary measure in the second moment sits EXACTLY at the critical bias.

For the biased measure at ratio 2/3, the full-period average of the truncated square is
prod_i (1 - 2p(1-p)) over K+1 factors = (1 - 2p(1-p))^(K+1), so the main term of the octave sum gives

    E_p(R) ~ (1 - 2p(1-p))^(K+1) * L,   L = R = (3/2)^K
    =>  exponent  alpha(p) = 1 + log(1 - 2p(1-p)) / log(3/2).

alpha(p) < 0 (decay) exactly when 1 - 2p(1-p) < 2/3, i.e. p(1-p) > 1/6, i.e.
p in ( (1 - 3^-0.5)/2 , (1 + 3^-0.5)/2 ) = (0.2113, 0.7887).

But p(1-p) = 1/6 is EXACTLY the condition that defined the auxiliary law in the second moment
(the off-diagonal weight of the normalised c_eps^2).  So the auxiliary measure sits precisely on the
boundary alpha = 0 - which is why Var(Err/L) grows LOGARITHMICALLY rather than as a power: a critical
exponent produces a logarithm.  That is an identity, not a numerical coincidence.
"""
import numpy as np
from math import log, sqrt

pc = (1 - 1 / sqrt(3)) / 2
print(f"critical bias p* = (1 - 1/sqrt3)/2 = {pc:.7f}   (and its mirror {1-pc:.7f})")
print(f"  p*(1-p*)            = {pc*(1-pc):.10f}   (exactly 1/6 = {1/6:.10f})")
print(f"  1 - 2 p*(1-p*)      = {1-2*pc*(1-pc):.10f}   (exactly 2/3)")
alpha = lambda p: 1 + log(1 - 2 * p * (1 - p)) / log(1.5)
print(f"  alpha(p*)           = {alpha(pc):.3e}   (exactly 0)")
print()
print(f"{'p':>9} {'1-2p(1-p)':>12} {'alpha(p)':>10}  main-term octave exponent")
for p in (0.5, 0.4, 0.3, 0.25, pc, 0.20, 0.15, 0.10, 0.05):
    print(f"{p:>9.4f} {1-2*p*(1-p):>12.6f} {alpha(p):>+10.4f}"
          + ("   <- unbiased, our case" if p == 0.5 else
             "   <- CRITICAL, the second moment's auxiliary" if abs(p-pc) < 1e-9 else
             "   no decay from the main term" if alpha(p) >= 0 else ""))

# measure it: octave energy exponent for a few p, exact product formula
def octave_exponent(p, jlo=8, jhi=16):
    def amp2(k):
        out = np.ones_like(k)
        r = 1.0
        while True:
            a = 2 * np.pi * k * r / 3.0
            if (np.abs(a)).max() < 1e-13:
                break
            out *= np.abs((1 - p) + p * np.exp(-1j * a)) ** 2
            r *= 2.0 / 3.0
        return out
    js, es = [], []
    for j in range(jlo, jhi + 1):
        k = np.arange(1 << j, 1 << (j + 1), dtype=float)
        es.append(float(amp2(k).sum())); js.append(j)
    a, b = np.polyfit(np.array(js, float), np.log2(np.array(es)), 1)
    return a

print()
print(f"{'p':>9} {'measured slope':>15} {'predicted alpha':>16}")
for p in (0.5, 0.3, pc, 0.20, 0.10):
    m = octave_exponent(p)
    print(f"{p:>9.4f} {m:>+15.4f} {alpha(p):>+16.4f}")
