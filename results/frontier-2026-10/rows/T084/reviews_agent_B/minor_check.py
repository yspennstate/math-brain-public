# T084, agent B: check the dossier's structure claim. For each monomial m of N (exponent set D = 2, Z = 0, S = 1), build the
# minor M' = (M/D)\Z on S + {e,f} as a binary matroid (contract D by projecting out its span), take the top coefficient of N for
# M' (the monomial with every element of S to the first power), and test c_m(q) == q^k * top(q) for a k >= 0.
import json
exec(open('amgm_cert.py').read().split("if __name__")[0])
def contract(cols, D):
    # quotient by span(D): reduce every vector modulo a basis of span(D) in echelon form
    piv = {}
    for v in [cols[i] for i in D]:
        while v:
            h = v.bit_length() - 1
            if h in piv: v ^= piv[h]
            else: piv[h] = v; break
    def red(v):
        for h in sorted(piv, reverse=True):
            if v >> h & 1: v ^= piv[h]
        return v
    return [red(c) for c in cols]
def check(name, cols, e, f):
    C = Npoly(cols, e, f); n = len(cols); free = [i for i in range(n) if i not in (e, f)]; bad = 0; cache = {}
    for m, c in C.items():
        D = [free[k] for k, a in enumerate(m) if a == 2]; S = [free[k] for k, a in enumerate(m) if a == 1]
        red = contract(cols, D); sub = [red[i] for i in S] + [red[e], red[f]]; ne, nf = len(S), len(S) + 1
        key = (tuple(sub),)
        if key not in cache:
            Cm = Npoly(sub, ne, nf); cache[key] = Cm.get(tuple([1] * len(S)), sp.Integer(0))
        top = cache[key]
        if top == 0: ok = (c == 0)
        else:
            r = sp.cancel(c / top); ok = r.is_polynomial(q) and sp.Poly(r, q).is_monomial and sp.Poly(r, q).LC() == 1
        bad += not ok
    print(json.dumps(dict(matroid=name, pair=(e, f), monomials=len(C), mismatches=bad)), flush=True)
check('AG(3,2)', [8 | v for v in range(8)], 0, 1)
A = [0b0111, 0b1011, 0b1101, 0b1111]
cols = [1, 2, 4, 8] + [sum(((A[r] >> (3 - c)) & 1) << r for r in range(4)) for c in range(4)]
check('S8', cols, 3, 7); check('S8', cols, 0, 1)
