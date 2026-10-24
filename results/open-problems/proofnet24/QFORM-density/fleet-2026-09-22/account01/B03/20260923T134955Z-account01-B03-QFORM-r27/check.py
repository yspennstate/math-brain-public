#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 50

def F(x):
    x = mp.mpf(x)
    if x <= 1:
        return 2*x
    return 2*(1+mp.log(x))

def G(x):
    x=mp.mpf(x)
    z=1/(1+x**4)
    return mp.mpf("0.5")*mp.log(1+x**4) + (x/2)*mp.betainc(mp.mpf(1)/4,mp.mpf(3)/4,0,z)

# Exact matching of the two density branches at Theta=1/2.
theta=mp.mpf("0.5")
low=4*mp.sqrt(2*theta)
high=4+2*mp.log(2*theta)
assert abs(low-high) < mp.mpf("1e-40")

# High-normalization branch improves the crude square-root envelope.
for k in range(0,1001):
    th=mp.mpf("0.5")*10**(mp.mpf(k)/250)
    assert 4+2*mp.log(2*th) <= 4*mp.sqrt(2*th) + mp.mpf("1e-40")

# K_a layer-cake upper bound agrees with the simple comparison K<=log_++log2/2.
for x in [mp.mpf("1e-6"), mp.mpf("0.01"), mp.mpf("0.1"), mp.mpf("0.5"),
          mp.mpf("1"), mp.mpf("2"), mp.mpf("10"), mp.mpf("1e6")]:
    assert G(x) <= F(x)+mp.log(2)/2 + mp.mpf("1e-40")

# Universal natural-scale logarithmic collision constant.
collision_const = 2*G(1)
expected = mp.log(2)+mp.betainc(mp.mpf(1)/4,mp.mpf(3)/4,0,mp.mpf(1)/2)
assert abs(collision_const-expected) < mp.mpf("1e-40")

# Constants for partner and sharpened residual half-Frostman estimates.
partner_power = 8*mp.sqrt(3)*2**(mp.mpf(1)/8)
self_power = 2**(mp.mpf(29)/8)

# Concrete target family B_L direct-sum star at L=1e4.
L=mp.mpf("10000")
new = L**(-mp.mpf(1)/2)*(4+2*mp.log(8*2**(mp.mpf(1)/4)*mp.sqrt(L)))
old_self = self_power*L**(-mp.mpf(1)/4)
old_partner = partner_power*L**(-mp.mpf(1)/4)
assert new < old_self < old_partner

print("QFORM_B03_LOG_COLLISION_PASS")
print("collision_const =", mp.nstr(collision_const,18))
print("partner_power_const =", mp.nstr(partner_power,18))
print("self_power_const =", mp.nstr(self_power,18))
print("L=1e4 new_log_bound =", mp.nstr(new,18))
print("L=1e4 old_self_power =", mp.nstr(old_self,18))
print("L=1e4 partner_power =", mp.nstr(old_partner,18))
