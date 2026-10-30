# Addendum — the entire B07 three-heavy-row O0 branch is already paid

The six-coordinate collar payment in `REPORT.md` can be strengthened substantially. No transpose localization is needed.

## 1. Input from fleet03/B07 r13

Fleet03/B07 r13, canonical

`yspennstate/math-open-problems@f2d3682e9f9d24d67ea14dc990d9f49bebeb5a6e`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T173711Z-fleet03-B07-qform-r13/REPORT.md`,

works in the O0 overlap branch with a disjoint physical cross block `B=A[L,R]` satisfying

`E=e_3(s(B)^2)>=1/256`.

When at least three row ridge leverages are at least `3/4`, its Theorem 4.1 produces a physical row triple `H subset L` such that

`det(B_H B_H^T)>=E/16>=1/4096`.                                  (1.1)

Equivalently, the aggregate three-dimensional cross volume of the physical triple `H` against the whole original-coordinate bank `R` satisfies

`s_H:=sqrt(det(A[H,R]A[H,R]^T))>=1/64`.                          (1.2)

## 2. Apply the completed B01 aggregate random-slope theorem directly

B01's completed `QFORM-RANDOM-SLOPE-CROSSMINOR-v1` report,

`yspennstate/math-open-problems@508b0985ba8bb658a7f6a935af5138a195cb89de`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260922T124907Z-b01-qform-auto11/REPORT.md`,

contains the following aggregate corollary. For any physical triple `I` and any disjoint original-coordinate bank `J`, let `C=A[I,J]` have row rank three and

`s=sqrt(det(CC^T))`.

The bounded-density projection theorem for the normalized three-dimensional projection of the independent coordinates in `J`, inserted into the exact random-slope Plancherel identity, yields

`||p_Q||_infinity <= 3 C_RV s^(-1/3)`,                            (2.1)

where `C_RV` is the universal one-dimensional-input projection constant from Rudelson--Vershynin. The characteristic function is integrable, hence the density is continuous and vanishes at infinity. Arbitrary self blocks on both sides and arbitrary outside couplings are retained by conditioning; no eigenbasis rotation of the independent inputs occurs.

Apply (2.1) with `I=H`, `J=R`. By (1.2),

`boxed( ||p_Q||_infinity <= 12 C_RV )`.                           (2.2)

Thus **every O0 configuration with at least three `3/4`-heavy row leverages is paid**, irrespective of the transpose leverage pattern. The later B07 split into transpose-diffuse versus three-heavy-column versus one/two-heavy-column subcases is unnecessary once the aggregate random-slope theorem is inserted.

The same conclusion holds if the three-heavy packet occurs on the column side, by transposing the symmetric cross block setup.

## 3. Why this is compatible with the correction inbox

`QFORM-CROSSMINOR-ALONE-FALSE` concerns a single curved `2x2` cross block. Here the currency is the **aggregate row-volume** `det(B_HB_H^T)=sum_{|T|=3}det B[H,T]^2`, and the three-dimensional product projection is averaged before any reciprocal determinant is paid. The Plancherel tail is `|t|^{-3/2}`, not the corrected borderline `|t|^{-1}` endpoint. No single `3x3` minor is selected.

## 4. Updated O0 residual

After fleet01/B04's effective-dimension-three diffuse payment and the argument above, the only O0 geometry still requiring synthesis is the B07 case with **fewer than three `3/4`-heavy coordinates on each relevant side**, i.e. the one-/two-heavy-coordinate aggregate skeleton carrying a fixed fraction of the third-volume currency. This is strictly narrower than the residual stated in B07 r13.

Full QFORM remains OPEN. Equation (2.2) proves a continuous density only on this O0 branch.
