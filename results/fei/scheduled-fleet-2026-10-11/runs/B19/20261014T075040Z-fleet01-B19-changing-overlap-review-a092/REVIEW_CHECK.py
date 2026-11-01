#!/usr/bin/env python3
"""Independent reconstruction of the changing-overlap counterfamily.

This implementation was written from the displayed Boolean function and
does not import or execute the producer checker.
"""
from fractions import Fraction
from math import comb, log, log2, pi


def fwht(values):
    a = [Fraction(v) for v in values]
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2*h):
            for k in range(j, j+h):
                u, v = a[k], a[k+h]
                a[k], a[k+h] = u+v, u-v
        h *= 2
    return [u/len(a) for u in a]


def q(t):
    t = float(t)
    return 0.0 if t == 0 else t*log2(1/t)+2*t/log(2)


def psi(k, t):
    return 0.0 if k == 0 else q(t)+float(t)*log2(k)


def orbit(p, block, base):
    ans = Fraction(0)
    a = block
    while True:
        ans += p[base | a]
        if a == 0:
            return ans
        a = (a-1) & block


def potential(values, block):
    p = [u*u for u in fwht(values)]
    n = len(values).bit_length()-1
    e0 = orbit(p, block, 0)
    singles = [orbit(p, block, 1 << i)
               for i in range(n) if not block & (1 << i)]
    return psi(block.bit_count(), e0)+sum(q(t) for t in singles), e0, singles, p


def influence(p, i):
    return sum(u for s, u in enumerate(p) if s & (1 << i))


def family(m):
    # Variable order y,x,z,u_1,...,u_m.
    n = m+3
    ans = []
    for s in range(1 << n):
        v = [1 if s & (1 << i) else -1 for i in range(n)]
        y, x, z = v[:3]
        maj = 1 if sum(v[3:]) > 0 else -1
        ans.append(x if y == 1 else z*maj)
    return tuple(ans)


def main():
    X = (1 << 0) | (1 << 1)  # {y,x}
    Y = (1 << 0) | (1 << 2)  # {y,z}
    cases = identities = 0
    for m in (1, 3, 5, 7, 9):
        f = family(m)
        LX, eX, sX, p = potential(f, X)
        LY, eY, sY, _ = potential(f, Y)
        a = Fraction(comb(m-1, (m-1)//2), 2**(m-1))
        checks = [
            eX == Fraction(1, 2),
            all(u == 0 for u in sX),
            eY == 0,
            sY[0] == Fraction(1, 2),
            all(u == a*a/2 for u in sY[1:]),
            influence(p, 0) == Fraction(1, 2),
            influence(p, 1) == Fraction(1, 2),
            influence(p, 2) == Fraction(1, 2),
            abs((LY-LX)-(m*q(a*a/2)-0.5)) < 1e-13,
        ]
        assert all(checks)
        cases += 1
        identities += len(checks)

    rows = []
    for m in (11, 101, 1001, 10001):
        a = Fraction(comb(m-1, (m-1)//2), 2**(m-1))
        gap = m*q(a*a/2)-0.5
        # Total influence of odd majority is m*a.
        total_I = 1.5+0.5*m*float(a)
        rows.append((m, gap, gap/log2(m), total_I))

    print("status=PASS")
    print(f"independent_direct_cases={cases}")
    print(f"exact_rational_identities={identities}")
    print("Inf_y=Inf_x=Inf_z=1/2")
    print("union_block_influence_sum=3/2")
    print("potential_gap=m*q(a_m^2/2)-1/2")
    print(f"asymptotic_log_coefficient=1/pi={1/pi:.15f}")
    for m, gap, ratio, total_I in rows:
        print(f"m={m} gap={gap:.15f} gap_over_log2m={ratio:.15f} I_f={total_I:.15f}")


if __name__ == "__main__":
    main()
