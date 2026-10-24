SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-23T08:54:00Z.
attacking: translation-uniform hyperbolic-square smoothing: prove C0 continuity and an integrated Fourier L2 estimate, then splice account02/B04's coefficient-projected row-star theorem on one genuinely rotated indefinite target matrix.

# account01/B04 — hyperbolic-square C0/Fourier-L2 upgrade and projected-rowstar splice

**Run:** `20260923T085400Z-account01-B04-QFORM-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** `2026-09-22.15`  
**Assignment:** Product Fourier rearrangement  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` — authenticated repository retrieval occurred, but no native learned-memory receiver/ingestion was verified.

The unrestricted theorem is **not** proved here. The full target and the full-target continuity statement remain open.

## 1. Source-match pivot: do not duplicate the density-cap theorem

The first planned implication was the translation-uniform hyperbolic-square estimate for

`T = 2 a X Y + H(Y) + b (Z+theta(Y))^2`.

A fresh source check found that this exact density-cap theorem is already complete in account02/B10:

- repository: `yspennstate/math-open-problems`
- canonical cited commit: `1eba911614ef9f6683f8eacb5d6608a0f9a4b833`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T1147Z-qform-rank3-coupled-B10-r1/REPORT.md`
- theorem: `QFORM-HYPERBOLIC-SQUARE-v1`.

It proves, for independent cap-one `X,Y,Z`, nonzero real `a,b`, and arbitrary measurable `H,theta`,

`||p_T||_infinity <= 4/sqrt(|ab|)`.

Its ambient physical-triple corollary also retains arbitrary outside couplings. Per owner instruction, this run therefore **stops duplicate work on that exact scope** and changes mechanism. The new step below is a continuity and integrated-Fourier upgrade that is not asserted in the source theorem.

## 2. New theorem: hyperbolic-square C0 and integrated Fourier L2

### Theorem `QFORM-HYPERBOLIC-SQUARE-C0-FOURIER-L2-v1`

Let `X,Y,Z` be independent real random variables with probability densities bounded by one. Let `a,b` be nonzero real numbers and let `H,theta:R->R` be arbitrary measurable functions. Define

`T = 2 a X Y + H(Y) + b (Z+theta(Y))^2`.

Then `T` admits a density `p_T` with a representative in `C_0(R)` and

`||p_T||_infinity <= 4/sqrt(|ab|)`.

With the Fourier convention

`phi_T(t)=E exp(i t T)`, 

one also has the integrated estimate

`int_R |phi_T(t)|^2 dt <= 8 pi / sqrt(|ab|)`,

or equivalently

`||phi_T||_2 <= 2 sqrt(2 pi) |ab|^(-1/4)`.

No pointwise Fourier decay is asserted.

### Proof

The completed B10 theorem already supplies the density construction and the uniform cap. Its proof gives something slightly more precise before the final `Y` integration. For almost every fixed `y != 0`, write

`T_y = 2 a y X + H(y) + b (Z+theta(y))^2`.

The variable `2ayX` has an `L^1` density, and `b(Z+theta(y))^2` has an `L^1` density. Therefore their convolution `p_y` is an `L^1*L^1` convolution and hence lies in `C_0(R)`.

The same two rearrangement inequalities used in B10 give, uniformly in `t`,

`p_y(t) <= sqrt(2/(|ab| |y|))`.

Indeed the square-density envelope contributes `|b|^(-1/2) v_+^(-1/2)` after sign normalization, and the one-sided affine inverse-square-root rearrangement in `X` gives `sqrt(2/(|a y|))`.

This domination is integrable against the law of `Y`: since `f_Y<=1`, the centered inverse-square-root bathtub inequality gives

`int f_Y(y) |y|^(-1/2) dy <= 2 sqrt(2)`.

Thus

`f_Y(y) p_y(t) <= sqrt(2/|ab|) f_Y(y)|y|^(-1/2)`

with a right side integrable in `y` and independent of `t`. Since `p_y(t)` is continuous in `t` for a.e. `y !=0`, dominated convergence proves that

`p_T(t)=int f_Y(y)p_y(t)dy`

is continuous. Since each `p_y(t)->0` as `|t|->infinity`, the same domination gives `p_T(t)->0`. Hence `p_T in C_0(R)`. The B10 estimate gives the same pointwise cap

`||p_T||_infinity <=4/sqrt(|ab|)`.

Finally `p_T` is a probability density, so

`||p_T||_2^2 <= ||p_T||_infinity ||p_T||_1 <=4/sqrt(|ab|)`.

Plancherel for `phi_T(t)=int exp(itx)p_T(x)dx` gives

`int |phi_T(t)|^2 dt = 2 pi int |p_T(x)|^2 dx <=8 pi/sqrt(|ab|)`.

This proves the theorem. `QED`

### Ambient physical-triple corollary

Suppose an arbitrary ambient quadratic form `Q=X^T A X` has three distinct original coordinates `(i,j,k)` such that, after reordering,

`A_ii=0`, `A_ik=0`, `a=A_ij!=0`, `b=A_kk!=0`.

No restriction is imposed on `A_jj,A_jk`, any outside quadratic coefficients, or any outside couplings. Conditioning on all outside original coordinates gives exactly the B10 translated/completed-square form above, with conditional `H,theta`. Every conditional density is in `C_0` and is bounded by the same `4/sqrt(|ab|)`. Dominated convergence over the outside variables therefore gives a global representative in `C_0(R)` with the same bound and the same Fourier-L2 estimate.

This is a continuity upgrade of the existing physical-triple branch, not a global extraction theorem.

## 3. Apply the designated account02/B04 theorem to an actual inequality

The freshest completed designated-partner result read this run is account02/B04's

`QFORM-COEFFICIENT-PROJECTED-ROWSTAR-CLEANBANK-v1`,

source:

- `yspennstate/math-open-problems@c7fbb4f97fef82c9e6920e17bc01fa3efc0da85e`
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260923T071501Z-account02-B04-QFORM-r11/REPORT.md`.

In its exact scope, if the original-coordinate `Y` bank is quadratically clean, `P` is a deterministic orthogonal projection on coefficient space, `N=MP` has exact rank two, and deleting one physical hub row of `N` leaves rank at most one, then

`||p_Q||_infinity <= 2^(3/4) sqrt(pi) E_2(N)^(-1/4)`.

The projection acts only on deterministic coefficient vectors, never on the random coordinates, so product independence is not rotated.

## 4. Genuinely rotated indefinite target matrix: continuous density with cap sqrt(2 pi)

Consider the five original independent coordinates `(x1,x2,x3,y1,y2)` and

`A = [[0,1,0,1,0],
      [1,0,0,0,1],
      [0,0,1,0,1],
      [1,0,0,0,0],
      [0,1,1,0,0]]`.

Thus

`Q = 2 x1 x2 + x3^2 + 2 x1 y1 + 2 x2 y2 + 2 x3 y2`.

This is non-diagonal and indefinite in the original independent coordinates.

### Target validity by exact interlacing

The leading `3x3` physical principal block is

`H = [[0,1,0],[1,0,0],[0,0,1]]`,

with exact eigenvalues `1,1,-1`. If the eigenvalues of the full `5x5` matrix are ordered decreasingly, Cauchy interlacing implies

`lambda_1(A)>=1`, `lambda_2(A)>=1`, and `lambda_5(A)<=-1`.

Hence this matrix satisfies the exact owner hypothesis of at least three eigenvalues of modulus at least one.

### C0 certificate

The coordinates `(x1,x2,x3)` satisfy the ambient triangular-hyperbolic hypotheses with

`a=A_12=1`, `b=A_33=1`, `A_11=A_13=0`.

The new theorem therefore gives a continuous density vanishing at infinity and

`||p_Q||_infinity <=4`.

### Partner row-star certificate on the same matrix

Treat `X_I=(x1,x2,x3)` and `Y_J=(y1,y2)`. The `Y` bank is quadratically clean and the physical cross block is

`M = [[1,0],[0,1],[0,1]]`.

Take the partner coefficient projection `P=I`. Then `N=M` has exact rank two, and deleting its first row leaves

`[[0,1],[0,1]]`,

which has rank one. Moreover

`N^T N = diag(1,2)`,

so

`E_2(N)=det(N^T N)=2`.

The account02/B04 theorem therefore gives the actual inequality

`||p_Q||_infinity <= 2^(3/4) sqrt(pi) 2^(-1/4) = sqrt(2 pi)`

`= 2.5066282746310002...`.

The C0 density from the first certificate is a version of the same law. Since it agrees almost everywhere with the partner-bounded density, continuity upgrades the partner essential bound to the pointwise bound

`sup_t p_Q(t) <= sqrt(2 pi)`.

Consequently the same genuinely rotated indefinite target matrix has

`p_Q in C_0(R)`,

`sup p_Q <= sqrt(2 pi) =2.5066282746310002...`,

and, by Plancherel,

`int |phi_Q(t)|^2 dt <= 2 pi sqrt(2 pi)`

`=15.749609945722417...`,

so

`||phi_Q||_2 <=3.9685778240728022...`.

This is a concrete product-Fourier estimate on a true target-valid rotated/indefinite form, not a pointwise stationary-phase estimate.

## 5. General dual-certificate synthesis

Whenever the **same** ambient form simultaneously admits

1. a B10 triangular-hyperbolic-square physical triple with coefficients `a,b`, and
2. an account02/B04 quadratically-clean-bank projected row-star certificate with cross projection `N`,

then the law has a representative in `C_0(R)` and

`||p_Q||_infinity <= min{ 4/sqrt(|ab|), 2^(3/4)sqrt(pi) E_2(N)^(-1/4) }`.

Therefore

`int |phi_Q(t)|^2 dt <= 2 pi * min{ 4/sqrt(|ab|), 2^(3/4)sqrt(pi) E_2(N)^(-1/4) }`.

The two certificates play distinct roles: the hyperbolic-square route supplies translation-uniform C0 regularity under arbitrary outside couplings, while the projected row-star route can supply the sharper L-infinity constant without rotating the random product law.

## 6. What remains unpaid

This does **not** show that the bare condition `s_3(A)>=1` forces either certificate. Current corrections explicitly rule out several tempting local-extraction shortcuts.

The next structural implication is therefore

`QFORM-C0-CERTIFICATE-ROUTING-v1`:

from only the full three-large-eigenvalue hypothesis, either force a target-scale product-preserving C0-producing channel (triangular hyperbolic-square, ridge/Fourier-L1, or another completed branch), or couple a sharper projected-rowstar / grouped-bank L-infinity certificate to such a continuity channel without selecting a reciprocal tiny local minor.

The zero/near-zero outer physical-pivot and arbitrary two-sided-curvature survivors remain genuine debt.

## 7. Integrity / corrections

No Gaussianity, log-concavity, moments, compact support, connected support, or diagonal-basis independence is used. No random-coordinate rotation is performed. No law-uniform pointwise van-der-Corput/Fresnel decay is used. No arbitrary-joint coarea lemma, conditional projection-density moment, fiber supremum, universal local cross-rank-three cut, or single-Schur-rank-two extraction is assumed. The source-matching theorem was recorded instead of being renamed as new work.

**Final mathematical status:** supporting theorem proved; explicit target-valid application proved; full QFORM density conjecture **OPEN**; full-target continuity **OPEN**.
