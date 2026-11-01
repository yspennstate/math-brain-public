"""Adversarial test in the regime where the bound is not saturated.

Kernels of the form K(x,.) = (1-a) nu + a R(x,.) have row diameter <= a.  For random such chains
(stationary and time-inhomogeneous), random interlacings S, T with dist >= n, compare the exact
maximal correlation rho(X_S, X_T) with the paper's bounds
    Psi(sqrt(Delta)),   2 sqrt(Delta) cos(pi/(m+1)),   min(1, 2 sqrt(2 phi)),
where Delta and phi are the window-maximal row diameter and row-to-marginal distances over pairs
(s,t) with t - s >= n.  Also records the largest observed ratio rho / sqrt(Delta) and rho / sqrt(phi).
"""
import math, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from break_main_theorem import tv, maxcorr_from_joint, path_law, joint_ST, blocks, Psi, window_coefficients, random_sets, rng


def make_kernel(d, a):
    nu = rng.dirichlet(np.ones(d) * rng.uniform(0.3, 3.0))
    R = rng.dirichlet(np.ones(d) * rng.uniform(0.1, 1.0), size=d)
    if rng.uniform() < 0.5:
        # make R rows nearly deterministic to push the diameter to a
        R = R ** rng.uniform(3, 10)
        R /= R.sum(axis=1, keepdims=True)
    return (1 - a) * nu[None, :] + a * R


def stationary_law(P):
    w, v = np.linalg.eig(P.T)
    pi = np.real(v[:, np.argmin(np.abs(w - 1))])
    pi = np.abs(pi) / np.abs(pi).sum()
    return pi


def run(trials, d, L, n, max_size, stationary, sets_per_chain=12):
    viol = 0
    worst_psi = (-9, None)
    worst_ratio_delta = (0, None)
    worst_ratio_phi = (0, None)
    tests = 0
    for k in range(trials):
        a = rng.uniform(0.02, 0.6)
        if stationary:
            P = make_kernel(d, a)
            mu0 = stationary_law(P)
            kernels = [P] * L
        else:
            mu0 = rng.dirichlet(np.ones(d))
            kernels = [make_kernel(d, rng.uniform(0.02, 0.6)) for _ in range(L)]
        path = path_law(mu0, kernels)
        Delta, phi = window_coefficients(mu0, kernels, n)
        if Delta < 1e-9:
            continue
        for _ in range(sets_per_chain):
            S, T = random_sets(L, n, max_size)
            rho = maxcorr_from_joint(joint_ST(path, S, T))
            m = blocks(S, T)
            b_psi = Psi(math.sqrt(Delta))
            b_path = min(1.0, 2 * math.sqrt(Delta) * math.cos(math.pi / (m + 1)))
            b_phi = min(1.0, 2 * math.sqrt(2 * phi))
            tests += 1
            if rho > b_psi + 1e-9 or rho > b_path + 1e-9 or rho > b_phi + 1e-9:
                viol += 1
                print("VIOLATION", rho, b_psi, b_path, b_phi, Delta, phi, S, T)
            if rho - b_psi > worst_psi[0]:
                worst_psi = (rho - b_psi, (rho, b_psi, b_path, b_phi, Delta, phi, m, S, T))
            if rho / math.sqrt(Delta) > worst_ratio_delta[0]:
                worst_ratio_delta = (rho / math.sqrt(Delta), (rho, Delta, m, S, T))
            if phi > 1e-12 and rho / math.sqrt(phi) > worst_ratio_phi[0]:
                worst_ratio_phi = (rho / math.sqrt(phi), (rho, phi, m, S, T))
    tag = 'stationary' if stationary else 'inhomog.'
    print(f"{tag} d={d} L={L} n={n} max|S|+|T|={max_size}: {tests} tests, violations={viol}")
    r, info = worst_psi
    print(f"   tightest vs Psi(sqrt Delta): rho-Psi={r:+.5f}  rho={info[0]:.4f} Psi={info[1]:.4f} path={info[2]:.4f} 2sqrt(2phi)={info[3]:.4f} Delta={info[4]:.4f} phi={info[5]:.4f} m={info[6]} S={list(map(int,info[7]))} T={list(map(int,info[8]))}")
    r, info = worst_ratio_delta
    print(f"   max rho/sqrt(Delta) = {r:.4f} (paper: <= Psi(sqrt D)/sqrt D <= 2)  rho={info[0]:.4f} Delta={info[1]:.4f} m={info[2]}")
    r, info = worst_ratio_phi
    print(f"   max rho/sqrt(phi)   = {r:.4f} (paper: <= 2 sqrt 2 = 2.828)  rho={info[0]:.4f} phi={info[1]:.4f} m={info[2]}")


if __name__ == '__main__':
    for stationary in (True, False):
        for (d, L, n, ms, trials) in ((2, 11, 1, 8, 200), (3, 9, 1, 7, 200), (4, 8, 1, 6, 150), (3, 9, 2, 7, 150), (5, 7, 1, 6, 80), (6, 6, 1, 6, 40), (2, 11, 3, 8, 150)):
            run(trials, d, L, n, ms, stationary)
    print("done")
