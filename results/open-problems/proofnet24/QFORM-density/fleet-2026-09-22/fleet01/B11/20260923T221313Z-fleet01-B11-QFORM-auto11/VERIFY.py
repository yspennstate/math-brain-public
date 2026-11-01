from math import sqrt, exp

beta0 = 289/15984
kappa = (34/111)*(17/288)**2
beta_floor = sqrt(255)/16
ell_floor = sqrt(765)/32
aligned_const = 3*exp(5/6)*(32/(sqrt(765)*beta0*kappa))**(1/3)
partner_const = 6*(8/(kappa*beta0))**(1/3)

assert abs(beta0-0.01808058058058058) < 1e-15
assert abs(kappa-0.001067256492603715) < 1e-15
assert beta_floor > 0.998
assert ell_floor > 0.864
assert aligned_const < 270.176
assert partner_const < 447.393

# Exact algebra used in the unique-heavy canonicalization:
# q>3/4, |alpha|<mu/16 and alpha^2+beta^2>=mu^2 imply
# q*(beta^2 + alpha^2*(1-q)) > (765/1024)*mu^2.
for q in (0.7500001, 0.8, 0.9, 0.99, 0.999999):
    # worst permitted beta^2 occurs at |alpha|=mu/16; set mu=1.
    alpha2 = 1/256
    beta2 = 1-alpha2
    lhs = q*(beta2 + alpha2*(1-q))
    assert lhs > 765/1024

print('beta0 =', beta0)
print('kappa_* =', kappa)
print('transverse beta / mu >', beta_floor)
print('heavy scalar-form norm / mu >', ell_floor)
print('aligned endpoint density constant <', aligned_const)
print('partner punctured density constant <', partner_const)
print('QFORM_B11_ORIGINAL_HUB_CHAIN_CHECK_PASS')
