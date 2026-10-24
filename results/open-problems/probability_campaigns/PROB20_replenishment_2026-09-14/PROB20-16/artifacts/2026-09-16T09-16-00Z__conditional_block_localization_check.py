#!/usr/bin/env python3
import itertools
import math
import numpy as np
import sympy as sp

SEED = 20260916
CASES = 200

def atom_prob(K, bits):
    n = K.shape[0]
    zeros = [i for i, b in enumerate(bits) if b == 0]
    M = K.copy().astype(complex)
    for i in zeros:
        M[i, i] -= 1
    return float((((-1) ** len(zeros)) * np.linalg.det(M)).real)

def entropy_hessian_direction(K, A):
    n = K.shape[0]
    h2 = 0.0
    psum = 0.0
    d2sum = 0.0
    for bits in itertools.product([0, 1], repeat=n):
        zeros = [i for i, b in enumerate(bits) if b == 0]
        M = K.copy().astype(complex)
        for i in zeros:
            M[i, i] -= 1
        sign = (-1) ** len(zeros)
        p = float((sign * np.linalg.det(M)).real)
        assert p > 1e-12
        Y = np.linalg.inv(M)
        tr1 = float(np.trace(Y @ A).real)
        dp = p * tr1
        d2p = p * (tr1 * tr1 - float(np.trace(Y @ A @ Y @ A).real))
        h2 += -(dp * dp / p + math.log(p) * d2p)
        psum += p
        d2sum += d2p
    assert abs(psum - 1.0) < 2e-11
    assert abs(d2sum) < 2e-10
    return h2

def conditional_pair(K, U, outside_bits):
    n = K.shape[0]
    R = [i for i in range(n) if i not in U]
    C = K[np.ix_(R, R)]
    B = K[np.ix_(U, R)]
    zeros = [i for i, b in enumerate(outside_bits) if b == 0]
    Q = C.copy().astype(complex)
    for i in zeros:
        Q[i, i] -= 1
    sign = (-1) ** len(zeros)
    mu = float((sign * np.linalg.det(Q)).real)
    assert mu > 1e-12
    F = K[np.ix_(U, U)] - B @ np.linalg.inv(Q) @ B.conj().T
    ev = np.linalg.eigvalsh(F)
    assert ev.min() > -2e-10 and ev.max() < 1 + 2e-10
    return mu, F

def symbolic_checks():
    a, b, q = sp.symbols("a b q", positive=True)
    p00 = (1-a)*(1-b)-q
    p10 = a*(1-b)+q
    p01 = (1-a)*b+q
    p11 = a*b-q
    assert sp.expand(p10*p01-p00*p11) == q
    ps = [p00,p10,p01,p11]
    ds = [-1,1,1,-1]
    hp = sp.simplify(-sum(ds[i]*(sp.log(ps[i])+1) for i in range(4)))
    target_hp = sp.log(p00*p11/(p10*p01))
    assert sp.simplify(sp.expand_log(hp-target_hp, force=True)) == 0
    hpp = sp.simplify(-sum(1/p for p in ps))
    assert sp.simplify(hpp + sum(1/p for p in ps)) == 0
    print("symbolic_two_site_identity=PASS")
    print("symbolic_entropy_derivatives=PASS")

def main():
    symbolic_checks()
    rng = np.random.default_rng(SEED)
    max_localization_error = 0.0
    max_edge_formula_error = 0.0
    largest_block_hessian = -float("inf")
    smallest_block_hessian = float("inf")
    min_edge_payment = float("inf")

    for _ in range(CASES):
        n = 5
        X = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
        H = (X + X.conj().T)/2
        H = H / np.linalg.norm(H, 2) * 0.22
        K = 0.5*np.eye(n) + H
        eig = np.linalg.eigvalsh(K)
        assert eig.min() > 0.27 and eig.max() < 0.73

        U = [0,1]
        Z = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2))
        D = (Z + Z.conj().T)/2
        D = D / np.linalg.norm(D, "fro") * 0.1
        A = np.zeros((n,n), complex)
        A[np.ix_(U,U)] = D

        full_h2 = entropy_hessian_direction(K,A)
        conditional_h2 = 0.0
        mu_sum = 0.0
        for y in itertools.product([0,1], repeat=n-2):
            mu,F = conditional_pair(K,U,y)
            conditional_h2 += mu*entropy_hessian_direction(F,D)
            mu_sum += mu
        assert abs(mu_sum-1.0) < 2e-11
        err = abs(full_h2-conditional_h2)
        max_localization_error = max(max_localization_error,err)
        largest_block_hessian = max(largest_block_hessian,full_h2)
        smallest_block_hessian = min(smallest_block_hessian,full_h2)
        assert err < 1e-10
        assert full_h2 <= 1e-10

        delta = 0.03+0.02j
        De = np.array([[0,delta],[delta.conjugate(),0]],complex)
        Ae = np.zeros((n,n),complex)
        Ae[np.ix_(U,U)] = De
        full_edge_h2 = entropy_hessian_direction(K,Ae)

        payment = 0.0
        for y in itertools.product([0,1], repeat=n-2):
            mu,F = conditional_pair(K,U,y)
            aa = float(F[0,0].real)
            bb = float(F[1,1].real)
            xi = F[0,1]
            qq = abs(xi)**2
            ps = np.array([
                (1-aa)*(1-bb)-qq,
                aa*(1-bb)+qq,
                (1-aa)*bb+qq,
                aa*bb-qq,
            ], dtype=float)
            assert ps.min() > 1e-12
            lam = math.log(ps[1]*ps[2]/(ps[0]*ps[3]))
            assert lam > -1e-11
            radial = float((xi.conjugate()*delta).real)
            term = 2*abs(delta)**2*lam + 4*radial**2*np.sum(1/ps)
            assert term > -1e-11
            payment += mu*term
        eerr = abs((-full_edge_h2)-payment)
        max_edge_formula_error = max(max_edge_formula_error,eerr)
        min_edge_payment = min(min_edge_payment,payment)
        assert eerr < 1e-10
        assert payment >= -1e-11

    print(f"seed={SEED}")
    print(f"cases={CASES}")
    print(f"max_localization_hessian_error={max_localization_error:.18e}")
    print(f"max_single_edge_formula_error={max_edge_formula_error:.18e}")
    print(f"largest_sampled_block_hessian={largest_block_hessian:.18e}")
    print(f"smallest_sampled_block_hessian={smallest_block_hessian:.18e}")
    print(f"minimum_sampled_edge_payment={min_edge_payment:.18e}")
    print("all_assertions=PASS")

if __name__ == "__main__":
    main()
