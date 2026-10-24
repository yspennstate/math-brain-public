#!/usr/bin/env python3
"""
Finite-field check of the two-trace counting lemma used in HARD8-06.

For p odd and x in F_{p^2} with x^(p+1)=1, x != +/-1, put t=x+x^{-1} in F_p.
Let
    S_d(x) = {sum_{j=0}^d eps_j x^j : eps_j in {0,1}}
and let C_0=2, C_1=t, C_{j+1}=t C_j-C_{j-1}, with
    T_d(t) = {sum_{j=0}^d eps_j C_j(t) : eps_j in {0,1}}.
Then
    |T_d(t)| <= |S_d(x)| <= |T_{d+1}(t)|^2.

The proof is exact: Frobenius sends x to x^{-1}; the map
Y -> (Tr(Y), Tr(xY)) is F_p-linear and injective when x != +/-1.

This script checks the inequalities by exhaustive subset-sum enumeration in F_101^2.
"""

p = 101
nu = 2  # nonsquare mod 101


def invmod(a):
    return pow(a % p, p - 2, p)


class Fp2:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a = a % p
        self.b = b % p
    def __add__(self, other):
        return Fp2(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return Fp2(self.a - other.a, self.b - other.b)
    def __neg__(self):
        return Fp2(-self.a, -self.b)
    def __mul__(self, other):
        return Fp2(self.a*other.a + nu*self.b*other.b,
                   self.a*other.b + self.b*other.a)
    def conj(self):
        return Fp2(self.a, -self.b)
    def norm(self):
        return (self.a*self.a - nu*self.b*self.b) % p
    def inv(self):
        n = invmod(self.norm())
        c = self.conj()
        return Fp2(c.a*n, c.b*n)
    def __truediv__(self, other):
        return self * other.inv()
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    def __hash__(self):
        return hash((self.a, self.b))
    def __repr__(self):
        return f"({self.a}+{self.b}u)"


def subset_sums(values, zero):
    out = {zero}
    for v in values:
        out |= {z + v for z in list(out)}
    return out


def main():
    one = Fp2(1, 0)
    u = Fp2(0, 1)
    g = one + u
    x = g / g.conj()  # norm-one
    assert x.norm() == 1
    assert x != one and x != -one
    assert x.conj() == x.inv()

    t2 = x + x.inv()
    assert t2.b == 0
    t = t2.a

    powers = [one]
    for _ in range(12):
        powers.append(powers[-1] * x)

    C = [2 % p, t]
    for _ in range(2, 14):
        C.append((t*C[-1] - C[-2]) % p)

    for j in range(13):
        tr = powers[j] + powers[j].conj()
        assert tr.b == 0 and tr.a == C[j]

    print("p =", p, "nu =", nu, "x =", x, "t =", t)
    print("d  |T_d|  |S_d|  |T_{d+1}|^2")
    for d in range(1, 9):
        Sd = subset_sums(powers[:d+1], Fp2(0, 0))
        Td = subset_sums(C[:d+1], 0)
        Tnext = subset_sums(C[:d+2], 0)

        seen = set()
        for Y in Sd:
            trY = Y + Y.conj()
            xY = x * Y
            trxY = xY + xY.conj()
            key = (trY.a, trxY.a)
            assert key not in seen
            seen.add(key)

        assert len(Td) <= len(Sd) <= len(Tnext)**2
        print(f"{d:1d} {len(Td):6d} {len(Sd):6d} {len(Tnext)**2:12d}")

    print("All finite-field assertions passed.")


if __name__ == "__main__":
    main()
