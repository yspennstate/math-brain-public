import math
import numpy as np
from statistics import NormalDist


def phi(x):
    return math.exp(-0.5*x*x)/math.sqrt(2.0*math.pi)


def run_check():
    out=[]
    alpha=6.0
    beta=1.0
    out.append("SIGNED_AFFINE_UNIVERSALITY_CHECK")
    out.append(f"alpha={alpha} beta={beta}")

    # Quantitative Gaussian-core corollary with delta_N=N^(1/4).
    # s=sqrt(4 log N) makes the standard Gaussian operator-norm tail N^-2.
    # tau is chosen so K*exp(-m^2 tau^2/(2 delta^2 L^2))=N^-2.
    for N in [10_000, 1_000_000, 100_000_000]:
        m=int(alpha*N)
        K=int(beta*N)
        delta=N**0.25
        s=math.sqrt(4.0*math.log(N))
        L=math.sqrt(m)+math.sqrt(N)+s
        tau=delta*L/m*math.sqrt(2.0*math.log(K*N**2))

        sigma=math.sqrt(1.0-1.0/m)
        a=1.0/(delta*sigma)
        neg_frac=NormalDist().cdf(-a)
        neg_mass=delta*sigma*phi(a)-NormalDist().cdf(-a)

        op_fail=math.exp(-0.5*s*s)
        cond_fail=K*math.exp(-0.5*(tau*m/(delta*L))**2)
        out.append(
            f"N={N} delta={delta:.12g} tau={tau:.12g} "
            f"op_fail={op_fail:.3e} cond_fail={cond_fail:.3e} "
            f"neg_frac={neg_frac:.12g} neg_mass={neg_mass:.12g}"
        )
        assert abs(op_fail-N**-2) <= max(1e-25,5e-12*N**-2)
        assert abs(cond_fail-N**-2) <= max(1e-25,5e-12*N**-2)

    # Finite-dimensional sanity: rows sum to one but have negative coefficients;
    # W and B are full rank for this deterministic seeded realization.
    rng=np.random.default_rng(20260920)
    N=24
    m=80
    K=N
    delta=3.0
    A=rng.normal(size=(m,N))
    Z=rng.normal(size=(K,m))
    PZ=Z-Z.mean(axis=1,keepdims=True)
    W=np.full((K,m),1.0/m)+delta/m*PZ
    B=W@A
    rowsums=W.sum(axis=1)
    out.append(f"finite_rowsum_maxerr={np.max(np.abs(rowsums-1.0)):.3e}")
    out.append(f"finite_negative_fraction={np.mean(W<0):.12g}")
    out.append(
        f"finite_rank_W={np.linalg.matrix_rank(W)} "
        f"finite_rank_B={np.linalg.matrix_rank(B)}"
    )
    assert np.max(np.abs(rowsums-1.0))<1e-12
    assert np.any(W<0)
    assert np.linalg.matrix_rank(W)==K
    assert np.linalg.matrix_rank(B)==N

    # One-row Gaussian tail sanity for a constructed projection vector y whose
    # coordinates all clear kappa+tau0.
    kappa=-1.0
    tau0=0.25
    y=(kappa+tau0)+rng.exponential(scale=0.8,size=m)
    Py=y-y.mean()
    sd=delta*np.linalg.norm(Py)/m
    exact_fail=NormalDist().cdf((kappa-y.mean())/sd)
    bound=math.exp(-0.5*(tau0*m/(delta*np.linalg.norm(Py)))**2)
    out.append(
        f"single_row_exact_fail={exact_fail:.12g} "
        f"gaussian_bound={bound:.12g}"
    )
    assert exact_fail<=bound+1e-15

    # A coordinate of an added row is a nontrivial Gaussian variance mixture.
    qmean=m-1
    Vmean=1.0/m+delta**2*qmean/m**2
    Vvar=delta**4*2.0*qmean/m**4
    kurt=3.0*(1.0+Vvar/Vmean**2)
    out.append(
        f"marginal_variance={Vmean:.12g} "
        f"standardized_fourth={kurt:.12g}"
    )
    assert kurt>3.0

    out.append("ALL_SIGNED_AFFINE_CHECKS_PASS")
    return "\n".join(out)


if __name__ == "__main__":
    print(run_check())
