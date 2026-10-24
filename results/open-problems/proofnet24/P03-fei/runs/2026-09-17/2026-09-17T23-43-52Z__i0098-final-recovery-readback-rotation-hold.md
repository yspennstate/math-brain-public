Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.** The prompt requested GPT-6 / maximum, but the exposed runtime provides no authenticated model-family selector, reasoning-effort selector, or applied-routing receipt.

# P03 HARD OUTSIDE — I0098 final recovery completion, peer audit, and rotation hold

Date: 2026-09-17 UTC.  
Repository: `yspennstate/math-open-problems`, branch `master`.  
Target entering this run: **I0098 / Zauner SIC-POVM conjecture**, Randomstrasse 101 Conjecture 24.  
Canonical claim: `operations/claims/I0098.md`, creation commit `8d79f25bb64122621849dc579166b0d097c02fb7`, blob `bdd93549f588d8aae00cae2545ff8225ed716bf7`.

## 1. Metric / lifecycle first

Frozen source-matching finite metric:

`d_SIC^contig` = largest `D` for which exact published/certified SICs exist in every dimension `1 <= d <= D`.

**Before: 28. After: 28. NO MOVEMENT.**

The first exact-list gap remains `d=29`; exact `d=30,31` solutions are already literature-listed, so a complete exact d=29 certificate would move the metric at least to 31.

I0098 had already reached the three-unchanged-run HARD trigger. Recovery episode 1/2 produced Claim 260. The repository changed during the present scheduled execution: before I could lawfully duplicate the final-recovery write, current master already contained the complete immutable final-recovery handoff

`proofnet24/P03-fei/handoffs/2026-09-17T23-28-54Z__I0098-hard-handoff.md`,

creation commit `bc67ae83d7fc9f8ca7bb8883f9e8c95c8e057101`, blob `d2ab7106e7ff21116a75304f0a786c675b7b715e`.

That handoff consumes recovery **2/2**, contains the final Claim 262 and exact artifacts, and explicitly forbids a third I0098 recovery absent reassignment. I therefore continued from that newest state rather than creating a conflicting duplicate handoff. Current lifecycle state after this report is

`I0098_HANDOFF_COMPLETE / ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED`.

## 2. Continuity and source/status check

I reread/recovered the repository README, hourly protocol, current fleet/new-method rules, root queue, canonical I0098 claim, newest P03 report/handoff state, current task-health admission state, and the newest P04/I0101 report/artifacts needed for the directed audit. Several large root surfaces are connector-truncated; I used exact paths and current claim/status files and do **not** claim a byte-for-byte reread of every large ledger.

The source target remains the literal all-dimensional statement: an ETF of `d^2` unit vectors in `C^d` for every `d`. Weyl--Heisenberg or Zauner symmetry is only a sufficient subclass.

Fresh source recovery of Gene Kopp, *SIC-POVMs and the Stark Conjectures*, Conjecture 5.1, confirms that for odd prime `d == 2 mod 3`, with the one-infinite-place ray field `L_(d)∞2`, the predicted real Galois-conjugate units `alpha_{m,n}` satisfy:

1. `alpha_{-m,-n}=alpha_{m,n}^{-1}`;
2. `alpha_{m,n} == 1 (mod P)` for **every** prime ideal `P` of the ray field above `d`;
3. the roots of `(d+1)x^2=alpha_{m,n}` lie in the same ray field;
4. after choosing the unique root congruent to `1 mod P`, the Weyl--Heisenberg matrix assembled from those roots is rank-one idempotent.

Kopp explicitly separates (2)--(4) as additional predictions beyond the underlying rank-one Stark statement. His theorem proves SIC existence conditional on these properties; his exact worked cases are `d=5,11,17,23`, not 29. Appleby--Flammia--Kopp's later constructive program is likewise conditional on number-theoretic conjectures. No exact d=29 SIC was promoted from a numerical solution in this run.

Broad source status therefore remains **OPEN / PARTIAL**. The withdrawn Joka all-dimensional claim is not counted as a resolution.

## 3. Final recovery theorem retained from newest immutable state

The final recovery established

`P03-I0098-D29-LOCAL-SQUARE-CLASS-SWITCH-262 = PROVED / LOCAL-STRUCTURAL-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.

I independently rechecked the core local argument while reading back the handoff and exact artifact. The theorem is the following.

### Theorem 262 — exact d=29 local/global square-class switch

Let

`K = Q(sqrt(195))`, `epsilon = 14+sqrt(195)`, `theta=15+sqrt(195)`,

and let `L=L_(29)∞2` be Kopp's **one-infinite-place** ray class field.

Then:

1. `29` is inert in `K`; equivalently `O_K/(29) ~= F_(29^2)`. Indeed the relevant residue is `195 == 21 (mod 29)`, and `21^14 == -1 (mod 29)`, so 21 is a nonsquare.
2. Kopp condition (2) removes the entire local 29-adic square/sign obstruction in condition (3). If `P|29` in `L` and `alpha == 1 (mod P)`, then for

   `f(X)=30 X^2-alpha`

   we have `f(1)==0 (mod P)` and `f'(1)=60==2 (mod29)`, a unit. Hensel's lemma gives a **unique** root `nu_P in 1+P`. Conversely, a root satisfying `nu_P==1 (mod P)` forces `alpha=30nu_P^2==1 (mod P)`. Thus the local root/sign requirement and condition (2) are equivalent once viewed at the chosen 29-adic branch.
3. The global square requirement does not disappear. The identity

   `(15+sqrt195)^2 = 30(14+sqrt195) = 30 epsilon`

   shows that

   `(30 x^2=alpha has a solution in L)` iff `[alpha]=[epsilon] in L^x/L^{x2}`.

   Equivalently, `L(sqrt(alpha))=L(sqrt(epsilon))=L(sqrt(30))`.
4. This square class is genuinely nontrivial in the d=29 ray field. The biquadratic field `Q(sqrt195,sqrt30)` has quadratic-subfield discriminants `780,120,104`, hence the relative discriminant norm over `K` is

   `(120*104)/780 = 16`.

   Therefore `K(sqrt30)/K` ramifies above 2. Kopp's ray extension `L_(29)∞2/K` is unramified at finite primes away from 29, so it cannot contain `K(sqrt30)`. Hence `epsilon` is not a square in `L`.
5. This differs sharply from the solved d=23 analogue. There `K=Q(sqrt30)`, `epsilon_23=11+2sqrt30`, and `(12+2sqrt30)^2=24 epsilon_23`; the corresponding Kummer extension is finite-prime-unramified and lies in the Hilbert-class layer. The d=29 square-root step therefore cannot be copied verbatim from d=23.

The local conclusion is deliberately narrow: **there is no 29-adic Hensel/sign obstruction once Kopp condition (2) holds, but condition (3) remains a nontrivial global Kummer/2-Selmer problem.** This is PARTIAL and does not construct a d=29 SIC.

Exact artifact retained from the final recovery:

- checker: `proofnet24/P03-fei/artifacts/2026-09-17/d29_local_square_class_switch_check.py`, creation commit `dedd45b5f42d3876fd2387b22b46f7eb4edc2dd8`, blob `cc62dcf369030b6ae4f19da5544fcee646e85989`;
- output: `proofnet24/P03-fei/artifacts/2026-09-17/d29_local_square_class_switch_check.out`, creation commit `d5fb9652e015bae4d2a1a7bf7b46c9320b4f321b`, blob `8131351f4648140decaaacfd14a1d4b0c2172bef`.

The archived output records `29_inert_in_Qsqrt195=PASS`, `one_infinite_ray_kernel_order=280`, `finite_prime_inertia_order=280`, `d29_Kummer_relative_discriminant_norm=16`, `d23_Kummer_relative_discriminant_norm=1`, `hensel_fprime_at_1_mod_29=2`, and terminates `ALL_EXACT_CHECKS_PASS=True`.

## 4. Section-B methods and failure reading

This final recovery used exactly the assigned methods.

### B4 — prove something weaker, completely

Rather than claiming the Stark construction globally, Claim 262 completely proves the local 29-adic square/sign theorem and the exact global square-class reformulation. It cleanly separates what local class-field/Hensel information gives from what remains global.

### B22 — read the failures, not the successes

Kopp's paper itself identifies the key failure boundary: properties (2), (3), and (4) are additional predictions, and a p-adic route is suggested only as a possible way to establish at least (2). Claim 262 explains why this is not wording trivia: proving (2) automatically supplies the distinguished **local** root at 29, but cannot by itself prove the **global** square-class identity required by (3).

### B26 — hunt the sporadic case

Dimension 29 is arithmetically different from the preceding solved prime `d=23`. At d=23 the Kummer square class is absorbed by an unramified Hilbert-class extension; at d=29 the analogous Kummer extension has relative discriminant norm 16 and therefore ramifies at 2. There is no source-valid contradiction to Zauner here, but there is a rigorous reason the d=23 exactification template stops at the first d=29 exact-list gap.

## 5. Exact blocker and hard handoff state

The retained I0098 package is now:

- Claim 256: 280 Zauner-orbit reduction and exact nonnegative defect;
- Claim 258: cyclic ray/centralizer `C_280` bridge, with the warning that its both-real-places ray field must not be conflated with Kopp's one-infinite-place field;
- Claim 260: under exact cyclic Galois seed hypotheses, all WH idempotence equations propagate from one nonzero convolution equation;
- Claim 262: condition (2) kills the local 29-adic square/sign obstruction, while condition (3) is a genuinely nontrivial global square-class match, already detecting ramification at 2.

The simplest unproved special case at handoff is therefore:

> In Kopp's `L_(29)∞2`, construct a d=29 Stark unit `alpha` in the predicted Galois orbit and prove simultaneously `alpha==1 mod P` for every `P|29` and `[alpha]=[14+sqrt195]` in `L^x/L^{x2}`; then verify the one surviving WH convolution identity from Claim 260.

A future re-entry should attack this through d-adic Stark/Gross--Stark congruences plus an explicit 2-Selmer/Kummer calculation. It should not repeat orbit counting, the cyclic-280 bridge, or numerical PSLQ exactification.

Both HARD recovery episodes are consumed. **No third I0098 recovery is permitted without explicit reassignment.**

## 6. Directed P04 / I0101 second audit

I independently audited the newest accessible theorem-sized P04 claim not used in earlier P03 audits:

`P04-I0101-FRONTIER-4073-4157-32 = PROVED / FINITE-PARTIAL`.

Peer report:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T23-04-46Z__run-report.md`, creation commit `6251e05cecffec17f155ddd3132b0ef09bef3037`, blob `149fc24279e1123fac155f63c50e312386d9e4b9`.

Exact checker:

`proofnet24/P04-closure-local-paley/artifacts/2026-09-17T23-04-46Z__frontier_4073_4157_exact.py`, creation commit `700395b14ccd91a3500f64a03c0bec159abe7349`, blob `b37dd1454ee498e8f944aeed756e476ffb12ee40`.

Archived output:

`proofnet24/P04-closure-local-paley/artifacts/2026-09-17T23-04-46Z__frontier_4073_4157_exact.out`, creation commit `e78e4532f44d301a9dff2e1a7d6e53d870a0b956`, blob `3b059073dd80927403c68a11007e1ed5fb71ec1b`.

Audit ID:

`P03-AUDIT-P04-I0101-FRONTIER-4073-4157-263 = PASS (CLAIM-SCOPED)`.

### Independent argument

The complete admissible-prime set in `(4057,4157]` is exactly

`{4073,4093,4129,4133,4153,4157}`;

I independently regenerated this set by exact primality testing and the source congruence `p==1 mod4`.

For each listed prime, the checker builds the exact localized Paley graph, exact anharmonic `S_3` vertex/pair orbits, and an integer-scaled dual matrix `DB`. Floating spectral projection and Cholesky are proposal mechanisms only. Exact acceptance verifies the required fixed diagonal/edge entries and `S_3` invariance, then forms

`M_int = D(tI-B)`

and an exact residual representation

`M_int = L_q L_q^T / 1024^2 + 512 I + R_num/1024^2`.

The archive checks

`max_i sum_j |R_num(i,j)| < 512*1024^2 = 536870912`.

Because `R_num` is symmetric, its operator norm is bounded by that maximum absolute row sum. Hence

`512 I + R_num/1024^2` is strictly positive definite; `L_qL_q^T/1024^2` is positive semidefinite; therefore `M_int` and `tI-B` are strictly positive definite. The exact dual feasibility conditions then give `theta(overline G_{p,2}) < t`.

The source comparison is also exact. With `t=T/10`,

`t < (2/3)sqrt(p)` iff `400p-9T^2>0`.

The archived exact margins for the six cases are respectively

`3575, 3916, 2944, 4544, 4831, 6431`,

all positive. The residual-PD slacks are respectively

`395126872, 393851659, 386479564, 389918898, 378792327, 386072715`,

all positive. Thus each of the six finite cases is rigorously certified, and the complete frontier metric move `4057 -> 4157` is valid.

Scope limitation: this is a **finite frontier theorem**. It does not prove P04's asymptotic/eventual-prime source conjecture.

## 7. Mandatory rotation screen

After recognizing that I0098 was already immutably handed off on current master, I performed a fresh ownership/admission check rather than stealing an old queue row.

Current facts:

- `I0078`, formerly a freshly admitted READY/HARD reserve target, is now canonically claimed by C27.
- `I0028`, formerly READY/HARD reserve, is now canonically claimed by the HARD10-01 successor slot.
- `I0079`, also from that admission wave, is now canonically claimed by R06 (and is CLOSABLE, not a free HARD successor).
- The historical queue remains explicit that PENDING rows are not dispatch permission.
- `I0047` remains the nearest previously screened unclaimed historical HARD row but is `PENDING SOURCE NARROWING / NOT READY`; later FPP-on-PA literature resolves substantial broad clauses, and inventing a residual model/tail/observable would not be source-faithful.
- `I0060`, `I0062`, and other old HARD rows are still queue candidates, not currently certified READY/unassigned records in the present source/current-literature/ownership checkpoint.
- The newest coordinator status recovered in this run reports current HARD slots as occupied and does not establish a newly free READY/HARD successor. It also reiterates that stale historical READY rows are no longer free reserve inventory.

Therefore **no genuinely unassigned READY HARD OUTSIDE successor is certified in this run**. I created no successor claim and no successor metric.

Lawful next state:

`I0098_HANDOFF_COMPLETE / ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED`.

A future run should continue the admission cursor with exact primary-source/current-literature/history/ownership checks on newly replenished HARD rows rather than recycling I0098 or any handed-off predecessor.

## 8. `ledger_delta` for P26

```text
ledger_delta:
  P03 predecessor: I0098 / Zauner SIC-POVM Conjecture 24
  P03 metric: d_SIC^contig 28 -> 28
  P03 source status: OPEN / PARTIAL
  P03 final recovery: 2/2 CONSUMED
  P03 new retained claim: P03-I0098-D29-LOCAL-SQUARE-CLASS-SWITCH-262
  P03 handoff: COMPLETE at proofnet24/P03-fei/handoffs/2026-09-17T23-28-54Z__I0098-hard-handoff.md
  P03 third recovery allowed: NO absent explicit reassignment
  successor: NONE CERTIFIED
  next state: I0098_HANDOFF_COMPLETE / ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
  P04 audit: P03-AUDIT-P04-I0101-FRONTIER-4073-4157-263 = PASS (CLAIM-SCOPED)
  shared_root_ledgers_edited_by_P03: false
```

P03 edited no shared root ledger and no peer file.

## 9. Model control

The exposed task-control surface still has no binding model-family selector, no reasoning-effort selector, and no authenticated applied-runtime receipt. GPT-6 / maximum remains prompt-only. Permission boundaries must be handled only through the owning context or platform/admin/support; no duplicate task or bypass is appropriate.

**End of complete run report.**