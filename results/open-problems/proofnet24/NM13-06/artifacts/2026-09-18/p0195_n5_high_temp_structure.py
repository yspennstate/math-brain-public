from itertools import permutations
import sympy as sp

N = 5
E = [(i,j) for i in range(N) for j in range(i+1,N)]
EI = {e:k for k,e in enumerate(E)}
PERMS = list(permutations(range(N)))
x = sp.symbols('x')


def pmask(m,p):
    out = 0
    for k,(a,b) in enumerate(E):
        if (m >> k) & 1:
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


def auts(m):
    return [p for p in PERMS if pmask(m,p) == m]


def marked_stabilizer_size(m,k):
    a,b = E[k]
    pair = {a,b}
    return sum(1 for p in auts(m) if {p[a],p[b]} == pair)


def amat(m):
    A = sp.zeros(N)
    for k,(i,j) in enumerate(E):
        if (m >> k) & 1:
            A[i,j] = A[j,i] = 1
    return A


def components(m):
    nbr = [set() for _ in range(N)]
    for k,(i,j) in enumerate(E):
        if (m >> k) & 1:
            nbr[i].add(j); nbr[j].add(i)
    seen=set(); ans=[]
    for v in range(N):
        if v in seen: continue
        stack=[v]; seen.add(v); C=[]
        while stack:
            u=stack.pop(); C.append(u)
            for w in nbr[u]:
                if w not in seen:
                    seen.add(w); stack.append(w)
        ans.append(tuple(sorted(C)))
    return tuple(sorted(ans, key=lambda C:(len(C),C)))


def top_interval(poly, eps=sp.Rational(1,10**80)):
    ints = poly.intervals(eps=eps)
    (a,b),mult = ints[-1]
    return sp.Rational(a), sp.Rational(b), mult


def overlaps(I,J):
    a,b,_ = I; c,d,_ = J
    return not (b < c or d < a)

CAN = sorted({canon(m) for m in range(1 << len(E))}, key=lambda m:(m.bit_count(),m))
assert len(CAN) == 34
MARKED = sorted({
    canon_marked(m,k)
    for m in CAN
    for k in range(len(E)) if not ((m >> k) & 1)
})
assert len(MARKED) == 74
TRANS = sorted({(m,canon(m|(1<<k))) for m,k in MARKED})
assert len(TRANS) == 74

CP = {m: sp.Poly(amat(m).charpoly(x).as_expr(), x, domain=sp.ZZ) for m in CAN}
strict=[]; ties=[]
for s,t in TRANS:
    Is = top_interval(CP[s])
    It = top_interval(CP[t])
    if It[0] > Is[1]:
        strict.append((s,t))
        continue
    g = sp.gcd(CP[s],CP[t])
    assert g.degree() > 0, (s,t,Is,It)
    Ig = top_interval(g)
    if overlaps(Is,Ig) and overlaps(It,Ig):
        ties.append((s,t,sp.factor(g.as_expr())))
    else:
        assert It[0] > Is[1], (s,t,Is,It,Ig)
        strict.append((s,t))

assert len(strict) == 71
assert [(s,t) for s,t,_ in ties] == [(1,20),(3,28),(19,184)]

# Exact component shapes of the three Perron-radius ties.
expected = {
    (1,20): (((2,), (3,), (4,), (0,1)), ((4,), (0,3), (1,2))),
    (3,28): (((3,), (4,), (0,1,2)), ((1,2), (0,3,4))),
    (19,184): (((3,), (4,), (0,1,2)), ((0,4), (1,2,3))),
}
for s,t,_ in ties:
    assert components(s) == expected[(s,t)][0]
    assert components(t) == expected[(s,t)][1]

trivial = [(m,k,canon(m|(1<<k))) for m,k in MARKED if marked_stabilizer_size(m,k) == 1]
assert len(trivial) == 22
assert trivial[0] == (3,5,21)
assert E[5] == (1,3)

print('n5_unlabeled_graph_classes', len(CAN))
print('n5_marked_edge_addition_types', len(MARKED))
print('adjacency_rho_strict_types', len(strict))
print('adjacency_rho_tie_types', len(ties))
for s,t,g in ties:
    print('rho_tie', s, t, 'common_top_factor', g, 'source_components', components(s), 'target_components', components(t))
print('marked_types_with_trivial_stabilizer', len(trivial))
print('first_trivial_marked_type', trivial[0], 'marked_nonedge', E[trivial[0][1]])
print('ALL_EXACT_CHECKS_PASS')
