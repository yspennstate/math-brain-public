from math import sqrt, e

mu = 1/48
alpha = (1-sqrt(3*mu))/2
ell = mu/alpha
epsilon = 1/16
sigma0 = alpha
sigma = sigma0-epsilon
tau = 1/2
gamma = tau*sigma
theta0 = 3/(1+tau*tau)
ridge_diag_bound = (sqrt(ell)+epsilon/gamma)**2
C = sqrt(e)/(sqrt(2)*gamma) * theta0/(theta0-2)
C_closed = 96*sqrt(2*e)/5

print(f"alpha={alpha:.15f}")
print(f"ell={ell:.15f}")
print(f"sigma={sigma:.15f}")
print(f"gamma={gamma:.15f}")
print(f"theta0={theta0:.15f}")
print(f"ridge_diag_bound={ridge_diag_bound:.15f}")
print(f"C={C:.15f}")
print(f"C_closed={C_closed:.15f}")
assert abs(alpha-3/8) < 1e-14
assert abs(ell-1/18) < 1e-14
assert abs(sigma-5/16) < 1e-14
assert abs(gamma-5/32) < 1e-14
assert abs(theta0-12/5) < 1e-14
assert ridge_diag_bound < 1/2
assert abs(C-C_closed) < 1e-12
print("QFORM_ROBUST_SEPARATOR_RIDGE_CHECK_PASS")
