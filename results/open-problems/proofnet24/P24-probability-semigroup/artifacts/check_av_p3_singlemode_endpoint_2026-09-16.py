from fractions import Fraction as F


def kappa(r):
    return r*(F(3)-r)/F(2)

def gamma(r):
    return r*(r-F(3))/F(2)

samples = [F(5,2), F(8,3), F(11,4)]
for r in samples:
    k = kappa(r)
    assert k > 0
    assert gamma(r) == -k
    c1 = r
    c2 = r*(r-F(1))
    c3 = r*(r-F(1))/F(2)
    eps_a = k/(F(6)*r)
    eps_b1 = k/(F(6)*r*(r-F(1)))
    eps_b2 = k/(F(3)*r*(r-F(1)))
    assert c1*eps_a == k/F(6)
    assert c2*eps_b1 == k/F(6)
    assert c3*eps_b2 == k/F(6)
    assert c1*eps_a + c2*eps_b1 + c3*eps_b2 == k/F(2)
    print(f"r={r}: kappa={k}, gamma={gamma(r)}, absorption={k/F(2)}")

assert kappa(F(3)) == 0
assert gamma(F(3)) == 0
assert gamma(F(4)) == F(2)
assert gamma(F(2)) == F(-1)

# General-beta family: gamma_{r,beta}= -r + r(r-1)beta^2/2,
# critical r_c=1+2/beta^2. Check exact prescribed-R construction.
for R in [F(5,2), F(3), F(4), F(10)]:
    beta2 = F(1) + F(1)/(R-F(1))
    rc = F(1) + F(2)/beta2
    target = F(3) - F(2)/R
    assert beta2 < F(2)
    assert rc == target
    assert rc < R
    print(f"R={R}: beta^2={beta2}, r_c={rc} < R")

print("P24_AV_P3_SINGLEMODE_EXACT_CHECK_PASS")
