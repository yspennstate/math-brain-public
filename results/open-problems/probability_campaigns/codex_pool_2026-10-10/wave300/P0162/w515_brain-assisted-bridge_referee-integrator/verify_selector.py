"""Independent finite check of w514-C002/C003; fresh gate: n=4,6 only, <=128 points, CPU <10 s."""
from itertools import product
from math import log2, prod
from time import monotonic

start = monotonic()


def walsh_entropy(values):
    dimension = len(next(iter(values)))
    coeff = []
    for mask in product((0, 1), repeat=dimension):
        a = sum(v * prod(xi for xi, mi in zip(x, mask) if mi) for x, v in values.items()) / len(values)
        coeff.append((mask, a))
    return sum(-a*a*log2(a*a) for _, a in coeff if a), coeff


def influence(values):
    dimension = len(next(iter(values)))
    result = []
    for i in range(dimension):
        count = 0
        for x, v in values.items():
            flipped = x[:i] + (-x[i],) + x[i+1:]
            count += v != values[flipped]
        result.append(count / len(values))
    return result


for n in (4, 6):
    cube = list(product((-1, 1), repeat=n))
    y = (1,) * n
    g = {x: prod((1+x[2*j]+x[2*j+1]-x[2*j]*x[2*j+1])//2 for j in range(n//2)) for x in cube}
    h = {x: v - 2*(x == y) for x, v in g.items()}
    F = {x+(t,): g[x] - (1-t)*(x == y) for x in cube for t in (-1, 1)}
    assert set(F.values()) <= {-1, 1}
    Hg, _ = walsh_entropy(g)
    Hh, _ = walsh_entropy(h)
    HF, _ = walsh_entropy(F)
    Ii = influence(F)
    delta = HF - (Hg + Hh)/2
    print(f"n={n} I_t={Ii[-1]:.12g} delta={delta:.12g} delta/I_t={delta/Ii[-1]:.9f} H/I={HF/sum(Ii):.9f}")
    assert abs(Ii[-1] - 2**(-n)) < 1e-12
    assert delta >= n*Ii[-1]
    assert HF <= 2*sum(Ii)

assert monotonic() - start < 10
