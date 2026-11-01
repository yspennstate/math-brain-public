from __future__ import annotations
from decimal import Decimal, getcontext
import math


def sqrt2_convergents(N: int):
    # sqrt(2) = [1;2,2,...], p_k/q_k, k starting at 0.
    p0, q0 = 1, 1
    if N <= 0:
        return []
    out = [(p0, q0)]
    if N == 1:
        return out
    p1, q1 = 3, 2
    out.append((p1, q1))
    for _ in range(2, N):
        p0, p1 = p1, 2 * p1 + p0
        q0, q1 = q1, 2 * q1 + q0
        out.append((p1, q1))
    return out


def nearest_sqrt3_integer_and_delta(q: int):
    """Exact nearest integer p to q*sqrt(3), and Delta=|3q^2-p^2|."""
    N = 3 * q * q
    s = math.isqrt(N)
    # Compare sqrt(N) with s+1/2 exactly by squaring after multiplying by 4.
    p = s + 1 if 4 * N >= 4 * s * s + 4 * s + 1 else s
    return p, abs(N - p * p)


def record_certificates(N: int = 10000):
    recs = []
    best = None  # (Delta,q), minimizing Delta/q exactly.
    for k, (p2, q) in enumerate(sqrt2_convergents(N)):
        p3, delta = nearest_sqrt3_integer_and_delta(q)
        assert abs(p2 * p2 - 2 * q * q) == 1
        s = math.isqrt(3 * q * q)
        assert p3 in (s, s + 1)
        if best is None or delta * best[1] < best[0] * q:
            best = (delta, q)
            recs.append((k, p2, q, p3, delta))
    return recs


def main():
    recs = record_certificates(10000)
    getcontext().prec = 30
    print("record count:", len(recs))
    print("k,digits(q),Delta/q,rigorous_simple_upper_bound")
    c = (Decimal(2).sqrt() + 1) * (Decimal(3).sqrt() + 1)
    for k, p2, q, p3, delta in recs:
        ratio = Decimal(delta) / Decimal(q)
        # Exact derivation behind this displayed decimal bound:
        # |q sqrt(2)-p2| = 1/(p2+q sqrt(2)) and
        # |q sqrt(3)-p3| = Delta/(p3+q sqrt(3)).
        # Since p2>=q and p3>=q for q>=1,
        # q||q sqrt(2)|| ||q sqrt(3)||
        # < (Delta/q)/((1+sqrt(2))(1+sqrt(3))).
        ub = ratio / c
        print(k, len(str(q)), ratio, ub)

    k, p2, q, p3, delta = recs[-1]
    print("\nlast record exact certificate")
    print("k =", k)
    print("p2 =", p2)
    print("q =", q)
    print("p3 =", p3)
    print("Delta =", delta)
    print("Pell check p2^2-2q^2 =", p2 * p2 - 2 * q * q)
    print("sqrt3 norm defect p3^2-3q^2 =", p3 * p3 - 3 * q * q)


if __name__ == "__main__":
    main()
