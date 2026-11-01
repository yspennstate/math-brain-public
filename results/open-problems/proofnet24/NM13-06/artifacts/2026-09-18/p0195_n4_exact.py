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
        if min(O) <= min(N):
            ans.append((O,N))
        else:
            ans.append((N,O))
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
            t = list(s)
            t[v] = 1
            P[ii,SI[tuple(t)]] += pp/4
            t = list(s)
            t[v] = -1
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
    ex = sp.together(Q.charpoly(L).as_expr()).as_numer_denom()[0]
    prim = sp.Poly(ex, L, domain=sp.QQ[z]).primitive()[1].as_expr()
    return sp.factor(prim)


def topint(f, zv, eps):
    q = sp.Poly(f.subs(z,zv), L, domain=sp.QQ)
    ints = q.intervals(eps=eps)
    assert sum(m for _,m in ints) == q.degree()
    (a,b),_ = ints[-1]
    return sp.Rational(a), sp.Rational(b)


def cmp(f, g, zv):
    eps = sp.Rational(1,10)
    for _ in range(20):
        a,b = topint(f,zv,eps)
        c,d = topint(g,zv,eps)
        if a > d:
            return 1
        if c > b:
            return -1
        if a == b == c == d:
            return 0
        eps /= 100
    raise Exception('overlap')


def factors(q):
    return [(sp.factor(f),m) for f,m in sp.factor_list(q,L)[1]]


def cand(q):
    fs = factors(q)
    best = fs[0][0]
    for f,m in fs[1:]:
        if cmp(f,best,sp.Rational(2)) > 0:
            best = f
    return best


def samples_res(f, g):
    r = sp.Poly(sp.resultant(f,g,L), z, domain=sp.QQ)
    if r.is_zero:
        return None
    d = sp.Poly(z-1, z, domain=sp.QQ)
    while r.eval(1) == 0:
        r = r.exquo(d)
    ints = r.intervals(eps=sp.Rational(1,10**5)) if r.degree() > 0 else []
    roots = []
    for (a,b),m in ints:
        a,b = sp.Rational(a),sp.Rational(b)
        if a > 1:
            roots.append((a,b,m))
    left = sp.Rational(1)
    ss = []
    for a,b,m in roots:
        ss.append((left+a)/2)
        left = b
    ss.append(left+1)
    return roots, ss


def ge(f, g):
    if sp.Poly(f,L,domain=sp.QQ.frac_field(z)).monic() == sp.Poly(g,L,domain=sp.QQ.frac_field(z)).monic():
        return True,0,1
    rr = samples_res(f,g)
    if rr is None:
        return True,0,0
    roots,ss = rr
    cs = [cmp(f,g,s) for s in ss]
    return min(cs) >= 0, len(roots), len(ss)


Q = [qpoly(m) for m in CAN]
C = [cand(q) for q in Q]
print('classes',len(CAN),[(i,m,m.bit_count(),sp.degree(C[i],L)) for i,m in enumerate(CAN)])
for i,q in enumerate(Q):
    for f,m in factors(q):
        if sp.Poly(f,L,domain=sp.QQ.frac_field(z)).monic() == sp.Poly(C[i],L,domain=sp.QQ.frac_field(z)).monic():
            continue
        ok,nr,ns = ge(C[i],f)
        assert ok,(i,f)
    print('dominance',i,'PASS')

TRANS = sorted({
    (IDX[m],IDX[canon(m|(1<<k))])
    for m in CAN for k in range(6) if not ((m>>k)&1)
})
print('trans',TRANS)
for i,j in TRANS:
    ok,nr,ns = ge(C[j],C[i])
    assert ok,(i,j)
    print('edge',i,j,'PASS',nr,ns)
print('ALL_EXACT_CHECKS_PASS')
