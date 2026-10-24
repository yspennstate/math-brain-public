"""Independent complete truth-table check of w504's quadratic selector family."""
import math


def transform(values):
    n = len(values)
    return [sum(values[x] * (-1 if (x & s).bit_count() & 1 else 1)
                for x in range(n)) / n for s in range(n)]


def entropy(values):
    return math.fsum(-c*c*math.log2(c*c) for c in transform(values) if c)


def restrict(values, j, bit):
    out = []
    for t in range(len(values)//2):
        x = (t & ((1 << j)-1)) | (bit << j) | ((t >> j) << (j+1))
        out.append(values[x])
    return out


def influence(values, j):
    return sum(values[x] != values[x ^ (1 << j)] for x in range(len(values))) / len(values)


def rlogr(u):
    return 0.0 if u == 0 else u*u*math.log2(u)


for m in (2, 4, 6, 8):
    n = 1 << m
    a = 2**(-m/2)
    t = 1/n
    base = [(-1)**sum(((x >> j) & (x >> (j+1)) & 1) for j in range(0,m,2))
            for x in range(n)]
    full = base + [-1 if x == 0 else base[x] for x in range(n)]
    h = entropy(full)
    qz = influence(full,m)
    dz = h-(entropy(restrict(full,m,0))+entropy(restrict(full,m,1)))/2
    assert abs(qz-t)<1e-12
    assert abs(sum(influence(full,j) for j in range(m+1))-(m/2+(m+1)*t))<1e-12
    for j in range(m):
        q = influence(full,j)
        d = h-(entropy(restrict(full,j,0))+entropy(restrict(full,j,1)))/2
        assert abs(q-(.5+t))<1e-12
        assert d <= 2-(m/2)*t+1e-11
        assert d < 4*q
    # The load-bearing Jensen sign is checked separately from the truth table.
    assert rlogr(1-a)+rlogr(1+a)>=-1e-12
    assert h <= 2*sum(influence(full,j) for j in range(m+1))+1e-12
    print(f"m={m} selector_ratio={dz/qz:.9f} base_ratio={d/q:.9f} "
          f"base_bound={2-(m/2)*t:.9f} H/I={h/(m/2+(m+1)*t):.9f}")
