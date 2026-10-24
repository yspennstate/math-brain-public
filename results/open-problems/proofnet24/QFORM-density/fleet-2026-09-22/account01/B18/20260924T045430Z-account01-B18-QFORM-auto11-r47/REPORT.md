SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-24T04:54:30Z.
attacking: convert the latest account02/B18 private-square receiver into a spectral-scale theorem for the exact-rank-three rank-one-cross chamber, using an exact inverse identity rather than an extra currency assumption.

# account01/B18 r47 — inverse-entry spectral currency for a rank-one cross plus a private physical scalar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: literature-to-proof transfer  
Status: **PROVED SUPPORTING TARGET-LEVEL BRANCH / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 1. Statement

Let the ORIGINAL coordinates be partitioned as

`I \sqcup J \sqcup {w} \sqcup K`.

Let `u in R^I`, `v in R^J` be unit vectors, extended by zero off their banks, and let `e_w` be the physical coordinate vector at the singleton original coordinate `w`. Assume the retained principal quadratic block on `I \sqcup J \sqcup {w}` is

`A_R = tau (u v^T + v u^T)
     + c v v^T
     + d (v e_w^T + e_w v^T)
     + e e_w e_w^T`,                                                   (1.1)

with `tau != 0`, `e != 0`. Thus the retained quadratic carrier has exact rank three and is supported on the orthonormal physical frame `(u,v,e_w)`. Allow the full ambient matrix to have completely arbitrary coefficients involving the outside ORIGINAL coordinates `K`.

Let the three nonzero eigenvalues of `A_R` be `mu_1,mu_2,mu_3`, and suppose

`min_j |mu_j| >= s > 0`.                                                (1.2)

Then, for arbitrary independent real ORIGINAL coordinates with probability densities bounded by one, the full ambient quadratic form `Q=X^T A X` has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <= 4 sqrt(2) / s`.                            (1.3)

Arbitrary affine terms are allowed as well. Continuity is NOT claimed by this argument.

I call (1.3) `QFORM-RANK1-CROSS-EXACTRANK3-INVERSE-CURRENCY-v1` for this run. This is a scoped supporting theorem, not the full conjecture.

## 2. Primary literature and exact hypothesis match

Two bounded-density projection results are source-valid under the owner's rough input class.

1. Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492, Theorem 1.2: if `X_j` are independent real random variables with densities bounded by `K`, and `sum a_j^2=1`, then the density of `sum a_j X_j` is bounded by `sqrt(2) K` a.e. No moment, iid, support, centering, symmetry, smoothness, or log-concavity hypothesis is imposed.

2. Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949: if `f(x)=prod_i f_i(x_i)` and each one-dimensional density is bounded by one, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. This is a joint-density cap, not post-rotation independence.

The primary quadratic-form regularity paper Herry--Malicet--Poly, arXiv:2303.09488, works with iid inputs whose common law is representable as a sufficiently smooth function of a Gaussian field. It therefore does not match the present arbitrary non-iid cap-one quantifiers and is not used as a full-target theorem.

I found no published theorem in this targeted check that exactly supplies all owner quantifiers. That is only a hypothesis comparison, not a novelty claim.

## 3. Completed designated-partner theorem used literally

The newest completed compatible account02/B18 theorem is source-pinned at

`yspennstate/math-open-problems@fedbabc70c2245476d15532f38c5c2555a0d6c31`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/account02-B18-20260924T031145Z-auto11/REPORT.md`.

Its theorem `QFORM-CONDITIONAL-CROSS-PRIVATEBANK-WEAKL2-v1` treats three genuinely disjoint ORIGINAL source banks. In the sharper singleton private-coordinate case, if

`T = X^T M Y + alpha^T X + G(Y) + a W^2 + r(Y) W + const`,             (3.1)

where `W` is one ORIGINAL scalar coordinate with density cap one, `X,Y,W` use disjoint original sources, `M != 0`, and `G,r` are arbitrary measurable functions of `Y`, then

`||p_T||_infinity <= 8 / sqrt(|a| ||M||_op)`.                          (3.2)

The proof uses the Rudelson--Vershynin linear-form density cap and a conditional weak-L2 square endpoint. In particular, it retains arbitrary `Y-Y` curvature and an arbitrary `Y`-dependent coefficient multiplying `W`.

## 4. Deterministic spectral bridge

In the orthonormal physical frame `(u,v,e_w)`, the nonzero part of (1.1) is exactly

`H = [[0,   tau, 0],
      [tau, c,   d],
      [0,   d,   e]]`.                                                  (4.1)

A direct calculation gives

`det H = - e tau^2`,                                                     (4.2)

and

`H^{-1} = [[(-c e+d^2)/(e tau^2), 1/tau, -d/(e tau)],
           [1/tau,                    0,            0],
           [-d/(e tau),               0,          1/e]]`.              (4.3)

Assumption (1.2) says the least singular value of the real symmetric invertible matrix `H` is at least `s`. Hence

`||H^{-1}||_op <= 1/s`.                                                  (4.4)

Every matrix entry has absolute value at most the operator norm. From the `(1,2)` and `(3,3)` entries in (4.3),

`1/|tau| <= 1/s`,   `1/|e| <= 1/s`.                                    (4.5)

Therefore

`boxed: |tau| >= s,  |e| >= s,  |e tau| >= s^2`.                       (4.6)

This is the key point: in this structural chamber the bare spectral scale itself forces the private-square/cross currency needed by the partner theorem. No extra determinant/minor lower bound is assumed.

## 5. Probabilistic application and ambient lift

Condition on the outside ORIGINAL coordinates `X_K=y`. Product provenance is preserved. The conditional retained polynomial is

`Q_y = 2 tau (u^T X_I)(v^T X_J)
      + c (v^T X_J)^2
      + 2 d (v^T X_J) W
      + e W^2
      + alpha_y^T X_I + beta_y^T X_J + kappa_y W + const_y`.           (5.1)

This is exactly (3.1) with

`X = X_I`, `Y = X_J`, `W=X_w`,
`M = 2 tau u v^T`,
`G_y(Y)=c(v^T Y)^2+beta_y^T Y`,
`r_y(Y)=2d(v^T Y)+kappa_y`,
`a=e`.                                                                  (5.2)

Since `u,v` are unit,

`||M||_op = 2 |tau|`.                                                    (5.3)

The completed account02/B18 result therefore yields, uniformly in the outside value `y`,

`||p_{Q_y}||_infinity
 <= 8 / sqrt(2 |e tau|)
 = 4 sqrt(2) / sqrt(|e tau|)
 <= 4 sqrt(2) / s`.                                                     (5.4)

Averaging the uniform conditional interval estimate over `y` proves the same bound for the full ambient quadratic form. This also proves absolute continuity of the unconditional law. No rotated variable is conditioned on, and no independence is asserted after projection.

## 6. Exact twisted target example

The spectral bridge is not restricted to the untwisted direct sum. For example take

`tau = sqrt(3/2)`,
`c   = 2/3`,
`d   = sqrt(7/18)`,
`e   = 4/3`.                                                            (6.1)

Then

`H = [[0, sqrt(3/2), 0],
      [sqrt(3/2), 2/3, sqrt(7/18)],
      [0, sqrt(7/18), 4/3]]`,                                           (6.2)

and exact symbolic factorization gives

`det(lambda I-H) = (lambda-2)(lambda-1)(lambda+1)`.                     (6.3)

Thus this is literally a target matrix with spectrum `{-1,1,2}` and a nonzero `v-W` twist. The partner inequality gives the sharper numerical instance

`||p_Q||_infinity <= 4 sqrt(2)/sqrt((4/3)*sqrt(3/2))
                    = 4.4267276788...`,                                (6.4)

for every admissible cap-one product input law, and the coarse spectral theorem gives `<=4sqrt(2)`.

## 7. Relation to prior fleet work; no novelty overclaim

An older interactive record already proves a broader-looking *literal singleton-hub* star-plus-transverse-square bound (Proposition S in `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/counterexample_search/REPORT.md`). In its own hypotheses, with a physical original-coordinate hub and a transverse square, it gives a uniform all-law bound and in particular `5.360` at unit square scale.

Therefore I do NOT claim qualitative novelty for the narrower case where `u` itself is one literal original-coordinate hub. The present transfer is useful because the account02/B18 receiver allows the hub factor `u^T X_I` to be an arbitrary linear projection of a whole disjoint original product bank, and (4.3)--(4.6) converts the exact rank-three spectral assumption directly into its needed currency.

## 8. What remains open

The full QFORM conjecture is still OPEN. The three-large-eigenvalue hypothesis does not currently force an arbitrary symmetric matrix into the product-separated structural form (1.1). The unproved compiler step is to extract, at universal scale, either

1. a rank-one cross carrier with a genuinely private physical scalar satisfying the zero `I-w` coupling required here; or
2. one of the already-paid rank-two-cross, physical-pair, grouped-hub, ridge, diffuse-product-Fourier, or dependent-pair branches,

while retaining all extra nonzero curvature rather than deleting a small tail.

Continuity is tracked separately. The partner theorem does not claim continuity for the general `Y`-dependent square shift, so this report proves essential boundedness only.

## 9. Correction audit

This argument does not use any refuted interface in the live correction inbox. In particular it does not use:

- law-uniform pointwise quadratic Fourier decay;
- arbitrary-joint three-dimensional coarea;
- conditional projected density caps as independence;
- post-rotation independence;
- deletion of a small nonzero quadratic remainder;
- a universal fixed good physical minor/cross-rank-three extraction;
- worst-fiber substitution.

The only probabilistic conditioning is on ORIGINAL outside coordinates, after which the designated partner theorem is invoked with genuinely disjoint original source banks.
