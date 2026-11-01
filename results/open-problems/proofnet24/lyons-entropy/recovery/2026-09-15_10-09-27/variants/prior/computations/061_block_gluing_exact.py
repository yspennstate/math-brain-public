#!/usr/bin/env python3
"""Exact checks for worker 061. Python standard library; no numerical signs.

Independently compares inclusion-exclusion and mixed-column determinants,
computes formal KL coefficients, and checks block-resolvent/projection formulas.
All examples use rational or Gaussian-rational matrices.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json


@dataclass(frozen=True)
class G:
    r: F = F(0)
    i: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "r", F(self.r))
        object.__setattr__(self, "i", F(self.i))

    def __add__(self, x):
        x = gg(x)
        return G(self.r+x.r, self.i+x.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, x):
        return self + -gg(x)

    def __rsub__(self, x):
        return gg(x) + -self

    def __mul__(self, x):
        x = gg(x)
        return G(self.r*x.r-self.i*x.i, self.r*x.i+self.i*x.r)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = gg(x)
        q = x.r*x.r+x.i*x.i
        assert q
        return self * G(x.r/q, -x.i/q)

    def conj(self):
        return G(self.r, -self.i)

    def norm2(self):
        return self.r*self.r+self.i*self.i

    def __bool__(self):
        return bool(self.r or self.i)

    def __str__(self):
        return str(self.r) if not self.i else f"({self.r})+({self.i})i"


def gg(x):
    return x if isinstance(x, G) else G(x)


def real(x):
    x = gg(x)
    assert not x.i
    return x.r


def mat(rows):
    return [[gg(x) for x in row] for row in rows]


def zero(n, m=None):
    return [[G() for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def adj(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def mm(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), G())
             for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return sum((A[i][i] for i in range(len(A))), G())


def add(A, B, scale=1):
    return [[x+scale*y for x, y in zip(a, b)] for a, b in zip(A, B)]


def sub(A, ix, jx=None):
    jx = ix if jx is None else jx
    return [[A[i][j] for j in jx] for i in ix]


def inv(A):
    n = len(A)
    M = [A[i][:]+eye(n)[i] for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if M[i][j])
        M[j], M[p] = M[p], M[j]
        d = M[j][j]
        M[j] = [x/d for x in M[j]]
        for i in range(n):
            if i != j:
                c = M[i][j]
                M[i] = [x-c*y for x, y in zip(M[i], M[j])]
    return [r[n:] for r in M]


def padd(a, b):
    c = [G()] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return c


def pmul(a, b, cap=None):
    size = len(a)+len(b)-1
    if cap is not None:
        size = min(size, cap+1)
    c = [G()] * size
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:max(0, size-i)]):
                if y:
                    c[i+j] += x*y
    return c


def pc(a, j):
    return a[j] if j < len(a) else G()


def dp(K, A):
    n = len(K)
    out = [G()]*(n+1)
    for perm in permutations(range(n)):
        factors = [[K[i][perm[i]], A[i][perm[i]]] for i in range(n)]
        if any(not x and not y for x, y in factors):
            continue
        sign = (-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = [G(sign)]
        for f in factors:
            term = pmul(term, f)
        out = padd(out, term)
    return out


def det(A):
    return dp(A, zero(len(A)))[0]


def atom_polys(K, A):
    n = len(K)
    principal = {}
    for mask in range(1 << n):
        ix = [i for i in range(n) if mask >> i & 1]
        principal[mask] = dp(sub(K, ix), sub(A, ix))
    out = {}
    for mask in range(1 << n):
        p = [G()]*(n+1)
        for sup in principal:
            if mask & sup == mask:
                sign = (-1)**(sup.bit_count()-mask.bit_count())
                p = padd(p, [sign*x for x in principal[sup]])
        mixed = [[K[i][j] if mask >> j & 1 else gg(i == j)-K[i][j]
                  for j in range(n)] for i in range(n)]
        direction = [[A[i][j] if mask >> j & 1 else -A[i][j]
                      for j in range(n)] for i in range(n)]
        assert p == dp(mixed, direction)
        assert all(not x.i for x in p)
        out[mask] = p
    assert [sum((p[j] for p in out.values()), G()) for j in range(n+1)] == [G(1)]+[G()]*n
    return out


def check_contraction(K, strict):
    n = len(K)
    assert K == adj(K)
    mins = []
    for M in (K, add(eye(n), K, -1)):
        ds = []
        for mask in range(1, 1 << n):
            ix = [i for i in range(n) if mask >> i & 1]
            q = real(det(sub(M, ix)))
            assert q > 0 if strict else q >= 0
            ds.append(q)
        mins.append(min(ds))
    return [str(x) for x in mins]


def assemble(blocks, edges):
    ix = []
    n = 0
    for C in blocks:
        ix.append(list(range(n, n+len(C))))
        n += len(C)
    K, B = zero(n), zero(n)
    for a, C in enumerate(blocks):
        for i, u in enumerate(ix[a]):
            for j, v in enumerate(ix[a]):
                K[u][v] = C[i][j]
    for (a, b), V in edges.items():
        for i, u in enumerate(ix[a]):
            for j, v in enumerate(ix[b]):
                B[u][v] = V[i][j]
                B[v][u] = V[i][j].conj()
    return K, B, ix


def block_data(C, D=None):
    n = len(C)
    D = zero(n) if D is None else D
    atoms = atom_polys(C, D)
    data = {}
    for x, p in atoms.items():
        q = real(p[0])
        if q:
            assert q > 0
            Q = [[C[i][j]-int(i == j and not (x >> i & 1)) for j in range(n)] for i in range(n)]
            R = inv(Q)
            score = real(tr(mm(R, D)))
            assert p[1] == q*score
            Rp = [[-z for z in row] for row in mm(mm(R, D), R)]
            data[x] = (q, R, score, Rp)
    return atoms, data


def covariance(C):
    n = len(C)
    return mat([[real(C[i][i])*(1-real(C[i][i])) if i == j else -C[i][j].norm2()
                 for j in range(n)] for i in range(n)])


def pair_formula(C, D, V, Ca=None, Cb=None, interior=True):
    _, da = block_data(C, Ca)
    _, db = block_data(D, Cb)
    kappa = deriv = F(0)
    table = {}
    for x, (p, R, s, Rp) in da.items():
        for y, (q, S, u, Sp) in db.items():
            T = real(tr(mm(mm(mm(R, V), S), adj(V))))
            Tp = real(tr(add(mm(mm(mm(Rp, V), S), adj(V)),
                             mm(mm(mm(R, V), Sp), adj(V)))))
            table[x, y] = T
            kappa += p*q*T*T
            deriv += p*q*((s+u)*T*T+2*T*Tp)
    # Each pair coefficient is centered in each block, including boundary cases.
    for y in db:
        assert sum(da[x][0]*table[x, y] for x in da) == 0
    for x in da:
        assert sum(db[y][0]*table[x, y] for y in db) == 0
    out = {"kappa": kappa, "kappa_derivative": deriv, "table": table}
    if interior:
        Ga, Gb = covariance(C), covariance(D)
        W = mat([[v.norm2() for v in row] for row in V])
        Ia, Ib = inv(Ga), inv(Gb)
        L = mm(mm(Ia, W), Ib)
        projection = real(tr(mm(mm(mm(Ia, W), Ib), adj(W))))
        diagonal = sum(V[i][j].norm2()**2 / (real(Ga[i][i])*real(Gb[j][j]))
                       for i in range(len(C)) for j in range(len(D)))
        residual = F(0)
        for (x, y), T in table.items():
            xa = [F(x >> i & 1)-real(C[i][i]) for i in range(len(C))]
            xb = [F(y >> j & 1)-real(D[j][j]) for j in range(len(D))]
            projected = sum(real(L[i][j])*xa[i]*xb[j] for i in range(len(C)) for j in range(len(D)))
            residual += da[x][0]*db[y][0]*(T-projected)**2
        assert kappa == projection+residual
        assert kappa >= projection >= diagonal > 0
        assert all(real(x) >= 0 for M in (Ia, Ib) for row in M for x in row)
        out.update(projection=projection, diagonal_lower_bound=diagonal, projection_residual=residual)
    return out


def formal_log(p, order):
    assert p[0]
    u = [G()] + [pc(p, k)/p[0] for k in range(1, order+1)]
    power = [G(1)]
    ans = [G()]*(order+1)
    for m in range(1, order+1):
        power = pmul(power, u, order)
        ans = padd(ans, [((-1)**(m+1))*x/m for x in power])
    return ans


def run_case(name, blocks, edges, internal=None, interior=True, order=7):
    K, B, ix = assemble(blocks, edges)
    internal = [zero(len(C)) for C in blocks] if internal is None else internal
    DD, _, _ = assemble(internal, {})
    A = add(B, DD)
    status = {"base": check_contraction(K, interior)}
    status["at_t_plus_one"] = check_contraction(add(K, A), interior)
    status["at_t_minus_one"] = check_contraction(add(K, A, -1), interior)
    atoms = atom_polys(K, A)
    block_atoms = [atom_polys(C, D) for C, D in zip(blocks, internal)]
    local_masks = {mask: tuple(sum(((mask >> g) & 1) << j for j, g in enumerate(part)) for part in ix)
                   for mask in atoms}
    # All block marginal polynomials checked separately.
    for a, part in enumerate(ix):
        for x, expected in block_atoms[a].items():
            observed = [sum((p[k] for mask, p in atoms.items() if local_masks[mask][a] == x), G())
                        for k in range(len(K)+1)]
            assert all(observed[k] == pc(expected, k) for k in range(len(observed)))
    kl = [G()]*(order+1)
    zero_atoms = []
    for mask, p in atoms.items():
        q = [G(1)]
        for a, x in enumerate(local_masks[mask]):
            q = pmul(q, block_atoms[a][x])
        assert p[0] == q[0]
        if not p[0]:
            assert not any(p)
            assert not any(q)
            zero_atoms.append(mask)
            continue
        logratio = padd(formal_log(p, order), [-x for x in formal_log(q, order)])
        kl = padd(kl, pmul(p, logratio, order))
    assert all(not x for x in kl[:4])
    pairs = {edge: pair_formula(blocks[edge[0]], blocks[edge[1]], V,
                                internal[edge[0]], internal[edge[1]], interior)
             for edge, V in edges.items()}
    kappa = sum((r["kappa"] for r in pairs.values()), F())
    deriv = sum((r["kappa_derivative"] for r in pairs.values()), F())
    assert kl[4] == kappa/2
    assert kl[5] == deriv/2
    # Exact pairwise orthogonality, density second coefficient, and F2/F3 orthogonality.
    pure = all(not x for D in internal for row in D for x in row)
    if pure:
        f2f3 = F(0)
        pair_products = {f"{e}:{f}": F() for e in pairs for f in pairs if e < f}
        for mask, p in atoms.items():
            if not p[0]:
                continue
            values = {e: -r["table"][local_masks[mask][e[0]], local_masks[mask][e[1]]]
                      for e, r in pairs.items()}
            assert p[1] == 0
            assert pc(p, 2)/p[0] == sum(values.values(), F())
            f2f3 += real(pc(p, 2)*pc(p, 3)/p[0])
            for e in pairs:
                for f in pairs:
                    if e < f:
                        pair_products[f"{e}:{f}"] += real(p[0])*values[e]*values[f]
        assert f2f3 == 0 and all(v == 0 for v in pair_products.values())
    summary_pairs = {str(e): {k: str(v) for k, v in r.items() if k != "table"} for e, r in pairs.items()}
    print(f"PASS {name}: kappa={kappa}, KL degree five={real(kl[5])}", flush=True)
    return {"K": [[str(x) for x in row] for row in K],
            "A": [[str(x) for x in row] for row in A], "blocks": ix,
            "contraction_checks": status, "zero_atoms": zero_atoms,
            "atoms": {str(x): [str(y) for y in p] for x, p in atoms.items()},
            "KL_coefficients_0_to_7": [str(real(x)) for x in kl],
            "kappa": str(kappa), "kappa_derivative": str(deriv), "pair_formulas": summary_pairs}


def main():
    halfblock = mat([[F(1, 2), F(1, 8)], [F(1, 8), F(1, 2)]])
    second = mat([[F(1, 3), F(1, 10)], [F(1, 10), F(2, 3)]])
    plus = mat([[F(1, 20), F(1, 20)], [F(1, 20), F(1, 20)]])
    minus = mat([[F(1, 20), F(1, 20)], [F(1, 20), F(-1, 20)]])
    results = {}
    results["phase_plus"] = run_case("two blocks, plus signs", [halfblock, second], {(0, 1): plus})
    results["phase_minus"] = run_case("two blocks, one sign reversed", [halfblock, second], {(0, 1): minus})
    assert results["phase_plus"]["kappa"] != results["phase_minus"]["kappa"]
    assert [[x.norm2() for x in row] for row in plus] == [[x.norm2() for x in row] for row in minus]
    # Two blocks imply an exactly even law, not merely a vanishing fifth entropy coefficient.
    for name in ("phase_plus", "phase_minus"):
        assert all(F(c) == 0 for p in results[name]["atoms"].values() for c in p[1::2])
        assert F(results[name]["KL_coefficients_0_to_7"][7]) == 0
    da = mat([[F(1, 20), G(0, F(1, 60))], [G(0, F(-1, 60)), F(-1, 30)]])
    db = mat([[F(1, 40), F(1, 70)], [F(1, 70), F(1, 50)]])
    results["moving_blocks"] = run_case("moving internal blocks", [halfblock, second], {(0, 1): minus}, [da, db])
    assert F(results["moving_blocks"]["KL_coefficients_0_to_7"][5]) != 0
    blocks = [mat([[F(2, 5), G(F(1, 12), F(1, 12))], [G(F(1, 12), F(-1, 12)), F(1, 2)]]),
              mat([[F(1, 3), G(F(1, 15), F(2, 15))], [G(F(1, 15), F(-2, 15)), F(3, 5)]]),
              mat([[F(2, 3)]])]
    edges = {(0, 1): mat([[F(1, 25), G(F(1, 30), F(1, 30))], [G(F(1, 20), F(-1, 40)), F(-1, 35)]]),
             (0, 2): mat([[G(F(1, 45), F(2, 45))], [F(1, 30)]]),
             (1, 2): mat([[F(1, 40)], [G(F(1, 50), F(-1, 50))]])}
    results["three_blocks_complex"] = run_case("three complex blocks", blocks, edges)
    assert any(F(p[3]) != 0 for p in results["three_blocks_complex"]["atoms"].values())
    assert F(results["three_blocks_complex"]["KL_coefficients_0_to_7"][7]) != 0
    v = mat([[F(3, 5)], [F(4, 5)]])
    ca = [[F(2, 5)*x for x in row] for row in mm(v, adj(v))]
    cb = mat([[F(1, 2), F(1, 10)], [F(1, 10), F(1, 3)]])
    w = mat([[F(1, 20)], [G(F(1, 30), F(1, 30))]])
    V = mm(v, adj(w))
    results["boundary_split"] = run_case("feasible noncoordinate boundary split", [ca, cb], {(0, 1): V}, interior=False)
    _, dcb = block_data(cb)
    virtual = sum(q*real(tr(mm(mm(adj(w), R), w)))**2 for q, R, _, _ in dcb.values()) / (F(2, 5)*F(3, 5))
    assert F(results["boundary_split"]["kappa"]) == virtual
    results["boundary_split"]["virtual_coordinate_kappa"] = str(virtual)
    # Full-support resolvent cancellation fails at boundary; only the needed compressed version is valid.
    _, dca = block_data(ca)
    mean = zero(2)
    for p, R, _, _ in dca.values():
        mean = add(mean, R, p)
    assert any(x for row in mean for x in row)
    assert tr(mm(mm(adj(v), mean), v)) == 0
    results["boundary_split"]["raw_mean_resolvent"] = [[str(x) for x in row] for row in mean]
    # Infeasible cross perturbation of an endpoint eigenvector.
    P = mat([[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]])
    badK, badB, _ = assemble([P, mat([[F(1, 2)]])], {(0, 1): mat([[F(1, 10)], [F(1, 10)]])})
    obstruction = dp(add(eye(3), badK, -1), [[-x for x in row] for row in badB])
    assert obstruction == [G(), G(), G(F(-1, 50)), G()]
    results["infeasible_boundary"] = {"det_I_minus_K_minus_tB": [str(x) for x in obstruction]}
    # Spectral equivalence does not identify the physical-coordinate law.
    diagonal = mat([[F(1, 4), 0], [0, F(3, 4)]])
    rotated = mat([[F(1, 2), F(-1, 4)], [F(-1, 4), F(1, 2)]])
    pa = atom_polys(diagonal, zero(2))
    pb = atom_polys(rotated, zero(2))
    assert tr(diagonal) == tr(rotated) and det(diagonal) == det(rotated)
    assert pa != pb
    results["same_spectrum_different_atoms"] = {"diagonal": [str(pa[x][0]) for x in pa], "rotated": [str(pb[x][0]) for x in pb]}
    output = {"all_exact_checks_passed": True, "arithmetic": "Python Fraction and explicit Gaussian rationals", "cases": results}
    destination = Path(__file__).with_name("061_block_gluing_exact_output.json")
    destination.write_text(json.dumps(output, indent=2)+"\n")
    print(f"PASS: all exact checks; wrote {destination.name}", flush=True)


if __name__ == "__main__":
    main()
