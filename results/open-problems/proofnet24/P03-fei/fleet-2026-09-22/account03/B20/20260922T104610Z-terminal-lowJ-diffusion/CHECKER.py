import math


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1.0-x)*math.log2(1.0-x)


def phase(q):
    t = 0.5 + math.sqrt(q*(1.0-q))
    return 1.0 - h2(t)


def phase_prime(q):
    s = math.sqrt(q*(1.0-q))
    t = 0.5 + s
    hp = math.log2((1.0-t)/t)
    tp = (1.0-2.0*q)/(2.0*s)
    return -hp*tp


def one_point(d, K=4.0):
    q = 2.0**(1-d)
    J = d*q
    p0 = (1.0-q)**2
    p = q*q
    H = -p0*math.log2(p0) + (2**d-1)*p*(2*d-2)
    P = d*phase(q)
    c0 = 2.0/math.log(2.0)
    diffusion_rhs = c0/math.log2(1.0/J)
    sigma = h2(q)-K*q
    robust_ratio = (d-1)*sigma / ((K+phase_prime(q))*q)
    assert q/J <= diffusion_rhs + 1e-14
    return d, J, q/J, diffusion_rhs, H/J, (H-P)/J, robust_ratio


print('c0', 2.0/math.log(2.0))
for d in (8, 16, 24, 32):
    vals = one_point(d)
    print('d=%d J=%.16g q_over_J=%.12g diffusion_rhs=%.12g H_over_J=%.12g F_over_J=%.12g robust_trigger_ratio=%.12g' % vals)
print('RESULT PASS')
