"""Independent truth-table audit of w505's selector obstruction (not FEI)."""
import math


def transform(values):
    n = len(values)
    return [sum(values[x] * (-1 if (x & s).bit_count() & 1 else 1)
                for x in range(n)) / n for s in range(n)]


def entropy(coefficients):
    return math.fsum(-c*c*math.log2(c*c) for c in coefficients if c)


def influence_from_table(values):
    d = (len(values)-1).bit_length()
    return sum(sum(values[x] != values[x ^ (1 << i)] for x in range(len(values)))
               / len(values) for i in range(d))


for m in (1, 2, 3):
    n = 1 << (2*m)
    a = 1 << m
    def bent(x):
        return -1 if ((x & (a-1)) & (x >> m)).bit_count() & 1 else 1
    plus = [bent(x) for x in range(n)]
    minus = [-1 if x == 0 else bent(x) for x in range(n)]
    full = plus + minus
    cf, cp, cm = transform(full), transform(plus), transform(minus)
    h_full, h_plus, h_minus = map(entropy, (cf, cp, cm))
    delta = h_full - (h_plus+h_minus)/2
    iy = sum(cf[s]**2 for s in range(n, 2*n))
    total_i = influence_from_table(full)
    lb = math.log2((a-1)**2+1)
    assert all(abs(abs(c)-1/a)<1e-12 for c in cp)
    assert abs(iy-1/n)<1e-12
    assert abs(total_i-(m+(2*m+1)/n))<1e-12
    assert delta/iy >= lb-1e-10
    assert delta >= 0
    print(f"m={m} delta/I_y={delta/iy:.9f} lower={lb:.9f} "
          f"I_y={iy:.9f} I={total_i:.9f} H/I={h_full/total_i:.9f}")
