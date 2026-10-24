SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T02:58:43Z.
attacking: apply the new fractional three-volume estimate with every marginal gate retained, then close the r17 span-aligned square/rank-two packet away from one exact Schur resonance.

# account03/B02 QFORM r18 — square-transfer of fractional-volume bounds and nonresonant span-aligned closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T025843Z-account03-B02-qform-r18`  
**Assignment:** Integrated Fourier estimate  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository access is not native learned-memory ingestion.  
**Full target:** OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** tracked separately; the new square-transfer and rank-two-potential branches below prove essential boundedness, not continuity of the final output.

## 1. Exact target and current proof obligation

The owner target remains: for every finite `n`, every vector `X=(X_1,...,X_n)` of independent real variables with probability densities `0<=f_i<=1`, and every real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one universal essential-supremum bound, or give a valid target-class counterexample. No moment, Gaussian, log-concavity, compact-support, connected-support, identical-law, or post-rotation-independence hypothesis is introduced.

The preceding B02 run, `math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`, proved an exact-rank-three physical cross-block Fourier theorem and thereby closed every *transverse* two-sided rank-two packet. Its only packet residue was

`alpha in Col(B), beta in Row(B)`

for

`Q=d z^2+2z(alpha^T x+beta^T y+c)+F(x)+G(y)+2x^T B y`,

where `rank(B)=2`. This run attacks that residue and also implements the newest owner-required fractional-volume source rather than merely citing it.

## 2. Newest source actually applied, with every gate retained

The required newest source is

- `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
- `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`,
- and its `PEER_TAIL_EXTENSION.md`.

Its fractional three-volume theorem states: for a physical original-coordinate cross block `M`, let

`Z_3=e_3(M^T M)>0`,

let `alpha_i` be the row three-volume inclusion marginals, and assume

`1<=q<3/2`, `alpha_i<=q/2` for every row.

Then, with arbitrary self-block phases, arbitrary outside couplings, and affine terms,

`||p_R||_infinity <= H_q := [3e/((3-2q)sqrt(q))] Z_3^(-1/6)`,          (2.1)

and `R` has a continuous density. The marginal gate is part of the hypothesis and is not discarded.

The same source proves two concrete admissibility certificates:

1. If `M=M0+E`, `s3(M0)>=a>0`, `max diag(P_range(M0))<=1/2`, and `||E||op<=a/16`, then

`||p_R||_infinity <= (24 sqrt(3)e)/(5a) < 23/a`.                      (2.2)

2. With an orthogonal row-space projection `P`, `max diag(P)<=1/2`, `T2=sum_{j>=3}s_j(M)^2`, and

`||(I-P)M||op <= sqrt(T2)/15`,

one has

`||p_R||_infinity <= (9 sqrt(3)e/2)[s1(M)^2 s2(M)^2 T2]^(-1/6)`.      (2.3)

These are supporting exits, not consequences of the bare three-eigenvalue hypothesis.

## 3. A general square-transfer lemma

### Lemma 3.1 — bounded residual density plus one genuine physical square

Let `Z` be one original coordinate, independent of the remaining original-coordinate vector `W`, with density bounded by one. Let `d!=0`, let `eta(W)` be arbitrary measurable, and let `R(W)` be any real random variable having a probability density `r` with

`||r||_infinity<=H`.

Define

`Q=d(Z+eta(W))^2+R(W)`.

Then `Q` has an essentially bounded density and

`boxed(||p_Q||_infinity <= 4 |d|^(-1/2) H^(1/2)).`                    (3.1)

No independence between `eta(W)` and `R(W)` is assumed.

### Proof

Condition on `W=w`. The conditional density of `d(Z+eta(w))^2` is bounded by

`|d|^(-1/2)|u|^(-1/2)`

on the appropriate sign half-line. Hence, for almost every `y`,

`p_Q(y) <= |d|^(-1/2) E |y-R|^(-1/2)`
`       =  |d|^(-1/2) int r(s)|y-s|^(-1/2) ds`.                       (3.2)

For any radius `rho>0`, split the last integral into `|y-s|<=rho` and its complement. Since `r<=H` and has mass one,

`int r(s)|y-s|^(-1/2) ds <= 4H sqrt(rho)+rho^(-1/2)`.                 (3.3)

The optimizer is `rho=(4H)^(-1)`, at which both contributions sum to `4sqrt(H)`. This proves (3.1). QED.

This elementary transfer is useful here because it preserves the original physical coordinate `Z`; it does not rotate or condition the input law into dependent spectral coordinates.

## 4. Actual application of the newest fractional-volume theorem

Suppose a nonzero physical pivot has been completed as

`Q=d(Z+eta(W))^2+R(W)`,

and the Schur remainder `R` contains a disjoint original-coordinate cross block `M` satisfying the fractional-volume hypotheses in Section 2. Applying (2.1) at the equation level inside Lemma 3.1 gives

`boxed(
 ||p_Q||_infinity
 <= 4 [3e/((3-2q)sqrt(q))]^(1/2)
      |d|^(-1/2) Z_3^(-1/12).
)`                                                                  (4.1)

Every row-marginal gate `alpha_i<=q/2` is retained. No small random-quadratic perturbation is inferred from an operator-norm statement.

At the concrete `q=4/3` gate,

`H_{4/3}=(9sqrt(3)e/2) Z_3^(-1/6)`,

so

`||p_Q||_infinity
 <=18.411697 |d|^(-1/2) Z_3^(-1/12)`.                               (4.2)

Using the near-diffuse stability certificate (2.2) instead gives the explicit new square-Schur exit

`boxed(
 ||p_Q||_infinity
 <=4 sqrt(24sqrt(3)e/5) (|d|a)^(-1/2)
 <19.015519 (|d|a)^(-1/2).
)`                                                                  (4.3)

Using the collective-tail certificate (2.3) gives

`boxed(
 ||p_Q||_infinity
 <=18.411697 |d|^(-1/2)
   [s1(M)^2 s2(M)^2 T2]^(-1/12),
)`                                                                  (4.4)

under exactly the projection and residual-operator gate stated above.

Equations (4.1)--(4.4) are the required application of the newest fractional-volume result to an actual new implication. The source theorem itself gives continuity for `R`; Lemma 3.1 only proves essential boundedness for the correlated shifted-square output `Q`, so continuity is **not** promoted automatically.

## 5. Exact-rank-two physical cross block: unconditional integrated estimate

The r17 bilinear-Plancherel argument at rank three has a useful rank-two endpoint that does not require the fractional-volume marginal gate.

### Lemma 5.1 — exact-rank-two cross Fourier envelope

Let `R` be any quadratic-plus-affine form of independent original-coordinate variables. Suppose disjoint original-coordinate banks `I,J` have physical cross block `C` of exact rank two. Let its two nonzero singular values be `s1,s2` and put

`Delta_C=s1 s2>0`.

Then

`|phi_R(t)| <= min(1,2pi Delta_C^(-1/2)|t|^(-1))`.                   (5.1)

Consequently

`int_R |phi_R(t)|^(3/2) dt <=12pi Delta_C^(-1/2)`,                   (5.2)

and `R` has an `L^3` density satisfying

`boxed(||p_R||_3 <= 6^(2/3) Delta_C^(-1/3)).`                        (5.3)

### Proof

Condition on every original coordinate outside `I union J`. Write a thin SVD

`C=U Sigma V^T`, `Sigma=diag(s1,s2)`.

Project the two complex bank amplitudes onto `range(U)` and `range(V)`. Their absolute values are bounded by the corresponding positive two-dimensional marginals of the original product laws. The Livshyts--Paouris--Pivovarov product-marginal theorem used in r17 gives cap at most `2^(2/2)=2` for each such marginal. Since each marginal has mass one, each complex projected amplitude has `L^2` norm at most `sqrt(2)`, so the product of the two `L^2` norms is at most `2`.

Bilinear Plancherel with phase `exp(2it u^T Sigma v)` then gives

`|phi_{R|outside}(t)|
 <= pi |t|^(-1) Delta_C^(-1/2) * 2`,

which is (5.1) after averaging over the outside variables and using `|phi_R|<=1`.

If `A0=2pi Delta_C^(-1/2)`, direct integration gives

`int min(1,A0/|t|)^(3/2)dt=6A0=12pi Delta_C^(-1/2)`,

proving (5.2). Inverse Hausdorff--Young, with this Fourier normalization, yields

`||p_R||_3 <=(2pi)^(-2/3)||phi_R||_(3/2)
            <=(2pi)^(-2/3)(12pi Delta_C^(-1/2))^(2/3)
            =6^(2/3)Delta_C^(-1/3)`,

which is (5.3). QED.

No law-uniform one-dimensional pointwise quadratic-phase estimate is used. The pointwise estimate (5.1) comes from a two-bank bilinear Plancherel calculation plus a source-valid product-marginal theorem.

## 6. Square plus an exact-rank-two Schur cross block

Combine Lemma 5.1 with the half-Riesz potential estimate already proved in the predecessor B02 work:

for every probability density `r` with `||r||_3<=L`,

`sup_y int r(s)|y-s|^(-1/2)ds <=4(4L/3)^(3/4)`.                     (6.1)

Taking `L=6^(2/3)Delta_C^(-1/3)` from (5.3) in the physical-square inequality (3.2) gives

`boxed(
 ||p_Q||_infinity
 <=16*3^(-1/4)|d|^(-1/2)Delta_C^(-1/4)
 <12.157371 |d|^(-1/2)Delta_C^(-1/4).
)`                                                                  (6.2)

This is `QFORM-SQUARE-RANK2-EXACTCROSS-v1`.

It removes the leverage gate from the earlier rank-two square-pivot determinant route when the Schur cross block itself has exact rank two. It proves essential boundedness. It does **not** by itself imply `phi_Q in L^1`, so continuity of the final `Q` is not claimed.

## 7. Main application: close the r17 span-aligned packet off exact resonance

Return to

`Q=d z^2+2z(alpha^T x+beta^T y+c)+F(x)+G(y)+2x^T B y`,              (7.1)

where `z`, the `x` bank, and the `y` bank are disjoint sets of original independent coordinates, `d!=0`, `rank(B)=2`, and

`alpha in Col(B)`, `beta in Row(B)`.                                  (7.2)

Let the thin SVD be

`B=U Sigma V^T`, `Sigma=diag(sigma1,sigma2)`,

write

`alpha=Ua`, `beta=Vb`,

and define the scalar

`theta := b^T Sigma^(-1)a = beta^T B^+ alpha`.                       (7.3)

Also put

`Delta_B=sigma1 sigma2`.

Complete the genuine physical `z` square:

`Q=d[z+(alpha^T x+beta^T y+c)/d]^2 + R(x,y)`,                         (7.4)

where all same-bank and affine terms are absorbed into `R`, and the new `x-y` cross block is

`C=B-alpha beta^T/d
  =U[ Sigma-a b^T/d ]V^T`.                                            (7.5)

The two-by-two matrix determinant lemma gives

`det(Sigma-a b^T/d)
 =det(Sigma)[1-b^T Sigma^(-1)a/d]
 =Delta_B(1-theta/d)`.                                                (7.6)

A rank-one perturbation of the invertible two-by-two `Sigma` has rank at least one. Therefore

- if `d!=theta`, then `C` has exact rank two and

`Delta_C=Delta_B |1-theta/d|
        =Delta_B |d-theta|/|d|`;                                     (7.7)

- if `d=theta`, then `C` has exact rank one.

Applying (6.2) in the nonresonant case gives the explicit closure

`boxed(
 ||p_Q||_infinity
 <=16*3^(-1/4)
    [Delta_B |d(d-theta)|]^(-1/4).
)`                                                                  (7.8)

This is `QFORM-SPAN-ALIGNED-NONRESONANT-v1`.

Thus the entire r17 span-aligned two-sided packet is now reduced to the **single exact scalar resonance**

`boxed(d=theta=beta^T B^+ alpha)`,                                   (7.9)

rather than the former two vector-span conditions. At resonance, the Schur `x-y` cross block has exact rank one; the third curvature must come from the same-bank/hub/tail geometry and cannot be manufactured by a random-variable shear without losing product provenance.

The full QFORM theorem does not automatically supply a dimension-free lower bound on `|d-theta|`; therefore (7.8) is a genuine supporting closure, not a complete structural reduction from the bare three-eigenvalue hypothesis.

## 8. Designated partner account04/B02 actually applied

The completed designated partner theorem is

- `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`,
- theorem `QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`.

It proves that if a quadratic form in independent original coordinates contains a nonsingular physical principal `3x3` block `D` with a zero diagonal entry, then

`||p||_infinity <=3*2^(2/3)|det D|^(-1/3)`,                          (8.1)

with a continuous density.

Apply this theorem not to the final `Q`, but to the Schur remainder `R(W)` after completing a nonzero genuine physical pivot. If the Schur matrix of `R` has such a physical block `D`, then (8.1) gives

`H=3*2^(2/3)|det D|^(-1/3)`.

Insert this exact partner inequality into Lemma 3.1. The result is the new partner-assisted square inequality

`boxed(
 ||p_Q||_infinity
 <=4 sqrt(3) 2^(1/3)
    |d|^(-1/2)|det D|^(-1/6)
 <8.728990 |d|^(-1/2)|det D|^(-1/6).
)`                                                                  (8.2)

This is an equation-level application of the designated partner result. It can close resonant cases when the rank-one cross remainder still contains a qualifying zero-diagonal triple elsewhere. The partner theorem gives continuity for `R`; the correlated square transfer (3.2) is used only to conclude essential boundedness for the full `Q`, so continuity is not claimed in (8.2).

## 9. Integrated-Fourier status

This run does **not** prove or refute a universal target-wide bound on

`int |E exp(it X^T A X)| dt`.

No target-valid counterexample to that stronger criterion was found. The exact-rank-two Schur remainder has the source-valid integrated estimate (5.2), and the newest fractional-volume branches have full `L^1` Fourier inversion at the residual level, but the completed physical square is shifted by the same variables that determine the remainder. A residual `L^1_t` estimate cannot simply be multiplied by an independent square factor. The density-potential transfer avoids that false independence step.

Therefore the stronger global `L^1_t` criterion remains open, while the bounded-density target has advanced on the stated branches.

## 10. Correction safety and exact remaining debt

This proof uses none of the live refuted interfaces:

- no law-uniform pointwise quadratic-phase van der Corput bound;
- no independence after spectral rotation;
- no arbitrary-joint rank-three coarea lemma;
- no positive moment of a worst conditional projection-density cap;
- no fixed uniformly good physical minor;
- no universal rank-three coordinate cross cut;
- no conversion of a small matrix operator norm into a small random quadratic perturbation on unbounded inputs.

All product-marginal and fractional-volume gates are stated explicitly. The full conjecture remains OPEN.

The first unpaid B02 implication is now sharply localized:

**Resonant span-aligned branch.** In (7.1)--(7.2), assume

`d=beta^T B^+ alpha`,

so the completed-square Schur cross block has exact rank one. If neither the newest fractional-volume/tail certificate nor the partner zero-diagonal residual certificate is available, exploit the remaining same-bank curvature/hub structure while preserving original-coordinate product provenance. A promising next mechanism is to combine the rank-one Schur packet with the completed exact-null scalar/dependent-pair kernel or a near-null interpolation, rather than retry the false Gabor-line restriction bound.

This is strictly smaller than the r17 residue.

## 11. Deterministic regression

`check_r18.py` tests the exact identity (7.7) on 100 seeded random rank-two matrices and evaluates the displayed constants. The recorded output is `CHECK_RESULTS.txt`:

`max_scaled_rank2_schur_error=1.543159425957068847e-15`,

`rank2_square_constant=12.157370970425481`,

`fractional_q_4_3_square_constant=18.411696309822325`,

`near_diffuse_square_constant=19.015518182232114`,

`partner_residual_square_constant=8.728989087773771`,

`STATUS=PASS`.

The numerical check is regression evidence only; the matrix determinant and analytic inequalities are proved above.

## 12. Review and completion status

The newest fractional-volume source is marked by its authors as a complete supporting argument with independent review pending; this report consumes its stated scope and does not upgrade its review status. The exact-rank-two algebra and square-transfer arguments in this report have not received an independent end-to-end worker review. Therefore this is a supporting result, not a full-candidate proof.

The full target and full-target continuity remain OPEN.
