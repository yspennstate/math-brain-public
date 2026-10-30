import math


def check(n):
    assert n % 4 == 0 and n > 16
    delta = n ** -0.5
    lam1 = (1 - 2 * delta) * n + 2 * delta
    lamv = delta * n + 2 * delta
    lamu = -delta * n + 2 * delta
    lamperp = 2 * delta
    q = (6 * n - 4) * delta ** 2
    pdiag = 3 / n

    assert lam1 >= 1
    assert lamv >= 1
    assert abs(lamu) >= 1
    assert abs(q - (6 - 4/n)) < 1e-12

    if n > 16384:
        assert lamperp < 1/64
        assert pdiag < 1/32

    return (delta, lam1, lamv, lamu, lamperp, q, pdiag)


for n in (10000, 16384, 20000, 65536):
    print(n, check(n))

partner = 6 * math.sqrt(math.pi) / (1 - 8/128)
ridge = 288 * math.sqrt(3 * math.e) / 13
print('partner_delta_1_over_128', partner)
print('ridge_constant', ridge)
assert partner < 11.344
assert ridge < 64
print('QFORM_B11_R26_BALANCED_FIXED_PACKET_CHECK_PASS')
