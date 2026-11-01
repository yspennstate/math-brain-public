import math, itertools
C3 = 3*math.sqrt(2)*math.e*(9/2)**(1/6)
C2 = 8*math.sqrt(math.e)*2**(-1/8)
L0 = 2 + 2*math.log(19)
def branches(eta, zeta):
    a0 = math.sqrt(eta*eta + zeta)
    c5 = (1 - eta - 5*math.sqrt(2)*a0)/2
    c3 = (1 - eta - 3*math.sqrt(2)*a0)/2
    if c5 <= 0: return None
    H_np = C2/math.sqrt(c3); H_pair = 16*zeta**-0.25
    H_sc = eta**-0.5*(math.pi + 4*math.log(2) + 2*L0) + 1
    H3 = max(H_np, H_pair, H_sc)
    d = dict(nopivot=C3/c5, scalar=eta**-0.5*H3, definite=math.pi/math.sqrt(zeta),
             indefinite=zeta**-0.5*(6 + math.log(16) + L0) + 1/math.e)
    return d, H3, c5, c3, a0
best = None
for eta in [i/1000 for i in range(20, 160)]:
    for zeta in [j/10000 for j in range(5, 200)]:
        r = branches(eta, zeta)
        if r is None: continue
        m = max(r[0].values())
        if best is None or m < best[0]: best = (m, eta, zeta, r)
print("optimum over grid:", best[0], "eta", best[1], "zeta", best[2]); print(best[3])
for eta, zeta in [(3/40, 1/400), (1/10, 1/200), (1/12, 1/300), (1/10, 1/250), (2/25, 1/250), (1/10, 1/300)]:
    r = branches(eta, zeta)
    print(eta, zeta, None if r is None else ({k: round(v, 2) for k, v in r[0].items()}, round(r[1], 2), round(r[2], 4)))
print("--- rational candidates ---")
from fractions import Fraction as F
for eta in (F(1,11), F(9,100), F(2,23), F(1,12), F(7,80), F(11,125)):
    for zeta in (F(1,200), F(1,210), F(1,216), F(1,220), F(1,225), F(1,250)):
        r = branches(float(eta), float(zeta))
        if r is None: continue
        m = max(r[0].values())
        if m < 255:
            print(eta, zeta, round(m, 2), {k: round(v, 1) for k, v in r[0].items()}, "H3", round(r[1], 2), "c5", round(r[2], 4))
