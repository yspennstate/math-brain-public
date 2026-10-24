"""Finite algebraic checks for REPORT.md, not a universal proof certificate.

Requires Python 3.10+, NumPy, and SymPy. No network, credentials, model calls,
remote jobs, or user-file changes are used. Output stays beside this script.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


def orthogonal(rng: np.random.Generator, n: int) -> np.ndarray:
    q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    return q


def main() -> None:
    rng = np.random.default_rng(230922)
    field_errors: list[float] = []
    geometric_ratios: list[float] = []
    root_ratios: list[float] = []
    for n in (3, 4, 7, 12, 25):
        for case in range(8):
            frame = orthogonal(rng, n)
            u = frame[:, :3]
            lam = rng.choice([-1., 1.], 3) * rng.uniform(1., 8., 3)
            # Other eigenvalues range over signs and many scales; no rank assumption.
            tail = rng.choice([-1., 1.], n-3) * 10. ** rng.uniform(-6., 5., n-3)
            a = (frame * np.concatenate([lam, tail])) @ frame.T
            b = rng.standard_normal(n)
            p = u @ u.T
            z0 = u @ (-0.5 * (u.T @ b) / lam)
            x = rng.standard_normal(n)
            grad = 2. * a @ x + b
            g = p @ grad
            stable_g = u @ (2. * lam * (u.T @ x) + u.T @ b)
            assert np.linalg.norm(g-stable_g) <= 2e-8 * (1.+np.linalg.norm(grad))
            identity_error = abs(grad @ g - g @ g) / (1.+abs(grad @ g))
            field_errors.append(float(identity_error))
            assert identity_error < 1e-7
            assert np.sum(np.abs(grad*g)) + 1e-7 >= g@g
            leverage = np.sum(u*u, axis=1)
            assert abs(leverage.sum()-3.) < 1e-11
            assert np.sqrt(leverage).sum() <= math.sqrt(3*n)+1e-11
            sigma = float(np.min(np.abs(lam)))
            for i in range(n):
                # Nullspace of row i, transported to E, is a physical-i-free 2-plane.
                _, _, vt = np.linalg.svd(u[i:i+1, :], full_matrices=True)
                wi = u @ vt[1:].T
                assert np.linalg.norm(wi.T@wi-np.eye(2)) < 1e-11
                assert np.linalg.norm(wi[i]) < 1e-11
                radius = np.linalg.norm(wi.T@(x-z0))
                lhs = abs(stable_g[i]) / (stable_g@stable_g)
                rhs = math.sqrt(leverage[i]) / (2.*sigma*radius)
                geometric_ratios.append(float(lhs/rhs))
                assert lhs <= rhs*(1.+1e-9)+1e-12
                # Roots at a target defined from a real sample (no assumed random-law cap).
                target = float(x@a@x+b@x)
                others = x.copy(); others[i] = 0.
                aa = float(a[i,i])
                bb = float(2.*a[i]@others+b[i])
                cc = float(others@a@others+b@others-target)
                roots = np.roots([aa, bb, cc]) if abs(aa)>1e-12 else np.roots([bb,cc])
                total = 0.
                for root in roots:
                    if abs(root.imag) > 1e-7:
                        continue
                    xr = others.copy(); xr[i] = root.real
                    gr = u @ (2.*lam*(u.T@xr)+u.T@b)
                    total += abs(gr[i])/(gr@gr)
                two_root_bound = math.sqrt(leverage[i])/(sigma*radius)
                root_ratios.append(float(total/two_root_bound))
                assert total <= two_root_bound*(1.+1e-7)+1e-10

    # Exact symbolic Jacobian for the ruled surface (one-sheet side s>0).
    s, theta, t = sp.symbols('s theta t', positive=True, real=True)
    z = sp.Matrix([sp.sqrt(s)*sp.cos(theta)-t*sp.sin(theta),
                   sp.sqrt(s)*sp.sin(theta)+t*sp.cos(theta), t])
    quad = z[0]**2+z[1]**2-z[2]**2
    assert sp.trigsimp(sp.expand(quad-s)) == 0
    jac = sp.trigsimp(sp.simplify(sp.det(z.jacobian([s,theta,t]))))
    assert jac == sp.Rational(1,2)
    surface_cross = z.diff(theta).cross(z.diff(t))
    gradient = sp.Matrix([2*z[0],2*z[1],-2*z[2]])
    assert sp.trigsimp(sp.expand(4*surface_cross.dot(surface_cross)-gradient.dot(gradient))) == 0

    core_ratios: list[float] = []
    core_case_count = 0
    for m in (3, 4, 7, 15, 30):
        for _ in range(10):
            v = orthogonal(rng, m)[:, :3]
            r = orthogonal(rng, 3)
            ge = rng.uniform(.8, .98, 3)
            gsqrt = (r*np.sqrt(ge))@r.T
            uh = v@gsqrt
            w = orthogonal(rng, 3)
            lams = rng.choice([-1.,1.],3)*rng.uniform(1.,4.,3)
            lam = (w*lams)@w.T
            base = uh@lam@uh.T
            raw = rng.standard_normal((m,m)); raw = (raw+raw.T)/2.
            perturbation = .1*raw/np.linalg.norm(raw,2)
            block = base+perturbation
            lower = float(ge.min()*np.abs(lams).min()-.1)
            third = float(np.linalg.svd(block,compute_uv=False)[2])
            assert third+1e-9 >= lower
            core_ratios.append(third/lower)
            core_case_count += 1

    schur_mins: list[float] = []
    for n in (3,5,10,20):
        for _ in range(10):
            u = orthogonal(rng,n)[:,:3]
            lam = rng.uniform(1.,6.,3)
            a = (u*lam)@u.T
            i = int(np.argmax(np.diag(a)))
            j = [k for k in range(n) if k != i]
            schur = a[np.ix_(j,j)]-np.outer(a[j,i],a[j,i])/a[i,i]
            eig = np.linalg.eigvalsh(schur)
            assert eig[0] > -1e-10
            assert eig[-2] >= np.min(lam)-1e-10
            if len(eig)>2:
                assert np.max(np.abs(eig[:-2])) < 1e-9
            schur_mins.append(float(eig[-2]/np.min(lam)))

    bound = 2.*math.sqrt(180.*math.pi)/.7
    assert bound < 68.
    constants = {
        'general_sqrt_n_prefactor': 2.*math.sqrt(6.*math.pi),
        'localized_core_example': bound,
        'semidefinite_rank3_existing_bound': 3.*math.e,
        'semidefinite_heavy_branch': 4.*math.sqrt(math.pi),
        'ruled_one_sheet_bound': math.pi*math.sqrt(2.),
    }
    assert constants['semidefinite_heavy_branch'] < constants['semidefinite_rank3_existing_bound']
    result = {
        'status': 'PASS',
        'scope': 'Finite algebra and matrix regressions; analytic proof supplied separately. No full-conjecture certificate.',
        'projected_field': {
            'matrices':len(field_errors),
            'max_relative_identity_error':max(field_errors),
            'fiber_geometric_checks':len(geometric_ratios),
            'max_single_term_ratio':max(geometric_ratios),
            'max_two_root_ratio':max(root_ratios),
        },
        'ruled_jacobian': {'exact_parameter_volume_jacobian':str(jac), 'coarea_cross_product_identity':'PASS'},
        'core_spectral_transfer': {'cases':core_case_count,'min_third_singular_over_lower_bound':min(core_ratios)},
        'psd_rank3_schur': {'cases':len(schur_mins),'min_second_schur_eigenvalue_over_min_input':min(schur_mins)},
        'constants':constants,
        'full_conjecture_verified':False,
        'independent_end_to_end_review_completed':False,
    }
    text = json.dumps(result,indent=2)+'\n'
    Path(__file__).with_name('check_results.json').write_text(text,encoding='utf-8')
    print(text)


if __name__ == '__main__':
    main()
