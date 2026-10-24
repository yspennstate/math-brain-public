#!/usr/bin/env python3
"""Exact C055 certificates plus labeled numerical illustrations."""
from pathlib import Path
import itertools
import json
import sympy as S
import mpmath as mp

ROOT = Path(__file__).resolve().parent
mp.mp.dps = 75
t, z, s = S.symbols("t z s", real=True)
I = S.I
R = S.Rational
MASKS2 = list(range(4))
MASKS4 = list(range(16))


def simple(x):
    return S.cancel(S.expand(x))


def assert_zero(x):
    if isinstance(x, S.MatrixBase):
        assert all(simple(e) == 0 for e in x)
    else:
        assert simple(x) == 0, x


def atoms(K):
    n = K.rows
    out = []
    for mask in range(1 << n):
        absent = [j for j in range(n) if not mask & (1 << j)]
        M = K - S.diag(*[int(j in absent) for j in range(n)])
        out.append(simple((-1) ** len(absent) * M.det()))
    assert_zero(sum(out) - 1)
    return out


def conj_norm2(M):
    return simple(sum(e * S.conjugate(e) for e in M))


def fourth(e):
    return simple((e * S.conjugate(e)) ** 2)


def marginal(p, keep, n):
    out = [S.Integer(0)] * (1 << len(keep))
    for mask, val in enumerate(p):
        small = sum(((mask >> j) & 1) << k for k, j in enumerate(keep))
        out[small] += val
    return [simple(v) for v in out]


def gershgorin(K):
    rows = []
    for j in range(K.rows):
        bound = sum(abs(S.re(K[j, k])) + abs(S.im(K[j, k]))
                    for k in range(K.cols) if j != k)
        assert K[j, j] > bound
        assert 1 - K[j, j] > bound
        rows.append([str(K[j, j] - bound), str(K[j, j] + bound)])
    return rows


def num(x):
    return mp.mpf(str(S.N(x, 80)))


def vec_num(v, tau):
    return [num(x.subs(t, tau)) for x in v]


def entropy(p):
    return -sum(x * mp.log(x) for x in p if x)


def kl(p, q):
    return sum(x * mp.log(x / y) for x, y in zip(p, q) if x)


def fmt(x):
    return mp.nstr(x, 45)


# Generic two-site determinant/Bregman coefficient, with complex coherence.
a, b, u, v, cr, ci, vr, vi = S.symbols("a b u v cr ci vr vi", real=True)
F0 = S.Matrix([[a, cr + I * ci], [cr - I * ci, b]])
E = S.Matrix([[u, vr + I * vi], [vr - I * vi, v]])
p0, p1, pt = atoms(F0), atoms(F0 + E), atoms(F0 + t * E)
delta = simple(E.det())
for k, sign in enumerate([1, -1, -1, 1]):
    assert_zero((1-t)*p0[k] + t*p1[k] - pt[k] - t*(1-t)*delta*sign)
assert_zero(p0[1]*p0[2] - p0[0]*p0[3] - cr**2-ci**2)

# Exact Green moments and the completed positive-square identity.
moments = [simple(S.integrate((1-t)*s**(k+1), (s, 0, t))
                  + S.integrate(t*(1-s)*s**k, (s, t, 1))) for k in range(3)]
for k in range(3):
    assert_zero(moments[k] - t*(1-t)*sum(t**j for j in range(k+1))/((k+1)*(k+2)))
bt, vt = cr + I*ci, vr + I*vi
d = 1+t+t*t
quadratic = (moments[0]*(bt*S.conjugate(bt))
             + moments[1]*(bt*S.conjugate(vt)+S.conjugate(bt)*vt)
             + moments[2]*vt*S.conjugate(vt))/(t*(1-t))
shift = vt + 2*(1+t)*bt/d
square_form = (R(1,18)+(1-t)**2/(9*d))*bt*S.conjugate(bt) + d*shift*S.conjugate(shift)/12
assert_zero(quadratic-square_form)

B = S.Matrix([[R(3,10), R(1,5)], [R(1,5), R(7,20)]])
DO = S.diag(R(2,5), R(11,20))
V = S.Matrix([[R(1,25), (2+I)/80], [(1+2*I)/80, -R(3,100)]])
C = S.Matrix([[R(9,20), (2-I)/50], [(2+I)/50, R(1,2)]])
As = {
    "definite": S.Matrix([[R(11,20), (12+I)/50], [(12-I)/50, R(3,5)]]),
    "indefinite": S.Matrix([[R(9,20), (7+2*I)/50], [(7-2*I)/50, R(3,10)]])
}
D = S.diag(B, DO)
pB = atoms(B)
pDO = atoms(DO)
pD = atoms(D)
q1 = atoms(C)
Ct = DO+t*(C-DO)
qy = atoms(Ct)
r = simple(B[0,1]*B[1,0])
d2 = simple(sum((C[j,j]-DO[j,j])**2 for j in range(2)))
e4 = fourth(C[0,1])
v4 = simple(sum(fourth(e) for e in V))
assert r == R(1,25)
assert simple(V.det()) == -R(3,2500)-I/R(1280)

certificate = {
    "generic_pair_atom_identity": "PASS",
    "generic_pair_odds_identity": "PASS",
    "green_moments": [str(x) for x in moments],
    "green_positive_square": "PASS",
    "D_gershgorin_intervals": gershgorin(D),
    "B": [[str(e) for e in row] for row in B.tolist()],
    "V": [[str(e) for e in row] for row in V.tolist()],
    "C": [[str(e) for e in row] for row in C.tolist()],
    "detV": str(simple(V.det())),
    "r_d2_e4_v4": list(map(str, [r,d2,e4,v4])),
    "examples": {}
}
results = {"status": "PASS", "scope": "exact identities and numerical illustrations; theorem signs are analytic", "examples": {}}

for name, A in As.items():
    K = A.row_join(V).col_join(V.conjugate().T.row_join(C))
    pK = atoms(K)
    Kt = D+t*(K-D)
    pKt = atoms(Kt)
    Mz = A.row_join(z*V).col_join((z*V.conjugate().T).row_join(DO+z*z*(C-DO)))
    pMz = atoms(Mz)
    pMt = []
    for poly in pMz:
        coeffs = S.Poly(poly, z)
        assert all(deg[0] % 2 == 0 for deg, val in coeffs.terms())
        pMt.append(simple(sum(val*t**(deg[0]//2) for deg, val in coeffs.terms())))

    # Exact classical exterior replacement against all 16 atom polynomials.
    for out in MASKS4:
        sx, sy = out & 3, out >> 2
        replaced = 0
        for old_y in MASKS2:
            trans = 1
            for j in range(2):
                bit = (sy >> j) & 1
                mu = DO[j,j] if bit else 1-DO[j,j]
                trans *= t*int(bit == ((old_y >> j)&1))+(1-t)*mu
            replaced += pK[sx+4*old_y]*trans
        assert_zero(replaced-pMt[out])
    for y in MASKS2:
        assert_zero(sum(pMt[x+4*y] for x in MASKS2)-qy[y])
        assert_zero(sum(pKt[x+4*y] for x in MASKS2)-qy[y])

    Fs, Gs, pFs, pGs, deltas = [], [], [], [], []
    for y in MASKS2:
        Q = Ct-S.diag(*[int(not(y & (1<<j))) for j in range(2)])
        F = (A-t*V*Q.inv()*V.conjugate().T).applyfunc(simple)
        G = ((1-t)*B+t*F).applyfunc(simple)
        pf, pg = atoms(F), atoms(G)
        dy = simple((F-B).det())
        for x, sign in enumerate([1,-1,-1,1]):
            assert_zero(qy[y]*pf[x]-pMt[x+4*y])
            assert_zero(qy[y]*pg[x]-pKt[x+4*y])
            assert_zero((1-t)*pB[x]+t*pf[x]-pg[x]-t*(1-t)*dy*sign)
        Fs.append(F); Gs.append(G); pFs.append(pf); pGs.append(pg); deltas.append(dy)

    assert_zero(sum((qy[y]*Fs[y] for y in MASKS2), S.zeros(2))-A)
    for j in range(2):
        covariance = sum((qy[y]*(Fs[y]-A)*(int(bool(y & (1<<j)))-Ct[j,j]) for y in MASKS2), S.zeros(2))
        assert_zero(covariance+t*V[:,j]*V[:,j].conjugate().T)

    delta_mid = [simple(dy.subs(t,R(1,2))) for dy in deltas]
    assert all(dy > 0 for dy in delta_mid) if name == "definite" else all(dy < 0 for dy in delta_mid)
    a2 = conj_norm2(A-B)
    uniform_bracket = simple(2*r*a2/9+2*d2+8*e4/3+r*v4/9)
    conditional_coherence_floor = simple(R(2,9)*R(1,4)*r*a2)
    certificate["examples"][name] = {
        "A": [[str(e) for e in row] for row in A.tolist()],
        "gershgorin_intervals": gershgorin(K),
        "det_A_minus_B": str(simple((A-B).det())),
        "conditional_determinants_at_half": list(map(str,delta_mid)),
        "conditional_probabilities_at_half": [str(simple(q.subs(t,R(1,2)))) for q in qy],
        "uniform_bracket": str(uniform_bracket),
        "new_pair_lower_bound_at_half": str(conditional_coherence_floor),
        "atom_polynomials_Kt": [str(x) for x in pKt],
        "atom_polynomials_Mt": [str(x) for x in pMt],
        "identities": "All atoms, classical replacement, both conditional laws, pair correction, matrix conditional mean and cross moments PASS"
    }

    numeric_rows=[]
    for tau in [R(1,4),R(1,2),R(3,4)]:
        tt=num(tau)
        pk, pd, pk_t, pm_t, qb, qd, qc, qt = [vec_num(x,tau) for x in [pK,pD,pKt,pMt,pB,pDO,q1,qy]]
        gap=entropy(pk_t)-(1-tt)*entropy(pd)-tt*entropy(pk)
        exterior=entropy(qt)-(1-tt)*entropy(qd)-tt*entropy(qc)
        loss=(entropy(pm_t)-entropy(qt))-(entropy(pk)-entropy(qc))
        pair_remainder=mp.mpf(0); correction=mp.mpf(0); pairgap=mp.mpf(0)
        conditional_norm=mp.mpf(0)
        for y in MASKS2:
            pf,pg=vec_num(pFs[y],tau),vec_num(pGs[y],tau)
            rem=(1-tt)*kl(qb,pg)+tt*kl(pf,pg)
            odds=mp.log(pg[1]*pg[2]/(pg[0]*pg[3]))
            corr=-tt*(1-tt)*num(deltas[y].subs(t,tau))*odds
            pair_remainder+=qt[y]*rem; correction+=qt[y]*corr
            pairgap+=qt[y]*(entropy(pg)-(1-tt)*entropy(qb)-tt*entropy(pf))
            conditional_norm+=qt[y]*num(conj_norm2(Fs[y]-B).subs(t,tau))
        assert abs(pairgap-pair_remainder-correction)<mp.mpf("1e-65")
        assert abs(gap-exterior-tt*loss-pair_remainder-correction)<mp.mpf("1e-65")

        # Retention-index mutual information and the exact Shearer KL slack.
        retention_info=mp.mpf(0); selected_entropy=mp.mpf(0)
        for mask in MASKS2:
            weight=tt**mask.bit_count()*(1-tt)**(2-mask.bit_count())
            channel_law=[]
            for out in MASKS2:
                val=mp.mpf(0)
                for old in MASKS2:
                    trans=mp.mpf(1)
                    for j in range(2):
                        out_bit=(out>>j)&1
                        if mask & (1<<j):
                            trans*=int(out_bit==((old>>j)&1))
                        else:
                            trans*=num(DO[j,j]) if out_bit else 1-num(DO[j,j])
                    val+=qc[old]*trans
                channel_law.append(val)
            retention_info+=weight*kl(channel_law,qt)
            keep=[j for j in range(2) if mask & (1<<j)]
            selected_entropy+=weight*entropy(vec_num(marginal(q1,keep,2),tau))
        shearer=selected_entropy-tt*entropy(qc)
        assert abs(exterior-retention_info-shearer)<mp.mpf("1e-65")
        positive_bregman=retention_info+shearer+tt*loss+pair_remainder
        assert abs(gap-positive_bregman-correction)<mp.mpf("1e-65")

        floor=num(uniform_bracket)*tt*(1-tt)
        param_bracket=2*r*a2/9+2*d2+8*(1+tau+tau*tau)*e4/3+(4*(1-tau)+R(8,9)*r*tau*tau)*v4/2
        param_floor=num(param_bracket)*tt*(1-tt)
        pair_floor=R(2,9)*r*tt*(1-tt)*conditional_norm
        old_det_floor=4*tt*(1-tt)*sum(qt[y]*max(mp.mpf(0),num(deltas[y].subs(t,tau))) for y in MASKS2)
        assert gap>=param_floor>=floor>0
        assert pairgap>=pair_floor
        assert all(x>=-mp.mpf("1e-65") for x in [retention_info,shearer,loss,pair_remainder])
        if name=="indefinite" and tau==R(1,2):
            assert old_det_floor==0 and pair_floor>0
        numeric_rows.append({
            "t":str(tau),"entropy_gap":fmt(gap),"positive_Bregman_sum":fmt(positive_bregman),
            "signed_determinant_correction":fmt(correction),"retention_index_KL":fmt(retention_info),
            "Shearer_KL_slack":fmt(shearer),"t_information_loss":fmt(tt*loss),
            "conditional_pair_Bregman":fmt(pair_remainder),"actual_conditional_pair_gap":fmt(pairgap),
            "new_conditional_pair_coherence_floor":fmt(pair_floor),"prior_positive_determinant_floor":fmt(old_det_floor),
            "parameter_dependent_global_floor":fmt(param_floor),"uniform_global_floor":fmt(floor)
        })
    results["examples"][name]=numeric_rows

ROOT.mkdir(parents=True,exist_ok=True)
(ROOT/"exact_certificate.json").write_text(json.dumps(certificate,indent=2)+"\n")
(ROOT/"results.json").write_text(json.dumps(results,indent=2)+"\n")
print("PASS: exact determinant, conditional, replacement, moment, and positive-square identities.")
for name, rows in results["examples"].items():
    mid=rows[1]
    print(name, "midpoint gap",mid["entropy_gap"],"uniform floor",mid["uniform_global_floor"],
          "signed correction",mid["signed_determinant_correction"])
