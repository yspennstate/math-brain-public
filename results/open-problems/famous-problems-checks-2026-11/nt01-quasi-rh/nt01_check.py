# Numerical test of Lemma 4.1 of the 5 Oct 2026 preprint (Hecke L-functions over Q(sqrt(-3)), zero-free region
# Re s > 11/12): the Gauss-Jacobi identities (4.1)-(4.6) for squarefree primary n in Z[w], w = exp(2 pi i/3).
#
# Definitions as in the paper (Section 2 and 4.1):
#   primary: n = 1 (mod 3);  chi_n(u) = (u/n)_6, the sextic residue symbol, zero when (u, n) != 1;
#   gamma_j(n) = N(n)^(-1/2) sum_{x mod n} chi_n(x)^j e(x/n),  e(z) = exp(4 pi i Im z / sqrt 3);
#   G(n) = chi_n(4) gamma_3(n);  mu = Moebius function of the ideal (n).
# The text extraction of the PDF loses overlines, so alpha(n) is tested both as n/|n| and as conj(n)/|n|, and
# every identity that contains alpha is tested in both forms. Each identity also has a planted wrong form that
# must fail.
import cmath, itertools, math, sys

def mul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)

def conj(x):
    a, b = x
    return (a - b, -b)

def norm(x):
    a, b = x
    return a * a - a * b + b * b

def cx(x):
    a, b = x
    return complex(a - b / 2.0, b * math.sqrt(3) / 2.0)

def reduce_mod(x, n):
    # x minus the nearest multiple of n
    N = norm(n)
    p = mul(x, conj(n))
    qa = (2 * p[0] + N) // (2 * N)
    qb = (2 * p[1] + N) // (2 * N)
    m = mul((qa, qb), n)
    return (x[0] - m[0], x[1] - m[1])

def divides(n, x):
    N = norm(n)
    p = mul(x, conj(n))
    return p[0] % N == 0 and p[1] % N == 0

def powmod(x, e, n):
    r = (1, 0)
    x = reduce_mod(x, n)
    while e:
        if e & 1:
            r = reduce_mod(mul(r, x), n)
        x = reduce_mod(mul(x, x), n)
        e >>= 1
    return r

UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]          # 1, -w^2, w, -1, w^2, -w  = zeta_6^k
ZETA = [cmath.exp(2j * math.pi * k / 6) for k in range(6)]
for k in range(6):
    assert abs(cx(UNITS[k]) - ZETA[k]) < 1e-12

def sextic_prime(u, p):
    # exponent k with (u/p)_6 = zeta_6^k, or None when p divides u
    if divides(p, u):
        return None
    t = powmod(u, (norm(p) - 1) // 6, p)
    for k in range(6):
        if divides(p, (t[0] - UNITS[k][0], t[1] - UNITS[k][1])):
            return k
    raise RuntimeError("no sixth root found")

def is_rat_prime(m):
    if m < 2:
        return False
    i = 2
    while i * i <= m:
        if m % i == 0:
            return False
        i += 1
    return True

def primary_primes(bound):
    out = []
    for a in range(-60, 61):
        for b in range(-60, 61):
            x = (a, b)
            N = norm(x)
            if N < 2 or N > bound or N % 2 == 0 or N % 3 == 0:
                continue
            if a % 3 != 1 or b % 3 != 0:
                continue
            if is_rat_prime(N) or (b == 0 and is_rat_prime(abs(a)) and abs(a) % 3 == 2):
                out.append(x)
    return sorted(out, key=norm)

def residues(n):
    c, d = n
    g = math.gcd(abs(c), abs(d))
    N = norm(n)
    return [(i, j) for j in range(g) for i in range(N // g)]

class Elt:
    def __init__(self, primes):
        self.primes = list(primes)
        n = (1, 0)
        for p in self.primes:
            n = mul(n, p)
        self.n = n
        self.N = norm(n)
        self.mu = (-1) ** len(self.primes)
        self._gam = {}
        self._tab = None

    def chi_exp(self, u):
        k = 0
        for p in self.primes:
            e = sextic_prime(u, p)
            if e is None:
                return None
            k += e
        return k % 6

    def table(self):
        if self._tab is None:
            nb = conj(self.n)
            tab = []
            for x in residues(self.n):
                k = self.chi_exp(x)
                if k is None:
                    continue
                phase = mul(x, nb)[1] % self.N        # e(x/n) = exp(2 pi i * (w-coordinate of x conj(n)) / N)
                tab.append((k, cmath.exp(2j * math.pi * phase / self.N)))
            self._tab = tab
        return self._tab

    def gamma(self, j):
        j %= 6
        if j not in self._gam:
            s = sum(ZETA[(k * j) % 6] * e for k, e in self.table())
            self._gam[j] = s / math.sqrt(self.N)
        return self._gam[j]

    def chi(self, u):
        k = self.chi_exp(u)
        return 0 if k is None else ZETA[k]

    def G(self):
        # GBAR = 1: G(n) = conj(chi_n(4)) gamma_3(n), the form the duplication formula for Gauss sums gives;
        # GBAR = 0: G(n) = chi_n(4) gamma_3(n), the formula as the text extraction prints it.
        c = self.chi((4, 0))
        return (c.conjugate() if GBAR else c) * self.gamma(3)

    def alpha(self, bar):
        z = cx(conj(self.n) if bar else self.n)
        return z / abs(z)

TOL = 1e-8
GBAR = int(sys.argv[2]) if len(sys.argv) > 2 else 1
def close(x, y):
    return abs(x - y) < TOL

def main():
    bound = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    P = [p for p in primary_primes(200)]
    elts = [Elt([])]
    for r in (1, 2, 3):
        for combo in itertools.combinations(P, r):
            N = 1
            for p in combo:
                N *= norm(p)
            if N <= bound:
                elts.append(Elt(combo))
    elts.sort(key=lambda e: e.N)
    print(f"G(n) = {'conj(chi_n(4))' if GBAR else 'chi_n(4)'} gamma_3(n)", flush=True)
    print(f"primary primes of norm <= 200 prime to 6: {len(P)}; squarefree primary n with N(n) <= {bound}: {len(elts)}", flush=True)
    names = ["|gamma_j| = 1, j = 1, 2, 3, -1",
             "(4.2a) gamma_2^3 = mu alpha, alpha = n/|n|",
             "(4.2a) gamma_2^3 = mu alpha, alpha = conj(n)/|n|",
             "control: gamma_2^3 = alpha without mu, either alpha",
             "(4.3) gamma_1 gamma_-1 = chi_n(-1)",
             "(4.2b) gamma_1 gamma_2 = mu alpha G, alpha = n/|n|",
             "(4.2b) gamma_1 gamma_2 = mu alpha G, alpha = conj(n)/|n|",
             "(4.4) alpha gamma_2 gamma_1 = mu G, alpha = n/|n|",
             "(4.4) alpha gamma_2 gamma_1 = mu G, alpha = conj(n)/|n|",
             "(4.5) mu gamma_-1 = chi_n(-1) G^-1 alpha gamma_2, alpha = n/|n|",
             "(4.5) mu gamma_-1 = chi_n(-1) G^-1 alpha gamma_2, alpha = conj(n)/|n|",
             "|G| = 1"]
    ok = [0] * len(names); tot = [0] * len(names)
    def rec(i, cond):
        tot[i] += 1; ok[i] += 1 if cond else 0
    for e in elts:
        g1, g2, g3, gm = e.gamma(1), e.gamma(2), e.gamma(3), e.gamma(-1)
        rec(0, all(close(abs(g), 1) for g in (g1, g2, g3, gm)))
        a0, a1 = e.alpha(False), e.alpha(True)
        G = e.G()
        rec(1, close(g2 ** 3, e.mu * a0)); rec(2, close(g2 ** 3, e.mu * a1))
        if e.mu == -1:
            rec(3, close(g2 ** 3, a0) or close(g2 ** 3, a1))
        rec(4, close(g1 * gm, e.chi((-1, 0))))
        rec(5, close(g1 * g2, e.mu * a0 * G)); rec(6, close(g1 * g2, e.mu * a1 * G))
        rec(7, close(a0 * g2 * g1, e.mu * G)); rec(8, close(a1 * g2 * g1, e.mu * G))
        rec(9, close(e.mu * gm, e.chi((-1, 0)) / G * a0 * g2)); rec(10, close(e.mu * gm, e.chi((-1, 0)) / G * a1 * g2))
        rec(11, close(abs(G), 1))
    for i, nm in enumerate(names):
        print(f"  {nm}: {ok[i]} of {tot[i]}", flush=True)

    # pairs: (4.1) and (4.6)
    small = [e for e in elts if 1 < e.N <= 150]
    pn = ["R(a,b) = chi_b(a)/chi_a(b) is +1 or -1",
          "(4.1) G(ab) = G(a) G(b) R(a,b)",
          "control: G(ab) = G(a) G(b) without R",
          "(4.6) a(ab) = a(a) a(b) chi_b(a)^4, alpha = n/|n|",
          "(4.6) a(ab) = a(a) a(b) chi_b(a)^4, alpha = conj(n)/|n|",
          "control: (4.6) with chi_b(a)^2 in place of chi_b(a)^4, either alpha"]
    pok = [0] * len(pn); ptot = [0] * len(pn)
    def prec(i, cond):
        ptot[i] += 1; pok[i] += 1 if cond else 0
    npairs = 0; rminus = 0
    for x, y in itertools.combinations(small, 2):
        if set(x.primes) & set(y.primes) or x.N * y.N > bound:
            continue
        npairs += 1
        ab = Elt(x.primes + y.primes)
        cba = y.chi(x.n); cab = x.chi(y.n)
        R = cba / cab
        isr = close(R, 1) or close(R, -1)
        rminus += 1 if close(R, -1) else 0
        prec(0, isr)
        prec(1, close(ab.G(), x.G() * y.G() * R))
        if close(R, -1):
            prec(2, close(ab.G(), x.G() * y.G()))
        for i, bar in ((3, False), (4, True)):
            lhs = ab.alpha(bar) * ab.gamma(2)
            rhs = x.alpha(bar) * x.gamma(2) * y.alpha(bar) * y.gamma(2) * cba ** 4
            prec(i, close(lhs, rhs))
        if not close(cba ** 2, cba ** 4):
            l0 = ab.alpha(False) * ab.gamma(2); r0 = x.alpha(False) * x.gamma(2) * y.alpha(False) * y.gamma(2) * cba ** 2
            l1 = ab.alpha(True) * ab.gamma(2); r1 = x.alpha(True) * x.gamma(2) * y.alpha(True) * y.gamma(2) * cba ** 2
            prec(5, close(l0, r0) or close(l1, r1))
    print(f"coprime pairs a, b with N(ab) <= {bound}: {npairs}; R = -1 on {rminus} of them", flush=True)
    for i, nm in enumerate(pn):
        print(f"  {nm}: {pok[i]} of {ptot[i]}", flush=True)

main()
