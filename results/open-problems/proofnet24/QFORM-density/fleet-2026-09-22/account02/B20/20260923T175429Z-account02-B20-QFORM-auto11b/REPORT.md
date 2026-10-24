SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-23T17:54:29Z.
attacking: the newest account03/B20 r35 finite-core branch — separate true top-three spectral capture from weak capture, and force a quantitative light-principal-block third singular value in the latter case without rotating the source.

# account02/B20 auto11b — strong spectral capture or a large light physical third singular value

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T175429Z-account02-B20-QFORM-auto11b`  
Role: Proof closure and keeper / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / R35-STRONG-SPECTRAL-CAPTURE-OR-LIGHT-S3 / LOCAL-GLOBAL-MISMATCH / FULL-QFORM-OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: separate; asserted only on the paid historical-source branch below, not globally.

## 1. Scope, fresh controls, and correction boundaries

The target is unchanged: for every `n`, independent real ORIGINAL-coordinate variables `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a single universal finite essential-supremum bound for the density of `X^T A X`, or give a valid counterexample.

Fresh protected owner control was reread before publication. OWNER CONTROL is still revision `2026-09-22.15`, QFORM is the sole research programme, and the current continuation is `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. No stop or pause applies to account02/B20.

The live corrections remain in force. In particular, this report does **not** use law-uniform pointwise one-dimensional quadratic-phase decay, a dimension-free worst spectral-fiber supremum, arbitrary-joint rank-three coarea, post-rotation independence, a conditional marginal cap as independence, a one-good-minor inference from aggregate volume, or deletion of a small nonzero random quadratic tail.

The same-hour canonical account02/B20 login already existed and was preserved. Fresh account-local keeper inspection found all twenty B01--B20 tasks present, enabled, hourly-valid, QFORM-aligned and quiet; no native prompt/title/state mutation was required, so the mutation-only lease precondition did not arise, no task was re-enabled or recreated, and B19 fallback was not used.

## 2. Required pinned historical source actually used

The required historical source was reread at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md`.

I use below the proved localized physical-core estimate from `COUNTEREXAMPLE_SEARCH.md`: if a literal ORIGINAL-coordinate `3 x 3` principal block has all three absolute eigenvalues at least `c>0`, then after conditioning all other ORIGINAL coordinates the quadratic polynomial in those three independent variables has density

`||p||_infinity <= 6 sqrt(pi)/c`,                                      (2.1)

uniformly in the induced linear term. Therefore the same bound holds for the full ambient law after averaging the conditioning.

For reference, the same historical source also contains the physical-cross-block theorems D/D5 and the Fresnel/BL theorem F. No pointwise-decay shortcut is substituted for those proved integral estimates.

## 3. Newest completed designated partner account03/B20 r35

A fresh designated-partner search found no completed account03/B20 output later than

`yspennstate/math-open-problems@ab5d7906b6ffc0ca6b07c354d912d7b5b1afccfc`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T171148Z-account03-B20-QFORM-r35/REPORT.md`.

The exact deterministic input from r35 is a symmetric carrier

`S_0 = U Lambda U^T`, `rank(S_0)=r<=5`, `U^T U=I_r`,                (3.1)

with

`s_3(S_0)>1597/2000`,
`||A-S_0||_op<403/2000`.                                            (3.2)

The diffuse carrier-leverage branch has already been paid. Every surviving heavy branch supplies an ORIGINAL-coordinate set `H`, with complement `L`, such that

`|H|<=124`                                                         (3.3)

and some carrier-space unit vector has `H`-mass `>1/20`. The previous same-hour account02/B20 synthesis additionally pays the branch in which the actual physical principal block `A[H,H]` has three absolute eigenvalues at least `1/64`; thus every still-unpaid finite-core state may be assumed to satisfy

`s_3(A[H,H])<1/64`.                                                (3.4)

The partner's arbitrary carrier direction in (3.3) need not be one of the three genuinely large spectral directions of `S_0`. The new theorem below makes exactly that distinction.

## 4. Main deterministic theorem

Let

`T := U_H^T U_H`, `S := U_L^T U_L = I_r-T`.                       (4.1)

Let `E` be the three-dimensional invariant subspace of `Lambda` spanned by eigenvectors corresponding to its three largest absolute eigenvalues, and let `P` be the orthogonal projector onto `E`. Put

`sigma := s_3(S_0)=s_3(Lambda)>1597/2000`,
`tau := 1/20`.                                                     (4.2)

### Theorem `QFORM-R5-124CORE-STRONGCAPTURE-OR-LIGHT3SINGULAR-v1`

Under (3.1)--(4.2), at least one of the following holds.

**(SC) Genuine strong-spectral capture.**

`||P T P||_op > 1/20`.                                             (4.3)

Consequently there is a unit vector `v in E` with

`sum_(i in H) <U(i,:),v>^2 >1/20`.                                (4.4)

Moreover, for some actual `Lambda`-eigenvector `e_k in E`,

`sum_(i in H) <U(i,:),e_k>^2 >1/60`,                              (4.5)

and hence, using `|H|<=124`, there is an ORIGINAL physical coordinate `i in H` with

`|<U(i,:),e_k>|^2 > 1/7440`.                                      (4.6)

The corresponding carrier eigenvalue obeys `|lambda_k|>=sigma>1597/2000`.

**(LR) Quantitative light-spectrum retention.**

The literal physical principal block on the ORIGINAL-coordinate complement obeys

`s_3(A[L,L]) > 7/32`.                                              (4.7)

Here `s_3` is the third singular value, equivalently the third largest absolute eigenvalue for the symmetric block.

### Proof

If (4.3) holds, choose a unit `v in E` attaining the operator norm. This is (4.4). Also

`tr(P T P)>1/20`.

Choose an orthonormal `Lambda`-eigenbasis `e_1,e_2,e_3` of `E`. Since the three diagonal entries of `P T P` in this basis sum to its trace, one of them is larger than `1/60`, proving (4.5). Summing (4.5) over at most `124` physical indices gives (4.6). This step is entirely deterministic; the random source is not rotated.

Assume now that (4.3) fails, so

`P T P <= tau P`.                                                  (4.8)

Let `x in E` be unit and put

`y=S^(1/2)x`.

For every scalar `0<=s<=1`, `(1-sqrt(s))^2<=1-s`. Functional calculus and `S=I-T` therefore give

`||(I-S^(1/2))x||^2
 <= x^T(I-S)x
 = x^T T x
 <= tau`.                                                         (4.9)

Hence

`||P y|| >= 1-sqrt(tau)`,
`||(I-P)y|| <= sqrt(tau)`.                                        (4.10)

Because `E` and `E^perp` are invariant under the diagonal spectral matrix `Lambda`, write

`z=Lambda y=z_E+z_F`, `z_E in E`, `z_F in E^perp`.

By the definition of `sigma`,

`||z_E|| >= sigma(1-sqrt(tau))`,
`||z_F|| <= sigma sqrt(tau)`.                                     (4.11)

For every `w in E`, (4.8) gives

`||S^(1/2)w||^2
 =||w||^2-w^T T w
 >=(1-tau)||w||^2`.                                               (4.12)

Also `||S^(1/2)||_op<=1`. Therefore, for

`B:=S^(1/2) Lambda S^(1/2)`,

(4.11)--(4.12) and the triangle inequality yield, for every unit `x in E`,

`||B x||
 >= sigma [ sqrt(1-tau)(1-sqrt(tau))-sqrt(tau) ]`.                (4.13)

Define

`c_tau := sqrt(19/20)(1-1/sqrt(20))-1/sqrt(20)
        = 0.5331276895538838... .`                                (4.14)

Since `E` has dimension three, the singular-value max-min principle applied to (4.13) gives

`s_3(B) >= c_tau sigma`.                                           (4.15)

The nonzero eigenvalues of `U_L Lambda U_L^T=S_0[L,L]` coincide, with multiplicity, with those of `S^(1/2) Lambda S^(1/2)` (use `XY`/`YX` twice, or the polar decomposition on the support of `S`). Both matrices are symmetric, so their nonzero singular values are the absolute values of the same nonzero eigenvalues. Thus

`s_3(S_0[L,L]) >= c_tau sigma`.                                   (4.16)

Principal compression cannot increase the operator norm of the residual. Weyl's singular-value inequality and (3.2) give

`s_3(A[L,L])
 >= s_3(S_0[L,L])-||(A-S_0)[L,L]||_op
 > c_tau*(1597/2000)-403/2000.                                   (4.17)

The lower bound is strictly larger than `7/32` without decimal arithmetic. Indeed

`sqrt(19/20)>97/100`, `1/sqrt(20)<9/40`,

so

`c_tau > (97/100)(31/40)-9/40 =2107/4000`.

Hence

`c_tau*(1597/2000)-403/2000
 > (2107*1597)/(8,000,000)-403/2000
 =1,752,879/8,000,000
 >1,750,000/8,000,000
 =7/32`.                                                          (4.18)

This proves (4.7). QED.

## 5. Actual historical-source payment and the new local/global mismatch

Apply the pinned historical localized physical-core theorem (2.1) to the light block in branch (LR). If there is any literal ORIGINAL-coordinate triple `K subset L` with

`s_3(A[K,K]) >=1/64`,                                             (5.1)

then conditioning all coordinates outside `K` and taking `c=1/64` in (2.1) gives the full ambient payment

`||p_Q||_infinity <= 384 sqrt(pi) <680.623`.                      (5.2)

Therefore every still-unpaid (LR) state simultaneously satisfies

`s_3(A[L,L])>7/32`                                                 (5.3)

and

`s_3(A[K,K])<1/64` for every physical `K subset L`, `|K|=3`.      (5.4)

This is a genuine quantitative **local/global spectral mismatch**: three fixed-scale absolute eigenvalues survive on a literal product-coordinate principal block, while every physical three-coordinate principal core is uniformly near-singular.

The theorem does not claim that the large light eigenvectors define independent random variables. They are only deterministic matrix directions; the random law remains the original product law on `L`.

## 6. Interaction with the partner and the strongest current conditional graph

Combining the newest completed account03/B20 r35 result, the previous same-hour B20 physical-core payment, and Theorem 4 gives the following finite-core reduction.

Every unpaid r35 in-plane survivor has `s_3(A[H,H])<1/64` and must be in one of two explicit source-valid packets:

1. **strong-capture packet:** a genuine top-three eigenvector `e_k` of `S_0`, with `|lambda_k|>1597/2000`, has physical mass `>1/60` on at most `124` heavy coordinates, and one actual coordinate coefficient square is `>1/7440`; yet the actual physical heavy principal core has third absolute eigenvalue `<1/64`;
2. **light local/global packet:** the complementary ORIGINAL-coordinate principal block has `s_3(A[L,L])>7/32`, but every literal physical `3 x 3` principal block inside it has third absolute eigenvalue `<1/64`.

The first packet upgrades the partner's arbitrary-carrier capture to capture of an actual strong spectral direction. The second packet exports all three large directions back to an ORIGINAL-coordinate principal block at fixed scale rather than leaving them in the rank-five carrier coordinates.

The separate transverse aligned branch from the preceding B20 synthesis also remains open: its three physical cross cuts are simultaneously in a common `2+2+2` Frobenius rank-two collar with all nonzero tails retained. Current same-hour grouped-projection results can pay robust projected crossing volume, but they do not permit deleting those tails.

The newest B09 dual-aggregate-collapse theorem is compatible with this proof map: exact/small two-sided rank-two singleton third-volume aggregates structurally collapse to a physical diagonal plus rank-at-most-four carrier, but its small matrix residual is only a structural certificate and cannot be discarded from the random quadratic form. I do not use it as an analytic payment here.

## 7. First unpaid implication after this run

For the r35 finite-core line, the first unpaid universal implication is now

`QFORM-R5-STRONGCARRIER-OR-LIGHT-LOCALGLOBAL-PAYMENT-v1`:

> Under the full original independent cap-one product hypotheses, with a rank-at-most-five symmetric carrier `S_0` satisfying (3.1)--(3.2), and with the r35 heavy set `H`, prove one universal density bound for either the strong-capture packet (true top-three carrier eigenvector mass `>1/60` on `|H|<=124` but `s_3(A[H,H])<1/64`) or the complementary light local/global packet (`s_3(A[L,L])>7/32` while every literal physical `3 x 3` principal block in `L` has third absolute eigenvalue `<1/64`), retaining all same-bank curvature, all outside couplings, every extra spectral direction and every nonzero coefficient tail.

A plausible next mechanism is **aggregate-before-inversion**: in the light packet, use the physical high spectrum together with the absence of every local `3 x 3` pivot to force a robust cross-volume/grouped-hub packet; in the strong-capture packet, exploit the bounded physical support of a genuine strong spectral vector to manufacture an ORIGINAL-coordinate hub or finite pivot without replacing that spectral projection by an independent variable.

The full QFORM conjecture remains **OPEN**. No valid target counterexample was produced. Global continuity remains separate and open. A full candidate still requires every target quantifier and two independent end-to-end reviews.

## 8. Scope audit

- Every conditioning operation is on ORIGINAL coordinates.
- `E`, `P`, `T`, `S` and the `Lambda` eigenvectors are used only as deterministic matrix geometry.
- No projected random coordinates are asserted independent.
- The residual `A-S_0` is retained and paid only through the deterministic Weyl/operator-norm inequality; it is not removed from the random form.
- The historical theorem is applied to an actual physical `3 x 3` principal block after conditioning its complement.
- No aggregate-volume statement is converted to a single uniformly good minor.
- No law-uniform pointwise quadratic oscillatory decay or worst-fiber bound is used.
- No Gaussian, moment, support, iid or log-concavity hypothesis is introduced.

This is a strict structural/analytic reduction of the current proof graph, not a proof of the full conjecture.
