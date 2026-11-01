from fractions import Fraction as F
from itertools import permutations, combinations


def q(re=0, im=0):
    return (F(re), F(im))


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def sub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def smul(a, z):
    return (a * z[0], a * z[1])


def sgn(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def det4(M):
    out = q()
    for p in permutations(range(4)):
        t = q(1)
        for i, j in enumerate(p):
            t = mul(t, M[i][j])
        out = add(out, smul(F(sgn(p)), t))
    return out


U = [
    [F(-64884, 690625), F(147, 3125), F(-41416, 138125), F(-7704, 8125)],
    [F(118503, 690625), F(3076, 3125), F(4872, 138125), F(168, 8125)],
    [F(668888, 690625), F(-504, 3125), F(-25413, 138125), F(-372, 8125)],
    [F(-106296, 690625), F(168, 3125), F(-129204, 138125), F(2549, 8125)],
]
a = [q(3, 3), q(-4, -5), q(2, 5), q(5, 4)]
b = [q(-1, -2), q(5, 5), q(5, 3), q(5, 2)]

# Exact orthogonality.
for i in range(4):
    for j in range(4):
        x = sum(U[k][i] * U[k][j] for k in range(4))
        assert x == (F(1) if i == j else F(0))

# Genericity checks used by the current MOC4 strict-support reduction.
assert len(set(a)) == 4 and len(set(b)) == 4
assert all(z != q() for z in a + b)
assert all(add(x, y) != q() for x in a for y in b)
assert all(U[i][j] != 0 for i in range(4) for j in range(4))

for rs in combinations(range(4), 2):
    for cs in combinations(range(4), 2):
        m00, m01 = U[rs[0]][cs[0]], U[rs[0]][cs[1]]
        m10, m11 = U[rs[1]][cs[0]], U[rs[1]][cs[1]]
        minor = m00 * m11 - m01 * m10
        assert minor != 0
        tr = m00 * m00 + m01 * m01 + m10 * m10 + m11 * m11
        disc = tr * tr - 4 * minor * minor
        assert disc != 0

# B = U diag(b) U^T (U is real orthogonal).
B = [[q() for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        z = q()
        for k in range(4):
            z = add(z, smul(U[i][k] * U[j][k], b[k]))
        B[i][j] = z

# With simple a, nonzero cross-block entries rule out a common coordinate reducing split.
assert all(B[i][j] != q() for i in range(4) for j in range(i + 1, 4))

M = [[B[i][j] for j in range(4)] for i in range(4)]
for i in range(4):
    M[i][i] = add(M[i][i], a[i])
D = det4(M)
D_expected = (
    F(5647508815927168, 59620361328125),
    F(2616083753751744, 11924072265625),
)
assert D == D_expected

verts = []
for p in permutations(range(4)):
    z = q(1)
    for i, j in enumerate(p):
        z = mul(z, add(a[i], b[j]))
    verts.append((p, z))
assert len({z for _, z in verts}) == 24

# Integer support direction with a unique maximizing permutation vertex.
Acoef, Bcoef = F(-985), F(-12348)


def L(z):
    return Acoef * z[0] + Bcoef * z[1]


maxscore = max(L(z) for _, z in verts)
achievers = [(p, z) for p, z in verts if L(z) == maxscore]
assert maxscore == F(-2687720)
assert achievers == [((2, 1, 0, 3), (F(-280), F(240)))]
LD = L(D)
gap = LD - maxscore
assert LD == F(-33415961428064187008, 11924072265625)
assert gap == F(-1367393918298562008, 11924072265625)
assert gap < 0

# Exact three-vertex Caratheodory certificate that D is inside the 24-point hull.
cert_perms = [(2, 1, 0, 3), (2, 3, 0, 1), (3, 0, 1, 2)]
weights = [
    F(7425176834653241, 7720486083984375),
    F(417322412914702, 50480101318359375),
    F(2186232758361696, 72915701904296875),
]
assert sum(weights, F(0)) == 1
assert all(w >= 0 for w in weights)
vmap = dict(verts)
combo = q()
for w, p in zip(weights, cert_perms):
    combo = add(combo, smul(w, vmap[p]))
assert combo == D

# Exact transposition identity used in the local-tangent theorem.
vid = q(1)
for i in range(4):
    vid = mul(vid, add(a[i], b[i]))
for i, j in combinations(range(4), 2):
    p = list(range(4))
    p[i], p[j] = p[j], p[i]
    vt = vmap[tuple(p)]
    rhs = mul(sub(a[j], a[i]), sub(b[j], b[i]))
    for k in range(4):
        if k not in (i, j):
            rhs = mul(rhs, add(a[k], b[k]))
    assert sub(vt, vid) == rhs

print("PASS exact rational-orthogonal MOC4 stress certificate")
print("det_re =", D[0])
print("det_im =", D[1])
print("unique_support_max_perm_1based =", tuple(x + 1 for x in achievers[0][0]))
print("unique_support_max_vertex =", achievers[0][1])
print("support_det =", LD)
print("support_max =", maxscore)
print("support_gap =", gap)
print("caratheodory_perms_1based =", [tuple(x + 1 for x in p) for p in cert_perms])
print("caratheodory_weights =", weights)
print("genericity = simple spectra; 24 distinct vertices; all 1x1/2x2 minors nonzero; all 2x2 compression discriminants nonzero; irreducible coordinate split")
