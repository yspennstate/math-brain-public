#!/usr/bin/env python3
"""Exact orbit-energy check for a changing-overlap counterfamily.

The finite identities use Fraction Walsh arithmetic.  Logarithms are used
only to print the potential values after the rational identities are known.
"""
from fractions import Fraction
from math import comb, log, log2


def fwht(values):
    a = [Fraction(v) for v in values]
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2*h):
            for k in range(j, j+h):
                x, y = a[k], a[k+h]
                a[k], a[k+h] = x+y, x-y
        h *= 2
    return [x/len(a) for x in a]


def q(t):
    t = float(t)
    if t == 0:
        return 0.0
    return t*log2(1/t)+2*t/log(2)


def psi(k, t):
    if k == 0:
        return 0.0
    return q(t)+float(t)*log2(k)


def orbit_energy(p, X, base):
    out = Fraction(0)
    sub = X
    a = sub
    # Iterate all A subset X by descending submasks.
    while True:
        out += p[base | a]
        if a == 0:
            break
        a = (a-1) & sub
    return out


def lambda_tilde(values, X):
    n = len(values).bit_length()-1
    p = [a*a for a in fwht(values)]
    k = X.bit_count()
    empty = orbit_energy(p, X, 0)
    private = []
    for i in range(n):
        if not X & (1 << i):
            private.append(orbit_energy(p, X, 1 << i))
    return psi(k, empty)+sum(q(t) for t in private), empty, private, p


def majority(bits):
    return 1 if sum(bits) > 0 else -1


def family(m):
    # Coordinates: y=0, x=1, z=2, u_j=3+j.
    n = m+3
    out = []
    for s in range(1 << n):
        vals = [1 if s & (1 << i) else -1 for i in range(n)]
        y, x, z = vals[:3]
        M = majority(vals[3:])
        out.append(x if y == 1 else z*M)
    return tuple(out)


def influence(p, i):
    return sum(a for s, a in enumerate(p) if s & (1 << i))


def main():
    direct = 0
    for m in (1, 3, 5, 7, 9):
        f = family(m)
        X = (1 << 0) | (1 << 1)  # {y,x}
        Y = (1 << 0) | (1 << 2)  # {y,z}
        LX, eX, privX, p = lambda_tilde(f, X)
        LY, eY, privY, _ = lambda_tilde(f, Y)
        a = Fraction(comb(m-1, (m-1)//2), 2**(m-1))
        assert eX == Fraction(1, 2)
        assert all(t == 0 for t in privX)
        assert eY == 0
        # Y-private order is x,u_0,...,u_{m-1}.
        assert privY[0] == Fraction(1, 2)
        assert all(t == a*a/2 for t in privY[1:])
        assert influence(p, 1) == Fraction(1, 2)
        assert influence(p, 2) == Fraction(1, 2)
        assert abs(LX-psi(2, Fraction(1, 2))) < 1e-13
        assert abs(LY-(q(Fraction(1, 2))+m*q(a*a/2))) < 1e-13
        direct += 1

    rows = []
    for m in (11, 51, 101, 501, 1001, 2001):
        a = Fraction(comb(m-1, (m-1)//2), 2**(m-1))
        gap = m*q(a*a/2)-Fraction(1, 2)
        normalized = gap/log2(m)
        rows.append((m, float(a*a), gap, normalized))

    print("status=PASS")
    print(f"direct_fraction_walsh_cases={direct}")
    print("blocks=X:{y,x};Y:{y,z}")
    print(f"Lambda_X_exact_form=psi_2(1/2)={psi(2,Fraction(1,2)):.15f}")
    print("Lambda_Y_exact_form=q(1/2)+m*q(a_m^2/2)")
    print("Inf_x=1/2")
    print("Inf_z=1/2")
    print("gap_exact_form=m*q(a_m^2/2)-1/2")
    print(f"predicted_log2_coefficient=1/pi={1/3.141592653589793:.15f}")
    for m, a2, gap, normalized in rows:
        print(f"m={m} a_m_squared={a2:.15e} gap={gap:.15f} gap_over_log2m={normalized:.15f}")


if __name__ == "__main__":
    main()
