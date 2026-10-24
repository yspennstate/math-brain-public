from itertools import combinations, product
from fractions import Fraction
from math import log2


def balanced_tables(n):
    N = 1 << n
    out = []
    for pos in combinations(range(N), N // 2):
        s = set(pos)
        out.append(tuple(1 if i in s else -1 for i in range(N)))
    return out


def fwht_int(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def spectral(vals):
    N = len(vals)
    return [Fraction(x * x, N * N) for x in fwht_int(vals)]


def HI(vals):
    H = 0.0
    I = Fraction(0, 1)
    for mask, q in enumerate(spectral(vals)):
        if q:
            x = float(q)
            H += -x * log2(x)
            I += mask.bit_count() * q
    return H, I


def influence_inputs(vals):
    n = (len(vals)).bit_length() - 1
    N = len(vals)
    ans = []
    for j in range(n):
        bit = 1 << j
        c = 0
        for x in range(N):
            if not (x & bit) and vals[x] != vals[x | bit]:
                c += 1
        ans.append(Fraction(c, N // 2))
    return ans


def compose3(outer, inners):
    # outer arity 3; each inner arity 3, disjoint blocks -> 9 variables
    out = []
    for x in range(1 << 9):
        idx = 0
        for i, h in enumerate(inners):
            local = (x >> (3 * i)) & 7
            if h[local] == 1:
                idx |= 1 << i
        out.append(outer[idx])
    return tuple(out)


def key_HI(v):
    H, I = HI(v)
    return round(H, 12), I


def main():
    balanced3 = balanced_tables(3)
    reps = {}
    for h in balanced3:
        reps.setdefault(key_HI(h), h)
    inners = list(reps.values())
    H_in, I_in = [], []
    for h in inners:
        H, I = HI(h)
        H_in.append(H)
        I_in.append(I)

    total = 0
    max_H_err = 0.0
    max_I_err = Fraction(0, 1)
    max_D_err = Fraction(0, 1)
    max_margin_err = 0.0
    C0 = 6.4548

    for G in balanced3:
        HG, IG = HI(G)
        a = influence_inputs(G)
        DG = IG - 1
        for inds in product(range(len(inners)), repeat=3):
            hs = [inners[t] for t in inds]
            F = compose3(G, hs)
            HF, IF = HI(F)
            Hrhs = HG + sum(float(a[i]) * H_in[inds[i]] for i in range(3))
            Irhs = sum(a[i] * I_in[inds[i]] for i in range(3))
            Drhs = DG + sum(a[i] * (I_in[inds[i]] - 1) for i in range(3))
            Herr = abs(HF - Hrhs)
            Ierr = abs(IF - Irhs)
            Derr = abs((IF - 1) - Drhs)
            MF = HF - C0 * float(IF - 1)
            Mrhs = (HG - C0 * float(DG)) + sum(
                float(a[i]) * (H_in[inds[i]] - C0 * float(I_in[inds[i]] - 1))
                for i in range(3)
            )
            Merr = abs(MF - Mrhs)
            max_H_err = max(max_H_err, Herr)
            max_I_err = max(max_I_err, Ierr)
            max_D_err = max(max_D_err, Derr)
            max_margin_err = max(max_margin_err, Merr)
            if Ierr or Derr or Herr > 2e-12 or Merr > 3e-12:
                raise AssertionError((inds, Herr, Ierr, Derr, Merr))
            total += 1

    print("status=PASS")
    print("balanced_outer_arity3=", len(balanced3))
    print("inner_representatives=", len(inners))
    print("inner_HI_types=", sorted((str(I), format(H, ".12g")) for H, I in zip(H_in, I_in)))
    print("heterogeneous_compositions_checked=", total)
    print("max_entropy_identity_abs_error=", format(max_H_err, ".18g"))
    print("max_influence_identity_exact_error=", max_I_err)
    print("max_defect_identity_exact_error=", max_D_err)
    print("max_margin_identity_abs_error=", format(max_margin_err, ".18g"))


if __name__ == "__main__":
    main()
