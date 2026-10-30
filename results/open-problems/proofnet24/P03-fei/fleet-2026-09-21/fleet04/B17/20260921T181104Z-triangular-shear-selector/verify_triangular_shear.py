#!/usr/bin/env python3
"""Exact/finite checks for B17 triangular-shear FEI mechanism.

All Walsh transforms and influence identities are integer/rational.
Floating point is used only to evaluate Shannon entropy after exact
Fourier-square masses are known.
"""
from fractions import Fraction
from math import log2


def fwht(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def hi(vals, n):
    W = fwht(vals)
    N = 1 << n
    den = N*N
    masses = [w*w for w in W]
    H = 0.0
    I_num = 0
    for s, num in enumerate(masses):
        if num:
            p = num/den
            H -= p*log2(p)
        I_num += num*s.bit_count()
    return H, Fraction(I_num, den), W, masses


def shear(vals, n, pivot, qbits):
    out = [0]*(1<<n)
    for z in range(1<<n):
        phi = 1
        for b in qbits:
            phi &= (z >> b) & 1
        out[z] = vals[z ^ (phi << pivot)]
    return out


def exhaustive_rank2_shear_n4():
    n, pivot = 4, 3
    checked = 0
    max_tax_ratio = -1.0
    max_tax_mask = None
    for mask in range(1 << 15):  # global sign normalized: f(0)=+1
        vals = [1] + [1 if ((mask >> (i-1)) & 1) == 0 else -1 for i in range(1, 16)]
        g = shear(vals, n, pivot, (0,1))
        Hf, If, Wf, mf = hi(vals, n)
        Hg, Ig, Wg, mg = hi(g, n)

        # Exact restriction block identities.
        f0 = vals[:8]
        f1 = vals[8:]
        a = [(u+v)//2 for u,v in zip(f0,f1)]
        b = [(u-v)//2 for u,v in zip(f0,f1)]
        hphase = [(-1 if ((x&1) and (x&2)) else 1) for x in range(8)]
        hb = [u*v for u,v in zip(hphase,b)]
        Wa, Wb, Whb = fwht(a), fwht(b), fwht(hb)
        assert all(Wf[s] == 2*Wa[s] for s in range(8))
        assert all(Wf[s|8] == 2*Wb[s] for s in range(8))
        assert all(Wg[s] == 2*Wa[s] for s in range(8))
        assert all(Wg[s|8] == 2*Whb[s] for s in range(8))

        # Exact pivot mass p = Inf_y(f).
        disagree = sum(u != v for u,v in zip(f0,f1))
        p = Fraction(disagree, 8)
        p_fourier = Fraction(sum(mf[s] for s in range(8,16)), 256)
        assert p == p_fourier

        # Exact total-influence block formula.
        Ia = Fraction(sum((Wa[s]*Wa[s])*s.bit_count() for s in range(8)), 64)
        Ib = Fraction(sum((Wb[s]*Wb[s])*s.bit_count() for s in range(8)), 64)
        Ihb = Fraction(sum((Whb[s]*Whb[s])*s.bit_count() for s in range(8)), 64)
        assert If == Ia + Ib + p
        assert Ig == Ia + Ihb + p

        # Rank-2 quadratic phase entropy tax: |Delta H| <= 2 p.
        if p:
            ratio = abs(Hf-Hg) / (2*float(p))
            assert ratio <= 1.0 + 1e-12
            if ratio > max_tax_ratio:
                max_tax_ratio, max_tax_mask = ratio, mask
        else:
            assert abs(Hf-Hg) < 1e-12
        checked += 1

    # Exact interior counterexample to any descent rule Delta H <= K Delta I.
    vals = [1,1,1,-1,1,-1,-1,1,-1,1,1,1,1,1,1,1]
    g = shear(vals, 4, 3, (0,1))
    Hf, If, Wf, mf = hi(vals, 4)
    Hg, Ig, Wg, mg = hi(g, 4)
    p = Fraction(sum(mf[s] for s in range(8,16)), 256)
    assert p == Fraction(1,2)
    assert If == Ig == Fraction(2,1)
    assert abs(Hf-3.0) < 1e-12 and abs(Hg-2.0) < 1e-12
    assert abs((Hf-Hg)-1.0) < 1e-12
    hist_f = {}
    hist_g = {}
    for num in mf:
        if num:
            hist_f[num] = hist_f.get(num,0)+1
    for num in mg:
        if num:
            hist_g[num] = hist_g.get(num,0)+1
    assert hist_f == {64:2, 16:8}   # masses: 2 x 1/4, 8 x 1/16
    assert hist_g == {64:4}         # masses: 4 x 1/4
    return {
        "normalized_boolean_functions_checked": checked,
        "max_rank2_entropy_tax_ratio": max_tax_ratio,
        "max_tax_mask": max_tax_mask,
        "interior_counterexample": {
            "truth_table_lex": vals,
            "pivot_influence": "1/2",
            "H_before": Hf,
            "H_after": Hg,
            "I_before": str(If),
            "I_after": str(Ig),
            "fourier_square_integer_hist_before_den256": hist_f,
            "fourier_square_integer_hist_after_den256": hist_g,
        }
    }


def selector_phase_composition_check():
    # z has 3 selector bits, x has 2 phase bits, y is the flag bit.
    # h(x)=(-1)^(x0*x1) has H(h)=2 and I(h)=1 exactly.
    checked = 0
    max_h_err = 0.0
    for Amask in range(256):
        vals0 = []
        valsh = []
        for state in range(64):
            z = state & 7
            x = (state >> 3) & 3
            y = (state >> 5) & 1
            active = (Amask >> z) & 1
            flag = -1 if y else 1
            h = -1 if ((x&1) and (x&2)) else 1
            vals0.append(flag if active else 1)
            valsh.append((flag*h) if active else 1)
        H0,I0,_,_ = hi(vals0,6)
        Hh,Ih,_,_ = hi(valsh,6)
        p = Fraction(Amask.bit_count(), 8)
        # Exact influence increment p*I(h)=p.
        assert Ih - I0 == p
        # Entropy increment p*H(h)=2p.
        err = abs((Hh-H0) - 2*float(p))
        max_h_err = max(max_h_err, err)
        assert err < 2e-12
        checked += 1
    return {
        "selector_events_checked": checked,
        "phase": "(-1)^(x0*x1)",
        "phase_H": 2,
        "phase_I": 1,
        "max_entropy_identity_abs_error": max_h_err,
    }


if __name__ == "__main__":
    import json
    result = {
        "rank2_triangular_shear_n4": exhaustive_rank2_shear_n4(),
        "selector_phase_composition": selector_phase_composition_check(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
