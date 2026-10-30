from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from math import log2

A_MASK = 0xDFAD
B_MASK = 0x24495BA0


def truth_from_positive_mask(n: int, mask: int):
    return [1 if (mask >> x) & 1 else -1 for x in range(1 << n)]


def fwht_int(vals):
    a = list(map(int, vals))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def v2(z: int):
    z = abs(z)
    assert z
    return (z & -z).bit_length() - 1


def packet_table(vals):
    N = len(vals)
    n = N.bit_length() - 1
    W = fwht_int(vals)
    groups = defaultdict(list)
    for s, w in enumerate(W):
        if w:
            groups[abs(w)].append((s, 1 if w > 0 else -1))
    out = {}
    for m, labels in groups.items():
        V = []
        for x in range(N):
            V.append(sum(sign * (-1 if ((s & x).bit_count() & 1) else 1)
                         for s, sign in labels))
        r = min(v2(z) for z in V if z)
        count = len(labels)
        p = Fraction(count*m*m, N*N)
        # In this checker all relevant meshes are powers of two.
        num = m * (1 << r)
        assert N % num == 0
        inv_b = N // num
        assert inv_b & (inv_b - 1) == 0
        depth = inv_b.bit_length() - 1
        Na = Fraction(count, 4**r)
        out[m] = dict(count=count, r=r, p=p, depth=depth, N=Na, V=V)
    return n, W, out


def D_from_packets(packets):
    return sum((d['p'] * d['depth'] for d in packets.values()), Fraction(0))


def N_from_packets(packets):
    return sum((d['N'] for d in packets.values()), Fraction(0))


def R_from_packets(packets):
    return sum((d['p'] * d['r'] for d in packets.values()), Fraction(0))


def influence(vals):
    N = len(vals)
    n = N.bit_length() - 1
    inf = []
    for i in range(n):
        crossings = sum(vals[x] != vals[x ^ (1 << i)] for x in range(N))
        inf.append(Fraction(crossings, N))
    return inf, sum(inf, Fraction(0))


def tensor_vals(left, right):
    # Lexicographic product ordering; Walsh magnitudes are unaffected by the exact block ordering.
    return [a*b for a in left for b in right]


def direct_tensor_power_A_B(t):
    vals = truth_from_positive_mask(5, B_MASK)
    Aval = truth_from_positive_mask(4, A_MASK)
    for _ in range(t):
        vals = tensor_vals(Aval, vals)
    return vals


def main():
    Avals = truth_from_positive_mask(4, A_MASK)
    Bvals = truth_from_positive_mask(5, B_MASK)
    nA, WA, PA = packet_table(Avals)
    nB, WB, PB = packet_table(Bvals)

    assert nA == 4 and nB == 5
    assert {m:(d['count'], d['r'], d['p'], d['depth']) for m,d in PA.items()} == {
        4:(8,2,Fraction(1,2),0),
        8:(2,1,Fraction(1,2),0),
    }
    assert {m:(d['count'], d['r'], d['p'], d['depth']) for m,d in PB.items()} == {
        4:(16,3,Fraction(1,4),0),
        8:(8,1,Fraction(1,2),1),
        16:(1,0,Fraction(1,4),1),
    }

    # A's two physical packets are integer signed selectors on disjoint cells.
    Ahs = []
    for m, d in sorted(PA.items()):
        h = [z // (1 << d['r']) for z in d['V']]
        assert all(z in (-1,0,1) for z in h)
        Ahs.append(h)
    for x in range(16):
        nz = [h[x] for h in Ahs if h[x] != 0]
        assert len(nz) == 1 and nz[0] == Avals[x]

    IA_vec, IA = influence(Avals)
    IB_vec, IB = influence(Bvals)
    assert IA == Fraction(7,4)
    assert IB == Fraction(25,8)

    DA = D_from_packets(PA)
    DB = D_from_packets(PB)
    NA = N_from_packets(PA)
    NB = N_from_packets(PB)
    assert DA == 0 and NA == 1
    assert DB == Fraction(3,4) and NB == Fraction(13,4)

    # Symbolic all-t theorem. A^t has exponent j in [t,2t] and all packet mesh depth 0.
    # B has exponent-depth pairs (3,0), (2,1), (1,1).
    rows = []
    for t in range(0, 13):
        q = Fraction(1, 2**(t+2)) # unique output packet retaining mesh depth 0
        Dt = 1 - q
        Nt = 4 - 3*q
        It = Fraction(7*t,4) + Fraction(25,8)
        growth = Dt - DB
        rows.append((t,q,Dt,Nt,It,growth))
        assert growth == Fraction(1,4) - q

    # Direct Walsh verification for t=0,1,2 (dimensions 5,9,13).
    for t in range(0,3):
        vals = direct_tensor_power_A_B(t)
        _, _, P = packet_table(vals)
        q = Fraction(1, 2**(t+2))
        assert D_from_packets(P) == 1-q
        assert N_from_packets(P) == 4-3*q
        _, I = influence(vals)
        assert I == Fraction(7*t,4)+Fraction(25,8)

    # The natural exact-scale proposal 2*Delta D <= packet-KL(A)+packet-KL(B) is already false at t=1.
    # KL(A)=0. KL(B)=log2(13/4)-3/2 = log2(13)-7/2.
    # KL(B) < 1/4 iff 13^4 < 2^15, checked exactly below.
    assert 13**4 < 2**15
    delta1 = rows[1][5]
    assert 2*delta1 == Fraction(1,4)

    # Even giving the collision the *entire* initial KL(B) (rather than half of it) fails cumulatively by t=3:
    # KL(B) < 7/32 iff 13^32 < 2^119.
    assert 13**32 < 2**119
    delta3 = rows[3][5]
    assert delta3 == Fraction(7,32)

    klB = log2(13/4) - 1.5
    print('PASS')
    print('A_mask=0x%04x B_mask=0x%08x' % (A_MASK, B_MASK))
    print('A_packets=', {m:(d['count'],d['r'],str(d['p']),d['depth']) for m,d in sorted(PA.items())})
    print('B_packets=', {m:(d['count'],d['r'],str(d['p']),d['depth']) for m,d in sorted(PB.items())})
    print('D_A=', DA, 'N_A=', NA, 'I_A=', IA, 'KL_A=0')
    print('D_B=', DB, 'N_B=', NB, 'I_B=', IB, 'KL_B=%.15f' % klB)
    for t,q,Dt,Nt,It,growth in rows[:7]:
        KLt = log2(float(Nt)) - 2*float(Dt)
        print('t=%d q=%s D=%s N=%s I=%s growth=%s KL=%.15f' % (t,q,Dt,Nt,It,growth,KLt))
    print('exact_KL_B_lt_1/4:', 13**4, '<', 2**15)
    print('exact_KL_B_lt_7/32:', 13**32, '<', 2**119)

if __name__ == '__main__':
    main()
