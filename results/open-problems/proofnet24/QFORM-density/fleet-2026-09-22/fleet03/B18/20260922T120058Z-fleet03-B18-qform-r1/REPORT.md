# fleet03/B18 — source-exact literature transfer to a bipartite/Schur branch

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T120058Z-fleet03-B18-qform-r1`  
**Assignment:** Literature-to-proof transfer  
**Status:** `ESSENTIAL_STEP_APPLIED / SOURCE_EXACT_BILINEAR_TRANSFER / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction state

The active conjecture is:

> For every `n`, independent real random variables `X_i` with probability densities `f_i` satisfying `0 <= f_i <= 1`, and every real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with `||p_Q||_infinity <= C` for one universal finite constant `C`, or give a valid counterexample.

No moments, centering, identical laws, log-concavity, continuity, or connected support are assumed. The stronger requested continuity conclusion is separate from the essential bounded-density target.

The live corrections are enforced here: law-uniform pointwise Fresnel decay is false; a rotation destroys coordinate independence; and an unrestricted fiber-supremum argument can lose dimension. None of those mechanisms is used below.

## 2. Primary source checked exactly

The transferable source is Jesse M. Banks, *Random Matrices and Provable Algorithms for Approximate Diagonalization*, UC Berkeley PhD thesis, 2022, Chapter 4, especially Theorem 4.15 and Corollary 4.18. Primary source: `https://escholarship.org/uc/item/1dn005fg`.

Banks defines `delta_infinity(Z)` as the `L^infinity` norm of the density of `Z`. Theorem 4.15 assumes two random matrices `X,Y` whose entries are independent and each have scalar density bounded a.e. by `K`, and deterministic `Z,U,V,W`; it controls the density of

`q(X,Y)=X^T Z Y + X^T U + V^T Y + W`.

For the scalar case `k=1`, Corollary 4.18 gives

`delta_infinity(q(X,Y)) <= 4 K^2 sqrt(2 e pi) * min_{j>=2} 1/[sqrt(j) (prod_{i=1}^j sigma_i(Z))^(1/j)]`.

The factor `4 K^2` is exactly `2 (sqrt(2)K)^2` from the source. The later Gaussian improvement in the same corollary is **not used**. Thus the part transferred below uses only independence and the one-dimensional density cap, exactly matching the owner's input class on disjoint coordinate groups. There are no hidden moment or log-concavity assumptions.

For comparison, Rudelson--Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, IMRN 2015, DOI `10.1093/imrn/rnu243`, supplies the underlying bounded-density projection technology. It is source-compatible with independent bounded-density coordinates, but projection density alone does not control an indefinite quadratic pushforward, so it is not promoted to a full proof here.

Results requiring Gaussianity, subgaussian tails/Hanson--Wright hypotheses, log-concavity/Carbery--Wright hypotheses, or finite moments were screened out: no such missing hypothesis is silently imported.

## 3. First transferred theorem: a physical bipartite block

Let `I,J,O` be disjoint coordinate sets, with `I` and `J` nonempty. Write `U=X_I`, `V=X_J`, and condition on `X_O=w`. Suppose the principal block on `I union J` has the form

`A_{I union J,I union J} = [[0,B],[B^T,0]]`.

All couplings from `I union J` to `O` are arbitrary. Conditional on `X_O=w`, the full quadratic form has the form

`Q_w(U,V)=2 U^T B V + alpha_w^T U + beta_w^T V + c_w`.

The entries of `U` and `V` are mutually independent and each have density at most one. If the two groups have unequal sizes, pad the shorter vector and the rectangular matrix `B` with independent auxiliary uniform coordinates and zero rows/columns; the scalar expression and its law do not change, while Banks' square-matrix statement applies exactly.

### Theorem 3.1 — `QFORM-BANKS-PHYSICAL-BIPARTITE-v1`

If `sigma_2(B)>0`, then `Q` has a density and

`||p_Q||_infinity <= 2 sqrt(e pi) / sqrt(sigma_1(B) sigma_2(B)).`

In particular, if `sigma_2(B)>=1`, then

`||p_Q||_infinity <= 2 sqrt(e pi) = 5.844564730644556... .`

### Proof

Apply Banks Corollary 4.18 with `K=1`, `Z=2B`, and `j=2`. Since

`(sigma_1(2B) sigma_2(2B))^(1/2)=2 sqrt(sigma_1(B)sigma_2(B))`,

its bound becomes

`4 sqrt(2 e pi) / [sqrt(2) * 2 sqrt(sigma_1(B)sigma_2(B))]`

`= 2 sqrt(e pi)/sqrt(sigma_1(B)sigma_2(B)).`

This bound is uniform in the conditioned outside value `w`, because Banks' theorem allows arbitrary deterministic linear terms. Averaging the conditional densities over `w` preserves the same `L^infinity` bound. QED.

### Corollary 3.2 — the entire pure bipartite target class is solved

If

`A=[[0,B],[B^T,0]]`

(up to extra zero coordinates), then the nonzero eigenvalues of `A` are the pairs `+sigma_i(B),-sigma_i(B)`. Therefore the owner's hypothesis of at least three eigenvalues with absolute value at least one forces `sigma_2(B)>=1`; pair symmetry actually gives at least four such eigenvalues. Theorem 3.1 yields

`||p_{X^T A X}||_infinity <= 2 sqrt(e pi)`

for arbitrary independent coordinate densities bounded by one.

This is a genuine target subclass with no Gaussian, moment, log-concavity, or diagonal assumption.

## 4. Substantive partner input

I consumed fleet04/B18's completed source-bound result `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, from scientific commit

`441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`,

report blob

`f33758725ac803c6375215b522c86bd6409d2521`.

That lemma proves: if `R` has density at most `M`, and conditionally on `R=r` a variable `V_r` has density at most one (no independence between `R` and `V_R` required), then for `a !=0`,

`T=R+a V_R^2`

has density at most

`2 sqrt(M/|a|)`.

The proof uses the exact one-square density kernel and a bathtub bound; it does not require moments, Gaussianity, or log-concavity.

## 5. New theorem from Banks + the partner smoothing lemma

Select one original coordinate `z` with diagonal pivot

`a=A_zz !=0`.

Write the remaining coordinates as `y`, the corresponding column as `b`, and the remaining principal block as `C`, so

`A=[[a,b^T],[b,C]]`.

Completing the square only in the original coordinate `X_z` gives the exact identity

`Q = a (X_z + a^{-1} b^T y)^2 + y^T S y`,

where

`S=C-bb^T/a`

is the Schur complement. No rotation is performed.

Assume that the coordinates of `y` contain disjoint groups `I,J` such that

`S_II=0`, `S_JJ=0`, and `B=S_IJ`.

All remaining coordinates are put in `O` and may couple arbitrarily to `I` and `J` through `S`.

### Theorem 5.1 — `QFORM-BANKS-BIPARTITE-SCHUR-SMOOTHING-v1`

For every `j>=2` with `sigma_j(B)>0`, define

`g_j(2B)=(prod_{i=1}^j sigma_i(2B))^(1/j)`.

Then the full quadratic form has a density satisfying

`||p_Q||_infinity <= 4 (2 e pi)^(1/4) / [ j^(1/4) sqrt(|a| g_j(2B)) ].`

In particular, if `|a|>=1` and `sigma_2(B)>=1`, then

`||p_Q||_infinity <= 2 sqrt(2) (e pi)^(1/4)`

`= 4.835106919456717... .`

### Proof

Condition on the coordinates `X_O=w`. In the Schur residual `R=y^T S y`, the zero within-block assumptions make the dependence on `U=X_I` and `V=X_J` exactly

`R_w(U,V)=2U^T B V + alpha_w^T U + beta_w^T V + c_w`.

Banks Corollary 4.18, with the same padding argument if necessary, therefore gives the uniform conditional density bound

`M_j = 4 sqrt(2 e pi)/[sqrt(j) g_j(2B)].`

Now write

`V_shift = X_z + a^{-1} b^T y`.

Because `X_z` is independent of every coordinate in `y` and has density at most one, conditioning on any value `R_w=r` makes the law of `V_shift` a mixture of translations of the density of `X_z`. Hence its conditional density is still at most one:

`p_{V_shift | R_w=r}(t) = E[ f_z(t-a^{-1}b^T y) | R_w=r ] <=1`

for almost every `r`.

This verifies, rather than assumes, the nonindependent conditional-density hypothesis in fleet04/B18's square-smoothing lemma. Applying that lemma to

`Q_w = R_w + a V_shift^2`

gives

`||p_{Q_w}||_infinity <= 2 sqrt(M_j/|a|)`

`=4(2e pi)^(1/4)/[j^(1/4) sqrt(|a|g_j(2B))].`

The bound is uniform in `w`, so averaging over `X_O` preserves it.

For `j=2` and `sigma_2(B)>=1`, monotonicity gives `sigma_1(B)>=1`, hence `g_2(2B)>=2`. Therefore

`||p_Q||_infinity <= 4(2e pi)^(1/4)/[2^(1/4) sqrt(2|a|)]`

`=2 sqrt(2)(e pi)^(1/4)/sqrt(|a|)`,

which is at most the displayed constant when `|a|>=1`. QED.

## 6. Why this is a real transfer rather than a hypothesis mismatch

The source theorem is **not** applied with the same vector on both sides of a bilinear form. That would violate its independence structure. Instead, `U` and `V` are disjoint sets of the original independent coordinates, and the cross term is exactly bilinear after physical-coordinate conditioning.

Likewise, the Schur completion does not rotate the input law. The only dependent object is the shifted square variable after conditioning on the residual, and fleet04/B18's proved lemma was designed precisely for this dependence; the conditional density cap is verified by a mixture-of-translations identity.

Thus every probabilistic hypothesis used is present in the owner's model.

## 7. Exact remaining implication

The full conjecture remains **OPEN / NOT PROVED**. The spectral hypothesis alone has not yet been shown to force either of the physical structures used above.

The next target-relevant structural implication is:

> From a real symmetric `A` with at least three eigenvalues `|lambda|>=1`, either extract (possibly after one physical scalar Schur pivot) disjoint original-coordinate groups `I,J` with a dimension-free lower bound on the second singular value or geometric top-two singular scale of the corresponding cross block, **or** prove an aggregate version of the Banks bound that pays over many weak cross blocks without selecting a single dimension-degrading minor.

The Hadamard/flat-eigenvector examples in the current programme show why a naive fixed-minor extraction can lose dimension. The theorem above therefore closes the analytic density step **conditional on a quantitative bipartite physical block**, but leaves the global spectral-to-coordinate bridge unpaid.

A second useful direction is to combine the partner's determinant-sensitive Schur-pivot branch with this bilinear branch: definite Schur complements are already paid by fleet04/B18, while sufficiently rank-two bipartite Schur components are paid here. The remaining 3-by-3 majority-sign and diffuse higher-dimensional residual geometries are the natural interface for B19/B20 proof assembly.

## 8. Claim statuses

- `QFORM-BANKS-PHYSICAL-BIPARTITE-v1`: **PROVED**, source-exact under the owner's density hypotheses.
- Pure bipartite target matrices with at least three `|lambda|>=1`: **PROVED** with constant `2 sqrt(e pi)`.
- `QFORM-BANKS-BIPARTITE-SCHUR-SMOOTHING-v1`: **PROVED**, using fleet04/B18's completed dependent square-smoothing lemma.
- Extraction/aggregation of the required physical block from the bare three-eigenvalue hypothesis: **OPEN**.
- Full universal QFORM conjecture: **OPEN / NOT PROVED**.
