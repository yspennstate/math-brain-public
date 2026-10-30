SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-23T09:19:58.819315Z.
attacking: fleet02/B20 r25's unpaid double-coloop heavy-row state by an exact original-coordinate anchored mixed-discriminant disjointization.

# fleet01/B20 auto11 — heavy-row anchored two-bank volume

## Status

**ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN.**

The unrestricted target is unchanged: for independent real original coordinates with one-dimensional probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a dimension-free essential density bound for `Q=X^TAX`, or give a valid counterexample. This report does not close that theorem. Global continuity remains open as a separate stronger conclusion.

Fresh owner control at publication was QFORM-only, revision `2026-09-22.15`; no later B20 stop was present. The live corrections are retained: no law-uniform pointwise quadratic oscillatory decay, no independence after spectral rotation, no arbitrary-joint coarea shortcut, no conditional-cap-to-independence inference, no one-good-minor inference from aggregate mass, and no deletion of a small operator-norm remainder unless a proved receiver permits it.

Execution context remains `WITHOUT_VERIFIED_BRAIN`: repository reads/writes are transport and are not native learned-memory receiver use. Model self-report is GPT-5.6 Sol. Configured reasoning effort and provider reasoning/thinking counters are not exposed and remain `UNKNOWN/null`.

## 1. Completed partner actually consumed

The completed designated partner is fleet02/B20 r25:

- scientific source `yspennstate/math-open-problems@1ed18b869e338fb93f2cf0572928ab124d8e34aa`;
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260923T082458Z-fleet02-B20-QFORM-r25/REPORT.md`.

Its exact-rank-three state is

`A = R M R^T`, `R^T R = I_3`, `M=M^T`, `s_min(M)>=1`,                 (1.1)

where the rows `r_i^T` of `R` are indexed by the **original physical coordinates**. In the still-unpaid double-coloop state, r25 proves that there is a physical row `h` with leverage

`c := ||r_h||_2^2 > 1/2`.                                             (1.2)

This is the partner inequality spent below.

A second compatible source used only to identify the current frontier is fleet03/B20 r30:

- `yspennstate/math-open-problems@00f21a8efa65d29fc13bad8686edd1b7e7d1388d`;
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T084738Z-fleet03-B20-QFORM-r30/REPORT.md`.

Its remaining structural suggestion was a quantitative Hall/mixed-discriminant dichotomy for three packet Grams. The theorem below shows that, after repartitioning around the actual r25 heavy row, a fixed-scale anchored mixed discriminant is automatic. This removes that particular structural precursor; it does **not** by itself give the missing analytic density payment.

## 2. Exact anchored-volume identity

### Theorem `QFORM-HEAVYROW-ANCHORED-MIXED-DISCRIMINANT-v1`

Let `R in R^{n x 3}` satisfy `R^T R=I_3`, with physical rows `r_1,...,r_n in R^3`. Fix any row `h` and put

`c=||r_h||_2^2`.

Then

`sum_{i<j, i,j != h} det(r_h,r_i,r_j)^2 = c`.                         (2.1)

Consequently there is a deterministic partition of the residual **original-coordinate** set

`[n]\{h}=U disjoint_union V`                                          (2.2)

such that

`sum_{i in U, j in V} det(r_h,r_i,r_j)^2 >= c/2`.                    (2.3)

If in addition `A=RMR^T` with an invertible `3x3` matrix `M`, then for the same partition

`sum_{i in U,j in V} |det A[{h,i,j},{h,i,j}]|
   >= |det M| c/2`.                                                    (2.4)

In the actual fleet02/B20 r25 state (1.1)-(1.2),

`boxed: sum_{i in U,j in V} |det A[{h,i,j},{h,i,j}]| > 1/4.`         (2.5)

Moreover every nonzero summand in (2.4) has the common sign `sign(det M)` before taking absolute values.

### Proof

If `c=0`, (2.1) is immediate, so assume `c>0` and put

`e = r_h/sqrt(c)`.

Let `P=I-ee^T` be orthogonal projection onto the two-dimensional plane `e^perp`, and for `i != h` define

`b_i = P r_i in e^perp`.                                               (2.6)

Since `sum_i r_i r_i^T=R^TR=I_3` and `Pr_h=0`, projection on both sides gives the exact plane Parseval identity

`sum_{i != h} b_i b_i^T = P`,                                         (2.7)

which, after identifying `e^perp` with `R^2`, reads

`sum_{i != h} b_i b_i^T = I_2`.                                       (2.8)

Cauchy--Binet in this two-dimensional plane yields

`sum_{i<j, i,j != h} det_{e^perp}(b_i,b_j)^2
 = det(sum_{i != h} b_i b_i^T)
 =1`.                                                                  (2.9)

Because adding multiples of `e` to the second and third columns does not change a determinant containing the first column `sqrt(c)e`,

`det(r_h,r_i,r_j)
 = sqrt(c) det_{e^perp}(b_i,b_j)`.                                    (2.10)

Squaring (2.10) and summing (2.9) proves (2.1).

Now independently color each residual physical coordinate into `U` or `V` with probability `1/2`. Every unordered pair `{i,j}` is separated by the cut with probability `1/2`. Therefore

`E_cut sum_{i in U,j in V} det(r_h,r_i,r_j)^2
 = (1/2) sum_{i<j,i,j!=h} det(r_h,r_i,r_j)^2
 = c/2`.                                                               (2.11)

At least one deterministic physical cut attains at least the expectation, proving (2.3). No random variable has been rotated; the random coloring is only a deterministic existence proof for a partition of original coordinates.

For `S={h,i,j}`, let `R_S` denote the square `3x3` matrix consisting of those physical rows. The principal block of `A` is

`A[S,S]=R_S M R_S^T`,                                                  (2.12)

hence

`det A[S,S] = det(M) det(R_S)^2`.                                     (2.13)

Thus all nonzero principal triple determinants in this exact-rank-three representation have the same sign, and taking absolute values in (2.13), summing over the cut, and using (2.3) gives (2.4).

Finally, in the actual r25 state `s_min(M)>=1`, so every singular value of `M` is at least one and therefore

`|det M|>=1`.                                                          (2.14)

Together with the partner's actual inequality `c>1/2`, (2.4) gives

`sum_{i in U,j in V}|det A[{h,i,j},{h,i,j}]|
 >= |det M| c/2
 > 1/4`,                                                               (2.15)

which is (2.5). QED.

## 3. Mixed-discriminant formulation

Define the positive-semidefinite packet Grams

`G_h = r_h r_h^T`,
`G_U = sum_{i in U} r_i r_i^T`,
`G_V = sum_{j in V} r_j r_j^T`.                                       (3.1)

By multilinearity of the determinant, the coefficient of `x y z` in

`det(x G_h + y G_U + z G_V)`                                          (3.2)

is precisely

`sum_{i in U,j in V} det(r_h,r_i,r_j)^2`.                             (3.3)

Thus the partition from Section 2 has an anchored one-from-each mixed-determinant coefficient at least `c/2`, and in r25 it is strictly bigger than `1/4`.

This should be compared with the fleet03/B20 r30 frontier. That report needed a large-vs-small mixed-discriminant dichotomy for its pre-existing three packets. The present theorem shows that in the actual r25 heavy-row survivor one may **repartition the remaining original coordinates around the physical heavy row** and obtain the large alternative for free, at a fixed numerical scale independent of dimension. Hence the previous structural issue is replaced by a cleaner analytic one: spend this anchored mixed volume without losing product provenance.

## 4. Exact residual pair-volume structure

The same proof gives a useful normalized two-dimensional law. In the plane `e^perp`, put

`w_{ij}=det_{e^perp}(b_i,b_j)^2`, `i<j`, `i,j!=h`.                    (4.1)

Equation (2.9) says that `w` is a probability law on residual pairs. Its physical-coordinate inclusion marginal is

`q_i = sum_{j != i,h} det_{e^perp}(b_i,b_j)^2 = ||b_i||_2^2`.         (4.2)

Indeed, choosing an orthonormal basis in `e^perp` and using `sum_j b_jb_j^T=I_2`,

`sum_j det(b_i,b_j)^2
 = ||b_i||^2 tr(I_2) - b_i^T I_2 b_i
 = ||b_i||^2`.                                                        (4.3)

Thus the exact partner-heavy state has not only total anchored third-volume `c`; it carries a canonical physical residual pair-volume law whose marginals are the transverse leverages. For the chosen cut,

`sum_{i in U,j in V} w_{ij} >= 1/2`.                                 (4.4)

Equivalently, with plane Grams

`H_U=sum_{i in U} b_ib_i^T`, `H_V=I_2-H_U`,                          (4.5)

the cross pair-volume equals the two-dimensional mixed determinant of `H_U,H_V` and is at least `1/2`.

This is potentially the correct currency for a next mixed-order Brascamp--Lieb or grouped-slope receiver, because it is aggregate before reciprocal localization and remains entirely in original-coordinate banks.

## 5. What this proves, and what it does not

The theorem is a strict structural advance on the fleet02/B20 r25 first unpaid implication. From r25's single inequality `c_h>1/2`, it derives an **actual target-matrix inequality** at fixed scale:

`boxed: there is a physical anchor h and a physical cut U|V with
 sum_{i in U,j in V}|det A[{h,i,j}]| > 1/4.}`                         (5.1)

No dimension-dependent cardinality or leverage factor appears.

However, (5.1) is an aggregate bank statement. It does **not** justify selecting one determinant bounded below by a universal constant, since the number of pairs can grow with `n`. It also does not automatically feed the reviewed rank-three cross-block Theorem D: its determinants are principal triples sharing the anchor `h`, whereas Theorem D spends `3x3` minors of one physical cross block between disjoint row and column banks. Therefore no density cap is claimed solely from (5.1).

The first remaining implication is now

`QFORM-HEAVYROW-ANCHORED-MIXEDVOLUME-RECEIVER-v1`:

> Given the exact-rank-three physical state (1.1), a physical anchor `h`, and disjoint original-coordinate banks `U,V` with the anchored aggregate (5.1), prove a universal density bound while retaining arbitrary cap-one product laws and without treating the spectral coordinate `<e,X>` as an independent random coordinate.

A promising next split is expressed entirely through (4.5). If `H_U` and `H_V` both retain a quantitative second direction, use their pair-volume before any reciprocal minor localization. If one is nearly rank one, the identity `H_U+H_V=I_2` forces the other packet toward the complementary direction; the resulting anchored star-plus-transverse geometry should be routed to an already reviewed hub/two-bank receiver. This final analytic routing is not proved in this report.

## 6. Correction audit

- Full QFORM: **OPEN**.
- Global continuity: **OPEN**.
- New anchored-volume theorem: **PROVED algebraically** in its exact-rank-three scope.
- Fleet02/B20 r25 is applied to the explicit inequalities `c>1/2`, `s_min(M)>=1`, yielding the concrete `>1/4` target-matrix bound (2.15).
- No Gaussian, moment, iid, compact-support, connected-support or log-concavity assumption is introduced.
- Spectral coordinates are used only to describe the deterministic three-dimensional row frame. No independence after rotation is asserted.
- No law-uniform pointwise quadratic oscillatory estimate is used.
- No arbitrary-joint coarea estimate is used.
- No conditional-density cap is converted into independence.
- No one-large-minor conclusion is inferred from aggregate determinant mass.
- The cut is among original physical coordinates, so product provenance is preserved.

## 7. Keeper note

A fresh native scheduler inventory during this run showed the same twenty fleet01 QFORM assignments B01--B20, each present exactly once, enabled, hourly-valid, and quiet (`notifications=false`, `email=false`). No missing authorized task, duplicate, B21/B22, owner pause, or cadence defect was found, so the correct keeper action is **zero scheduler mutations**. Native task assignment is not being conflated with worker login or substantive-result state, and a missing login is not treated as an outage.
