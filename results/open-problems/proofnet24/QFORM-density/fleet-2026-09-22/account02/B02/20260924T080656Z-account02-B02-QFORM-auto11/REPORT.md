SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-24T08:06:56Z.
attacking: QFORM-R47-STRONGHUB-TWOSIDED-CURVATURE-OR-DIFFUSE-E2-L1-v1; test the genuine two-sided-curvature endpoint before forcing another E3/E5 extraction, then spend the third physical smoothing direction through a fractional-potential receiver if local unweighted Fourier L1 is false.

# account02/B02 — two-sided 2x2 Fourier criticality, a 4D half-Riesz receiver, and a scalar-pivot compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T080656Z-account02-B02-QFORM-auto11`  
Role: Integrated Fourier estimate / complementary constructions and source-valid counterexamples  
Status: **NEW SUPPORTING HALF-POTENTIAL/DENSITY THEOREM + EXACT LOCAL FOURIER-L1 OBSTRUCTION / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Execution context: `VERIFIED_BRAIN` (authenticated repository retrieval plus actual use of the preceding B02 receiver-memory snapshot; no native learned-memory ingestion is claimed).

The exact owner target is unchanged: arbitrary independent ORIGINAL real inputs with one-dimensional probability densities at most one; arbitrary real symmetric `A`; at least three eigenvalues of modulus at least one. No moments, compact/connected support, log-concavity, iid assumption, diagonal-basis assumption, or independence after a spectral rotation is used. Essential boundedness and continuity remain separate conclusions.

## 1. Fresh source state and exact premises

Fresh `math-research-brain/main` was resolved during the run; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The live correction boundary was re-read before publication. In particular this report does not use law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, worst-fiber conditional-density caps, a universally good physical minor, coefficient-smallness as a probabilistic perturbation, or one-heavy-row same-square absorption.

The required pinned source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed ingredients actually used below are:

1. D' and D5 on literal disjoint physical cross blocks;
2. the fractional-potential interface and scalar square peel;
3. scalar-Schur persistence of large eigenvalues;
4. the scalar-square `L^3_t` / three-independent-block Hölder mechanism.

The orientation-free rank-two affine half-Riesz theorem is source-pinned at

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`:

`H_{1/2}(X^T U Lambda U^T X+b^T X) <=128 |det Lambda|^{-1/4}`

for rank two and arbitrary affine terms.

The generic physical-edge quarter-potential theorem used in one case is source-pinned at

`yspennstate/math-open-problems@25a695084d9acb02a3c81da41ef3e23953fb1a34`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260924T050513Z-account02-B01-qform-auto11/REPORT.md`:

`H_{1/4}(R)<=C_edge |mu|^{-1/4}`, `C_edge=3.179662567631707...`,

for any literal nonzero physical edge `mu`, with arbitrary remaining quadratic/affine terms.

The preceding B02 receiver memory actually consumed here is

`math-research-brain@6a6802c4c29df79d7a7c904f53dca268d27e9dc0`,

which left the first unpaid implication `QFORM-R47-STRONGHUB-TWOSIDED-CURVATURE-OR-DIFFUSE-E2-L1-v1`.

### Newest designated partner

The latest completed compatible `account03/B02` result remains r47:

`yspennstate/math-open-problems@859066cc3edee1bbeafe367e3bf2d630a4c425d9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260924T045848Z-account03-B02-qform-r47/REPORT.md`.

Its live full physical cut `N=A[L,R]` has, on the robust rank-two branch,

`x1*x2 > kappa :=247/576`,

where `x1,x2` are the two largest squared singular values. Its global spectral-window dichotomy pays the diffuse branch, while the remaining strong physical alternatives include a literal diagonal `|A_ii|>1/228`, a carrier-aligned hub, or at most four near-coloops. Section 5 below applies this result to an exact target matrix and pays one strong-diagonal endpoint.

## 2. Exact obstruction: an invertible physical 2x2 crossing with two-sided curvature need not be Fourier-L1

Let `U1,U2,V1,V2` be independent `Uniform[-1/2,1/2]` and put

`Q4=(U1+V1)^2+(U2+V2)^2`.                                    (2.1)

With `U=(U1,U2)`, `V=(V1,V2)`,

`Q4=U^T I2 U+2 U^T I2 V+V^T I2 V`.                           (2.2)

Thus the physical cross block is literally `C=I2`, so `det C=1`, but both source banks retain quadratic curvature.

For `Z=U1+V1`, the density is

`h(z)=(1-|z|) 1_{|z|<=1}`.                                    (2.3)

Its square characteristic function is

`g(t)=E exp(it Z^2)`
`    =2 int_0^1 exp(it z^2)(1-z) dz`
`    =2 int_0^1 exp(it z^2) dz-(exp(it)-1)/(it).`             (2.4)

For `t->+infinity`, the ordinary Fresnel tail integration by parts gives

`2 int_0^1 exp(it z^2) dz`
` =e^{i pi/4} sqrt(pi) t^{-1/2}+O(t^{-1}).`                    (2.5)

Hence

`g(t)=e^{i pi/4} sqrt(pi) t^{-1/2}+O(t^{-1})`,                (2.6)

and therefore

`|g(t)|^2=pi/t+O(t^{-3/2}).`                                  (2.7)

The two pairs `(U1,V1)` and `(U2,V2)` are independent, so

`phi_Q4(t)=g(t)^2`,

and (2.7) yields the logarithmic divergence

`boxed: integral_R |phi_Q4(t)| dt = infinity.`                (2.8)

This is a rigorous obstruction to the proposed local theorem

> invertible physical `2x2` cross block + arbitrary quadratic curvature on both banks => unweighted Fourier `L1`.

It does **not** refute QFORM: the coefficient matrix in (2.2) has only two nonzero eigenvalues, both equal to two. It also does not refute the target-wide Fourier-L1 conjecture. What it proves is that the previous one-sided-twist theorem cannot be extended to arbitrary two-sided curvature merely by retaining the same local unweighted-L1 conclusion.

This is the required mechanism change: the two-sided rank-two remainder must be paid at a weaker fractional-potential level until a genuine third smoothing resource is spent.

## 3. New theorem: every 4-variable form with two large directions has a uniform half-potential

### Theorem 3.1 — `QFORM-4D-S2-HALFRIESZ-v1`

Let `H` be a real symmetric `4x4` matrix with at least two eigenvalues of modulus at least `s>0`. Let `X=(X1,...,X4)` have independent densities at most one. Arbitrary affine and constant terms are allowed. Then

`boxed: H_{1/2}(X^T H X+b^T X+c) <201 s^{-1/2}.}`             (3.1)

No sign, principal-minor, support, or moment hypothesis is imposed.

### Proof

By scaling it suffices to take `s=1`. Fix

`delta=1/100`.                                                  (3.2)

There are two exhaustive cases.

#### Case A: every physical diagonal is smaller than `delta`

Since at least two eigenvalues have modulus at least one,

`||H||_F^2>=2`.                                                  (3.3)

If every `|H_ii|<delta`, then

`2 sum_{i<j} H_ij^2 > 2-4 delta^2`.                             (3.4)

There are six edges, so one literal edge `mu=H_ij` satisfies

`mu^2 > (2-4 delta^2)/12`.                                      (3.5)

For its physical principal pair

`B=[[H_ii,mu],[mu,H_jj]]`,

(3.5) and `|H_ii H_jj|<delta^2` give

`|det B| > 1/6-(4/3)delta^2`
`          =0.166533333333... .`                               (3.6)

In particular `B` is invertible. Condition on the other two ORIGINAL coordinates. The pair remains an independent two-variable product law and acquires only arbitrary affine terms. The orientation-free rank-two affine half-Riesz theorem therefore gives

`H_{1/2}`
` <=128 [1/6-(4/3)delta^2]^{-1/4}`
` =200.3709124597... <201.`                                    (3.7)

#### Case B: some physical diagonal has modulus at least `delta`

Let `a=H_ii`, `|a|>=delta`, and complete this ORIGINAL coordinate exactly:

`X^T H X+b^T X+c = a(X_i+h)^2+T`.                              (3.8)

The scalar Schur coefficient of `T` is `3x3`. By the pinned Schur-persistence lemma, because `H` has two eigenvalues of modulus at least one, this Schur coefficient has at least one eigenvalue of modulus at least one. Hence its operator norm is at least one.

For a symmetric `3x3` matrix the operator norm is at most three times its largest entry modulus, so some physical coefficient of `T` has modulus at least `1/3`. If it is a diagonal coefficient, the scalar-square quarter-potential gives

`H_{1/4}(T)<=4*3^{1/4}`.                                       (3.9)

If it is an off-diagonal edge, `QFORM-PHYSICAL-EDGE-QUARTER-RIESZ-v1` gives a smaller constant, so (3.9) still holds.

The proved two-square logarithmic half-potential bridge from the pinned Fourier route, together with `log_+ z <=4 z^{1/4}`, gives

`H_{1/2}(a(X_i+h)^2+T)`
` <=8 |a|^{-1/2}+8*4^{-1/4} H_{1/4}(T)|a|^{-1/4}.`             (3.10)

Using `|a|>=delta=1/100` and (3.9),

`H_{1/2}`
` <=8 delta^{-1/2}+16 sqrt(2) 3^{1/4} delta^{-1/4}`
` =174.1705906042... <201.`                                    (3.11)

Cases A and B prove (3.1). Rescaling restores `s^{-1/2}`. QED.

The theorem is deliberately a half-potential statement, not an unweighted Fourier-L1 statement; Section 2 shows that demanding the latter would already be false for a natural two-sided-curvature rank-two carrier.

## 4. New scalar-pivot compiler: arbitrary two-sided 2x2 curvature is now payable

### Theorem 4.1 — `QFORM-SCALARPIVOT-FULL2X2-TWOSIDED-DENSITY-v1`

Let `i` be a literal original coordinate with scalar pivot

`a=A_ii!=0`.                                                     (4.1)

Complete it exactly and let `S` be the scalar Schur complement on the remaining original coordinates. Suppose there are disjoint physical two-coordinate sets `U,V` in the complement of `i` for which

`C=S[U,V]` is invertible and `s_2(C)>=sigma>0`.                  (4.2)

Then the full ambient quadratic form, with every other coefficient and every induced affine term arbitrary, has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity <201 (|a| sigma)^{-1/2}.}`             (4.3)

Continuity is not asserted by this argument.

### Proof

Condition on every Schur variable outside `U union V`. The remaining four original variables are still independent, with cap-one densities, and have some symmetric `4x4` quadratic coefficient `H4` whose `U x V` submatrix is exactly `C`; conditioning changes only affine and constant terms.

Coordinate restriction is a contraction on both sides, so singular-value monotonicity gives

`s_2(C)<=s_2(H4)`.                                               (4.4)

Because `H4` is symmetric, its singular values are the moduli of its eigenvalues. Thus `H4` has at least two eigenvalues of modulus at least `sigma`. Theorem 3.1, uniformly in every outside conditioning value, gives

`H_{1/2}(Schur remainder) <201 sigma^{-1/2}.`                    (4.5)

Finally the pinned scalar square peel gives

`||p_Q||_infinity`
` <=|a|^{-1/2} H_{1/2}(Schur remainder)`
` <201(|a|sigma)^{-1/2}.`                                       (4.6)

QED.

This theorem is the positive replacement for the false local Fourier-L1 extension. It allows completely arbitrary quadratic curvature on both sides of the literal `2x2` physical Schur crossing.

For the partner r47 fixed diagonal scale, if `|a|>1/228` and one such Schur crossing has `s_2(C)>=1/100`, then immediately

`||p_Q||_infinity <201 sqrt(22800)=30350.33443... .`             (4.7)

The constant is intentionally not optimized; the point is a source-valid uniform payment with no post-rotation independence and no deletion of a nonzero tail.

## 5. Exact-target application of account03/B02 r47 and live D'/D5 obstruction

Consider five original coordinates ordered as `(U1,U2,V1,V2,W)` and the physical matrix

`A_* =`
`[[1,0,1,0,0],`
` [0,1,0,1,0],`
` [1,0,1,0,0],`
` [0,1,0,1,0],`
` [0,0,0,0,1]].`                                               (5.1)

Its eigenvalues are exactly

`0,0,1,2,2`,                                                    (5.2)

so it lies in the exact owner target.

Take the partner r47 full physical cut

`L={U1,U2}`, `R={V1,V2,W}`.                                    (5.3)

Then

`N=A_*[L,R]=[I2  0]`,                                           (5.4)

so its two nonzero squared singular values are `x1=x2=1` and

`x1*x2=1>247/576`.                                              (5.5)

Thus this is a literal instance of the partner's robust rank-two packet. Its high-spectral-window projector has diagonal `(1/2,1/2,1/2,1/2,1)`, so the diffuse `1/72` leverage branch does not fire. Instead r47 lands in its strong physical-diagonal alternative: in fact every diagonal in (5.1) is one, hence certainly exceeds `1/228`.

Choose the pivot `W`, so `a=1`. Its Schur complement is the four-variable form

`Q4=(U1+V1)^2+(U2+V2)^2`,                                      (5.6)

and the physical `U x V` Schur crossing is `C=I2`, `s_2(C)=1`. Theorem 4.1 therefore pays this actual r47 endpoint by

`boxed: ||p_Q||_infinity <201.}`                                (5.7)

This is the requested equation-level application of the newest designated partner result.

### D', reviewed sharp-HY E3, and D5 are genuinely unavailable here

The only nonzero off-diagonal edges of `A_*` are the two disjoint matching edges `U1--V1` and `U2--V2`. Therefore every disjoint physical cross block of `A_*` has rank at most two. Consequently, for every disjoint physical `I,J`,

`boxed: E3(A_*[I,J])=0,   E5(A_*[I,J])=0.}`                    (5.8)

Hence D', the reviewed marginal-free sharp-HY `E3` refinement, and D5 all have exactly zero exterior-volume currency on this exact-target family. The deterministic enumeration checked all 180 nonempty disjoint physical cuts among the `3^5` assignments: 84 have rank zero, 84 rank one, 12 rank two, and none rank three or higher.

This is a target-valid obstruction to the strategy

> every r47 strong-diagonal/two-sided-curvature endpoint must eventually create positive physical E3 or E5.

It is **not** a QFORM counterexample.

### The full target family is nevertheless Fourier-L1 by product-preserving grouping

For arbitrary cap-one input laws on (5.1), define

`Y1=U1+V1`, `Y2=U2+V2`.                                       (5.9)

These are not spectral rotations. They are functions of disjoint original-coordinate pairs, so `Y1,Y2,W` are genuinely independent. Moreover convolution gives

`||p_Y1||_infinity, ||p_Y2||_infinity <=1`.                    (5.10)

Thus

`Q=Y1^2+Y2^2+W^2`                                              (5.11)

is a diagonal three-square form in three independent cap-one grouped variables. The current diagonal theorem gives

`boxed: ||p_Q||_infinity<=pi.}`                                 (5.12)

There is also a genuine unweighted Fourier-L1 estimate. If `Y` has density at most one and `G_Y(t)=E exp(itY^2)`, the square density `h` satisfies `h(s)<=s^{-1/2}` and

`int h(s)^{3/2} ds <= E |Y|^{-1/2} <=5`.                        (5.13)

Hausdorff--Young therefore gives

`||G_Y||_3 <= (2pi)^{1/3} 5^{2/3}`.                             (5.14)

Applying Hölder in time to the three independent square factors in (5.11),

`boxed: integral_R |phi_Q(t)| dt <=50 pi.}`                     (5.15)

Hence this exact-target family has a continuous `C0` density. The third genuinely independent smoothing group repairs the logarithmic divergence (2.8) of the two-sided rank-two remainder.

For the specific uniform laws of Section 2, (2.8) shows the contrast exactly:

`integral |phi_Q4|=infinity`, while `integral |phi_Q5|<infinity`. (5.16)

This is the main conceptual gain of the run.

## 6. What changed and first unpaid implication

Three possible continuations of the previous one-sided theorem were tested:

1. extend local unweighted Fourier L1 directly to an arbitrary two-sided-curvature invertible `2x2` carrier — **refuted by (2.8)**;
2. force the r47 endpoint back into physical E3 — **refuted on the exact-target family (5.1) by (5.8)**;
3. force D5 instead — **also refuted there by (5.8)**.

The mechanism therefore changes to **fractional potential first, third smoothing second**.

The live next edge is

`QFORM-R47-DIAGONAL-SCHUR-E2-DIFFUSE-OR-FIXED-CARRIER-v1`:

on the partner's physical-diagonal branch `|A_ii|>1/228`, after exact scalar completion, prove that the Schur remainder either

- has a quantitatively conditioned literal physical `2x2` cross block, paid by Theorem 4.1;
- has diffuse aggregate physical pair-volume, paid by the completed `D2` half-potential receiver followed by the square peel; or
- collapses to a source-preserving grouped bi-star/near-coloop carrier that must be handled directly.

A one-good-minor theorem is not being assumed: the concentrated pair-volume endpoint can be genuinely diffuse over the second row/column, and existing corrections rule out that shortcut. The remaining carrier-aligned off-diagonal-hub and near-coloop branches are also still unpaid.

The unrestricted QFORM conjecture therefore remains **OPEN**. Full-target continuity remains **OPEN**. The target-wide universal unweighted Fourier-L1 criterion remains **OPEN / not refuted**: this run refutes only the local two-sided `2x2` unweighted-L1 receiver before the third target direction is spent.

## 7. Deterministic checks and telemetry boundary

`check_obstruction.py` and `CHECK_RESULTS.txt` in this run directory verify the spectrum (5.2), enumerate all disjoint physical cross-cut ranks, and verify the constants in Theorem 3.1. Status: `PASS`.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort: `UNKNOWN`. Provider reasoning-token count and provider thinking seconds: `null / NOT_EXPOSED`. Elapsed wall time is `UNKNOWN/null`; no pure-thinking duration is inferred.
