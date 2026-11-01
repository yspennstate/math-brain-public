from math import sqrt, e

# Exact/rational threshold checks used in REPORT.md.
eps_hat = 1/1024 + 1/17
eps_star = (39 - 6*sqrt(30))/98
delta = lambda x: 0.5 - x - sqrt(2*x)
q = 7/5

assert 1041 * 50 < 3 * 17408  # eps_hat < 3/50
assert eps_hat < eps_star
assert delta(eps_hat) > (11 - 5*sqrt(3))/25
assert 3/(11 - 5*sqrt(3)) < q < 1.5
assert 25/1024 < 1/32

C_diff_exact = 3*e/(sqrt(2*q)*delta(eps_hat)*(3-2*q))
C_diff_safe = 375*e/(sqrt(14/5)*(11-5*sqrt(3)))
C_heavy_64 = 2*sqrt(3*e)*(64*17)**(1/6)

print('eps_hat=', repr(eps_hat))
print('eps_star=', repr(eps_star))
print('delta(eps_hat)=', repr(delta(eps_hat)))
print('2eps/delta=', repr(2*eps_hat/delta(eps_hat)))
print('C_diff_exact=', repr(C_diff_exact))
print('C_diff_safe=', repr(C_diff_safe))
print('C_heavy_if_|a|^2|mu|>=1/64=', repr(C_heavy_64))

assert C_diff_safe < 261
assert C_heavy_64 < 18.32
