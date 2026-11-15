"""Independent exact finite-state hitting calculation; no author code."""
from fractions import Fraction as F
import json
import mpmath as mp
import signal
signal.alarm(280)


def recursion(t, lam):
    if not t:
        return F(1)
    s = sum((recursion(v, lam) for v in t), F(0))
    return s / (lam + s)


def solve(a, b):
    n = len(b)
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        b[col], b[pivot] = b[pivot], b[col]
        q = a[col][col]
        a[col] = [x / q for x in a[col]]
        b[col] /= q
        for i in range(n):
            if i == col:
                continue
            q = a[i][col]
            a[i] = [u - q * v for u, v in zip(a[i], a[col])]
            b[i] -= q * b[col]
    return b


def linear(t, lam):
    nodes, parents, children = [], [], []

    def visit(tree, parent):
        idx = len(nodes)
        nodes.append(tree)
        parents.append(parent)
        children.append([])
        for v in tree:
            children[idx].append(visit(v, idx))
        return idx

    visit(t, -1)
    interior = [i for i, v in enumerate(nodes) if v]
    ids = {v: i for i, v in enumerate(interior)}
    n = len(ids)
    a = [[F(0) for _ in range(n)] for _ in range(n)]
    rhs = [F(0) for _ in range(n)]
    for v, row in ids.items():
        deg = len(children[v])
        a[row][row] = lam + deg
        if parents[v] >= 0:
            a[row][ids[parents[v]]] -= lam
        for w in children[v]:
            if w in ids:
                a[row][ids[w]] -= 1
            else:
                rhs[row] += 1
    return solve(a, rhs)[0], n


def main():
    leaf = ()
    one = (leaf,)
    two = (leaf, leaf)
    three = (leaf, leaf, leaf)
    trees = [(one, three), (one, two), (three, one, two),
             ((one, two), (three,), (two, one)),
             (((one,), (two, three)), ((three, two, one),))]
    rows = []
    for idx, tree in enumerate(trees, 1):
        for lam in map(F, ['0', '1/3', '1', '3/2', '3']):
            b = recursion(tree, lam)
            h, n = linear(tree, lam)
            assert b == h
            rows.append(dict(tree=idx, interior=n, lam=str(lam), recursion=str(b), linear=str(h)))
    mp.mp.dps = 70
    laws = {
        '12': [(1, mp.mpf(1)/2), (2, mp.mpf(1)/2)],
        '24': [(2, mp.mpf(1)/2), (4, mp.mpf(1)/2)],
        '123': [(i, mp.mpf(1)/3) for i in (1, 2, 3)],
        'geom': [(i, mp.mpf(2)**(-i)) for i in range(1, 401)],
    }
    constants = {}
    for name, law in laws.items():
        a = sum(p/n for n,p in law)
        ell = sum(p*mp.log(n) for n,p in law)
        h = sum(p*mp.log(n)/n for n,p in law)
        slope = (1-a)*(a*ell-h)
        sym = sum(p*q*(mp.log(n)-mp.log(k))*(1/mp.mpf(k)-1/mp.mpf(n)) for n,p in law for k,q in law)/2
        assert abs(slope-(1-a)*sym) < mp.mpf('1e-65')
        constants[name] = {k:mp.nstr(v,60) for k,v in dict(a=a,d0=ell,slope=slope,logm=mp.log(sum(p*n for n,p in law))).items()}
    result = dict(exact_trees=rows,tree_notation=repr(trees),constants=constants,
                  geometric_tail='k>400: log(k)<=k; sum k*2^-k=(402)*2^-400 < 1.6e-118')
    with open('exact_results.json','w') as f:
        json.dump(result,f,indent=2)
    for row in rows:
        print(row)
    print(json.dumps(constants,indent=2))


if __name__ == '__main__':
    main()
