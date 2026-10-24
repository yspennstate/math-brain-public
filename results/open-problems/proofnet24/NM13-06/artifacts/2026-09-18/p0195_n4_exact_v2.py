from itertools import permutations, product
import sympy as sp

z, L = sp.symbols('z L')
E = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
EI = {e:i for i,e in enumerate(E)}
PERMS = list(permutations(range(4)))
STATES = list(product((-1,1), repeat=4))
SI = {s:i for i,s in enumerate(STATES)}


def pmask(m, p):
    out = 0
    for k, (a,b) in enumerate(E):
        if (m >> k) & 1:
            x, y = sorted((p[a], p[b]))
            out |= 1 << EI[(x,y)]
    return out


def canon(m):
    return min(pmask(m,p) for p in PERMS)


CAN = sorted({canon(m) for m in range(64)}, key=lambda m:(m.bit_count(),m))
IDX = {m:i for i,m in enumerate(CAN)}
assert len(CAN) == 11


def auts(m):
    return [p for p in PERMS if pmask(m,p) == m]


def pst(s, p):
    t = [0]*4
    for i in range(4):
        t[p[i]] = s[i]
    return tuple(t)


def neg(s):
    return tuple(-x for x in s)


def orbit_pairs(m):
    A = auts(m)
    seen = set()
    ans = []
    for s in STATES:
        if s in seen:
            continue
        O = {pst(s,p) for p in A}
        N = {neg(t) for t in O}
        seen |= O | N
        if O == N:
            continue
        ans.append((O,N) if min(O) <= min(N) else (N,O))
    return ans


def edges(m):
    return [e for k,e in enumerate(E) if (m >> k) & 1]


def Pmat(m):
    nbr = {i:[] for i in range(4)}
    for a,b in edges(m):
        nbr[a].append(b)
        nbr[b].append(a)
    P = sp.zeros(16)
    for ii,s in enumerate(STATES):
        for v in range(4):
            h = sum(s[w] for w in nbr[v])
            pp = sp.cancel(z**h/(1+z**h))
            t = list(s); t[v] = 1
            P[ii,SI[tuple(t)]] += pp/4
            t = list(s); t[v] = -1
            P[ii,SI[tuple(t)]] += (1-pp)/4
    return P


def qpoly(m):
    P = Pmat(m)
    pairs = orbit_pairs(m)
    reps = [min(O) for O,N in pairs]
    Q = sp.zeros(len(pairs))
    for i,r in enumerate(reps):
        for j,(O,N) in enumerate(pairs):
            Q[i,j] = sp.cancel(
                sum(P[SI[r],SI[t]] for t in O)
                - sum(P[SI[r],SI[t]] for t in N)
            )
    num = sp.together(Q.charpoly(L).as_expr()).as_numer_denom()[0]
    return sp.factor(sp.Poly(num, L, domain=sp.QQ[z]).primitive()[1].as_expr())


def factors(q):
    return [sp.factor(f) for f,m in sp.factor_list(q,L)[1] for _ in range(m)]


def top_interval(f, zv, eps=sp.Rational(1,10**8)):
    q = sp.Poly(f.subs(z,zv), L, domain=sp.QQ)
    ints = q.intervals(eps=eps)
    # For every factor used below all roots are certified real at every sample.
    assert sum(m for _,m in ints) == q.degree(), (f,zv,ints)
    (a,b), mult = ints[-1]
    return sp.Rational(a), sp.Rational(b)


def compare_top(f, g, zv):
    eps = sp.Rational(1,10**4)
    for _ in range(12):
        a,b = top_interval(f,zv,eps)
        c,d = top_interval(g,zv,eps)
        if a > d:
            return 1
        if c > b:
            return -1
        if a == b == c == d:
            return 0
        eps /= 100
    raise AssertionError(('root intervals failed to separate',f,g,zv,a,b,c,d))


def monic_over_Qz(f):
    return sp.Poly(f,L,domain=sp.QQ.frac_field(z)).monic()


def top_factor(q):
    fs = factors(q)
    best = fs[0]
    for f in fs[1:]:
        if compare_top(f,best,sp.Rational(2)) > 0:
            best = f
    return best


def positive_resultant_root_intervals(f,g):
    if monic_over_Qz(f) == monic_over_Qz(g):
        return []
    r = sp.Poly(sp.resultant(f,g,L), z, domain=sp.QQ)
    assert not r.is_zero, ('unexpected common factor',f,g)
    d = sp.Poly(z-1,z,domain=sp.QQ)
    while r.eval(1) == 0:
        r = r.exquo(d)
    if r.degree() <= 0:
        return []
    raw = r.intervals(eps=sp.Rational(1,10**10))
    ans = []
    for (a,b), mult in raw:
        a,b = sp.Rational(a), sp.Rational(b)
        if b <= 1:
            continue
        if a <= 1:
            # z=1 is not a root after division. Refine until the interval lies
            # strictly on one side of 1; retain it iff it lies to the right.
            a,b = map(sp.Rational, r.refine_root(a,b,eps=sp.Rational(1,10**20)))
            if b <= 1:
                continue
            assert a > 1, (r,a,b)
        ans.append((a,b,mult))
    return ans


def comparison_samples(f,g):
    roots = positive_resultant_root_intervals(f,g)
    samples = []
    left = sp.Rational(1)
    for a,b,m in roots:
        assert left < a
        samples.append((left+a)/2)
        left = b
    samples.append(left+1)
    return roots,samples


def certify_ge(f,g):
    if monic_over_Qz(f) == monic_over_Qz(g):
        return True, [], [sp.Rational(2)], [0]
    roots,samples = comparison_samples(f,g)
    signs = [compare_top(f,g,s) for s in samples]
    return min(signs) >= 0, roots, samples, signs


Q = [qpoly(m) for m in CAN]
TOP = [top_factor(q) for q in Q]
print('classes',len(CAN),[(i,m,m.bit_count(),len(orbit_pairs(m)),sp.degree(TOP[i],L)) for i,m in enumerate(CAN)])

# Certify that the selected factor carries the largest root of the entire odd,
# automorphism-invariant quotient for every z>1.
for i,q in enumerate(Q):
    for f in factors(q):
        if monic_over_Qz(f) == monic_over_Qz(TOP[i]):
            continue
        ok,roots,samples,signs = certify_ge(TOP[i],f)
        assert ok,(i,f,roots,samples,signs)
    print('dominance',i,'PASS')

TRANS = sorted({
    (IDX[m],IDX[canon(m|(1<<k))])
    for m in CAN for k in range(6) if not ((m>>k)&1)
})
assert len(TRANS) == 14
print('trans',TRANS)

# Edge addition decreases the spectral gap iff it increases lambda_2.  For each
# isomorphism transition certify maxroot(TOP[target]) >= maxroot(TOP[source])
# throughout z>1, partitioning only at exact resultant roots.
for i,j in TRANS:
    ok,roots,samples,signs = certify_ge(TOP[j],TOP[i])
    assert ok,(i,j,roots,samples,signs)
    print('edge',i,j,'PASS','resultant_roots_gt1',len(roots),'regions',len(samples),'signs',signs)

print('ALL_EXACT_CHECKS_PASS')
