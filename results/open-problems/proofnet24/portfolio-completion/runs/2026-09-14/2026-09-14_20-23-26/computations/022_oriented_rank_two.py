"""Worker 022: deterministic checks for oriented rank-two Fisher reduction.

No randomized trials. The endpoint obstruction is checked with exact rational
arithmetic; matrix identities and scalar-root attainment use floating point.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import numpy as np


BITS = list(product((0, 1), repeat=3))
SIGMA = np.array([
    [[1, 0], [0, 1]],
    [[0, 1], [1, 0]],
    [[0, -1j], [1j, 0]],
    [[1, 0], [0, -1]],
], dtype=complex)


def det3(a):
    return (a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1])
            - a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0])
            + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0]))


def rational_atoms(k, a):
    out = []
    for bits in BITS:
        sign = (-1) ** (3 - sum(bits))
        n = [[k[i][j] - (F(1-bits[i]) if i == j else 0)
              for j in range(3)] for i in range(3)]
        p = sign * det3(n)
        dp = F(0)
        ddp = F(0)
        for j in range(3):
            mat = [[a[r][c] if c == j else n[r][c]
                    for c in range(3)] for r in range(3)]
            dp += sign * det3(mat)
            for h in range(j + 1, 3):
                mat2 = [[a[r][c] if c in (j, h) else n[r][c]
                         for c in range(3)] for r in range(3)]
                ddp += 2 * sign * det3(mat2)
        out.append((p, dp, ddp))
    assert sum(v[0] for v in out) == 1
    assert sum(v[1] for v in out) == 0
    assert sum(v[2] for v in out) == 0
    return out


def endpoint_obstruction():
    k = [[F(52 if i == j else 49, 300) for j in range(3)]
         for i in range(3)]
    a = [[F(1, 2), F(1, 2), F(0)],
         [F(1, 2), F(1, 2), F(0)],
         [F(0), F(0), F(1)]]
    atoms = rational_atoms(k, a)
    fisher = sum(dp*dp/p for p, dp, ddp in atoms)
    extreme = sum(atoms[i][1]**2/atoms[i][0] for i in (0, 7))
    assert extreme == F(12401, 2500)
    assert extreme < 5
    r0, r1 = F(10201, 597), F(39601, 29997)
    assert r0 > 16 and r1 > 1
    # beta > (99/100)*log(16) > (99/100)*(8/3) = 66/25.
    # The second strict inequality follows from log(2) > 2/3.
    beta_lower = F(66, 25)
    assert 2*beta_lower > 5
    beta = .99*np.log(float(r0)) + .01*np.log(float(r1))
    actual_curvature = -sum(float(ddp)*np.log(float(p))
                            for p, dp, ddp in atoms)
    assert abs(actual_curvature - 2*beta) < 1e-12
    return {
        "atoms_p_dp_ddp": [[str(v) for v in row] for row in atoms],
        "fisher_exact": str(fisher),
        "endpoint_fisher_exact": str(extreme),
        "beta_strict_lower_bound": str(beta_lower),
        "curvature": float(actual_curvature),
        "entropy_second_derivative": float(-fisher + actual_curvature),
        "certificate": "endpoint Fisher < 5 < 132/25 < logarithmic curvature",
    }


def numeric_atoms(k, a):
    p, dp, ddp = [], [], []
    for bits in BITS:
        n = k - np.diag(1 - np.array(bits))
        sign = (-1) ** (3 - sum(bits))
        prob = float((sign * np.linalg.det(n)).real)
        r = np.linalg.solve(n, a)
        tr = np.trace(r).real
        p.append(prob)
        dp.append(prob * tr)
        ddp.append(prob * (tr*tr - np.trace(r@r).real))
    return np.array(p), np.array(dp), np.array(ddp)


def fixed_plane(k, z):
    z = np.asarray(z, complex)
    z /= np.linalg.norm(z)
    # QR only parameterizes the direction plane; it never rotates atom labels.
    seed = np.column_stack((z, np.eye(3)[:, 0], np.eye(3)[:, 1]))
    basis, _ = np.linalg.qr(seed)
    u = basis[:, 1:]
    assert np.linalg.norm(u.conj().T@z) < 1e-12
    assert np.linalg.eigvalsh(k).min() > 0
    assert np.linalg.eigvalsh(k).max() < 1
    gram = np.zeros((4, 4))
    p = []
    for bits in BITS:
        n = k - np.diag(1-np.array(bits))
        sign = (-1)**(3-sum(bits))
        detn = np.linalg.det(n)
        prob = float((sign*detn).real)
        bmat = sign * u.conj().T @ (detn*np.linalg.inv(n)) @ u
        coeff = np.array([np.trace(bmat@s).real for s in SIGMA])
        gram += np.outer(coeff, coeff)/prob
        p.append(prob)
    p = np.array(p)
    q = float((z.conj()@k@z).real)
    weights = abs(z)**2
    rcoef = np.array([(-1)**(3-sum(bits)) *
                     (q-sum(weights[i] for i in range(3) if not bits[i]))
                     for bits in BITS])
    beta = float(-rcoef@np.log(p))
    assert beta > -1e-12
    g, v = gram[1:, 0], gram[1:, 1:]
    def secular(lam):
        return gram[0, 0]-lam-g@np.linalg.solve(v+lam*np.eye(3), g)
    lo, hi = 0., max(1., gram[0, 0])
    while secular(hi) > 0:
        hi *= 2
    for _ in range(100):
        mid = (lo+hi)/2
        if secular(mid) > 0:
            lo = mid
        else:
            hi = mid
    lam = (lo+hi)/2
    spatial = -np.linalg.solve(v+lam*np.eye(3), g)
    scalar = 1/np.sqrt(1-spatial@spatial)
    d = scalar*(SIGMA[0]+sum(spatial[i]*SIGMA[i+1] for i in range(3)))
    a = u@d@u.conj().T
    probs, dp, ddp = numeric_atoms(k, a)
    fisher = float(np.sum(dp*dp/probs))
    assert abs(np.linalg.det(d)-1) < 1e-10
    assert abs(fisher-lam) < 1e-8
    assert np.max(abs(ddp-2*rcoef)) < 1e-9
    dual = gram-lam*np.diag([1., -1., -1., -1.])
    assert np.linalg.eigvalsh(dual).min() > -1e-8
    x, w = probs[0], probs[-1]
    mixed = (q-float((z.conj()@k@k@z).real)-x*q-w*(1-q))/np.sqrt(x*w)
    ep_formula = 2*(1+np.sqrt((2*q-1)**2+mixed*mixed))
    e1 = u.conj().T @ (np.linalg.det(k)*np.linalg.inv(k)) @ u / np.sqrt(w)
    ik = np.eye(3)-k
    e0 = u.conj().T @ (np.linalg.det(ik)*np.linalg.inv(ik)) @ u / np.sqrt(x)
    assert abs(np.linalg.det(e1)-q) < 1e-10
    assert abs(np.linalg.det(e0)-(1-q)) < 1e-10
    adj_e1 = np.trace(e1)*np.eye(2)-e1
    assert abs(np.trace(adj_e1@e0).real-mixed) < 1e-10
    vals, vecs = np.linalg.eigh(np.array([[q, mixed/2], [mixed/2, 1-q]]))
    weight = vecs[:, -1]
    if weight[0] < 0:
        weight = -weight
    c = weight[0]*e1+weight[1]*e0
    ep_d = np.sqrt(np.linalg.det(c).real)*np.linalg.inv(c)
    ep_attained = np.trace(e1@ep_d).real**2+np.trace(e0@ep_d).real**2
    assert abs(ep_attained-ep_formula) < 1e-9
    counts = np.array([sum(bits) for bits in BITS])
    pc = np.array([probs[counts == j].sum() for j in range(4)])
    dc = np.array([dp[counts == j].sum() for j in range(4)])
    ddc = np.array([ddp[counts == j].sum() for j in range(4)])
    ic = float(np.sum(dc*dc/pc))
    hcard = float(-ic-ddc@np.log(pc))
    hfull = float(-fisher-ddp@np.log(probs))
    level_uniform = all(np.ptp(probs[counts == j]) < 1e-12 for j in range(4))
    identity_error = None
    if level_uniform:
        identity_error = abs(hfull-(hcard-(fisher-ic)-2*np.log(3)))
        assert identity_error < 1e-8
        assert hfull <= -2*np.log(3)+1e-9
    return {
        "kernel_eigenvalues": np.linalg.eigvalsh(k).tolist(),
        "q": q,
        "beta": beta,
        "full_fisher_minimum": lam,
        "endpoint_fisher_minimum": float(ep_formula),
        "minimum_minus_2beta": lam-2*beta,
        "attainment_error": abs(fisher-lam),
        "dual_smallest_eigenvalue": float(np.linalg.eigvalsh(dual).min()),
        "level_uniform": level_uniform,
        "cardinality_identity_error": identity_error,
    }


def main():
    examples = {
        "complex_kernel_complex_plane": (
            np.array([[.35, .12+.04j, .06-.03j],
                      [.12-.04j, .55, -.08+.02j],
                      [.06+.03j, -.08-.02j, .65]]), [1, 2j, 1+1j]),
        "exchangeable_complex_plane": (
            .17*np.eye(3)+.11*np.ones((3, 3)), [1, 2j, 1+1j]),
        "endpoint_obstruction_plane": (
            .01*np.eye(3)+(.49/3)*np.ones((3, 3)), [1, -1, 0]),
    }
    out = {"exact_endpoint_obstruction": endpoint_obstruction(),
           "fixed_examples": {name: fixed_plane(k, z)
                              for name, (k, z) in examples.items()}}
    path = Path(__file__).with_name("022_oriented_rank_two_output.json")
    path.write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
