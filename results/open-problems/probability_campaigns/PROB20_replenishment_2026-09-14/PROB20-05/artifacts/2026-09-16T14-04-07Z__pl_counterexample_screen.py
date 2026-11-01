from __future__ import annotations

import itertools
from fractions import Fraction
from math import factorial, isqrt
import numpy as np
from scipy.optimize import linear_sum_assignment

BENCH = Fraction(1,10)


def exact_dual_certificate(C: np.ndarray, capacity: int):
    """Solve balanced transportation by duplicated-column assignment, then certify exactly.

    Sources have supply 1, targets demand `capacity`.  C is integer m x n with
    m=n*capacity.  SciPy is used only as a locator.  Exact optimality is verified
    by constructing integer dual potentials for
       max sum alpha_s + capacity sum beta_t,
       alpha_s + beta_t <= C[s,t].
    """
    ns, nt = C.shape
    assert ns == nt * capacity
    full = np.repeat(C, capacity, axis=1)
    r, c = linear_sum_assignment(full)
    assert np.array_equal(r, np.arange(ns))
    a = (c // capacity).astype(np.int64)
    counts = np.bincount(a, minlength=nt)
    assert np.all(counts == capacity)
    primal = int(C[np.arange(ns), a].sum())

    # Difference constraints beta_t-beta_a <= min_{s:a(s)=a}(C_st-C_sa).
    INF = np.iinfo(np.int64).max // 8
    w = np.full((nt, nt), INF, dtype=np.int64)
    for aa in range(nt):
        idx = np.where(a == aa)[0]
        dif = C[idx, :] - C[idx, aa, None]
        w[aa, :] = dif.min(axis=0)

    beta = np.zeros(nt, dtype=np.int64)
    # Bellman-Ford with a zero super-source.  In-place relaxations are harmless;
    # finish by direct feasibility check, which is the actual certificate.
    for _ in range(nt * nt + 1):
        changed = False
        for aa in range(nt):
            cand = beta[aa] + w[aa]
            mask = cand < beta
            if np.any(mask):
                beta[mask] = cand[mask]
                changed = True
        if not changed:
            break
    else:
        raise AssertionError("difference constraints failed to stabilize")

    alpha = C[np.arange(ns), a] - beta[a]
    slack = C - alpha[:, None] - beta[None, :]
    assert int(slack.min()) >= 0
    assert np.all(slack[np.arange(ns), a] == 0)
    dual = int(alpha.sum() + capacity * beta.sum())
    assert dual == primal
    return primal, tuple(int(x) for x in a), tuple(int(x) for x in beta)


def sqrt_bounds(fr: Fraction, D: int = 10**18):
    p, q = fr.numerator, fr.denominator
    z = (p * D * D) // q
    k = isqrt(z)
    while (k + 1) * (k + 1) * q <= p * D * D:
        k += 1
    while k * k * q > p * D * D:
        k -= 1
    ku = k if k * k * q == p * D * D else k + 1
    return Fraction(k, D), Fraction(ku, D)


def continuum_interval(primal: int, N: int, slope_abs: int):
    # Discrete midpoint approximation: cost is scaled by (2N)^2 and each
    # of N^2 source atoms has mass 1/N^2.
    A = Fraction(primal, 4 * N**4)
    source_err2 = Fraction(1, 6 * N**2)
    target_err2 = Fraction(1 + slope_abs**2, 12 * N**2)
    lA, uA = sqrt_bounds(A)
    ls, us = sqrt_bounds(source_err2)
    lt, ut = sqrt_bounds(target_err2)
    dlo = max(Fraction(0), lA - us - ut)
    dup = uA + us + ut
    return A, dlo*dlo, dup*dup


def full_branch_ty_num(N: int, m: int, kind: str):
    out = []
    for k in range(N):
        xnum = 2*k + 1
        if kind == "saw":
            ynum = (m * xnum) % (2*N)
        elif kind == "tent":
            z = (m * xnum) % (4*N)
            ynum = z if z <= 2*N else 4*N-z
        else:
            raise ValueError(kind)
        out.append(int(ynum))
    return np.array(out, dtype=np.int64)


def cost_matrix_from_ty(N: int, ty: np.ndarray):
    mids = (2*np.arange(N)+1).astype(np.int64)
    I, J = np.meshgrid(mids, mids, indexing="ij")
    sx, sy = I.ravel(), J.ravel()
    tx = mids
    return (sx[:,None]-tx[None,:])**2 + (sy[:,None]-ty[None,:])**2


def check_full_branch_examples():
    rows = []
    for kind in ("saw", "tent"):
        for m in range(2, 11):
            # Six midpoint samples per monotone branch, aligned with all breaks.
            N = 6*m
            ty = full_branch_ty_num(N, m, kind)
            C = cost_matrix_from_ty(N, ty)
            primal, _, beta = exact_dual_certificate(C, N)
            A, lo, up = continuum_interval(primal, N, m)
            assert up < BENCH
            analytic = Fraction(1, 6*m*m)
            assert analytic < BENCH
            rows.append((kind,m,N,primal,A,lo,up,analytic,min(beta),max(beta)))
    return rows


def signed_shuffle_ty_num(m: int, perm, signs, N: int):
    assert N % m == 0
    out=[]
    for k in range(N):
        xnum=2*k+1
        # branch/local coordinate exactly as rationals on denominator 2N.
        i=(m*xnum)//(2*N)
        rem=m*xnum - 2*N*i  # local u = rem/(2N)
        j=perm[i]
        if signs[i] == 1:
            # y=(j+u)/m => numerator on denominator 2N is 2N*j/m + rem/m
            num=(2*N*j + rem)//m
            assert (2*N*j + rem) % m == 0
        else:
            num=(2*N*(j+1) - rem)//m
            assert (2*N*(j+1) - rem) % m == 0
        out.append(int(num))
    return np.array(out,dtype=np.int64)


def exact_signed_shuffle_screen(max_m=5):
    summaries=[]
    for m in range(2,max_m+1):
        N=2*m
        total=0
        best=None
        best_nonext=None
        ties=0
        for perm in itertools.permutations(range(m)):
            for bits in range(1<<m):
                signs=tuple(-1 if (bits>>i)&1 else 1 for i in range(m))
                ty=signed_shuffle_ty_num(m,perm,signs,N)
                C=cost_matrix_from_ty(N,ty)
                primal,_,_=exact_dual_certificate(C,N)
                val=Fraction(primal,4*N**4)
                total+=1
                extremal = (perm == tuple(range(m)) and all(s==1 for s in signs)) or \
                           (perm == tuple(range(m-1,-1,-1)) and all(s==-1 for s in signs))
                if best is None or val>best[0]:
                    best=(val,perm,signs,primal); ties=1
                elif val==best[0]:
                    ties+=1
                if not extremal and (best_nonext is None or val>best_nonext[0]):
                    best_nonext=(val,perm,signs,primal)
        assert total == factorial(m)*(1<<m)
        summaries.append((m,N,total,best,ties,best_nonext))
    return summaries


def fmt(fr: Fraction):
    return f"{fr.numerator}/{fr.denominator} = {float(fr):.12f}"


def main():
    print("PROB20-05 exact counterexample screen")
    print("benchmark W2^2 = 1/10")
    print()
    print("A. full-branch saw/tent examples with exact transport primal-dual checks")
    rows=check_full_branch_examples()
    for kind,m,N,pr,A,lo,up,analytic,bmin,bmax in rows:
        print(f"{kind:4s} m={m:2d} N={N:3d} primal={pr:9d} discrete={fmt(A)} "
              f"continuum_interval=[{float(lo):.12f},{float(up):.12f}] "
              f"analytic_upper={fmt(analytic)} dual_beta=[{bmin},{bmax}]")
    print("ALL FULL-BRANCH FINITE CERTIFICATES PASS; all rigorous continuum upper intervals < 1/10.")
    print()
    print("B. exact coarse signed-shuffle screen (locator only; not a continuum theorem)")
    sums=exact_signed_shuffle_screen(5)
    for m,N,total,best,ties,non in sums:
        print(f"m={m} N={N} candidates={total} best={fmt(best[0])} ties={ties} "
              f"best_perm={best[1]} best_signs={best[2]}")
        print(f"    best_nonext={fmt(non[0])} perm={non[1]} signs={non[2]} primal={non[3]}")
    print("ALL SIGNED-SHUFFLE DISCRETE OPTIMA HAVE EXACT INTEGER PRIMAL-DUAL CERTIFICATES.")

if __name__ == "__main__":
    main()
