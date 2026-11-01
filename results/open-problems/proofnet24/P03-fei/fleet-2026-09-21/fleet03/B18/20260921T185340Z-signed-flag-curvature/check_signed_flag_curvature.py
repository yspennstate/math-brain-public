#!/usr/bin/env python3
from fractions import Fraction
import random
import json

def popcount(x):
    return x.bit_count()

def vals_from_truth(n, truth):
    return [1 if ((truth >> x) & 1) else -1 for x in range(1 << n)]

def derivative_row(vals, n, i):
    reps = [x for x in range(1 << n) if ((x >> i) & 1) == 0]
    d = {x: (vals[x] - vals[x ^ (1 << i)]) // 2 for x in reps}
    return reps, d

def walsh_energy(reps, d, n, i):
    N = len(reps)
    others = ((1 << n) - 1) ^ (1 << i)
    out = {}
    U = others
    while True:
        num = sum(d[x] * (-1 if (popcount(U & x) & 1) else 1) for x in reps)
        h = Fraction(num, N)
        out[U] = h * h
        if U == 0:
            break
        U = (U - 1) & others
    return out

def flag_case(vals, n, i, L):
    reps, d = derivative_row(vals, n, i)
    N = len(reps)
    alpha = Fraction(sum(v * v for v in d.values()), N)

    ws = []
    w = L
    while True:
        ws.append(w)
        if w == 0:
            break
        w = (w - 1) & L

    cs = []
    ps = []
    os = []
    for w in ws:
        cnum = pnum = onum = 0
        for x in reps:
            dx, dy = d[x], d[x ^ w]
            cnum += (dx - dy) ** 2
            pnum += abs(dx * dx - dy * dy)
            onum += int(dx != 0 and dy == -dx)
        c = Fraction(cnum, N)
        p = Fraction(pnum, N)
        o = Fraction(onum, N)
        assert c == p + 4 * o
        cs.append(c)
        ps.append(p)
        os.append(o)

    M = len(ws)
    Ec = sum(cs, Fraction(0)) / M
    Ec2 = sum((z * z for z in cs), Fraction(0)) / M
    Ep = sum(ps, Fraction(0)) / M
    Eo = sum(os, Fraction(0)) / M

    energies = walsh_energy(reps, d, n, i)
    A = {}
    for U, mass in energies.items():
        V = U & L
        A[V] = A.get(V, Fraction(0)) + mass
    T = sum((mass for V, mass in A.items() if V), Fraction(0))
    coll = sum((mass * mass for V, mass in A.items() if V), Fraction(0))

    assert Ec == 2 * T
    assert Ec2 == 4 * T * T + 4 * coll
    assert Ec <= 2 * alpha
    assert Eo <= alpha / 2
    assert Ec2 <= 8 * alpha * alpha
    assert Ec2 <= 8 * alpha
    if alpha <= Fraction(1, 2):
        assert Ec2 <= 4 * alpha
    return alpha, Ec, Ec2, Ep, Eo, T, coll

def exhaustive_through_3():
    cases = 0
    max_ratio = Fraction(0)
    sharp = None
    for n in range(1, 4):
        for truth in range(1 << (1 << n)):
            vals = vals_from_truth(n, truth)
            for i in range(n):
                others = ((1 << n) - 1) ^ (1 << i)
                L = others
                while True:
                    alpha, Ec, Ec2, Ep, Eo, T, coll = flag_case(vals, n, i, L)
                    cases += 1
                    if alpha:
                        ratio = Ec2 / alpha
                        if ratio > max_ratio:
                            max_ratio = ratio
                            sharp = {
                                "n": n, "truth": truth, "i": i, "L": L,
                                "alpha": str(alpha), "E_c": str(Ec),
                                "E_c2": str(Ec2), "E_p": str(Ep),
                                "E_o": str(Eo)
                            }
                    if L == 0:
                        break
                    L = (L - 1) & others
    return cases, max_ratio, sharp

def sampled_n4(samples=4096, seed=180340):
    rng = random.Random(seed)
    n = 4
    cases = 0
    max_ratio = Fraction(0)
    for _ in range(samples):
        truth = rng.getrandbits(1 << n)
        vals = vals_from_truth(n, truth)
        for i in range(n):
            others = ((1 << n) - 1) ^ (1 << i)
            L = others
            while True:
                alpha, Ec, Ec2, Ep, Eo, T, coll = flag_case(vals, n, i, L)
                cases += 1
                if alpha:
                    max_ratio = max(max_ratio, Ec2 / alpha)
                if L == 0:
                    break
                L = (L - 1) & others
    return cases, max_ratio

def parity_sharpness():
    rows = []
    for n in range(2, 11):
        # f(x)=(-1)^{sum x_j}; encode +1 on even parity.
        vals = [1 if (popcount(x) % 2 == 0) else -1 for x in range(1 << n)]
        total_alpha = Fraction(0)
        total_Ec2 = Fraction(0)
        # natural order 0<1<...<n-1, later set = {i+1,...,n-1}
        for i in range(n):
            L = sum(1 << j for j in range(i + 1, n))
            alpha, Ec, Ec2, Ep, Eo, T, coll = flag_case(vals, n, i, L)
            total_alpha += alpha
            total_Ec2 += Ec2
            if i < n - 1:
                assert alpha == 1 and Ep == 0 and Eo == Fraction(1, 2)
                assert Ec == 2 and Ec2 == 8
            else:
                assert Ec2 == 0
        rows.append({
            "n": n,
            "I": str(total_alpha),
            "sum_E_c2": str(total_Ec2),
            "ratio_to_I": str(total_Ec2 / total_alpha),
        })
    return rows


def folded_sharp_example():
    # Coordinates a=0, i=1, b=2 with order a < i < b, so L_i={b}.
    # f=1 on a=1; on a=0, f=(-1)^(i+b).
    n = 3
    vals = []
    for x in range(1 << n):
        a = (x >> 0) & 1
        i = (x >> 1) & 1
        b = (x >> 2) & 1
        vals.append(1 if a else (1 if ((i ^ b) == 0) else -1))
    alpha, Ec, Ec2, Ep, Eo, T, coll = flag_case(vals, n, 1, 1 << 2)
    assert alpha == Fraction(1, 2)
    assert Ec == 1
    assert Ec2 == 2
    assert Ep == 0
    assert Eo == Fraction(1, 4)
    return {
        "alpha": str(alpha),
        "E_flag_kappa": str(Ec),
        "E_flag_kappa2": str(Ec2),
        "E_flag_unsigned_p": str(Ep),
        "E_flag_opposite_sign": str(Eo),
        "E_kappa_over_alpha": str(Ec / alpha),
        "E_kappa2_over_alpha": str(Ec2 / alpha),
        "E_opposite_over_alpha": str(Eo / alpha)
    }

def main():
    ecases, emax, sharp = exhaustive_through_3()
    scases, smax = sampled_n4()
    parity = parity_sharpness()
    folded = folded_sharp_example()
    out = {
        "status": "PASS",
        "claim": "signed ordered-flag curvature identity and influence payment",
        "exhaustive_cases_n_le_3": ecases,
        "sampled_n4_cases": scases,
        "sampled_n4_functions": 4096,
        "sample_seed": 180340,
        "max_coordinate_Ec2_over_alpha_exhaustive": str(emax),
        "max_coordinate_Ec2_over_alpha_sample_n4": str(smax),
        "sharp_case": sharp,
        "parity_sharpness": parity,
        "folded_sharp_example": folded,
        "identities_checked": [
            "c_i(w)=p_i(w)+4 o_i(w)",
            "E_flag c_i=2 T_i",
            "E_flag c_i^2=4 T_i^2+4 sum_V A_i(V)^2",
            "E_flag c_i<=2 Inf_i",
            "E_flag o_i<=Inf_i/2",
            "E_flag c_i^2<=8 Inf_i^2<=8 Inf_i",
            "if Inf_i<=1/2 then E_flag c_i^2<=4 Inf_i"
        ]
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
