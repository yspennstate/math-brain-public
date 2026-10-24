import math

CSTAR = 16 * math.sqrt(2) / (3 ** (3/4))
print(f"CSTAR={CSTAR:.15g}")

for eta in (1e-2, 1e-4, 1e-8, 1e-12):
    r = math.sqrt(1 + eta)
    logterm = math.log((r + 1 + math.sqrt(eta)) ** 2 / (2 * math.sqrt(eta)))
    H = 2 * math.sqrt(2 * eta) / r * logterm
    b = (1 - eta) / (2 * eta)
    a = (1 + eta) / (2 * eta)
    eig_hi = 1 / eta
    eig_lo = 1.0
    Hscaled = H * math.sqrt(b)
    coll_pivot = CSTAR / math.sqrt(a)
    coll_cross = 8 / math.sqrt(b)
    delta = (1 / eta) / (b * b)

    assert abs(delta - 4 * eta / (1 - eta) ** 2) <= 1e-12 * max(1, delta)
    assert abs(Hscaled - 2 * math.sqrt((1-eta)/(1+eta)) * logterm) <= 1e-12 * max(1, Hscaled)
    print(
        f"eta={eta:.0e} eig=({eig_hi:.12g},{eig_lo:.12g}) "
        f"b={b:.12g} H={H:.12g} Hsqrtb={Hscaled:.12g} "
        f"collPivot<={coll_pivot:.12g} collCross<={coll_cross:.12g} "
        f"delta={delta:.12g}"
    )

print("STATUS=PASS")
