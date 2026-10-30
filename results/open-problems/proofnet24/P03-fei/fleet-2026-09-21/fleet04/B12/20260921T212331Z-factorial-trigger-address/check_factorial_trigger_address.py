from fractions import Fraction
from math import factorial, lgamma, log, log2

EPS = Fraction(1, 16)
TOL = 1e-12


def fwht(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for base in range(0, len(a), 2*h):
            for j in range(base, base+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def palm_law(mu, n, i, ji):
    rem = [k for k in range(n) if k != i]
    out = {}
    for S, p in enumerate(mu):
        if p and ((S >> i) & 1):
            b = 0
            for q, k in enumerate(rem):
                if (S >> k) & 1:
                    b |= 1 << q
            out[b] = out.get(b, Fraction()) + p / ji
    return rem, out


def tv_to_uniform_power(P, rem, F):
    local = 0
    for q, k in enumerate(rem):
        if (F >> k) & 1:
            local |= 1 << q
    u = Fraction(1, 1 << local.bit_count())
    tv = Fraction()
    for b in range(1 << len(rem)):
        target = u if (b & ~local) == 0 else Fraction()
        tv += abs(P.get(b, Fraction()) - target)
    return tv / 2


def closest_trigger(mu, n, i, ji):
    rem, P = palm_law(mu, n, i, ji)
    best = None
    for F in range(1 << n):
        if (F >> i) & 1:
            continue
        tv = tv_to_uniform_power(P, rem, F)
        key = (tv, F.bit_count(), F)
        if best is None or key < best[0]:
            best = (key, F, P, rem)
    return best[0][0], best[1], best[2], best[3]


def A(c):
    # E[ log_2(T!)/T ], T=1+Bin(c-1,1/2)
    n = c - 1
    ans = 0.0
    for r in range(n+1):
        p = float(Fraction(factorial(n), factorial(r)*factorial(n-r)*(1 << n)))
        t = 1 + r
        g = 0.0 if t == 1 else log2(factorial(t)) / t
        ans += p * g
    return ans

# Analytic-constant diagnostics (the theorem itself has an exact proof).
amin = (10.0, None)
for c in range(2, 257):
    ratio = A(c) / log2(c)
    if ratio < amin[0]:
        amin = (ratio, c)
    assert A(c) + TOL >= 0.25 * log2(c)

stats = []
violations = []
identity_checks = 0
row_checks = 0
sum_checks = 0
max_sum_ratio = 0.0

for n in range(1, 5):
    N = 1 << n
    funcs = robust_funcs = robust_nontrivial_rows = 0
    for tail in range(1 << (N-1)):
        vals = [1] + [1 if (tail >> (x-1)) & 1 else -1 for x in range(1, N)]
        W = fwht(vals)
        mu = [Fraction(w*w, N*N) for w in W]
        elogfact = sum(float(p) * log2(factorial(S.bit_count()))
                       for S, p in enumerate(mu) if S.bit_count() >= 2)

        js = [sum((p for S, p in enumerate(mu) if (S >> i) & 1), Fraction())
              for i in range(n)]

        # Exact Palm partition identity for the factorial rebate.
        palm_partition = 0.0
        for i, ji in enumerate(js):
            if not ji:
                continue
            conditional = 0.0
            for S, p in enumerate(mu):
                if p and ((S >> i) & 1):
                    k = S.bit_count()
                    conditional += float(p / ji) * (0.0 if k <= 1 else log2(factorial(k))/k)
            palm_partition += float(ji) * conditional
        identity_checks += 1
        if abs(palm_partition - elogfact) > TOL:
            violations.append(("partition", n, tail, palm_partition, elogfact))
            break

        robust_any = False
        lhs = 0.0
        for i, ji in enumerate(js):
            if not ji:
                continue
            tv, F, P, rem = closest_trigger(mu, n, i, ji)
            if tv > EPS:
                continue
            robust_any = True
            m = F.bit_count()
            if m == 0:
                continue
            robust_nontrivial_rows += 1
            row_checks += 1
            c = m + 1

            actual = 0.0
            for b, prob in P.items():
                k = 1 + b.bit_count()
                actual += float(prob) * (0.0 if k <= 1 else log2(factorial(k))/k)
            lower_exact = A(c) - float(tv) * log2(c)
            lower_uniform = (0.25 - float(tv)) * log2(c)
            if actual + TOL < lower_exact or actual + TOL < lower_uniform:
                violations.append(("row", n, tail, i, float(tv), m, actual, lower_exact, lower_uniform))
                break
            lhs += (0.25 - float(EPS)) * float(ji) * log2(c)
        if violations:
            break
        if robust_any:
            robust_funcs += 1
        sum_checks += 1
        if lhs > elogfact + TOL:
            violations.append(("sum", n, tail, lhs, elogfact))
            break
        if elogfact > 0:
            max_sum_ratio = max(max_sum_ratio, lhs / elogfact)
        funcs += 1
    stats.append((n, funcs, robust_funcs, robust_nontrivial_rows))
    if violations:
        break

print("theorem_constant_min_numeric", amin)
print("epsilon", f"{EPS.numerator}/{EPS.denominator}")
print("functions_total", sum(x[1] for x in stats))
print("stats_n_functions_robust_functions_cumulative_nontrivial_rows", stats)
print("identity_checks", identity_checks)
print("robust_row_checks", row_checks)
print("summed_factorial_checks", sum_checks)
print("max_lhs_over_factorial_rebate", format(max_sum_ratio, ".12g"))
print("violations", len(violations))
if violations:
    print("first_violation", violations[0])
    raise SystemExit(1)
print("PASS")
