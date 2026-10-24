from math import gamma, pi, sqrt, exp

# Exact p=3 constant from the general formula.
p = 3.0
q = p/(p-1.0)
Aq = gamma(2.0-q)*gamma(q+1.0)
K = (2.0/(2.0-q))*(((2.0-q)/q)**(q/2.0))*sqrt(Aq)
K_clean = 2.0*sqrt(pi)/(3.0**0.25)
assert abs(Aq-3.0*pi/4.0) < 1e-14
assert abs(K-K_clean) < 1e-14

# Closed-form extremizer identities for several M scales.
for M in (0.1, 1.0, 10.0):
    lam = sqrt(pi)*(M**0.75)/(2.0*(3.0**0.25))
    c = 4.0*(lam**1.5)/pi
    mass = c*(pi/4.0)*(lam**(-1.5))
    l3cubed = (c**3)*(3.0*pi/4.0)*(lam**(-0.5))
    objective = c*pi*(lam**(-0.5))
    rhs = K_clean*(M**0.75)
    assert abs(mass-1.0) < 1e-12
    assert abs(l3cubed-M**3) < 1e-10*max(1.0,M**3)
    assert abs(objective-rhs) < 1e-12*max(1.0,rhs)

# Improvement on the localized-diffuse branch.
new_branch = K_clean*sqrt(3.0*exp(1.0))
old_branch = 4.0*sqrt(3.0*exp(1.0))
ratio = new_branch/old_branch
assert new_branch < old_branch
assert abs(ratio - sqrt(pi)/(2.0*(3.0**0.25))) < 1e-14

print(f"A_3/2={Aq:.15f}")
print(f"K3={K_clean:.15f}")
print(f"new_localized_diffuse_constant={new_branch:.15f}")
print(f"old_localized_diffuse_constant={old_branch:.15f}")
print(f"new_over_old={ratio:.15f}")
print("EXTREMIZER_IDENTITIES=PASS")
print("STATUS=PASS")
