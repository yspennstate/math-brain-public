from fractions import Fraction
import random
from math import sqrt

SEED = 20260922
TRIALS = 200
N = 8
M = 3


def objective(K, fs):
    s = Fraction(0)
    for i in range(N):
        if not fs[0][i]:
            continue
        for j in range(N):
            if not fs[1][j]:
                continue
            for k in range(N):
                if K[i][j][k]:
                    s += fs[0][i] * fs[1][j] * fs[2][k]
    return s


def contract(K, fs, d, x):
    total = Fraction(0)
    if d == 0:
        for j in range(N):
            for k in range(N):
                if K[x][j][k]:
                    total += fs[1][j] * fs[2][k]
    elif d == 1:
        for i in range(N):
            for k in range(N):
                if K[i][x][k]:
                    total += fs[0][i] * fs[2][k]
    else:
        for i in range(N):
            for j in range(N):
                if K[i][j][x]:
                    total += fs[0][i] * fs[1][j]
    return total


rng = random.Random(SEED)
min_gain = None
for _ in range(TRIALS):
    K = [[[rng.randrange(2) for _ in range(N)] for _ in range(N)] for _ in range(N)]
    fs = []
    for _ in range(3):
        S = set(rng.sample(range(N), M))
        T = set(rng.sample(range(N), M))
        lam = Fraction(rng.randrange(1, 10), 10)
        f = [lam * (x in S) + (1 - lam) * (x in T) for x in range(N)]
        assert sum(f) == M
        assert all(Fraction(0) <= z <= Fraction(1) for z in f)
        fs.append(f)

    prev = objective(K, fs)
    for d in range(3):
        h = [contract(K, fs, d, x) for x in range(N)]
        chosen = set(sorted(range(N), key=lambda x: (h[x], x), reverse=True)[:M])
        fs[d] = [Fraction(1 if x in chosen else 0) for x in range(N)]
        cur = objective(K, fs)
        assert cur >= prev
        gain = cur - prev
        min_gain = gain if min_gain is None or gain < min_gain else min_gain
        prev = cur

    assert all(all(z in (0, 1) for z in f) for f in fs)

R = 2.0
epsilon = 0.1
ell = sqrt(R * R + epsilon) - R
assert 2 * ell < 1
assert 2 * R > 1

print('QFORM-B13 sanity check')
print(f'discrete purification trials: {TRIALS}')
print('all coordinate replacements nondecreasing: PASS')
print(f'minimum observed one-step gain: {float(min_gain):.16g}')
print('final vectors bang-bang in every trial: PASS')
print(f'fiber falsifier parameters: R={R}, epsilon={epsilon}')
print(f'branch length ell=sqrt(R^2+epsilon)-R={ell:.15f}')
print(f'two-branch captured length={2*ell:.15f}')
print(f'single-unit-interval maximum captured length={ell:.15f}')
print('ratio disconnected/single=2 exactly')
print(f'2*ell<1: {2*ell < 1}')
print(f'branch gap=2R={2*R} > 1: {2*R > 1}')
