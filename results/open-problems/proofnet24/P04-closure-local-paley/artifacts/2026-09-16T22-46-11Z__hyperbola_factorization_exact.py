#!/usr/bin/env python3
"""Exact finite self-check for P04/I0101 hyperbola quotient and conference identities.

All decisions use exact integer modular arithmetic.  The checker verifies, for
p in {149,257,1009,4001}, the quotient parametrization

  phi(u)=(u+1)^2/(4u),   u in Q minus {+/-1}, modulo u~u^{-1},

and the two-localized conference factorization

  chi(phi(alpha^k)-phi(alpha^l))
    = h[k-l] h[k+l],   h[r]=chi(alpha^r-1).

For p=149,257 it also verifies directly the exact block identity

  C_A^2 + U U^T = p I - 3 J,

where U is the conference block from V_2 to all non-anchor vertices outside V_2.
"""

PRIMES = [149, 257, 1009, 4001]

def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def factor(n):
    fs = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            fs.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        fs.append(n)
    return fs

def primitive_root(p):
    fac = factor(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1)//r, p) != 1 for r in fac):
            return g
    raise AssertionError("no primitive root found")

def matmul_int(A, B):
    n = len(A)
    k = len(B)
    m = len(B[0]) if B else 0
    out = [[0]*m for _ in range(n)]
    BT = list(zip(*B))
    for i,row in enumerate(A):
        for j,col in enumerate(BT):
            out[i][j] = sum(x*y for x,y in zip(row,col))
    return out

def check_prime(p):
    assert p % 4 == 1
    q = (p - 1)//2
    assert q % 2 == 0
    m = (p - 5)//4
    assert q//2 == m + 1

    g = primitive_root(p)
    alpha = pow(g, 2, p)
    assert pow(alpha, q, p) == 1
    assert pow(alpha, q//2, p) == p-1

    # Canonical quotient reps k=1,...,m.
    inv4 = pow(4, -1, p)
    xs = []
    us = []
    for k in range(1, m+1):
        u = pow(alpha, k, p)
        us.append(u)
        x = ((u + 1) * (u + 1) * inv4 * pow(u, -1, p)) % p
        xs.append(x)

    assert len(set(xs)) == m
    V2 = sorted(
        x for x in range(p)
        if x not in (0,1) and chi(x,p) == 1 and chi(x-1,p) == 1
    )
    assert sorted(xs) == V2

    # phi(u)=phi(v) iff v=u or u^{-1}; test over all nonexcluded Q.
    domain = [pow(alpha,k,p) for k in range(q) if k not in (0,q//2)]
    buckets = {}
    for u in domain:
        x = ((u + 1) * (u + 1) * inv4 * pow(u, -1, p)) % p
        buckets.setdefault(x, []).append(u)
    assert set(buckets) == set(V2)
    assert all(len(vs) == 2 for vs in buckets.values())
    for vs in buckets.values():
        u,v = vs
        assert (u*v) % p == 1

    # h is an even sequence on Z_q.
    h = [chi(pow(alpha,r,p)-1,p) for r in range(q)]
    assert h[0] == 0
    assert all(h[(-r) % q] == h[r] for r in range(q))

    # Difference identity and conference factorization.
    C = [[0]*m for _ in range(m)]
    for i,k in enumerate(range(1,m+1)):
        u = us[i]
        x = xs[i]
        for j,l in enumerate(range(1,m+1)):
            v = us[j]
            y = xs[j]
            if i == j:
                assert chi(x-y,p) == 0
                C[i][j] = 0
                continue
            # Exact field identity phi(u)-phi(v)=(u-v)(uv-1)/(4uv).
            lhs = (x-y) % p
            rhs = ((u-v) * ((u*v)-1) * inv4 * pow((u*v) % p, -1, p)) % p
            assert lhs == rhs
            val = h[(k-l) % q] * h[(k+l) % q]
            assert val in (-1,1)
            assert chi(lhs,p) == val
            C[i][j] = val

    # Lift to E=Z_q\{0,q/2}: M is C tensor J_2 after pair ordering.
    # Test entrywise without allocating the full q x q matrix.
    for i,k in enumerate(range(1,m+1)):
        for j,l in enumerate(range(1,m+1)):
            expected = C[i][j]
            for sk in (k, (-k) % q):
                for sl in (l, (-l) % q):
                    val = h[(sk-sl) % q] * h[(sk+sl) % q]
                    assert val == expected

    # For small instances verify C_A^2+U U^T=pI-3J exactly.
    conf_identity = "SKIPPED_LARGE"
    if p in (149,257):
        Aset = xs[:]  # same order as C
        outside = [z for z in range(p) if z not in Aset and z not in (0,1)]
        U = [[chi(x-z,p) for z in outside] for x in Aset]
        CT = [list(col) for col in zip(*C)]
        UT = [list(col) for col in zip(*U)]
        C2 = matmul_int(C, C)
        UUT = matmul_int(U, UT)
        for i in range(m):
            for j in range(m):
                target = (p if i == j else 0) - 3
                assert C2[i][j] + UUT[i][j] == target

        # Exhaustive three-cell / elliptic-trace formula for every distinct pair.
        cells = {}
        for aa,bb in ((1,1),(1,-1),(-1,1),(-1,-1)):
            Z = [z for z in range(p)
                 if z not in (0,1) and chi(z,p) == aa and chi(z-1,p) == bb]
            Uc = [[chi(x-z,p) for z in Z] for x in Aset]
            cells[(aa,bb)] = matmul_int(Uc, [list(col) for col in zip(*Uc)])
        for i,x in enumerate(Aset):
            for j,y in enumerate(Aset):
                if i == j:
                    continue
                S1 = sum(chi(z*(x-z)*(y-z),p) for z in range(p))
                S2 = sum(chi((z-1)*(x-z)*(y-z),p) for z in range(p))
                S12 = sum(chi(z*(z-1)*(x-z)*(y-z),p) for z in range(p))
                for aa,bb in ((1,1),(1,-1),(-1,1),(-1,-1)):
                    rhs_num = -3 + aa*(S1-1) + bb*(S2-1) + aa*bb*S12
                    assert rhs_num % 4 == 0
                    assert cells[(aa,bb)][i][j] == rhs_num//4
                assert cells[(1,1)][i][j] == C2[i][j]
        conf_identity = "PASS+THREE_CELL_TRACE_PASS"

    return {
        "p": p, "primitive_root": g, "q": q, "m": m,
        "v2_size": len(V2), "conference_identity": conf_identity,
    }

rows = [check_prime(p) for p in PRIMES]
print("P04-I0101-HYPERBOLA-FACTORIZATION-EXACT=PASS")
for r in rows:
    print(
        "p={p} primitive_root={primitive_root} q={q} |V2|={v2_size} "
        "quotient_reps={m} conference_block_identity={conference_identity}".format(**r)
    )
print("PARAMETRIZATION=PASS")
print("PHI_TWO_TO_ONE_MOD_INVERSION=PASS")
print("H_EVENNESS=PASS")
print("DIFFERENCE_IDENTITY=PASS")
print("CIRCULANT_HANKEL_FACTOR=PASS")
print("LIFT_C_TENSOR_J2=PASS")
print("THREE_CELL_TRACE_FORMULA_SMALL_PRIMES=PASS")
