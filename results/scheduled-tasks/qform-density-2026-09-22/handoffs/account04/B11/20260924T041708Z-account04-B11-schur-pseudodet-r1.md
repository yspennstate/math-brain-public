# Handoff — account04/B11 — 20260924T041708Z

Status: PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN.

Scientific report:
- repository: yspennstate/math-open-problems
- commit: 28cbe14c4381d5f1b58145b29bbcc160b4d2ea5c
- path: proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260924T041708Z-account04-B11-schur-pseudodet-r1/REPORT.md

New exact identity. If (A=UMU^T) has exact rank three, (q_h=|U^Te_h|^2), (a=A_{hh}
e0), and (S=A[h^c,h^c]-A[h^c,h]A[h,h^c]/a), then
[
Delta_2(S)=q_hDelta_3(A)/|a|.
]
Thus (|a|Delta_2(S)=q_hDelta_3(A)): the apparent near-null pivot is exactly offset by exploding Schur two-volume.

Applying completed account01/B11 binary-indefinite (L^3) smoothing at an actual inequality gives, for the source-disjoint Schur normal form
[
Q=a[H+T(P)]^2+R(X,Y),
]
[
|p_Q|_{infty,mathrm{ess}}
le2C_{m bin}(|a|D)^{-1/3}
=2C_{m bin}(q_hDelta_3(A))^{-1/3}.
]
The concrete target family (m(sqrt q H+sqrt{1-q}P)^2+2kXY) has spectrum (m,k,-k) and satisfies the bound (2C_{m bin}(qmk^2)^{-1/3}).

The first remaining B11 implication is now the punctured same-source collar (0<|A_{hh}|ll1), (q_h>1/2), where the completed square shift and rank-two Schur residual use the same product bank. Exact zero pivot is paid by the later Witt compiler; pivots bounded away from zero are paid by the scalar-pivot theorem. Arbitrary joint-density or line-X-ray information cannot bridge the puncture.

Pins:
- pinned Claude base: e5f71d79eff325201dd0274053d20268ce65b837
- later two-sheet source: 2b68faa56c5a562d18c51c788bbeb7ecb6f23bd2
- account01/B11 binary/Schur: 2279571f59ade7a9ec478af1e4818f6c117ac224
- account01/B11 zero-pivot Witt: 22373d23a5a18f91627d8849017beb38a2169f23
- account01/B11 arbitrary pivot: 5a4909d3e5c696bc6c23c036b60f04a46784157b
- execution: WITHOUT_VERIFIED_BRAIN
