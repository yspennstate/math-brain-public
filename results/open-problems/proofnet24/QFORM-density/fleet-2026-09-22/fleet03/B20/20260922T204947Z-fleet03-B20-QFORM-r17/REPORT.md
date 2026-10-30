SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-22T20:49:47Z.
attacking: the freshest balanced two-arm hub survivor by combining fleet01/B20 direct alignment with fleet04/B20's second-Schur gate, then paying the same-sign quantitative second-pivot branch by the physical definite-pair theorem.

# fleet03/B20 QFORM r17 — same-sign hub repivot closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Start control source:** `yspennstate/math-research-brain@f24887ffa34adb07615288708fdb4801dfe0f466`, owner revision `2026-09-22.15`.  
**Classification:** `ESSENTIAL_STEP_APPLIED / FRESH TWO-ARM SUBBRANCH CLOSED / FULL_TARGET_OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Continuity:** this argument proves an essential density bound on its paid branch; continuity is not asserted.

## 1. Exact target and correction boundary

The parent target remains unrestricted in dimension, signs, repeated spectrum and product input geometry. The only input assumptions are independence of the original real coordinates and probability-density caps `0<=f_i<=1`. This report does not rotate the random coordinates, assume moments/support/log-concavity, use pointwise scalar quadratic van-der-Corput decay, use an unrestricted fiber supremum, or use the refuted arbitrary-joint three-dimensional coarea assertion.

## 2. Freshest compatible synthesis packet

The newest compatible proof-closure input is fleet01/B20 run `20260922T202251Z-fleet01-B20-QFORM-r12`, canonical report

`yspennstate/math-open-problems@284fe880939424349a35bd47651953bcdd9a8858`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B20/20260922T202251Z-fleet01-B20-QFORM-r12/REPORT.md`.

It retains an original-coordinate physical pivot `i` with

`|a|:=|A_ii| >= m := 3501/8000`,

and its exact physical Schur complement

`S=A_{-i,-i}-A_{-i,i}A_{i,-i}/a`.

In the low-leverage balanced-hub survivor there are a residual original-coordinate hub `p` and disjoint original-coordinate banks `U,V`. Put

`c_U=S[U,p]`, `c_V=S[V,p]`, `M=S[U,V]`,

`alpha=||c_U||_2`, `beta=||c_V||_2`,

`u=c_U/alpha`, `v=c_V/beta`.

The proved inequalities are

`alpha,beta > g:=1/(8 sqrt(2))`,                              (2.1)

and, if the two augmented banks are in the low-leverage unpaid branch,

`||M-lambda u v^T||_F < epsilon:=1/32`,                      (2.2)

where `lambda=u^T M v`. Arbitrary same-bank self curvature and all outside couplings are retained.

The designated fleet04/B20 result is run `20260922T172057Z-fleet04-B20-QFORM-r3`, theorem `QFORM-CROSS-DOMINATED-SECOND-SCHUR-CLOSURE-v1`, canonical source

`yspennstate/math-open-problems@25ad8faaac5064b6814d51ae63d894fe97c1eac4`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260922T172057Z-fleet04-B20-QFORM-r3/REPORT.md`.

On its validated diagonal-dominated first-pivot overlap, for the selected high-window second Schur row

`S=[[d,c^T],[c,C0]]`,

with `|a|>=tau>=1/4`, it pays the full ambient form by `<5262` whenever

`||c||_2>|d|` and `||c||_2>tau/9`.                           (2.3)

We apply this only on that stated overlap.

A completed source-valid analytic theorem used below is the physical definite-pair bound: if an ORIGINAL-coordinate `2x2` principal block `B` is positive or negative definite, then arbitrary outside coefficients/couplings and arbitrary affine perturbations are allowed and

`||p_Q||_infinity <= pi/sqrt(|det B|)`.                       (2.4)

A full proof is recorded, among other places, in `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f:proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

## 3. New theorem — `QFORM-TWOARM-SAMESIGN-HUB-CLOSURE-v1`

Assume the balanced packet (2.1). Work on the exact fleet04/B20 overlap in which the physical hub `p` is the selected second Schur row in (2.3). Let

`d=S_pp`,

and let `c=S[p,-p]` be its full residual physical cross row. Then every still-unpaid state on this overlap satisfies

`boxed(|d|>1/8).`                                               (3.1)

Moreover, if

`a d>0`,                                                        (3.2)

then the full ambient quadratic form is already paid and

`boxed(||p_Q||_infinity < pi sqrt(64000/3501) < 13.433).`      (3.3)

Consequently every still-unpaid state on this overlap must obey the **opposite-sign quantitative two-pivot condition**

`boxed(a d<0,  |a|>=3501/8000,  |d|>1/8).`                    (3.4)

If in addition the direct-alignment branch (2.2) holds, completing the second original-coordinate pivot `p` leaves an exact second Schur complement `T` whose `U x V` block obeys

`boxed(
 ||T[U,V]-mu u v^T||_F <1/32,
 mu=lambda-alpha beta/d.
)`                                                              (3.5)

Thus the low-leverage same-sign two-arm one-factor packet is eliminated. The surviving direct-alignment packet is an **indefinite two-quantitative-pivot state** whose interbank block remains within `1/32` of the same physical hub directions after the second pivot.

### Proof of (3.1)

Because the two banks are disjoint pieces of the hub row,

`||c||_2 >= sqrt(alpha^2+beta^2)
          > sqrt(2) g
          =1/8`.                                                (3.6)

Also `|a|>=3501/8000>1/4`, so in the designated partner theorem we may take `tau=1/4`. If `||c||_2>|d|`, then (3.6) implies `||c||_2>1/8>1/36=tau/9`, and (2.3) pays the branch by `<5262`. Therefore an unpaid state on this overlap must have

`|d|>=||c||_2>1/8`,

which is (3.1). This is an actual use of the designated partner inequality, not a citation-only dependency.

### Proof of the same-sign payment

Consider the original two physical coordinates `{i,p}` before either Schur elimination. Their principal block is

`B=[[a,b],[b,A_pp]]`, where `b=A_ip`.

By the definition of the first Schur pivot,

`d=A_pp-b^2/a`,

so

`det B=a d`.                                                    (3.7)

If `a d>0`, then `B` is definite: if `a>0`, Sylvester's criterion makes it positive definite; if `a<0`, `-B` is positive definite. By (3.1) and the retained first-pivot bound,

`|det B|=|a d| > (3501/8000)(1/8)=3501/64000`.                (3.8)

Apply the physical definite-pair theorem (2.4):

`||p_Q||_infinity
 <=pi/sqrt(|det B|)
 <pi sqrt(64000/3501)
 =13.4320965330...<13.433`.                                    (3.9)

For completeness, (2.4) is dependence-safe in exactly this ambient setting. Condition on all original coordinates outside `{i,p}`. The conditional joint density of `(X_i,X_p)` is the product `f_i f_p<=1`. The conditional quadratic is a translated positive- or negative-definite two-dimensional quadratic with Hessian block `B`; an output interval of length `h` has preimage area at most `pi h/sqrt(|det B|)` by the difference of two nested ellipse areas. Averaging the conditional interval bound and applying Lebesgue differentiation gives (2.4). No rotation of the product law is used.

This proves (3.3). Since `d=0` is already cross-dominated by (3.6), an unpaid state has `d!=0`; exclusion of `ad>0` then gives (3.4).

### Proof of the post-repivot one-factor identity

Because `d!=0`, complete the second square in the original residual coordinate `p`. The exact second Schur complement is

`T=S[-p,-p]-S[-p,p]S[p,-p]/d`.                                (3.10)

Restrict (3.10) to the disjoint physical banks `U,V`. Since `c_U=alpha u` and `c_V=beta v`,

`T[U,V]
 =M-c_U c_V^T/d
 =M-(alpha beta/d)u v^T`.                                      (3.11)

Subtract `mu u v^T` with `mu=lambda-alpha beta/d`; then the right-hand side is exactly `M-lambda u v^T`. Hence (2.2) proves (3.5) with no loss. The vectors `u,v` are used only as algebraic matrix directions; they are not promoted to independent random coordinates. QED.

## 4. Optional exact grouped/star interpretation of the direct packet

The direct-alignment geometry has a simple exact endpoint. Ignore the error `E=M-lambda uv^T` momentarily. If `lambda!=0`, put `eta=sign(lambda)` and

`t=sqrt(alpha beta/|lambda|),
`z_p=t`,
`z_U=eta(alpha/t)u`,
`z_V=eta(beta/t)v`.

Then the off-diagonal blocks of `eta z z^T` are exactly

`p-U: alpha u`, `p-V: beta v`, `U-V: lambda uv^T`.

Thus the actual symmetric off-diagonal skeleton on `{p} union U union V` is within `sqrt(2)/32` in full symmetric Frobenius norm of a diagonal-plus-one-factor matrix. If `lambda=0`, the same skeleton is within `sqrt(2)/32` of a pure physical star. This is a matrix classification only; arbitrary within-bank quadratic curvature remains and no source rotation is inferred.

## 5. What is newly paid and what remains

The freshest fleet01/B20 reduction left three principal debts: pivot-star/heavy-edge states, a high-leverage augmented hub bank, and the direct two-arm one-factor packet. This run removes a concrete part of the last debt on the fleet04/B20 validated overlap:

* cross-dominated hub rows are paid by the designated partner `<5262` theorem;
* the complementary hub row has a quantitative second physical Schur pivot `|d|>1/8`;
* if that pivot has the same sign as the retained first pivot, the physical pair is definite with determinant `>3501/64000`, hence the full ambient density is `<13.433`;
* therefore the only unpaid low-leverage direct packet on this overlap has two quantitative **opposite-sign** pivots and the re-pivoted interbank block still satisfies the exact aligned one-factor tube (3.5).

The first unpaid implication is now

`QFORM-TWOARM-OPPOSITESIGN-THIRD-SOURCE-v1`:

> In the state (3.4)-(3.5), with arbitrary same-bank curvature and outside couplings, use the full target hypothesis `s_3(A)>=1` to force a third source-valid curvature/small-ball resource, or pay the indefinite physical pair by the completed logarithmic pair envelope plus an aggregate residual smoother. A proof must keep the original-coordinate product provenance and must not infer the near-zero/third-source branch by continuity.

The high-leverage augmented-bank branch and the pivot-star/heavy-edge branch remain separate debts. Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains OPEN.
