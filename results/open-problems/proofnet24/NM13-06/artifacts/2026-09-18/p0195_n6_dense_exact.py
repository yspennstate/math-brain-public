from itertools import permutations, product
import sys
from functools import lru_cache
import sympy as sp

N = 6
x, L = sp.symbols('x L')
E = [(i,j) for i in range(N) for j in range(i+1,N)]
EI = {e:k for k,e in enumerate(E)}
PERMS = list(permutations(range(N)))
STATES = list(product((-1,1), repeat=N))
SI = {s:i for i,s in enumerate(STATES)}
FULL = (1 << len(E)) - 1

# Three marked isomorphism types with >=13 source edges:
# complement 2K2, complement P3, complement K2.
CASES = [
    (30591, (1,4), 'complement_2K2_to_K2'),
    (22527, (2,5), 'complement_P3_to_K2'),
    (32763, (0,3), 'complement_K2_to_empty'),
]


def pmask(m,p):
    out = 0
    for k,(a,b) in enumerate(E):
        if (m >> k) & 1:
            u,v = sorted((p[a],p[b]))
            out |= 1 << EI[(u,v)]
    return out


@lru_cache(None)
def auts(m):
    return tuple(p for p in PERMS if pmask(m,p) == m)


def pst(s,p):
    t = [0]*N
    for i in range(N):
        t[p[i]] = s[i]
    return tuple(t)


def neg(s):
    return tuple(-a for a in s)


def orbit_pairs(m):
    A = auts(m)
    seen, ans = set(), []
    for s in STATES:
        if s in seen:
            continue
        O = {pst(s,p) for p in A}
        M = {neg(t) for t in O}
        seen |= O | M
        if O == M:
            continue
        ans.append((O,M) if min(O) <= min(M) else (M,O))
    return ans


def tanh_mult(h):
    if h == 0:
        return sp.Integer(0)
    sg = 1 if h > 0 else -1
    a = abs(h)
    if a == 1:
        t = x
    elif a == 2:
        t = 2*x/(1+x**2)
    elif a == 3:
        t = (3*x+x**3)/(1+3*x**2)
    elif a == 4:
        t = 4*x*(1+x**2)/(1+6*x**2+x**4)
    elif a == 5:
        t = (5*x+10*x**3+x**5)/(1+10*x**2+5*x**4)
    else:
        raise ValueError(a)
    return sg*t


def edges(m):
    return [e for k,e in enumerate(E) if (m >> k) & 1]


def Pmat(m):
    nbr = {i:[] for i in range(N)}
    for a,b in edges(m):
        nbr[a].append(b); nbr[b].append(a)
    P = sp.zeros(2**N)
    for ii,s in enumerate(STATES):
        for v in range(N):
            h = sum(s[w] for w in nbr[v])
            pp = sp.cancel((1+tanh_mult(h))/2)
            t = list(s); t[v] = 1
            P[ii, SI[tuple(t)]] += pp/N
            t = list(s); t[v] = -1
            P[ii, SI[tuple(t)]] += (1-pp)/N
    return P


@lru_cache(None)
def qpoly(m):
    P = Pmat(m)
    pairs = orbit_pairs(m)
    reps = [min(O) for O,M in pairs]
    Q = sp.zeros(len(pairs))
    for i,r in enumerate(reps):
        for j,(O,M) in enumerate(pairs):
            Q[i,j] = sp.cancel(
                sum(P[SI[r],SI[t]] for t in O)
                - sum(P[SI[r],SI[t]] for t in M)
            )
    num = sp.together(Q.charpoly(L).as_expr()).as_numer_denom()[0]
    poly = sp.Poly(num, L, domain=sp.QQ[x]).primitive()[1]
    return sp.factor(poly.as_expr())


def top_interval(f,xv,eps=sp.Rational(1,10**10)):
    p = sp.Poly(sp.cancel(f.subs(x,xv)),L,domain=sp.QQ)
    ints = p.intervals(eps=eps)
    assert sum(mult for _,mult in ints) == p.degree()
    (a,b),_ = ints[-1]
    return sp.Rational(a), sp.Rational(b)


def compare_top(f,g,xv):
    eps = sp.Rational(1,10**6)
    for _ in range(15):
        a,b = top_interval(f,xv,eps)
        c,d = top_interval(g,xv,eps)
        if a > d:
            return 1
        if c > b:
            return -1
        if a == b == c == d:
            return 0
        eps /= 100
    raise AssertionError(('root separation failed',xv,a,b,c,d))


def resultant_roots_01(f,g):
    r = sp.Poly(sp.resultant(f,g,L),x,domain=sp.QQ).sqf_part()
    while r.degree() > 0 and r.eval(0) == 0:
        r = sp.Poly(sp.cancel(r.as_expr()/x),x,domain=sp.QQ)
    while r.degree() > 0 and r.eval(1) == 0:
        r = sp.Poly(sp.cancel(r.as_expr()/(x-1)),x,domain=sp.QQ)
    roots = []
    if r.degree() <= 0:
        return r, roots
    for (a,b),mult in r.intervals(eps=sp.Rational(1,10**7)):
        a,b = sp.Rational(a), sp.Rational(b)
        if b <= 0 or a >= 1:
            continue
        if a <= 0 or b >= 1:
            a,b = map(sp.Rational, r.refine_root(a,b,eps=sp.Rational(1,10**12)))
        if 0 < a and b < 1:
            roots.append((a,b,mult))
    return r, roots


def certify_ge_01(target, source):
    r, roots = resultant_roots_01(target, source)
    samples = []
    left = sp.Rational(0)
    for a,b,_ in roots:
        samples.append((left+a)/2)
        left = b
    samples.append((left+1)/2)
    signs = [compare_top(target,source,s) for s in samples]
    assert min(signs) >= 0
    return r.degree(), roots, samples, signs

# Exact finite classification of the relevant marked graph types.
# For a 6-vertex graph with >=13 edges, its complement has 0,1,2 edges.
# If an edge is missing, the source complement is K2, P3, or 2K2;
# within each type all missing edges are automorphism-equivalent.
selected = CASES if len(sys.argv) < 2 else [c for c in CASES if c[2] == sys.argv[1]]
assert selected
for source, e, label in selected:
    k = EI[tuple(sorted(e))]
    assert not ((source >> k) & 1)
    target = source | (1 << k)
    missing = [ee for kk,ee in enumerate(E) if not ((source >> kk) & 1)]
    print('case', label, 'source_mask', source, 'target_mask', target,
          'source_edges', source.bit_count(), 'missing', missing,
          'aut_source', len(auts(source)), 'odd_dim_source', len(orbit_pairs(source)),
          'aut_target', len(auts(target)), 'odd_dim_target', len(orbit_pairs(target)))

    fs = qpoly(source)
    ft = qpoly(target)
    # In each of these highly symmetric cases the odd quotient characteristic
    # polynomial is irreducible over Q(x), so its largest real root is the top
    # odd-quotient eigenvalue, which equals lambda_2 by the monotone-eigenfunction
    # plus spin-flip/automorphism-averaging lemma used in the track proof.
    sf = sp.factor_list(fs,L)[1]
    tf = sp.factor_list(ft,L)[1]
    assert len(sf) == 1 and sf[0][1] == 1
    assert len(tf) == 1 and tf[0][1] == 1
    print('degrees', sp.Poly(fs,L).degree(), sp.Poly(ft,L).degree())

    # Method #29 diagnostic: compactify the temperature parameter by x=1.
    # The zero-temperature boundary is not part of the finite-beta theorem,
    # but exact specialization shows the slow mode degenerates to lambda=1
    # on both endpoints. This explains the tiny positive margins near x=1
    # without using the boundary point to prove the interior inequality.
    for which, poly in [('source', fs), ('target', ft)]:
        q1 = sp.factor(poly.subs(x, 1))
        ints1 = sp.Poly(q1, L, domain=sp.QQ).intervals(eps=sp.Rational(1,10**12))
        (ta,tb), _ = ints1[-1]
        ta, tb = sp.Rational(ta), sp.Rational(tb)
        assert ta == 1 and tb == 1
        div1, rem1 = sp.div(sp.Poly(q1,L,domain=sp.QQ), sp.Poly(L-1,L,domain=sp.QQ))
        assert rem1.is_zero and div1.eval(1) != 0
        print('x1_boundary', which, 'top_root', 1, 'L_minus_1_multiplicity', 1,
              'factorization', q1)

    rdeg, roots, samples, signs = certify_ge_01(ft,fs)
    print('resultant_degree_after_endpoint_removal', rdeg)
    print('interior_resultant_roots', len(roots))
    print('interval_signs', signs)
    print('PASS', label)

print('theorem_scope', 'all 6-vertex simple graphs with at least 13 edges, every absent edge, every finite beta>=0')
print('metric', 'n_edge^* remains >= 6 (restricted-class theorem; not full n=6 coverage)')
print('ALL_EXACT_CHECKS_PASS')
