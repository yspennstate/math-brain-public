from math import sqrt

# Strict N3 threshold used in the current compiler.
tau = 1.0/128.0
eta = sqrt(tau + tau*tau)
delta = tau + eta
lev = 2.0*eta*eta/(1.0-delta)**2
star = 4.0/(1.0-delta)
partner = 2.0*sqrt(2.0)/(1.0-delta)

print(f"tau={tau:.16f}")
print(f"eta={eta:.16f}")
print(f"delta={delta:.16f}")
print(f"leverage_bound={lev:.16f}")
print(f"star_density_bound={star:.16f}")
print(f"partner_zero_core_bound={partner:.16f}")

assert delta < 1.0
assert lev < 0.5
assert star < 4.428
assert partner < 3.131

# Exact determinant identity used in the aligned-clique rank-two approximant.
# In the orthonormal basis (e_h, e_k, w/||w||), the proposed approximant is
# [[alpha, theta*v_k, theta*r],
#  [theta*v_k, lambda*v_k^2+d, lambda*v_k*r],
#  [theta*r, lambda*v_k*r, lambda*r^2]].
# Direct expansion gives d*r^2*(alpha*lambda-theta^2).
# Setting alpha=theta^2/lambda makes the determinant zero, hence rank <=2.

def determinant_formula(alpha, theta, vk, r, lam, d):
    a11 = alpha
    a12 = theta*vk
    a13 = theta*r
    a22 = lam*vk*vk + d
    a23 = lam*vk*r
    a33 = lam*r*r
    return (a11*(a22*a33-a23*a23)
            - a12*(a12*a33-a13*a23)
            + a13*(a12*a23-a13*a22))

samples = [
    (3.0, 2.0, 5.0, 7.0, 11.0, 13.0),
    (-4.0, 1.5, -2.0, 0.7, -3.0, 8.0),
]
for _, theta, vk, r, lam, d in samples:
    alpha = theta*theta/lam
    val = determinant_formula(alpha, theta, vk, r, lam, d)
    scale = max(1.0, abs(theta), abs(vk), abs(r), abs(lam), abs(d))**6
    assert abs(val) <= 1e-10*scale

print("aligned_clique_rank2_determinant_check=PASS")
