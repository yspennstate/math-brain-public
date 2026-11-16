# Appendix A.1 of the 5 Oct 2026 preprint: numerical test of (A.1) and of the closed formula that follows it.
#   Gquad(c) := |c|^-1 sum_{x mod c} e(x^2/c) = (1/2) sum_{y mod 2O} e(-c y^2/4) = (1 + i^-b + i^a + i^(b-a))/2
# for c = a + b w in O = Z[w], w = exp(2 pi i/3), c coprime to 2, with e(z) = exp(4 pi i Im z / sqrt 3).
# Also: the Jacobi sum J(chi_p^2, chi_p^2) = -p for primary primes p = 1 mod 3 (cubic character
# chi_p^2(x) = x^((q-1)/3) mod p), and the control that the conjugate formula fails.
import cmath, math, sys
from math import gcd

W = cmath.exp(2j * math.pi / 3)
S3 = math.sqrt(3.0)

def e(z):
    return cmath.exp(4j * math.pi * z.imag / S3)

def val(a, b):
    return a + b * W

def residues(a, b):
    n = a * a - a * b + b * b
    g = gcd(abs(a), abs(b))
    return [(m, k) for m in range(n // g) for k in range(g)], n

def gquad(a, b):
    c = val(a, b)
    res, n = residues(a, b)
    s = 0
    for m, k in res:
        x = val(m, k)
        s += e(x * x / c)
    return s / math.sqrt(n), n

def dual(a, b):
    c = val(a, b)
    return sum(e(-c * y * y / 4) for y in (0, 1, W, W * W)) / 2

def closed(a, b):
    return (1 + 1j ** (-b) + 1j ** a + 1j ** (b - a)) / 2

def closed_conj(a, b):
    return closed(a, b).conjugate()

tested = ok_dual = ok_closed = ok_res = 0
ctrl = ctrl_fail = 0
vals = {}
B = 14
for a in range(-B, B + 1):
    for b in range(-B, B + 1):
        n = a * a - a * b + b * b
        if n == 0 or n > 330:
            continue
        if a % 2 == 0 and b % 2 == 0:
            continue                      # 2 is inert: c coprime to 2 iff not both even
        res, _ = residues(a, b)
        # residue system check: all differences are non-multiples of c
        g, nn = gquad(a, b)
        d = dual(a, b)
        cl = closed(a, b)
        tested += 1
        ok_dual += abs(g - d) < 1e-7
        ok_closed += abs(d - cl) < 1e-9
        vals[round(cl.real, 6), round(cl.imag, 6)] = vals.get((round(cl.real, 6), round(cl.imag, 6)), 0) + 1
        if abs(cl.imag) > 0.5:
            ctrl += 1
            ctrl_fail += abs(g - closed_conj(a, b)) > 1e-3
print("A.1 pairs tested (c coprime to 2, norm <= 330):", tested)
print("  |c|^-1 sum e(x^2/c) = (1/2) sum_{y mod 2} e(-c y^2/4):", ok_dual, "of", tested)
print("  = (1 + i^-b + i^a + i^(b-a))/2:", ok_closed, "of", tested)
print("  values taken:", sorted(vals.items()))
print("  control, conjugate formula on the c with value +-i: fails on", ctrl_fail, "of", ctrl)

# residue-system sanity: the sum over the system of e(x/c) must vanish for c a non-unit
bad = 0; cnt = 0
for a, b in ((5, 0), (3, 6), (7, 0), (1, 3), (9, 3), (5, 10)):
    if a % 2 == 0 and b % 2 == 0:
        continue
    c = val(a, b); res, n = residues(a, b)
    s = sum(e(val(m, k) / c) for m, k in res)
    cnt += 1; bad += abs(s) > 1e-7
print("residue systems with sum e(x/c) = 0:", cnt - bad, "of", cnt)

# Jacobi sum J(chi^2, chi^2) = -p for primary primes p = a + b w, p = 1 mod 3 (a = 1 mod 3, b = 0 mod 3)
def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def cubic_char_table(a, b, q):
    # O/(p) = Z/q for a split prime; w corresponds to r with a + b r = 0 mod q
    r = (-a * pow(b, -1, q)) % q
    # chi^2(x) = w^j where x^((q-1)/3) = r^j mod q
    t = {1: 0, r: 1, (r * r) % q: 2}
    return r, t

jt = jok = jctrl = 0
for a in range(-40, 41):
    for b in range(-40, 41):
        if b == 0 or a % 3 != 1 or b % 3 != 0:
            continue
        q = a * a - a * b + b * b
        if q > 700 or not isprime(q) or q % 3 != 1:
            continue
        r, t = cubic_char_table(a, b, q)
        J = 0
        for x in range(2, q):
            j1 = t[pow(x, (q - 1) // 3, q)]
            j2 = t[pow((1 - x) % q, (q - 1) // 3, q)]
            J += W ** ((j1 + j2) % 3)
        p = val(a, b)
        jt += 1
        jok += abs(J + p) < 1e-6
        jctrl += abs(J + p.conjugate()) < 1e-6
print("Jacobi sums J(chi_p^2, chi_p^2) = -p:", jok, "of", jt, "; equal to -conj(p):", jctrl)
sys.stdout.flush()
