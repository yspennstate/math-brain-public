"""Independent rational walk-law and symbolic checks. No author code is imported.

Run: nice -n 10 python3 independent_exact.py > independent_exact.out
Each execution has a 240-second alarm and uses one process.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import signal
import time
import resource

signal.alarm(240)
started = time.monotonic()


def solve(matrix, rhs):
    """Small dense Gauss-Jordan elimination over Q, implemented here."""
    n = len(rhs)
    a = [[F(x) for x in row] + [F(rhs[i])] for i, row in enumerate(matrix)]
    for k in range(n):
        p = next(i for i in range(k, n) if a[i][k])
        a[k], a[p] = a[p], a[k]
        z = a[k][k]
        a[k] = [x / z for x in a[k]]
        for i in range(n):
            if i != k and a[i][k]:
                z = a[i][k]
                a[i] = [x - z * y for x, y in zip(a[i], a[k])]
    return [row[-1] for row in a]


def graph(ell, weights, heterogeneous=False):
    A, B, C, D, R = weights
    edges = [(0, 1, A), (0, 2, B), (1, 2, R)]
    legs = []
    nv = 4
    for root, w in ((1, C), (2, D)):
        leg = [root]
        for j in range(ell):
            nxt = 3 if j == ell - 1 else nv
            nv += nxt != 3
            edges.append((leg[-1], nxt, w + j if heterogeneous else w))
            leg.append(nxt)
        legs.append(leg)
    adj = [[] for _ in range(nv)]
    for x, y, w in edges:
        adj[x].append((y, w))
        adj[y].append((x, w))
    paths = [(0,) + tuple(legs[0]), (0,) + tuple(legs[1]),
             (0, 1) + tuple(legs[1]), (0, 2) + tuple(legs[0])]
    return edges, adj, paths


def reversed_law(adj, paths):
    """Sum the actual stopped walk by its sequence of vertex discoveries.

    Inside the visited set V, integrate *all* excursions by solving the
    transient walk equations. The next discovery has an entrance edge x->y;
    record that parent. At F follow first-entrance parents to N. This is the
    reversed chronological loop erasure, without any spanning-tree theorem.
    """
    nv = len(adj)
    transition = [{y: F(w, sum(z for _, z in adj[x])) for y, w in adj[x]}
                  for x in range(nv)]

    @lru_cache(None)
    def exits(visited, start):
        vertices = [x for x in range(nv) if visited & (1 << x)]
        # (I-P_V)^T times expected occupation column = unit at start.
        mat = [[F(i == j) - transition[y].get(x, F(0))
                for j, y in enumerate(vertices)] for i, x in enumerate(vertices)]
        occ = solve(mat, [F(x == start) for x in vertices])
        out = []
        for x, visits in zip(vertices, occ):
            for y, prob in transition[x].items():
                if not visited & (1 << y):
                    out.append((x, y, visits * prob))
        assert sum(z for _, _, z in out) == 1
        return out

    @lru_cache(None)
    def discover(parents, start):
        visited = sum(1 << x for x, p in enumerate(parents) if p != -1)
        result = [F(0)] * 4
        for x, y, prob in exits(visited, start):
            new = list(parents)
            new[y] = x
            if y == 3:
                path = [3]
                while path[-1] != 0:
                    path.append(new[path[-1]])
                result[paths.index(tuple(reversed(path)))] += prob
            else:
                for i, q in enumerate(discover(tuple(new), y)):
                    result[i] += prob * q
        return tuple(result)

    answer = discover((0,) + (-1,) * (nv - 1), 0)
    return answer, discover.cache_info().currsize, exits.cache_info().currsize


def forward_law(adj, paths):
    r"""Sum erased loops using killed Green functions, independently of trees.

    For path v0,...,vk=F, its probability is product over j<k of
    G_{V\{F,v0,...,v(j-1)}}(vj,vj) P(vj,v(j+1)). The Green factor sums any
    number of returns before the last departure from vj. This is a direct
    decomposition of the stopped walk at its successive last visits.
    """
    transition = [{y: F(w, sum(z for _, z in adj[x])) for y, w in adj[x]}
                  for x in range(len(adj))]
    answer = []
    for path in paths:
        q = F(1)
        forbidden = {3}
        for x, y in zip(path, path[1:]):
            domain = [v for v in range(len(adj)) if v not in forbidden]
            mat = [[F(i == j) - transition[v].get(w, F(0))
                    for j, w in enumerate(domain)] for i, v in enumerate(domain)]
            green = solve(mat, [F(v == x) for v in domain])[domain.index(x)]
            q *= green * transition[x][y]
            forbidden.add(x)
        answer.append(q)
    assert sum(answer) == 1
    return tuple(answer)


def tree_law(edges, nv, paths):
    totals = [0] * 4
    count = 0
    for selected in combinations(edges, nv - 1):
        adj = [[] for _ in range(nv)]
        weight = 1
        for x, y, w in selected:
            adj[x].append(y)
            adj[y].append(x)
            weight *= w
        parent = {0: None}
        todo = [0]
        for x in todo:
            for y in adj[x]:
                if y not in parent:
                    parent[y] = x
                    todo.append(y)
        if len(parent) != nv:
            continue
        count += 1
        path = [3]
        while path[-1] != 0:
            path.append(parent[path[-1]])
        totals[paths.index(tuple(reversed(path)))] += weight
    return tuple(F(x, sum(totals)) for x in totals), count


def closed_form(ell, weights):
    A, B, C, D, R = weights
    m = [A*C*(D + ell*B + ell*R), B*D*(C + ell*A + ell*R),
         ell*A*R*D, ell*B*R*C]
    return tuple(F(x, sum(m)) for x in m)


print("Exact distributions in order pi1, pi2, pi3, pi4")
for ell in (1, 2, 3):
    for weights in ((1, 1, 1, 1, 1), (2, 3, 1, 4, 2), (5, 2, 3, 4, 1),
                    (1, 17, 13, 2, 9)):
        edges, adj, paths = graph(ell, weights)
        rev, states, systems = reversed_law(adj, paths)
        fwd = forward_law(adj, paths)
        tree, count = tree_law(edges, len(adj), paths)
        assert rev == fwd == tree == closed_form(ell, weights)
        assert sum(rev) == 1 and count == 2 + 6 * ell
        print(f"l={ell} weights={weights}: {', '.join(map(str, rev))}")
        print(f"  reverse=forward=trees=Lemma2.2 PASS; discovery states={states}; systems={systems}; trees={count}")
    if ell >= 2:
        edges, adj, paths = graph(ell, (2, 3, 1, 4, 2), True)
        rev, states, systems = reversed_law(adj, paths)
        assert rev == forward_law(adj, paths) == tree_law(edges, len(adj), paths)[0]
        print(f"l={ell} heterogeneous leg edges: {', '.join(map(str, rev))}; reverse=forward=trees PASS")

# A concrete walk separates the erasures pathwise, although their laws agree.
def erase(walk):
    path = []
    for x in walk:
        if x in path:
            path = path[:path.index(x) + 1]
        else:
            path.append(x)
    return path

walk = [0, 1, 2, 0, 2, 1, 3]
print("G1 walk N,u,v,N,v,u,F:", "forward", erase(walk),
      "reversed-back", list(reversed(erase(list(reversed(walk))))))

import sympy as s
a, c, h, L, S = s.symbols("a c h L S", positive=True)
b, d = 1-a, 1-c
Q = L*a*b + c*d + L*h
q = [a*c*(L*b+d+L*h)/Q, b*d*(L*a+c+L*h)/Q,
     L*a*h*d/Q, L*b*h*c/Q]
inc_a, inc_c, inc_h = q[0]+q[2], q[0]+q[3], q[2]+q[3]
fa, fc, fh = inc_a-a, inc_c-c, inc_h-h
g = a*d + b*c - a*b - c*d/L
mart_inc = [1/(a*S)+L/(c*S), -1/(b*S)-L/(d*S),
            1/(a*S)-L/(d*S), -1/(b*S)+L/(c*S)]
checks = {
    "probability sum": sum(q)-1,
    "Nu drift": fa-L*a*b*(c-a)/Q,
    "Nv drift": (q[1]+q[3]-b)+L*a*b*(c-a)/Q,
    "u-leg drift": fc-c*d*(a-c)/Q,
    "v-leg drift": (q[1]+q[2]-d)-c*d*(c-a)/Q,
    "rung drift": fh-L*h*(g-h)/Q,
    "exact harmonic martingale conditional increment": sum(x*y for x, y in zip(q, mart_inc)),
    "continuous logit conserved drift": fa/(a*b)+L*fc/(c*d),
    "delta drift": fa-fc+(L*a*b+c*d)*(a-c)/Q,
    "g diagonal and claimed constant": g.subs(c, a)-(1-1/L)*a*b,
    "l=1 identity": g.subs(L, 1)-(a-c)**2,
    "equilibrium Q": Q.subs({c:a, h:(1-1/L)*a*b})-2*L*a*b,
    "harmonic rung drift": inc_h/(h*S)-1/S-L*(g-h)/(Q*S),
    "rung linearization": s.diff(fh,h).subs({c:a,h:(1-1/L)*a*b})+(1-1/L)/2,
    "geodesic contraction on equilibrium": ((L*a*b+c*d)/Q).subs({c:a,h:(1-1/L)*a*b})-(L+1)/(2*L),
    "small-h amplification": (inc_h/h).subs({c:a,h:0})-2*L/(L+1),
}
for label, expr in checks.items():
    residual = s.factor(expr)
    assert residual == 0, (label, residual)
    print(f"SYMBOLIC {label}: residual={residual} PASS")
q_initial = [x.subs({a:F(1,2),c:F(1,2),h:F(1,2)}) for x in q]
dm_initial = [x.subs({a:F(1,2),c:F(1,2),S:2}) for x in mart_inc]
variance = s.factor(sum(x*y*y for x,y in zip(q_initial,dm_initial)))
print("First martingale increment variance:", variance)
assert s.factor(variance-(3*L**3+3*L**2+5*L+1)/(3*L+1)) == 0

# Polynomial tree enumeration for arbitrary symbols, separately from the walk tests.
A, B, C, D, R = s.symbols("A B C D R")
for ell in range(1,6):
    edges, adj, paths = graph(ell,(A,B,C,D,R))
    totals = [s.Integer(0)]*4
    count = 0
    for selected in combinations(edges,len(adj)-1):
        par = {0:None}
        todo = [0]
        for x in todo:
            for u,v,_ in selected:
                y = v if u == x else u if v == x else None
                if y is not None and y not in par:
                    par[y] = x
                    todo.append(y)
        if len(par) != len(adj):
            continue
        path = [3]
        while path[-1] != 0:
            path.append(par[path[-1]])
        count += 1
        totals[paths.index(tuple(reversed(path)))] += s.prod(w for _,_,w in selected)
    common = C**(ell-1)*D**(ell-1)
    expected = [A*C*(D+ell*B+ell*R), B*D*(C+ell*A+ell*R), ell*A*R*D, ell*B*R*C]
    assert all(s.expand(t-common*m)==0 for t,m in zip(totals,expected))
    assert s.expand(sum(expected)-(C*D*(A+B)+ell*A*B*(C+D)+ell*R*(A+B)*(C+D))) == 0
    print(f"SYMBOLIC tree enumeration l={ell}: {count} trees, all four polynomials PASS")
print(f"ALL EXACT CHECKS PASS; elapsed_seconds={time.monotonic()-started:.3f}")
print(f"peak_rss_bytes_macos={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}")
