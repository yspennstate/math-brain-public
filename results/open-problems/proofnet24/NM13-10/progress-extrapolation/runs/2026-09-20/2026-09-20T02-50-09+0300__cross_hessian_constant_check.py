from math import sqrt

# Numerical sanity check for NM10-AVP3-CROSS-HESSIAN-01.
# The theorem proof is analytic; this script only evaluates the old/new
# quantitative brackets and the endpoint-normalized constants.


def kappa(p):
    return p * (1.0 + sqrt(2.0 * p - 3.0)) / 4.0


def r_star(p, beta=1.0):
    return 1.0 / (sqrt(2.0 / (p - 1.0)) - beta)


def old_upper(p, beta=1.0):
    return sqrt(p / 2.0) * r_star(p, beta)


def new_upper(p, beta=1.0):
    delta = 1.0 - beta * beta * (p - 1.0) / 2.0
    k = kappa(p)
    return (beta * k + sqrt(beta * beta * k * k + delta * p * (p - 1.0))) / (2.0 * delta)


print("p        R_lower        C_new          C_old          new/old      (3-p)C_new")
for p in (2.10, 2.25, 2.50, 2.75, 2.90, 2.99):
    lo = r_star(p)
    new = new_upper(p)
    old = old_upper(p)
    assert lo <= new <= old
    print(f"{p:4.2f}  {lo:13.9f}  {new:13.9f}  {old:13.9f}  {new / old:11.9f}  {(3 - p) * new:13.9f}")

asym_lower = 4.0
asym_new = 3.0 * (1.0 + sqrt(3.0)) / 2.0
asym_old = 4.0 * sqrt(3.0 / 2.0)
print()
print(f"endpoint normalized lower   = {asym_lower:.12f}")
print(f"endpoint normalized new up  = {asym_new:.12f}")
print(f"endpoint normalized old up  = {asym_old:.12f}")
print(f"new residual relative gap   = {asym_new / asym_lower - 1.0:.12%}")
print("NUMERICAL_SANITY_CHECK_PASS")
