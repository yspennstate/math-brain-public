from itertools import permutations, product, combinations
from functools import lru_cache
from math import comb, atanh
import sympy as sp
import numpy as np

N = 6
x, L, t, y = sp.symbols('x L t y')
EDGES = list(combinations(range(N), 2))
EIDX = {e:i for i,e in enumerate(EDGES)}
PERMS = list(permutations(range(N)))
STATES = list(product((-1,1), repeat=N))
SI = {s:i for i,s in enumerate(STATES)}
G_MASK = 4095
ADD_EDGE = (3,4)
H_MASK = G_MASK | (1 << EIDX[ADD_EDGE])
assert G_MASK.bit_count() == 12 and H_MASK.bit_count() == 13

def pmask(m,p):
    out = 0
    for k,(a,b) in enumerate(EDGES):
        if (m >> k) & 1:
            u,v = sorted((p[a],p[b]))
            out |= 1 << EIDX[(u,v)]
    return out

@lru_cache(None)
def auts(m):
    return tuple(p for p in PERMS if pmask(m,p) == m)

def pst(s,p):
    q = [0]*N
    for i in range(N):
        q[p[i]] = s[i]
    return tuple(q)

def neg(s):
    return tuple(-a for a in s)

def orbit_pairs(m):
    A = auts(m)
    seen, ans = set(), []
    for s in STATES:
        if s in seen:
            continue
        O = {pst(s,p) for p in A}
        M = {neg(u) for u in O}
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
        z = x
    elif a == 2:
        z = 2*x/(1+x**2)
    elif a == 3:
        z = (3*x+x**3)/(1+3*x**2)
    elif a == 4:
        z = 4*x*(1+x**2)/(1+6*x**2+x**4)
    elif a == 5:
        z = (5*x+10*x**3+x**5)/(1+10*x**2+5*x**4)
    else:
        raise ValueError(a)
    return sg*z

def edge_list(m):
    return [e for k,e in enumerate(EDGES) if (m >> k) & 1]

def pmat(m):
    nbr = {i:[] for i in range(N)}
    for a,b in edge_list(m):
        nbr[a].append(b); nbr[b].append(a)
    P = sp.zeros(2**N)
    for ii,s in enumerate(STATES):
        for v in range(N):
            h = sum(s[w] for w in nbr[v])
            pp = sp.cancel((1+tanh_mult(h))/2)
            q = list(s); q[v] = 1
            P[ii,SI[tuple(q)]] += pp/N
            q = list(s); q[v] = -1
            P[ii,SI[tuple(q)]] += (1-pp)/N
    return P

def odd_quotient_poly(m):
    P = pmat(m)
    pairs = orbit_pairs(m)
    reps = [min(O) for O,M in pairs]
    Q = sp.zeros(len(pairs))
    for i,r in enumerate(reps):
        for j,(O,M) in enumerate(pairs):
            Q[i,j] = sp.cancel(sum(P[SI[r],SI[u]] for u in O) - sum(P[SI[r],SI[u]] for u in M))
    num = sp.together(Q.charpoly(L).as_expr()).as_numer_denom()[0]
    f = sp.Poly(num, L, domain=sp.QQ[x]).primitive()[1]
    return Q, sp.factor(f.as_expr())

def bernstein_coeffs_interval(poly_t, a=sp.Rational(1,10)):
    n = poly_t.degree()
    q = sp.Poly(sp.expand(poly_t.as_expr().subs(t,a*y)), y, domain=sp.QQ)
    c = [q.nth(j) for j in range(n+1)]
    out = []
    for k in range(n+1):
        b = sp.Rational(0)
        for j in range(k+1):
            b += c[j] * sp.Rational(comb(k,j), comb(n,j))
        out.append(sp.factor(b))
    return out

def sign_certificate(expr, wanted):
    p = sp.Poly(sp.expand(expr), t, domain=sp.QQ)
    b = bernstein_coeffs_interval(p)
    if wanted == 'positive':
        assert all(v > 0 for v in b)
    elif wanted == 'negative':
        assert all(v < 0 for v in b)
    else:
        raise ValueError(wanted)
    return p.degree(), min(b), max(b)

QG, fG = odd_quotient_poly(G_MASK)
QH, fH = odd_quotient_poly(H_MASK)
assert QG.rows == 8 and QH.rows == 12
assert sp.Poly(fG,L).degree() == 8 and sp.Poly(fH,L).degree() == 12
facG1 = sp.factor(fG.subs(x,1))
facH1 = sp.factor(fH.subs(x,1))
expectedG1 = sp.factor(9674588160000*L*(L-1)*(3*L-2)**2*(6*L-5)**2*(6*L-1)**2)
expectedH1 = sp.factor(178322008965120000*L*(L-1)*(3*L-2)**3*(6*L-5)**3*(72*L**2-66*L+13)*(72*L**2-30*L+1))
assert sp.expand(facG1-expectedG1) == 0
assert sp.expand(facH1-expectedH1) == 0
for qpoly in [72*L**2-66*L+13, 72*L**2-30*L+1]:
    roots = sp.solve(sp.Eq(qpoly,0), L)
    assert all(sp.simplify(r < sp.Rational(9,10)) is sp.S.true for r in roots)
deg_G_09, min_G_09, max_G_09 = sign_certificate(fG.subs({x:1-t, L:sp.Rational(9,10)}), 'negative')
deg_H_09, min_H_09, max_H_09 = sign_certificate(fH.subs({x:1-t, L:sp.Rational(9,10)}), 'negative')
barrier = 1 - t**7/sp.Integer(32)
assert sp.simplify(barrier.subs(t,sp.Rational(1,10)) > sp.Rational(9,10)) is sp.S.true
exprG = sp.expand(fG.subs({x:1-t, L:barrier}))
exprH = sp.expand(fH.subs({x:1-t, L:barrier}))
polyG = sp.Poly(exprG, t, domain=sp.QQ)
polyH = sp.Poly(exprH, t, domain=sp.QQ)
ordG = min(k[0] for k,v in polyG.terms())
ordH = min(k[0] for k,v in polyH.terms())
assert ordG == ordH == 7
redG = sp.cancel(exprG/t**7)
redH = sp.cancel(exprH/t**7)
deg_G_bar, min_G_bar, max_G_bar = sign_certificate(redG, 'positive')
deg_H_bar, min_H_bar, max_H_bar = sign_certificate(redH, 'negative')

def leading_gap_coefficient(f):
    p = sp.Poly(sp.expand(f.subs({x:1-t,L:1})), t, domain=sp.QQ)
    order = min(k[0] for k,v in p.terms())
    coeff = p.nth(order)
    dL = sp.diff(f,L).subs({x:1,L:1})
    return order, sp.factor(coeff/dL)

leadG = leading_gap_coefficient(fG)
leadH = leading_gap_coefficient(fH)
assert leadG == (7, sp.Rational(9,160))
assert leadH == (7, sp.Rational(9,608))
assert sp.Rational(9,608) < sp.Rational(1,32) < sp.Rational(9,160)
assert sp.Rational(9,160)-sp.Rational(9,608) == sp.Rational(63,1520)

PMAPS = []
for p in PERMS:
    mp=[]
    for u,v in EDGES:
        a,b=sorted((p[u],p[v])); mp.append(EIDX[(a,b)])
    PMAPS.append(tuple(mp))

def transform(mask,mp):
    out=0
    for i,j in enumerate(mp):
        if (mask>>i)&1: out |= 1<<j
    return out

def connected(mask):
    adj=[0]*N
    for i,(u,v) in enumerate(EDGES):
        if (mask>>i)&1:
            adj[u] |= 1<<v; adj[v] |= 1<<u
    seen=front=1
    while front:
        nxt=0
        for v in range(N):
            if (front>>v)&1: nxt |= adj[v]
        nxt &= ~seen; seen |= nxt; front=nxt
    return seen==(1<<N)-1

def graph_representatives():
    seen=set(); reps=[]
    for mask in range(1<<len(EDGES)):
        if mask in seen: continue
        orb={transform(mask,mp) for mp in PMAPS}
        seen |= orb; reps.append(mask)
    assert len(reps)==156
    return reps

@lru_cache(None)
def aut_maps(mask):
    return tuple(mp for mp in PMAPS if transform(mask,mp)==mask)

def missing_edge_orbit_reps(mask):
    aut=aut_maps(mask)
    missing=[i for i in range(len(EDGES)) if not((mask>>i)&1)]
    seen=set(); reps=[]
    for i in missing:
        if i in seen: continue
        orb={mp[i] for mp in aut}; seen |= orb; reps.append(min(orb))
    assert seen==set(missing)
    return reps

def lambda2_numeric(mask, xval=0.5):
    beta = atanh(xval)
    es = edge_list(mask)
    nbr=[[] for _ in range(N)]
    for a,b in es:
        nbr[a].append(b); nbr[b].append(a)
    P=np.zeros((64,64),dtype=float)
    energy=np.zeros(64,dtype=float)
    for ii,s in enumerate(STATES):
        energy[ii]=sum(s[a]*s[b] for a,b in es)
        for v in range(N):
            h=sum(s[w] for w in nbr[v])
            pp=(1+np.tanh(beta*h))/2
            q=list(s); q[v]=1
            P[ii,SI[tuple(q)]] += pp/N
            q=list(s); q[v]=-1
            P[ii,SI[tuple(q)]] += (1-pp)/N
    w=np.exp(beta*energy); pi=w/w.sum()
    S=(np.sqrt(pi)[:,None]*P)/np.sqrt(pi)[None,:]
    S=(S+S.T)/2
    return np.linalg.eigvalsh(S)[-2]

conn=[m for m in graph_representatives() if connected(m)]
assert len(conn)==112
records=[]
for m in conn:
    ls=lambda2_numeric(m)
    for ei in missing_edge_orbit_reps(m):
        lt=lambda2_numeric(m|(1<<ei))
        records.append((lt-ls,m,ei,EDGES[ei],m.bit_count(),ls,lt))
assert len(records)==402
minimum=min(records,key=lambda r:r[0])
unresolved=[r for r in records if r[4] <= 12]
minimum_unresolved=min(unresolved,key=lambda r:r[0])
assert minimum[0] > 0 and minimum_unresolved[0] > 0

print('source_mask',G_MASK,'target_mask',H_MASK,'source_edges',G_MASK.bit_count(),'target_edges',H_MASK.bit_count())
print('odd_quotient_dimensions',QG.rows,QH.rows)
print('x1_factor_G',facG1)
print('x1_factor_H',facH1)
print('threshold_09_bernstein',{'G_degree':deg_G_09,'G_max':max_G_09,'H_degree':deg_H_09,'H_max':max_H_09})
print('barrier','1-t^7/32','t_interval','[0,1/10]')
print('barrier_bernstein',{'G_degree':deg_G_bar,'G_min':min_G_bar,'H_degree':deg_H_bar,'H_max':max_H_bar})
print('gap_leading_terms',{'G':leadG,'H':leadH,'difference_coefficient':sp.Rational(63,1520)})
print('proved_tail','tanh(beta)>=9/10 equivalently beta>=atanh(9/10)=1/2*log(19)')
print('proved_comparison','lambda2(H)>lambda2(G), hence gap(H)<gap(G), for every finite beta>=1/2*log(19)')
print('typical_x_half_diagnostic_only',{'marked_types':len(records),'min_lambda2_increment':minimum,'min_unresolved_increment':minimum_unresolved})
print('metric','n_edge^* remains >= 6 (restricted blocker-tail theorem only)')
print('ALL_EXACT_CHECKS_PASS')
