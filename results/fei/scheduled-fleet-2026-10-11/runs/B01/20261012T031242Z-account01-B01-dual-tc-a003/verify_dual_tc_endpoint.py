#!/usr/bin/env python3
"""Finite audit of the A003 dual-total-correlation endpoint.

The all-dimensional claim is analytic.  This checker independently rebuilds
truth tables, Walsh spectra, physical restrictions, the conditional spectral
entropies E_i, and the Jensen--Shannon remainders J_i=Delta_i H-E_i.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache
from itertools import product

getcontext().prec = 80
D = Decimal
LN2 = D(2).ln()
C = D(2) / LN2
TOL = D("1e-60")


def fwht(values):
    a = list(values)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def qdec(q):
    return D(q.numerator) / D(q.denominator)


@lru_cache(None)
def entropy_from_weights(weights):
    total = sum(weights)
    ans = D(0)
    for w in weights:
        if w:
            p = D(w) / D(total)
            ans -= p * (p.ln() / LN2)
    return ans


def restrict_table(table, n, coord, bit):
    out = []
    lowmask = (1 << coord) - 1
    for y in range(1 << (n-1)):
        x = (y & lowmask) | (bit << coord) | ((y >> coord) << (coord+1))
        out.append(table[x])
    return tuple(out)


def spectral_data(table, n):
    N = 1 << n
    w = fwht(table)
    weights = tuple(v*v for v in w)
    assert sum(weights) == N*N
    H = entropy_from_weights(weights)
    alphas = []
    Es = []
    for i in range(n):
        num = sum(weights[m] for m in range(N) if (m >> i) & 1)
        alpha = Fraction(num, N*N)
        alphas.append(alpha)
        aggregated = [0]*(N//2)
        lowmask = (1 << i) - 1
        for m, wt in enumerate(weights):
            reduced = (m & lowmask) | ((m >> (i+1)) << i)
            aggregated[reduced] += wt
        Es.append(H - entropy_from_weights(tuple(aggregated)))
    return H, alphas, Es


def analyze(table, n):
    H, alphas, Es = spectral_data(table, n)
    I = sum((qdec(a) for a in alphas), D(0))
    if I == 0:
        return None
    R = H/I
    deltas, Js = [], []
    for i in range(n):
        hp = entropy_from_weights(tuple(v*v for v in fwht(restrict_table(table,n,i,0))))
        hm = entropy_from_weights(tuple(v*v for v in fwht(restrict_table(table,n,i,1))))
        delta = H - (hp+hm)/2
        J = delta - Es[i]
        assert J >= -TOL
        cap = C * min(qdec(alphas[i]), D(1)-qdec(alphas[i]))
        assert J <= cap + TOL
        deltas.append(delta)
        Js.append(J)
    B = H - sum(Es, D(0))
    assert B >= -TOL
    # Chain-rule identity definition of DTC and restriction-critical payment.
    critical = all(deltas[i] + TOL >= R*qdec(alphas[i])
                   for i in range(n) if alphas[i] > 0)
    if critical:
        assert B <= sum(Js, D(0)) + TOL
        assert B <= C*I + TOL
        if H > 0:
            assert B/H <= C/R + TOL
    return H, I, R, B, sum(Js,D(0)), critical


def sign_table(mask, n):
    return tuple(1 if (mask >> x) & 1 else -1 for x in range(1 << n))


def point_defect(n):
    return tuple(1 if x == 0 else -1 for x in range(1 << n))


def parity(n):
    return tuple(1 if x.bit_count() % 2 == 0 else -1 for x in range(1 << n))


def majority3():
    return tuple(1 if x.bit_count() >= 2 else -1 for x in range(8))


def addressing(a):
    n = a + (1 << a)
    out = []
    for x in range(1 << n):
        address = x & ((1 << a)-1)
        bit = (x >> (a+address)) & 1
        out.append(1 if bit else -1)
    return tuple(out), n


def tensor(f, g):
    return tuple(u*v for v in g for u in f)


def main():
    checks = 0
    critical_count = 0
    max_ratio = (D(0), None)

    # Exhaustive genuine Boolean functions through dimension three.
    for n in range(1, 4):
        for mask in range(1, (1 << (1 << n))-1):
            ans = analyze(sign_table(mask,n),n)
            checks += 1
            if ans[-1]: critical_count += 1
            if ans[2] > max_ratio[0]: max_ratio = (ans[2], ("exhaustive",n,mask,ans))

    # Deterministic n=4 coverage, with no pseudorandom seed.
    seen = set()
    modulus = 1 << 16
    for k in range(4096):
        mask = ((40503*k + 97) ^ (k*k*257) ^ (k << (k % 7))) & (modulus-1)
        if mask in (0,modulus-1) or mask in seen:
            continue
        seen.add(mask)
        ans = analyze(sign_table(mask,4),4)
        checks += 1
        if ans[-1]: critical_count += 1
        if ans[2] > max_ratio[0]: max_ratio = (ans[2], ("n4",4,mask,ans))

    # Mandatory controls: sparse defects, parity, addressing, prime gate,
    # exact tensors, and a one-point near-tensor surgery.
    controls = []
    for n in range(1, 11): controls.append((f"q{n}", point_defect(n), n))
    for n in range(1, 9): controls.append((f"parity{n}", parity(n), n))
    controls.append(("majority3", majority3(), 3))
    for a in (1,2):
        tab,n = addressing(a); controls.append((f"address{a}",tab,n))
    and2 = point_defect(2)
    product_gate = tensor(and2, majority3())
    controls.append(("tensor_and2_maj3", product_gate, 5))
    surg = list(product_gate); surg[0] *= -1
    controls.append(("near_tensor_one_flip", tuple(surg), 5))
    for name,tab,n in controls:
        ans = analyze(tab,n)
        if ans is not None:
            checks += 1
            if ans[-1]: critical_count += 1
            if ans[2] > max_ratio[0]: max_ratio = (ans[2], (name,n,None,ans))

    # Direct DTC additivity under disjoint products for all nonconstant
    # functions through two variables.
    small=[]
    for n in (1,2):
        for mask in range(1,(1 << (1 << n))-1):
            small.append((sign_table(mask,n),n))
    tensor_checks=0
    for f,n in small:
        af=analyze(f,n)
        for g,m in small:
            ag=analyze(g,m)
            at=analyze(tensor(f,g),n+m)
            assert abs(at[0]-(af[0]+ag[0])) < TOL
            assert abs(at[1]-(af[1]+ag[1])) < TOL
            assert abs(at[3]-(af[3]+ag[3])) < TOL
            tensor_checks += 1

    print("PASS")
    print(f"function_checks={checks}")
    print(f"critical_functions={critical_count}")
    print(f"n4_unique_nonconstant={len(seen)}")
    print(f"explicit_controls={len(controls)}")
    print(f"tensor_additivity_checks={tensor_checks}")
    print("randomness=NONE")
    print("arithmetic=exact integer Walsh/Fraction marginals; Decimal(80) entropy")
    print(f"largest_ratio={max_ratio[0]}")
    print(f"largest_case={max_ratio[1][:3]}")


if __name__ == "__main__":
    main()
