# is the ap_9c group (order 36 on 9 points) a subgroup of the k33c group (order 72 on the 9 edges of K_{3,3}) after a
# relabelling of the 9 points?  Tries every bijection of the 9 points.  usage: python3 ap9_in_k33.py CODEDIR
import sys
import itertools
sys.path.insert(0, sys.argv[1])
import sym_search as S


def closure(gens, n):
    idt = tuple(range(n)); seen = {idt}; stack = [idt]
    while stack:
        x = stack.pop()
        for g in gens:
            y = tuple(g[x[i]] for i in range(n))
            if y not in seen:
                seen.add(y); stack.append(y)
    return seen


def points(name):
    m, gens, _ = S.struct(name)
    assert m == 18
    pg = [tuple(g[:9]) for g in gens]
    assert all(max(p) < 9 for p in pg)                                    # points map to points
    assert all(all(g[9 + i] == 9 + g[i] for i in range(9)) for g in gens)  # each coin follows its point
    return pg


A = points("ap_9c"); K = closure(points("k33c"), 9); KS = closure(points("k33cs"), 9)
GA = closure(A, 9)
print("orders: ap_9c", len(GA), "k33c", len(K), "k33cs", len(KS))
found = 0; found_s = 0; first = None
for s in itertools.permutations(range(9)):
    if s[0] != 0:                      # the k33c group is transitive on the 9 points: fix the image of point 0
        break
    inv = [0] * 9
    for i, x in enumerate(s):
        inv[x] = i
    conj = [tuple(s[g[inv[i]]] for i in range(9)) for g in A]
    if all(c in K for c in conj):
        found += 1
        if first is None:
            first = s
        if all(c in KS for c in conj):
            found_s += 1
print("bijections fixing point 0 that carry ap_9c into k33c:", found, "of 40320; of those also into k33cs:", found_s)
print("first:", first)
