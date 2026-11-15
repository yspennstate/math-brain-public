VERDICT: PROVED TW1 with deterministic finite-size centering for the projected spherical kernel with any fixed polynomial activation of Hermite rank at least two

The round 5 result holds on rechecking. This session removes its Lipschitz
restriction for fixed polynomial activations. Let X have independent
spherical columns of radius sqrt(d), let W have independent standard real
Gaussian entries, and assume N/d tends to alpha in (0,infinity) and
b_N=m/N tends to b in (0,infinity), b!=1. For any fixed nonzero polynomial
sigma with E sigma(Z)=E[Z sigma(Z)]=0 and v=E sigma(Z)^2, set

    e=(1,...,1)^T/sqrt(N),    K_P=Y(I-ee^T)Y^T/N.

Then

    [b_N^(1/6)/(v(1+sqrt(b_N))^(4/3))] N^(2/3)
      [lambda_max(K_P)-v(1+sqrt(b_N))^2] => TW_1.

Thus lambda_max(K_P) tends in probability to v(1+sqrt(b))^2. The
quadratic Hermite coefficient is arbitrary, including critical and
supercritical values for the unprojected covariance spike. The activation
degree and coefficients must remain fixed. The full T248 problem remains
unresolved.

The new ingredient is a dimension-uniform quadratic-form concentration
lemma for projected polynomial Gaussian features. If z=Q^T sigma(U^Tg),
the columns of U are unit vectors, Q has orthonormal columns, ||U||op<=C_U
and T=E zz^T has ||T||op<=C_T, then for degree k and real symmetric A,

    ||z^T A z-Tr(AT)||_p
      <=2 C_U ||sigma'(Z)||_4 3^(k/2) sqrt(C_T) (p-1)^k ||A||F.

Gaussian Poincare bounds the variance through the exact gradient.
Cauchy–Schwarz and finite-degree hypercontractivity control the derivative
without bounding it pointwise. Hypercontractivity of the centered quadratic
form gives every fixed p. The lemma requires only a_0=0, so it may also be
useful when a linear term is retained. It does not by itself establish
covariance regularity for that case.

[PROOF.md](PROOF.md) gives the full argument. The projected covariance
still has operator distance o_p(1) from vI, bounded trace defect and bounded
squared Frobenius defect. Its conditional edge moves by O_p(N^-1), which
is negligible at the TW scale. The conditional universality input is
Corollary 1.4 of Guangchen Chen and Xing Lyu, *Tracy–Widom law for sample
covariance matrices under quadratic form concentration*,
[arXiv:2610.41416v2](https://arxiv.org/html/2610.41416v2), used as stated.
The classical hypercontractivity input is equation (1.1) in Yuu Hariya,
*A unification of the hypercontractivity and its exponential variant of
the Ornstein-Uhlenbeck semigroup*,
[arXiv:1707.03163v2](https://arxiv.org/html/1707.03163). Its polynomial
consequence and Gaussian Poincare are derived in the proof. The bounded
literature search found no newer full solution.

Commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r5/briefs/T248/verify_projection.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B verify_polynomial.py
```

Both passed. The predecessor rerun reproduced its projection identities,
scalar-edge checks and normalization. The new [script](verify_polynomial.py)
checks 36 exact rational cases, with degrees two through five, orthogonal,
correlated, repeated and antipodal directions, and three symmetric test
matrices. Direct Gaussian monomial moments and an independent conversion
to product Hermite coefficients agree exactly on variances and gradient
energies. Covariances agree with the Hermite correlation formula. Every
step of the variance bound passes. The run took 0.842 seconds and used
17.3 MiB peak RSS. These are algebra checks, not a TW simulation.

What failed: factoring the derivative and feature moments as if independent
is false. With sigma=L=He2, E[sigma'^2 L^2]=40 but the product of means is
8; the resulting naive variance bound would be 32, below the true 56.
The proof handles that dependence explicitly. A bounded-derivative argument
also cannot apply directly to these activations.

What remains uncertain or unproved: the cited universality theorem is an
external input, not independently refereed here. No gap was identified
within the stated projected polynomial model. Growing-degree activations,
random column norms, the linear-component bulk, b=1, and the first
unprojected eigenvalue below supercritical spikes are outside the theorem.
Projection and interlacing do not supply eigenvalue sticking. The entrywise
moment check is asymptotic and gives no threshold for moderate widths.
The exact ratio b_N must remain in the center unless a convergence rate
to b is supplied.

Next worker: apply the new polynomial concentration lemma to the round 4
unprojected strictly subcritical model, q alpha sqrt(b)<v. Its covariance
and edge lemmas should carry over unchanged. Verify the resulting complete
conditional argument rather than infer it from interlacing. The harder
supercritical original-model sticking estimate remains a separate target.

Both launchers printed a priority-adjustment warning, but both scripts
measured effective nice value 20 before computing. All runs used one
thread and stayed far below the memory and time limits. All writes stayed
in this folder; earlier folders were read-only. No git or subagents.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first clock reading 11:31:19 +04.
