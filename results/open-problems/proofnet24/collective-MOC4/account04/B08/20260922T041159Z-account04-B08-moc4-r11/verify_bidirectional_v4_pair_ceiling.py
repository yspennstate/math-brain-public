from fractions import Fraction
from itertools import permutations, combinations

S4 = list(permutations(range(4)))
TRANS = list(combinations(range(4), 2))
ID = (0, 1, 2, 3)
V4 = [ID, (1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0)]


def compose(p, q):
    return tuple(p[q[i]] for i in range(4))


def inv(p):
    q = [0] * 4
    for i, x in enumerate(p):
        q[x] = i
    return tuple(q)


def swap_values(p, i, j):  # tau o p
    return tuple(j if x == i else i if x == j else x for x in p)


def swap_positions(p, i, j):  # p o tau
    q = list(p)
    q[i], q[j] = q[j], q[i]
    return tuple(q)


def gmul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def support_vertices(a, b, eta=(1, 0)):
    H = {}
    for p in S4:
        z = (1, 0)
        for i in range(4):
            z = gmul(z, gadd(a[i], b[p[i]]))
        # Re(eta*z) for eta=(eta_re,eta_im)
        H[p] = Fraction(eta[0] * z[0] - eta[1] * z[1], 1)
    return H


def cosets_v4():
    unseen = set(S4)
    out = []
    while unseen:
        p = next(iter(unseen))
        c = {compose(p, v) for v in V4}
        assert len(c) == 4
        out.append(c)
        unseen -= c
    assert len(out) == 6
    return out


COSETS = cosets_v4()


def metrics(a, b, eta=(1, 0)):
    H = support_vertices(a, b, eta)
    M = max(H.values())
    m = sum(H.values(), Fraction(0)) / 24
    Q = max(sum((H[p] for p in c), Fraction(0)) / 4 for c in COSETS)
    d = M - m
    Delta = M - Q

    # G_out uses tau o sigma, matching the current lead theorem.
    # G_in uses sigma o tau, obtained by swapping a,b and inverting sigma.
    gout = []
    gin = []
    for i, j in TRANS:
        gout.append(2 * M - max(H[p] + H[swap_values(p, i, j)] for p in S4))
        gin.append(2 * M - max(H[p] + H[swap_positions(p, i, j)] for p in S4))

    Gout = sum(gout, Fraction(0))
    Gin = sum(gin, Fraction(0))
    R_out = 3 * d - Delta - Gout / 2
    R_in = 3 * d - Delta - Gin / 2
    R_bi = min(R_out, R_in)
    return H, M, m, Q, d, Delta, gout, gin, Gout, Gin, R_out, R_in, R_bi


def fmt(x):
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def show(name, data):
    _, M, m, Q, d, Delta, gout, gin, Gout, Gin, R_out, R_in, R_bi = data
    print(name)
    print("M", fmt(M), "m", fmt(m), "Q", fmt(Q), "d", fmt(d), "Delta", fmt(Delta))
    print("G_out gaps", [fmt(x) for x in gout], "G_out", fmt(Gout))
    print("G_in gaps ", [fmt(x) for x in gin], "G_in", fmt(Gin))
    print("R_out", fmt(R_out), "R_in", fmt(R_in), "R_bi", fmt(R_bi),
          "gamma_ceiling", fmt(R_bi / 4))


# Campaign-lead exact endpoint datum from MOC4-V4-PAIR-GAP-CEILING-v1.
lead_a = [(-1, 0), (2, 0), (1, 0), (0, 0)]
lead_b = [(-1, 0), (1, 0), (-2, 0), (2, 0)]
lead = metrics(lead_a, lead_b)
show("lead", lead)

# Assigned partner account01/B09 simple-complex dense-lift adversary, eta=1.
partner_a = [(-4, 4), (0, -1), (-3, 2), (-4, -4)]
partner_b = [(-4, -4), (2, -1), (2, -4), (4, -1)]
partner = metrics(partner_a, partner_b)
show("partner", partner)

# Exact inversion symmetry H_{b,a}(sigma)=H_{a,b}(sigma^{-1}).
Ha = support_vertices(lead_a, lead_b)
Hswap = support_vertices(lead_b, lead_a)
assert all(Hswap[p] == Ha[inv(p)] for p in S4)

# Exact regression values.
assert lead[8] == 141
assert lead[9] == 145
assert lead[-1] == 0
assert partner[8] == 862
assert partner[9] == 746
assert partner[-1] == 529

print("PASS MOC4-BIDIRECTIONAL-V4-PAIR-CEILING-v1")
