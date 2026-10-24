from sympy import symbols, Rational, factor, simplify

n, q, s = symbols("n q s", positive=True)
alpha = 1/q
beta = 1 - alpha

def assert_eq(a,b):
    assert simplify(a-b) == 0, (a,b,simplify(a-b))

inverse_power_coefficient = factor(beta * (beta + alpha - 1))
assert_eq(inverse_power_coefficient, 0)

rho_S = factor(beta*s*((n-1)*alpha + beta*(s-1)))
assert_eq(rho_S, s*(q-1)*(n + q*s - q - s)/q**2)

metric_scale = q**2/(2*(q-1))
lambda_S = factor(metric_scale*rho_S)
assert_eq(lambda_S, s*(n + q*s - q - s)/2)

lambda_unc = factor(metric_scale*(n/q))
assert_eq(lambda_unc, n*q/(2*(q-1)))

lambda_sign_min = factor(lambda_S.subs(s, 2))
assert_eq(lambda_sign_min, n + q - 2)

sign_minus_unc = factor(lambda_sign_min - lambda_unc)
assert_eq(sign_minus_unc, (q-2)*(n + 2*q - 2)/(2*(q-1)))

lambda_step = factor(lambda_S.subs(s, s+1)-lambda_S)
assert_eq(lambda_step, (n + 2*q*s - 2*s - 1)/2)

c = Rational(2, 1)/(q-1)
variance_ratio = factor(c/(lambda_unc+c))
assert_eq(variance_ratio, 4/(n*q+4))

source_ratio = Rational(2, 1)/(n+2)
target_slack = factor(source_ratio-variance_ratio)
assert_eq(target_slack, 2*n*(q-2)/((n+2)*(n*q+4)))

covariance_margin = factor(
    n/Rational(2,1) * (1-(n/Rational(2,1)+1)*variance_ratio)
)
assert_eq(covariance_margin, n**2*(q-2)/(2*(n*q+4)))

assert_eq(variance_ratio.subs({n:3,q:4}), Rational(1,4))
assert_eq(source_ratio.subs(n,3), Rational(2,5))
assert_eq(target_slack.subs({n:3,q:4}), Rational(3,20))
assert_eq(covariance_margin.subs({n:3,q:4}), Rational(9,16))
assert_eq(Rational(19,55)-Rational(1,4), Rational(21,220))

print("INVERSE_POWER_COEFFICIENT =", inverse_power_coefficient)
print("RHO_S =", rho_S)
print("LAMBDA_S =", lambda_S)
print("LAMBDA_UNCONDITIONAL =", lambda_unc)
print("LAMBDA_SIGN_MIN =", lambda_sign_min)
print("SIGN_SECTOR_MINUS_UNCONDITIONAL =", sign_minus_unc)
print("LAMBDA_STEP_S_TO_S_PLUS_1 =", lambda_step)
print("GRADIENT_SHARE_ENERGY_CONSTANT =", factor(c))
print("VARIANCE_RATIO_BOUND =", variance_ratio)
print("SOURCE_TARGET_RATIO =", source_ratio)
print("TARGET_SLACK =", target_slack)
print("COVARIANCE_MARGIN_COEFFICIENT =", covariance_margin)
print("N3_Q4_VARIANCE_RATIO =", variance_ratio.subs({n:3,q:4}))
print("N3_Q4_SOURCE_TARGET =", source_ratio.subs(n,3))
print("N3_Q4_TARGET_SLACK =", target_slack.subs({n:3,q:4}))
print("N3_Q4_COVARIANCE_MARGIN =", covariance_margin.subs({n:3,q:4}))
print("N3_Q4_SLACK_TO_19_OVER_55 =", Rational(21,220))
print("ALL_EXACT_CHECKS_PASS = True")
