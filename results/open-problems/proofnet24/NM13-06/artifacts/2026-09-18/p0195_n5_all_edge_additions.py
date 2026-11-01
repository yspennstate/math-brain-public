from itertools import permutations, product
from functools import lru_cache
import sympy as sp

N = 5
x, L = sp.symbols('x L')
E = [(i,j) for i in range(N) for j in range(i+1,N)]
EI = {e:k for k,e in enumerate(E)}
PERMS = list(permutations(range(N)))
STATES = list(product((-1,1), repeat=N))
SI = {s:i for i,s in enumerate(STATES)}


def pmask(m,p):
    out = 0
    for k,(a,b) in enumerate(E):
        if (m>>k)&1:
            u,v = sorted((p[a],p[b]))
            out |= 1 << EI[(u,v)]
    return out


def pebit(k,p):
    a,b = E[k]
    u,v = sorted((p[a],p[b]))
    return EI[(u,v)]


def canon(m):
    return min(pmask(m,p) for p in PERMS)


def canon_marked(m,k):
    return min((pmask(m,p), pebit(k,p)) for p in PERMS)


@lru_cache(None)
def auts(m):
    return tuple(p for p in PERMS if pmask(m,p)==m)


def pst(s,p):
    t = [0]*N
    for i in range(N):
        t[p[i]] = s[i]
    return tuple(t)


def neg(s):
    return tuple(-a for a in s)


def orbit_pairs(m):
    A = auts(m)
    seen = set()
    ans = []
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
    else:
        raise ValueError(a)
    return sg*t


def edges(m):
    return [e for k,e in enumerate(E) if (m>>k)&1]


def Pmat(m):
    nbr = {i:[] for i in range(N)}
    for a,b in edges(m):
        nbr[a].append(b)
        nbr[b].append(a)
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
    return sp.factor(sp.Poly(num,L,domain=sp.QQ[x]).primitive()[1].as_expr())


def factors(q):
    return [sp.factor(f) for f,mul in sp.factor_list(q,L)[1] for _ in range(mul)]


def monic(f):
    return sp.Poly(f,L,domain=sp.QQ.frac_field(x)).monic()


def top_interval(f,xv,eps=sp.Rational(1,10**10)):
    p = sp.Poly(sp.cancel(f.subs(x,xv)),L,domain=sp.QQ)
    ints = p.intervals(eps=eps)
    assert sum(mult for _,mult in ints) == p.degree()
    (a,b),_ = ints[-1]
    return sp.Rational(a), sp.Rational(b)


def compare_top(f,g,xv):
    eps = sp.Rational(1,10**5)
    for _ in range(12):
        a,b = top_interval(f,xv,eps)
        c,d = top_interval(g,xv,eps)
        if a > d:
            return 1
        if c > b:
            return -1
        if a == b == c == d:
            return 0
        eps /= 100
    raise AssertionError(('root separation failed', xv, a,b,c,d))


def resultant_roots_01(f,g):
    if monic(f) == monic(g):
        return []
    r = sp.Poly(sp.resultant(f,g,L),x,domain=sp.QQ)
    assert not r.is_zero
    # Multiplicity is irrelevant for partitioning (0,1); square-free first
    # makes the ubiquitous x=0 and occasional x=1 endpoint factors cheap.
    r = r.sqf_part()
    if r.degree() > 0 and r.eval(0) == 0:
        r = sp.Poly(sp.cancel(r.as_expr()/x), x, domain=sp.QQ)
    if r.degree() > 0 and r.eval(1) == 0:
        r = sp.Poly(sp.cancel(r.as_expr()/(x-1)), x, domain=sp.QQ)
    if r.degree() <= 0:
        return []
    ans = []
    for (a,b),mult in r.intervals(eps=sp.Rational(1,10**6)):
        a,b = sp.Rational(a), sp.Rational(b)
        if b <= 0 or a >= 1:
            continue
        if a <= 0 or b >= 1:
            a,b = map(sp.Rational, r.refine_root(a,b,eps=sp.Rational(1,10**12)))
        if 0 < a and b < 1:
            ans.append((a,b,mult))
    return ans


def certify_ge_01(f,g):
    if monic(f) == monic(g):
        return True, [], [sp.Rational(1,2)], [0]
    roots = resultant_roots_01(f,g)
    samples = []
    left = sp.Rational(0)
    for a,b,_ in roots:
        samples.append((left+a)/2)
        left = b
    samples.append((left+1)/2)
    signs = [compare_top(f,g,s) for s in samples]
    return min(signs) >= 0, roots, samples, signs


CANONS = sorted(set(canon(m) for m in range(1<<len(E))))
MARKED = sorted({canon_marked(m,k)
                 for m in range(1<<len(E))
                 for k in range(len(E)) if not ((m>>k)&1)})
assert len(CANONS) == 34
assert len(MARKED) == 74
print('canonical_graph_classes', len(CANONS))
print('marked_edge_addition_types', len(MARKED))

# For each unlabeled endpoint graph, identify and rigorously certify the factor
# carrying the largest eigenvalue in the odd Aut(G)-invariant quotient for all
# x in (0,1).  By LPW Lemma 22.17 plus spin-flip and automorphism averaging,
# this quotient contains the true second eigenvalue of the full heat-bath chain.
TOP = {}
top_factor_degrees = {}
for m in CANONS:
    fs = factors(qpoly(m))
    best = fs[0]
    for f in fs[1:]:
        if compare_top(f,best,sp.Rational(1,2)) > 0:
            best = f
    for f in fs:
        if monic(f) == monic(best):
            continue
        ok,roots,samples,signs = certify_ge_01(best,f)
        assert ok, ('endpoint top-factor failure',m,sp.factor(best),sp.factor(f),roots,signs)
    TOP[m] = best
    top_factor_degrees[m] = sp.Poly(best,L).degree()
print('endpoint_top_factors_certified', len(TOP))
print('endpoint_top_factor_max_degree', max(top_factor_degrees.values()))

# Certify every marked isomorphism type of a single missing-edge addition.
# For x=tanh(beta) in (0,1), the target second eigenvalue must be at least the
# source second eigenvalue; x=0 (beta=0) is exact equality for every graph.
tie_types = []
max_interior_resultant_roots = 0
sum_interior_resultant_roots = 0
for idx,(s,k) in enumerate(MARKED):
    t = canon(s | (1<<k))
    ok,roots,samples,signs = certify_ge_01(TOP[t],TOP[s])
    assert ok, ('edge monotonicity failure',idx,s,k,t,roots,signs)
    if monic(TOP[t]) == monic(TOP[s]):
        tie_types.append((s,k,t))
    max_interior_resultant_roots = max(max_interior_resultant_roots, len(roots))
    sum_interior_resultant_roots += len(roots)
    print('transition', idx, s, k, t, 'PASS',
          'interior_resultant_roots', len(roots),
          'interval_signs', ','.join(map(str,signs)))

assert tie_types == [(1,7,20),(3,9,28),(19,9,184)]
print('all_temperature_tie_types', tie_types)
print('max_interior_resultant_roots', max_interior_resultant_roots)
print('sum_interior_resultant_roots', sum_interior_resultant_roots)
print('metric_certificate', 'n_edge^* >= 6')
print('ALL_EXACT_CHECKS_PASS')
