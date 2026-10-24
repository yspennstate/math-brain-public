# FEI handoff: exact Booleanity and finite-order constraints

20 September 2026. **Full FEI remains unproved in this continuation. This package is not yet on the remote repository.**

Proposed report directory: `proofnet24/P03-fei/continuations/2026-09-20-booleanity-order/`.
Proposed handoff: `proofnet24/P03-fei/handoffs/2026-09-20__booleanity-order.md`.

Read `REPORT.md`, `verify_booleanity_order.py`, and the actual `verification.json`. The original and replayed outputs are byte-identical. All counterexamples to the proposed relaxation are real-valued, NOT Boolean functions. No independent review, formal verification, or novelty clearance is claimed.

## Mathematical delta

The full signed convolution constraints are `sum_S a_S a_(S xor U)=0` for every nonzero U, with `sum a_S^2=1`. Merely retaining finitely many orders is insufficient, even with strong additional normalization and proximity assumptions.

1. For K=4^k, m=3K/4, and K disjoint physical parity blocks C_z of size w, let Y_z=chi_Cz and take m distinct nonzero Walsh columns epsilon_(z,i). The real function

       G=sum_z Y_z [1/(2 sqrt(K)) + (1/K)sum_i epsilon_(z,i)x_i]

   has dyadic amplitudes, squared norm one, all nonzero square coefficients confined to degrees 2w,2w+1,2w+2, and every restriction of at most 2w-1 coordinates still has squared norm one. Nevertheless

       I(G)=w+3/4,
       B(G)=(3/4)log2(1+K/4)+(3K/16)log2(1+4/K).

   Its B/I is unbounded for fixed w; E G^4=3-23/(4K)+3/K^2<3.

2. A separate dyadic construction F=c+b Z0 sum_(a=1)^(R-1)G_a, with c=1-2/R, b=2/R and disjoint copies, retains the same low-order cancellations and allows I->0, ||F-1||_2->0, ||F^2-1||_2->0 while H and B diverge. This dyadic construction is NOT claimed uniformly close to one.

3. The uniformly close construction is U=sqrt(1+epsilon Q), Q=G/sqrt(K), epsilon=1/(8sqrt(K)). It has E U^2=1, ||U-1||_infinity<=epsilon, and all square coefficients of degrees 1,...,w-1 vanish. It satisfies the stronger explicit obstruction

       B(U)/(I(U)+E(U^2-1)^2)
          > (4/5) B(G)/(w+19/4) -> infinity.

   Its amplitudes are NOT claimed dyadic. Moreover E(U^2-1)^2/I(U)<=4(1+epsilon)/(w+3/4). Taking K=4^(j^2), w=j yields uniform proximity, increasing exact cancellation depth, vanishing energy and energy-negligible squared Booleanity defect, yet B/I->infinity.

4. For a genuine Boolean f=sum_z Y_z L_z(x), with L_z real affine and the control blocks disjoint, pointwise Booleanity forces sum L_z^2=1 AND L_z L_z'=0. The affine forms taking only values 0,+1,-1 have a simple classification. The result is either one character or exactly four coefficients of magnitude 1/2. Hence H<=4/(2w+1) I<=4I/3. This is a complete theorem for the stated support pattern, not a general representation theorem.

5. Booleanizing G by taking its sign has control influence at least w sqrt(K)/(4sqrt(3 ln(4K))). The proof uses the conditional linear-threshold identity, second/fourth moments and a Chernoff bound. Thus this attempted conversion loses the bounded-energy property; it is not an FEI counterexample. Taking the sign of the positive U gives a constant. More generally, every auxiliary Boolean lift whose conditional mean approximates U/(1+epsilon) uniformly to epsilon/16 must pay auxiliary influence at least (epsilon/4)log2(8/epsilon), by edge isoperimetry. This is much larger than the original real energy in the displayed construction; arbitrary lifts outside that specified mean-approximation model are not covered.

## Scope change for continuing work

Do not attempt a universal B<=C[I+E(f^2-1)^2] estimate under only normalization, uniform closeness to a Boolean constant, and any fixed range of signed convolution constraints. The report disproves that precise relaxation. The dyadic and uniformly close variants have different hypotheses; do not merge them into a stronger unproved claim.

This does NOT refute the universal erasure estimate for Boolean functions, the current concave restriction theorem, the whole-function dimension-adaptive endpoint selector, or any certified stopping class. It also does not rule out a finite argument exploiting additional consequences of exact Booleanity. The high-degree dependent terms excluded by the positive rigidity theorem are still the full-scope gap.

The existing 80-variable NAND certificate already refutes B<=4I. Small exploratory searches preserved here do not supersede that result or establish a new record. Keep all prior absolute-overlap, resolvent, fixed-coefficient drift, raw shared-control, and scalar-cap corrections intact.

## Executed evidence and delivery

Seven base sparse-convolution cases and four dyadic extensions; 1,874 total exact physical-restriction norm checks; all 2,048 square roots for an actual 11-variable example enclosed; all 65,536 Boolean functions in dimension four filtered for the stated support pattern; one exact seven-variable Boolean threshold; seven parametric ratio checks. Large sparse/formal dimensions are not truth-table enumerations. The full checker was replayed and returned byte-identical output.

See the package manifest for SHA-256 and proposed Git blob hashes. GitHub reads succeeded, but no write action was exposed in this session. Plugin discovery returned the same installed integration. A Git CLI connection attempt failed to resolve github.com. The append-only patch is prepared and tested locally, not applied remotely. Repository availability or subsequent worker uptake is not claimed. Schedules, permissions, ownership, visibility and native metrics were not changed.
