SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T09:16:13Z.
attacking: spectral-window complementary Schur shielding for arbitrary extra signed spectrum, allowing an arbitrary singular/unbounded complementary tail and charging only its coupling leakage.

# account03/B12 — spectral-window complementary Schur shield with arbitrary complementary spectrum

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T091613Z-qform-eigenvalue-r29`  
Assignment: additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**  
Continuity: **not claimed by the new shield branch**; only essential boundedness is compiled there.

## 1. Scope and sources

The full target remains: for every dimension, every independent real product law with one-dimensional densities bounded by one, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal essential density bound for `X^T A X`, or give a valid counterexample. No moments, Gaussianity, compact support, connected support, log-concavity, or independence after spectral rotation are introduced below.


The designated partner result actually used at an equation is account04/B12:

`yspennstate/math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T081758Z-account04-B12-complementary-schur-shield-r4/REPORT.md`.

Its completed complementary-Schur theorem is used in Section 3 below.

The newest Claude-derived source actually used in this run is:

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`

(current package commit `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`). Its near-diffuse three-volume bound is applied in Section 7. The bounded-dimensional physical receiver used below is Corollary 4.1 of the Claude synthesis `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`: on `m` original independent coordinates, three eigenvalues of modulus at least `sigma` imply density at most `2 sqrt(6 pi m)/sigma`, uniformly in affine terms.

## 2. The new deterministic geometry

Let `I` be an ACTUAL original-coordinate principal block of size `m`. Inside this finite matrix only, choose an orthogonal decomposition

`R^m = W direct_sum Z`.

This is deterministic matrix algebra; the random coordinates are never rotated. Write the principal block as

`H = [[C, B], [B^T, D]]`,

with `C=C^T`, `D=D^T`. Let `P` be any orthogonal projection on `Z` that commutes with `D`; put `Q=I-P`. In the reducing decomposition `Z=PZ direct_sum QZ`, write

`D = D_P direct_sum D_Q`,

`B = (B_P, B_Q)`.

Assume only:

1. `rank(P)>=3`;
2. every singular value of `D_P` is at least `mu>0`;
3. no hypothesis at all on `C` or `D_Q`.

Define

`rho = ||B_P D_P^{-1}||_op`,

`epsilon = ||B_Q||_op`,

`ell(rho) = (sqrt(rho^2+4)-rho)/2`.

The quantity `D_Q` may be singular, may have any signs, and may contain arbitrarily large positive and negative eigenvalues.

## 3. Main theorem — `QFORM-SPECTRAL-WINDOW-COMPLEMENTARY-SHIELD-v1`

Under the hypotheses above,

`boxed: s_3(H) >= ell(rho)^2 mu - epsilon.`                    (3.1)

More generally, if `T=T^T` is any ambient symmetric perturbation whose compression to the actual physical block obeys

`||T[I,I]||_op <= delta`,

then

`boxed: s_3(H+T[I,I]) >= ell(rho)^2 mu - epsilon - delta.`    (3.2)

Whenever

`gamma := ell(rho)^2 mu - epsilon - delta > 0`,              (3.3)

the full ambient quadratic form, with arbitrary coefficients and couplings outside `I`, satisfies

`boxed: ||p_(X^T A X)||_infinity <= 2 sqrt(6 pi m)/gamma.`    (3.4)

All input laws remain arbitrary independent probability densities bounded by one. No continuity conclusion is asserted from this receiver.

### Proof

Set `B_Q=0` temporarily. Then, after the deterministic orthogonal basis change inside the finite matrix, the resulting matrix is the direct sum

`H_0 = H_active direct_sum D_Q`,

where

`H_active = [[C, B_P], [B_P^T, D_P]].`

Apply account04/B12's completed complementary-Schur shield to `H_active`. Its theorem allows the active Schur block/top-left block to be completely arbitrary and gives

`s_3(H_active) >= ell(rho)^2 mu.`                              (3.5)

Because `H_0` is a direct sum, its singular values are the union of the singular values of `H_active` and `D_Q`. In particular the three singular values supplied by (3.5) remain present regardless of every eigenvalue of `D_Q`, so

`s_3(H_0) >= ell(rho)^2 mu.`                                  (3.6)

Now restore the omitted coupling to the unprotected complementary modes. The difference is

`E = [[0, 0, B_Q], [0, 0, 0], [B_Q^T, 0, 0]]`                (3.7)

in the `W direct_sum PZ direct_sum QZ` decomposition. The nonzero eigenvalues of this symmetric off-diagonal matrix are `+s_j(B_Q)` and `-s_j(B_Q)`, hence

`||E||_op = ||B_Q||_op = epsilon.`                            (3.8)

Weyl's singular-value perturbation inequality applied to `H=H_0+E` yields (3.1). Applying it once more to the local compression `T[I,I]` yields (3.2).

Because the final actual ORIGINAL-coordinate principal block has at least three eigenvalues of modulus at least `gamma`, condition on all original coordinates outside `I`. They remain independent inside `I`; outside values create only deterministic affine and constant terms. The bounded-dimensional physical receiver gives (3.4), uniformly in the conditioning. Averaging finishes the proof. QED.

## 4. Spectral-window form: the smaller/larger eigenvalues are retained exactly

A useful canonical choice is the spectral projection

`P_mu = 1_{|D|>=mu}`.

If `rank(P_mu)>=3`, then every singular value of `D_P` is at least `mu`. Thus

`rho_mu = ||B P_mu (D|_{P_mu Z})^{-1}||_op`,

`epsilon_mu = ||B (I-P_mu)||_op`,

and

`boxed: s_3(H) >= mu ell(rho_mu)^2 - epsilon_mu.`              (4.1)

The cruder but sometimes convenient bound

`rho_mu <= ||B P_mu||_op/mu`

gives

`boxed: s_3(H) >= mu ell(||B P_mu||_op/mu)^2 - ||B(I-P_mu)||_op.`  (4.2)

This is a true matrix-level stability theorem for additional eigenvalues:

- every eigenvalue of `D_Q`, smaller OR larger than the protected three, of either sign, is kept in the final matrix and costs **zero directly**;
- arbitrary signed changes inside `C` cost **zero**;
- the only charge for the unprotected complementary sector is the actual coupling leakage `||B_Q||_op`;
- a dense ambient perturbation costs only its LOCAL compression `||T[I,I]||_op`;
- all spectrum and couplings completely outside `I` cost zero.

No statement is made that the random quadratic term corresponding to a small matrix is small. Everything is paid through deterministic singular-value geometry before the probabilistic receiver is invoked.

An optimized certificate is therefore

`Gamma(H;W) = sup_{mu>0, rank(P_mu)>=3}`

`    [mu ell(rho_mu)^2 - ||B(I-P_mu)||_op]_+`.                (4.3)

Whenever this is positive on a bounded-size physical block, the QFORM density is bounded by the corresponding physical-fiber constant.

## 5. Why this strictly extends the partner's invertible-complement shield

The partner theorem requires the chosen complementary block `D` itself to be invertible. The new theorem permits `D_Q` to contain exact zero modes, arbitrarily many very small eigenvalues, and arbitrary additional large eigenvalues. Only the selected reducing spectral packet `D_P` is inverted.

This matters exactly for the B12 assignment: an arbitrary extra signed spectrum can be left in the complementary tail instead of being folded into an alleged independent convolution. The protected packet supplies the three substantial singular values; the rest of the spectrum is present throughout the proof.

## 6. Concrete exact-target inequality

Take a seven-coordinate physical block and, for deterministic matrix algebra, use dimensions

`dim W=2`, `dim PZ=3`, `dim QZ=2`.

Let

`D_P = diag(2,-2,2)`,

`B_P = [[1,0,0],[0,1,0]]`,

so `mu=2`, `rho=1/2`, and

`ell(1/2)^2 = (9-sqrt(17))/8 = 0.6096117967977924...`.

Let `C` be ANY real symmetric `2x2` matrix, with arbitrarily large positive/negative eigenvalues. Let `D_Q` be ANY real symmetric `2x2` matrix, also with arbitrary signs and arbitrarily large or zero eigenvalues. Let `B_Q` be arbitrary subject only to

`||B_Q||_op <= 1/10`,

and let an additional ambient symmetric matrix `T` satisfy only

`||T[I,I]||_op <= 1/10`.

Then

`gamma >= 2(9-sqrt(17))/8 - 1/10 - 1/10`

`      = 1.019223593595585... > 1.`                            (6.1)

Thus the exact original target spectral condition holds through this physical block for every such `C,D_Q,B_Q,T`, and

`boxed: ||p_Q||_infinity <= 2 sqrt(42 pi)/gamma`

`                         = 22.540321632646464... .`          (6.2)

All further original coordinates, their self-block, their cross-couplings to these seven coordinates, and their eigenvalues are unrestricted.

## 7. Required application of the newest Claude volume result

The newest Claude-derived volume-stability theorem is not needed to prove (3.1), but it gives a second, dimension-free exit that can be combined with this shield without circularity.

If the same final ambient matrix has any disjoint ORIGINAL-coordinate cross block `M=A[J,K]` satisfying

`M=M0+E`, `s3(M0)>=a`,

`max_i (P_range(M0))_ii <=1/2`, `||E||_op<=a/16`,             (7.1)

then the current volume theorem gives directly

`boxed: ||p_Q||_infinity <= (24 sqrt(3)e)/(5a) < 23/a`,       (7.2)

with a continuous `C_0` density. All self blocks and outside couplings are arbitrary in that result.

Therefore a full structural reduction may now discard two distinct paid classes:

1. a bounded physical block with positive window certificate (4.3), paid by (3.4);
2. a near-diffuse actual cross block satisfying (7.1), paid by (7.2).

The genuinely unpaid B12 geometry must fail both mechanisms: no positive bounded-window Schur shield and no admissible near-diffuse three-volume cut. This is an actual mathematical narrowing of the remaining case, not a copied source citation.

## 8. Finite deterministic checks

`CHECK.py` tests 5,000 random block matrices with arbitrary large/small top and complementary spectra, exact protected packets, and leakage scaled to a prescribed operator norm. It verifies the deterministic inequality

`s3(H) >= ell(rho)^2 mu - ||B_Q||op`

with zero violations. The smallest observed margin was `0.6094614119088269`; the symmetric leakage block had operator norm exactly `||B_Q||op` to floating-point precision. The explicit example constants in Section 6 were independently recomputed. These are only sanity checks; the proof is the algebra above.

## 9. Remaining gap

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.** The bare condition `s3(A)>=1` has not been shown to force a bounded-size physical block for which the optimized spectral-window certificate (4.3) is positive, nor to force the newest cross-volume gate. Diffuse no-pivot matrices can spread the protected spectrum and the hostile coupling over many coordinates.

The next useful B12 step is therefore structural: starting from N3/no-pivot data, prove that either one can choose a bounded original-coordinate block and algebraic decomposition with small unprotected coupling leakage, or an actual original-coordinate cross cut enters the three-volume/ridge/grouped-bank exits. The theorem above removes invertibility of the entire complementary sector as an obstacle; only leakage into the unprotected sector remains.

Independent review status: none yet. Continuity: proved only in the separate newest-Claude volume branch (7.2), not by the spectral-window Schur shield itself.
