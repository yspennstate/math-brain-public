#!/usr/bin/env python3
"""Worker 057: exact polynomial certificates, standard library only.

Construction uses Macaulay row reduction for three quadrics in three variables.
Every reported final certificate is rechecked by univariate substitution; a
finite computation is not a substitute for the universal proofs in agents/057.md.
"""
from fractions import Fraction as Q
from itertools import product, permutations
from math import gcd, lcm
import json
from pathlib import Path
import random
import sys


def clean(f):
    return {a: b for a, b in f.items() if b}


def add(f, g):
    h = dict(f)
    for a, b in g.items():
        h[a] = h.get(a, 0) + b
    return clean(h)


def scale(f, c):
    return clean({a: c*b for a, b in f.items()})


def mul(f, g):
    h = {}
    for a, b in f.items():
        for c, d in g.items():
            e = tuple(x+y for x, y in zip(a, c))
            h[e] = h.get(e, 0) + b*d
    return clean(h)


def derivative(f, j):
    g = {}
    for a, c in f.items():
        if a[j]:
            b = list(a)
            b[j] -= 1
            g[tuple(b)] = c*a[j]
    return g


def monomials(n, degree):
    return sorted((a for a in product(range(degree+1), repeat=n)
                   if sum(a) <= degree), key=lambda a: (sum(a), a), reverse=True)


def coordinates(n):
    one = {(0,)*n: Q(1)}
    xs = [{tuple(int(i == j) for i in range(n)): Q(1)} for j in range(n)]
    last = one
    for x in xs:
        last = add(last, scale(x, -1))
    return xs + [last]


def qso_system(rows, ntypes=4):
    xs = coordinates(ntypes-1)
    vs = [{} for _ in range(ntypes)]
    for (i, j), row in rows.items():
        assert i <= j
        assert len(row) == ntypes and sum(row) == 1
        assert row[i] == row[j] == 0 and min(row) >= 0
        w = scale(mul(xs[i], xs[j]), 1 if i == j else 2)
        for k, a in enumerate(row):
            vs[k] = add(vs[k], scale(w, a))
    fs = [add(xs[k], scale(vs[k], -1)) for k in range(ntypes)]
    assert not clean(sum_polys(fs))
    return fs[:-1]


def sum_polys(fs):
    ans = {}
    for f in fs:
        ans = add(ans, f)
    return ans


def rref(a, prime=None):
    a = [list(row) for row in a]
    if prime:
        a = [[int(x.numerator)*pow(int(x.denominator), -1, prime) % prime
              if isinstance(x, Q) else x % prime for x in row] for row in a]
    pivots = []
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, prime) if prime else 1/Q(a[r][c])
        a[r] = [x*inv % prime if prime else x*inv for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [(x-q*y) % prime if prime else x-q*y
                        for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a, pivots


def solve(a, b, prime=None):
    n = len(a)
    rr, piv = rref([list(row)+[v] for row, v in zip(a, b)], prime)
    if piv != list(range(n)):
        raise ValueError('singular linear solve')
    return [row[-1] for row in rr]


def matvec(a, b, prime=None):
    v = [sum(x*y for x, y in zip(row, b)) for row in a]
    return [x % prime for x in v] if prime else v


def macaulay_rur(fs, prime=None):
    """Return q(t), coordinate polynomials, and exact truncated rank data.

    The returned identities are separately checked; the Macaulay construction
    is not trusted as an ideal-dimension oracle.
    """
    n = len(fs)
    top = n+1
    mons = monomials(n, top)
    index = {m: i for i, m in enumerate(mons)}
    rows = []
    for f in fs:
        for mon in monomials(n, top-2):
            ff = mul(f, {mon: Q(1)})
            rows.append([ff.get(m, Q(0)) for m in mons])
    rr, piv = rref(rows, prime)
    free = [j for j in range(len(mons)) if j not in piv]
    basis = [mons[j] for j in free]
    if len(basis) != 2**n or max(map(sum, basis)) > n:
        raise ValueError(('unexpected Macaulay basis', basis))
    reds = {}
    for j, col in enumerate(free):
        reds[mons[col]] = [Q(int(i == j)) for i in range(len(free))]
    for i, col in enumerate(piv):
        reds[mons[col]] = [(-rr[i][j]) % prime if prime else -rr[i][j] for j in free]
    d = len(basis)
    # Use the last free state coordinate as t.
    tmon = tuple(int(i == n-1) for i in range(n))
    cols = [reds[tuple(a+b for a, b in zip(m, tmon))] for m in basis]
    mt = [[cols[j][i] for j in range(d)] for i in range(d)]
    vec = reds[(0,)*n]
    powers = [vec]
    for _ in range(d):
        powers.append(matvec(mt, powers[-1], prime))
    krylov = [[powers[j][i] for j in range(d)] for i in range(d)]
    co = solve(krylov, powers[d], prime)
    q = [(-v) % prime if prime else -v for v in co] + [Q(1)]
    gs = []
    for j in range(n):
        unit = tuple(int(i == j) for i in range(n))
        gs.append(solve(krylov, reds[unit], prime))
    return q, gs, {'macaulay_rows':len(rows), 'macaulay_columns':len(mons),
                   'rank':len(piv), 'basis':basis}


def trim(f):
    f = list(f)
    while f and not f[-1]:
        f.pop()
    return f


def uadd(f, g, prime=None):
    h = [0]*max(len(f), len(g))
    for a in range(len(h)):
        h[a] = (f[a] if a < len(f) else 0)+(g[a] if a < len(g) else 0)
        if prime:
            h[a] %= prime
    return trim(h)


def uscale(f, a, prime=None):
    return trim([x*a % prime if prime else x*a for x in f])


def umul(f, g, prime=None):
    h = [0]*(max(0, len(f)+len(g)-1))
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            h[i+j] += a*b
            if prime:
                h[i+j] %= prime
    return trim(h)


def urem(f, q, prime=None):
    f, q = trim(f), trim(q)
    while f and len(f) >= len(q):
        a = f[-1]*pow(q[-1], -1, prime) % prime if prime else Q(f[-1])/q[-1]
        shift = len(f)-len(q)
        for j, b in enumerate(q):
            f[shift+j] -= a*b
            if prime:
                f[shift+j] %= prime
        f = trim(f)
    return f


def upow(f, exponent, q, prime=None):
    ans = [1]
    while exponent:
        if exponent & 1:
            ans = urem(umul(ans, f, prime), q, prime)
        f = urem(umul(f, f, prime), q, prime)
        exponent >>= 1
    return ans


def ugcd(f, g, prime=None):
    f, g = trim(f), trim(g)
    while g:
        f, g = g, urem(f, g, prime)
    inv = pow(f[-1], -1, prime) if prime else 1/Q(f[-1])
    return uscale(f, inv, prime)


def irreducible_mod(q, prime):
    q = [Q(a).numerator*pow(Q(a).denominator, -1, prime) % prime for a in q]
    if not q[-1]:
        return False
    q = uscale(q, pow(q[-1], -1, prime), prime)
    n = len(q)-1
    x = [0, 1]
    # All degrees here are powers of two. Rabin's criterion has one gcd.
    assert n in (2,4,8)
    a = upow(x, prime**n, q, prime)
    b = upow(x, prime**(n//2), q, prime)
    return a == x and ugcd(q, uadd(b, uscale(x,-1,prime),prime),prime) == [1]


def sturm_sequence(q):
    q = [Q(a) for a in q]
    seq = [trim(q), [i*q[i] for i in range(1,len(q))]]
    while seq[-1]:
        rem = urem(seq[-2],seq[-1])
        if not rem:
            break
        seq.append(uscale(rem,-1))
    return seq


def ueval(q,t):
    ans = Q(0)
    for a in reversed(q):
        ans = ans*t+a
    return ans


def variations(seq,t):
    vals = [ueval(f,t) for f in seq]
    signs = [1 if a>0 else -1 for a in vals if a]
    return sum(a!=b for a,b in zip(signs,signs[1:]))


def interval_mul(a,b):
    prods = [x*y for x in a for y in b]
    return (min(prods),max(prods))


def interval_eval(g,ab):
    out = (Q(0),Q(0))
    for c in reversed(g):
        lo,hi = interval_mul(out,ab)
        out = (lo+c,hi+c)
    return out


def certify_simplex_interval(q,gs,ab):
    assert 0 < ab[0] < ab[1] < 1
    seq = sturm_sequence(q)
    counts = (variations(seq,ab[0]),variations(seq,ab[1]))
    assert counts[0]-counts[1] == 1
    intervals = [interval_eval(g,ab) for g in gs]
    intervals.append((1-sum(v[1] for v in intervals),1-sum(v[0] for v in intervals)))
    assert all(0 < lo <= hi < 1 for lo,hi in intervals)
    return counts, intervals


def rational_reconstruction(g,q,ndeg=3,ddeg=4):
    """A short rational function representing g modulo q, if one exists."""
    n = len(q)-1
    columns = []
    for j in range(ddeg+1):
        v = urem([0]*j+list(g),q)
        columns.append(v+[Q(0)]*(n-len(v)))
    for j in range(ndeg+1):
        columns.append([Q(-int(i==j)) for i in range(n)])
    matrix = [[c[i] for c in columns] for i in range(n)]
    rr,piv = rref(matrix)
    free = [j for j in range(len(columns)) if j not in piv]
    if not free:
        raise ValueError('no rational reconstruction')
    v = [Q(0)]*len(columns)
    v[free[0]] = 1
    for i,j in enumerate(piv):
        v[j] = -rr[i][free[0]]
    ints = primitive(v)
    den,num = trim(ints[:ddeg+1]),trim(ints[ddeg+1:])
    assert not urem(uadd(umul(den,g),uscale(num,-1)),q)
    assert ugcd(den,q) == [1]
    return num,den


def substitute(f, gs, q):
    out = []
    for mon, coeff in f.items():
        t = [coeff]
        for j, exponent in enumerate(mon):
            t = urem(umul(t, upow(gs[j], exponent, q)), q)
        out = uadd(out, t)
    return urem(out, q)


def detpoly(a):
    n = len(a)
    out = {}
    for perm in permutations(range(n)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1,n))
        term = {(0,)*n: Q(sign)}
        for i, j in enumerate(perm):
            term = mul(term, a[i][j])
        out = add(out, term)
    return out


def primitive(q):
    den = lcm(*(Q(a).denominator for a in q))
    nums = [int(a*den) for a in q]
    div = gcd(*nums)
    nums = [a//div for a in nums]
    return [-a for a in nums] if nums[-1] < 0 else nums


def random_rows(seed, ntypes=4):
    rng = random.Random(seed)
    rows = {}
    for i in range(ntypes):
        for j in range(i, ntypes):
            allowed = [k for k in range(ntypes) if k not in (i,j)]
            nums = [rng.randint(1,3) for _ in allowed]
            den = sum(nums)
            row = [Q(0)]*ntypes
            for k, a in zip(allowed, nums):
                row[k] = Q(a,den)
            rows[i,j] = row
    return rows


def degree8_rows():
    table = {
        '11':['0','2/5','2/5','1/5'],
        '12':['0','0','2/5','3/5'],
        '13':['0','1/2','0','1/2'],
        '14':['0','1/2','1/2','0'],
        '22':['1/3','0','1/2','1/6'],
        '23':['3/4','0','0','1/4'],
        '24':['2/3','0','1/3','0'],
        '33':['1/6','1/2','0','1/3'],
        '34':['1/2','1/2','0','0'],
        '44':['1/2','1/6','1/3','0'],
    }
    return {(int(s[0])-1,int(s[1])-1):list(map(Q,row)) for s,row in table.items()}


def degree4_rows():
    table = {
        '11':['0','1/2','1/2'],
        '12':['0','0','1'],
        '13':['0','1','0'],
        '22':['3/5','0','2/5'],
        '23':['1','0','0'],
        '33':['1/2','1/2','0'],
    }
    return {(int(s[0])-1,int(s[1])-1):list(map(Q,row)) for s,row in table.items()}


def quadratic_family_rows(a):
    rows = {}
    for i in range(4):
        for j in range(i,4):
            row = [Q(0)]*4
            if j < 3:
                row[3] = a
                active = [k for k in range(3) if k not in (i,j)]
                for k in active:
                    row[k] = (1-a)/len(active)
            else:
                active = [k for k in range(3) if k != i]
                for k in active:
                    row[k] = Q(1,len(active))
            rows[i,j] = row
    return rows


def verify_rur(rows, q, gs, prime, ntypes=4):
    fs = qso_system(rows, ntypes)
    assert len(q)-1 == 2**(ntypes-1)
    assert irreducible_mod(q,prime)
    assert trim(gs[-1]) == [0,1]
    for f in fs:
        assert not substitute(f,gs,q)
    d = detpoly([[derivative(f,j) for j in range(ntypes-1)] for f in fs])
    drem = substitute(d,gs,q)
    assert drem and ugcd(q,drem) == [1]
    return drem


def serialized(rows, q, gs, prime, data, drem):
    return {'rows':{str(i+1)+str(j+1):[str(a) for a in row]
                    for (i,j),row in rows.items()},
            'q_ascending_integer_coefficients':primitive(q),
            'coordinate_polynomials_ascending':[list(map(str,g)) for g in gs],
            'irreducibility_prime':prime,
            'jacobian_remainder_ascending':list(map(str,drem)),
            **data}


def search(ntypes=4):
    for seed in range(100):
        rows = random_rows(seed, ntypes)
        fs = qso_system(rows, ntypes)
        for prime in (5,7,11,13,17,19,23,29,31):
            try:
                q, gs, data = macaulay_rur(fs, prime)
                if irreducible_mod(q, prime):
                    print('FOUND',ntypes,seed,prime,flush=True)
                    q, gs, data = macaulay_rur(fs)
                    drem = verify_rur(rows,q,gs,prime,ntypes)
                    out = serialized(rows,q,gs,prime,data,drem)
                    out['seed'] = seed
                    print(json.dumps(out,indent=2),flush=True)
                    return out
            except (ValueError,ZeroDivisionError):
                continue
    raise ValueError('bounded search exhausted')


def verify_all():
    expected = {
        4:[22266087444,70025386176,-464892173868,-963347705904,
           312874547176,-273507556136,106485302812,-10697171526,79795739],
        3:[675,-900,-3150,-900,671],
    }
    brackets = {
        4:(Q(23940196,10**8),Q(23940197,10**8)),
        3:(Q(33331790,10**8),Q(33331791,10**8)),
    }
    all_data = {}
    for n,rows,prime in [(4,degree8_rows(),7),(3,degree4_rows(),13)]:
        assert rows == random_rows(0,n)
        if n == 4:
            assert all(a>0 for (i,j),row in rows.items()
                       for k,a in enumerate(row) if k not in (i,j))
        fs = qso_system(rows,n)
        q,gs,data = macaulay_rur(fs)
        assert primitive(q) == expected[n]
        drem = verify_rur(rows,q,gs,prime,n)
        counts,intervals = certify_simplex_interval(q,gs,brackets[n])
        out = serialized(rows,q,gs,prime,data,drem)
        out['isolating_interval'] = list(map(str,brackets[n]))
        out['sturm_variations_at_endpoints'] = counts
        state_box = []
        for lo,hi in intervals:
            low = (lo*10**6).numerator//(lo*10**6).denominator
            high = -((-hi*10**6).numerator//(-hi*10**6).denominator)
            state_box.append([str(Q(low,10**6)),str(Q(high,10**6))])
        out['state_enclosure'] = state_box
        qm = [a%prime for a in expected[n]]
        qm = uscale(qm,pow(qm[-1],-1,prime),prime)
        out['monic_mod_prime_ascending'] = qm
        out['half_frobenius_ascending'] = upow([0,1],prime**((len(q)-1)//2),qm,prime)
        out['full_frobenius_ascending'] = upow([0,1],prime**(len(q)-1),qm,prime)
        if n == 3:
            numerator,denominator = [15,0,-13],[30,30]
            assert not urem(uadd(umul(denominator,gs[0]),uscale(numerator,-1)),q)
            assert ugcd(q,denominator) == [1]
            # The linear combination 2 f_1+f_2 is the safe linear solve.
            one,x,y = {(0,0):Q(1)},{(1,0):Q(1)},{(0,1):Q(1)}
            rhs = add(scale(mul(x,add(one,y)),3),
                      add(scale(mul(y,y),Q(13,10)),scale(one,Q(-3,2))))
            assert add(scale(fs[0],2),fs[1]) == rhs
            out['short_x1_numerator_ascending'] = numerator
            out['short_x1_denominator_ascending'] = denominator
            # A complete four-type embedding, whose fourth output is zero.
            embedded = {ij:row+[Q(0)] for ij,row in rows.items()}
            for ij,k in [((0,3),1),((1,3),2),((2,3),0),((3,3),0)]:
                embedded[ij] = [Q(int(j==k)) for j in range(4)]
            embedded_fs = qso_system(embedded,4)
            g3 = uadd([1],uscale(uadd(gs[0],gs[1]),-1))
            assert all(not substitute(f,[gs[0],gs[1],g3],q) for f in embedded_fs)
            out['embedded_four_type_rows'] = {
                str(i+1)+str(j+1):list(map(str,row)) for (i,j),row in embedded.items()}
        all_data['degree_'+str(2**(n-1))] = out
        print('Verified degree',2**(n-1),': irreducible mod',prime,
              '; exact substitution; nonsingular roots; simplex interval',brackets[n])

    # A fully positive, S3-symmetric rational coefficient array of degree two.
    rows2 = quadratic_family_rows(Q(1,2))
    q2 = [1,-4,1]
    r = [Q(1,3),Q(-1,3)]
    assert irreducible_mod(q2,5)
    assert all(not substitute(f,[r,r,r],q2) for f in qso_system(rows2))
    assert all(a>0 for (i,j),row in rows2.items()
               for k,a in enumerate(row) if k not in (i,j))
    all_data['degree_2'] = {
        'rows':{str(i+1)+str(j+1):list(map(str,row)) for (i,j),row in rows2.items()},
        'x4_polynomial_ascending':q2,
        'x1_x2_x3_polynomial_in_x4_ascending':list(map(str,r)),
        'exact_x4':'2-sqrt(3)',
        'irreducibility_prime':5,
    }

    # Fully symmetric positive array: one simplex and four other real roots.
    rows1 = {(i,j):[Q(0) if k in (i,j) else Q(1,4-len({i,j})) for k in range(4)]
             for i in range(4) for j in range(i,4)}
    fs = qso_system(rows1)
    xs = coordinates(3)
    squares = sum_polys([mul(x,x) for x in xs])
    one = {(0,0,0):Q(1)}
    for i,f in enumerate(fs):
        rhs = add(scale(mul(xs[i],xs[i]),4),
                  add(scale(xs[i],-12),add(scale(one,3),scale(squares,-1))))
        assert not add(scale(f,6),rhs)
    rational_points = [[Q(1,4)]*4]+[[Q(4 if i==j else -1) for i in range(4)] for j in range(4)]
    for point in rational_points:
        gs = [[a] for a in point[:3]]
        assert all(not substitute(f,gs,[0,1]) for f in fs)
    all_data['degree_1'] = {
        'rows':{str(i+1)+str(j+1):list(map(str,row)) for (i,j),row in rows1.items()},
        'all_affine_fixed_points':[[str(a) for a in point] for point in rational_points],
        'all_points_at_infinity_up_to_sign':[[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]],
    }
    print('Verified the degree-two family witness and all five symmetric rational fixed points.')
    destination = Path(__file__).with_name('057_exact_certificates.json')
    destination.write_text(json.dumps(all_data,indent=2)+'\n')
    print('All exact coefficient, elimination, irreducibility, Jacobian, and root-isolation checks passed.')
    print('Certificate file:',destination)


if __name__ == '__main__':
    if len(sys.argv)>1:
        search(int(sys.argv[1]))
    else:
        verify_all()
