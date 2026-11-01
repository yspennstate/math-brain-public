from itertools import combinations
from collections import defaultdict
from math import comb

def closure(n, rel):
    R = set(rel)
    changed = True
    while changed:
        changed = False
        add = set()
        for a, b in tuple(R):
            for c, d in tuple(R):
                if b == c and a != d and (a, d) not in R:
                    add.add((a, d))
        if any(a == b or (b, a) in R for a, b in add):
            return None
        if add:
            R |= add
            changed = True
    return R

def linear_extensions(vertices, R):
    V = tuple(vertices)
    pred = {v: {a for a, b in R if b == v and a in V} for v in V}
    out = []
    def rec(prefix, remaining):
        if not remaining:
            out.append(tuple(prefix))
            return
        rem = set(remaining)
        mins = [v for v in remaining if not (pred[v] & rem)]
        for v in mins:
            rec(prefix + (v,), tuple(w for w in remaining if w != v))
    rec(tuple(), V)
    return out

def build(m, d, ncount, ucount, mask_dn, mask_nu):
    C = list(range(m))
    off = m
    D = list(range(off, off + d)); off += d
    N = list(range(off, off + ncount)); off += ncount
    U = list(range(off, off + ucount)); off += ucount
    rel = set()

    rel |= {(C[i], C[i+1]) for i in range(m-1)}
    rel |= {(D[i], D[i+1]) for i in range(d-1)}
    rel |= {(U[i], U[i+1]) for i in range(ucount-1)}

    for x in D:
        for c in C:
            rel.add((x, c))
    for c in C:
        for x in U:
            rel.add((c, x))

    it = iter(mask_dn)
    for x in D:
        for y in N:
            if next(it):
                rel.add((x, y))

    it = iter(mask_nu)
    for y in N:
        for x in U:
            if next(it):
                rel.add((y, x))

    R = closure(off, rel)
    if R is None:
        return None
    if any((x, c) in R or (c, x) in R for x in N for c in C):
        return None
    return off, C, D, N, U, R

def central_k(tau, D, N, U):
    pos = {v: i for i, v in enumerate(tau)}
    last_D = max([pos[x] for x in D], default=-1)
    first_U = min([pos[x] for x in U], default=len(tau))
    return sum(last_D < pos[x] < first_U for x in N)

cases = fibers = adjacent_swaps = 0

for m in range(1, 4):
    for d in range(0, 3):
        for ncount in range(1, 3):
            for ucount in range(0, 3):
                for mask_dn_int in range(1 << (d * ncount)):
                    mask_dn = [(mask_dn_int >> i) & 1 for i in range(d * ncount)]
                    for mask_nu_int in range(1 << (ncount * ucount)):
                        mask_nu = [(mask_nu_int >> i) & 1 for i in range(ncount * ucount)]
                        built = build(m, d, ncount, ucount, mask_dn, mask_nu)
                        if built is None:
                            continue

                        total, C, D, N, U, R = built
                        Q = D + N + U
                        LEQ = linear_extensions(Q, R)
                        LEP = linear_extensions(list(range(total)), R)
                        if len(LEP) > 50000:
                            continue

                        fiber = defaultdict(int)
                        for L in LEP:
                            tau = tuple(v for v in L if v not in C)
                            fiber[tau] += 1

                        kvals = set()
                        for tau in LEQ:
                            k = central_k(tau, D, N, U)
                            kvals.add(k)
                            assert fiber[tau] == comb(m + k, k)
                            fibers += 1

                        boundary_complete = (
                            all((x, y) in R for x in D for y in N)
                            and all((y, z) in R for y in N for z in U)
                        )
                        assert (len(kvals) == 1) == boundary_complete
                        if boundary_complete:
                            assert kvals == {len(N)}

                        for tau in LEQ:
                            k = central_k(tau, D, N, U)
                            for i in range(len(tau) - 1):
                                a, b = tau[i], tau[i+1]
                                if (a, b) in R or (b, a) in R:
                                    continue
                                swapped = tau[:i] + (b, a) + tau[i+2:]
                                if swapped not in fiber:
                                    continue
                                kp = central_k(swapped, D, N, U)
                                assert abs(k - kp) <= 1
                                if k == kp:
                                    assert fiber[tau] == fiber[swapped]
                                else:
                                    lo, hi = sorted((k, kp))
                                    expected_ratio_num = m + hi
                                    expected_ratio_den = hi
                                    wlo = comb(m + lo, lo)
                                    whi = comb(m + hi, hi)
                                    assert whi * expected_ratio_den == wlo * expected_ratio_num
                                adjacent_swaps += 1

                        cases += 1

print("POS3_AUTONOMOUS_CHAIN_CORRIDOR_CHECK_PASS")
print("generated_cases =", cases)
print("fiber_checks =", fibers)
print("adjacent_incomparable_swap_checks =", adjacent_swaps)
