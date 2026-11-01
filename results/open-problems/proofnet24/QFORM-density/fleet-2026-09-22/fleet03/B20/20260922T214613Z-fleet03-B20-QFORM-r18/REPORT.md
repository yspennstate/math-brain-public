SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-22T21:46:13Z.
attacking: the heavy physical Schur-edge alternative left by the uniform-near-rank-one cut gluing, using a two-pivot/physical-triple dichotomy and the designated fleet04/B20 second-Schur closure.

# fleet03/B20 QFORM r18 — heavy Schur edge closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Classification:** `ESSENTIAL_STEP_APPLIED / STRUCTURAL BRANCH CLOSED / FULL TARGET OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Continuity:** not proved by this branch; only existence of an essentially bounded density is claimed.

## 1. Full target and correction boundary

The target remains the unrestricted statement: for every finite `n`, independent real coordinates with probability densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential-supremum bound for the density of `Q=X^TAX`, or produce a valid counterexample.

This run uses only original-coordinate conditioning and exact Schur identities. It does not rotate the independent source, use law-uniform pointwise quadratic-phase decay, assume a bounded conditional density after exposing a dependent statistic, select a uniformly good fixed minor from `s_3(A)>=1`, or apply an arbitrary-joint 3D coarea statement. The live correction ledger was refreshed after the derivation and does not refute the ingredients used below.

## 2. Fresh source-bound inputs

### 2.1 fleet02/B20 r18: the heavy-edge alternative

Source handoff: `math-research-brain@3bbe882a1095601d04d6ada8a36c3bb9b8e2d0cf`, path

In the retained physical-pivot branch there is an original coordinate `i` with

`|a|=|A_ii| >= m := 3501/8000`.

Let `O` be the remaining original coordinates and let

`S=A[O,O]-A[O,i]A[i,O]/a`

be the exact first physical Schur complement. One of the structural alternatives left by r18 is a **heavy physical Schur edge**: distinct `p,z in O` with

`|S_pz| > 1/8`.                                                   (2.1)

The purpose of this run is to pay (2.1) completely, without assumptions on the rest of `S`.

### 2.2 fleet03/B19 r18: sequential two-pivot theorem

Source handoff: `math-research-brain@f27c94cca288145b54f94c7e9cfad15a5cab9efd`; canonical mathematics recorded there as `math-open-problems@4caa949abfce263bcfdcdf7fe175a4a999ae35b5`.

If an original-coordinate principal pair

`B=[[a,b],[b,c]]`

has `a!=0` and second scalar Schur pivot

`d=c-b^2/a=det(B)/a !=0`,

then for `s_3(A)>=s>0`, arbitrary independent cap-one laws and arbitrary affine terms,

`||p_Q||_infinity <= [4sqrt(2)/sqrt(|ad|)]
  [2+log_+((5/sqrt(2))(|d|/s)^(1/4))].`                         (2.2)

The theorem is sign-uniform and retains the complete higher-rank remainder. Here `s=1`.

### 2.3 fleet03/B20 r15: physical-triple determinant theorem

Canonical source: `math-open-problems@c07c544cf5963360e66f9467c24c78f7a5aa53c6`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260922T184724Z-fleet03-B20-QFORM-r15/REPORT.md`.

For any three ORIGINAL coordinates `I={i,p,z}`, if `M=A[I,I]`, `a=M_ii!=0`, and `det M!=0`, then

`||p_Q||_infinity <=128 |a det M|^(-1/4).`                      (2.3)

This is an analytic payment for a source-valid physical triple; it does not assert that the global spectral hypothesis alone produces a good triple.

### 2.4 designated partner fleet04/B20

Canonical source: `math-open-problems@25ad8faaac5064b6814d51ae63d894fe97c1eac4`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260922T172057Z-fleet04-B20-QFORM-r3/REPORT.md`.

Inside its validated high-window first-pivot reduction, the selected second Schur row

`S=[[d,c^T],[c,C]]`

has inherited `|a|>=tau>=1/4`. Its cross-dominated unpaid state satisfies

`||c||_2>|d|`, `||c||_2>tau/9`,                                (2.4)

and the partner proves

`||p_Q||_infinity<5262`.                                        (2.5)

I use (2.4)-(2.5) only on that stated overlap.

## 3. New theorem — every heavy physical Schur edge is paid

### Theorem 3.1 — `QFORM-HEAVY-SCHUR-EDGE-CLOSURE-v1`

Assume the full target hypotheses, retain an original-coordinate scalar pivot `i` with

`|a|>=m=3501/8000`,

and form the exact first physical Schur complement `S`. If there are distinct residual physical coordinates `p,z` such that

`|e|:=|S_pz|>1/8`,                                                (3.1)

then `Q=X^TAX` has an essentially bounded density and, with the current archive constants,

`boxed: ||p_Q||_infinity <548.`                                  (3.2)

No condition is imposed on the signs of `a,S_pp,S_zz,e`, on the self blocks outside `{p,z}`, or on any remaining eigenvalues/couplings.

### Proof

Write

`d=S_pp`, `f=S_zz`, `e=S_pz`.

Set the scalar threshold

`r0=1/1024`.                                                       (3.3)

We split exhaustively.

#### Case 1: `|d|>=r0`

The original-coordinate principal pair `{i,p}` has first pivot `a` and exact second pivot `d`; in particular its determinant is `ad`. Apply (2.2) with `s=1` and `u=|d|`:

`F(u)= [4sqrt(2)/sqrt(|a|u)] [2+log_+((5/sqrt(2))u^(1/4))].`     (3.4)

Using `|a|>=m`, it is enough to bound the right side with `m` in place of `|a|`.

The logarithm activates at

`u0=(sqrt(2)/5)^4=4/625`,

and `r0<u0`. For `r0<=u<=u0`, (3.4) is simply proportional to `u^(-1/2)` and decreases. For `u>=u0`, write

`g(u)=u^(-1/2)[2+log((5/sqrt(2))u^(1/4))]`.

Then

`g'(u)=u^(-3/2)[-3/4-(1/2)log((5/sqrt(2))u^(1/4))] <0`,          (3.5)

because the logarithm is nonnegative in this range. Hence the global maximum over `u>=r0` occurs at `u=r0`, where `log_+=0`. Thus

`F(u)<=256 sqrt(2)/sqrt(m) <548.`                                (3.6)

The last inequality is exact after squaring:

`256^2*2 <548^2*(3501/8000)`.

#### Case 2: `|f|>=r0`

Use the original-coordinate pair `{i,z}` instead. Its exact second pivot is `f`, so the identical argument gives (3.6).

#### Case 3: `|d|<r0` and `|f|<r0`

Now the physical `2x2` Schur principal block on `{p,z}` has determinant

`Delta=df-e^2`.

From (3.1) and (3.3),

`|Delta| >= e^2-|df|
 > 1/64 - 1/1024^2
 =: delta0 >0.`                                                   (3.7)

Let `M=A[{i,p,z},{i,p,z}]`. The exact Schur determinant identity gives

`det M = a Delta`.                                                (3.8)

Therefore

`|a det M|=|a|^2 |Delta| > m^2 delta0`.                          (3.9)

Apply the physical-triple theorem (2.3):

`||p_Q||_infinity
 <128 (m^2 delta0)^(-1/4)
 <548.`                                                           (3.10)

The last inequality is checked exactly by fourth powers:

`128^4 <548^4*(3501/8000)^2*(1/64-1/1024^2)`.

Cases 1-3 are exhaustive, proving (3.2). QED.

## 4. Why this closes the fleet02/B20 heavy-edge branch

The heavy-edge alternative in fleet02/B20 r18 is exactly (3.1) after the same retained original-coordinate pivot `|a|>=m`. Theorem 3.1 therefore removes that branch completely. In particular, a heavy Schur edge is no longer an unpaid endpoint that must be aggregated over many coordinates: either one endpoint Schur diagonal itself is at least `1/1024` and the new sequential-two-pivot theorem spends the third spectral direction globally, or both endpoint diagonals are tiny and the edge forces a quantitatively nonsingular physical triple through (3.7)-(3.9).

This is a source-preserving dichotomy. It never treats Schur eigenvectors as new independent random coordinates.

## 5. Required fleet04/B20 result applied to an actual inequality

Consider the overlap where the heavy edge (3.1) lies in the **selected second Schur row of fleet04/B20's validated high-window setup**. Then its row vector satisfies

`||c||_2 >= |e| >1/8`.                                           (5.1)

If this selected row is cross dominated, `||c||>|d|`, the partner setup also supplies its inherited `||c||>tau/9`; hence (2.4)-(2.5) apply directly and give

`||p_Q||_infinity<5262.`                                         (5.2)

On the complementary selected-row alternative `|d|>=||c||`, (5.1) implies `|d|>1/8`. The sequential two-pivot theorem (2.2), with `|a|>=3501/8000`, gives the sharper current archive value `<67` (the B19 handoff records `66.3430374943...`). Thus the full heavy-edge selected-row overlap is paid from two independent existing-worker mechanisms.

This use of fleet04/B20 is intentionally scoped: (5.2) is not asserted for an arbitrary Schur row lacking the partner theorem's inherited high-window hypotheses. The general `<548` theorem in Section 3 does not need those extra hypotheses.

## 6. Consequence for the current structural frontier

Fleet02/B20 r18 had reduced its low-leverage survivor to a pivot-star possibility, a heavy-Schur-edge possibility, or a balanced two-bank aligned-hub possibility. The middle possibility is now closed by Theorem 3.1.

Thus the first remaining implication in that packet is now

`QFORM-PIVOTSTAR-OR-BALANCED-ALIGNED-BANK-PAYMENT-v1`:

pay either the physical pivot star `||A[i,O]||_2>1/8`, or the balanced residual hub with two disjoint arms of norm `>1/(8sqrt(2))` and its near-rank-one common bank, while retaining arbitrary self blocks and all remaining spectrum. One acceptable exit is to force another quantitative physical Schur pivot, because fleet03/B19 r18 now pays every such two-pivot state without a small ordinary singular-value loss.

The high-leverage augmented-bank packet and the arbitrary-self Frobenius matching problem remain separate global debts. The unrestricted QFORM conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**. The owner-requested universal continuity conclusion is also still open; this theorem establishes only an essentially bounded density in its branch.

## 7. Verification

`check_v2.py` contains only exact rational assertions for the two displayed `<548` constants and for `r0<4/625`. An equivalent same-run exact-arithmetic check terminated with

`QFORM_B20_R18_V2_CHECK_PASS`.

The computation verifies constants only; the proof is the analytic argument above.

## 8. Keeper / execution status

Fresh current-account inventory contained the same twenty managed fleet03 QFORM tasks. They were enabled, hourly-valid, nonduplicated, and quiet, and their native titles/prompts already matched the current source rollout. Under the account/hour keeper lease no scheduler mutation was needed: no task was created, restarted, rescheduled, disabled/enabled, or given email/push delivery.

Authenticated repository retrieval and writes occurred. Native receiver-memory ingestion was not established, so execution remains `WITHOUT_VERIFIED_BRAIN` and `full_brain_connected=false`.

Model self-report: `GPT-5.6 Sol`. Highest actually supported reasoning was requested. `reasoning_effort_configured=UNKNOWN`; provider reasoning-token and provider-thinking-time counters are not exposed and are therefore `null/UNKNOWN`, not zero.
