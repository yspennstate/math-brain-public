#!/usr/bin/env python3
from fractions import Fraction
from math import gcd
import sympy as sp

class CyclotomicRing:
    """Exact arithmetic in Q[x]/Phi_n(x), low-degree coefficients first."""
    def __init__(self, n):
        x = sp.Symbol("x")
        poly = sp.Poly(sp.cyclotomic_poly(n, x), x, domain=sp.ZZ)
        coeff_hi = [int(c) for c in poly.all_coeffs()]
        assert coeff_hi[0] == 1
        self.mod = [Fraction(c) for c in reversed(coeff_hi)]
        self.d = poly.degree()
        self.zero = (Fraction(0),) * self.d
        self.one = (Fraction(1),) + (Fraction(0),) * (self.d - 1)
        self.x = ((Fraction(-self.mod[0]),) if self.d == 1 else
                  (Fraction(0), Fraction(1)) + (Fraction(0),) * (self.d - 2))

    def reduce(self, coeffs):
        a = list(coeffs) + [Fraction(0)] * max(0, self.d - len(coeffs))
        while len(a) > self.d:
            lead = a[-1]
            deg = len(a) - 1
            if lead:
                shift = deg - self.d
                for i in range(self.d):
                    a[shift+i] -= lead * self.mod[i]
            a.pop()
        a += [Fraction(0)] * (self.d - len(a))
        return tuple(a)

    def add(self, a, b):
        return tuple(a[i] + b[i] for i in range(self.d))

    def mul(self, a, b):
        c = [Fraction(0)] * (2*self.d - 1)
        for i, ai in enumerate(a):
            if not ai:
                continue
            for j, bj in enumerate(b):
                if bj:
                    c[i+j] += ai*bj
        return self.reduce(c)

    def pow(self, a, n):
        r, b = self.one, a
        while n:
            if n & 1:
                r = self.mul(r, b)
            n >>= 1
            if n:
                b = self.mul(b, b)
        return r

    def rat(self, value):
        return (Fraction(value),) + (Fraction(0),) * (self.d - 1)

def mat_zero(q, R):
    return [[R.zero for _ in range(q)] for _ in range(q)]

def mat_eye(q, R):
    M = mat_zero(q, R)
    for i in range(q):
        M[i][i] = R.one
    return M

def mat_add(A, B, R):
    q = len(A)
    return [[R.add(A[i][j], B[i][j]) for j in range(q)] for i in range(q)]

def mat_mul(A, B, R):
    q = len(A)
    C = mat_zero(q, R)
    for i in range(q):
        for k in range(q):
            if A[i][k] == R.zero:
                continue
            for j in range(q):
                if B[k][j] != R.zero:
                    C[i][j] = R.add(C[i][j], R.mul(A[i][k], B[k][j]))
    return C

def mat_scale(a, A, R):
    return [[R.mul(a, x) for x in row] for row in A]

def mat_pow(A, n, R):
    q = len(A)
    P = mat_eye(q, R)
    B = A
    while n:
        if n & 1:
            P = mat_mul(P, B, R)
        n >>= 1
        if n:
            B = mat_mul(B, B, R)
    return P

def check_instance(q, p):
    # eta primitive 2q-th root; zeta = eta^(2p) primitive q-th root.
    R = CyclotomicRing(2*q)
    eta = R.x
    zeta = R.pow(eta, 2*p)

    U = mat_zero(q, R)
    for k in range(q):
        U[k][k] = R.pow(zeta, k)

    S = mat_zero(q, R)
    for k in range(q):
        S[(k-1) % q][k] = R.one
    V = mat_scale(eta, S, R)
    I = mat_eye(q, R)

    # Both sides of (U+tV)^q = (1-t^q)I have degree at most q in t.
    # Exact agreement at q+1 distinct rational t values certifies the
    # polynomial identity for this finite (p,q) instance.
    t_values = [Fraction(k, q+2) for k in range(q+1)]
    for t in t_values:
        A = mat_add(U, mat_scale(R.rat(t), V, R), R)
        lhs = mat_pow(A, q, R)
        rhs = mat_scale(R.rat(1 - t**q), I, R)
        assert lhs == rhs, (q, p, t)
    return len(t_values)

instances = 0
evaluations = 0
for q in range(2, 11):
    for p in range(1, q):
        if gcd(p, q) == 1:
            n = check_instance(q, p)
            instances += 1
            evaluations += n
            print(f"q={q:2d} p={p:2d} q+1={n:2d} EXACT_PARAMETER_EVALS PASS")

print(f"TOTAL_EXACT_INSTANCES={instances}")
print(f"TOTAL_EXACT_PARAMETER_EVALUATIONS={evaluations}")
print("ALL_PARAMETER_POWER_IDENTITIES_PASS")
