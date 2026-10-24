SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-24T09:07:49Z.
attacking: grouped-reflection Schur localization — transfer the newest physical reflection boundary dichotomy to product-preserving disjoint banks, make arbitrary outside positive localization exactly mass-homogeneous, and quantify why physical-coordinate reciprocal payment cannot replace bank aggregation.

# account02/B14 — grouped reflection Schur-boundary localization

Run: `20260924T090749Z-account02-B14-QFORM-auto11`

Status: `SUPPORTING_LOCALIZATION_THEOREM_PROVED / FIXED_SOURCE_APPLIED / DESIGNATED_PARTNER_APPLIED / FULL_QFORM_OPEN`.

Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. The unrestricted target remains open and continuity is kept separate from the universal-height question.

## 1. First unpaid implication

`QFORM-BANK-REFLECTION-FACTOR-OR-SAMEBANK-CURVATURE-EXIT-v1`:

Starting only from `s_3(A)>=1`, expose a product-preserving three-bank receiver whose paid quadratic core remains uniformly nondegenerate after every same-bank term is retained, with the remaining sources entering through admissible affine/environment variables; otherwise force an already-paid D'/D5/projected-crossing/shared-bank/pair/ridge/hub exit. The calculation below proves that, once such a reflection bank exists, arbitrary translations, fragmented/unbounded outside laws and conditioning-generated affine terms are zero-tax. What remains unpaid is the structural extraction of the bank receiver from a general matrix without deleting nonseparable same-bank curvature.

## 2. Fixed source and designated partner

The pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was read through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The source results used below are:

1. **Theorem A:** in dimension three, if all eigenvalues have modulus at least `sigma`, arbitrary linear terms are allowed and

   `||p_Q||_infinity <= 6 sqrt(pi)/sigma`.

2. **Theorem F:** a rank-three quadratic part with all active coordinate leverages at most `1/2`, plus an arbitrary residual whose active-active block is diagonal, has the uniform Fresnel/Brascamp-Lieb bound; in the unit-eigenvalue/full-frame case used below this gives `||p_Q||_infinity <=12`.

3. **Theorem B:** under the exact three-large-eigenvalue hypothesis,

   `||p_Q||_infinity <= 2 sqrt(2 pi) sum_i ||P e_i||`,

   where `P` projects to the large-eigenvalue range.

The newest compatible designated partner is account03/B14 run `20260924T083635Z-account03-B14-QFORM-auto11`, canonical math commit `58a185c004fe59f2c6d4c35965ae058d00d80192`. Its `QFORM-REFLECTION-SCHUR-BOUNDARY-DICHOTOMY-v1` treats the physical reflection block

`B_* = I_3 - (2/3) 1 1^T`,

whose spectrum is `{1,1,-1}`. For a block matrix `[[B_*,C],[C^T,D]]`, it identifies the Schur boundary matrix

`R=D-C^T B_* C`.

If `R!=0`, every deterministic translation makes the boundary a nonconstant quadratic polynomial of the outside absolutely continuous variables, hence atomless, and the majority sheet has a global `C_0` density of height at most `pi sqrt(2)`. If `R=0`, the compressed matrix has rank three and the two one-sided sheet-edge traces must cancel in the assembled full `C_0` density; the full height remains at most `6 sqrt(pi)`. This run transfers that exact invariant to grouped variables while preserving product provenance.

## 3. Mass-homogeneous affine-mixture compiler

### Theorem `QFORM-REFLECTION-AFFINE-SUBMEASURE-COMPILER-v1`

Let `S=(S_1,S_2,S_3)` have independent real coordinates with density caps

`||p_{S_r}||_infinity <= K`.

Let `tau` be any finite positive measure of mass `m` on a parameter space `Omega`; no density, product structure, moment, support or boundedness assumption is imposed on `tau`. Let `b:Omega->R^3` and `c:Omega->R` be measurable. Define the output finite measure

`eta(E)=int P(S^T B_* S+b(omega)^T S+c(omega) in E) tau(d omega)`.

Then

`boxed(||d eta/ds||_{infinity,ess} <= 6 sqrt(pi) K^2 m).`                 (3.1)

#### Proof

Fix `omega`. Put `Y=K S`; its three coordinates are independent and have density cap at most one. Then

`S^T B_* S+b^T S+c
 =Y^T (B_*/K^2)Y+(b/K)^T Y+c`.

All three eigenvalues of `B_*/K^2` have modulus `K^{-2}`. Fixed-source Theorem A therefore gives, uniformly in `b,c`,

`P(S^T B_* S+b^T S+c in I) <= 6 sqrt(pi) K^2 |I|`

for every bounded interval `I`. Integrating this inequality against the positive measure `tau` gives (3.1). No normalization of `tau` is performed, so the estimate is exactly linear in its mass. QED.

### Consequences

* Arbitrary deterministic or random translations are free: take

  `b(t)=2 B_* t`, `c(t)=t^T B_* t`.

* Arbitrary conditioning-generated affine fields are free as long as the active quadratic object remains this bank reflection core.

* If `tau=sum_j tau_j` is any finite or countable positive localization of an outside environment, then each output piece costs `6 sqrt(pi)K^2 tau_j(Omega)` and summing returns the same bound. Fragment number, fragment separation, support diameter, tails and moments never appear.

This is the exact localization property needed for the assignment: localize the **outside/environment label**, not the active bank law on which curvature is paid.

## 4. Product-preserving grouped-bank reflection theorem

Partition original coordinates into three disjoint active banks `I_1,I_2,I_3` and an outside set `J`. Choose unit vectors `u_r` supported on `I_r`, and let `U` be the `3 x |I|` matrix with rows `u_r^T`. Because the supports are disjoint,

`UU^T=I_3`

and

`S=U X_I=(u_1^T X_{I_1},u_2^T X_{I_2},u_3^T X_{I_3})`

has **independent** coordinates. This is genuine original-product provenance; no independence after rotation is asserted.

Consider the exact original-coordinate matrix

`A = [[U^T B_* U, U^T C], [C^T U, D]]`,                         (4.1)

where `C` is arbitrary and `D` is arbitrary symmetric. Then

`Q=X^TAX=S^T B_* S+2 S^T C Z+Z^T D Z`,                         (4.2)

with `Z=X_J` independent of `S`.

If `||p_{S_r}||_infinity<=K`, (3.1), with the outside variable itself as the mixture parameter, gives

`boxed(||p_Q||_{infinity,ess} <= 6 sqrt(pi) K^2).`               (4.3)

This remains true under arbitrary deterministic translations of every original coordinate: those translations only alter the bank shifts, the outside parameter and the affine/constant terms in (4.2).

### Exact target verification

The active principal block in (4.1) is `U^T B_* U`. Its nonzero eigenvalues equal those of

`B_* UU^T=B_*`,

namely `{1,1,-1}`. Hence the active principal block has two eigenvalues `>=1` and one `<=-1`. Cauchy interlacing with the full matrix A therefore yields

`lambda_1(A)>=1`, `lambda_2(A)>=1`, and `lambda_min(A)<=-1`.

Thus **every matrix (4.1) is already in the exact owner target**, regardless of `C,D`.

## 5. The newest partner's Schur boundary survives bank compression exactly

Define

`R=D-C^T B_* C`.

Because `B_*^{-1}=B_*`, (4.2) completes exactly as

`Q=(S+B_* C Z)^T B_*(S+B_* C Z)+Z^T R Z`.                      (5.1)

After a deterministic translation of the original variables, the same identity holds with translated `S,Z`, and the sheet boundary is

`z -> (z+t_J)^T R (z+t_J)`.

This is the **same Schur-boundary invariant** as in the newest account03/B14 physical theorem. The only nontrivial provenance check is independence of the three compressed coordinates; here it is supplied by the disjoint original banks.

To place the active densities under the partner's unit cap, scale `Y=K S` and multiply the output by `K^2`. The active matrix becomes exactly `B_*`; the cross block becomes `K C`; and the Schur remainder becomes

`K^2 D-(KC)^T B_*(KC)=K^2 R`.

Therefore the partner dichotomy transfers without alteration of its zero/nonzero branch.

### Non-flat branch

If `R!=0` and the outside law is an absolutely continuous product law, then every translated boundary is atomless. The majority-sheet submeasure of Q has

`boxed(p_+ in C_0(R),  ||p_+||_infinity <= pi sqrt(2) K^2).`     (5.2)

More generally, let `tau` be any positive **outside submeasure** of mass `m` that is absolutely continuous with respect to the original outside product law. The partner's conditional majority kernels have uniform height `pi sqrt(2)K^2`, so direct positive mixing gives

`boxed(||p_{+,tau}||_infinity <= pi sqrt(2) K^2 m).`             (5.3)

Thus arbitrary finite or countable outside fragmentation is exactly zero-tax even at the sheet level.

### Schur-flat branch

If `R=0`, the boundary is deterministic for every translation and cannot itself regularize either sheet. But (4.1) factors as

`A=F^T B_* F`,   `F=[U, B_* C]`,

so `rank(A)=3`. After the same scale reduction, the newest partner theorem says the two one-sided sheet traces must match in the assembled full density. The full law obeys (4.3); for an outside positive piece of mass `m`, (3.1) gives

`boxed(||p_{tau}||_infinity <= 6 sqrt(pi) K^2 m).`               (5.4)

Hence the flat branch is also exactly mass-homogeneous **provided the two sheets are reassembled before taking the localization supremum**. Absoluteizing them separately would destroy a real boundary cancellation.

This proves the grouped/bank analogue explicitly requested by the newest partner, under the exact factor-through-bank structure (4.1).

## 6. Arbitrary fragmented/unbounded flat banks

The grouped theorem is not a compact-support or finite-fragment statement. Take an even bank size `m=2r` and put

`u_r = m^{-1/2}(1,...,1)`

on each bank. Let all original coordinates have arbitrary independent densities bounded by one; they may be translated arbitrarily, have countably fragmented or unbounded support, and need have no moments.

The Rogozin/Ball estimate used in the fixed source's Lemma 1 says that the density of a sum of `2r` independent cap-one variables is at most `1/sqrt(r)`. Therefore

`||p_{S_r}||_infinity
 <= sqrt(m)/sqrt(r)
 = sqrt(2).`

Thus `K=sqrt(2)` is valid without any geometric assumption on the source laws, and the grouped reflection theorem gives

`boxed(||p_Q||_{infinity,ess} <= 12 sqrt(pi))`                  (6.1)

for every factor-through-bank matrix (4.1), every `C,D`, and every allowed rough product input.

If `R!=0`, the majority-sheet bound sharpens to

`boxed(||p_+||_infinity <= 2 pi sqrt(2)).`                       (6.2)

Again no fragment number, separation, diameter, support radius or moment appears.

## 7. Completed fixed-source result applied to a real obstruction

Now set `C=D=0` and denote

`A_m=U^T B_* U`.

This matrix has exactly three nonzero eigenvalues `{1,1,-1}`, so it is an exact-target rank-three family.

### 7.1 Every physical triple degenerates

Every physical coefficient is `O(1/m)`. A physical 3x3 principal block is singular unless it chooses one coordinate from each of the three banks. Every invertible physical triple is a permutation of

`m^{-1} B_*`,

so its least absolute eigenvalue is exactly `1/m`. Fixed-source Theorem A, applied after conditioning on all other coordinates, therefore yields only

`boxed(||p_Q||_infinity <= 6 sqrt(pi) m)`                       (7.1)

from **every** physical triple.

A physical pair from two different banks is

`m^{-1} [[1/3,-2/3],[-2/3,1/3]]`,

whose eigenvalues are `1/m` and `-1/(3m)`; a same-bank pair is singular. Thus physical pair/pivot reciprocal payment also loses a factor growing with `m`.

### 7.2 The original-coordinate fibre theorem also loses dimension

For `A_m`, the range projection is `P=U^T U`. Every one of the `3m` active coordinates has

`||P e_i||=1/sqrt(m)`.

Hence fixed-source Theorem B gives only

`boxed(||p_Q||_infinity <= 6 sqrt(2 pi) sqrt(m)).`               (7.2)

This is the exact diffuse-eigenvector loss predicted by the source counterexample search.

### 7.3 But the completed whole-law Fourier theorem stays constant

Diagonalize `B_*` inside the three-dimensional bank space. The three eigenvectors of `A_m` are spread over the physical coordinates with leverage exactly `1/m`. For every `m>=2` this is at most `1/2`. Taking all `3m` active coordinates as the set `I`, the residual active-active block is zero (hence diagonal), `G_I=I_3`, and the three eigenvalue magnitudes equal one. Fixed-source Theorem F therefore gives

`boxed(||p_Q||_infinity <= 12)`                                 (7.3)

for the **same** exact-target family, uniformly in `m` and for all arbitrary cap-one product marginals.

This is a real source-valid obstruction to physical localization: (7.1) grows linearly and (7.2) grows like `sqrt(m)`, while the completed whole-law theorem (7.3) is constant. The underlying law is not changing; only the proof interface is.

It also shows why the new grouped Schur theorem is relevant rather than cosmetic. When the core is diffuse, the correct object is the entire disjoint bank, not a chosen physical triple or a sum of physical-cell suprema.

## 8. What is new and what is source-matched

Source-matched, not claimed new:

* fixed-source Theorems A, B, F and the Rogozin/Ball concentration input;
* account03/B14's physical reflection Schur-boundary dichotomy, moving-boundary regularity and flat-branch sheet cancellation;
* ordinary conditioning and positive-mixture linearity.

New supporting synthesis proved here:

1. `QFORM-REFLECTION-AFFINE-SUBMEASURE-COMPILER-v1`: exact mass-homogeneous arbitrary positive mixing of all conditioning-generated affine fields around an active reflection bank, with no assumption on the mixing law.

2. `QFORM-GROUPED-REFLECTION-SCHUR-BOUNDARY-LOCALIZATION-v1`: the newest physical Schur-boundary dichotomy transfers verbatim to **product-preserving disjoint linear banks**, because bank independence is genuine before compression and the Schur invariant is unchanged by the cap-normalizing scale. In the non-flat branch even majority-sheet outside localization is mass-linear; in the flat branch full-law sheet cancellation must be retained before localization.

3. The explicit flat-bank family `A_m=U^T B_*U` gives a quantitative comparison of three completed source routes: physical triple `O(m)`, fibre `O(sqrt(m))`, whole-bank Fresnel `12`. This isolates aggregation-before-reciprocal-payment as a genuine structural requirement.

## 9. Exact remaining gap

The full QFORM theorem is still OPEN. A general symmetric A with `s_3(A)>=1` need not have the factor-through-bank form (4.1). In particular, after selecting a promising bank direction, arbitrary same-bank quadratic curvature and cross components orthogonal to that direction cannot be deleted: for unbounded rough sources, small coefficient norm is not a small random quadratic error.

So the next unpaid implication is genuinely structural, not translational:

`QFORM-BANK-REFLECTION-FACTOR-OR-SAMEBANK-CURVATURE-EXIT-v1`.

Either derive a quantitatively nondegenerate product-bank core with all residual same-bank terms still represented, or prove those residual terms force an already-paid whole-law receiver. The present run removes arbitrary translations, outside positive fragmentation, unbounded supports and Schur-boundary motion from that remaining debt.
