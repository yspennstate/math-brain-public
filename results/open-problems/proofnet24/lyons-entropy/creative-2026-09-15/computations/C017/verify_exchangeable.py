"""Exact polynomial verification and independent high-precision diagnostics.

Run from the campaign root: python computations/C017/verify_exchangeable.py
The proof is in agents/C017.md; numerical diagnostics are not universal proofs.
"""
from pathlib import Path
import json
import sympy as sp
import mpmath as mp

HERE = Path(__file__).resolve().parent


def symbolic_check():
    x, r, U, V = sp.symbols("x r U V", positive=True)
    a = x / (1 + x)
    c = x * r / (1 + x * r)
    p = (1 - a) ** 2 * (1 - c)
    mu = 2 * a + c
    v = 2 * a * (1 - a) + c * (1 - c)
    W = sp.factor((1 - p) * v - p * mu ** 2)
    Q = 2*r*r*x*x + 4*r*r*x + 2*r*r + r*x*x + 8*r*x + 5*r + 2
    assert sp.cancel(W - x**3 * Q / ((1+x)**4*(1+x*r)**2)) == 0
    F11 = 4*(1+x)**2*(r**3*x**3+2*r**3*x**2+r**3*x+3*r*r*x*x+
                       2*r*r*x+4*r*x+2*r+1)/(x*(1+r*x)*Q)
    F12 = 2*(1+x)**2*(1+r*x)*(r*x+2*r+1)/(x*Q)
    F22 = (1+r*x)**2*(2*r+x*x+4*x+1)/(x*Q)
    direct = [
        4*((1-p)-2*p*mu/(1-a)+p*v/(1-a)**2)/W,
        2*((1-p)-p*mu*(1/(1-a)+1/(1-c))+p*v/((1-a)*(1-c)))/W,
        ((1-p)-2*p*mu/(1-c)+p*v/(1-c)**2)/W,
    ]
    for claim, expression in zip([F11, F12, F22], direct):
        assert sp.cancel(claim-expression) == 0
    detF = 4*p*(c-a)**2/((1-a)**2*(1-c)**2*W)
    assert sp.cancel(F11*F22-F12*F12-detF) == 0
    m, t = (U+x*r*V)/(1+x*r), (U+x*V)/(1+x)
    d2 = (r-1)**2
    q = [
        2*((6*r+3)*U+2*d2),
        2*(-(4*r*r+10*r+4)*U*U+(6*r*r+27*r+6)*U+
           (-2*r*r+7*r+4)*V+2*d2*(r+4)),
        2*(-(8*r*r+16*r)*U*U-(8*r*r+20*r+8)*U*V+
           (24*r*r+40*r+2)*U+(-2*r**3+3*r*r+26*r+12)*V+
           4*d2*(2*r+3)),
        4*(-(2*r*r+r)*U*U-(8*r*r+16*r)*U*V+
           (17*r*r+11*r-1)*U-(2*r*r+5*r+2)*V*V+
           (-2*r**3+10*r*r+19*r+6)*V+2*d2*(3*r+2)),
        2*(-(8*r*r+4*r)*U*V+(20*r*r+2*r-1)*U-
           (8*r*r+16*r)*V*V+(-2*r**3+26*r*r+26*r+4)*V+
           2*d2*(4*r+1)),
        2*r*((4*r-1)*U-(4*r+2)*V*V+(14*r+7)*V+2*d2),
        6*V*r*r,
    ]
    denominator = x*(1+x)**2*Q
    detG = detF-2*m*F22+4*t*F12-4*t*t
    assert sp.cancel(detG*denominator-sum(q[j]*x**j for j in range(7))) == 0
    assert sp.expand((2*r+1)*(r+2)**2-2*r*(r-1)**2) == 13*r*r+10*r+4
    # Exact coefficient bookkeeping for the three UV absorptions.
    assert sp.expand(24*r*r+40*r+2-(8*r*r+20*r+8)/3) == (64*r*r+100*r-2)/3
    assert sp.expand(17*r*r+11*r-1-(8*r*r+16*r)/3) == (43*r*r+17*r-3)/3
    assert sp.expand(20*r*r+2*r-1-(8*r*r+4*r)/3) == (52*r*r+2*r-3)/3
    return {"determinant_identity": "PASS", "fisher_inverse_identity": "PASS",
            "coefficient_and_log_bound_identities": "PASS"}


def trace(M):
    return sum(M[i, i] for i in range(M.rows))


def real_matrix(M):
    return mp.matrix([[mp.re(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])


def frob(M):
    return mp.sqrt(sum(abs(z)**2 for z in M))


def diagnostic(a_s, c_s):
    a, c = mp.mpf(a_s), mp.mpf(c_s)
    I = mp.eye(3)
    P = mp.matrix([[mp.mpf(1)/3 for j in range(3)] for i in range(3)])
    K = a*(I-P)+c*P
    basis = []
    for i in range(3):
        B = mp.zeros(3)
        B[i, i] = 1
        basis.append(B)
    for imaginary in (False, True):
        for i, j in ((0, 1), (0, 2), (1, 2)):
            B = mp.zeros(3)
            B[i, j] = (1j if imaginary else 1)/mp.sqrt(2)
            B[j, i] = mp.conj(B[i, j])
            basis.append(B)
    FI, frozen = mp.zeros(9), mp.zeros(9)
    for mask in range(8):
        Q = K.copy()
        for i in range(3):
            if not (mask >> i) & 1:
                Q[i, i] -= 1
        p = mp.re((-1)**(3-mask.bit_count())*mp.det(Q))
        assert p > 0
        Qinv = Q**-1
        T = [Qinv*B for B in basis]
        scores = [mp.re(trace(Z)) for Z in T]
        for i in range(9):
            for j in range(9):
                FI[i, j] += p*scores[i]*scores[j]
                mixed = mp.re(scores[i]*scores[j]-trace(T[i]*T[j]))
                frozen[i, j] -= p*mp.log(p)*mixed
    H = frozen-FI
    x = a/(1-a)
    r = (c/(1-c))/x
    U = mp.log((r+2)**2/(3*(2*r+1)))
    V = mp.log((2*r+1)**2/(3*r*(r+2)))
    m, t = (1-c)*U+c*V, (1-a)*U+a*V
    R = mp.matrix([[2*m, 2*t], [2*t, 0]])
    p = (1-a)**2*(1-c)
    mu, v = 2*a+c, 2*a*(1-a)+c*(1-c)
    Cov = mp.matrix([[v, -p*mu], [-p*mu, p*(1-p)]])
    J = mp.matrix([[2, 1], [-2*p/(1-a), -p/(1-c)]])
    F = J.T*(Cov**-1)*J
    G = F-R
    inv_dirs = [I-P, P]
    coord = mp.matrix([[mp.re(trace(basis[i]*inv_dirs[j])) for j in range(2)] for i in range(9)])
    exact_frozen = coord.T*frozen*coord
    assert frob(exact_frozen-R) < mp.mpf("1e-55")*(1+frob(R))
    residual_fisher = coord.T*FI*coord-F
    fisher_min = mp.eigsy(residual_fisher, eigvals_only=True)[0]
    assert fisher_min > -mp.mpf("1e-55")*(1+frob(FI))
    unit_coord = coord.copy()
    for i in range(9):
        unit_coord[i, 0] /= mp.sqrt(2)
    projection = unit_coord*unit_coord.T
    cross = frob(projection*H*(mp.eye(9)-projection))
    assert cross < mp.mpf("1e-55")*(1+frob(H))
    hess_eigs = mp.eigsy(H, eigvals_only=True)
    # Complement the count+empty diagnostic if c<a, as in the proof.
    Gmin = mp.eigsy(G, eigvals_only=True)[0]
    if c > a:
        assert Gmin > 0
    if c != a:
        assert hess_eigs[8] < 0
    else:
        assert abs(hess_eigs[8]) < mp.mpf("1e-55")
    return {"a": a_s, "c": c_s,
            "full_hessian_largest_eigenvalue": mp.nstr(hess_eigs[8], 30),
            "count_empty_compensation_min_eigenvalue": mp.nstr(Gmin, 30),
            "fisher_residual_min_eigenvalue": mp.nstr(fisher_min, 12),
            "symmetry_cross_norm": mp.nstr(cross, 5)}


if __name__ == "__main__":
    output = symbolic_check()
    mp.mp.dps = 90
    samples = [
        ("0.1", "0.9"), ("0.8", "0.9"),
        ("0.0000001", "0.8"), ("0.4", "0.9999999999"),
        ("0.00000001", "0.99999999"),
        ("0.99999999", "0.9999999999"),
        ("0.75", "0.2"), ("0.3", "0.3"),
        ("0.333333333333333333", "0.333334333333333333"),
    ]
    output["full_hessian_diagnostics"] = [diagnostic(a, c) for a, c in samples]
    output["status"] = "PASS"
    (HERE / "verification_results.json").write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, indent=2))
