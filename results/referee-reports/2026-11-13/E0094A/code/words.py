"""Exact permutation certificates for the doubling-generator argument."""
import json
from pathlib import Path


def inverse(word):
    return [-s for s in reversed(word)]


def power_c(i):
    """A binary word for c**i; letters 1=c, 2=sigma, 3=tau."""
    if i == 0:
        return []
    bits = bin(i)[2:]
    word = [1]
    for bit in bits[1:]:
        word = [2] + word + [-2] + ([1] if bit == "1" else [])
    return word


def transpose_word(n, i, j):
    d = (j - i) % n
    assert d
    positions = [k for k in range(d.bit_length()) if (d >> k) & 1]
    # B = sigma**j1 tau c sigma**(j2-j1) ... tau c sigma**(jr-jr-1).
    b = [2] * positions[0]
    for u, v in zip(positions, positions[1:]):
        b += [3, 1] + [2] * (v - u)
    a = power_c(i)
    return a + b + [3] + inverse(b) + inverse(a)


def evaluate(n, word):
    ident = list(range(n))
    sigma = [2 * x % n for x in ident]
    si = [0] * n
    for x, y in enumerate(sigma):
        si[y] = x
    gs = {1: [(x + 1) % n for x in ident],
          -1: [(x - 1) % n for x in ident], 2: sigma, -2: si,
          3: [1, 0] + list(range(2, n))}
    gs[-3] = gs[3]
    p = ident
    for s in word:
        p = [p[gs[s][x]] for x in ident]
    return p


def main():
    rows = []
    for n in list(range(3, 102, 2)) + [127, 129, 255, 257]:
        maxlen = 0
        for i in range(n):
            for j in range(i + 1, n):
                w = transpose_word(n, i, j)
                p = list(range(n))
                p[i], p[j] = p[j], p[i]
                assert evaluate(n, w) == p, (n, i, j)
                assert len(w) <= 12 * (n - 1).bit_length()
                maxlen = max(maxlen, len(w))
        rows.append(dict(n=n, pairs=n*(n-1)//2, max_length=maxlen,
                         bound=12*(n-1).bit_length()))
        print(rows[-1], flush=True)
    Path('data/word_certificates.json').write_text(json.dumps(rows, indent=2)+'\n')


if __name__ == '__main__':
    main()
