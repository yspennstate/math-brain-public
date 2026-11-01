"""Analytic constants for the logarithmic union theorem at a = 1.44, beta = 10.
g(b) = sup_{b' >= b} phi_{l(b')}(2^{1-b'}) <= Cg 2^{-gam b} for all b >= 0 (checked on a fine grid up to b = 20000,
and for b beyond it via the exponent of the leading term). Then
E G <= (4a/ln2)(ln(2kB)+1) + (2/gam)(log2(2k Cg) + log2 e)
C(k) <= 2.886 + 1.443 + (1+a) log2 k + beta + 2 log2 3 + log2(ea/(a-1)) + 1 + log2(2e) + E G."""
import math
LN2 = math.log(2); B = 3 * math.sqrt(3 / math.pi)
a, beta = 1.44, 10.0
def log2phi(b):
    if b <= beta: return -math.inf
    l = math.ceil(b / beta) - 2
    lx = (1 - b)          # log2 of 2^{1-b}
    if l == 0: return lx
    return lx + l * math.log2(2 * math.e * (b - 1) * LN2 / l)
for gam in (0.40, 0.42, 0.44, 0.45):
    # Cg = sup_b 2^{gam b} g(b) = sup_b 2^{gam b} sup_{b'>=b} phi(b') <= sup_{b'} 2^{gam b'} phi(b')
    best = -1e9; bstar = None
    b = 0.0
    while b < 20000:
        v = log2phi(b) + gam * b
        if v > best: best, bstar = v, b
        b += 0.01
    # leading exponent for large b: log2phi(b) ~ -b + (b/beta) log2(2e beta ln2) ; slope - (1 - log2(2e beta ln2)/beta)
    slope = 1 - math.log2(2 * math.e * beta * LN2) / beta
    Cg = 2 ** best
    print(f"gam={gam}: log2 Cg = {best:.3f} (at b={bstar:.2f}); asymptotic decay exponent {slope:.4f} > gam: {slope > gam}")
gam = 0.44
best = max(log2phi(b / 100) + gam * b / 100 for b in range(0, 2000000))
Cg = 2 ** best
def C(k):
    # int_0^inf min(1, M 2^{-gam v}) dv <= (log2^+ M + log2 e)/gam (the log2 M form is wrong for M < 1)
    EG = (4 * a / LN2) * (math.log(2 * k * B) + 1) + (2 / gam) * (max(0.0, math.log2(2 * k * Cg)) + math.log2(math.e))
    return 2.886 + 1.443 + (1 + a) * math.log2(k) + beta + 2 * math.log2(3) + math.log2(math.e * a / (a - 1)) + 1 + math.log2(2 * math.e) + EG
c0 = C(1); c1 = (1 + a) + 4 * a + 2 / gam
assert 2 * Cg < 1  # so log2^+(2kCg) <= log2 k
print(f"C(k) <= {c0:.2f} + {c1:.3f} log2 k exactly (affine in log2 k); C(10)={C(10):.1f}, C(1000)={C(1000):.1f}")

# FEI+ for unions: 2/ln2 + 8 + 2 log2 e + K_u + max(2 EG, a log2(4k^2) + log2(4k))
def EGk(k):
    return (4 * a / LN2) * (math.log(2 * k * B) + 1) + (2 / gam) * (max(0.0, math.log2(2 * k * Cg)) + math.log2(math.e))
def CP(k):
    Ku = (1 + a) * math.log2(k) + beta + 2 * math.log2(3) + math.log2(math.e * a / (a - 1)) + 1 + math.log2(2 * math.e)
    return 2 / LN2 + 8 + 2 * math.log2(math.e) + Ku + max(2 * EGk(k), a * math.log2(4 * k * k) + math.log2(4 * k))
worstF = max(C(k) - (54 + 12.8 * math.log2(k)) for k in [1, 2, 3, 4, 8, 9, 10, 100, 10**4, 10**8, 10**16])
worstP = max(CP(k) - (93 + 23.1 * math.log2(k)) for k in [1, 2, 3, 4, 8, 9, 10, 100, 10**4, 10**8, 10**16])
print(f"FEI  C(k) - (54 + 12.8 log2 k) <= {worstF:.3f};  FEI+ C'(k) - (93 + 23.1 log2 k) <= {worstP:.3f}  (both must be <= 0)")
