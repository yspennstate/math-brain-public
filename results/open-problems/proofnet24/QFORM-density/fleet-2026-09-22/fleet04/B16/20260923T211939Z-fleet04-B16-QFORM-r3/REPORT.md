SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B16, 2026-09-23T21:19:39Z.
attacking: near-coloop projection-product split; apply the completed crossing/Fresnel receiver to the innovation-dominant branch and quantify the residual punctured slope collar.

# fleet04/B16 r3 — innovation payment and normalized slope collar

Programme: QFORM-DENSITY-3EIG-20260922
Run: 20260923T211939Z-fleet04-B16-QFORM-r3
Status: ESSENTIAL_STEP_APPLIED / NEW LIVE-BRANCH COMPILER / FULL QFORM OPEN
Continuity: continuous C_0 density on the paid branch; unrestricted continuity remains open.
Execution: WITHOUT_VERIFIED_BRAIN

## 1. Scope and source pins

The target remains the full conjecture for arbitrary independent real cap-one coordinate laws and arbitrary real symmetric matrices with at least three eigenvalues of modulus at least one. No iid, support, moment, sign, exact-rank, smoothness, or post-rotation independence assumption is added to that target.


The following completed inputs are used.

1. fleet01/B16, canonical mathematical commit 178419f09a3e2c7629d4e7ccc203b63a433916a5, report
   proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/20260923T204205Z-fleet01-B16-QFORM-auto11/REPORT.md.
   Its theorem QFORM-TWO-BANK-COUPLED-INNOVATION-GRAM-IDENTITY-v1 supplies the exact identity used at (2.2) below.

2. fleet01/B16, commit b904f281b6c39d431d51a8b5a40d99f07fb57db2, report
   proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/20260923T194021Z-fleet01-B16-QFORM-auto11/REPORT.md.
   Its source-valid crossing/Fresnel theorem, specialized to crossing rank two and same-side Fresnel rank one, gives (3.1).

3. fleet02/B16 r36, commit be8062b160868bcc71aff45a77c56ff2d0501a9a, gives the exact-coloop fresh-hub payment
   ||p_Q||_infinity <= 3*2^(4/3) < 7.56
   on the target witness where every innovation and slope currency vanishes. This is used only to identify the true punctured stability gap; it is not silently extended to a nonzero hub square.

All live corrections are retained: no arbitrary-joint indefinite coarea, no independence after rotation, no worst conditional-density supremum, no uniform scalar pointwise stationary-phase estimate, and no deletion of a small quadratic term multiplying an unbounded input.

## 2. The live balanced near-coloop packet

Use the exact-rank-three Parseval-frame notation of fleet01/B16. A physical hub row is

    r_0 = sqrt(h) e,       h > 63/64,

and the remaining rows are split into disjoint original-coordinate banks J and K. Their transverse Grams satisfy

    (1/4) I_2 <= G_J,G_K <= (3/4) I_2,
    G_J+G_K=I_2.                                             (2.1)

Let delta_J and delta_K be the genuine source innovations after least-squares removal of the two transverse directions in each bank. Let q_J,q_K be the corresponding slopes and put d=q_J-q_K.

The completed fleet01 identity is

    epsilon := 1-h
      = delta_J^2 + delta_K^2 + d^T G_J G_K d.                (2.2)

This is an exact equality, not a heuristic or a lower bound. In particular, every currency in (2.2) may tend to zero at the exact coloop endpoint.

Because G_K=I-G_J, the matrices commute. Under (2.1),

    (3/16) I_2 <= G_JG_K <= (1/4) I_2.                         (2.3)

## 3. New compiler: innovation payment or normalized slope collar

### Theorem QFORM-NEARCOLOOP-INNOVATION-OR-SLOPE-COLLAR-v1

Assume the balanced packet (2.1)-(2.2), and assume one orientation of the exact quadratic phase satisfies the hypotheses of fleet01/B16's completed rank-two-cross/rank-one-Fresnel receiver. Denote its two cross singular values by s_1,s_2 and its scalar same-side curvature coefficient by Gamma != 0.

Then one of the following alternatives holds.

(A) Innovation-dominant payment:

    d^T G_JG_K d <= epsilon/2,                                (3.0)

and the full conditioned quadratic form has a continuous C_0 density satisfying

    ||p_Q||_infinity
      <= (20/3)
         [ |Gamma| (s_1 s_2)^2 epsilon ]^(-1/5).               (3.1)

(B) Slope-dominant collar:

    delta_J^2+delta_K^2 < epsilon/2,                            (3.2)

    epsilon/2 < d^T G_JG_K d <= epsilon,                       (3.3)

and therefore

    2 epsilon < ||d||_2^2 <= (16/3) epsilon.                   (3.4)

The theorem preserves all dependence inside each projected bank. Original-coordinate product structure is used exactly where the completed crossing/Fresnel theorem requires it.

### Proof

The completed fleet01/B16 rank-two-cross/rank-one-Fresnel estimate is

    ||p_Q||_infinity
      <= C_35
         [ |Gamma| (s_1 s_2)^2 delta_B^2 ]^(-1/5),             (3.5)

for either bank B whose source representation meets its row-leverage and diagonal-original-coordinate gates, where

    C_35 = (5/3) 2^(8/5)
         = 5.0523885550346606... .                              (3.6)

Suppose (3.0) holds. Equation (2.2) gives

    delta_J^2+delta_K^2 >= epsilon/2.

Hence at least one bank B satisfies

    delta_B^2 >= epsilon/4.                                    (3.7)

Apply (3.5) on that orientation. Since

    C_35 * 4^(1/5)
      = (5/3) 2^(8/5) 2^(2/5)
      = 20/3,                                                   (3.8)

we obtain (3.1). The L1 characteristic-function majorant in the completed receiver also proves the stated C_0 continuity.

If (3.0) fails, (2.2) immediately gives (3.2)-(3.3). The upper matrix bound in (2.3) and the strict lower bound (3.3) imply

    epsilon/2 < (1/4)||d||_2^2,

so ||d||_2^2>2epsilon. The lower matrix bound in (2.3), together with d^T G_JG_Kd<=epsilon, implies

    (3/16)||d||_2^2 <= epsilon,

which is the upper bound in (3.4). QED.

## 4. Concrete target inequality

Introduce the exact source currency

    Xi := |Gamma| (s_1s_2)^2 (1-h).                             (4.1)

On the innovation-dominant branch, if

    Xi >= 2^(-20),                                              (4.2)

then (3.1) gives the explicit universal bound

    ||p_Q||_infinity
      <= (20/3) (2^(-20))^(-1/5)
      = 320/3
      < 106.667.                                                 (4.3)

This is an actual density inequality on the live original-coordinate phase, including arbitrary same-bank dependence permitted by the completed receiver. It is not a one-sided estimate renamed as a full solution.

More generally, (3.1) pays every collar on which Xi is bounded below. The threshold 2^(-20) in (4.2) is only a convenient displayed gate; the exact scale-sensitive statement is (3.1).

## 5. Interaction with the exact-coloop receiver

At epsilon=0, equation (2.2) forces

    delta_J=delta_K=0,   d=0.                                  (5.1)

Thus neither branch estimate obtained by inverting an innovation can be uniform at the endpoint. This is genuine geometry, not a defect in the constants.

The completed fleet02/B16 fresh-hub theorem separately pays the exact target witness

    Q = 2 X_0 L + V^2

and the larger overlapping family

    Q = 2 X_0 L + V^2 + 2 L T

by

    ||p_Q||_infinity <= 3*2^(4/3) < 7.56,                      (5.2)

when X_0 is the untouched physical hub, (L,V) has its source-valid planar projection cap, and T may depend on the same leaf sources. No independence among L,V,T is asserted.

Equations (3.1)-(3.4) and (5.2) identify the remaining stability problem precisely. After the present compiler, a genuinely unpaid punctured configuration must simultaneously have:

1. a nonzero physical hub-square pivot, so the zero-pivot theorem (5.2) does not directly apply;
2. slope dominance (3.2)-(3.4), rather than innovation dominance;
3. Xi below the chosen paid threshold, if a universal numerical gate such as (4.2) is imposed;
4. overlapping leaf provenance, since the fully source-split punctured model is already paid by the completed disjoint-bank theorem.

The normalized slope cannot wander arbitrarily: its squared magnitude is trapped between 2epsilon and (16/3)epsilon. This is the new quantitative reduction.

## 6. What remains

The full universal density conjecture remains OPEN / NOT PROVED / NOT DISPROVED. The new result closes only the innovation-dominant part of the balanced near-coloop packet at the exact scale (3.1).

The first unpaid B16 implication is now the slope-dominant punctured-hub stability statement:

    0 < |a|D < 2^(-12),
    delta_J^2+delta_K^2 < (1-h)/2,
    2(1-h) < ||q_J-q_K||^2 <= (16/3)(1-h),

with overlapping original leaf sources. A valid receiver must interpolate to (5.2) as a->0 and h->1 without dividing by delta_J, delta_K, d, a, or 1-h individually. Treating the leaf projections as an arbitrary capped joint law is forbidden by the current counterexamples and corrections.

Arbitrary additional spectrum also remains unresolved. Continuity is proved only on the paid crossing/Fresnel branch.
