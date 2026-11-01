"""A043 v1: exact cofactor-row factorization census; no entropy estimates."""
import itertools, json, time
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'out'
checks = 0
def verify(q):
    global checks
    assert q
    checks += 1

def essential(t, n):
    return all(any(t[x] != t[x ^ (1 << i)] for x in range(1 << n)) for i in range(n))

def join(a, b, B, D):
    return sum(((a >> i) & 1) << j for i, j in enumerate(B)) | sum(((b >> i) & 1) << j for i, j in enumerate(D))

def factor(t, n):
    for k in range(2, n):
        for B in itertools.combinations(range(n), k):
            D = tuple(i for i in range(n) if i not in B)
            rows = [tuple(t[join(a,b,B,D)] for b in range(1 << len(D))) for a in range(1 << k)]
            uniq = sorted(set(rows))
            if len(uniq) == 2:
                h = tuple(uniq.index(row) for row in rows)
                g = tuple(uniq[y & 1][y >> 1] for y in range(1 << (len(D)+1)))
                return B,D,h,g
    return None

def certify(t, n):
    verify(essential(t,n))
    f = factor(t,n)
    if f is None:
        return {'arity':n,'table':sum(v<<i for i,v in enumerate(t))}
    B,D,h,g = f
    verify(2 <= len(B) < n)
    verify(essential(h,len(B)))
    verify(essential(g,len(D)+1))
    for a in range(1 << len(B)):
        for b in range(1 << len(D)):
            verify(t[join(a,b,B,D)] == g[h[a] | (b << 1)])
    return {'arity':n,'block':B,'inner':certify(h,len(B)), 'outer':certify(g,len(D)+1)}

start = time.perf_counter()
result = {'helper':'A043-cofactor-v1','arithmetic':'exact integers/tuples','symmetry':'none','counts':[]}
examples = {}
for n in range(1,5):
    total = 1 << (1 << n)
    ess = primes = 0
    for mask in range(total):
        t = tuple((mask >> x) & 1 for x in range(1 << n))
        if not essential(t,n):
            continue
        ess += 1
        tree = certify(t,n)
        if 'block' not in tree:
            primes += 1
            examples.setdefault(str(n), tree)
    result['counts'].append({'n':n,'truth_tables':total,'essential':ess,'prime':primes,'decomposable':ess-primes})
    verify(time.perf_counter()-start < 60)
result['assertions'] = checks
result['runtime_seconds'] = time.perf_counter()-start
result['prime_examples'] = examples
OUT.mkdir(exist_ok=True)
(OUT/'census.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
