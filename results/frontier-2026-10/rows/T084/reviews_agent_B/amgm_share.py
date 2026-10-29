# T084, agent B: AM-GM certificate with shared partners. A positive monomial used by k negatives gives each 1/k of
# its coefficient; a triple (m; m1, m2) is valid when 4 c_m1 c_m2 - k1 k2 c_m^2 >= 0 wherever c_m < 0 on (0,1) (exact).
# Search: backtracking over candidate pairs, preferring pairs whose monomials are least used; verify every triple whose
# monomials' usage changed.
import sys, json, itertools
exec(open('amgm_cert.py').read().split("if __name__")[0])
def certify_share(name, cols, e, f, maxnodes=200000):
    C = Npoly(cols, e, f); neg = [m for m in C if not nonneg01(C[m])]; pos = set(m for m in C if m not in neg)
    cand = {}
    for m in neg:
        cand[m] = []
        for m1 in pos:
            m2 = tuple(2 * a - b for a, b in zip(m, m1))
            if m1 < m2 and m2 in pos and nonneg01(4 * C[m1] * C[m2] - C[m] ** 2, where=C[m]): cand[m].append((m1, m2))
    if any(not cand[m] for m in neg):
        out = dict(matroid=name, pair=(e, f), negative=len(neg), certificate=False, reason='a negative monomial has no partner pair',
                   uncovered=[(str(m), str(sp.factor(C[m]))) for m in neg if not cand[m]][:6]); print(json.dumps(out), flush=True); return out
    memo = {}
    def ok(m, m1, m2, k1, k2):
        key = (m, m1, m2, k1, k2)
        if key not in memo: memo[key] = nonneg01(4 * C[m1] * C[m2] - k1 * k2 * C[m] ** 2, where=C[m])
        return memo[key]
    order = sorted(neg, key=lambda m: len(cand[m])); use = {}; pick = {}; nodes = [0]
    def valid_all():
        return all(ok(m, a, b, use[a], use[b]) for m, (a, b) in pick.items())
    def bt(i):
        nodes[0] += 1
        if nodes[0] > maxnodes: return None
        if i == len(order): return True
        m = order[i]
        for (a, b) in sorted(cand[m], key=lambda p: use.get(p[0], 0) + use.get(p[1], 0)):
            use[a] = use.get(a, 0) + 1; use[b] = use.get(b, 0) + 1; pick[m] = (a, b)
            if valid_all():
                r = bt(i + 1)
                if r: return True
                if r is None: return None
            use[a] -= 1; use[b] -= 1; del pick[m]
        return False
    r = bt(0)
    out = dict(matroid=name, pair=(e, f), negative=len(neg), certificate=bool(r), exhausted=(r is None), nodes=nodes[0],
               max_share=max(use.values()) if r else None, assignment={str(m): [str(a), str(b)] for m, (a, b) in pick.items()} if r else None)
    print(json.dumps(out), flush=True); return out
if __name__ == '__main__':
    A = [0b0111, 0b1011, 0b1101, 0b1111]
    cols = [1, 2, 4, 8] + [sum(((A[r] >> (3 - c)) & 1) << r for r in range(4)) for c in range(4)]
    for e, f in [(0, 1), (4, 5), (3, 7)]: certify_share('S8', cols, e, f)
