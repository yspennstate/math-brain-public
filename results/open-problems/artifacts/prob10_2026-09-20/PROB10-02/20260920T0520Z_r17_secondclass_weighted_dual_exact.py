from itertools import product
from fractions import Fraction

UV = ((0,0),(0,1),(1,0),(1,1))

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

def carrier_and_update(xmask, gmask, m, u, v):
    x = bits(xmask, m)
    g = bits(gmask, m)
    d = [0] * (m + 1)
    for i in range(1, m + 1):
        d[i] = (1 - g[i-1]) * int(d[i-1] or (x[i-1] == v))
    gp = [0] * m
    for i in range(1, m):
        gp[i-1] = g[i] + d[i+1] - d[i]
        assert gp[i-1] in (0,1)
    gp[m-1] = (1 - d[m]) * int(u == v)
    xp = x[1:] + (u,)
    return d, mask_from_bits(xp), mask_from_bits(gp)

def edge_transition_detail(idx, m, u, v):
    xmask, gmask, j = decode(idx, m)
    hmask = gmask | (1 << (m - 1 - j))
    dg, xp, gp = carrier_and_update(xmask, gmask, m, u, v)
    dh, xp2, hp = carrier_and_update(xmask, hmask, m, u, v)
    assert xp == xp2
    diff = gp ^ hp
    if diff == 0:
        return -1, dg, dh
    assert diff & (diff - 1) == 0
    j2 = m - 1 - (diff.bit_length() - 1)
    assert ((gp >> (m - 1 - j2)) & 1) == 0
    assert ((hp >> (m - 1 - j2)) & 1) == 1
    return encode(xp, gp, j2, m), dg, dh

def verify_local_classification(idx, m, u, v):
    xmask, gmask, j0 = decode(idx, m)
    x = bits(xmask, m)
    g = bits(gmask, m)
    q, dg, dh = edge_transition_detail(idx, m, u, v)
    j = j0 + 1
    A = int(dg[j-1] or (x[j-1] == v))
    assert dg[j] == A and dh[j] == 0
    if A == 0:
        if j == 1:
            assert q == -1
        else:
            assert q >= 0
            _, _, j20 = decode(q, m)
            assert j20 + 1 == j - 1
    else:
        k = None
        for kk in range(j+1, m+1):
            if g[kk-1] == 1 or x[kk-1] == v:
                k = kk
                break
        if k is not None:
            assert q >= 0
            _, _, j20 = decode(q, m)
            assert j20 + 1 == k - 1
        else:
            if u == v:
                assert q >= 0
                _, _, j20 = decode(q, m)
                assert j20 + 1 == m
            else:
                assert q == -1
    if q >= 0:
        _, _, j20 = decode(q, m)
        # Z_{t+1}=(t+1)+(j20+1), Z_t=t+j, so need j20+1 >= j-1.
        assert (j20 + 1) >= j - 1
    return q

def exact_weighted_dual(m, T):
    n = m * (1 << m) * (1 << (m - 1))
    trans = [[-1]*4 for _ in range(n)]
    for i in range(n):
        for a,(u,v) in enumerate(UV):
            q = verify_local_classification(i,m,u,v)
            trans[i][a] = q
    # Interior monochromatic self-loop obstruction for m>=4, one-based defect j=2.
    if m >= 4:
        x = 0
        g = 0
        j0 = 1
        idx = encode(x,g,j0,m)
        q,_,_ = edge_transition_detail(idx,m,0,0)
        assert q == idx
    N = [1]*n
    for _ in range(T):
        NN = [0]*n
        for i,row in enumerate(trans):
            s = 0
            for q in row:
                if q >= 0:
                    s += N[q]
            NN[i] = s
        N = NN
    alpha_num = max(N)
    alpha_den = 4**T
    alpha = Fraction(alpha_num, alpha_den)
    NN = [0]*n
    for i,row in enumerate(trans):
        s = 0
        for q in row:
            if q >= 0:
                s += N[q]
        NN[i] = s
    lam = Fraction(0,1)
    arg = -1
    for i,(a,b) in enumerate(zip(NN,N)):
        if b:
            r = Fraction(a, 4*b)
            if r > lam:
                lam = r
                arg = i
    assert lam < 1
    assert m*alpha < 1
    C = Fraction(m+T,1) + m*alpha/(1-lam)
    return n, alpha, lam, C, arg

print("R17 PROB10-02 exact second-class / weighted-dual checker")
last = None
for m in range(2,9):
    T = 4*m
    n, alpha, lam, C, arg = exact_weighted_dual(m,T)
    last = (m,n,alpha,lam,C,arg)
    print(
        f"m={m} edge_states={n} T={T} "
        f"alpha={alpha.numerator}/{alpha.denominator}={float(alpha):.18f} "
        f"lambda={lam.numerator}/{lam.denominator}={float(lam):.18f} "
        f"C={C.numerator}/{C.denominator}={float(C):.18f} arg={arg}"
    )

# Exact advertised width-4 (m=8) certificate.
m,n,alpha8,lam8,C8,arg8 = last
assert m == 8 and C8 < 43
print("m=8 environment-weighted finite-horizon/stationary certificate: C_8 < 43; PASS")
print("m>=4 monochromatic interior self-loop obstruction checked; PASS")
print("local second-class transition classification and Z-monotonicity checked through m=8; PASS")
print("ALL_EXACT_CHECKS_PASS")
