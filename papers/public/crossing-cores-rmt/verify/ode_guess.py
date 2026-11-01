"""Experimental-math attack: is the even-moment generating function of
gamma_T / gamma_H algebraic, or holonomic of low order?

Method (exact rational arithmetic throughout): write the truncated series
M(z) = sum_{k<=7} m_2k z^k + X z^8 with X a formal unknown (the next
moment).  For each small ansatz

  algebraic:  P(z, M) = sum_{i<=dz, j<=dm} c_ij z^i M^j = 0
  holonomic:  sum_{j<=r} p_j(z) M^(j)(z) = 0, deg p_j <= d

impose the z^0..z^7 coefficient equations on the c's (these involve only the
known moments), compute the exact nullspace, and require it be
one-dimensional: then the z^8 coefficient equation is a + b X = 0 and, when
b != 0, the ansatz PREDICTS the next moment X = -a/b.

For gamma_H the next moment is known (9179819/840, computed tonight): a
matching prediction is evidence of real structure; mismatches kill the
ansatz.  For gamma_T the prediction is banked and will be compared against
the kappa_8 sweep's exact m_16 when it lands.

X-arithmetic note: every series here carries X only in its z^8 coefficient,
and truncation at z^8 means no X*X term can appear (it would sit at z^16),
so coefficients live in {u + v X} with exact Fractions u, v.

Run:  python -u ode_guess.py
"""
from fractions import Fraction as Fr

N = 9  # coefficients z^0..z^8

mT = [Fr(1), Fr(1), Fr(8, 3), Fr(11), Fr(908, 15), Fr(415), Fr(23840, 7),
      Fr(325719, 10)]
mH = [Fr(1), Fr(1), Fr(2), Fr(11, 2), Fr(281, 15), Fr(2717, 36), Fr(1052, 3),
      Fr(1331087, 720)]
M16_H = Fr(9179819, 840)

Z0 = (Fr(0), Fr(0))

def ser(moments):
    s = [(m, Fr(0)) for m in moments]
    s.append((Fr(0), Fr(1)))  # X at z^8
    return s

def smul(A, B):
    out = [Z0] * N
    for i, (au, av) in enumerate(A):
        if au == 0 and av == 0:
            continue
        for j in range(0, N - i):
            bu, bv = B[j]
            if bu == 0 and bv == 0:
                continue
            u = au * bu
            v = au * bv + av * bu  # av*bv would sit at z^16: dropped safely
            ou, ov = out[i + j]
            out[i + j] = (ou + u, ov + v)
    return out

def sshift(A, i):
    return [Z0] * i + A[:N - i]

def sderiv(A):
    return [(A[k + 1][0] * (k + 1), A[k + 1][1] * (k + 1))
            for k in range(N - 1)] + [Z0]

def nullspace(rows, ncols):
    """Exact nullspace basis of the rational matrix (list of row tuples)."""
    m = [list(r) for r in rows]
    nr = len(m)
    piv_cols = []
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, nr) if m[i][c] != 0), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(nr):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [x - f * y for x, y in zip(m[i], m[r])]
        piv_cols.append(c)
        r += 1
        if r == nr:
            break
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [Fr(0)] * ncols
        v[fc] = Fr(1)
        for ri, pc in enumerate(piv_cols):
            v[pc] = -m[ri][fc]
        basis.append(v)
    return basis

def attack(moments, label, known_next=None):
    S = ser(moments)
    results = []
    # ---- algebraic ansatzes
    for dz in range(1, 5):
        for dm in range(1, 5):
            if (dz + 1) * (dm + 1) > 16:
                continue
            terms = []
            Mp = [ [ (Fr(1), Fr(0)) ] + [Z0] * (N - 1) ]  # M^0
            for _ in range(dm):
                Mp.append(smul(Mp[-1], S))
            for j in range(dm + 1):
                for i in range(dz + 1):
                    terms.append(sshift(Mp[j], i))
            ncols = len(terms)
            rows = [tuple(t[n][0] for t in terms) for n in range(8)]
            basis = nullspace(rows, ncols)
            if len(basis) != 1:
                continue
            c = basis[0]
            a = sum(ci * t[8][0] for ci, t in zip(c, terms))
            b = sum(ci * t[8][1] for ci, t in zip(c, terms))
            if b == 0:
                continue
            pred = -a / b
            verdict = ""
            if known_next is not None:
                verdict = "MATCH - REAL STRUCTURE?" if pred == known_next else "wrong"
            results.append(("alg", dz, dm, pred, verdict))
    # ---- holonomic ansatzes
    for r_ord in range(1, 4):
        for d in range(0, 5):
            if (r_ord + 1) * (d + 1) > 16:
                continue
            derivs = [S]
            for _ in range(r_ord):
                derivs.append(sderiv(derivs[-1]))
            terms = []
            for j in range(r_ord + 1):
                for i in range(d + 1):
                    terms.append(sshift(derivs[j], i))
            ncols = len(terms)
            # derivative of z^8 X term pushes X into z^7 for M', z^6 for M''...
            # so X can contaminate lower coefficients: build equations only
            # from coefficient rows whose X-part is zero for ALL terms
            usable = [n for n in range(8)
                      if all(t[n][1] == 0 for t in terms)]
            rows = [tuple(t[n][0] for t in terms) for n in usable]
            basis = nullspace(rows, ncols)
            if len(basis) != 1:
                continue
            c = basis[0]
            # first coefficient row that DOES carry X gives the prediction
            for n in range(N):
                a = sum(ci * t[n][0] for ci, t in zip(c, terms))
                b = sum(ci * t[n][1] for ci, t in zip(c, terms))
                if b != 0:
                    pred = -a / b
                    verdict = ""
                    if known_next is not None:
                        verdict = ("MATCH - REAL STRUCTURE?"
                                   if pred == known_next else "wrong")
                    results.append(("ode", r_ord, d, pred, verdict))
                    break
                if a != 0:
                    break  # inconsistent at an X-free row: dead ansatz
    print(f"=== {label} ===")
    if not results:
        print("no uniquely-determined small ansatz (all nullspaces trivial or degenerate)")
    for kind, p1, p2, pred, verdict in results:
        tag = f"{kind}({p1},{p2})"
        print(f"{tag}: predicted next moment = {pred} ~ {float(pred):.4f}  {verdict}")
    return results

print("gamma_H: validation mode (true m_16 = 9179819/840 ~ 10928.356)")
rH = attack(mH, "gamma_H", known_next=M16_H)
print()
print("gamma_T: prediction mode (m_16 lands tonight from the kappa_8 sweep)")
rT = attack(mT, "gamma_T")
print()
preds = sorted({p for _, _, _, p, _ in rT})
print("banked gamma_T m_16 predictions to test against the sweep:",
      [str(p) for p in preds])
