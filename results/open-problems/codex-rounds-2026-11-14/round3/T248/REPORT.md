VERDICT: PROVED TW1 with deterministic finite-size centering for spherical inputs and Lipschitz activations of Hermite rank at least three, away from aspect ratio one

The earlier conditional application checks out. The new result completes its proposed next step for a precise subclass: independent spherical input columns; a fixed Lipschitz activation with Gaussian Hermite coefficients a_0=a_1=a_2=0 and variance v>0; N/d tending to a positive finite constant; and b_N=m/N tending to b in (0,infinity) with b!=1. For K=YY^T/N,

    [b_N^(1/6)/(v(1+sqrt(b_N))^(4/3))] N^(2/3)
       [lambda_max(K)-v(1+sqrt(b_N))^2] => TW_1.

Consequently lambda_max(K) converges in probability to v(1+sqrt(b))^2. This is a special-case result, not a solution of the full original T248 statement.

The complete argument is in [PROOF.md](PROOF.md). Its new deterministic lemma bounds the covariance-edge displacement by

    C Tr((Sigma_X-vI)^2)/N,

when Sigma_X is near vI and Tr Sigma_X=Nv. Exact trace cancellation removes the linear perturbation term. For spherical inputs and Hermite rank at least three,

    E||Sigma_X-vI||_F^2
       <= 15 v^2 N(N-1)/[d(d+2)(d+4)] = O(d^-1).

The conditional covariance edge therefore differs from v(1+sqrt(N/m))^2 by O_p(d^-2), which is negligible at the TW scale. The proof verifies covariance regularity and gives a direct Gaussian rotation proof of the quadratic-form moment bounds. A deterministic bad-sequence argument justifies uniform conditional application and removal of conditioning.

The universality input is the already identified Corollary 1.4 of Guangchen Chen and Xing Lyu, *Tracy–Widom law for sample covariance matrices under quadratic form concentration*, [arXiv:2610.41416v2](https://arxiv.org/html/2610.41416v2). Its theorem is used as stated; it is not independently reproved here. The under-five-minute literature check reopened the cited papers and found no newer complete solution. No SOLVED_ELSEWHERE.md was created. The earlier folder contains no PROOF.md or research scripts to rerun.

Independent checks are recorded in [LOG.md](LOG.md). [verify_edge.py](verify_edge.py) checks 32 two-point population spectra using both derivative bisection and independent direct minimization of the edge function; they agree within 1.776e-15. The quadratic coefficient is also checked by finite differences, with maximum relative discrepancy 3.909e-08. The spherical sixth moment is checked through two exact formulas. The matrix-transposition scale agrees within relative error 2.220e-16. These are algebra checks; no numerical TW experiment is claimed.

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_edge.py
```

The run exited successfully in under a second and used only the Python standard library. The sandbox rejected the nice priority adjustment with `setpriority: Operation not permitted`; the scalar script then ran. No further numerical program was launched. All task writes stayed inside this folder. No git or subagents were used.

What fails outside the subclass: a nonzero a_2 invalidates the Frobenius-small covariance argument; non-normalized inputs invalidate exact conditional centering and constant trace; the external theorem excludes aspect ratio one; and no proof is given for linear components, finite-rank supercritical outliers or the next eigenvalue below them, or non-Lipschitz polynomial activations. Replacing the exact aspect ratio by its limit also requires a convergence rate that is not assumed here.

Next worker: handle a nonzero second Hermite coefficient for spherical inputs in the strictly subcritical regime. First isolate its rank-one covariance component and prove a quantitative bound for the remainder; then check pole separation and the finite covariance-edge shift. Critical and supercritical spikes require an additional theorem and should be treated separately.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first clock reading 03:37:12 +04.
