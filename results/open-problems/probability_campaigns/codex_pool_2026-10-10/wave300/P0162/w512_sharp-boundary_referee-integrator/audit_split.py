"""Independent grouped-coefficient check of w511's split formulas."""

from math import log2, log


def ent_term(weight: float) -> float:
    return -weight * log2(weight) if weight else 0.0


for m in (2, 4, 6, 8, 12, 16):
    n = 1 << m
    root = 1 << (m // 2)
    p = 1 / n
    s = 1 / root
    pos, neg = (n + root) // 2, (n - root) // 2
    hg = float(m)
    hh = (pos * ent_term((s - 2 * p) ** 2)
          + neg * ent_term((-s - 2 * p) ** 2))
    hf = (pos * ent_term((s - p) ** 2)
          + neg * ent_term((-s - p) ** 2)
          + n * ent_term(p ** 2))
    delta = hf - (hg + hh) / 2
    h2p = ent_term(p) + ent_term(1 - p)
    assert delta / p >= m - 4 / log(2) - 1e-7
    assert 0 <= delta <= 2 + 1e-8
    l1 = (pos * abs(s ** 2 - (s - 2 * p) ** 2)
          + neg * abs(s ** 2 - (-s - 2 * p) ** 2))
    assert abs(l1 / p - 4 * (1 - p) / s) < 1e-7
    print(f"m={m} delta/p={delta/p:.9f} lower={m-4/log(2):.9f} "
          f"sharp_residue={(delta-h2p)/p:.9f} "
          f"target={2/log(2):.9f} proxy_l1/p={l1/p:.6f}")
