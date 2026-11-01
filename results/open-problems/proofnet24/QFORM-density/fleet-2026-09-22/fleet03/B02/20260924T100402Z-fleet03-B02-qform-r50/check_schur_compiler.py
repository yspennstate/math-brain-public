import math
import numpy as np

rng = np.random.default_rng(20260924100402)
violations = 0
max_ratio = 0.0
trials = 0

for n in range(3, 11):
    for _ in range(200):
        G = rng.normal(size=(n, n))
        A = (G + G.T) / 2.0
        h = int(rng.integers(0, n))
        if abs(A[h, h]) < 1e-6:
            A[h, h] += 0.25 if A[h, h] >= 0 else -0.25
        idx = [i for i in range(n) if i != h]
        a = A[h, h]
        b = A[idx, h]
        C = A[np.ix_(idx, idx)]
        S = C - np.outer(b, b) / a
        sA = np.linalg.svd(A, compute_uv=False)
        sS = np.linalg.svd(S, compute_uv=False)
        lhs = sA[2]
        rhs = sS[1]
        trials += 1
        if rhs > 0:
            max_ratio = max(max_ratio, lhs / rhs)
        if lhs > rhs + 2e-10 * max(1.0, lhs, rhs):
            violations += 1

alpha = 1 / 228
C2 = 23.34314135471538
c_diffuse = C2 * math.sqrt(228)
c_second = 100 * math.sqrt(2) * math.sqrt(228) * (228 ** 0.25)
c_local_second = 100 * math.sqrt(2) * math.sqrt(228) * ((2 * math.sqrt(2) * 228) ** 0.25)
delta_min = (1 - 1 / math.sqrt(2)) * alpha**2 / 2
c_indef = math.sqrt(228) * 16 * delta_min ** (-0.25)
c_definite = 228 * math.pi
partner_p2 = math.sqrt(3) * 2 ** (1 / 3)
partner_p4 = math.sqrt(c_diffuse * partner_p2)

assert violations == 0
assert abs(c_diffuse - 352.47370485444577) < 1e-9
assert abs(c_second - 8297.860570633205) < 1e-9
assert abs(c_local_second - 10760.993806976143) < 1e-9
assert abs(c_indef - 5897.0525699759855) < 1e-9
assert abs(c_definite - 716.2831250184728) < 1e-9
assert abs(partner_p2 - 2.1822472719434427) < 1e-12
assert abs(partner_p4 - 27.734180731552403) < 1e-9

print('QFORM_R50_SCHUR_COMPILER_CHECK_PASS')
print(f'trials={trials}')
print(f'violations={violations}')
print(f'max_ratio_s3A_over_s2S={max_ratio:.16f}')
print(f'diffuse_density_constant={c_diffuse:.15f}')
print(f'second_scalar_constant={c_second:.15f}')
print(f'localized_second_scalar_constant={c_local_second:.15f}')
print(f'localized_indefinite_constant={c_indef:.15f}')
print(f'definite_pair_constant={c_definite:.15f}')
print(f'partner_p2_constant={partner_p2:.15f}')
print(f'partner_overlap_p4_constant={partner_p4:.15f}')
