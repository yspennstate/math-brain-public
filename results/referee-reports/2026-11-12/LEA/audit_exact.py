"""Independent, exact finite-state path-law audit. No simulation or author's imports.

Forward erasure is an absorbing chain on simple stacks. Backward erasure is
computed by discovering the original walk's first-entrance tree: all excursions
inside its visited set are summed by rational matrix inversion before each new
discovery. Neither calculation uses a spanning-tree probability formula.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
from functools import lru_cache
import random


def solve(matrix, rhs):
    a = [list(map(F, row)) + list(map(F, val)) for row, val in zip(matrix, rhs)]
    n, m = len(a), len(rhs[0])
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        t = a[j][j]
        a[j] = [x / t for x in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                t = a[i][j]
                a[i] = [x - t * y for x, y in zip(a[i], a[j])]
    return [row[n:n+m] for row in a]


def adj_of(edges):
    adj = defaultdict(dict)
    for x, y, w in edges:
        adj[x][y] = adj[y][x] = F(w)
    return dict(adj)


def forward(edges):
    adj = adj_of(edges)
    states, index, terminal = [(0,)], {(0,): 0}, set()
    transitions = []
    for stack in states:
        row = defaultdict(F)
        x = stack[-1]
        total = sum(adj[x].values())
        for y, w in adj[x].items():
            new = stack[:stack.index(y)+1] if y in stack else stack + (y,)
            if y == 3:
                terminal.add(new)
            elif new not in index:
                index[new] = len(states)
                states.append(new)
            row[new] += w / total
        transitions.append(row)
    terminal = sorted(terminal)
    ti = {s: i for i, s in enumerate(terminal)}
    n = len(states)
    mat = [[F(i == j) for j in range(n)] for i in range(n)]
    rhs = [[F(0) for _ in terminal] for _ in states]
    for i, row in enumerate(transitions):
        for s, p in row.items():
            if s[-1] == 3:
                rhs[i][ti[s]] += p
            else:
                mat[i][index[s]] -= p
    out = solve(mat, rhs)[0]
    return dict(zip(terminal, out)), len(states)


def backward(edges):
    adj = adj_of(edges)
    law = defaultdict(F)

    @lru_cache(None)
    def exits(visited):
        # Distribution of first outward edge (x,y) for each starting vertex.
        vertices = sorted(visited)
        ix = {x: i for i, x in enumerate(vertices)}
        border = [(x, y) for x in vertices for y in adj[x] if y not in visited]
        n = len(vertices)
        mat = [[F(i == j) for j in range(n)] for i in range(n)]
        rhs = [[F(0) for _ in border] for _ in vertices]
        bi = {e: i for i, e in enumerate(border)}
        for x in vertices:
            total = sum(adj[x].values())
            for y, w in adj[x].items():
                if y in visited:
                    mat[ix[x]][ix[y]] -= w / total
                else:
                    rhs[ix[x]][bi[(x, y)]] = w / total
        return vertices, border, solve(mat, rhs)

    def discover(parent, current, mass):
        vertices, border, probs = exits(frozenset(parent))
        for (x, y), p in zip(border, probs[vertices.index(current)]):
            if not p:
                continue
            new = dict(parent)
            new[y] = x
            if y == 3:
                path = [3]
                while path[-1] != 0:
                    path.append(new[path[-1]])
                law[tuple(reversed(path))] += mass * p
            else:
                discover(new, y, mass * p)
    discover({0: None}, 0, F(1))
    return dict(law), exits.cache_info().currsize


def trees(edges):
    vertices = set(adj_of(edges))
    law, count = defaultdict(F), 0
    for inds in combinations(range(len(edges)), len(vertices)-1):
        parent, stack = {0: None}, [0]
        adj = defaultdict(list)
        weight = F(1)
        for i in inds:
            x, y, w = edges[i]
            adj[x].append(y)
            adj[y].append(x)
            weight *= w
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in parent:
                    parent[y] = x
                    stack.append(y)
        if set(parent) != vertices:
            continue
        count += 1
        path = [3]
        while path[-1] != 0:
            path.append(parent[path[-1]])
        law[tuple(reversed(path))] += weight
    return dict(law), count


def graph(ell, weights):
    A, B, C, D, R = weights
    edges = [(0, 1, A), (0, 2, B), (1, 2, R)]
    nxt = 4
    for root, w in [(1, C), (2, D)]:
        prev = root
        for i in range(ell):
            end = 3 if i == ell-1 else nxt
            if end != 3:
                nxt += 1
            edges.append((prev, end, w))
            prev = end
    return edges


def normalized(law):
    z = sum(law.values())
    return {p: w / z for p, w in law.items()}


def formula(ell, weights):
    A, B, C, D, R = weights
    return [A*C*(D+ell*B+ell*R), B*D*(C+ell*A+ell*R), ell*A*R*D, ell*B*R*C]


def four_masses(law):
    out = [F(0)] * 4
    for path, w in law.items():
        rung = any({x,y} == {1,2} for x,y in zip(path, path[1:]))
        out[(path[1] == 2) + 2*rung] += w
    return out


if __name__ == '__main__':
    randomizer = random.Random(20261112)
    for ell in range(1, 5):
        for trial in range(12):
            weights = [F(randomizer.randint(1, 13), randomizer.randint(1, 11)) for _ in range(5)]
            masses, count = trees(graph(ell, weights))
            factor = weights[2]**(ell-1)*weights[3]**(ell-1)
            assert count == 2+6*ell
            assert four_masses(masses) == [factor*m for m in formula(ell, weights)]
        print(f'Lemma law ell={ell}: 12 rational weight vectors PASS; trees={count}')

    cases = [('G1', graph(1, list(map(F, [2,3,1,4,2])))),
             ('G2', graph(2, [F(2,3),F(7,5),F(3,2),F(11,7),F(5,4)])),
             ('K4 plus a leaf', [(0,1,F(2,3)),(0,2,F(3,4)),(0,3,F(5,7)),
                                  (1,2,F(7,5)),(1,3,F(11,9)),(2,3,F(13,8)),(1,4,F(17,6))])]
    for name, edges in cases:
        f, ns = forward(edges)
        b, nv = backward(edges)
        t, nt = trees(edges)
        t = normalized(t)
        assert sum(f.values()) == sum(b.values()) == sum(t.values()) == 1
        assert f == b == t
        print(f'{name}: forward stack chain ({ns} states) = backward discovery chain ({nv} visited sets) = trees ({nt}), EXACT PASS')
        for p in sorted(t):
            print(f'  {p}: {t[p]}')
    print('ALL INDEPENDENT EXACT CHECKS PASS')
