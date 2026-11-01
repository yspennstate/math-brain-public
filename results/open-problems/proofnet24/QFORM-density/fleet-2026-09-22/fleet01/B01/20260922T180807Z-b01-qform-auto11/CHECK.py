import math

try:
    import mpmath as mp
except Exception:
    mp = None


def M(m):
    if mp is None:
        g = math.gamma
        return g(4/3)**3 * g(m+1)**3 / (m * g(m+1/3)**3)
    return mp.gamma(mp.mpf(4)/3)**3 * mp.gamma(m+1)**3 / (m * mp.gamma(m+mp.mpf(1)/3)**3)

print("Gamma(4/3)^3 =", float((mp.gamma(mp.mpf(4)/3)**3) if mp else math.gamma(4/3)**3))
for m in [2,3,5,10,20,50,100,500]:
    val = float(M(m))
    print(f"m={m:3d} M_m={val:.15f} M_m/m={val/m:.15f}")

c = 3 * 256**(1/3)
print("3*256^(1/3) =", repr(c))
assert 19.04 < c < 19.05
assert float(M(500)) > 350
print("STATUS=PASS")
