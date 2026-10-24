import math

gamma = 2.0
exponents = [8, 12, 16, 20]

print("benchmark: k=sqrt(m), sigma=m^(-1/3), q=1/(m log(m)^2), gamma=2")
print("columns: exp mu d d/k log_union_bound old_D1_ratio row_loss_bound S1 S2ratio atom3")
prev_old = None
for exp in exponents:
    m = 10.0**exp
    N = gamma*m
    k = math.sqrt(m)
    sigma = m**(-1.0/3.0)
    q = 1.0/(m*math.log(m)**2)
    mu = N*q
    L = math.log(1.0/(math.e*mu))
    assert L > 0
    d = math.ceil(3.0*math.log(m)/L)
    log_union = math.log(m) + d*(1.0 + math.log(mu) - math.log(d))
    old_D1_ratio = N*m*q/k
    row_loss_bound = mu
    S1 = m*sigma*sigma / math.log(math.e/sigma)
    S2ratio = k*(math.log(m)+math.log(math.e/sigma))/m
    atom3 = (q/2.0)**3
    print(exp, f"{mu:.12g}", d, f"{d/k:.12g}", f"{log_union:.12g}",
          f"{old_D1_ratio:.12g}", f"{row_loss_bound:.12g}",
          f"{S1:.12g}", f"{S2ratio:.12g}", f"{atom3:.12g}")
    assert mu < 0.01
    assert d/k < 0.002
    assert log_union < -10
    assert old_D1_ratio > 10
    assert row_loss_bound < 0.01
    assert S1 > 10
    assert S2ratio < 0.01
    assert atom3 > 0
    if prev_old is not None:
        assert old_D1_ratio > prev_old
    prev_old = old_D1_ratio

print("ASYMPTOTIC_IDENTITIES:")
print("mu ~ gamma/log(m)^2 -> 0")
print("old_D1_ratio ~ gamma*sqrt(m)/log(m)^2 -> infinity")
print("occupancy_d = O(log(m)/loglog(m)) = o(sqrt(m))")
print("defective_row_fraction <= mu -> 0")
print("ALL_COLUMNWISE_OCCUPANCY_CHECKS_PASS")
