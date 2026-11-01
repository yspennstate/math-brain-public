#!/usr/bin/env python3
"""Independent reconstruction checks for B05's bent-overlap payment.

This checker intentionally uses direct character sums (not B05's FWHT code)
for the small exact-formula tests.  Fractions certify every algebraic bound;
Decimal logarithms are used only for evaluating U and observed ratios.
"""

from decimal import Decimal, getcontext
from fractions import Fraction as Q

getcontext().prec = 90
LOG2 = Decimal(2).ln()


def D(q):
    return Decimal(q.numerator) / Decimal(q.denominator)


def spectrum(values):
    size = len(values)
    return [
        Q(sum(values[x] * (-1 if (s & x).bit_count() & 1 else 1)
              for x in range(size)), size)
        for s in range(size)
    ]


def spectrum_recursive(values):
    """Recursive character decomposition, used only for larger dimensions."""
    if len(values) == 1:
        return [Q(values[0])]
    even = spectrum_recursive(values[0::2])
    odd = spectrum_recursive(values[1::2])
    return [(x+y)/2 for x, y in zip(even, odd)] + [(x-y)/2 for x, y in zip(even, odd)]


def caps(weights):
    out = []
    for s in range(len(weights)):
        out.append(sum(weights[t] for t in range(len(weights))
                       if (t & s) == s))
    return out


def caps_fast(weights):
    out = list(weights)
    n = len(out).bit_length()-1
    for bit in range(n):
        mask = 1 << bit
        for s in range(len(out)):
            if not s & mask:
                out[s] += out[s | mask]
    return out


def upper_entropy_from_spectrum(coeff):
    weight = [x * x for x in coeff]
    cap = caps_fast(weight)
    ans = Decimal(0)
    for mass, upper in zip(weight, cap):
        if mass:
            ans += D(mass) * (D(upper / mass).ln() / LOG2)
    return ans


def upper_entropy(values):
    return upper_entropy_from_spectrum(spectrum(values))


def switched_values(g, h, depth):
    zsize = 1 << depth
    return [h[y >> depth] if (y & (zsize - 1)) == 0 else g[y >> depth]
            for y in range(len(g) * zsize)]


def formula(g, h, depth):
    a, b = spectrum(g), spectrum(h)
    return formula_from_coeff(a, b, depth, caps( [x*x for x in a]),
                              caps([x*x for x in b]))


def formula_from_coeff(a, b, depth, A=None, B=None):
    p = Q(1, 1 << depth)
    aa, bb = [x*x for x in a], [x*x for x in b]
    diff = [y-x for x, y in zip(a, b)]
    dd = [x*x for x in diff]
    if A is None:
        A = caps_fast(aa)
    if B is None:
        B = caps_fast(bb)
    C = caps_fast(dd)
    coherent = [(1-p)*x+p*y for x, y in zip(a, b)]
    total = Decimal(0)
    for c, acap, bcap, q, qcap in zip(coherent, A, B, dd, C):
        c2 = c*c
        if c2:
            total += D(c2) * (D(((1-p)*acap+p*bcap)/c2).ln()/LOG2)
        if q:
            total += D(p*(1-p)*q) * (D(qcap/q).ln()/LOG2)
    total += D((p*depth/Q(2)-p*p*depth)*sum(dd, Q(0)))
    return total


def direct_control_influence(values, depth):
    size = len(values)
    total = Q(0)
    for bit in range(depth):
        total += Q(sum(values[x] != values[x ^ (1 << bit)]
                       for x in range(size)), size)
    return total


def bent(k, linear=0, sign=1):
    vals = []
    for x in range(1 << k):
        phase = (x & linear).bit_count() & 1
        for j in range(0, k, 2):
            phase ^= ((x >> j) & 1) & ((x >> (j+1)) & 1)
        vals.append(sign * (-1 if phase else 1))
    return vals


def one_flip(g, point):
    h = list(g)
    h[point] = -h[point]
    return h


def charge_by_formula(g, h, depth):
    p = D(Q(1, 1 << depth))
    return formula(g, h, depth) - (Decimal(1)-p)*upper_entropy(g) - p*upper_entropy(h)


def certify_analytic_box():
    # Worst permitted values: alpha=1/16, p=1/2.
    alpha, p = Q(1, 16), Q(1, 2)
    umax = vmax = Q(17, 4)*alpha
    wmax = Q(33, 8)*p*alpha
    # Bounds after factoring p where appropriate.
    uu_over_p = p*(1+wmax)/(1-p*umax)**2 + (1+vmax)/(1-umax)**2
    uv_over_p = 1/(1-umax)
    uw_over_p = 1/(1-p*umax)
    vv_over_p = 1/(1-vmax)
    ww = 1/(1-wmax)
    assert uu_over_p < 4
    assert uv_over_p < Q(3, 2)
    assert uw_over_p < Q(6, 5)
    assert vv_over_p < Q(3, 2)
    assert ww < Q(6, 5)

    A, B = Q(17, 4), Q(33, 8)
    bracket = (4*A*A + 3*A*A + Q(6, 5)*A*B
               + Q(3, 2)*A*A + Q(3, 5)*B*B)
    taylor_constant = 4 + bracket/2
    assert taylor_constant == Q(61689, 640)
    assert taylor_constant < 97

    # ln 2 = sum_{m>=1} 1/(m 2^m), so a positive partial sum is a
    # rigorous lower bound.  This closes 97/ln2 < 140 without floats.
    ln2_lower = sum((Q(1, m*(1 << m)) for m in range(1, 13)), Q(0))
    assert ln2_lower > Q(693, 1000)
    assert Q(97, 1) / Q(693, 1000) < 140
    return uu_over_p, uv_over_p, uw_over_p, vv_over_p, ww, taylor_constant, ln2_lower


def main():
    assertions = 0
    max_identity_error = Decimal(0)
    direct_cases = 0
    # Exhaust all ordered pairs of genuine Boolean children through n=2.
    for n in (1, 2):
        width = 1 << n
        functions = [[1 if (code >> x) & 1 else -1 for x in range(width)]
                     for code in range(1 << width)]
        for g in functions:
            for h in functions:
                for depth in (1, 2, 3):
                    F = switched_values(g, h, depth)
                    err = abs(upper_entropy(F)-formula(g, h, depth))
                    max_identity_error = max(max_identity_error, err)
                    assert err < Decimal("1e-82")
                    assertions += 1
                    direct_cases += 1
    print(f"exact_shared_identity cases={direct_cases} max_error={max_identity_error:.2E}")

    # Directly reconstruct the physical selector influence, including both
    # endpoints of every active-word edge.
    influence_cases = 0
    for k in (2, 4, 6):
        for linear in (0, 1, (1 << k)-1):
            g = bent(k, linear, -1 if linear == 1 else 1)
            for point in (0, (1 << k)//3, (1 << k)-1):
                h = one_flip(g, point)
                for depth in (1, 2, 4):
                    F = switched_values(g, h, depth)
                    got = direct_control_influence(F, depth)
                    want = 2*Q(1, 1 << depth)*depth*Q(1, 1 << k)
                    assert got == want
                    assertions += 1
                    influence_cases += 1
    print(f"physical_control_influence cases={influence_cases} exact=yes")

    bounds = certify_analytic_box()
    assertions += 8
    print("analytic_box " + " ".join(str(x) for x in bounds))

    # Independently recompute every relative perturbation and the claimed
    # all-parameter inequality on a growing set of bent dimensions.
    theorem_cases = 0
    max_ratio = Decimal("-Infinity")
    for k in (8, 10, 12):
        alpha, delta = Q(1, 1 << (k//2)), Q(1, 1 << k)
        for linear in (0, 1, (1 << k)-1):
            g = bent(k, linear, -1 if linear == 1 else 1)
            for point in (0, (1 << k)//3, (1 << k)-1):
                h = one_flip(g, point)
                a, b = spectrum_recursive(g), spectrum_recursive(h)
                A, B = caps_fast([x*x for x in a]), caps_fast([x*x for x in b])
                Ug = upper_entropy_from_spectrum(a)
                Uh = upper_entropy_from_spectrum(b)
                for depth in (1, 2, 4, 8, 16):
                    p = Q(1, 1 << depth)
                    for x, y, ac, bc in zip(a, b, A, B):
                        c = (1-p)*x+p*y
                        u = bc/ac-1
                        v = y*y/delta-1
                        w = c*c/delta-1
                        assert abs(u) <= Q(17, 4)*alpha
                        assert abs(v) <= Q(17, 4)*alpha
                        assert abs(w) <= Q(33, 8)*p*alpha
                        assert p*v-w == 4*p*(1-p)*delta
                        assertions += 4
                    parent = formula_from_coeff(a, b, depth, A, B)
                    J = parent-(Decimal(1)-D(p))*Ug-D(p)*Uh
                    I = D(2*p*depth*delta)
                    ratio = J/I
                    max_ratio = max(max_ratio, ratio)
                    assert J <= Decimal(71)*I
                    assertions += 1
                    theorem_cases += 1
    print(f"bent_payment cases={theorem_cases} max_J_over_Ictl={max_ratio:.15f}")
    print(f"assertions={assertions} failures=0 randomness=none")


if __name__ == "__main__":
    main()
