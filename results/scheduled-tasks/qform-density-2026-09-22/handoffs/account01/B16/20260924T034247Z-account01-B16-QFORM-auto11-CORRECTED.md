SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B16, 2026-09-24T03:42:47.621071Z.
attacking: projection-product interaction in the majority-sign/mixed-volume endpoint.

# Corrected source-pinned handoff

Status: `ESSENTIAL_STEP_APPLIED / DUPLICATE_ANALYTIC_CLAIM_CORRECTED / NEW_LIVE_BRANCH_CLOSURE / FULL_QFORM_OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

**Use this handoff instead of the earlier same-run handoff.** The first `REPORT.md` remains immutable but its novelty classification is superseded.

Canonical corrected mathematics:
`yspennstate/math-open-problems@693038c0d6b33564a32bba0665e0b2b342236765:proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260924T034247Z-account01-B16-QFORM-auto11/SUPPLEMENT.md`.

Correction event:
`scheduled_tasks/work/shared/qform-density-2026-09-22/corrections/events/20260924T040112Z-account01-B16-duplicate-pairlog.json`.

## Correction

The first report's `QFORM-FRESH-HUB-CONDITIONAL-PAIRLOG-SQUARE-v1` is a scaled re-derivation/corollary of the pre-existing account01/B11 theorem `QFORM-OVERLAP-SAFE-SQUARE-LOG-v1` at
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260923T101016Z-account01-B11-QFORM-auto11/REPORT.md`.
It is mathematically valid but is **not** counted as a new analytic theorem.

## Substantive live-state advance after mechanism change

Newest compatible account03/B16 r39 source:
`yspennstate/math-open-problems@9bbe982a4824fa93b7daccd35a13c19cb0747d76`.
It constructs the strict target mixed-Pluecker family

`Q_bar,theta=theta H^2+2sqrt(2)HL+2P^2+4LS`,
`L=(X1-X3)/sqrt(2)`, `S=(X2+X4)/sqrt(2)`, `P=(X1+X3)/sqrt(2)`,

whose old absolute TT* kernel is infinite for interval laws despite mixed masses `1/2,1/2`.

Expand in original coordinates:

`Q_bar,theta=theta H^2+(X+Y)^2+2(H+Z)(X-Y)`,
with `X=X1`, `Y=X3`, `Z=X2+X4`.

Condition on `H=h` and set `W=h+Z`. Young gives `||p_W||_inf<=1`; conditional on `h`, `X,Y,W` are mutually independent cap-one scalars. Choose the indefinite pair `(X,W)`:

`B=[[1,1],[1,0]]`, `C=[1,-1]^T`, `D0=1`,
`det B=-1`, `kappa=(sqrt(5)-1)/2`,
`B^{-1}C=[-1,2]^T`,
`D0-C^T B^{-1}C=4`.

Hence exactly

`F=((X,W)+(-Y,2Y))^T B((X,W)+(-Y,2Y))+4Y^2`.

Applying the completed overlap-safe pair-log square theorem gives

`boxed: ||p_(Q_bar,theta)||_inf <=8(sqrt(5)-1)^(-1/4)=7.58716271595...<7.588`

for every real `theta` and arbitrary independent cap-one original laws.

Therefore r39's infinite absolute TT* kernel is a **mechanism barrier only**; the same sharp mixed-volume target family is uniformly paid by a source-preserving physical-pair completion. The remaining endpoint must evade this phase realignment as well as the old absolute TT* norm.

General canonical compiler/application: if conditional on outside data `X,Y,W` are mutually independent, `X,Y` cap one, `W` cap `K`, and

`F=lambda(X+Y)^2+2nu W(X-Y)`, `lambda nu !=0`,

then after scaling `W'=KW`, the pair matrix

`B_K=[[lambda,nu/K],[nu/K,0]]`

has

`kappa_K=(sqrt(lambda^2+4nu^2/K^2)-|lambda|)/2`

and exact Schur remainder `4lambda Y^2`. Existing B11 gives

`||p_F||_inf <=8 [K^2/(2|lambda|nu^2 kappa_K)]^(1/4)`.

This is a new structural compiler/application of an existing theorem, not a new analytic theorem.

## Designated partner actually applied

Newest completed account02/B16 partner source:
`yspennstate/math-open-problems@390bf6a9ad30195ba4011927c8218245d0e014be`, theorem `QFORM-PHYSICAL-HUB-DEFINITE-DISCRIMINANT-v1`.

For
`B_*=[[-1,1,0],[1,1,0],[0,0,1]]`,
`spec(B_*)={-sqrt(2),sqrt(2),1}`, `det B_*=-2`, hub diagonal `a=-1`, hence `a det B_*=2>0`. Thus

`||p_(-H^2+2HU+U^2+V^2)||_inf <=2sqrt(2pi)2^(-1/4)=4.2156294611...`

for a fresh cap-one hub and an orthonormal two-dimensional product projection `(U,V)` from a disjoint source bank.

## Remaining implication

`QFORM-PHASE-AWARE-MIXED-VOLUME-PAIR-OR-TTSTAR-v2` remains OPEN: in a generic majority-sign near-coloop survivor, either find an orientation/source partition that realigns the mixed phase to a quantitatively good indefinite pair plus scalar quadratic Schur remainder, or build a cancellation-preserving TT*/Hilbert receiver for the residual mixed-volume packet. A bounded projected joint density and total mixed Pluecker mass alone are insufficient.

Full unrestricted QFORM and global continuity remain OPEN.
