from __future__ import annotations

import itertools
import math
from collections import Counter

TOL = 1e-10


def fwht(values):
    a = [float(v) for v in values]
    h = 1
    n = len(a)
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]


def influence(f, n, i):
    mask = 1 << i
    return sum(1 for x in range(1 << n) if f[x] != f[x ^ mask]) / (1 << n)


def fold(f, n):
    R = 0
    for i in range(n):
        if influence(f, n, i) > 0.5:
            R |= 1 << i
    g = []
    for x, v in enumerate(f):
        g.append(-v if ((x & R).bit_count() & 1) else v)
    return g, [influence(g, n, i) for i in range(n)]


def derivative_row(f, n, i):
    others = [k for k in range(n) if k != i]
    row = []
    for y in range(1 << (n-1)):
        x0 = 0
        for pos, k in enumerate(others):
            if (y >> pos) & 1:
                x0 |= 1 << k
        x1 = x0 | (1 << i)
        row.append((f[x0] - f[x1]) // 2)
    return row, others


def row_depth(row):
    m = (len(row)).bit_length() - 1
    d = 0.0
    N = len(row)
    for pos in range(m):
        mask = 1 << pos
        d += sum(((row[y] - row[y ^ mask]) / 2.0) ** 2 for y in range(N)) / N
    return d


def exact_subcube(row, others):
    supp = [y for y, v in enumerate(row) if v]
    if not supp:
        return None
    signs = {1 if row[y] > 0 else -1 for y in supp}
    if len(signs) != 1:
        return None
    fixed, pattern = set(), {}
    for pos, k in enumerate(others):
        bits = {(y >> pos) & 1 for y in supp}
        if len(bits) == 1:
            fixed.add(k)
            pattern[k] = next(iter(bits))
    expected = set()
    for y in range(len(row)):
        ok = True
        for pos, k in enumerate(others):
            if k in fixed and ((y >> pos) & 1) != pattern[k]:
                ok = False
                break
        if ok:
            expected.add(y)
    if expected != set(supp):
        return None
    return fixed, pattern, next(iter(signs))


def spectrum_entropy(f, n):
    coeff = fwht(f)
    p = [a*a for a in coeff]
    H = sum(-q * math.log2(q) for q in p if q > TOL)
    return H, p


def analyze(f, n):
    f, infl = fold(f, n)
    data = {}
    Z = set()
    for i, j in enumerate(infl):
        if j <= TOL:
            continue
        row, others = derivative_row(f, n, i)
        d = row_depth(row)
        delta = d/j - 0.5*math.log2(1.0/j)
        info = exact_subcube(row, others)
        if abs(delta) <= TOL:
            assert info is not None
            Z.add(i)
        data[i] = {"j": j, "d": d, "delta": delta, "info": info}
    E = set(data) - Z

    # Components of the zero-defect graph i~k iff k is a fixed support coordinate of row i.
    un = set(Z)
    components = []
    while un:
        s = un.pop()
        C = {s}
        stack = [s]
        while stack:
            i = stack.pop()
            Fi = data[i]["info"][0]
            for k in list(un):
                if k in Fi:
                    un.remove(k)
                    C.add(k)
                    stack.append(k)
        components.append(C)

    gates = []
    for C in components:
        if len(C) > 1:
            closed = [{i} | data[i]["info"][0] for i in C]
            assert all(N == closed[0] for N in closed)
            N = closed[0]
            T = N - C
            assert T <= E
            common = {}
            for i in C:
                patt = data[i]["info"][1]
                for k, bit in patt.items():
                    if k in common:
                        assert common[k] == bit
                    common[k] = bit
            tpatt = {k: common[k] for k in T}
        else:
            i = next(iter(C))
            T = set(data[i]["info"][0])
            assert T <= E
            tpatt = {k: data[i]["info"][1][k] for k in T}
        gates.append((C, T, tpatt))

    # Distinct zero components have incompatible gates.
    for a in range(len(gates)):
        for b in range(a+1, len(gates)):
            _, T1, p1 = gates[a]
            _, T2, p2 = gates[b]
            compatible = all(p1[k] == p2[k] for k in T1 & T2)
            assert not compatible

    H, p = spectrum_entropy(f, n)
    HZ = 0.0
    for S, q in enumerate(p):
        if q > TOL and any((S >> i) & 1 for i in Z):
            HZ -= q * math.log2(q)

    formula = 0.0
    JZ = 0.0
    gate_bank = 0.0
    for C, T, _ in gates:
        r, t = len(C), len(T)
        js = [data[i]["j"] for i in C]
        assert max(js) - min(js) <= TOL
        j = js[0]
        JC = r*j
        JZ += JC
        gate_bank += JC*t
        w = (2.0/r) * (1.0 - 2.0**(-r)) * JC
        formula += w * 2.0 * (t+r-1)
    assert abs(HZ-formula) <= 5e-9

    DE = sum(data[k]["d"] for k in E)
    assert gate_bank <= 2.0*DE + 5e-9
    assert HZ <= 4.0*JZ + 4.0*DE + 5e-9
    return H, HZ, JZ, DE, len(Z), len(E)


def product(f, n, g, m):
    out = []
    for y in range(1 << m):
        for x in range(1 << n):
            out.append(f[x] * g[y])
    return out


def tensor_defects(f, n, g, m):
    F = product(f, n, g, m)
    ff, inf_f = fold(f, n)
    gg, inf_g = fold(g, m)
    FF, inf_F = fold(F, n+m)
    If = sum(inf_f)
    Ig = sum(inf_g)
    # Product of already folded factors is equal to folded product up to a character/sign;
    # defect values are invariant under this coordinate-wise fold.
    for i in range(n):
        if inf_f[i] <= TOL:
            continue
        row, _ = derivative_row(ff, n, i)
        d = row_depth(row)
        df = d/inf_f[i] - 0.5*math.log2(1.0/inf_f[i])
        rowF, _ = derivative_row(FF, n+m, i)
        dF = row_depth(rowF)
        dprod = dF/inf_F[i] - 0.5*math.log2(1.0/inf_F[i])
        assert abs(dprod - (df + Ig)) <= 5e-9
    for j in range(m):
        if inf_g[j] <= TOL:
            continue
        row, _ = derivative_row(gg, m, j)
        d = row_depth(row)
        dg = d/inf_g[j] - 0.5*math.log2(1.0/inf_g[j])
        idx = n+j
        rowF, _ = derivative_row(FF, n+m, idx)
        dF = row_depth(rowF)
        dprod = dF/inf_F[idx] - 0.5*math.log2(1.0/inf_F[idx])
        assert abs(dprod - (dg + If)) <= 5e-9


def main():
    total = 0
    zero_cases = 0
    max_gap = -1e99
    by_shape = Counter()
    for n in range(1, 5):
        N = 1 << n
        for bits in range(1 << (N-1)):
            f = [1] + [1 if ((bits >> (x-1)) & 1) else -1 for x in range(1, N)]
            H, HZ, JZ, DE, z, e = analyze(f, n)
            total += 1
            if z:
                zero_cases += 1
                by_shape[(n, z, e)] += 1
                max_gap = max(max_gap, HZ - (4*JZ + 4*DE))
    # Tensor identity checks on representative nonconstant factors.
    and2 = [1, 1, 1, -1]
    maj3 = []
    for x in range(8):
        ones = x.bit_count()
        maj3.append(1 if ones <= 1 else -1)
    onepoint3 = [-1] + [1]*7
    tensor_defects(and2, 2, maj3, 3)
    tensor_defects(and2, 2, onepoint3, 3)
    tensor_defects(maj3, 3, onepoint3, 3)
    print("PASS")
    print("boolean_functions_checked", total)
    print("functions_with_zero_defect_rows", zero_cases)
    print("max_entropy_bound_excess", f"{max_gap:.3e}")
    print("tensor_product_identity_pairs", 3)
    print("zero_row_shape_counts")
    for key in sorted(by_shape):
        print(key, by_shape[key])


if __name__ == "__main__":
    main()
