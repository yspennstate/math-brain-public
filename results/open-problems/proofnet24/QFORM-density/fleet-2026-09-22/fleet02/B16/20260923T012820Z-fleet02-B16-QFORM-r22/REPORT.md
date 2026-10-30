# QFORM-PROJECTION-CAP-DEFINITE-RECEIVER-CLASSIFICATION-v1

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Account/slot:** `fleet02/B16`  
**Status:** supporting route classification and nonzero-near-null application; **FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
**Continuity:** separate; this report proves essential-density bounds only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication

The remaining B16 difficulty is not whether a genuine two-dimensional product projection has a bounded joint density. It does. The issue is exactly when that density-height information survives the nonlinear quadratic pushforward.

This run proves the sign-sharp receiver classification needed at that interface:

- for a **definite** two-dimensional quadratic receiver, the projected joint-density cap alone is enough, uniformly under arbitrary translations depending on disjoint original-coordinate variables;
- for an **indefinite** or rank-deficient receiver, a joint-density cap alone is not enough, even at a fixed two-dimensional Hessian.

Thus any remaining nonzero-pivot/two-sheet branch must retain stronger original-product provenance. This is consistent with, and quantitatively sharpens the routing consequence of, the designated partner fleet03/B16 r20 barrier.

## 2. Sources actually used at equations


Required Claude source pinned by the owner:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

Its proved rank-two positive-semidefinite statement is

`||p_{lambda_1 Y_1^2+lambda_2 Y_2^2}||_infinity
 <= pi ||p_Y||_infinity / sqrt(lambda_1 lambda_2)
 <= 2 pi / sqrt(lambda_1 lambda_2)`

for a genuine two-dimensional orthogonal projection `Y` of the original cap-one product source. The same source records the product-projection height `||p_Y||_infinity<=2` and explicitly does **not** infer independence of `Y_1,Y_2`.

The designated completed partner is fleet03/B16 r20:

`yspennstate/math-open-problems@bf4ea19e3c7e327cd53615128f4daaeee0e53811`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260923T000300Z-fleet03-B16-QFORM-r20/REPORT.md`.

It proves that for a nonzero scalar pivot an arbitrary dependent two-dimensional receiver with joint density cap one and both coordinate-marginal caps one can still make `X^2+2UV` have peak density `(1/2)sqrt(log R)`. It also identifies the valid source replacement: square peel plus the genuine rank-two affine half-Riesz theorem, whose in-range constant is `16 sqrt(30) |det H|^(-1/4)`.

## 3. Receiver theorem: a planar density cap is sufficient exactly on definite curvature

### Theorem 3.1 — definite planar curved pushforward

Let `Z` be an arbitrary random vector in `R^2` with probability density `rho` satisfying

`||rho||_infinity <= M`.

Let `B` be a real symmetric definite `2 x 2` matrix, `ell in R^2`, and `c in R`. Then

`T = Z^T B Z + ell^T Z + c`

has an essential density satisfying

`boxed: ||p_T||_infinity <= pi M / sqrt(det |B|).`               (3.1)

No independence between the coordinates of `Z` is assumed.

### Proof

It is enough to treat `B>0`; for `B<0` replace `T` by `-T`. Complete the square in the **value variable** `z`:

`z^T B z + ell^T z
 = (z+a)^T B (z+a) - a^T B a`,

`a=(1/2)B^(-1)ell`.

Translation does not change a density cap. Put

`w=B^(1/2)(z+a)`.

The density of `W` is bounded by

`M_B = M/sqrt(det B)`.

For every interval `I` of length `h`,

`{w: |w|^2 in I}`

is an annulus, a disk, or empty, and has planar area at most `pi h`. Therefore

`P(T in I) <= pi M_B h`.

Lebesgue differentiation gives (3.1). No continuity assertion is used. QED.

### Proposition 3.2 — cap-only failure for every nondefinite quadratic Hessian

The definiteness assumption cannot be removed if one keeps only a two-dimensional density cap.

For the canonical indefinite form `q(u,v)=uv`, fix `R>1` and put

`epsilon=1/(2 log R)`,

`E_R={(u,v):1<=u<=R, |uv|<=epsilon}`.

Then `|E_R|=1`, so `rho_R=1_{E_R}` is a probability density with cap one. Under `(u,v)->(u,s=uv)` the Jacobian is `1/u`, hence

`p_{uv}(s)=int_1^R du/u=log R`,  `|s|<=epsilon`.

Thus `||p_{uv}||_infinity>=log R -> infinity` at one fixed indefinite Hessian. By an invertible linear change of variables and rescaling the cap, the same conclusion holds for every fixed invertible indefinite `B`.

For rank-one semidefinite curvature, the unit-square law already makes the density of `U^2` behave as `1/(2 sqrt(s))` at zero. Hence no finite cap-only theorem exists for rank-deficient quadratic curvature either.

So, at the level of arbitrary planar receiver laws, **definite curvature is exactly the safe cap-only regime**. This is the positive counterpart to the partner's nonzero-pivot hyperbolic obstruction.

## 4. Product-projection corollary with arbitrary disjoint hub variables

Let `X_L` be a vector of independent original-coordinate variables, each with density at most one, and let

`Z=C^T X_L in R^2`,

where `C` is a real `|L| x 2` matrix of rank two. Put `G=C^T C`.

Whitening the two columns of `C` and applying the source two-dimensional product-projection theorem gives

`||p_Z||_infinity <= 2 / sqrt(det G)`.                           (4.1)

Let `H` be any random object independent of `X_L`; no density or moment condition on `H` is needed for the following conditioning step. Suppose

`Q = h(H) + ell(H)^T Z + Z^T B Z`,                              (4.2)

where `B` is fixed and definite. Applying Theorem 3.1 conditionally on `H`, uniformly in its value, and averaging gives

`boxed:
 ||p_Q||_infinity
 <= 2 pi / sqrt(det(C^T C) det|B|).`                            (4.3)

Again, the two coordinates of `Z` are generally dependent; only their source-valid joint projection density is used.

If `K=C B C^T` is the rank-two leaf quadratic block, then the product of its two nonzero eigenvalue magnitudes is

`pdet(|K|)=det(C^T C) det|B|`,

so (4.3) can be written invariantly as

`||p_Q||_infinity <= 2 pi / sqrt(pdet(|K|)).`                   (4.4)

A physical-matrix sufficient condition for (4.2) is that the leaf block factor as `K=CBC^T` and every outside-to-leaf coupling vector lie in `range(C)`. Conditioning the outside original coordinates then creates only the `ell(H)` term in (4.2).

## 5. Strict-N3 nonzero near-null family paid uniformly by the definite receiver

This is a diagnostic application of (4.3), not a claim that the exact-null endpoint is new.

Let `m` be even and choose balanced signs `eps_j in {+1,-1}`. Define orthonormal leaf directions

`a_j=1/sqrt(m)`, `b_j=eps_j/sqrt(m)`,

and

`Y=a^T X_L`, `Z=b^T X_L`.

For `-1<delta` define

`c_delta=sqrt(2(1+delta))`

and

`Q_delta
 = delta X_0^2 + 2 c_delta X_0 Y + Y^2 + Z^2`.                 (5.1)

Here `X_0` is an original coordinate independent of the leaf bank. The spectral matrix on the orthonormal span `(X_0,Y,Z)` is

`M_delta=[[delta,c_delta,0],[c_delta,1,0],[0,0,1]]`.

Its characteristic polynomial is

`-(lambda-1)(lambda+1)(delta-lambda+2)`,

so

`spec_nonzero(A_delta)={delta+2,-1,1}`.                         (5.2)

Thus every `delta>-1` lies in the three-large-eigenvalue target class.

The leaf pair `(Y,Z)` is a genuine two-dimensional projection of the same leaf product law; it is not asserted to have independent coordinates. Equation (4.1) gives `||p_(Y,Z)||_infinity<=2`. Conditional on `X_0=x`,

`Q_delta
 = (Y+c_delta x)^2 + Z^2 + (delta-c_delta^2)x^2`.

The projected pair has merely been translated, so Theorem 3.1 gives

`boxed: ||p_{Q_delta}||_infinity <= 2 pi`                       (5.3)

for every `m`, every `delta>-1`, and arbitrary independent cap-one input densities.

This includes every **nonzero** `delta` arbitrarily close to the null pivot.

### Physical no-pivot check

The physical entries are

`A_00=delta`, `A_jj=2/m`, `A_0j=c_delta/sqrt(m)`,

`A_jk=(1+eps_j eps_k)/m` for distinct leaves. Hence

`det A[{0,j},{0,j}]
 = 2 delta/m - c_delta^2/m
 = -2/m`,                                                        (5.4)

while for two leaves

`det A[{j,k},{j,k}]
 = 0` if `eps_j=eps_k`, and `4/m^2` if `eps_j=-eps_k`.          (5.5)

Therefore for every fixed no-pivot threshold `tau in (0,1]`, choosing

`0<|delta|<tau`, `m>2/tau`

puts (5.1) in strict N3: every physical diagonal and every physical pair determinant has magnitude `<tau`, while the three actual nonzero eigenvalues still have modulus at least one.

The source ruled one-sheet theorem already pays one sign side of such rank-three signature `(2,1)` forms. Equation (5.3) pays **both** sides for this factor-through-definite-receiver subclass.

## 6. Actual designated-partner application: why scalar Schur completion is the wrong payment here

For `delta!=0`, completing the physical hub variable in (5.1) gives

`Q_delta
 = delta (X_0 + c_delta Y/delta)^2
   + H_delta[Y,Z]`,

where

`H_delta[Y,Z]
 = -(2+delta)/delta * Y^2 + Z^2`.                               (6.1)

Thus

`|det H_delta|=(2+delta)/|delta|`.                              (6.2)

Applying the **valid** partner route—scalar square peel followed by the completed in-range rank-two affine half-Riesz theorem—yields the certificate

`||p_Qdelta||_infinity
 <= 16 sqrt(30) |delta|^(-1/2) |det H_delta|^(-1/4)`

`=16 sqrt(30) |delta|^(-1/4)(2+delta)^(-1/4)`.                  (6.3)

This diverges as `delta->0`, even though the true source-valid bound (5.3) stays at `2 pi`.

So (6.3) is not a false theorem; it is a quantitatively lossy routing choice. In this branch, conditioning on the original hub and spending the **definite projected-pair curvature before Schur completion** avoids the artificial near-null loss.

This is the concrete equation-level use of fleet03/B16 r20: its half-Riesz replacement remains necessary on genuinely indefinite receivers, but it should not be invoked before checking whether conditioning exposes a definite two-dimensional projected receiver.

## 7. Relation to the current proof map

The result does not solve N3 or full QFORM. It gives an exact routing rule:

1. If, after conditioning a disjoint original-coordinate hub/outside bank, the remaining nonlinear dependence factors through a two-dimensional product projection with **definite** quadratic part, use (4.3); projected-coordinate independence is irrelevant.
2. If that two-dimensional quadratic part is indefinite or rank deficient, the projection-height abstraction alone is mathematically insufficient. Proposition 3.2 and fleet03/B16 r20 both show why.
3. The genuinely unpaid B16 interface is therefore the **indefinite near-null / overlapping-product-provenance** regime. A successful bridge there must retain a source invariant stronger than `||p_Z||_infinity`, such as the rank-two half-Riesz/Fourier geometry, or an original-coordinate mixed-Fresnel/grouped-bank structure before any singular Schur factor is inverted.

This also explains why a theorem that merely says “every two-dimensional projection has density at most two” cannot finish the remaining two-sheet branch, while the same theorem is already sufficient on definite curved fibers.

## 8. Scope and review status

- Full QFORM: **OPEN**.
- Full N3: **OPEN**.
- Theorem 3.1 and Proposition 3.2: elementary complete proofs above.
- Product-projection corollary (4.3): complete given the source-pinned two-dimensional projection theorem.
- Family (5.1): complete target-valid supporting subclass, including nonzero near-null strict-N3 parameters.
- Continuity: not claimed here; only essential boundedness is proved.
- No moments, support bounds, log-concavity, identical-law assumption, diagonal-basis independence, or post-rotation independence are used.
- No end-to-end independent review of this report has been performed.
