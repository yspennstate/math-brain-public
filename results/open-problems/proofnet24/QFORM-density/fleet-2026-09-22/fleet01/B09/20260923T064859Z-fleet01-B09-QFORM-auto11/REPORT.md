SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T06:48:59Z.
attacking: a coefficient-exact singular physical-pair endpoint, using Schur-cross minor energy and conditional linear anti-concentration to retain arbitrary outside curvature without a square-root interval loss.

# fleet01/B09 — singular-pair Schur-cross smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture is not claimed solved. This report proves a new exact endpoint for a singular physical `2 x 2` pair, identifies its invariant as a norm of `Az` for a two-sparse null vector of the pair, and applies the newest designated partner fleet02/B09 core-pair extraction to obtain a quantitative target-valid branch. All conditioning is in original independent coordinates. No Gaussianity, moments, compact support, connected support, log-concavity, pointwise van-der-Corput estimate, arbitrary-joint coarea bound, post-rotation independence, worst-fiber density supremum, or perturbative deletion of a small quadratic coefficient is used.

## 1. Setup

Choose two distinct original coordinates, denoted `X` and `Y`, and let `Z=(Z_k)` be the bank of all remaining original coordinates. All are independent and every one-dimensional density is bounded by one. Write the exact quadratic-plus-affine form as

`Q = a X^2 + 2 b X Y + d Y^2
     + 2 X(<u,Z>+alpha) + 2 Y(<v,Z>+beta) + H(Z)`,             (1.1)

where `H` is completely arbitrary measurable for the analytic theorem (and in the quadratic-form application it is the full remaining quadratic-plus-affine term). Let

`E=[[a,b],[b,d]]`.                                              (1.2)

Assume throughout Sections 2--5 that

`det E = ad-b^2 = 0`,                                          (1.3)

and that `E` is not the zero matrix. If `a=0`, then (1.3) forces `b=0` and therefore `d !=0`; swapping `X,Y` reduces to the case `a !=0`. Thus no nonzero singular physical pair is omitted.

Define the Schur-cross vector

`g = a v - b u`,                                                (1.4)

and its squared energy

`Gamma = ||g||_2^2`.                                           (1.5)

The main theorem pays the branch `Gamma>0` directly.

## 2. Two elementary cap-one lemmas

### Lemma 2.1 — one-dimensional half-Riesz cap

If a real random variable `T` has density bounded by `M`, then

`sup_s E |T-s|^(-1/2) <= 2 sqrt(2M)`.                           (2.1)

Proof. By the bathtub/rearrangement principle, among densities `0<=p<=M` of mass one the integral against the radially decreasing kernel `|x-s|^(-1/2)` is maximized by `p=M` on the centered interval of length `1/M`. Hence

`E|T-s|^(-1/2)
 <= M int_{-1/(2M)}^{1/(2M)} |x|^(-1/2) dx
 =2 sqrt(2M)`.                                                  (2.2)

For a scalar cap-one variable `X`, this gives

`sup_s E|X-s|^(-1/2) <=2 sqrt(2)`.                              (2.3)

### Lemma 2.2 — product linear projection

For independent cap-one coordinates `Z_k` and nonzero `w`, the standard one-dimensional product-projection estimate used by the designated partner gives

`||p_<w,Z>||_infinity <= sqrt(2)/||w||_2`.                      (2.4)

This is exactly the marginal estimate used in fleet02/B09 `QFORM-K2-COREPAIR-LINE-EXTRACTION-v1`; it asserts no independence between `<w,Z>` and any other function of the same bank.

## 3. New theorem: singular physical pair plus nonzero Schur-cross energy

### Theorem `QFORM-SINGULAR-PAIR-SCHURCROSS-SMOOTHING-v1`

Under (1.1)--(1.5), suppose `a !=0` and `Gamma>0`. Then the law of `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 2^(11/4) Gamma^(-1/4).`             (3.1)

Consequently, for every interval `I`,

`boxed: P{Q in I} <= 2^(11/4) Gamma^(-1/4) |I|.`               (3.2)

The theorem is uniform over the arbitrary term `H(Z)`. It proves essential boundedness and the linear interval exponent. Continuity is **not** claimed by this proof.

### Proof

Complete the square in the original physical variable `X`:

`Q = a [X+(bY+<u,Z>+alpha)/a]^2 + R`,                           (3.3)

where

`R = (d-b^2/a)Y^2
     +2Y[<v,Z>+beta-(b/a)(<u,Z>+alpha)]
     +H(Z)-(<u,Z>+alpha)^2/a`.                                  (3.4)

The singularity identity `ad-b^2=0` kills the residual `Y^2` coefficient **exactly**. Put

`w=v-(b/a)u`,
`gamma=beta-(b/a)alpha`,
`G(Z)=H(Z)-(<u,Z>+alpha)^2/a`.                                  (3.5)

Then

`R=2Y(<w,Z>+gamma)+G(Z)`.                                       (3.6)

This exact cancellation is the key reason the arbitrary same-bank curvature in `G` is harmless. We do not delete or approximate any coefficient.

Fix `Z=z` and any target `t`. Since `Y` is independent of `Z`, (2.3) and a scalar change of variables give

`E_Y |R-t|^(-1/2)
 = |2(<w,z>+gamma)|^(-1/2)
   E_Y |Y-s(z,t)|^(-1/2)
 <= 2 |<w,z>+gamma|^(-1/2)`.                                   (3.7)

(The null coefficient occurs on a probability-zero set because `w !=0` and `<w,Z>` has a density.) Averaging over `Z`, using (2.4) with

`M <= sqrt(2)/||w||_2`,                                        (3.8)

and then Lemma 2.1 yields

`sup_t E|R-t|^(-1/2)
 <= 2 * 2 sqrt(2M)
 <= 2^(11/4) ||w||_2^(-1/2).`                                  (3.9)

Now condition on `(Y,Z)`. The variable

`a[X+m(Y,Z)]^2`                                                 (3.10)

has conditional density bounded pointwise by

`|a|^(-1/2) |s|^(-1/2)`                                        (3.11)

on its appropriate half-line (and by the same absolute-value expression everywhere). Therefore the conditional mixture (3.3) gives, for almost every `t`,

`p_Q(t) <= |a|^(-1/2) E|R-t|^(-1/2)`.                          (3.12)

Since

`g=a w`,                                                        (3.13)

(3.9)--(3.12) become

`||p_Q||_infinity
 <=2^(11/4) |a|^(-1/2)||w||^(-1/2)
 =2^(11/4)||g||^(-1/2)
 =2^(11/4) Gamma^(-1/4)`,                                      (3.14)

which is (3.1). Integrating over `I` gives (3.2). QED.

### Remarks on the mechanism

1. The proof never converts a square-root small-ball estimate into a final square-root interval estimate. The half-Riesz singularity from the outer square is integrated exactly against a genuine linear-product marginal, so the final interval scale is `O(|I|)`.
2. The arbitrary outside curvature `H(Z)` survives untouched inside `G(Z)` because the conditional linear estimate (3.7) is translation invariant.
3. This is not the refuted same-square absorption shortcut. The second physical square vanishes only because `det E=0` gives the exact Schur identity `d-b^2/a=0`.

## 4. Exact structural identity: the Schur-cross energy is `||Az||^2`

Return to the full symmetric matrix `A`. Let the selected original coordinates be `i,j`, so

`a=A_ii`, `b=A_ij`, `d=A_jj`,
`u=(A_ik)_(k notin{i,j})`,
`v=(A_jk)_(k notin{i,j})`.                                     (4.1)

Define the two-sparse vector

`z = a e_j - b e_i`.                                           (4.2)

Under `ad-b^2=0`, its two selected coordinates are annihilated:

`(Az)_i = a A_ij-b A_ii =0`,
`(Az)_j = a A_jj-b A_ji =ad-b^2=0`.                            (4.3)

For every outside coordinate `k`,

`(Az)_k = a A_kj-b A_ki`.                                      (4.4)

Therefore

`boxed: Gamma = sum_{k notin{i,j}}(a A_jk-b A_ik)^2 = ||Az||_2^2.`  (4.5)

This has a useful exact dichotomy:

- if `Gamma>0`, Theorem (3.1) pays the singular pair;
- if `Gamma=0`, then `z` is a literal nonzero two-sparse kernel vector of `A`.

No near-kernel inference or perturbation is used. Equation (4.5) also makes scaling transparent: under `A -> cA`, `Gamma -> c^4 Gamma`, so `Gamma^(-1/4)` has the correct density scaling `|c|^-1`.

If the nonzero pivot is `d` rather than `a`, swap the pair. The symmetric companion vector `z'=d e_i-b e_j` gives the same theorem with

`Gamma' = sum_{k notin{i,j}}(d A_ik-b A_jk)^2`.                 (4.6)

## 5. Applying the newest designated partner fleet02/B09 to an actual inequality

The newest completed partner is fleet02/B09 run `20260923T061324Z-fleet02-B09-QFORM-auto11`, canonical source

`yspennstate/math-open-problems@c21646b7383471bbdd8f964f798ea4a2b6b67c30`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T061324Z-fleet02-B09-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-K2-COREPAIR-LINE-EXTRACTION-v1` starts from the partner `k=2` physical rank split at scale `eta` and selects physical `i,j` whose two-row map on the active two-plane `F` has

`singular_min >= c_eta := (1-eta)/sqrt(6)`.                    (5.1)

Let `U` be the orthonormal three-frame used in that rank split, chosen from eigenvectors of `A` with eigenvalue magnitudes at least one. For a singular actual physical pair `E=A[{i,j},{i,j}]`, choose a nonzero pivot `a` and `z=a e_j-b e_i` as in (4.2). Since the selected two-row map has (5.1),

`||U^T z||
 >= ||P_F U^T z||
 >= c_eta sqrt(a^2+b^2)`.                                      (5.2)

On the chosen active eigenspace `|lambda|>=1`, hence

`||Az|| >= ||U^T z||`.                                         (5.3)

Combining (4.5), (5.2), and (5.3),

`Gamma^(1/2) >= c_eta sqrt(a^2+b^2)`.                           (5.4)

The new theorem therefore gives the actual partner-paid inequality

`boxed: ||p_Q||_infinity
 <= 2^(11/4) [c_eta sqrt(a^2+b^2)]^(-1/2).`                    (5.5)

This is an application of the partner's completed extraction to the full quadratic form, not merely a citation. It retains all outside quadratic curvature and all signs.

At the partner's concrete `eta=1/16`,

`c_eta = 15/(16 sqrt(6)) =0.3827327723...`.                    (5.6)

Thus, for example, if the selected singular actual pair has

`sqrt(a^2+b^2) >=1/8`,                                         (5.7)

then

`boxed: ||p_Q||_infinity <30.756`.                              (5.8)

For a nonzero rank-one symmetric `E`, one may choose the better of the two pivot orientations. The larger physical row norm is at least `||E||op/sqrt(2)`. Hence the partner branch also has the symmetric corollary

`boxed: ||p_Q||_infinity
 <=2^(11/4)[c_eta ||E||op/sqrt(2)]^(-1/2).`                    (5.9)

At `eta=1/16` and `||E||op>=1/8`, this is

`||p_Q||_infinity <36.576`.                                    (5.10)

These constants are not presented as optimal. The important point is that the exact singular-pair boundary of the partner `k=2` actual-core problem can now be paid by an aggregate Schur-cross norm rather than by reciprocal individual outside coefficients.

## 6. A literal full-target stress example

Consider

`A = [[1,1,0],
      [1,1,2],
      [0,2,1]]`.                                                (6.1)

Its characteristic polynomial is

`(lambda-1)(lambda^2-2lambda-4)`,                               (6.2)

so its eigenvalues are

`1, 1-sqrt(5), 1+sqrt(5)`.                                     (6.3)

All three have modulus at least one. Thus (6.1) is a genuine target matrix, not merely a supporting lower-rank test.

Take the first two physical coordinates. Their principal pair is

`E=[[1,1],[1,1]]`,                                              (6.4)

so `det E=0`, and with the third coordinate as the outside bank,

`u=0`, `v=2`,
`g=a v-bu=2`,
`Gamma=4`.                                                      (6.5)

Theorem (3.1) gives, for **every** admissible independent cap-one input law,

`boxed: ||p_(X^TAX)||_infinity <=2^(9/4)<4.757`,                (6.6)

and therefore

`boxed: P{X^TAX in I} <=2^(9/4)|I|`.                            (6.7)

This example is indefinite and non-diagonal. It exercises exactly the singular-pair plus Schur-cross mechanism.

## 7. What this does and does not close

This report closes the following exact endpoint:

`QFORM-K2-SINGULAR-ACTUALPAIR-SCHURCROSS-v1`:

> in a partner-selected `k=2` physical core pair, if the actual total `2 x 2` principal pair is nonzero singular, then every nonzero Schur-cross minor energy is paid directly by (3.1); the energy is `||Az||^2`, and partner active-frame conditioning converts a quantitative physical pair scale into a universal numerical density bound.

It also identifies the zero-energy endpoint as an **exact two-sparse kernel**, rather than an uncontrolled limiting case.

The first unpaid implication remains the genuinely coupled near-singular/tiny-core branch:

`QFORM-K2-PUNCTURED-NEARSINGULAR-OR-TINYPAIR-ROUTING-v1`:

> handle `0<|det E|<<1` without a logarithmic or reciprocal-minor blowup, and handle the singular case when the actual physical pair scale itself is tiny, by routing the third spectral resource into an already-paid rank-two-cross transverse theorem, pair-log/definite physical-pair theorem, grouped-coordinate smoother, ridge exit, or a product-preserving finite-core descent.

The fleet02/B09 cancellation regression remains mandatory: a favorable *displayed* core component may be canceled by arbitrary same-bank residual curvature, leaving only `2XY`. The present theorem is immune because it is formulated entirely in terms of the **actual total physical pair** and the exact actual matrix invariant `||A(ae_j-be_i)||`.

## 8. Correction ledger consumed

The proof respects the current source corrections: law-uniform pointwise quadratic-phase decay is false; rotations do not preserve independence; arbitrary-joint rank-three coarea is false; positive moments of conditional projection heights can diverge; one single Schur pivot need not expose a rank-two cross block; same-square absorption with arbitrary same-bank curvature is false; and no small matrix term is treated as a small random quadratic error.

Full QFORM remains OPEN. Global continuity remains OPEN. The new endpoint proves essential boundedness and an exact linear interval bound; continuity is not asserted here.
