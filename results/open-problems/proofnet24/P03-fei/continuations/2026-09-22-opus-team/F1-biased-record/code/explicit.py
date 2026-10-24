"""Explicit compositions of g, AND, OR, NOT on fresh variables, evaluated exactly by the composition identity:
for F = G(f_1, ..., f_k) with independent inputs,
    Pr[F] from the biased spectrum,  I(F) = sum_i (It_i/V_i) I(f_i),  H(F) = Htilde_G + sum_i (It_i/V_i)(H(f_i) - h(V_i)).
A function is a record (p, I, H).  Moves used by the policy of the value iteration:
    A(F): g with all nine core inputs fed by copies of F, auxiliaries by fresh variables;
    B(F): g with core input 0 fed by F, all other inputs fresh variables;
    P(F): g with auxiliary 9 fed by F and auxiliary 10 by NOT F (exactly balanced for every F).
Reports s_C(F) = C I - H and, for balanced F, H/(I - 1) against the record.
"""
import math
import numpy as np
import fast_gate as FG

CREC = 6.521845710923046575
VAR = (0.5, 1.0, 0.0)


def h2(v):
    if v <= 0.0 or v >= 1.0:
        return 0.0
    return -v * math.log2(v) - (1 - v) * math.log2(1 - v)


def gate_g(inputs):
    """inputs: list of 18 records (p, I, H)."""
    p = np.array([f[0] for f in inputs])
    Ht, It, po, c = FG.evaluate(p)
    I = 0.0; H = Ht
    for i, (pi, Ii, Hi) in enumerate(inputs):
        V = 4 * pi * (1 - pi)
        w = It[i] / V
        I += w * Ii
        H += w * (Hi - h2(V))
    return (po, I, H)


def NOT(f):
    return (1 - f[0], f[1], f[2])


def AND(a, b):
    p, q = a[0], b[0]
    Vp, Vq = 4 * p * (1 - p), 4 * q * (1 - q)
    Ita, Itb = q * Vp, p * Vq
    w0 = (1 - 2 * p * q) ** 2; wab = w0 + Ita + Itb - 1
    ws = [w0, Ita - wab, Itb - wab, wab]
    Ht = sum(-w * math.log2(w) for w in ws if w > 0)
    I = q * a[1] + p * b[1]
    H = Ht + q * (a[2] - h2(Vp)) + p * (b[2] - h2(Vq))
    return (p * q, I, H)


def OR(a, b):
    return NOT(AND(NOT(a), NOT(b)))


def A(F):
    return gate_g([F] * 9 + [VAR] * 9)


def B(F):
    return gate_g([F] + [VAR] * 17)


def P(F):
    return gate_g([VAR] * 9 + [F, NOT(F)] + [VAR] * 7)


def slack(F, C=CREC):
    return C * F[1] - F[2]


if __name__ == "__main__":
    # sanity: g on variables, and AND/OR identities
    g0 = gate_g([VAR] * 18)
    print("g: p=%.6f I=%.10f H=%.12f ratio=%.15f" % (g0[0], g0[1], g0[2], g0[2] / (g0[1] - 1)))
    x = VAR
    print("AND(x,y):", AND(x, x), " OR(x,AND(y,z)):", OR(x, AND(x, x)))
