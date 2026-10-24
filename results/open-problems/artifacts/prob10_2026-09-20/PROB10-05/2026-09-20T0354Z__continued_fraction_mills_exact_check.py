from fractions import Fraction as F
import sympy as sp

# Symbolic Riccati supersolution identity.
x = sp.symbols('x', positive=True)
P = x**10 + 54*x**8 + 938*x**6 + 6090*x**4 + 12645*x**2 + 3840
Q = x**10 + 55*x**8 + 990*x**6 + 6930*x**4 + 17325*x**2 + 10395
u = P/(x*Q)
residual = sp.factor(sp.diff(u, x) - (x*u - 1))
target_residual = -sp.Integer(39916800)/(x**2 * Q**2)
assert sp.simplify(residual - target_residual) == 0

# Frozen inherited parameters.
r = F(7,8)
rho = F(168557580,170952323)
q = F(202269096,1697549515)
sqrt_lb = F(8398,100000)

# Tenth even continued-fraction rational for x*m(x), q=x^{-2}.
R10 = (
    1 + 54*q + 938*q**2 + 6090*q**3 + 12645*q**4 + 3840*q**5
) / (
    1 + 55*q + 990*q**2 + 6930*q**3 + 17325*q**4 + 10395*q**5
)
assert R10 < F(909,1000)
assert R10 < F(91,100)

# Guaranteed improvement over the prior 0.91 resolvent cap, normalized by 1-r^4.
delta_norm = sqrt_lb * (F(91,100) - R10) / (16*(1-r**4))
peq_norm_cap = F(1090902,10**6) - delta_norm

# Consume the independently archived 256-block Plackett decrement >743/200000.
plackett_dec = F(743,200000)
trace_exact_cap = peq_norm_cap - plackett_dec/(1-r**4)
trace_simple_cap = F(270477519,250000000)  # 1.081910076
assert trace_exact_cap < trace_simple_cap

# New candidate exponent and rational spectral threshold.
theta = F(20685439,125000000)              # 0.165483512
exp4theta = 4*theta
x0 = F(572127961,625000000)                # 0.9154047376

# Exact logarithm enclosure:
# -log(a)=2*sum_{k>=0} z^(2k+1)/(2k+1), z=(1-a)/(1+a)
# tail after k=N is <= 2 z^(2N+3)/[(2N+3)(1-z^2)].
def neglog_bounds(a, N):
    z = (1-a)/(1+a)
    lo = sum(F(2)*z**(2*k+1)/F(2*k+1) for k in range(N+1))
    tail = F(2)*z**(2*N+3)/(F(2*N+3)*(1-z*z))
    return lo, lo+tail

Lx, Ux = neglog_bounds(x0, 3)
Lr, Ur = neglog_bounds(r, 3)
log_margin = Lx - exp4theta*Ur
assert log_margin > 0
# Therefore -log x0 > 4 theta (-log r), i.e. x0 < r^(4 theta).

# Fourth-trace tail separation and Temple contradiction.
mu_lo = F(9116948312,10_000_000_000)
mu_hi = F(9116948313,10_000_000_000)
eps2 = F(47004495,100_000_000_000)
beta = F(7849948769,10_000_000_000)

assert x0 > mu_hi
assert mu_lo > beta
tail_margin = beta**4 - (trace_simple_cap - x0**4)
assert tail_margin > 0
temple_margin = (x0-mu_hi)*(mu_lo-beta) - eps2
assert temple_margin > 0

old_theta = F(165483,10**6)
old_width = F(1,4)-old_theta
new_width = F(1,4)-theta
assert theta > old_theta
assert new_width < old_width

def dec(fr, digits=18):
    return f"{float(fr):.{digits}g}"

print("Riccati residual identity =", residual)
print("R10 =", R10)
print("R10_decimal =", dec(R10))
print("0.909_minus_R10 =", F(909,1000)-R10)
print("delta_norm =", delta_norm)
print("delta_norm_decimal =", dec(delta_norm))
print("peq_norm_cap_decimal =", dec(peq_norm_cap))
print("trace_exact_cap_decimal =", dec(trace_exact_cap))
print("trace_simple_cap =", trace_simple_cap, dec(trace_simple_cap))
print("log_margin =", log_margin)
print("log_margin_decimal =", dec(log_margin))
print("tail_margin =", tail_margin)
print("tail_margin_decimal =", dec(tail_margin))
print("temple_margin =", temple_margin)
print("temple_margin_decimal =", dec(temple_margin))
print("old_theta =", old_theta, dec(old_theta))
print("new_theta =", theta, dec(theta))
print("theta_gain =", theta-old_theta, dec(theta-old_theta))
print("old_width =", old_width, dec(old_width))
print("new_width =", new_width, dec(new_width))
print("ALL_EXACT_CHECKS_PASS = True")
