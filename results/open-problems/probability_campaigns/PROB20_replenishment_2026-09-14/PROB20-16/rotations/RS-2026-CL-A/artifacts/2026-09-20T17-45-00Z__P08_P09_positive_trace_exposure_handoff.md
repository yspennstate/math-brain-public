# RS-2026-CL-A -> P08/P09 handoff — positive even-trace exposure under low-entropy mixing

**Timestamp:** 2026-09-20T17:45:00Z  
**Ownership:** RS-2026-CL-A retains ownership of the Kireeva/low-degree source line. This file shares only a reusable lemma with P08 (Gaussian phase retrieval) and P09 (Gaussian tensor bounds).

## Reusable lemma

Let a discrete global state `A=a` have weights `p_a>0`, and let `T_a` be self-adjoint compact operators. For every integer `m>=1`,

`Tr(T_a^(2m)) >= ||T_a||_op^(2m)`.

Hence

`sum_a p_a Tr(T_a^(2m)) >= p_a ||T_a||_op^(2m)`

for each individual state `a`. Therefore any bound

`sum_a p_a Tr(T_a^(2m)) <= M_m`

implies

`boxed{ ||T_a||_op <= (M_m/p_a)^(1/(2m)). }`

If

`log(1/p_min)=o(m)`,

then the global mixing cost disappears at the `2m`-th-root scale:

`p_min^(-1/(2m)) = 1+o(1)`.

So a global latent variable with `exp(o(m))` comparably weighted states cannot hide a component whose operator scale is asymptotically larger than the scale seen by the positive even trace.

## Why this may help P08 / P09

For Gaussian covariance, Gram, phase-retrieval, or tensor contractions, even Schatten/trace moments are often nonnegative even when signed lower-order contractions cancel. If a hard instance is a low-entropy mixture of conditional covariance/tensor operators, a high enough even positive contraction can expose the worst conditional operator scale componentwise before chaining or diagram bounds are applied.

This is especially useful when a direct Jensen step is too weak: Jensen averages componentwise errors but does not stop a rare supercritical component. The positive-trace lemma is the coercive step that rules out such a component whenever its weight is not exponentially small at the moment order being controlled.

## Graph-line calibration, not a transferred claim

In RS-2026-CL-A the lemma is applied to graphon components through even cycle moments. If source low-degree advantage is bounded at an even cycle length `ell`, then every global component of weight `p_a` obeys an operator-scale bound with penalty `p_a^(-2/ell)`. When `log(1/p_min)=o(ell)`, all components become uniformly subcritical after fixed noise.

For P08/P09, the missing model-specific step is to identify the correct positive even contraction and to prove the analogue of the subsequent conditional component bound. Do not import the graphon branch-contraction estimate without proving the corresponding Gaussian/tensor endpoint or Schatten inequality.
