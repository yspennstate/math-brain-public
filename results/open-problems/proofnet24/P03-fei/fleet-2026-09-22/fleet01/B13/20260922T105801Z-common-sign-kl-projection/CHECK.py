import math


def h2(p):
    if p == 0.0 or p == 1.0:
        return 0.0
    return -p*math.log2(p) - (1-p)*math.log2(1-p)


def metrics(m):
    p = 2.0**(1-m)
    hmax = m*h2(p)
    hp = -((1-p)**2)*math.log2((1-p)**2) - (2*p-p*p)*math.log2(p*p)
    k = hmax-hp
    influence_excess = m*p
    lower = (m-1)*(m-5)*p
    maxgap_upper = p/math.log(2.0)
    return p, k, influence_excess, lower, maxgap_upper


rows = []
for m in range(6, 33):
    p, k, I, lower, maxup = metrics(m)
    assert k + 1e-15 >= lower
    assert maxup/I <= 1.0/(m*math.log(2.0)) + 1e-15
    rows.append((m, k/I, maxup/I, lower/I))

print("PASS")
print("m  K_occ/Iexcess  maxgap_upper/Iexcess  analytic_joint_lower/Iexcess")
for m in (6, 8, 12, 16, 24, 32):
    p, k, I, lower, maxup = metrics(m)
    print(m, f"{k/I:.15f}", f"{maxup/I:.15f}", f"{lower/I:.15f}")
