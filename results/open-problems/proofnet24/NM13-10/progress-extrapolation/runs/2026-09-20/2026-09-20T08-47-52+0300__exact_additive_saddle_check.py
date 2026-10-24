import math
from scipy.integrate import quad
from scipy.special import log_ndtr


def q_boundary(t, r, c):
    rhs = 1.5*r + 0.5*t + math.log(c*r)
    q = 1.5*r + 0.5*t
    for _ in range(60):
        f = q + math.log(q) - rhs
        step = f / (1.0 + 1.0/q)
        q -= step
        if abs(step) <= 1e-14 * max(1.0, q):
            break
    assert q > 0
    return q


def scaled_tail_constant(r, c, K=12.0):
    sr = math.sqrt(r)

    def integrand(u):
        t = r + u*sr
        if t <= 0:
            return 0.0
        q = q_boundary(t, r, c)
        b = t + q
        a = b / math.sqrt(t)
        return sr * math.exp(float(log_ndtr(-a)) + 4.5*r)

    lo = max(-K, -0.999*sr)
    val, err = quad(integrand, lo, K, epsabs=1e-12, epsrel=1e-10, limit=300)
    return val, err


def expected_tail_constant(c):
    return 16.0 / (9.0*c**3)


def critical_norm_constant():
    return (16.0/9.0)**(1.0/3.0) * (2.0/9.0)**(2.0/3.0)


def old_lower_constant():
    return 2.0**(5.0/3.0) / 9.0


print("CHECK: exact asymptotic constants for the critical additive witness")
print("predicted tail constant at c=2 =", 2.0/9.0)
print("predicted critical endpoint lower constant =", critical_norm_constant())
print("old certified lower constant =", old_lower_constant())
print("improvement factor =", critical_norm_constant()/old_lower_constant())
assert abs(critical_norm_constant() - 4.0/9.0) < 1e-14

for c in (1.0, 2.0, 4.0):
    target = expected_tail_constant(c)
    print(f"\nc={c:g}, predicted exp(9r/2)*tail -> {target:.15f}")
    for r in (20.0, 80.0, 320.0, 1280.0):
        val, err = scaled_tail_constant(r, c)
        rel = val/target - 1.0
        print(f"  r={r:7.1f}  scaled_tail={val:.15f}  rel_error={rel:+.6e}  quad_err={err:.2e}")

for c in (1.0, 2.0, 4.0):
    val, _ = scaled_tail_constant(1280.0, c)
    target = expected_tail_constant(c)
    assert abs(val/target - 1.0) < 2e-3

print("\nCHECK_PASS")
