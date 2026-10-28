SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-23T17:20:58Z.
attacking: integrated Fourier estimate — remove the critical degree-4 volume-marginal gate by an original-coordinate hub cascade, and apply the newest account02/B02 marginal-free E3 theorem to an actual E4 inequality.

# account01/B02 r33 — marginal-free physical E4 Fourier compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE UNIVERSAL FOURIER-L1 OPEN_NOT_REFUTED / WITHOUT_VERIFIED_BRAIN**.

This run proves a new dimension-free, unweighted Fourier-L1 theorem for every actual original-coordinate physical cross block carrying nonzero fourth exterior volume. It removes the degree-4 row-marginal gate by cascading heavy volume marginals through one, two, three, and finally four literal physical hubs. The theorem does **not** prove that the bare three-large-eigenvalue hypothesis forces a uniformly large physical `E4`, so it is a supporting theorem rather than a full solution.

No Gaussianity, log-concavity, moments, compact support, connected support, identical laws, post-rotation independence, pointwise van der Corput decay, arbitrary-joint coarea cap, conditional-density supremum, fixed-good-minor inference, or deletion of a coefficient-small quadratic tail is used.

## 1. Fresh controls and source-pinned inputs

The canonical login for this actual hour already existed before this report and was not overwritten:

`math-research-brain:scheduled_tasks/status/account01/logins/2026-09-23T17Z/B02.json`, run id `20260923T172058Z-account01-B02-qform-auto11-r33`.


### 1.1 Designated partner actually applied

The newest completed `account02/B02` report consumed here is

`yspennstate/math-open-problems@3fccd9b82b456e198758e5839be364b4b0ec5024`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T170839Z-account02-B02-qform-auto11/REPORT.md`.

It proves for every original-coordinate physical cross block `M` with

`Z3=E3(M)=e3(M^T M)>0`

the marginal-free estimate

`||p_Q||_infinity <= 10.345084 Z3^(-1/6)`,

`integral_R |phi_Q(t)| dt <= 2 pi * 10.345084 Z3^(-1/6)`,

with a continuous `C0` density. Section 5 below applies this theorem to a concrete Maclaurin inequality relating `E3` and `E4`; this is the required partner-to-equation use.

### 1.2 Degree-4 sharp-Hausdorff--Young source

The designated-partner degree-4 checkpoint is

`yspennstate/math-open-problems@221e2d8972267cfffbb61e119d118f5011f8a265`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T153854Z-account02-B02-qform-fa558934/CHECKPOINT.md`.

For a physical cross block `B`, if its natural fourth-volume row marginals obey

`alpha_i^(4) <= q/2`, `q>=1`,

then the full ambient form obeys

`|phi_Q(t)| <= min(1,
  exp(2/q) q^(-1/q) pi^(2/q) E4(B)^(-1/(4q)) |t|^(-2/q))`.       (1.1)

When `q<2`, exact integration gives

`||p_Q||_infinity <= [2e/((2-q)sqrt(q))] E4(B)^(-1/8)`.          (1.2)

All same-bank quadratic phases, outside couplings and affine terms are retained.

### 1.3 Grouped projected-crossing receiver

The current owner continuation asks workers B01--B04 to apply

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For `k` literal hub coordinates and projected light crossing order `ell`, with `d=k+ell>2`, hub projection-density cap `M_H`, hub-to-light singular-value product `S`, projected crossing exterior volume `Z_ell`, and all natural `ell`-volume row marginals at most `1/2`, it gives

`||p_Q||_infinity <= [d/(d-2)]
  2^((k+3ell)/(2d)) exp(ell/(2d))
  M_H^(1/d) S^(-1/d) Z_ell^(-1/(2d))`,                           (1.3)

with the exponential omitted for `ell=1`, and with genuine `phi_Q in L1`. Internal hub functions, same-bank curvature, diagonals and affine terms are allowed. In this run every hub is a set of literal original coordinates, so `M_H<=1` without rotating random variables.

The same source's exact-rank crossing theorem gives, for `r` literal original hub rows and a rank-`r` cross block with Gram determinant `K`,

`||p_Q||_infinity <= [r/(r-2)] 2^(1/2) K^(-1/(2r))`.             (1.4)

For `r=4` this is `2 sqrt(2) K^(-1/8)`.

## 2. Exact incident-volume descent

Let `M=A[L,R]` be any ORIGINAL-coordinate physical cross block. Fix a literal row `i in L` and define its incident fourth-volume

`J_i^(4)
 = sum_{S subset L, |S|=4, i in S}
     sum_{T subset R, |T|=4} det M[S,T]^2`.                        (2.1)

Assume `J_i^(4)>0`.

For a selected literal hub-row set `H_s subset L`, `|H_s|=s`, put

`P_s=M[H_s,R]`,

and assume `P_s` has row rank `s`. Define the coefficient projection

`C_s=M[L\H_s,R](I-Pi_row(P_s))`,                                  (2.2)

and

`K_s=det(P_s P_s^T) E_(4-s)(C_s)`,                                (2.3)

for `s=1,2,3`. Cauchy--Binet plus Gram--Schmidt gives the exact identity

`K_s
 = sum_{S subset L, |S|=4, H_s subset S}
     sum_{T subset R, |T|=4} det M[S,T]^2`.                        (2.4)

Thus for `H_1={i}`,

`K_1=J_i^(4)`.                                                      (2.5)

### Heavy-marginal promotion identity

Let `ell=4-s`. For a residual literal row `a notin H_s`, its natural `ell`-volume marginal in `C_s` is

`mu_a = [sum of squared ell-minors of C_s incident to row a]
        / E_ell(C_s)`.                                             (2.6)

If `mu_a>1/2`, promote that literal row:

`H_(s+1)=H_s union {a}`.

Its component perpendicular to `row(P_s)` is the corresponding row of `C_s`, so `P_(s+1)` has full row rank. A second Gram--Schmidt/Cauchy--Binet identity gives

`K_(s+1) = K_s mu_a > K_s/2`.                                     (2.7)

No random variable is sheared; (2.2) is only coefficient algebra.

Iterating, if stages `1,...,s-1` all fail their `1/2` marginal gates, then

`K_s > J_i^(4) / 2^(s-1)`.                                       (2.8)

## 3. Main incident theorem — `QFORM-INCIDENT-E4-MARGINALFREE-L1-v1`

Under the exact target input assumptions, for every original-coordinate physical cross block and every literal row with `J_i^(4)>0`,

`boxed:
 ||p_Q||_infinity <= C14 [J_i^(4)]^(-1/8),`

`boxed:
 integral_R |phi_Q(t)| dt <= 2 pi C14 [J_i^(4)]^(-1/8),`

where

`C14 = 2^(9/4) exp(3/8)
     = 6.921144570127356... < 6.922`.                               (3.1)

The density therefore has a continuous representative vanishing at infinity.

### Proof

Condition only the original coordinates outside `L union R`; all remaining scalar coordinates retain independence and density cap one. Outside interactions become affine terms allowed by the source receivers.

**Stage 1: one literal hub, three projected crossing directions.**

Take `H_1={i}`. If every natural third-volume row marginal of `C_1` is at most `1/2`, apply (1.3) with

`k=1`, `ell=3`, `d=4`, `M_H<=1`, and `S^2 Z_3=K_1=J_i^(4)`.

This yields

`||p_Q||_infinity
 <= 2^(9/4) e^(3/8) [J_i^(4)]^(-1/8)
 = C14 [J_i^(4)]^(-1/8)`.                                        (3.2)

**Stage 2: two literal hubs, two projected crossing directions.**

Otherwise promote a heavy row. By (2.7), `K_2>J_i^(4)/2`. If every natural second-volume row marginal of `C_2` is at most `1/2`, apply (1.3) with `k=2`, `ell=2`, `d=4`:

`||p_Q||_infinity
 <= 4 e^(1/4) K_2^(-1/8)
 < 2^(17/8) e^(1/4) [J_i^(4)]^(-1/8)`,                            (3.3)

and

`2^(17/8)e^(1/4)=5.600958583346847... < C14`.

**Stage 3: three literal hubs, one projected crossing direction.**

If stage 2 fails, promote another heavy row, so `K_3>J_i^(4)/4`. If every one-volume row marginal of `C_3` is at most `1/2`, apply (1.3) with `k=3`, `ell=1`, `d=4`; the `ell=1` exponential is omitted:

`||p_Q||_infinity
 <= 2^(7/4) K_3^(-1/8)
 < 4 [J_i^(4)]^(-1/8) < C14 [J_i^(4)]^(-1/8)`.                   (3.4)

**Stage 4: four literal hubs / exact rank-four crossing.**

If stage 3 also fails, a residual row has one-volume marginal `>1/2`. Promote it to obtain `P_4` with

`K_4:=det(P_4P_4^T)>K_3/2>J_i^(4)/8`.                             (3.5)

Condition the remaining rows in `L` if desired and apply the exact rank-four crossing theorem (1.4) to the four literal hub rows against the still-independent column bank `R`:

`||p_Q||_infinity
 <=2 sqrt(2) K_4^(-1/8)
 <2^(15/8) [J_i^(4)]^(-1/8)`,                                    (3.6)

and `2^(15/8)=3.668016172818685...<C14`.

Every stage supplies a genuine unweighted `L1` characteristic-function estimate. Uniformity under the initial outside-coordinate conditioning passes the same bound to the unconditional characteristic function. This proves (3.1). QED.

## 4. Aggregate theorem — `QFORM-CROSS-E4-MARGINALFREE-L1-v1`

Let

`Z4=E4(M)=e4(M^T M)>0`,                                           (4.1)

and let

`alpha_i=J_i^(4)/Z4`.                                              (4.2)

Then `0<=alpha_i<=1` and `sum_i alpha_i=4`.

Fix `h` with `1/2<=h<1`.

If every `alpha_i<=h`, apply the degree-4 sharp-HY theorem (1.2) with `q=2h<2`:

`||p_Q||_infinity
 <= C_D(h) Z4^(-1/8)`,

`C_D(h)= e / [(1-h)sqrt(2h)]`.                                    (4.3)

If some `alpha_i>h`, Theorem 3 gives

`||p_Q||_infinity
 < C14 h^(-1/8) Z4^(-1/8)`.                                      (4.4)

Therefore

`boxed:
 ||p_Q||_infinity
 <= max{ e/[(1-h)sqrt(2h)], C14 h^(-1/8) } Z4^(-1/8),`            (4.5)

and the same coefficient times `2pi` bounds `integral |phi_Q|`.

Take the clean rational choice

`h=2/3`, `q=4/3`.                                                   (4.6)

The diffuse constant is

`C_D(2/3)=3 sqrt(3)e/2
         =7.06230335427344...`,                                    (4.7)

while the incident branch is

`C14 (3/2)^(1/8)
 =7.280971453882114...`.                                           (4.8)

Hence:

`boxed:
 ||p_Q||_infinity < 7.281 E4(M)^(-1/8),`                          (4.9)

`boxed:
 integral_R |phi_Q(t)| dt <45.748 E4(M)^(-1/8).`                  (4.10)

This is a marginal-free, unweighted integrated-Fourier theorem for **every** physical original-coordinate cross block of rank at least four. It has no leverage, stable-rank, support-shape, moment, or sign hypothesis.

For reference only, balancing the two branch constants numerically gives `h*=0.6788693686...` and coefficient `7.26449...`; no numerical optimization is needed for (4.9).

## 5. Newest account02/B02 result applied to an actual E4 inequality

This section is deliberately separate from the new direct E4 proof. It applies the designated partner's completed marginal-free E3 theorem to a concrete inequality, as required by the assignment.

Let the squared singular values of the same physical block be

`x_1,...,x_r>0`, `r>=4`.

Maclaurin's inequality for elementary symmetric polynomials gives

`(E3 / C(r,3))^(1/3)
 >= (E4 / C(r,4))^(1/4)`,                                         (5.1)

so

`E3 >= c_r E4^(3/4)`,

`c_r=C(r,3)/C(r,4)^(3/4)`.                                       (5.2)

Since `C(r,4)=C(r,3)(r-3)/4`,

`c_r^4
 = (32/3) * r(r-1)(r-2)/(r-3)^3
 >=32/3`.                                                          (5.3)

Thus, uniformly in rank,

`E3 >= c_infty E4^(3/4)`,

`c_infty=(32/3)^(1/4)=1.8072040072196895...`.                     (5.4)

Feed (5.4) into account02/B02's theorem:

`||p_Q||_infinity
 <=10.345084 c_infty^(-1/6) E4^(-1/8)
 <9.374 E4^(-1/8)`,                                                (5.5)

with `phi_Q in L1`.

So the newest designated partner already turns any positive physical `E4` into a marginal-free `E4^(-1/8)` estimate. The direct degree-4 cascade in Sections 2--4 improves the coefficient from `<9.374` to `<7.281` and isolates the exact critical mechanism at degree four.

There is also a direct use of the earlier account02/B02 two-sided D4-failure conclusion. If the `q=3/2` D4 gate fails in both orientations, their checkpoint gives a literal row `i` and column `j` with joint incident fourth-volume

`J4(i,j)>E4(M)/2`.                                                 (5.6)

Since the one-row incident volume satisfies `J_i^(4)>=J4(i,j)`, Theorem 3 yields immediately

`||p_Q||_infinity
 < C14 2^(1/8) E4(M)^(-1/8)
 <7.548 E4(M)^(-1/8)`.                                             (5.7)

Thus the old two-sided D4 star obstruction is now a paid unweighted-L1 branch.

## 6. Relation to the early r33 checkpoint

The early same-run checkpoint proved, after a two-sided D4 gate failure and writing the selected physical row/column decomposition

`B=[[b,r^T],[c,M]]`,

the non-divisive exterior inequality

`J4^(1/2)
 <= |b| E3(M)^(1/2) + ||r|| ||c|| E2(M)^(1/2)`,                  (6.1)

hence

`max{b^2E3(M), ||r||^2||c||^2E2(M)} > E4(B)/8`.                  (6.2)

That compression remains correct and useful coefficient currency, but the new incident-E4 cascade is strictly cleaner for the integrated-Fourier assignment: it pays the entire joint fourth-volume star without dividing by `b`, selecting a single minor, or needing an extra smoothing source beyond the current projected-crossing theorem.

## 7. Exact remaining gap

The full QFORM conjecture remains **OPEN**. The new theorem says:

`physical cross E4 at scale c >0  =>  universal Fourier-L1 at scale c^(-1/8)`.

Together with the newest partner result,

`physical cross E3 at scale c >0  =>  universal Fourier-L1 at scale c^(-1/6)`.

Therefore the Fourier pathway's structural debt has moved below rank four: the remaining target configurations can only evade these universal cross-volume receivers by having every useful physical cut carry very small `E3` (and hence very small `E4`), i.e. genuinely low-cross-rank / hub / diagonal / semidefinite geometry. The first unpaid implication for this slot is now

`QFORM-LOW-CROSSRANK-STRONGCUT-TO-INTEGRATED-RECEIVER-v2`:

connect the near-rank-one / near-rank-two strong-cut survivors, including the rough single-hub small-leak family, to a product-preserving grouped-hub/ridge/same-bank-curvature receiver with a **uniform** scale. The current projected-crossing theorem explicitly still deteriorates on the small-leak parameter in `Q_eps`; no claim is made that this has been closed.

No valid counterexample to the target-wide uniform

`integral_R |E exp(it X^T A X)| dt <= C`

was found. That stronger criterion remains **OPEN_NOT_REFUTED**. The new E4 branches prove continuity; unrestricted full-target continuity remains open.

## 8. Delivery / integrity notes

Changed-file allowlist for this mathematical repository write: only this run's own immutable `REPORT.md`. Manual privacy review found only mathematical formulas, repository/commit/path identifiers and run metadata authorized by the control; no credentials, signed URLs, unrelated personal data, financial/client material, or public-release action is present. No installation, remote workflow, scheduler mutation, email, notification, permission or visibility change was performed.

MODEL: GPT-5.6 Sol.
THINKING LEVEL: UNKNOWN / not exposed; requested standing preference = maximum actually supported.
THINKING USAGE: reasoning tokens NOT_EXPOSED; provider thinking time NOT_EXPOSED; coverage unavailable.
