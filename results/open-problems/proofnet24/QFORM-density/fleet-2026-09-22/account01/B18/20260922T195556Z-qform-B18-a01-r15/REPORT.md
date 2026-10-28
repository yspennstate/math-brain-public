SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-22T19:55:56Z.
attacking: literature-to-proof transfer; replace determinant/smallest-singular-value payment in the exact one-sided Schur-cross branch by a stable-rank/Hilbert-Schmidt aggregate payment.

# QFORM B18 r15 — stable-rank aggregate half-Riesz transfer

## Status

**PROVED SUPPORTING THEOREM / ESSENTIAL STEP APPLIED. Full QFORM remains OPEN.**

Target: for arbitrary independent real coordinates with densities at most one and symmetric `A` with at least three eigenvalues of modulus at least one, prove one dimension-independent finite density bound for `X^T A X`. Continuity is separate and is **not** claimed by the theorem proved here.


## Source theorem transferred exactly

Primary source:

- Mark Rudelson and Roman Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, IMRN 2015, arXiv:1402.4492, DOI 10.1093/imrn/rnu243.
- Their Theorem 1.2: if independent real `V_i` have densities bounded by `1` and `c != 0`, the density of `c.V` is bounded by `sqrt(2)/||c||_2` after normalization.
- Their Theorem 1.4: if `U_i` are independent and `L(U_i,t)<=p`, then for every matrix `M` and `eps in (0,1)`,

  `L(MU, t ||M||_HS) <= (C_eps p)^((1-eps) r(M))`,

  where `r(M)=floor(||M||_HS^2/||M||^2)` in the paper's convention. In particular, for cap-one densities, `L(U_i,t)<=2t`, so with `eps=1/10` and `q=0.9 r(M)>=0.9`,

  `P(||MU-z||<=s) <= min(1,(2 C_.1 s/||M||_HS)^q)`

  uniformly in the center `z`.

No centering, variance, moment, support, log-concavity, iid assumption, or post-rotation independence is used.

A targeted literature check did **not** locate an exact prior theorem matching the full owner target. In particular, the Herry--Malicet--Poly quadratic-form regularity results (arXiv:2303.09488) impose substantially stronger distributional/smoothness and asymptotic hypotheses, so they do not settle the present arbitrary cap-one product-law target. This is a scope statement, not a novelty claim.

## Designated partner actually applied

Completed partner result:

`account02/B18`, run `20260922T181504Z-account02-B18-QFORM-r12`, canonical mathematics
`yspennstate/math-open-problems@aa0b07137085e1b6e948c00052ff0689343a0cee:proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260922T181504Z-account02-B18-QFORM-r12/REPORT.md`
with late-correction supplement at commit `55114f49ab8188c8a90cf998c66d8627d655dec4`.

I use two completed ingredients from that run:

1. the original-coordinate one-sided-cross architecture
   `T=G(U)+2 U^T B V+beta^T V`, with `U,V` disjoint independent coordinate banks and arbitrary measurable `G(U)`;
2. the **fractional square transducer**: if `sup_t E|R-t|^{-1/2}<=M` and the conditional density of a scalar `W|R=r` is at most `K`, then `R+aW^2` has density at most `K M/sqrt(|a|)`.

The new step below replaces the partner's singular-product payment by an aggregate Hilbert--Schmidt payment, using Rudelson--Vershynin.

## Lemma 1: half-Riesz from a scalar density cap

If a real random variable `Z` has density bounded by `L`, then for every `t`,

`E |Z-t|^(-1/2) <= 2 sqrt(2L)`.

Proof. Among probability densities bounded by `L`, the decreasing kernel `|x-t|^{-1/2}` is maximized by placing density `L` on the centered interval of length `1/L`. Therefore

`E |Z-t|^(-1/2)
 <= L int_{-1/(2L)}^{1/(2L)} |x|^(-1/2) dx
 = 2 sqrt(2L)`.

Applying Rudelson--Vershynin Theorem 1.2 to `c.V` gives

`sup_t E |c.V-t|^(-1/2)
 <= 2^(7/4) ||c||_2^(-1/2).`  (1)

This is translation-uniform.

## Lemma 2: stable-rank aggregate inverse-half moment

Let `U` have independent cap-one coordinate densities and let `M` be any nonzero matrix. Put `H=||M||_HS`. Then

`sup_z E ||MU-z||_2^(-1/2) <= C_SR H^(-1/2)`,  (2)

where one may take

`C_SR = (9/4) sqrt(2 C_.1)`,

and `C_.1` is the absolute constant in Rudelson--Vershynin Theorem 1.4 at `eps=1/10`.

Proof. Set `q=0.9 r(M)>=0.9`. The source theorem and the cap-one concentration bound give

`P(||MU-z||<=s) <= min(1,(2 C_.1 s/H)^q)`.

For any positive random variable `Y`,

`E Y^(-1/2) = (1/2) int_0^infty s^(-3/2) P(Y<s) ds`.

Integrating the displayed small-ball envelope, splitting at `s0=H/(2 C_.1)`, yields exactly

`E ||MU-z||^(-1/2)
 <= sqrt(2 C_.1/H) * q/(q-1/2)`.

Since `q>=0.9`, `q/(q-1/2)<=9/4`, proving (2).

The point is structural: the payment depends on the **aggregate cross energy** `||M||_HS`, not on a smallest singular value, determinant, or a chosen minor.

## Theorem: Hilbert--Schmidt one-sided-cross half-Riesz bound

Let `U,V` be mutually independent coordinate families, each coordinate having density at most one. Let `G(U)` be arbitrary measurable, `B` any nonzero matrix, and `beta` arbitrary. Define

`T = G(U) + 2 U^T B V + beta^T V`.

Then

`sup_t E |T-t|^(-1/2)
 <= C_x ||B||_HS^(-1/2)`,  (3)

with the universal source-exact constant

`C_x = (9/4) 2^(7/4) sqrt(C_.1)`.

Proof. Conditional on `U=u`, the random part in `V` is the linear form

`c(u).V`,   `c(u)=2B^T u+beta`.

By (1),

`sup_t E_V[|T-t|^(-1/2) | U=u]
 <=2^(7/4) ||2B^T u+beta||^(-1/2).`

Write `Y=B^T U+beta/2`. Applying Lemma 2 to `M=B^T`, then using `||2Y||^(-1/2)=2^(-1/2)||Y||^(-1/2)`, gives

`E ||2B^T U+beta||^(-1/2)
 <= (9/4) sqrt(C_.1) ||B||_HS^(-1/2).`

Multiplying proves (3).

This is genuinely different from a determinant/smallest-singular-value estimate. It remains finite for every nonzero `B` and improves parametrically when many weak cross directions contribute aggregate Frobenius mass.

## Corollary: physical square + aggregate one-sided Schur cross

Let `Q=X^T A X`. Choose an original coordinate `i` with physical pivot `a=A_ii !=0`. Completing the square in `X_i` writes

`Q = a (X_i + ell(Z)/a)^2 + R(Z)`,

where `Z=X_{-i}` and `R` is the physical Schur residual.

Suppose the remaining original coordinates can be partitioned into disjoint banks `I,J,K` such that, after conditioning on `K`,

- `R[J,J]=0` (exact one-sided-zero geometry),
- the cross block `B=R[I,J]` is nonzero,
- all self-curvature on `I`, affine terms produced by `K`, and all `K`-terms are arbitrary.

Then

`||p_Q||_infinity
 <= C_x / sqrt(|a| ||B||_HS).`  (4)

Proof. After conditioning on `K`, `R` has the form in (3), so its translation-uniform half-Riesz norm is bounded by `C_x ||B||_HS^(-1/2)`, uniformly in the conditioning. Average over `K`.

Now apply the completed account02/B18 fractional square transducer. Conditional on `R`, the variable

`W = X_i + ell(Z)/a`

has density at most one: `X_i` is independent of `Z`, and conditioning on `R=R(Z)` only produces a mixture of translations of the original cap-one density of `X_i`. Hence `K=1` in the transducer, giving (4).

No continuity conclusion is extracted from this argument; only essential boundedness is proved.

## Why this closes a genuinely new implication

The partner theorem already paid rank one by `sigma_1(B)` and higher ranks by selected singular products. Formula (4) supplies a **Frobenius aggregate certificate**:

`|a| ||B||_HS >= delta  =>  ||p_Q||_infinity <= C_x / sqrt(delta).`

Thus many individually weak cross directions can be aggregated *before inversion*. For example, if `B_m=m^(-1/2) I_m`, then every singular value is `m^(-1/2)` and any fixed-singular-direction payment degenerates with `m`, while `||B_m||_HS=1`, so (3)--(4) remain dimension-free. This is exactly the kind of diffuse cross cloud that a one-minor or one-row extraction can miss.

This does **not** prove that the bare spectral hypothesis `s_3(A)>=1` always forces an exact one-sided-zero Schur bank with `|a| ||B||_HS` bounded below. The latest correction set explicitly forbids such an unsupported extraction. Formula (4) is therefore a new paid branch, not a full solution.

## Corrections checked and preserved

The proof does not use any of the following refuted interfaces:

- a single good cross minor;
- post-rotation independence;
- a worst conditional spectral-fiber density cap;
- arbitrary-joint rank-three coarea;
- positive moments of normalized conditional projection densities;
- a universal finite-fragment localization;
- small/near-zero Schur self-curvature treated as exact zero.

In particular the latest `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` correction is respected: (4) requires **exactly** `R[J,J]=0`. No perturbative claim is made for merely small self-curvature on `J`.

## Remaining full-target implication

The new unpaid structural statement is:

> Starting only from `s_3(A)>=1`, outside the already-paid ridge-window, invertible-indefinite-pair, and other grouped-coordinate branches, prove an exhaustive product-preserving reduction that either supplies a physical pivot and an exact one-sided-zero cross packet with `|a| ||B||_HS >= c`, or pays simultaneous self-curvature by another source-valid aggregate mechanism.

The new theorem makes **Frobenius cross mass** a legitimate currency for that reduction; it removes the need to extract a quantitatively large single singular value or determinant inside this exact branch.

## Classification

`ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM`.

Full conjecture: **OPEN / NOT PROVED**.
Continuity for this new branch: **NOT CLAIMED**.
Native brain ingestion: **WITHOUT_VERIFIED_BRAIN**; authenticated repository retrieval/coordination is not native learned-memory ingestion.
