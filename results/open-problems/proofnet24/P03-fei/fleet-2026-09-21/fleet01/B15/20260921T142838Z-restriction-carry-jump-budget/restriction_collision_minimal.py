from itertools import product


def fwht(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def v2(z):
    z = abs(int(z))
    assert z != 0
    r = 0
    while z % 2 == 0:
        r += 1
        z //= 2
    return r


def packet_depths(W):
    ans = {}
    for m in sorted({abs(w) for w in W if w}):
        eps = [0 if abs(w) != m else (1 if w > 0 else -1) for w in W]
        V = fwht(eps)
        r = min(v2(z) for z in V if z)
        supp = [j for j, w in enumerate(W) if abs(w) == m]
        ans[m] = (r, supp, V)
    return ans


def restrict_values(vals, n, i, bit):
    return [vals[x] for x in range(1 << n) if ((x >> i) & 1) == bit]


def expand_child_index(T, i):
    low = (1 << i) - 1
    return (T & low) | ((T & ~low) << 1)


def witness(vals, n):
    W = fwht(vals)
    pp = packet_depths(W)
    if len(pp) < 2 or any(r != 0 for r, _, _ in pp.values()):
        return None
    for i in range(n):
        b = 1 << i
        for bit in (0, 1):
            s = 1 if bit == 0 else -1
            child = restrict_values(vals, n, i, bit)
            CW = fwht(child)
            cp = packet_depths(CW)
            for mag, (r, supp, V) in cp.items():
                if r < 1:
                    continue
                collisions = []
                for T in supp:
                    U = expand_child_index(T, i)
                    u, v = W[U], W[U | b]
                    d = (u + s * v) // 2
                    assert d == CW[T]
                    if u and v and abs(u) != abs(v):
                        collisions.append((T, u, v, d))
                if collisions:
                    return {
                        "W": W,
                        "parent": pp,
                        "i": i,
                        "bit": bit,
                        "CW": CW,
                        "child": cp,
                        "mag": mag,
                        "collisions": collisions,
                    }
    return None


def vals_from_mask(n, mask):
    N = 1 << n
    return [1 if ((mask >> x) & 1) else -1 for x in range(N)]


def main():
    first = {}
    counts = {}
    for n in (1, 2, 3):
        total = 1 << (1 << n)
        count = 0
        first_w = None
        for mask in range(total):
            vals = vals_from_mask(n, mask)
            w = witness(vals, n)
            if w is not None:
                count += 1
                if first_w is None:
                    first_w = (mask, vals, w)
        counts[n] = count
        first[n] = first_w

    assert counts[1] == 0
    assert counts[2] == 0
    assert counts[3] > 0

    mask, vals, w = first[3]
    assert mask == 1
    assert w["W"] == [-6, 2, 2, 2, 2, 2, 2, 2]
    assert w["CW"] == [-2, 2, 2, 2]
    assert {m: r for m, (r, _, _) in w["parent"].items()} == {2: 0, 6: 0}
    assert {m: r for m, (r, _, _) in w["child"].items()} == {2: 1}
    assert w["collisions"][0][1:] == (-6, 2, -2)

    print("PASS")
    print("property: all parent nonzero magnitude packets have carry depth 0;")
    print("          some one-coordinate restriction has a carry-positive child packet")
    print("          containing a coefficient formed from unequal nonzero parent magnitudes")
    for n in (1, 2, 3):
        print(f"n={n} total_functions={1 << (1 << n)} witnesses={counts[n]}")
    print("first_n3_mask=1")
    print("parent_truth_values=" + repr(vals))
    print("parent_W=" + repr(w["W"]))
    print("parent_packet_depths=" + repr({m: r for m, (r, _, _) in w["parent"].items()}))
    print("restriction_coordinate=0 branch_bit=0")
    print("child_W=" + repr(w["CW"]))
    print("child_packet_depths=" + repr({m: r for m, (r, _, _) in w["child"].items()}))
    print("unequal_collision(T,u,v,d)=" + repr(w["collisions"][0]))


if __name__ == "__main__":
    main()
