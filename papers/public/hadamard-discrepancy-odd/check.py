"""Checks for 'The discrepancy of Sylvester-Hadamard matrices in odd dimension'. Plain Python 3, no packages.

1. disc(H_k) = 2^k - 2 rho(1,k) by exhaustive search over all sign vectors, k = 1..4.
2. The Walsh transform of f(y) + b(z), b bent, is W_f(a) W_b(c) (random f; k = 3, 5; m = 2, 4).
3. The arithmetic of the corollary.
"""
import itertools
import random


def walsh_signs(x):
    """Fast Walsh-Hadamard transform of a +-1 vector of length 2^k: returns H_k x
    with (H_k)_{a,y} = (-1)^{a.y}, the Sylvester ordering."""
    v = list(x)
    h = 1
    while h < len(v):
        for i in range(0, len(v), 2 * h):
            for j in range(i, i + h):
                v[j], v[j + h] = v[j] + v[j + h], v[j] - v[j + h]
        h *= 2
    return v


def walsh(f):
    return walsh_signs([1 - 2 * b for b in f])


def check_identity(k):
    n = 2 ** k
    disc = min(max(abs(t) for t in walsh_signs(x)) for x in itertools.product((-1, 1), repeat=n))
    rho = max((n - max(abs(t) for t in walsh(f))) // 2 for f in itertools.product((0, 1), repeat=n))
    assert disc == n - 2 * rho, (k, disc, rho)
    print(f"k={k}: disc(H_k)={disc}, rho(1,k)={rho}, 2^k-2rho={n - 2 * rho}")


def bent(m):
    """Maiorana-McFarland bent function b(u, v) = u.v on F_2^(m/2) x F_2^(m/2)."""
    h = m // 2
    return [bin((z >> h) & (z & (2 ** h - 1))).count("1") % 2 for z in range(2 ** m)]


def check_direct_sum(k, m, trials=20, seed=1):
    rng = random.Random(seed)
    b = bent(m)
    Wb = walsh(b)
    assert {abs(t) for t in Wb} == {2 ** (m // 2)}
    for _ in range(trials):
        f = [rng.randint(0, 1) for _ in range(2 ** k)]
        g = [f[y] ^ b[z] for y in range(2 ** k) for z in range(2 ** m)]  # index y*2^m + z
        Wf, Wg = walsh(f), walsh(g)
        assert Wg == [Wf[a] * Wb[c] for a in range(2 ** k) for c in range(2 ** m)]
        assert max(map(abs, Wg)) == 2 ** (m // 2) * max(map(abs, Wf))
    print(f"direct sum k={k}, m={m}: W_g = W_f x W_b on {trials} random f")


if __name__ == "__main__":
    for k in range(1, 5):
        check_identity(k)
    for k, m in [(3, 2), (3, 4), (5, 2)]:
        check_direct_sum(k, m)
    for k, rho in [(1, 0), (3, 2), (5, 12), (7, 56)]:
        assert 2 ** k - 2 * rho == 2 ** ((k + 1) // 2)
    assert 512 - 2 * 242 == 28 and 512 - 2 * 241 == 30 and 28 < 32
    assert 2 ** 15 - 2 * 16276 == 216 and 216 * 32 == 27 * 256
    print("corollary arithmetic: ok")
