"""Exact (Fraction) verification of the credit-inequality failure on OR(y_h, AND_s(lights)) for s=4,8:
compute P(S) exactly by the butterfly, then V, I, rho_i, the credit and H+/Delta (logs in mpmath)."""
from fractions import Fraction as F
import mpmath as mp
from biased import exact_spectrum
mp.mp.dps = 50
def run(s):
    x = F(1, s); pl = x / 50
    a2 = pl ** s
    ph = a2 * (1 - x) / (x + a2 * (1 - x))
    n = s + 1            # coordinate 0 = heavy (weight s), 1..s lights (weight 1)
    T = []
    for idx in range(1 << n):
        W = s * (idx & 1) + bin(idx >> 1).count('1')
        T.append(1 if W >= s else 0)
    q = [ph] + [pl] * s
    spec = exact_spectrum(T, q)
    P = {S: s2 * g * g for (S, s2, g) in spec}
    V = sum(P[S] for S in P if S != 0)
    I = sum(bin(S).count('1') * P[S] for S in P)
    Delta = I - V
    rho = [spec[1 << i][2] for i in range(n)]          # g_{i} = rho_i
    sig2 = [4 * qi * (1 - qi) for qi in q]
    Ii = [sig2[i] * rho[i] for i in range(n)]
    assert sum(Ii) == I, 'influence identity'
    cred = sum(mp.mpf(Ii[i].numerator) / Ii[i].denominator * max(0, mp.log(mp.mpf((4 * rho[i] / V).numerator) / (4 * rho[i] / V).denominator)) for i in range(n))
    Vm = mp.mpf(V.numerator) / V.denominator; Im = mp.mpf(I.numerator) / I.denominator
    E = mp.mpf(0)
    for (S, s2, g) in spec:
        if S != 0 and g != 0:
            gg = mp.mpf((g * g).numerator) / (g * g).denominator
            E += mp.mpf(s2.numerator) / s2.denominator * gg * mp.log(1 / gg)
    Dm = mp.mpf(Delta.numerator) / Delta.denominator
    print('s', s, 'exact Parseval', sum(P.values()) == 1, ' (VlnV-credit)/I =', mp.nstr((Vm * mp.log(1 / Vm) - cred) / Im, 6),
          ' H+/Delta =', mp.nstr(E / mp.log(2) / Dm, 6))
for s in (4, 8, 10):
    run(s)
