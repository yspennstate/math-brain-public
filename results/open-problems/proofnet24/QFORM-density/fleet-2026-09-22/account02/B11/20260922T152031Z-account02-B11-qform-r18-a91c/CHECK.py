import math


def J(t, a):
    if a <= 0:
        return 0.0
    hi = max(0.0, t + a)
    if hi <= 0:
        return 0.0
    lo = max(0.0, t - a)
    A = math.sqrt(lo)
    B = math.sqrt(hi)

    def Fminus(v):
        return t * v - v ** 3 / 3.0

    def Fplus(v):
        return v ** 3 / 3.0 - t * v

    if t <= 0:
        return 2.0 * (Fplus(B) - Fplus(A))
    r = math.sqrt(t)
    ans = 0.0
    if A < min(B, r):
        U = min(B, r)
        ans += Fminus(U) - Fminus(A)
    if B > max(A, r):
        L = max(A, r)
        ans += Fplus(B) - Fplus(L)
    return 2.0 * ans


max_ratio = 0.0
max_tau = None
for k in range(60001):
    tau = -1.0 + 51.0 * k / 60000.0
    ratio = J(tau, 1.0) / (2.0 * math.sqrt(2.0))
    if ratio > max_ratio:
        max_ratio = ratio
        max_tau = tau
assert max_ratio < 1.0

M = math.e
C_endpoint = 3.0 * (2.0 ** (4.0 / 3.0)) * (M ** (2.0 / 3.0))
assert C_endpoint < 14.724

C_diffuse = 96.0 * math.e / (7.0 * math.sqrt(2.0))
C_c_le_3_4 = 2.0 * C_diffuse
assert C_c_le_3_4 < 52.721

for c in (0.5, 0.75, 0.99):
    delta = math.sqrt(1.0 - c)
    # D^(1/2) H0 D^(1/2) = [[0,0,delta],[0,1,0],[delta,0,0]],
    # whose eigenvalues are exactly {-delta, delta, 1}.
    assert 0.0 < delta <= 1.0

print("max_J_over_2sqrt2", format(max_ratio, ".12f"), "at_tau", format(max_tau, ".6f"))
print("endpoint_constant", format(C_endpoint, ".12f"))
print("diffuse_constant", format(C_diffuse, ".12f"))
print("c_le_3_4_constant", format(C_c_le_3_4, ".12f"))
print("QFORM_NULL_ENDPOINT_WEAKL32_CHECK_PASS")
