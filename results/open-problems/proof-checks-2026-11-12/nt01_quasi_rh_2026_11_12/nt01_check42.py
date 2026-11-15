# Numerical test of Lemma 4.2 (twisted Poisson summation with excluded primes), formula (4.8), as printed on
# page 14:
#   sum_k chi(k) 1_{(k,r)=1} Phi(N(k)/H)
#     = H gamma(chi)/sqrt(N(m)) * sum_{d | rad r} mu(d) chi(d)/N(d) * sum_h conj(chi(h)) Phihat(H N(h)/(N(d) N(m)))
# with Phihat(|w|^2) = (2/sqrt 3) int Phi(|z|^2) e(-zw) dx dy and e(z) = exp(4 pi i Im z / sqrt 3).
# For Phi(t) = exp(-pi t) this gives Phihat(t) = (2/sqrt 3) exp(-4 pi t / 3).
# chi = chi_n^j for a primary prime n (sextic symbol to the power j, primitive for j = 1..5), r = a product of
# one or two other primes. Both sides are summed over a box large enough that the tail is below 1e-13.
import io, os, sys, cmath, math
here = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(here, "nt01_check.py"), encoding="utf-8").read()
exec(src[:src.index("TOL = 1e-8")])
S3 = math.sqrt(3.0)

def divisible(k, p):
    q = norm(p); t = mul(k, conj(p))
    return t[0] % q == 0 and t[1] % q == 0

def box(bound):
    B = int(math.sqrt(4 * bound / 3)) + 2
    for a in range(-B, B + 1):
        for b in range(-B, B + 1):
            if a * a - a * b + b * b <= bound:
                yield (a, b)

def lhs(e, j, rprimes, H):
    cut = 14 * H
    s = 0j
    for k in box(cut):
        if k == (0, 0) or any(divisible(k, p) for p in rprimes):
            continue
        c = e.chi(k)
        if c == 0:
            continue
        s += c ** j * math.exp(-math.pi * norm(k) / H)
    return s

def rhs(e, j, n, rprimes, H, sqrt_form=True, bar=True):
    Nm = norm(n)
    ds = [((1, 0), 1)]
    for p in rprimes:
        ds += [(mul(d, p), -mu) for d, mu in ds]
    tot = 0j
    for d, mu in ds:
        cd = e.chi(d)
        if cd == 0:
            continue
        Nd = norm(d)
        scale = H / (Nd * Nm)
        cut = 3 * 34 / (4 * math.pi * scale)
        s = 0j
        for h in box(cut):
            c = e.chi(h)
            if c == 0:
                continue
            c = c ** j
            s += (c.conjugate() if bar else c) * (2 / S3) * math.exp(-4 * math.pi * scale * norm(h) / 3)
        tot += mu * cd ** j / Nd * s
    pref = H * e.gamma(j) / (math.sqrt(Nm) if sqrt_form else Nm)
    return pref * tot

primes = primary_primes(80)
# The sum over k runs over elements, so it vanishes unless chi^j is trivial on the six units; chi_n(u) = u^((N(n)-1)/6)
# on units, so norms 37 and 73 give a nonzero sum for every j, norm 19 for even j, norm 13 for j = 3.
moduli = [p for p in primes if norm(p) in (13, 19, 37, 73)]
cases = []
for n in moduli:
    others = [p for p in primes if norm(p) != norm(n)]
    for rprimes in ([], [others[0]], [others[1], others[2]]):
        for j in (1, 2, 3, 4, 5):
            for H in (7.0, 23.5):
                cases.append((n, tuple(rprimes), j, H))
ok = bad_n = bad_bar = nbar = nnz = 0; worst = 0.0
for n, rprimes, j, H in cases:
    e = Elt([n])
    L = lhs(e, j, rprimes, H)
    R = rhs(e, j, n, rprimes, H)
    err = abs(L - R); worst = max(worst, err)
    ok += err < 1e-9
    if abs(L) > 1e-6:
        nnz += 1
        bad_n += abs(L - rhs(e, j, n, rprimes, H, sqrt_form=False)) < 1e-9
    if j != 3 and abs(L) > 1e-6:
        nbar += 1
        bad_bar += abs(L - rhs(e, j, n, rprimes, H, bar=False)) < 1e-9
big = sum(1 for n, rp, j, H in cases if abs(lhs(Elt([n]), j, rp, H)) > 1e-3)
print(f"cases {len(cases)} ({len(moduli)} moduli of norm {[norm(p) for p in moduli]}, r with 0, 1, 2 primes, j in 1..5, H in 7, 23.5)", flush=True)
print(f"(4.8) as printed: holds to 1e-9 in {ok} of {len(cases)}; largest difference {worst:.2e}; left side above 1e-3 in {big} cases", flush=True)
print(f"control, 1/N(m) in place of 1/sqrt(N(m)) (the text-file form): left side above 1e-6: holds in {bad_n} of {nnz}", flush=True)
print(f"control, chi(h) without the bar, j not 3, left side above 1e-6: holds in {bad_bar} of {nbar}", flush=True)
