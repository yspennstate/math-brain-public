SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-23T19:02:14Z.
attacking: newest fleet03/B20 r37 common-plane three-fan survivor; turn every diffuse mixed fan cut into either a fixed third-cross-volume payment or a simultaneous normalized Schur-cancellation/planar-twist collar, without rotating the random source.

# fleet02/B20 — r37 mixed-fan Schur compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control: revision `2026-09-22.15`  
Status: **ESSENTIAL STEP APPLIED / DIFFUSE R37 PAID OUTSIDE A SIX-RELATION SCHUR COLLAR / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted target remains OPEN: for arbitrary independent real inputs with one-dimensional densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^T A X`, or produce a valid counterexample.  No moment, support, log-concavity, iid, diagonal-basis, or post-rotation-independence hypothesis is introduced below.  Continuity is tracked separately and is not claimed for the new branch.

## 1. Fresh controls, source corrections, and keeper state

Fresh `math-research-brain/main` was resolved at the beginning of the run and the current owner control, role files, protocol, QFORM manifest/current research/claims/deltas/correction inbox/pathways/memory protocol, both required requests, the current exclusive-sign-in continuation, the current Fisher continuation, and `assignments/fleet02/B20.json` were read.  The current source-backed corrections remain active: no law-uniform pointwise quadratic-phase decay, no dimension-free worst-fiber supremum, no conditional-cap-as-independence shortcut, no independence after spectral rotation, no deletion of a small nonzero random quadratic tail on rough unbounded inputs, and no inference of a uniformly good physical minor from aggregate volume alone.

Fresh account-local keeper inspection found the same twenty `fleet02` QFORM tasks `B01`--`B20`, all enabled, hourly-valid, QFORM-aligned, and quiet.  No native prompt/title/state repair was needed; consequently no mutation lease, re-enable, duplicate creation, or `B19` fallback was used.

## 2. Required historical source: an actual physical fifth-volume exit

The pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

at

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was reread, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its unrestricted fifth-volume theorem applies to an ACTUAL original-coordinate cross block `M` with

`Z_5=e_5(M^T M)`

and gives

`||p_Q||_infinity <= 5 sqrt(2e) Z_5^(-1/10)`.                    (2.1)

There is no row-marginal hypothesis in this theorem, and arbitrary same-bank quadratic blocks and affine terms remain present.  In particular, on every physical mixed fan cut introduced below,

`Z_5 >= 1/1024`

would imply

`boxed: ||p_Q||_infinity <= 10 sqrt(2e) < 23.317.`               (2.2)

Thus a still-unpaid mixed fan may be assumed to have `Z_5<1/1024`.  This is the required equation-level application of the pinned source; it is not a rotated-coordinate statement.

## 3. Newest completed designated partner: fleet03/B20 r37

The newest compatible completed designated result at publication preparation is fleet03/B20 r37,

`math-open-problems@598dae792b4a447492bc318bfa830fece803bb6d`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T184417Z-fleet03-B20-QFORM-r37/REPORT.md`.

On the surviving common-plane chamber it supplies three disjoint ORIGINAL-coordinate banks

`D_1, D_2, K`

and a common two-dimensional physical `K`-plane.  Its heavy/diffuse dichotomy uses the constants

`beta = 0.01651671529470044`,
`epsilon = 0.0023595307563857772`,
`a_H = beta/4-epsilon = 0.0017696480672893325`,

and, in the diffuse branch,

`boxed: a_D = beta/sqrt(12)-epsilon
             = 0.002408434254376076.`                            (3.1)

The diffuse conclusion is one literal partition

`K=K_1 disjoint_union K_2 disjoint_union K_3`                    (3.2)

such that for `r=1,2` and every `b=1,2,3`, if `U_r` is the partner's two-dimensional physical left frame then

`boxed: s_2(U_r^T A[D_r,K_b]) > a_D.`                            (3.3)

Equivalently, every one of the six arm blocks has singular-product resource strictly larger than

`a_D^2 = 5.800555557652045e-6`.                                  (3.4)

This exact partner expression is the input used below.  The partner's separate heavy branch gives one physical `k in K` with both arm norms bigger than `a_H`; that branch remains a separate first-edge debt after the present diffuse closure.

## 4. Physical mixed-fan compression

For each bank `K_b`, choose an orthonormal two-frame `R_b` in the ORIGINAL coordinate space of `K_b` so that

`A_b := U_1^T A[D_1,K_b] R_b`                                    (4.1)

is a `2 x 2` invertible matrix whose singular values are the two nonzero singular values of the rank-two row map `U_1^T A[D_1,K_b]`.  Likewise choose an orthonormal two-frame `L_b` in the physical coordinate space of `K_b` so that

`B_b := L_b^T A[K_b,D_2] U_2`                                    (4.2)

is `2 x 2` invertible with the two singular values of `U_2^T A[D_2,K_b]`.  By (3.3),

`boxed: s_2(A_b)>a_D,   s_2(B_b)>a_D`                            (4.3)

for every `b`.

Put

`C_0 := U_1^T A[D_1,D_2] U_2`,                                  (4.4)

and for ordered distinct `a,b`,

`D_ab := L_a^T A[K_a,K_b] R_b`.                                 (4.5)

Now form the ACTUAL original-coordinate physical cross cut

`M_ab := A[D_1 union K_a, K_b union D_2]`.                       (4.6)

Compress its row space by `diag(U_1,L_a)` and its column space by `diag(R_b,U_2)`.  This is deterministic coefficient geometry only.  The resulting `4 x 4` matrix is

`T_ab = [[A_b, C_0],
         [D_ab,B_a]].`                                           (4.7)

No random variable has been rotated and no projected random coordinates are asserted to be independent.

## 5. Exact Schur-minor identity

Define

`S_ab := B_a-D_ab A_b^(-1) C_0`.                                (5.1)

For `q,j in {1,2}`, take the `3 x 3` minor of `T_ab` formed by the two top rows plus bottom row `q`, and the two left-block columns plus right-block column `j`.  The elementary block-determinant formula gives exactly

`det minor(q,j)
  = det(A_b) [ (B_a)_(qj) - (D_ab A_b^(-1) C_0)_(qj) ]
  = det(A_b) (S_ab)_(qj).`                                      (5.2)

Summing these four squared minors,

`e_3(T_ab T_ab^T)
  >= det(A_b)^2 ||S_ab||_F^2.`                                  (5.3)

Also

`e_3(M M^T)=||wedge^3 M||_HS^2`.

Orthogonal row/column compression cannot increase this exterior Hilbert--Schmidt norm.  Hence

`e_3(M_ab M_ab^T)
  >= e_3(T_ab T_ab^T)
  >= det(A_b)^2 ||S_ab||_F^2.`                                  (5.4)

By (4.3), `|det A_b|=s_1(A_b)s_2(A_b)>a_D^2`, and therefore

`boxed:
 e_3(M_ab M_ab^T) > a_D^4 ||S_ab||_F^2.`                        (5.5)

This is the main new deterministic identity.  It spends the partner's exact two-singular-value resource on a literal physical mixed cut while retaining every same-bank term and every extra spectral direction.

## 6. Fixed payment or normalized six-relation collar

Set the universal threshold

`delta_0 := a_D^2
          = 5.800555557652045e-6.`                               (6.1)

A fresh completed full-law receiver, `QFORM-Z3-CROSSING-MARGINAL-FREE-v1` (fleet02/B03), says that for any actual original-coordinate cross cut `M` with

`Z_3=e_3(MM^T)>0`,

arbitrary same-side quadratic blocks, affine terms, and additional spectrum are allowed and

`||p_Q||_infinity
 <= C_3 Z_3^(-1/6),
 C_3=10.5501688311648... .`                                     (6.2)

Therefore if for some ordered pair `a!=b`,

`||S_ab||_F >= delta_0`,                                        (6.3)

then (5.5) gives

`Z_3 > a_D^4 delta_0^2 = a_D^8`,                                (6.4)

and (6.2) yields the explicit full-law payment

`boxed:
 ||p_Q||_infinity
 < C_3 a_D^(-4/3)
 < 32679.823.`                                                   (6.5)

Thus every diffuse r37 state not already paid by (2.2) or (6.5) satisfies simultaneously, for all six ordered pairs `a!=b`,

`boxed:
 ||B_a-D_ab A_b^(-1) C_0||_F < a_D^2.`                         (6.6)

This is already much stronger than the bare three-fan statement: all six possible mixed-fan Schur defects are tiny at the same fixed absolute scale.

Normalize (6.6) on the left.  Since `||B_a^(-1)||_op < 1/a_D`,

`boxed:
 || I_2 - B_a^(-1) D_ab A_b^(-1) C_0 ||_op < a_D
 < 0.002409.`                                                    (6.7)

Equation (6.7) is a dimensionless coherent planar-twist collar.  It retains all coefficients; no small random quadratic term is discarded.

## 7. Immediate rank consequences

Because `s_2(B_a)>a_D`, (6.6) also forces `C_0` and every `D_ab` to be invertible in an unpaid diffuse survivor.

Indeed, if `rank C_0<=1` or `rank D_ab<=1`, then

`rank(D_ab A_b^(-1) C_0)<=1`.                                   (7.1)

By Eckart--Young, the operator distance from the invertible `B_a` to any rank-at-most-one matrix is at least `s_2(B_a)>a_D`.  But (6.6) gives the stronger operator estimate

`||B_a-D_ab A_b^(-1) C_0||_op
 <= ||S_ab||_F
 < a_D^2
 < a_D`,                                                        (7.2)

contradiction.  Hence

`boxed: det C_0 !=0,   det D_ab !=0 for every a!=b.`             (7.3)

This removes the rank-one/self-edge-degenerate part of the diffuse three-fan chamber automatically.  The remaining diffuse endpoint is therefore not an arbitrary rank-two tube; it is a three-bank triangle of invertible compressed `2 x 2` transitions satisfying six simultaneous near-identity normalized cocycle relations (6.7).

## 8. Strongest current source-pinned proof graph

The present synthesis keeps all previously completed payments and replaces the newest r37 diffuse edge as follows.

Starting from the full target, current reductions may route to already-paid physical scalar/pair, finite-core, grouped-square/hub, ridge, third/fifth-cross-volume, and diffuse-carrier exits.  In the newest common-plane r37 chamber:

1. the pinned historical D5 theorem immediately pays any literal mixed cut with `e_5>=1/1024` by `<23.317`;
2. r37 gives either its physical heavy common two-arm anchor, or the diffuse three-fan (3.2)--(3.4);
3. on the diffuse branch, every ordered mixed fan cut has the exact Schur-minor lower bound (5.5);
4. if one Schur defect is at least `a_D^2`, the marginal-free physical `Z_3` receiver pays the entire quadratic form by `<32679.823`;
5. every still-unpaid diffuse state therefore lies in the simultaneous six-relation collar (6.7), and all compressed self/cross transitions there are invertible.

All random conditioning used by the cited physical receivers is on ORIGINAL coordinates.  Orthogonal frames in Sections 4--7 are used only to calculate deterministic matrix volumes and minors.

## 9. First unpaid universal implication after this run

The newest first edge is now

`QFORM-R37-HEAVY-OR-COHERENT-PLANARTWIST-PAYMENT-v1`.

Under the full owner hypotheses and the r37 common-plane survivor, prove a universal density bound in either of these two remaining source-valid states:

**H (heavy common physical anchor).**  There is one ORIGINAL coordinate `k in K` with

`||A[D_1,{k}]||_2 > a_H`,
`||A[D_2,{k}]||_2 > a_H`,
`a_H=0.0017696480672893325`,                                    (9.1)

while all arbitrary same-bank phases/outside couplings/extra spectrum remain.

**P (coherent diffuse planar twist).**  There are three disjoint ORIGINAL banks `K_1,K_2,K_3`, matrices `A_b,B_b,C_0,D_ab` as above, and for every ordered `a!=b`,

`s_2(A_b),s_2(B_b)>a_D`,

`||I_2-B_a^(-1)D_ab A_b^(-1)C_0||_op<a_D`,                     (9.2)

with `C_0,D_ab` invertible.  Pay (9.2) using a grouped `2+2+2` phase-weighted/Fresnel receiver, or show that the six near-identity relations force a previously paid original-coordinate pair/ridge/volume configuration.

The natural next mechanism is no longer another single-minor selection.  It is to exploit the simultaneous *cycle consistency* of the six normalized maps in (9.2), ideally by composing around `K_1->K_2->K_3->K_1` before inversion and using symmetry of the physical `K`-block.  This is precisely the information that the previous bare three-fan statement did not contain.

## 10. Scope and status

No valid QFORM counterexample was found.  The full target remains OPEN, arbitrary-extra-spectrum terms are retained throughout the new physical-cut payment, and global continuity remains a separate open issue.  This run is not a full proof candidate and therefore does not claim the two independent end-to-end reviews required for closure.

Model self-report: `GPT-5.6 Sol`.  Requested reasoning effort: maximum actually supported.  Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`.  Known actual reasoning effort: `UNKNOWN`.  Provider reasoning-token and pure-thinking-time counters were not exposed.  Wall-clock execution is recorded separately in the run receipt and is not pure thinking time.
