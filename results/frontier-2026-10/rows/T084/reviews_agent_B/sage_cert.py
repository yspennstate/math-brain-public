# T084, agent B: SAGE (sums of AM/GM exponentials, Chandrasekaran-Shah 2016) certificate for N >= 0 on y > 0 at fixed q.
# In log coordinates N = sum_m c_m exp(m . x). For each negative term k an AGE piece: split coefficients C_k >= 0 of the positive
# terms (sum_k C_k <= c), nu_k >= 0 with sum_j nu_kj (p_j - m_k) = 0 and D(nu_k, e C_k) <= c_mk. Minimize slack s in
# D(nu_k, e C_k) <= c_mk + s |c_mk|; s* <= 0 certifies N >= 0 at that q (numerically). Positive terms offered to a negative:
# those within L1 distance RAD of it.
import sys, json, itertools, numpy as np, cvxpy as cp
exec(open('amgm_cert.py').read().split("if __name__")[0])
def sage(C, qv, RAD=4):
    keys = list(C.keys()); M = np.array(keys, float)
    cv = np.array([float(sp.Poly(C[k], q).eval(sp.Rational(qv).limit_denominator(10**9))) for k in keys])
    neg = [i for i in range(len(keys)) if cv[i] < -1e-15]; pos = [i for i in range(len(keys)) if cv[i] > 1e-15]
    if not neg: return dict(q=qv, negative=0, s=None)
    s = cp.Variable(); use = {j: [] for j in pos}; cons = []
    for k in neg:
        J = [j for j in pos if np.abs(M[j] - M[k]).sum() <= RAD]
        Ck = cp.Variable(len(J), nonneg=True); nu = cp.Variable(len(J), nonneg=True)
        cons += [(M[J] - M[k]).T @ nu == 0, cp.sum(cp.rel_entr(nu, np.e * Ck)) <= cv[k] + s * abs(cv[k])]
        for t, j in enumerate(J): use[j].append(Ck[t])
    cons += [cp.sum(cp.hstack(v)) <= cv[j] for j, v in use.items() if v]
    pr = cp.Problem(cp.Minimize(s), cons + [s >= -1])
    try: pr.solve(solver='CLARABEL')
    except Exception as ex: return dict(q=qv, negative=len(neg), s=None, status=str(ex)[:80])
    return dict(q=qv, negative=len(neg), s=None if s.value is None else round(float(s.value), 5), status=pr.status)
def circuits4(cols, e, f):
    return sum(1 for S in itertools.combinations([i for i in range(len(cols)) if i not in (e, f)], 2)
               if rank([cols[i] for i in (e, f) + S]) == 3 and all(rank([cols[i] for i in T]) == 3 for T in itertools.combinations((e, f) + S, 3)))
if __name__ == '__main__':
    A = [0b11001, 0b11100, 0b01110, 0b00111, 0b10011]
    colsR10 = [1 << i for i in range(5)] + [sum(((A[row] >> (4 - c)) & 1) << row for row in range(5)) for c in range(5)]
    sig = {}
    for e, f in itertools.combinations(range(10), 2): sig.setdefault(circuits4(colsR10, e, f), []).append((e, f))
    print(json.dumps({'pair_classes_by_4circuits': {str(k): len(v) for k, v in sig.items()}}), flush=True)
    for k, v in sorted(sig.items()):
        e, f = v[0]; C = Npoly(colsR10, e, f)
        negs = sorted(set(str(sp.factor(C[m])) for m in C if not nonneg01(C[m])))
        print(json.dumps(dict(pair=(e, f), four_circuits=k, monomials=len(C), negative_polys=negs)), flush=True)
        for qv in [0.0, 0.05, 0.2, 0.4, 0.55]:
            print(json.dumps(dict(pair=(e, f), **sage(C, qv))), flush=True)
    # control: S8 true bad pair must NOT certify at small q; F7 must certify
    Acon = [0b0111, 0b1011, 0b1101, 0b1111]
    cs8 = [1, 2, 4, 8] + [sum(((Acon[r] >> (3 - c)) & 1) << r for r in range(4)) for c in range(4)]
    for qv in [0.01, 0.2]: print(json.dumps(dict(control='S8 (3,7)', **sage(Npoly(cs8, 3, 7), qv))), flush=True)
    for qv in [0.01, 0.2]: print(json.dumps(dict(control='S8 (0,1)', **sage(Npoly(cs8, 0, 1), qv))), flush=True)
