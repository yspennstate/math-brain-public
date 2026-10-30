SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-24T04:00:00Z.
attacking: the newest fleet03/B20 r46 physical-hub alternative, by using its one-singular E3 gate on a GLOBAL original-coordinate cut containing every outside coupling; then stress-test the r46 three-cut gluing endpoint against exact target-valid four-bank constructions.

# fleet02/B20 r44 — globalize the r46 hub and obstruct over-compression of the three-cut carrier

Programme: `QFORM-DENSITY-3EIG-20260922`
Status: **ESSENTIAL STEP APPLIED / GLOBAL-HUB-R2-CUT FUNNEL / THREECUT-RANK8-OBSTRUCTION / FULL QFORM OPEN**.
Continuity: proved only on the explicit physical-E3 payment branches below; unrestricted continuity remains OPEN.
Execution: `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred, but no actual native learned-memory receiver ingestion was exposed).

The target is unchanged: for every n, independent original real coordinates with probability densities at most one, and every real symmetric A with at least three eigenvalues of modulus at least one, prove a universal essential-supremum bound for the density of X^T A X or give a valid counterexample. No Gaussianity, moments, log-concavity, compact/connected support, iid hypothesis, spectral-coordinate independence, post-rotation independence, arbitrary-joint coarea shortcut, fiber supremum, or law-uniform pointwise quadratic-phase decay is used. Every cut below is a literal partition of original independent coordinates. Small coefficient tails are retained; they are never deleted as random perturbations.

## 1. Fresh source graph and newest completed partner

The newest compatible completed designated partner at the source refresh is fleet03/B20 r46:

`yspennstate/math-open-problems@9ae7023224386e95ab2bd7f088347db8750c7b06`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260924T034736Z-fleet03-B20-QFORM-auto11-r46/REPORT.md`.

Its inherited strong-carrier chamber has disjoint original-coordinate banks R,C and

    N=A[R,C],
    dist_F(N,rank<=2)<2^-16,
    s2(N)>=1/64,
    s1(N)s2(N)>28159/(4194304 sqrt(2)).

The r46 theorem has two relevant outputs.

(1) In the heavy second-singular-vector alternative there is a literal physical coordinate j on one side with the opposite-bank arm

    ||A[R,j]||_2 >= 1/128                                      (1.1)

(or the transpose-symmetric version).

(2) Its new exact coefficient inequality `QFORM-ONE-SINGULAR-TO-R2-E3-v1` says for every real matrix M

    E3(M) >= (1/3) s1(M)^2 dist_F(M,rank<=2)^4.                (1.2)

The same report proves that, outside the heavy-arm alternative and already-paid E3 exits, its fully diffuse branch has a four-bank original-coordinate partition with

    A[H,H]=diag(A_1,A_2,A_3,A_4)+K+E_H,
    rank K<=12,
    ||E_H||_op<33/131072.                                      (1.3)

All four same-bank blocks and the coefficient tail E_H are retained.

The completed physical-E3 receiver used by r46 is fleet03/B04 r42:

`yspennstate/math-open-problems@563bc41e4f9247f9daf3343a57757f45e3f6e703`.

For every literal original-coordinate cross block M,

    ||p_Q||_infinity <= C_E3 E3(M)^(-1/6),
    C_E3=8.4530212255281768747049...,                           (1.4)

for the FULL ambient quadratic-plus-affine law, retaining arbitrary same-bank terms, outside couplings, signs and extra spectrum; this paid branch has a continuous C_0 density.

## 2. New theorem: one heavy arm globalizes to a whole rank-two cut

### Theorem 2.1 — `QFORM-R46-HUB-TO-GLOBAL-R2-CUT-v1`

Assume the r46 heavy-arm alternative (1.1). Let

    O=(R union C)^c,
    L=R union (C\{j}),
    J={j} union O,

so L and J form a literal partition of ALL original coordinates. Put

    W=A[L,J].                                                   (2.1)

Then

    s1(W)>=||A[R,j]||_2>=1/128.                                (2.2)

Fix

    eps=2^-12.                                                  (2.3)

There is an exhaustive dichotomy:

* either the FULL ambient law has a continuous C_0 density and

      ||p_Q||_infinity < 13098,                                (2.4)

* or the whole global physical cut is rank-two thin:

      dist_F(W,rank<=2)<2^-12.                                 (2.5)

#### Proof

The column of W indexed by j contains the physical subcolumn A[R,j], so (2.2) is immediate. Apply the newest partner's exact inequality (1.2) to the ACTUAL W. If (2.5) fails, then

    E3(W)
      >= (1/3)(1/128)^2 (2^-12)^4
      = 2^-62/3.                                               (2.6)

Now apply the completed marginal-free physical-E3 receiver (1.4) to this literal global cut. It gives

    ||p_Q||_infinity
      <= C_E3 (2^-62/3)^(-1/6)
      = C_E3 3^(1/6) 2^(31/3)
      = 13097.109458857976...
      <13098.                                                    (2.7)

The receiver is full-ambient and affine-uniform, so every within-L and within-J quadratic coefficient, including the entire outside block O and all extra spectrum, remains present. Its Fourier proof also gives continuity and vanishing at infinity on this branch. If (2.5) holds, no random perturbation is deleted; (2.5) is only the deterministic coefficient normal form for the next step. QED.

The transpose-symmetric heavy-arm alternative is identical after exchanging R and C.

### Why this is stronger than a local hub packet

The r46 heavy exit only certified one strong arm into the inherited carrier. The cut (2.1) deliberately puts every outside coordinate on the hub side. Thus any third direction that crosses between the old carrier and the outside world contributes to the SAME W. If it supplies enough aggregate rank beyond two, (1.2) turns it directly into E3 and pays the full law. A surviving heavy state therefore cannot hide arbitrary high-rank outside crossing curvature: the entire global cut is within Frobenius 2^-12 of rank two.

## 3. Required owner-pinned source spent on the same live cut

The required pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was read through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its proved unrestricted fifth-volume estimate D5 states that for any literal physical cross block M,

    ||p_Q||_infinity <= 5 sqrt(2e) e5(M^T M)^(-1/10),          (3.1)

with NO volume-marginal condition.

Apply (3.1) to the actual global W from (2.1). If

    e5(W^T W)>=1/1024=2^-10,                                  (3.2)

then

    ||p_Q||_infinity
      <=5 sqrt(2e) (2^-10)^(-1/10)
      =10 sqrt(2e)
      =23.316439815971243...
      <23.317.                                                  (3.3)

Hence every still-unpaid heavy-arm state may simultaneously assume

    dist_F(W,rank<=2)<2^-12,
    e5(W^T W)<1/1024.                                          (3.4)

This is an equation-level use of the requested e5f71... source on the current frontier, not a generic citation.

The same D5 check can be imposed on each of the three r46 balanced cuts in the fully diffuse branch; if any has fifth volume at least 1/1024, (3.3) pays the full law immediately.

## 4. Exact target-valid obstruction: three rank-two cuts do NOT force global rank <=6

The r46 diffuse endpoint naturally tempts one to improve its rank-12 gluing by a purely algebraic claim that three exact rank-two balanced cuts must yield a much smaller global off-diagonal rank. That fails already inside the exact target.

Let the coordinates be four physical banks A,B,C,D, each of dimension two, and define the 8 by 8 symmetric matrix

    A_*=(J_4-I_4) tensor I_2,                                   (4.1)

where J_4 is the all-ones 4 by 4 matrix. Thus every same-bank 2 by 2 block is zero and every off-diagonal bank block is I_2.

The scalar matrix J_4-I_4 has eigenvalues 3,-1,-1,-1. Therefore

    spec(A_*)={3,3,-1,-1,-1,-1,-1,-1},                         (4.2)

so A_* has eight actual eigenvalues of modulus at least one and satisfies the full QFORM spectral target strongly.

For any of the three balanced 2+2 bank cuts, after ordering the two banks on each side the physical cross matrix is

    [[I_2,I_2],
     [I_2,I_2]]
      =J_2 tensor I_2.                                         (4.3)

Hence every one of those three cross matrices has EXACT rank two and zero rank-two Frobenius defect. Nevertheless

    rank(A_*)=8.                                                (4.4)

Therefore the implication

    `three balanced physical cross matrices have rank <=2`
        => `global four-bank off-diagonal carrier has rank <=6`

is false, even with zero same-bank blocks and even under the exact full QFORM spectral hypothesis. A fortiori rank <=4 is impossible. This rules out a tempting repeated rank-compression mechanism for the r46 endpoint. It does NOT refute QFORM.

The pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A also pays this stress family rather than producing a QFORM counterexample: because n=8 and every eigenvalue of A_* has modulus at least sigma=1, its proved full-rank estimate gives

    ||p_{X^T A_* X}||_infinity
      <= (8/1)(7/6) kappa_7^(1/7)
      = (28/3) kappa_7^(1/7)<infinity,                          (4.5)

for every independent cap-one input law, with arbitrary linear terms allowed in that theorem. Thus (4.1) is a source-valid obstruction to an intermediate structural shortcut, not a counterexample to the owner target.

## 5. Strongest current conditional closure after this run

Combining the newest completed fleet03/B20 r46 result with Theorem 2.1 gives the following source-pinned frontier for its live chamber.

**Heavy-arm branch.** Either the full law is already continuously paid by `<13098` (and by `<23.317` whenever the D5 gate (3.2) holds), or there is a GLOBAL literal physical cut W satisfying all of

    s1(W)>=1/128,
    dist_F(W,rank<=2)<2^-12,
    e5(W^T W)<1/1024.                                          (5.1)

All outside couplings are included in W; no tail was dropped.

**Fully diffuse branch.** r46 already pays by `<30838` unless on its four original banks

    A[H,H]=diag(A_1,A_2,A_3,A_4)+K+E_H,
    rank K<=12,
    ||E_H||op<33/131072,                                       (5.2)

with arbitrary same-bank blocks retained. In addition, D5 lets an unpaid state assume fifth volume `<1/1024` on each of the three balanced cuts. The exact family (4.1) proves that the mere three-cut rank-two information cannot be compressed to a global rank-6 (or rank-4) carrier; the next mechanism must spend product structure / grouped smoothing, not repeat that algebraic shortcut.

Accordingly the first current unpaid implication is now

`QFORM-R46-GLOBAL-R2-SEPARATOR-OR-FOURBANK-R12-PAYMENT-v1`:

> Under the full original cap-one product hypotheses and target spectrum, pay either (5.1), a global strong-arm rank-two tube with every outside coupling retained, or (5.2), a four-bank rank-at-most-twelve inter-bank carrier with retained operator tail and arbitrary same-bank quadratic blocks; alternatively route either state to an already-proved physical pair, grouped hub/projected crossing, ridge/window, E3, E5, or principal-block receiver with every quantitative gate checked.

The target-valid obstruction (4.1) shows why a fourth unchanged attempt to lower the diffuse carrier rank solely from the three balanced cuts would be the wrong mechanism. The natural next move is analytic: exploit the independence of the four original source banks in the finite-rank inter-bank carrier, or use the global separator (5.1) to find the missing third smoothing resource without deleting its nonzero tail.

## 6. Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. No valid counterexample to the target was found. Full-target continuity remains **OPEN**. Pointwise-decay, fiber-supremum, conditional-cap, arbitrary-joint-coarea and post-rotation-independence shortcuts remain excluded exactly as in the live correction inbox.
