from fractions import Fraction
import math


def fwht(vals):
    a = [int(x) for x in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def root_metrics(vals):
    N = len(vals)
    n = N.bit_length() - 1
    W = fwht(vals)
    mu = [Fraction(w*w, N*N) for w in W]
    I = sum(mu[s] * s.bit_count() for s in range(N))
    p, v = [], []
    for i in range(n):
        pi = sum(mu[s] for s in range(N) if (s >> i) & 1)
        vi = sum(mu[s] / s.bit_count()
                 for s in range(1, N) if (s >> i) & 1)
        p.append(pi)
        v.append(vi)
    r = sum(v)
    B0 = sum(float(vi) * math.log2(float(r/vi)) for vi in v if vi)
    cap_ratio = 0.0
    for pi, vi in zip(p, v):
        if not pi:
            continue
        pf, vf = float(pi), float(vi)
        L = math.log(1.0/pf)
        cap = min(pf, 2.0*pf/(L + math.log(4.0)))
        cap_ratio = max(cap_ratio, vf/cap)
    return float(I), float(r), B0, B0/float(I), cap_ratio


def onepoint(n):
    return [-1 if x == 0 else 1 for x in range(1 << n)]


def majority(n):
    return [1 if x.bit_count() > n//2 else -1 for x in range(1 << n)]


def tribes2(m):
    vals = []
    for x in range(1 << (2*m)):
        out = any(((x >> (2*b)) & 3) == 3 for b in range(m))
        vals.append(1 if out else -1)
    return vals


def simpson(f, a, b, N=200000):
    assert N % 2 == 0
    h = (b-a)/N
    s = f(a) + f(b)
    s += 4*sum(f(a+(2*k-1)*h) for k in range(1, N//2+1))
    s += 2*sum(f(a+2*k*h) for k in range(1, N//2))
    return s*h/3


CROOT = (2.0 + 1.0/(4.0*math.e))/math.log(2.0)
print(f"C_root={CROOT:.15f}")

for name, vals in [
    ("onepoint_n16", onepoint(16)),
    ("majority_n15", majority(15)),
    ("width2_tribes_m7", tribes2(7)),
]:
    I, r, B0, ratio, capratio = root_metrics(vals)
    print(name)
    print(f"  I={I:.15g}")
    print(f"  nonempty_mass={r:.15g}")
    print(f"  root_branch_bits={B0:.15g}")
    print(f"  root_branch_over_I={ratio:.15g}")
    print(f"  max_v_over_singleton_cap={capratio:.15g}")

# Exact 2-bit one-defect obstruction to deleting the derivative-granularity factor.
vals = [-1, 1, 1, 1]
W = fwht(vals)
mu = [Fraction(w*w, 16) for w in W]
nu12 = mu[3]
v12 = mu[3]  # only superset of {1,2} in n=2
F_no_granularity = simpson(
    lambda t: 2.0*t*(0.25 ** (t/(2.0-t))), 0.0, 1.0
)
rhs_no_granularity = float(nu12) * F_no_granularity
print("two_bit_one_defect")
print(f"  nu_12={nu12}")
print(f"  v_12={v12}")
print(f"  no_granularity_factor_F={F_no_granularity:.15g}")
print(f"  false_no_granularity_rhs={rhs_no_granularity:.15g}")
print(f"  stronger_bound_refuted={float(v12) > rhs_no_granularity}")
