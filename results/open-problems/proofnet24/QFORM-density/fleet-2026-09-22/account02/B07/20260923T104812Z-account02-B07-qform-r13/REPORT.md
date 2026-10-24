# account02/B07 r13 — curvature-compatible pair/tail compiler

Programme: QFORM-DENSITY-3EIG-20260922

Status: **ESSENTIAL_STEP_APPLIED / EDGE-E2 COMPILED TO QUANTITATIVE-PAIR HIGH-TAIL OR NEARSINGULAR-PAIR/STRONG-RANK2 / FULL_QFORM_OPEN**.

This is a supporting argument, not a proof or disproof of the unrestricted conjecture.

## First unpaid implication

`QFORM-EDGE-E2-NEARSINGULAR-PAIR-OR-RANK2-TUBE-v1`.

In the physical edge-E2 branch supplied by account03/B07 r30, the still-unpaid configurations can now be restricted to either (i) a quantitatively near-singular physical anchor pair, or (ii) a quantitatively strong rank-two far cross core. The complementary state — a quantitatively invertible physical pair together with nontrivial singular mass beyond rank two — is paid by a new explicit curvature-compatible receiver below. The receiver keeps arbitrary same-bank quadratic curvature, affine terms, outside couplings and extra spectrum. It never rotates the product law and never selects or divides by an individual far minor.

## 1. General pair-log smoothing at an arbitrary positive exponent

Let two ORIGINAL independent cap-one coordinates be the physical pair, with invertible indefinite coefficient matrix `B`. Write

`Delta=|det B|`, `kappa=sigma_min(B)>0`.

After completing the pair, the already-proved physical-pair logarithmic envelope gives, for every `r>0`,

`p_Q(t) <= 2 sqrt(2)/r + Delta^(-1/2) E log_+(2 r^2/(kappa |t-R|))`.   (1.1)

Here `R` is the full Schur-complement random variable in all remaining ORIGINAL coordinates; it may contain arbitrary quadratic and affine terms. The shifts of the two pair coordinates may depend arbitrarily on those remaining coordinates.

Suppose, for some `alpha>0`,

`sup_t P(|R-t|<rho) <= H rho^alpha` for every `rho>0`.                 (1.2)

Then for every `a>0`, layer cake gives

`E log_+(a/|t-R|)`
` = int_0^infinity P(|t-R|<a exp(-v)) dv`
` <= H a^alpha / alpha`.                                             (1.3)

Putting `a=2r^2/kappa` in (1.1),

`p_Q(t) <= A/r + C r^(2alpha)`,

where `A=2 sqrt(2)` and

`C=Delta^(-1/2) H 2^alpha/(alpha kappa^alpha)`.

The minimizing relation is `A=2 alpha C r^(2alpha+1)`. Therefore

`boxed:
 ||p_Q||_infinity
 <= K_alpha H^(1/(2alpha+1))
    Delta^(-1/(2(2alpha+1)))
    kappa^(-alpha/(2alpha+1)),`                                      (1.4)

with

`K_alpha = 2 sqrt(2) * (2alpha+1)/(2alpha)
           * 2^((alpha-1/2)/(2alpha+1)).`                             (1.5)

At `alpha=1/2`, (1.4) is exactly the previously proved square-root-small-ball pair estimate

`4 sqrt(2H) (Delta kappa)^(-1/4)`.

Thus (1.4) is an explicit arbitrary-positive-exponent refinement of the completed pair-log mechanism, not a claim that the physical-pair theorem was previously absent.

## 2. Apply the required pinned e5 determinant-volume theorem after pair completion

Let `S` be the Schur-complement matrix after completing the physical pair. Choose disjoint ORIGINAL-coordinate banks `I,J` among the remaining coordinates and write

`M=S[I,J]`, `L=||M||_F`.

For `k=1`, the completed determinant-volume theorem `D_k` from the required pinned source has

`Z_1=e_1(M^T M)=L^2`.

Its volume marginal is automatically at most one, so the admissible choice `q=2` requires no diffuse-marginal hypothesis. The theorem gives

`|phi_R(t)| <= min(1, B |t|^(-1/4))`,                                (2.1)

where

`B=(pi sqrt(2e))^(1/4) L^(-1/4)`.                                   (2.2)

Apply the same source's fractional-potential Lemma 4.1 with `alpha=1/8`, `b=1/4`. Since

`c_alpha = 2^(1-alpha) Gamma((1-alpha)/2)
           /(2 sqrt(pi) Gamma(alpha/2))`,

the lemma yields

`H_(1/8)(R):=sup_s E|R-s|^(-1/8)
 <= C_1 L^(-1/8)`,                                                   (2.3)

where

`C_1 = 32 c_(1/8) (pi sqrt(2e))^(1/8)
     = 2.777316075398203...`.                                        (2.4)

In particular Markov gives

`sup_s P(|R-s|<rho) <= C_1 L^(-1/8) rho^(1/8)`.                      (2.5)

Substitute `alpha=1/8`, `H=C_1 L^(-1/8)` into (1.4). Since

`K_(1/8)=10*2^(1/5)=11.48698354997035...`,

we obtain the curvature-safe receiver

`boxed:
 ||p_Q||_infinity
 <= C_* Delta^(-2/5) kappa^(-1/10) L^(-1/10),`                       (2.6)

with

`C_* = 10*2^(1/5) C_1^(4/5)
     = 26.00795741955...`.                                           (2.7)

This is the requested real use of a completed result from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`. It is applied after the physical pair has been completed, so the volume currency is genuinely present in the actual Schur remainder. The argument does not reuse a determinant bank that existed only before completion.

### Scope

The pair `B` in (2.6) must be an actual invertible indefinite principal pair of ORIGINAL coordinates. The banks `I,J` are also ORIGINAL-coordinate banks. No orthogonal change of the input coordinates is made. All same-bank quadratic terms stay inside `R`; `D_1` loses them by legitimate decoupling rather than by discarding them. No support, moment, log-concavity or continuity hypothesis is used.

For a definite physical pair, the already-proved ellipse estimate gives

`||p_Q||_infinity <= pi Delta^(-1/2)`                                 (2.8)

for arbitrary ambient remainder, so only the indefinite case needs (2.6).

## 3. A rank-two Schur-loss alternative

Before pair completion, let the far physical cross block between two chosen remaining banks be `D`. Completing a two-coordinate pair changes this block by

`M = D - C_I B^(-1) C_J^T`,                                         (3.1)

and the correction has rank at most two. Let

`T_2(D)=sum_(j>=3) s_j(D)^2`,                                        (3.2)

where `s_1(D)>=s_2(D)>=...` are the singular values. Eckart--Young then gives the deterministic inequality

`L=||M||_F >= dist_F(D, rank<=2)=sqrt(T_2(D))`.                       (3.3)

Thus (2.6) implies

`boxed:
 ||p_Q||_infinity
 <= 26.007958 Delta^(-2/5) kappa^(-1/10) T_2(D)^(-1/20)`              (3.4)

whenever `B` is invertible indefinite and `T_2(D)>0`.

This is deliberately weak in the tail exponent, but it is stable under the worst legitimate rank-two Schur correction and therefore avoids the exact failure found in the previous B07 run.

For a scale-normalized form, put

`R_0=max(||B||_op, ||D||_F)`.

Since for a 2 by 2 invertible matrix `kappa >= Delta/||B||_op >= Delta/R_0`, if

`Delta >= delta R_0^2`, `T_2(D)>=epsilon R_0^2`,                     (3.5)

then

`boxed:
 ||p_Q||_infinity
 <= 26.007958 delta^(-1/2) epsilon^(-1/20) R_0^(-1).`                (3.6)

Indeed the powers of `R_0` cancel exactly:

`Delta^(-2/5) (Delta/R_0)^(-1/10) (epsilon R_0^2)^(-1/20)
 <= delta^(-1/2) epsilon^(-1/20) R_0^(-1)`.

Hence a quantitatively non-singular physical pair fails this new receiver only if the far cross block lies in a quantitative rank-two Frobenius tube.

## 4. Compile the latest designated partner's edge-E2 branch

The latest completed designated partner result available at final source resolution is account03/B07 r30. For its actual physical cross block

`N=[[b,r^T],[c,D]]`, `F=||N||_F`,

it has an anchored third-volume certificate

`G=G_3^(i,a)(N) > gamma F^6`,

`gamma=113246208^(-2)`,                                              (4.1)

and its edge-E2 branch gives

`|b| sqrt(E_2(D)) >= sqrt(G)/2`.                                     (4.2)

Since `|b|<=F`,

`E_2(D) > (gamma/4) F^4`.                                           (4.3)

Let `lambda_j=s_j(D)^2`, `T_2=sum_(j>=3)lambda_j`. Then

`E_2(D)-lambda_1 lambda_2
 = (lambda_1+lambda_2)T_2 + e_2(lambda_3,lambda_4,...)
 <= ||D||_F^2 T_2
 <= F^2 T_2`.                                                        (4.4)

The first inequality follows from `e_2(tail)<=T_2^2/2<=T_2^2`.

Choose `epsilon=gamma/8`. If

`T_2(D) <= (gamma/8)F^2`,                                           (4.5)

then (4.3)--(4.4) force

`boxed:
 s_1(D)s_2(D) > sqrt(gamma/8) F^2.`                                  (4.6)

So the low-tail survivor is not an amorphous near-rank-two state: it contains a quantitatively strong rank-two far core.

Now inspect the actual physical principal pair on the two partner anchors,

`B_anchor=[[A_ii,b],[b,A_aa]]`.

No assertion is made that the edge coefficient `b` alone controls `det B_anchor`; it does not. The branch compiler is therefore:

* If `B_anchor` is definite and quantitatively nonsingular, the ellipse estimate pays it.
* If `B_anchor` is indefinite and quantitatively nonsingular and `T_2(D)` is quantitatively large, (3.6) pays it.
* Otherwise the state is reduced to a quantitatively near-singular physical anchor pair, or to the strong rank-two tube (4.6).

This is the precise gain. It does **not** turn the partner's single edge into a pair determinant, and it does **not** claim the pre-completion `E_2(D)` survives pair completion.

## 5. Regression against the exact Schur-collapse family

The previous B07 run constructed a target-valid no-pivot family with an anchor edge and far block `D` having exactly two nonzero singular values. It has

`|b| sqrt(E_2(D))=1`, `G_3=1`,

but the legitimate pair Schur correction annihilates one rank-one component of `D`, so the post-completion far cross block has rank one and `E_2=0`.

For that family

`T_2(D)=0`.                                                         (5.1)

Therefore the present theorem deliberately routes it to the strong-rank-two low-tail survivor rather than falsely declaring it paid by (3.4). This is the required compatibility with the earlier obstruction.

## 6. Why this is coordinate-minor progress

The new payment uses only the Frobenius `1`-volume of the **post-completion** physical cross block. That quantity is the aggregate

`Z_1(M)=sum_(i in I,j in J) |M_ij|^2`,                               (6.1)

so the determinant/volume weight is retained through conditioning before inversion. No claim is made that one entry of `M` is universally good. The only structural use of singular vectors is the deterministic Eckart--Young distance (3.3), which does not rotate the input probability law.

This also closes the bounded-dimensional spectral subproblem for the high-tail side of a quantitative physical pair: once a fixed pair is quantitatively invertible, **any** positive amount of cross singular mass beyond rank two gives an explicit density bound via a post-Schur aggregate. The residual coordinate-core extraction problem is now concentrated on near-singular physical pairs and genuine rank-two tubes.

## 7. Remaining implication

The sharpened first unpaid implication is

`QFORM-EDGE-E2-NEARSINGULAR-PAIR-OR-RANK2-TUBE-v1`:

starting from the partner r30 edge-E2 reserve and (4.3), pay either

1. a physical anchor pair whose determinant/small singular value is quantitatively tiny relative to the ambient edge-E2 scale, or
2. the strong rank-two far core (4.6),

while retaining arbitrary same-bank curvature and without assuming any pre-Schur determinant bank survives completion.

The partner's projected star-star-core sibling, rank-one core tube, nested-E2 and four-star BICORE routes remain separate obligations. Full QFORM remains open.

## 8. Sources used

Required pinned source, used in the real inequality (2.1)--(2.7):

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`

Specifically Extension `D_k` with `k=1,q=2` and Lemma 4.1.

Physical-pair logarithmic envelope:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`

Latest completed designated partner consumed:

`account03/B07 r30`, source-pinned in the handoff for this run.

## 9. Verification scope

`CHECKS.py` verifies the numerical constants, the deterministic spectral inequality (4.4) on 16,807 integer spectra, the intended placement of the earlier exact Schur-collapse family, and the `epsilon=gamma/8` algebra. `CHECKS.txt` ends in

`QFORM_B07_PAIRTAIL_CHECK_PASS`.

These checks are regression aids only; the mathematical proof is the argument above.
