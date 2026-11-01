from fractions import Fraction
from collections import defaultdict


def add(B, k, v):
    B[k] = B.get(k, Fraction(0)) + Fraction(v)


def c_value(A, N):
    return A.get(-N, Fraction(0)) - 2*A.get(2*N, Fraction(0)) - A.get(2*N-1, Fraction(0))


def subtract_scaled(A, B, scale):
    out = dict(A)
    for k, v in B.items():
        out[k] = out.get(k, Fraction(0)) - scale*v
        assert out[k] >= 0
        if out[k] == 0:
            del out[k]
    return out


def case1_block(N, i):
    B = {}
    if i == 0:
        add(B, -N, 2)
        add(B, 2*N, 1)
    elif i == 1:
        add(B, -N, 1)
        add(B, -N+1, 1)
        add(B, 2*N-1, 1)
    else:
        raise ValueError(i)
    return B


def case2_block(N, M, i):
    # For d=2, q=1 and r=2N-M in Wang-Wang Lemma 2.6.
    B = {}
    add(B, -N, 1)
    add(B, N-M+i, 1)
    add(B, M-i, 1)
    return B


def decompose_d2(A, N, pieces=None):
    if pieces is None:
        pieces = []
    A = {k: v for k, v in A.items() if v != 0}
    if not A:
        return pieces
    assert sum(Fraction(k)*v for k, v in A.items()) == 0
    if all(k == 0 for k in A):
        pieces.append((A[0]/3, {0: Fraction(3)}))
        return pieces
    assert N >= 1
    assert all(-N <= k <= 2*N for k in A)
    C = c_value(A, N)
    assert C >= 0

    if C == 0:
        if A.get(-N, Fraction(0)) == 0:
            assert A.get(2*N, Fraction(0)) == 0
            assert A.get(2*N-1, Fraction(0)) == 0
            return decompose_d2(A, N-1, pieces)
        b0 = A.get(2*N, Fraction(0))
        b1 = A.get(2*N-1, Fraction(0))
        if b0:
            B0 = case1_block(N, 0)
            pieces.append((b0, B0))
            A = subtract_scaled(A, B0, b0)
        if b1:
            B1 = case1_block(N, 1)
            pieces.append((b1, B1))
            A = subtract_scaled(A, B1, b1)
        return decompose_d2(A, N-1, pieces)

    M = max(A)
    assert N <= M <= 2*N
    # d=2 implies q=1, r=2N-M, i=0,...,2M-N.
    T = defaultdict(Fraction)
    blocks = []
    for i in range(2*M-N+1):
        B = case2_block(N, M, i)
        blocks.append(B)
        for k, v in B.items():
            T[k] += v
    CT = c_value(T, N)
    assert CT > 0
    assert T[M] > 0
    b = min(A[M]/T[M], C/CT)
    assert b > 0
    for B in blocks:
        pieces.append((b, B))
    A = subtract_scaled(A, T, b)
    return decompose_d2(A, N, pieces)


def verify(A, pieces):
    rec = defaultdict(Fraction)
    for weight, B in pieces:
        assert weight >= 0
        assert sum(B.values()) == 3
        assert sum(Fraction(k)*v for k, v in B.items()) == 0
        for k, v in B.items():
            rec[k] += weight*v
    keys = set(A) | set(rec)
    assert all(A.get(k, Fraction(0)) == rec.get(k, Fraction(0)) for k in keys)
    assert sum(weight for weight, _ in pieces) == Fraction(1, 3)


def beta_centered_floor(N):
    # Exact test law on [-1,2]: p(y)=(4-2y)/9, the image of Beta(1,2)
    # under y=3x-1.  This density is decreasing and has mean zero.
    pbar = {}
    for k in range(-N, 2*N):
        a = Fraction(k, N)
        b = Fraction(k+1, N)
        # integral_a^b (4-2y)/9 dy = [(4y-y^2)/9]_a^b
        pbar[k] = ((4*b-b*b) - (4*a-a*a))/9
    pbar[2*N] = Fraction(0)
    return pbar


def corrected_approximation(N):
    pbar = beta_centered_floor(N)
    mbar = sum(Fraction(k, N)*v for k, v in pbar.items())
    assert Fraction(-1, N) <= mbar <= 0
    # Uniform law on {-1,-1+1/N,...,2} has mean 1/2.
    lam = -mbar/(Fraction(1, 2)-mbar)
    assert Fraction(0) <= lam < Fraction(2, N)
    p = {}
    for k in range(-N, 2*N+1):
        p[k] = (1-lam)*pbar.get(k, Fraction(0)) + lam*Fraction(1, 3*N+1)
    assert sum(p.values()) == 1
    assert sum(Fraction(k)*v for k, v in p.items()) == 0
    assert all(p[k] >= p[k+1] for k in range(-N, 2*N))
    return p, mbar, lam


def main():
    print('D0008 n=3 Wang-Wang discrete decomposition exact self-check')
    for N in range(1, 9):
        A, mbar, lam = corrected_approximation(N)
        pieces = decompose_d2(A, N)
        verify(A, pieces)
        print(f'N={N} mbar={mbar} lambda={lam} pieces={len(pieces)} PASS')
    print('D0008 N3 DISCRETE DECOMPOSITION EXACT CHECK PASSED')


if __name__ == '__main__':
    main()
