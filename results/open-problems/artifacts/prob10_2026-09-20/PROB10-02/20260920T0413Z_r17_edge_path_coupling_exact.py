from itertools import product


def bits(mask, m):
    return tuple((mask >> (m - 1 - i)) & 1 for i in range(m))


def mask_from_bits(xs):
    z = 0
    for b in xs:
        z = (z << 1) | b
    return z


def compress_zero_bit(gmask, j, m):
    gs = bits(gmask, m)
    z = 0
    for i, b in enumerate(gs):
        if i != j:
            z = (z << 1) | b
    return z


def expand_zero_bit(c, j, m):
    bs = bits(c, m - 1)
    out = []
    k = 0
    for i in range(m):
        if i == j:
            out.append(0)
        else:
            out.append(bs[k])
            k += 1
    return mask_from_bits(out)


def encode(xmask, gmask, j, m):
    B = 1 << (m - 1)
    return ((xmask * m + j) * B) + compress_zero_bit(gmask, j, m)


def decode(idx, m):
    B = 1 << (m - 1)
    c = idx % B
    q = idx // B
    j = q % m
    xmask = q // m
    return xmask, expand_zero_bit(c, j, m), j


def upd(xmask, gmask, m, u, v):
    # Exact correlated strip update.  The same v is used against the whole raw window.
    x = bits(xmask, m)
    g = bits(gmask, m)
    d = [0] * (m + 1)
    for i in range(1, m + 1):
        d[i] = (1 - g[i - 1]) * int(d[i - 1] or (x[i - 1] == v))
    gp = [0] * m
    for i in range(1, m):
        gp[i - 1] = g[i] + d[i + 1] - d[i]
        assert gp[i - 1] in (0, 1)
    gp[m - 1] = (1 - d[m]) * int(u == v)
    xp = x[1:] + (u,)
    return mask_from_bits(xp), mask_from_bits(gp)


def edge_transition_idx(idx, m, u, v):
    # Edge state: same x, lower gradient g with g_j=0, upper gradient h=g+e_j.
    x, g, j = decode(idx, m)
    h = g | (1 << (m - 1 - j))
    xp, gp = upd(x, g, m, u, v)
    _, hp = upd(x, h, m, u, v)
    diff = gp ^ hp
    if diff == 0:
        return -1  # absorbed / coalesced
    # Previous flux theorem says D'<=D=1; check the exact edge closure here.
    assert diff & (diff - 1) == 0
    j2 = m - 1 - (diff.bit_length() - 1)
    assert ((gp >> (m - 1 - j2)) & 1) == 0
    assert ((hp >> (m - 1 - j2)) & 1) == 1
    return encode(xp, gp, j2, m)


def verify_position_only_obstruction():
    # Exact reachable obstruction inherited from the preceding R17 run:
    # x=(1,0,1), g=(0,0,1), h=(0,1,1).  The single defect is at j=2
    # (one-based) and survives at the same position for all four source inputs.
    m = 3
    x = mask_from_bits((1, 0, 1))
    g = mask_from_bits((0, 0, 1))
    j = 1
    idx = encode(x, g, j, m)
    outs = []
    for u, v in product((0, 1), repeat=2):
        q = edge_transition_idx(idx, m, u, v)
        assert q >= 0
        _, _, j2 = decode(q, m)
        assert j2 == j
        outs.append(q)
    return outs


def alpha_block(m, T):
    # Exact backward word count N_t(e) = number of length-t input words for which
    # a single defect started from edge e has not yet coalesced.
    n = m * (1 << m) * (1 << (m - 1))
    uv = list(product((0, 1), repeat=2))
    trans = [[0] * 4 for _ in range(n)]
    for i in range(n):
        for a, (u, v) in enumerate(uv):
            trans[i][a] = edge_transition_idx(i, m, u, v)
    N = [1] * n
    for _ in range(T):
        NN = [0] * n
        for i, row in enumerate(trans):
            s = 0
            for q in row:
                if q >= 0:
                    s += N[q]
            NN[i] = s
        N = NN
    mx = max(N)
    arg = N.index(mx)
    return n, mx, 4 ** T, arg


print("R17 PROB10-02 exact single-defect edge-chain checker")
outs = verify_position_only_obstruction()
print("m=3 position-only contraction obstruction: all four inputs survive at j=2; PASS")
print("output_edge_indices=", outs)

for m in range(2, 9):
    T = 4 * m
    n, num, den, arg = alpha_block(m, T)
    print(
        f"m={m} edge_states={n} T={T} "
        f"alpha_num={num} alpha_den={den} alpha={num/den:.18f} "
        f"arg={arg} m_alpha={m*num/den:.18f}"
    )
    assert num < den

# For m=8, the exact alpha is strong enough to give the simple additive
# stationary-bias constant C_8 < 50 from the path-coupling theorem in the report.
# With T=32 and alpha=num/den, C <= 8+32*(1+8*alpha/(1-alpha)).
# C<50 is equivalent to 133*num < 5*den.
m = 8
_, num8, den8, _ = alpha_block(m, 4 * m)
assert 133 * num8 < 5 * den8
print("m=8 exact path-coupling stationary-bias certificate: C_8 < 50; PASS")
print("ALL_EXACT_CHECKS_PASS")
