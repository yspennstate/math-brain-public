"""K(a,b;m) of the T067 q=4 draft (sec 6, Table 2, Appendix A), written from the paper text only.
Works for any ring of scalars (Fraction, float, or polynomial objects supporting + - * and division by s via callback)."""
from fractions import Fraction as F
from itertools import permutations

G = {0: F(32189, 5000), 1: F(307513, 304635), 2: F(1349531, 958408), 3: F(13119169, 971828),
     8: F(2046290, 998719), 10: F(10803745609, 1218540000), 11: F(649352, 585675), 12: F(-96567, 5000),
     13: F(-33529637, 939631), 14: F(-96567, 5000), 15: F(1007541, 284861), 16: F(2858842, 731359),
     17: F(8086351, 894289), 18: F(314989, 778090), 19: F(-293112, 998719), 20: F(390816, 998719),
     21: F(2119698, 387547), 22: F(-760908, 859123), 23: F(-9410, 911487),
     29: F(-1454253, 671354), 30: F(-1640643, 978656), 31: F(-146556, 998719), 32: F(-505057, 629438)}
G24_BASE = F(-44673597587449418976423934191113, 1462309266444848905334068011200160)
G24_SHIFT = F(1743, 480965)
G[24] = G24_BASE + G24_SHIFT
assert G[24] == F(-3787526362446847631199691392941357033, 140663915267129350750800004201376990880)
BETA = F(1, 10**6)
U = F(1375940705703331, 30399297484750848)
MBIG = 8 * U
assert MBIG == F(1375940705703331, 3799912185593856)
PERMS = list(permutations(range(4)))


def pw(a, b, i, j):
    return sum(a[k] ** i * b[k] ** j for k in range(4))


def features(a, b, m):
    """returns (pieces) where K = poly + R1/s + R2/s^2 + R3/s^3 ; R_k are polynomial in a,b,m."""
    A, B = pw(a, b, 2, 0), pw(a, b, 0, 2)
    ta, tb = pw(a, b, 3, 0), pw(a, b, 0, 3)
    sa, sb = pw(a, b, 4, 0), pw(a, b, 0, 4)
    c = pw(a, b, 1, 1)
    p21, p12, p22 = pw(a, b, 2, 1), pw(a, b, 1, 2), pw(a, b, 2, 2)
    p31s = pw(a, b, 3, 1) + pw(a, b, 1, 3)
    p32, p23, p33 = pw(a, b, 3, 2), pw(a, b, 2, 3), pw(a, b, 3, 3)
    p42, p24 = pw(a, b, 4, 2), pw(a, b, 2, 4)
    ell = p21 + p12
    kap = c * ell - (B * ta + A * tb) / 3
    H = [a[i] + b[i] + a[i] * b[i] - c / 4 for i in range(4)]
    N = sum(h * h for h in H)
    J = sum(h * h * h for h in H)
    sym4 = sum(sum(a[k] * b[p[k]] for k in range(4)) ** 4 for p in PERMS)
    # polynomial part and parts over s, s^2, s^3
    P = {}
    P[0] = (F(2, 3) * ta * tb - BETA * m * A * B
            + G[1] * (A * B * (A + B) + m * (A * A + B * B))
            - G[0] * m * (ta + tb)
            + G[2] * (A + B) * (c * c - A * B / 3) + G[3] * m * (c * c - A * B / 3)
            + G[8] * (c ** 3 - F(2, 3) * ta * tb) + G[10] * m * c * (A + B) + G[11] * c * ta * tb
            + G[12] * m * ell + G[13] * m * (p22 - A * B / 4) + G[14] * m * p31s
            + G[15] * m * c * (ta + tb) + G[16] * m * ell * (A + B) + G[17] * m * kap
            + G[18] * m * (p32 + p23 - (B * ta + A * tb) / 4) + G[19] * (c * p22 - ta * tb / 3)
            + G[20] * (p33 - ta * tb / 4) + G[21] * (p42 + p24 - (B * sa + A * sb) / 4)
            + G[22] * m * c * (A * A + B * B) + G[23] * (24 * c ** 4 - sym4)
            + G[24] * (A * B * (A + B) - m * (A * A + B * B))
            + G[29] * (c * p31s - (B * sa + A * sb) / 3)
            + G[30] * (p21 ** 2 + p12 ** 2 - (B * sa + A * sb - A * B * (A + B) / 4) / 3)
            + G[31] * (p21 * p12 - ta * tb / 3) + G[32] * (A + B) * (p22 - A * B / 4))
    P[1] = -N * c * c                  # over s
    P[2] = G[0] * m * J                # over s^2
    P[3] = -G[1] * m * N * N           # over s^3
    return P, 1 + c / 4


def K(a, b, m):
    P, s = features(a, b, m)
    return P[0] + P[1] / s + P[2] / s ** 2 + P[3] / s ** 3
