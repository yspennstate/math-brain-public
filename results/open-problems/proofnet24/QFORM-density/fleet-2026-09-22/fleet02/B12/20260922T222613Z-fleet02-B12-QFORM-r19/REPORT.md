SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-22T22:26:13Z.
attacking: opposite-leverage dual physical certificates: route the sign of one arbitrary rank-one spectral addition to an indefinite physical pair whose Sherman--Morrison denominator moves away from zero, then invoke the completed fleet03/B12 two-bank third-source theorem on the actual final matrix.

# QFORM B12: opposite-leverage sign routing for one arbitrary spectral spike

## Status

**PROVED SUPPORTING TARGET-LEVEL REDUCTION + EXACT TARGET-CLASS STRESS FAMILY. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** Essential boundedness only; continuity is not proved here.

This run addresses the assignment's extra-eigenvalue question without diagonalizing the product source. The new point is that a single indefinite physical pair has a finite hostile rank-one resonance, but two complementary indefinite pairs with opposite Sherman--Morrison leverage signs let the deterministic sign of the added spectral coefficient choose a pair whose conditioning can only improve in the dangerous denominator. This permits an arbitrarily small or arbitrarily large rank-one addition of either sign, provided the final matrix remains in the target and the two base certificates satisfy explicit quantitative hypotheses.


## Completed assigned-partner theorem actually applied

Read in full:

`yspennstate/math-open-problems@e71ed8023266f157a6f5c7a04ea6f9c53acc59c5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T214833Z-qform-eigenvalue-r18/REPORT.md`.

Its theorem `QFORM-TWO-BANK-THIRD-SOURCE-ARBITRARY-COMPLETION-v1` states, in particular, that if two disjoint original-coordinate scalar banks form an invertible indefinite pair `B`, the reduced core `H` satisfies `s_3(H)>=s>0`, `D=|det B|`, and `kappa=sigma_min(B)`, then

`||p_Q||_infinity <= 6*400^(1/3)*(D^2*kappa*s)^(-1/6)`,

with arbitrary outside completion/cross coupling handled without an independent-convolution step. For singleton banks we use this theorem exactly as stated; no rotated coordinates are introduced.

## Theorem: dual-leverage sign routing

Let `A_tau=A_0+tau v v^T` be a real symmetric matrix in ORIGINAL independent coordinates, where `tau` is any real number and `v` is deterministic. Assume the FINAL matrix obeys

`s_3(A_tau)>=s>0`,

where singular values are in decreasing order. For a symmetric matrix this means that at least three final eigenvalues have absolute value at least `s`.

Suppose there are two physical coordinate pairs `P_+` and `P_-` (they need not be disjoint from each other because only one is used for a fixed sign of `tau`). Write

`B_sigma=A_0[P_sigma,P_sigma]`, `w_sigma=v|_(P_sigma)`, `sigma in {+,-}`.

Assume both `B_+` and `B_-` are invertible indefinite and, for some `d_0,M,L,q_0>0`,

`|det B_sigma|>=d_0`,
`||B_sigma^(-1)||_op<=M`,
`||w_sigma||_2<=L`,

and their rank-one leverages have opposite signs with a quantitative gap:

`q_+ := w_+^T B_+^(-1) w_+ >= q_0`,
`q_- := w_-^T B_-^(-1) w_- <= -q_0`.

Define

`beta_* := 1/(M + M^2 L^2/q_0)`.

Then, for every real `tau` for which `s_3(A_tau)>=s`, the law of `X^T A_tau X` for arbitrary independent input densities bounded by one has an essentially bounded density satisfying

`boxed(||p_(X^T A_tau X)||_infinity <= 6*400^(1/3)*(d_0^2 beta_* s)^(-1/6)).`

The bound is uniform in the sign and magnitude of `tau`.

### Proof

If `tau>=0`, choose `P_+`; if `tau<=0`, choose `P_-`. Denote the chosen objects simply by `B,w,q`. By construction,

`tau q >=0`.

The final physical pair is

`B(tau)=B+tau w w^T`.

The matrix determinant lemma gives

`det B(tau)=det B*(1+tau q)`.

Because `tau q>=0`,

`1+tau q>=1`,

so `B(tau)` never crosses singularity along the segment from `0` to `tau`, its inertia remains the same as the base pair, and in particular it remains indefinite. Moreover

`D(tau):=|det B(tau)|>=|det B|>=d_0`.

Sherman--Morrison gives

`B(tau)^(-1)=B^(-1) - [tau/(1+tau q)] B^(-1) w w^T B^(-1)`.

Since `tau q>=0` and `|q|>=q_0`,

`|tau|/|1+tau q| = |tau|/(1+|tau||q|) <= 1/|q| <=1/q_0`.

Hence

`||B(tau)^(-1)||_op`
` <= ||B^(-1)||_op + (1/q_0)||B^(-1)w||_2^2`
` <= M + M^2 L^2/q_0`.

Therefore

`kappa(tau):=sigma_min(B(tau)) >= beta_*`.

Now use the chosen physical pair as the two singleton banks in the completed fleet03/B12 theorem, and let all remaining ORIGINAL coordinates form its core `Z`; there is no coordinate rotation. Under the corresponding permutation its reduced matrix `H` is exactly the FINAL matrix `A_tau`, so

`s_3(H)=s_3(A_tau)>=s`.

The partner theorem yields

`||p||_infinity`
` <=6*400^(1/3)*(D(tau)^2 kappa(tau) s)^(-1/6)`
` <=6*400^(1/3)*(d_0^2 beta_* s)^(-1/6)`.

No moment, support, Gaussian, post-rotation independence, conditional-fiber supremum, or convolution assumption is used. QED.

## Exact target-class family: each single pair has a hostile resonance, two pairs are uniform

Let

`A_0=diag(1,-1,1,-1)`,
`v=(e_1+e_4)/sqrt(2)`,
`A_tau=A_0+tau v v^T`.

The spectrum is exactly

`{1,-1, (tau+sqrt(tau^2+4))/2, (tau-sqrt(tau^2+4))/2}`.

The last two eigenvalues have product `-1`, so one has absolute value at least one. Hence every real `tau` satisfies

`s_3(A_tau)=1`;

this is a genuine target-class family for all spike magnitudes and both signs.

Take

`P_+=(1,2)`, `P_-=(3,4)`.

Both base pairs equal `diag(1,-1)`. The spike restrictions are

`w_+=(1/sqrt(2),0)`, `w_-=(0,1/sqrt(2))`,

so

`q_+=1/2`, `q_-=-1/2`.

For `tau>=0`, the positive-leverage pair is

`B_+(tau)=diag(1+tau/2,-1)`,

while for `tau<=0`, the negative-leverage pair is

`B_-(tau)=diag(1,-1+tau/2)`.

In the chosen branch, for every `tau`,

`|det B_sigma(tau)|>=1`, `sigma_min(B_sigma(tau))=1`, `s_3(A_tau)=1`.

Therefore the completed partner theorem gives the completely uniform bound

`boxed(||p_(X^T A_tau X)||_infinity <= 6*400^(1/3) = 44.2083779836846...)`.

This family also makes the mechanism barrier exact. If one insists only on `P_+`, then it becomes singular at the hostile value `tau=-2`. If one insists only on `P_-`, it becomes singular at `tau=+2`. Thus no one fixed indefinite pair is uniformly stable under an arbitrary signed spike, while the two complementary leverage signs remove both resonances without rotating the product source.

## What this pays and what remains unpaid

**Paid:** one arbitrary rank-one spectral addition may be arbitrarily small or arbitrarily large and may have either sign. If two physical indefinite pair certificates have quantitatively opposite rank-one leverage signs, the sign of the actual spectral coefficient selects a source-valid pair whose determinant does not shrink and whose inverse remains uniformly bounded. The completed fleet03/B12 theorem then supplies the density bound using the FINAL matrix's third singular direction wherever it lies. Arbitrary other coefficients are retained in the original-coordinate quadratic form rather than treated as an independent convolution.

**Unpaid:** the bare QFORM hypothesis `s_3(A)>=1` does not yet force such an opposite-leverage pair system for a useful decomposition `A=A_0+tau vv^T`. The previous disjoint-triple hostile-budget theorem and the concurrent weighted-core theorem show other stable branches; heavily overlapping/Hadamard frames can still evade naive fixed-certificate selection. A full proof must derive a finite sign-routable family of physical/grouped certificates from the global spectral hypothesis, or switch to an already-paid ridge/aggregate branch, before reciprocal local conditioning is paid.

The theorem establishes essential boundedness in the displayed scope. Continuity is not asserted. Full QFORM remains OPEN.

Claim ID: `QFORM-DUAL-LEVERAGE-RANKONE-SIGN-ROUTING-v1`.
