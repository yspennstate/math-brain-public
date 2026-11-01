import math, random

random.seed(0)
max_cross = 0.0
max_level = 0.0
max_scaled_integrand = 0.0

for _ in range(10000):
    s = 10 ** random.uniform(-6, 3)
    th = random.uniform(0.0, 2.0 * math.pi)
    t = random.uniform(-100.0, 100.0)
    c, si = math.cos(th), math.sin(th)
    rs = math.sqrt(s)

    z = (rs*c - t*si, rs*si + t*c, t)
    dth = (-rs*si - t*c, rs*c - t*si, 0.0)
    dt = (-si, c, 1.0)
    cross = (
        dth[1]*dt[2] - dth[2]*dt[1],
        dth[2]*dt[0] - dth[0]*dt[2],
        dth[0]*dt[1] - dth[1]*dt[0],
    )
    half_grad = (z[0], z[1], -z[2])
    max_cross = max(max_cross, max(abs(cross[i]-half_grad[i]) for i in range(3)))
    max_level = max(max_level, abs(z[0]*z[0] + z[1]*z[1] - z[2]*z[2] - s))

    l1 = 10 ** random.uniform(0, 4)
    l2 = 10 ** random.uniform(0, 4)
    mu = 10 ** random.uniform(0, 4)
    denom = math.sqrt(l2*mu*si*si + l1*mu*c*c + l1*l2)
    max_scaled_integrand = max(max_scaled_integrand, math.sqrt(2.0)/denom)

print('samples=10000')
print('max_cross_identity_error=', repr(max_cross))
print('max_level_identity_error=', repr(max_level))
print('max_sqrt2_times_integrand=', repr(max_scaled_integrand))
print('STATUS=', 'PASS' if max_scaled_integrand <= 1.0 + 1e-12 else 'FAIL')
