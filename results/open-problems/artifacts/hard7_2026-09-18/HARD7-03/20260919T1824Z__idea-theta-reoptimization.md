# HARD7-03 idea-before-code: parameter-uniform exact-pair envelope and theta reoptimization

Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum, and no maximum-reasoning claim is made.**

Active target remains canonical claim `D0025`, Seppäläinen 1999 Problem 4, frozen case `K=2`, `Q=(delta_{1/2}+delta_1)/2`. Carry-in certified metric is

`L = 2500000/29210369 = 0.0855860465165640... <= Delta_2(Q)`.

This note is exploratory and precedes the exact checker. It is not by itself a theorem certificate.

## Three routes for this run

### B3 — prove something stronger

The latest report solved the nonnested centre adjacent pair exactly only at the inherited rational Chernoff parameter `theta=723/1250`, but every ingredient of that calculation is actually parameter-uniform. The common-overlap envelope, the exact nested edge/near-edge transforms, and the full centre winner decomposition are all finite sums of rational functions of `theta` for `0<theta<1` (on the same six first-layer exponential order cones). Therefore combine them *before* selecting theta.

Define `q=1-theta`. Let `U_common(theta)` be the exact common-window four-step envelope from the 14:18Z checkpoint, with the previously proved mixed-sign/local-minimum triple corrections already included. Let

- `d_edge(theta)=P_edge-Q_edge`,
- `d_near(theta)=P_near-Q_near`,
- `d_center(theta)=P_center-Q_center`,

where the first two are the exact two-clock nested-pair gains and the last is the exact four-winner centre-pair gain. The proposed uniform all-pair envelope is

`U_exact(theta) = U_common(theta) - 4*(d_edge(theta)+d_near(theta)+d_center(theta))/q`.

The factor four is the same exact multiplicity already used in the immutable pair checkpoints: two reflected adjacent pairs of each class and two fourth-step predecessor windows per pair. At `theta=723/1250` this formula must reproduce the latest immutable value

`U_exact = 861.013982588807266...`.

That equality is the first consistency condition for the checker; if it fails, this route is abandoned rather than patched numerically.

### B5 — add/differentiate the Chernoff parameter

Once `U_exact(theta)` is available as a parameter-uniform exact envelope, the shape certificate at fixed theta is governed by

`A(theta) > log(U_exact(theta))/(4 theta)`.

A private scouting calculation (not a certificate) suggests the inherited `theta=0.5784` is no longer near-optimal after the full pair corrections: the objective drops from about `2.9210369` to about `2.9209113` near `theta≈0.57343`. The exact route is therefore to choose a simple rational theta near that point and certify a rational `A` directly by the one-sided truncated exponential series, avoiding any reliance on floating optimization.

Candidate exact values to test:

`theta_* = 57343/100000`,

`A_* = 36511391/12500000 = 2.92091128`.

The checker must prove with exact `Fraction` arithmetic

`U_exact(theta_*) < S_32(4 theta_* A_*) < exp(4 theta_* A_*)`,

where `S_32(x)=sum_{k=0}^{32} x^k/k!`. If successful, the already established block Chernoff/shape transfer gives

`G_1(0) <= A_*`

and hence

`Delta_2(Q) >= 1/(4 A_*) = 3125000/36511391`.

This is strictly stronger than the carry-in bound if the exact rational comparison passes.

### B20 — find why the algorithm still fails

Even if the theta reoptimization succeeds, it cannot solve Seppäläinen Problem 4. The full adjacent-pair loss at the four-step level is then removed, so the remaining four-step slack is no longer a pair-decoupling issue. It lies in the earlier deterministic inclusion/global-envelope treatment of triple and higher-overlap configurations, plus the finite four-block truncation itself. The checker should therefore report the decomposition `U_common`, exact pair gains, and final `U_exact`, so the next run can attack the largest *remaining* term rather than manufacture another certificate for the same pair correction.

## Refutation-oriented checks before accepting the route

1. Reconstruct `U_exact(723/1250)` independently from the parameter-uniform formulas and demand exact equality with the immutable 17:21Z rational.
2. Require each exact pair gain to be strictly positive at `theta_*`; a sign reversal would invalidate the claimed subtraction.
3. Require every order-cone Laplace denominator used by the formula to be strictly positive at `theta_*`.
4. Require the exact `S_32-U_exact` margin to be positive; no decimal/log comparison is allowed to certify the new `A_*`.
5. Compare `3125000/36511391` exactly to `2500000/29210369` before recording metric movement.

Only after these tests pass should code/output and a theorem-level run report be archived.