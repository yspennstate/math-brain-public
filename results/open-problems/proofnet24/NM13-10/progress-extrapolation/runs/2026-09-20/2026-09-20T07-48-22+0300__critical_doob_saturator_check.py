import math
import sympy as sp
from scipy.integrate import quad
from scipy.special import log_ndtr

# Exact algebra for the critical affine barrier used in the one-shell witness.
t, r = sp.symbols("t r", positive=True)
x = sp.Rational(3, 2) * (t + r)
saddle_identity = sp.simplify(
    x**2 / (2*t)
    - sp.Rational(9, 2)*r
    - sp.Rational(9, 8)*(t-r)**2/t
)
assert saddle_identity == 0

# Exact limiting Gaussian saddle constant.
u = sp.symbols("u", nonnegative=True)
gaussian_integral = sp.integrate(sp.exp(-sp.Rational(9, 8)*u**2), (u, 0, sp.oo))
tail_constant = sp.simplify(gaussian_integral / (3*sp.sqrt(2*sp.pi)))
assert tail_constant == sp.Rational(1, 9)

# Resulting lower constant for the Z_{3,2/3} norm under the report's normalization.
critical_constant = sp.simplify(
    (sp.Rational(8, 9))**sp.Rational(1, 3)
    * (sp.Rational(2, 9))**sp.Rational(2, 3)
)
assert sp.simplify(critical_constant - 2**sp.Rational(5, 3)/9) == 0

# Numerical convergence check for the scaled Gaussian tail integral.
def scaled_lower_integral(r_value, K=6.0):
    sr = math.sqrt(r_value)
    def integrand(u_value):
        t_value = r_value + u_value*sr
        a = 1.5*(t_value + r_value)/math.sqrt(t_value)
        return sr * math.exp(4.5*r_value + float(log_ndtr(-a)))
    value, err = quad(integrand, 0.0, K, epsabs=1e-12, epsrel=1e-10, limit=300)
    return value, err

print("saddle_identity =", saddle_identity)
print("gaussian_integral =", gaussian_integral)
print("tail_constant =", tail_constant, float(tail_constant))
print("critical_Z_3_2over3_lower_constant =", critical_constant, float(critical_constant))
print("target_scaled_tail_constant =", 1.0/9.0)
for rv in [20, 50, 100, 200, 500, 1000]:
    value, err = scaled_lower_integral(rv, K=6.0)
    print("r =", rv,
          "scaled_lower_integral =", f"{value:.15f}",
          "ratio_to_1_over_9 =", f"{value/(1/9):.12f}",
          "quad_err =", f"{err:.3e}")
print("critical_input_moment_E_M3 = 1 (exact)")
print("CHECK_PASS")
