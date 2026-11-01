from itertools import product, permutations
from math import isqrt, gcd
from collections import Counter


def matmul(A, B, n):
    return tuple(sum(A[n*i+k] * B[n*k+j] for k in range(n))
                 for i in range(n) for j in range(n))


def trace(A, n):
    return sum(A[n*i+i] for i in range(n))


def charpoly_coeffs(A, n):
    # det(xI-A)=x^n-e1*x^(n-1)+e2*x^(n-2)-...
    powers = []
    cur = A
    for k in range(1, n+1):
        powers.append(trace(cur, n))
        if k < n:
            cur = matmul(cur, A, n)
    e = [1]
    for k in range(1, n+1):
        s = 0
        for i in range(1, k+1):
            s += ((-1) ** (i-1)) * e[k-i] * powers[i-1]
        assert s % k == 0
        e.append(s // k)
    return tuple(((-1) ** k) * e[k] for k in range(n+1))


def divisors_signed(z):
    if z == 0:
        return [0]
    z = abs(z)
    out = []
    for d in range(1, isqrt(z)+1):
        if z % d == 0:
            q = z // d
            out.extend((d, -d))
            if q != d:
                out.extend((q, -q))
    return sorted(set(out))


def eval_poly(c, r):
    v = 0
    for a in c:
        v = v*r + a
    return v


def synthetic_div(c, r):
    out = [c[0]]
    for a in c[1:-1]:
        out.append(a + r*out[-1])
    rem = c[-1] + r*out[-1]
    assert rem == 0
    return tuple(out)


def has_quadratic_split_quartic(c):
    # c=(1,A,B,C,D), and no integer root has already been found.
    _, A, B, C, D = c
    assert D != 0
    for b in divisors_signed(D):
        if b == 0 or D % b:
            continue
        d = D // b
        ac = B - b - d
        disc = A*A - 4*ac
        if disc < 0:
            continue
        sd = isqrt(disc)
        if sd*sd != disc or (A + sd) % 2:
            continue
        a = (A + sd) // 2
        cc = A - a
        if a*d + b*cc == C:
            return True
    return False


def factor_degrees(c):
    c = tuple(c)
    deg = len(c) - 1
    degrees = []
    while deg >= 2:
        const = c[-1]
        roots = [0] if const == 0 else divisors_signed(const)
        root = None
        for r in roots:
            if eval_poly(c, r) == 0:
                root = r
                break
        if root is None:
            break
        degrees.append(1)
        c = synthetic_div(c, root)
        deg -= 1
    if deg == 0:
        pass
    elif deg == 1:
        degrees.append(1)
    elif deg == 2:
        A, B, C = c
        disc = B*B - 4*A*C
        sd = isqrt(disc) if disc >= 0 else -1
        if disc >= 0 and sd*sd == disc:
            raise AssertionError(("missed integer root", c))
        degrees.append(2)
    elif deg == 3:
        degrees.append(3)
    elif deg == 4:
        if has_quadratic_split_quartic(c):
            degrees.extend((2, 2))
        else:
            degrees.append(4)
    else:
        raise AssertionError(deg)
    return tuple(sorted(degrees))


def code_to_matrix(code, n):
    return tuple(1 if ((code >> k) & 1) else -1 for k in range(n*n))


def transform_code(code, n, p, sgn):
    out = 0
    for i in range(n):
        for j in range(n):
            src = n*p[i] + p[j]
            bit = (code >> src) & 1
            if sgn[i] * sgn[j] == -1:
                bit ^= 1
            out |= bit << (n*i+j)
    return out


def signed_perm_orbits_n4():
    n = 4
    transformations = []
    for p in permutations(range(n)):
        for tail in product((-1, 1), repeat=n-1):
            s = (1,) + tail  # D and -D act identically by conjugation.
            transformations.append((p, s))
    assert len(transformations) == 192
    visited = set()
    total_orbits = irreducible_orbits = 0
    sizes = Counter()
    for code in range(1 << (n*n)):
        if code in visited:
            continue
        orb = {transform_code(code, n, p, s) for p, s in transformations}
        visited.update(orb)
        total_orbits += 1
        sizes[len(orb)] += 1
        pat = factor_degrees(charpoly_coeffs(code_to_matrix(code, n), n))
        if pat == (4,):
            irreducible_orbits += 1
    assert len(visited) == 1 << (n*n)
    return total_orbits, irreducible_orbits, sizes


print("EXACT_RADEMACHER_CHARACTERISTIC_POLYNOMIAL_CHECK")
for n in range(1, 5):
    total = 1 << (n*n)
    patterns = Counter()
    distinct = Counter()
    for code in range(total):
        A = code_to_matrix(code, n)
        c = charpoly_coeffs(A, n)
        pat = factor_degrees(c)
        patterns[pat] += 1
        distinct[c] += 1
    irreducible = patterns.get((n,), 0)
    reducible = total - irreducible
    g = gcd(irreducible, total)
    print(f"n={n} total={total} irreducible={irreducible} reducible={reducible} "
          f"P_irred={irreducible//g}/{total//g} factor_patterns={dict(sorted(patterns.items()))} "
          f"distinct_charpolys={len(distinct)}")
    if n == 4:
        nonlinear = patterns.get((2, 2), 0)
        g2 = gcd(nonlinear, total)
        print(f"n=4 pure_2x2_reducible_no_linear_factor={nonlinear} "
              f"probability={nonlinear//g2}/{total//g2}")

o, io, sizes = signed_perm_orbits_n4()
print(f"n=4 signed_permutation_similarity_group_size=192 orbits={o} "
      f"irreducible_orbits={io} reducible_orbits={o-io} orbit_size_distribution={dict(sorted(sizes.items()))}")
print("ALL_EXACT_CHECKS_PASS")
