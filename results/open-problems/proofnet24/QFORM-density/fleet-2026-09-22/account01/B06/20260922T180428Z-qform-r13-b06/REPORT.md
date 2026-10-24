# account01/B06 — group before curvature: finite spectral-direction aggregation

**Run:** `20260922T180428Z-qform-r13-b06`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control source:** `yspennstate/math-research-brain@70e831492a1b8e841d2b31e818dbfdbadde6a237`, OWNER CONTROL revision `2026-09-22.11`  
**Assignment:** Curved fiber integration  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact target and source dependencies

The full target remains open: for every finite `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal finite constant, or give a valid target counterexample. Continuity is a separate desired conclusion.

This report changes mechanism relative to my preceding local-triple run. The previous theorem, canonical source

`yspennstate/math-open-problems@1bc95193312b70572b2765529ac3b6d98e3fe754:proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260922T160048Z-qform-r12-b06/REPORT.md`,

proved the following physical three-coordinate bound. If `M` is an invertible symmetric `3x3` Hessian block and three independent inputs have density cap one, then arbitrary affine perturbations satisfy

`||p||_infinity <= 2 sqrt(2 pi) K(M)`,

where

`K(M)=|det M|^(-1/2) (sum_j |M e_j|^(1/3))^(3/2)`.

In particular, if `sigma_min(M)>=kappa`, then

`||p||_infinity <= 6 sqrt(6 pi)/kappa`.                                      (0.1)

That run also proved that applying (0.1) separately to tiny physical triples and only afterward averaging the scalar constants can lose linearly in dimension on a delocalized Hadamard rank-three frame.

The named designated-partner result actually consumed and applied here is account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical source

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For an `N x k` matrix `R` with orthonormal columns and independent cap-one input coordinates, it proves

`||p_(R^T X)||_infinity <= exp(k/2)`.                                      (0.2)

More precisely it gives the leverage-weighted product bound

`product_i (1-ell_i)^(-(1-ell_i)/2)`, `ell_i=||r_i||^2`.

The proof keeps the original product density inside the affine-fiber integral via geometric Brascamp--Lieb. This is precisely the allowed weighted replacement for the refuted unrestricted fiber supremum.

The live correction inbox was refreshed before this report. In particular this proof does not use pointwise quadratic phase decay, post-rotation independence, a generic X-ray cap, a conditional density cap created by a change of variables, a fixed good physical minor, direct Pluecker-to-pivot support identification, or post-hoc reciprocal-minor averaging.

## 1. Conditional end-to-end route and the first missing implication

For exact rank three write

`A=R Lambda R^T`, `R^T R=I_3`, `|lambda_j|>=1`.

The previous obstruction says that a delocalized frame can make every individual physical triple ill-conditioned even though the frame itself has only a few repeated directions. This suggests aggregating all original coordinates lying on the same spectral row direction *before* applying curved coarea.

The first implication attempted here is therefore:

> If the physical spectral rows occupy only finitely many one-dimensional directions, can one group each direction into one independent scalar with a dimension-free density cap, and then recover a quantitatively nonsingular three-variable Hessian from Cauchy--Binet?

The answer is yes. The result below closes every exact-rank-three finite-direction frame with a constant depending only on the number of row directions, not on `n`, the multiplicities, the input laws, or the sizes/signs of the three eigenvalues beyond `|lambda_j|>=1`.

## 2. Finite-direction grouping theorem

### Theorem — `QFORM-RANK3-FINITE-DIRECTION-GROUPING-v1`

Let

`A=R Lambda R^T`, `R in R^(n x 3)`, `R^T R=I_3`,

where `Lambda` is real diagonal and `min_j |lambda_j|>=1`. Assume the nonzero rows of `R` lie in at most `m` one-dimensional subspaces of `R^3`. Let `X_1,...,X_n` be independent real random variables with probability densities bounded by one. Then `Q=X^T A X` has an essentially bounded density and

`||p_Q||_infinity <= 6 e sqrt(6 pi) binom(m,3)`.                         (2.1)

Since `rank R=3`, necessarily `m>=3`. The conclusion is valid for every signature of `Lambda`. No moment, support, connectedness, Gaussianity or log-concavity assumption is used. Continuity is not asserted.

### Proof

Partition the indices of the nonzero rows into direction classes `G_1,...,G_m`. For every `a`, choose a nonzero representative `v_a in R^3` and write

`r_i=c_i v_a`, `i in G_a`.

Put

`alpha_a=(sum_{i in G_a} c_i^2)^(1/2)`,
`w_a=alpha_a v_a`,
`Z_a=alpha_a^(-1) sum_{i in G_a} c_i X_i`.                              (2.2)

The groups are disjoint, so the random variables `Z_1,...,Z_m` are independent.

Let `W` be the `m x 3` matrix whose `a`th row is `w_a^T`. Grouping preserves the Parseval identity exactly:

`W^T W=sum_a alpha_a^2 v_a v_a^T=sum_i r_i r_i^T=R^T R=I_3`.            (2.3)

Also

`R^T X=sum_a v_a sum_{i in G_a} c_i X_i=sum_a w_a Z_a=W^T Z`,           (2.4)

hence

`Q=Z^T B Z`, `B=W Lambda W^T`.                                         (2.5)

The nonzero spectrum of `B` is the same as the nonzero spectrum of `A`, namely the diagonal entries of `Lambda`.

Now apply the named account02/B06 theorem (0.2) to each group separately with `k=1`. The coefficient vector

`u^(a)=(c_i/alpha_a)_(i in G_a)`

has Euclidean norm one, so it is a one-column orthonormal matrix. Therefore

`||p_(Z_a)||_infinity <= e^(1/2)=sqrt(e)`                               (2.6)

for every `a`. This is the actual partner inequality used in the proof. It is important that (2.6) was obtained by integrating the original product density before any curved reciprocal payment; no conditional independence after a spectral rotation is claimed.

Next use Cauchy--Binet on (2.3):

`sum_{J subset [m], |J|=3} det(W_J)^2=det(W^T W)=1`.                    (2.7)

Let

`p=max_{|J|=3} det(W_J)^2`.

Then

`p>=1/binom(m,3)`.                                                       (2.8)

Choose a triple `J` attaining `p`. Since `W^T W=I_3`, the operator norm of every row-restriction `W_J` is at most one. If its singular values are `s_1>=s_2>=s_3>0`, then `s_1,s_2<=1` and

`s_1 s_2 s_3=|det W_J|=sqrt(p)`.

Consequently

`sigma_min(W_J)=s_3>=sqrt(p)`.                                         (2.9)

The corresponding `3x3` physical principal block of the grouped Hessian is

`M=B[J,J]=W_J Lambda W_J^T`.                                           (2.10)

Because `W_J` and `Lambda` are invertible,

`sigma_min(M)>=sigma_min(W_J)^2 sigma_min(Lambda)>=p`.                  (2.11)

Condition now on all grouped variables `Z_{J^c}`. The conditional polynomial in the three independent variables `Z_J` has fixed quadratic Hessian `M`, plus an arbitrary affine term and constant depending on the conditioned variables. The three input densities have cap `L=sqrt(e)` rather than cap one. Rescale

`Y_j=L Z_j`, `j in J`.

Then each `Y_j` has a probability density bounded by one, while the quadratic Hessian becomes `M/L^2=M/e`. By (2.11),

`sigma_min(M/e)>=p/e`.                                                   (2.12)

Apply the prior curved coarea estimate (0.1), uniformly in the arbitrary conditional affine term:

`||p_(Q | Z_{J^c})||_infinity <= 6 sqrt(6 pi)/(p/e)
                              =6 e sqrt(6 pi)/p`.                       (2.13)

Averaging the conditional densities over `Z_{J^c}` cannot increase this uniform bound. Combining (2.8) and (2.13) yields (2.1). `QED`

## 3. Exact repair of the Hadamard obstruction

The theorem directly closes the source-valid delocalized family that defeated post-hoc local-triple averaging.

Take the rank-three Sylvester--Hadamard frame whose rows are the four types

`(1,s,t)/sqrt(n)`, `s,t in {+1,-1}`,

each repeated `n/4` times, and take `Lambda=diag(1,1,-1)`. Every individual invertible physical triple has determinant of order `n^(-3/2)`, and the previous local coarea constants grow like `n`; moreover the partner showed same-sign Pluecker support can be disjoint from nonzero two-pivot physical determinants.

Here there are only `m=4` row directions. Grouping each repeated type as in (2.2) produces four independent scalars and the `4x3` Parseval frame with rows

`w_(s,t)=(1,s,t)/2`.                                                     (3.1)

Every three-row minor has determinant magnitude `1/2`, hence `p=1/4`. Formula (2.13) gives

`||p_Q||_infinity <= 24 e sqrt(6 pi) < 283.25`,                         (3.2)

uniformly in `n` and in all cap-one input laws. Thus the linear-in-`n` loss from the preceding B06 report was entirely an artifact of paying curvature before grouping the product variables.

The same mechanism closes the singleton-plus-two-banks rank-three family with `m=3` and `p=1`, giving

`||p_Q||_infinity <= 6 e sqrt(6 pi) < 70.82`,                           (3.3)

again uniformly in the bank sizes. Other existing methods give better constants on that family; the point here is structural: the assigned curved-fiber mechanism now survives both canonical delocalization stress tests without selecting a tiny original physical minor.

## 4. What this changes and what remains unpaid

The new theorem establishes a clean principle:

> **Group before curvature.** When many physical coordinates contribute along the same spectral direction, first aggregate each disjoint coordinate bank into one independent scalar and use the weighted affine-fiber Brascamp--Lieb theorem to preserve a universal density cap. Only then select a three-variable curved block. Cauchy--Binet acts on the grouped Parseval frame, where the relevant minors are no longer diluted by multiplicity.

This is strictly stronger than the previous local-triple theorem on repeated-direction frames, and it implements the partner result at the exact point where the earlier Hadamard obstruction demanded it.

It is not the full QFORM theorem. Two major gaps remain:

1. **Approximate/grouped versus diffuse rank-three frames.** An arbitrary exact-rank-three frame may have very many genuinely different row directions. One now needs a quantitative decomposition showing either that the row mass can be aggregated into a bounded number of coherent direction groups with controlled angular error, or that the remaining diffuse component falls into an already paid ridge/diffuse theorem. The decomposition must keep the product variables independent by grouping disjoint original-coordinate sets, and it cannot pay inverse tiny physical minors after the grouping step.
2. **Additional spectral components.** The theorem is exact rank three. The owner target allows arbitrary additional eigenvalues of any sign and size. A full proof still needs a product-preserving passage that keeps those components from destroying the grouped curved estimate. Existing ridge-window/regularized-determinant results pay important diffuse branches but do not yet supply the exhaustive reduction from the bare three-large-eigenvalue hypothesis.

A precise next implication is therefore

`QFORM-APPROX-GROUP-OR-RIDGE-CLOSE-v1`:

> For an exact-rank-three Parseval frame (and ultimately for the three-large spectral subspace inside a general matrix), produce a dimension-free partition into disjoint original-coordinate groups such that either a bounded number of grouped spectral directions carries a quantitatively nonsingular three-minor after aggregation, or the residual row leverage/cross structure satisfies one of the already proved diffuse/ridge hypotheses.

This aligns with the current proof-assembly high-offdiagonal/overlap gap but avoids the refuted fixed-good-minor and direct Pluecker-pivot mechanisms.

## 5. Status and correction audit

Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`.

The theorem proves essential boundedness only. It does not separately prove a continuous representative. It does not establish a universal constant independent of `m` for arbitrary exact-rank-three frames, and it does not absorb arbitrary higher-rank spectral tails. Therefore it is not promoted to a full solution.

Corrections respected in the derivation: no law-uniform pointwise Fresnel decay; no post-rotation independence; no unrestricted fiber supremum; no generic X-ray-only indefinite trace bound; no conditional-cap-as-independence substitution; no fixed good principal minor/cross-rank dichotomy; no direct same-sign Pluecker-to-full-pivot identification; and no post-hoc determinant-weighted average of already-inverted local curvature costs.
