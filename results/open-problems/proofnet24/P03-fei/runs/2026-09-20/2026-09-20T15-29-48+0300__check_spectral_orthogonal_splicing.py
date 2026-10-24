import json, math, random

SEED = 20260920
TOL = 1e-10


def fwht(vals):
    a = [float(v) for v in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]


def fwht_int(vals):
    a = [int(v) for v in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def entropy_prob(ps):
    return -sum(p*math.log2(p) for p in ps if p > 0.0)


def entropy_fourier(vals):
    a = fwht(vals)
    return entropy_prob([x*x for x in a])


def influence_fourier(vals):
    a = fwht(vals)
    return sum(s.bit_count() * x*x for s, x in enumerate(a))


def support_exact(vals):
    return {i for i, x in enumerate(fwht_int(vals)) if x}


def bool_funcs(n, quotient=False):
    N = 1 << n
    if quotient:
        for mask in range(1 << (N-1)):
            yield [1] + [1 if (mask >> (x-1)) & 1 else -1 for x in range(1, N)]
    else:
        for mask in range(1 << N):
            yield [1 if (mask >> x) & 1 else -1 for x in range(N)]


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1-x)*math.log2(1-x)


def block_conditional_entropy(vals, a, m):
    coeff = fwht(vals)
    ps = [x*x for x in coeff]
    ymarg = [0.0] * (1 << m)
    for s, p in enumerate(ps):
        ymarg[s >> a] += p
    return entropy_prob(ps) - entropy_prob(ymarg)


def build_F(u0, u1, gp, gm, a, m):
    c = [(gp[y] + gm[y])/2.0 for y in range(1 << m)]
    d = [(gp[y] - gm[y])/2.0 for y in range(1 << m)]
    vals = []
    for idx in range(1 << (a+m)):
        aa = idx & ((1 << a)-1)
        y = idx >> a
        z = u0[aa]*c[y] + u1[aa]*d[y]
        if abs(z) != 1.0:
            raise AssertionError("F is not Boolean")
        vals.append(int(z))
    return vals, c, d


def virtual_selector(gp, gm):
    c = [(x+y)/2.0 for x, y in zip(gp, gm)]
    d = [(x-y)/2.0 for x, y in zip(gp, gm)]
    ch, dh = fwht(c), fwht(d)
    B = 0.0
    M = 0.0
    for x, y in zip(ch, dh):
        aa, bb = x*x, y*y
        q = aa + bb
        mm = min(aa, bb)
        M += mm
        if q > 0.0 and mm > 0.0:
            B += q*h2(mm/q)
    return B, M, ch, dh


def check_case(u0, u1, gp, gm, a, m, stats):
    F, c, d = build_F(u0, u1, gp, gm, a, m)
    beta = sum(x*x for x in d) / len(d)
    H0, H1 = entropy_fourier(u0), entropy_fourier(u1)
    I0, I1 = influence_fourier(u0), influence_fourier(u1)
    BV, M, ch, dh = virtual_selector(gp, gm)

    BA = block_conditional_entropy(F, a, m)
    rhs_B = (1-beta)*H0 + beta*H1 + BV
    stats["max_block_identity_error"] = max(stats["max_block_identity_error"], abs(BA-rhs_B))

    coeffF = fwht(F)
    maskA = (1 << a)-1
    IA = sum((s & maskA).bit_count() * x*x for s, x in enumerate(coeffF))
    IY = sum((s >> a).bit_count() * x*x for s, x in enumerate(coeffF))
    rhs_IA = (1-beta)*I0 + beta*I1
    rhs_IY = 0.5*(influence_fourier(gp) + influence_fourier(gm))
    stats["max_controller_influence_identity_error"] = max(
        stats["max_controller_influence_identity_error"], abs(IA-rhs_IA))
    stats["max_residual_influence_identity_error"] = max(
        stats["max_residual_influence_identity_error"], abs(IY-rhs_IY))

    j = min(beta, 1-beta)
    stats["max_M_minus_j"] = max(stats["max_M_minus_j"], M-j)
    stats["max_B_minus_h2M"] = max(stats["max_B_minus_h2M"], BV-h2(M))

    pg = [x*x for x in fwht(gp)]
    pm = [x*x for x in fwht(gm)]
    iso = max(abs(x-y) for x, y in zip(pg, pm)) <= 1e-12
    if iso:
        stats["isospectral_cases"] += 1
        stats["max_isospectral_virtual_B"] = max(stats["max_isospectral_virtual_B"], abs(BV))

    stats["cases"] += 1


def tensor_vals(a, b):
    # First block uses low-order bits, second block high-order bits.
    return [a[i] * b[j] for j in range(len(b)) for i in range(len(a))]


def translate(vals, n, shift):
    return [vals[x ^ shift] for x in range(1 << n)]


def main():
    stats = {
        "seed": SEED,
        "status": "PASS",
        "controller_pairs": 0,
        "cases": 0,
        "exhaustive_cases": 0,
        "random_cases": 0,
        "cases_by_controller_dim": {},
        "isospectral_cases": 0,
        "max_block_identity_error": 0.0,
        "max_controller_influence_identity_error": 0.0,
        "max_residual_influence_identity_error": 0.0,
        "max_B_minus_h2M": 0.0,
        "max_M_minus_j": 0.0,
        "max_isospectral_virtual_B": 0.0,
    }

    # Exhaustive controller pairs modulo independent global signs, dimensions 1..3.
    # Residual child pairs are exhaustive through dimension 2.
    for a in range(1, 4):
        ctrls = [(v, support_exact(v)) for v in bool_funcs(a, quotient=True)]
        pairs = [(u0, u1) for u0, s0 in ctrls for u1, s1 in ctrls if s0.isdisjoint(s1)]
        stats["controller_pairs"] += len(pairs)
        before = stats["cases"]
        for m in range(1, 3):
            children = list(bool_funcs(m, quotient=False))
            for u0, u1 in pairs:
                for gp in children:
                    for gm in children:
                        check_case(u0, u1, gp, gm, a, m, stats)
        local = stats["cases"] - before
        stats["cases_by_controller_dim"][str(a)] = local
    stats["exhaustive_cases"] = stats["cases"]

    # Higher-dimensional deterministic-seed stress tests.  Tensoring the explicit
    # 3-bit disjoint-support pair with the same arbitrary Boolean w preserves
    # disjoint Fourier supports.  Half the residual sibling pairs are made exactly
    # isospectral by translation; the others are independent random Boolean pairs.
    rng = random.Random(SEED)
    base0 = [1, 1, -1, -1, -1, -1, -1, -1]
    base1 = [1, -1, -1, 1, 1, -1, 1, -1]
    for trial in range(500):
        extra = rng.randint(1, 3)
        w = [1 if rng.getrandbits(1) else -1 for _ in range(1 << extra)]
        u0 = tensor_vals(base0, w)
        u1 = tensor_vals(base1, w)
        a = 3 + extra
        if not support_exact(u0).isdisjoint(support_exact(u1)):
            raise AssertionError("tensor controller lost spectral orthogonality")
        m = rng.randint(3, min(6, 10-a)) if a < 7 else 3
        gp = [1 if rng.getrandbits(1) else -1 for _ in range(1 << m)]
        if trial % 2 == 0:
            shift = rng.randrange(1 << m)
            sign = -1 if rng.getrandbits(1) else 1
            gm = [sign*x for x in translate(gp, m, shift)]
        else:
            gm = [1 if rng.getrandbits(1) else -1 for _ in range(1 << m)]
        check_case(u0, u1, gp, gm, a, m, stats)
        stats["random_cases"] += 1

    bad = max(
        stats["max_block_identity_error"],
        stats["max_controller_influence_identity_error"],
        stats["max_residual_influence_identity_error"],
        stats["max_B_minus_h2M"],
        stats["max_M_minus_j"],
        stats["max_isospectral_virtual_B"],
    )
    if bad > TOL:
        stats["status"] = "FAIL"
    print(json.dumps(stats, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
