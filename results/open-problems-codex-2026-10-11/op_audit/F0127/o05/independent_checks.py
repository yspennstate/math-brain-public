from pathlib import Path
import itertools
import sympy as s


def check(name, nu, transitive=True):
    n = nu.rows
    assert nu == nu.T and all(sum(nu.row(i)) == 1 for i in range(n))
    q = (nu - s.eye(n)) / 2
    # Solve the killed pair-chain equations, without assuming a relative walk.
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    index = {p: k for k, p in enumerate(pairs)}
    a = s.zeros(len(pairs))
    for p, k in index.items():
        i, j = p
        a[k, k] = q[i, i] + q[j, j]
        for z in range(n):
            if z != i and (z, j) in index:
                a[k, index[z, j]] += q[i, z]
            if z != j and (i, z) in index:
                a[k, index[i, z]] += q[j, z]
    h = (-a).inv() * s.ones(len(pairs), 1)
    meeting = sum(h) / n**2
    hitting = []
    for target in range(n):
        keep = [i for i in range(n) if i != target]
        hitting.append(sum((-q.extract(keep, keep)).inv() * s.ones(n-1, 1)) / n)
    # K = trace of group inverse of -Q, evaluated rationally.
    proj = s.ones(n) / n
    kemeny = s.trace((-q + proj).inv() - proj)
    if transitive:
        assert all(x == kemeny for x in hitting)
        assert meeting == kemeny / 2
        # Test the claimed Laplace transform directly from killed generator.
        for rate in [s.Rational(1, 7), s.Rational(3, 2)]:
            laplace = 1 - rate * sum((rate*s.eye(len(pairs))-a).inv()*s.ones(len(pairs),1)) / n**2
            spectral_sum = s.trace((rate*s.eye(n)-2*q).inv()) - 1/rate
            assert s.simplify(laplace - 1/(1+rate*spectral_sum)) == 0
    # Independently solve full coalescence on subsets, layer by layer.
    means = {frozenset([i]): s.Integer(0) for i in range(n)}
    for size in range(2, n+1):
        states = list(map(frozenset, itertools.combinations(range(n), size)))
        ix = {v: j for j, v in enumerate(states)}
        gen = s.zeros(len(states)); rhs = s.ones(len(states), 1)
        for v, row in ix.items():
            for x in v:
                for y in range(n):
                    if y == x or q[x,y] == 0:
                        continue
                    w = (v-{x}) | {y}
                    gen[row,row] -= q[x,y]
                    if len(w) == size:
                        gen[row,ix[w]] += q[x,y]
                    else:
                        rhs[row] += q[x,y]*means[w]
        solved = (-gen).inv()*rhs
        means.update({v: solved[row] for v, row in ix.items()})
    coal = means[frozenset(range(n))]
    return f'{name}: n={n}, tau_meet={meeting}, K={kemeny}, stationary target means={hitting}, E_coal={coal}, ratio={s.factor(coal/meeting)}; all applicable identities passed'


results = []
for n in range(2, 7):
    nu = (s.ones(n)-s.eye(n))/(n-1)
    results.append(check(f'complete K{n}',nu))
for n in [4, 5, 6]:
    nu = s.zeros(n)
    for i in range(n):
        nu[i,(i+1)%n] = nu[i,(i-1)%n] = s.Rational(1,2)
    results.append(check(f'cycle C{n}',nu))
nu = s.zeros(6)
for i in range(6):
    for step, weight in [(1,s.Rational(1,6)),(-1,s.Rational(1,6)),(2,s.Rational(1,3)),(-2,s.Rational(1,3))]:
        nu[i,(i+step)%6] += weight
results.append(check('weighted transitive circulant',nu))
for n in range(2,51):
    meeting = s.Rational((n-1)**2,n)
    coal = sum(s.Rational(2*(n-1),k*(k-1)) for k in range(2,n+1))
    assert coal == 2*meeting
results.append('Complete graph holding-time formula: exact rational checks n=2,...,50 passed.')
Path('independent_checks.txt').write_text('\n'.join(results)+'\n',encoding='utf-8')
print('\n'.join(results))
