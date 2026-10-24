"""The octave endpoints are EXACT zeros of F_K, and the phase law is exactly uniform.

F_K(x) = prod_{i=0..K} cos^2(pi x 2^i / 3^(i+1)) as a function on the reals.
At x = R = (3/2)^K the factor i = K-1 reads
    cos^2( pi (3/2)^K 2^(K-1) / 3^K ) = cos^2( pi 3^0 2^(-1) ) = cos^2(pi/2) = 0.
At x = 2R the factor i = K-2 reads cos^2(3 pi / 2) = 0.
So the octave [R, 2R] is exactly the gap between two zeros of F_K - not approximately, identically,
for every K.  This is what makes the octave position special, and it is the same fact as the phase
frequency landing on the band edge, seen in the other variable.

Consequence (round 4's agent): the c-weighted phase law is exactly uniform, so replacing G(nu) by
G(0) = L gives Err/L = -1 EXACTLY - the phases alone annihilate the whole main term, and the measured
-0.955 is that identity plus a residual of about 4.5 pct.

Check all of it here, and check that it dies under the p-substitution as it must.
"""
import numpy as np
from mpmath import mp, mpf, cos, pi
mp.dps = 60

def F(x, K):
    v = mpf(1)
    for i in range(K + 1):
        v *= cos(pi * x * mpf(2) ** i / mpf(3) ** (i + 1)) ** 2
    return v

print("F_K at the octave endpoints, in 60-digit arithmetic:")
print(f"{'K':>4} {'F_K(R)':>14} {'F_K(2R)':>14} {'F_K(1.5R) (interior)':>22}")
for K in (4, 8, 12, 16, 20, 24):
    R = (mpf(3) / 2) ** K
    print(f"{K:>4} {mp.nstr(F(R,K),6):>14} {mp.nstr(F(2*R,K),6):>14} {mp.nstr(F(mpf(3)/2*R,K),6):>22}")

print()
print("Which factor vanishes: at x = R it should be i = K-1, at x = 2R it should be i = K-2.")
for K in (6, 10, 14):
    R = (mpf(3) / 2) ** K
    for lab, x in (("R", R), ("2R", 2 * R)):
        vals = [abs(cos(pi * x * mpf(2) ** i / mpf(3) ** (i + 1))) for i in range(K + 1)]
        j = int(np.argmin([float(v) for v in vals]))
        print(f"  K={K:>3} x={lab:>2}: smallest |cos| at i={j} (= K-{K-j}), value {mp.nstr(vals[j],4)}")

print()
print("p-substitution: the vanishing factor becomes 1 - 4p(1-p), zero ONLY at p = 1/2.")
for p in (0.5, 0.35, 0.2113, 0.10, 0.05):
    print(f"  p={p:>7.4f}:  1 - 4p(1-p) = {1-4*p*(1-p):+.6f}")
print("So the mechanism is a property of the fair coin, not of the functional equation,")
print("and it correctly supplies nothing where the measure is singular.")
