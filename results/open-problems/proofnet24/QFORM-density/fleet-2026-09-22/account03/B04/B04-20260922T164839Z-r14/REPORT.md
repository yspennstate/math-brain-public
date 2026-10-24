# account03/B04 QFORM — scalar-pivot rank-two Schur closure without a leverage hypothesis

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B04-20260922T164839Z-r14`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope, fresh control, and source pins

The exact target remains: for every dimension, every product law with independent real coordinate densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal bound for the density of `X^T A X`, or give a valid counterexample. Continuity is tracked separately.

Fresh owner control at publication is revision `2026-09-22.7`; the proof-first continuation keeps all workers on the full QFORM target. The designated partner `account04/B04` had no completed current-QFORM handoff/report visible at the fresh snapshot, so no partner result is fabricated. This run instead applies a completed compatible other-worker theorem to an actual inequality:

- `account02/B16`, `QFORM-HEAVY-ROW-PROJECTED-RANK2-HALF-RIESZ-v1`, canonical source `yspennstate/math-open-problems@d2e3dd1587a3fa93707631ea847c48279f3dc6dc`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260922T163840Z-account02-B16-qform-r13/REPORT.md`.

It is combined with the earlier B04 product-Fourier theorem:

- `QFORM-DIFFUSE-RANK2-L3-v1` and `QFORM-DIFFUSE-SCHUR-PIVOT-v1`, source `yspennstate/math-open-problems@685929d9daee92a164dbf6ba6f9305d2e6550826`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/a03-b04-20260922T125025Z-qform-r12/REPORT.md`.

The live correction ledger was refreshed immediately before publication. In particular this proof does not use uniform one-dimensional pointwise Fresnel decay, independence after spectral rotation, a fixed good principal triple, a single-Schur-extraction implication from the global hypothesis, or fiberwise conditional-density independence.

## 2. A square-kernel reduction that preserves original-coordinate product structure

Let the last original coordinate be denoted `Z`, let the remaining coordinates be `W`, and write

`A = [[C,b],[b^T,a]]`, with `a != 0`.

Define its Schur complement

`S = C - b b^T/a`.

Completing the square only in the original coordinate `Z` gives the exact identity

`Q = X^T A X = R(W) + a V(W,Z)^2`,

where

`R(W)=W^T S W`,
`V(W,Z)=Z+a^(-1)b^T W`.

Conditional on `W`, `V` is only a translate of the original variable `Z`; hence its conditional density is bounded by one. The conditional density of `aV^2` therefore obeys, for `s` on the appropriate half-line,

`p_{aV^2 | W}(s) <= |a|^(-1/2)|s|^(-1/2)`.

Consequently, for almost every `t`,

`p_Q(t) <= |a|^(-1/2) E |t-R(W)|^(-1/2)`.            (2.1)

No independence between `R` and `V` is asserted or needed.

Assume from now on that `S` has rank exactly two, with nonzero eigenvalues `mu_1,mu_2`, and write

`S=U diag(mu_1,mu_2) U^T`,

where `U` has orthonormal columns. Let `ell_j=||u_j||_2^2` denote its physical row leverages.

## 3. Indefinite Schur complement: diffuse and heavy rows meet exactly

Assume `mu_1 mu_2<0`.

### 3.1 Diffuse half: all row leverages at most 1/2

If `max_j ell_j <=1/2`, the earlier B04 product-Fourier theorem gives

`||p_R||_3 <= (3e)^(2/3)|mu_1 mu_2|^(-1/3)`.

The already-proved dependent-square smoothing step applied to the actual completed-square identity above yields

`||p_Q||_infinity
 <= 4 sqrt(3e) |a|^(-1/2)|mu_1 mu_2|^(-1/4)`.       (3.1)

Numerically `4 sqrt(3e)=11.4226760335...`.

### 3.2 Heavy half: one row leverage exceeds 1/2

Suppose instead that some row has `ell_i>1/2`. Apply the completed `account02/B16` theorem directly to

`Y=U^T W`, `S_2=diag(mu_1,mu_2)`.

That theorem gives

`sup_t E |t-R(W)|^(-1/2)
 <= 2^(1/4) C_ind ell_i^(-1/4)|mu_1 mu_2|^(-1/4)`,       (3.2)

where

`C_ind = 8*3^(3/4)*5^(1/4)/sqrt(e)
       = 16.5396451661...`.

Because `ell_i>1/2`,

`ell_i^(-1/4) < 2^(1/4)`.

Substitute (3.2) into (2.1). Then

`||p_Q||_infinity
 <= sqrt(2) C_ind |a|^(-1/2)|mu_1 mu_2|^(-1/4)`.       (3.3)

Thus the formerly missing overlap between a scalar completed square and a heavy rank-two projected residual is paid without assuming a fresh independent third direction.

## 4. Definite Schur complement: an unconditional two-dimensional projection cap

Assume `mu_1 mu_2>0`. We first record an explicit product-measure projection bound sufficient here.

### Lemma 4.1 — every two-dimensional orthogonal projection has density at most e

Let `Y=U^T W` for an arbitrary `m x 2` orthonormal frame `U` and independent coordinate densities bounded by one. Then `Y` has a density `rho` satisfying

`||rho||_infinity <= e`.                                      (4.1)

Proof. If every row leverage is at most `1/2`, the same geometric Brascamp--Lieb/Hausdorff--Young calculation underlying `QFORM-DIFFUSE-RANK2-L3-v1`, now with no coordinate potentials, gives

`||hat rho||_1 <= (2pi)^2 e`,

and Fourier inversion gives (4.1).

If a row `i` has leverage `c=ell_i>1/2`, rotate the two-dimensional output plane so that row `i` is `(sqrt(c),0)`. Write the contribution of all other physical coordinates as `(V_1,V_2)`. For the joint density,

`rho(y_1,y_2)
 = integral f_i(x) rho_V(y_1-sqrt(c)x,y_2) dx
 <= c^(-1/2) p_{V_2}(y_2)`.

The coefficient vector defining `V_2` has Euclidean norm one, because the rotated second frame column is orthogonal to row `i`. The standard one-dimensional product projection theorem used in the cited `account02/B16` source gives `||p_{V_2}||_infinity<=sqrt(2)`. Hence

`||rho||_infinity <= sqrt(2/c) <2<e`.

This proves (4.1). QED.

### Lemma 4.2 — definite rank-two quadratic density

For `R=Y^T diag(mu_1,mu_2)Y` with `mu_1 mu_2>0`, Lemma 4.1 and the polar/coarea formula give

`||p_R||_infinity <= pi e |mu_1 mu_2|^(-1/2) =: B`.      (4.2)

Indeed after scaling by `diag(sqrt(|mu_1|),sqrt(|mu_2|))`, the joint density is at most `e/sqrt(|mu_1mu_2|)`, and the density of squared radius costs exactly a factor `pi`. Reflection handles the negative-definite case.

For any probability density bounded by `B`, splitting the half-Riesz integral at radius `r>0` gives

`E|t-R|^(-1/2) <=4B sqrt(r)+r^(-1/2)`.

Choosing `r=1/(4B)` yields

`sup_t E|t-R|^(-1/2) <=4 sqrt(B)
 <=4 sqrt(pi e)|mu_1mu_2|^(-1/4)`.                       (4.3)

Combining (4.3) with (2.1),

`||p_Q||_infinity
 <=4 sqrt(pi e)|a|^(-1/2)|mu_1mu_2|^(-1/4)`,             (4.4)

with coefficient `11.6891294613...`.

## 5. Main theorem — no leverage hypothesis remains in the rank-two Schur branch

### Theorem 5.1 — `QFORM-RANK2-SCHUR-NOLEVERAGE-v1`

Let the physical coordinates of `X=(W,Z)` be independent and have densities at most one. Suppose

`A=[[C,b],[b^T,a]]`, `a!=0`,

and the Schur complement `S=C-bb^T/a` has rank exactly two with nonzero eigenvalues `mu_1,mu_2`. Then `Q=X^TAX` has an essentially bounded density satisfying

`||p_Q||_infinity
 <= C_* |a|^(-1/2)|mu_1mu_2|^(-1/4)`,                    (5.1)

where

`C_* = sqrt(2) C_ind
     = 8 sqrt(2) 3^(3/4) 5^(1/4)/sqrt(e)
     = 23.3905905108... <23.391`.

Proof. If `S` is indefinite and diffuse, use (3.1); if indefinite and has a row of leverage above `1/2`, use (3.3); if definite, use (4.4). Each of the two smaller constants is below `C_*`. QED.

This theorem is the direct product-preserving resolution of the scalar-pivot/rank-two **overlapping innovation** obstruction: the completed square may reuse all physical coordinates supporting the rank-two residual through its shift `a^(-1)b^T W`. No post-rotation independence is required.

The theorem proves absolute continuity and an essential-supremum bound in its stated branch. This argument does not separately prove that the density has a continuous representative.

## 6. Exact-rank-three determinant aggregation corollary

Assume additionally that `A` has rank exactly three. For a physical coordinate `i` with `a=A_ii!=0`, its Schur complement has rank exactly two. Define

`P_i := sum_{j<k; j,k != i} |det A_{ {i,j,k} }|`.

By the Schur determinant identity,

`det A_{ {i,j,k} } = a det S_{ {j,k} }`.

If `S=U diag(mu_1,mu_2)U^T`, then

`det S_{ {j,k} } = mu_1mu_2 det(U_{ {j,k} })^2`.

Cauchy--Binet gives `sum_{j<k}det(U_{ {j,k} })^2=1`, hence

`P_i=|a| |mu_1mu_2|`.                                         (6.1)

Theorem 5.1 therefore becomes the aggregate physical-coordinate bound

`||p_Q||_infinity <= C_* (|A_ii| P_i)^(-1/4)`.            (6.2)

Writing an exact-rank-three spectral decomposition `A=R Lambda R^T`, with `R^TR=I_3`, the fixed-row Cauchy--Binet identity gives

`P_i=|det Lambda| ||r_i||_2^2`.                               (6.3)

Thus

`||p_Q||_infinity
 <= C_* [ |r_i^T Lambda r_i| |det Lambda| ||r_i||_2^2 ]^(-1/4)`.   (6.4)

Under the exact target normalization `|lambda_1lambda_2lambda_3|>=1`, any row with simultaneously nontrivial spectral leverage and non-negligible physical diagonal is quantitatively controlled. The remaining exact-rank-three obstruction is therefore genuinely the high-leverage **near-isotropic/zero-diagonal** geometry, not overlap of the third square with the residual pair.

This does not contradict the live correction refuting a universal good single Schur extraction from the global hypothesis: (6.2) is a conditional aggregate certificate and can be large when every usable pivot is near isotropic.

## 7. Explicit genuinely rotated indefinite target instance

Let

`u=(sqrt(3)/2,1/2,0)^T`, `v=(0,0,1)^T`,

and

`S=2uu^T-2vv^T
 = [[3/2,sqrt(3)/2,0],
    [sqrt(3)/2,1/2,0],
    [0,0,-2]].`

Its nonzero eigenvalues are `2,-2`, and its spectral row leverages are `3/4,1/4,1`; therefore the old diffuse requirement `max ell_j<=1/2` fails maximally.

Take

`a=2`, `b=(1/10,1/10,1/10)^T`,

and define the four-dimensional physical matrix

`A=[[S+bb^T/2,b],[b^T,2]]`.

All physical diagonal entries are nonzero, the matrix is fully coupled to the pivot, and its Schur complement at the fourth physical coordinate is exactly `S`. Hence `rank(A)=3`.

Compare it with `diag(S,2)`, whose spectrum is `{2,2,0,-2}`. The perturbation

`E=[[bb^T/2,b],[b^T,0]]`

has

`||E|| <= ||b||^2/2+||b|| = 3/200+sqrt(3)/10 <0.189`.

Weyl therefore gives two positive eigenvalues larger than `1.81` and one negative eigenvalue smaller than `-1.81`; this is an exact genuinely rotated indefinite target instance.

Using the heavy-row theorem with the exact leverage `ell=1`, `|a|=2` and `|mu_1mu_2|=4`, equations (2.1)--(3.2) sharpen the generic constant to

`||p_Q||_infinity
 <= 2^(1/4) C_ind /2
 = 9.8345318556...`.                                         (7.1)

This bound holds for every allowed product input law.

## 8. What remains unpaid

The full QFORM conjecture remains OPEN. The current B04 scalar-pivot rank-two overlap problem is paid, but the global three-large-eigenvalue hypothesis need not provide a quantitatively good nonzero scalar pivot, and arbitrary additional spectral components can prevent a rank-two Schur reduction.

The first precise remaining implication is now:

`QFORM-NEAR-ISOTROPIC-HEAVY-ROW-ROUTING-v1` — in the high-leverage branch excluded by the `1/39` spectral-window theorem, either obtain a row with dimension-free lower bound on `|A_ii| P_i` (so (6.2) closes it), or use original-product bank aggregation to control the case where high spectral leverage is concentrated on rows with `A_ii` near zero. The exact-zero pair/cubic-bank theorem of account03/B16 is a compatible endpoint. Arbitrary additional spectral components must remain present rather than being silently discarded.

No full-solution, novelty, continuity, designated-partner-completion, or native-brain-ingestion claim is made.
