Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; there is still no surviving frozen counterexample candidate, so the original four-obligation candidate metric is not presently scoreable. The repository handoff’s post-switch `2/4` positive-route value remains frozen and is not reinterpreted as a live-candidate score. `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111 I prove an exact second-order SDP gate for every positive quadratic `C_1` contact; I then rigorously refute the preceding rank-one pair-mass candidate on a 16-coordinate two-level family while exhibiting a different positive quadratic contact that passes the complete local Hessian gate on the same family. Methods #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #14 FIND THE GROUP ACTING, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

# R15 retained screen — the quadratic contact SDP, a rank-one no-go, and a curvature-sparing replacement

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All new mathematics below is **SELF_CHECK_ONLY**. Nothing here reopens Burdzy–Scheutzow Problem 7.2 after its mandatory six-run handoff, promotes F0111 from `PENDING / NOT READY`, claims publication novelty, or satisfies the fleet closure/audit standard.

## 1. Continuity, source fidelity, and admission state

Before doing new mathematics I recovered the current campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, current coordinator status `operations/task_health/runs/2026-09-19T015000Z/status.md`, the controlling I0076 handoff

`runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`,

and the immediately preceding own report

`runs/R15/20260919_0157Z_successor_screen_f0111_secondfailure_dual_y71v.md`.

The coordinator status still records `E_READY_CLOSABLE: 0 -> 0`: no free, source-current, ownership-clear CLOSABLE successor is admitted. `QUEUE.md` likewise distinguishes sixty listed candidates from certified READY inventory and still reports zero newly certified READY entries. I therefore create no successor claim and touch no shared root.

I also rechecked the primary Burdzy--Scheutzow PDF itself, not a paraphrase. Definition 2.1 says:

- FBM: there are random times `S_n -> -infinity` a.s. such that each complete centered future from `S_n` is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there is one random time `S` at which the complete centered future and centered past are independent standard Brownian motions.

Problem 7.2 assumes only FBM + BBM and existence of an arbitrary random time `T` such that the two complete centered half-paths at `T` are independent. It does **not** say `T` is a stopping time and does not separately assume either half at `T` is Brownian. Problem 7.5 is distinct and remains excluded.

The six-run handoff remains controlling. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but no source-valid independent real seam. The later Brownian-prefix/BES candidate had FBM, BBM and an exact independent seam but was proved actually to be 2BM. Thus there is no surviving frozen counterexample candidate on which a third or fourth source obligation can honestly be counted. The handoff’s later `2/4` number is the post-switch positive-route gate metric, not a live score for either eliminated candidate.

A fresh dated exact-title / `Problem 7.2` web check again recovered the source and its citation trail but no accessible later primary source explicitly announcing a solution of exact Problem 7.2. That is bounded negative evidence only, not a worldwide openness certificate.

## 2. Carried retained screen: heterogeneous cardinality two

The retained pending screen is Talagrand, *Are Many Small Sets Explicitly Small?*, Definition 10.1 / Problem 10.9. For the cardinality-two threshold put

`F(t)=F_{n,2}(t)=-log P_t(|X|<2)`.

Writing

`T(t)=sum_i t_i`,
`S(t)=1+sum_i (exp(t_i)-1)=sum_i exp(t_i)-(n-1)`,             (2.1)

we have exactly

`F(t)=T(t)-log S(t)`.                                        (2.2)

Fix an interior base `q>0` and write

`r_i=exp(q_i)/S(q)`,
`z_i=q_i r_i`,
`m_i=q_i(1-r_i)`,
`D=sum_i m_i=<q,grad F(q)>`,
`W=D-F(q)`.                                                   (2.3)

The immediately preceding report proved SELF_CHECK_ONLY

`F(q) <= D <= 2F(q)`                                         (2.4)

and characterized the full positive degree-`<=2` **local** contact cone. A quadratic positive polynomial with contact masses

`a_i=alpha_i q_i`,
`e_ij=beta_ij q_i q_j`                                       (2.5)

has exact value and gradient contact at `q` precisely when

`a_i+sum_{j!=i} e_ij=m_i`,                                  (2.6)
`sum_{i<j} e_ij=W`,                                         (2.7)

with all `a_i,e_ij>=0`. This local cone is nonempty at every interior base. What remained was global majorization.

The previous report proposed the curvature-aligned **rank-one** point

`R_2=sum_{i<j} z_i z_j`,
`kappa=W/R_2`,
`e_ij^*=kappa z_i z_j`,
`a_i^*=m_i-kappa z_i(Z-z_i)`,  `Z=sum_i z_i`.                (2.8)

It was explicitly left conjectural. This run tests it exactly rather than grid-sampling it.

---

## 3. Method #30 — the exact second-order gate for any quadratic contact

A global majorant with exact interior contact has a local minimum of `P-F` at `q`. Thus its Hessian must be positive semidefinite. For quadratic multilinear `P`, this gives an exact finite-dimensional cone condition.

Use normalized coordinates

`t_i=q_i x_i`.

At `x=1`, (2.2) gives

`q_i^2 F_ii(q)=-q_i^2 r_i(1-r_i)`,                           (3.1)
`q_i q_j F_ij(q)=z_i z_j`,  `i!=j`.                         (3.2)

For the quadratic contact polynomial, the normalized mixed second derivative is exactly the pair contact mass `e_ij`, and the pure second derivatives vanish. Therefore the normalized Hessian of `P-F` at contact is the symmetric matrix

`M(e)_ii = d_i := q_i^2 r_i(1-r_i)`,                         (3.3)
`M(e)_ij = e_ij-z_i z_j`,  i!=j.                            (3.4)

### Theorem R15-F0111-SDP2 — necessary quadratic contact gate

If a positive quadratic multilinear polynomial globally majorizes `F_{n,2}` and has exact value contact at an interior base `q`, then its contact masses satisfy (2.6)--(2.7) **and**

`boxed: M(e) >= 0.`                                          (3.5)

This is only a necessary condition for global majorization, but it is exact and immediately falsifies candidate contact polynomials that pass all zeroth- and first-order tests.

There is also a useful direction-local theorem which does not require positivity.

### Lemma R15-F0111-FIBER — one-coordinate fibers can never be the failure

Let `P` be **any multilinear polynomial** with

`P(q)=F(q)`, `grad P(q)=grad F(q)`.

Fix all coordinates except `i` at their base values. Then for every `s>=0`,

`P(q_1,...,q_{i-1},s,q_{i+1},...,q_n) >=`
`F(q_1,...,q_{i-1},s,q_{i+1},...,q_n)`.                      (3.6)

Proof: multilinearity makes `P-T` affine in `s`, while

`d^2/ds^2 log S = r_i(s)(1-r_i(s)) >=0`.                     (3.7)

Hence `P-F=P-T+log S` is convex on that fiber. Its value and first derivative vanish at `s=q_i`, so `q_i` is its global minimum. QED.

Thus any failure of a contact polynomial must move at least two coordinates simultaneously. This is the exact “one direction at a time” reduction used below.

---

## 4. Methods #5 and #14 — a two-level family and the rank-one Hessian criterion

Introduce a parameter and a large symmetry group. Let

`b=log 2`, `m=14`, `n=m+2=16`,

and for `epsilon>0` define the interior two-level base

`q^(epsilon)=(epsilon,...,epsilon,b,b)`,                      (4.1)

with fourteen copies of `epsilon`. The base is invariant under `S_14 x S_2`.

For the rank-one contact (2.8), put

`delta=1-kappa`.

Whenever `delta>0`, (3.3)--(3.4) become

`M^* = diag(d_i+delta z_i^2) - delta z z^T`.                 (4.2)

Let

`A_i=d_i+delta z_i^2>0`.

Congruence by `diag(A_i^{-1/2})` gives

`A^{-1/2} M^* A^{-1/2}`
` = I-delta vv^T`, `v_i=z_i/sqrt(A_i)`.                      (4.3)

Therefore

`boxed: M^*>=0 iff delta sum_i z_i^2/(d_i+delta z_i^2) <=1.` (4.4)

This is an exact criterion, not a numerical test.

### The singular limit

As `epsilon ->0+`,

`S(q^(epsilon)) -> 3`,
`r_s ->1/3`, `r_b ->2/3`,
`z_s/epsilon ->1/3`,
`z_b -> 2b/3`.                                               (4.5)

Here `s` and `b` denote a small and a big coordinate. Also

`W -> W_0 := log 3 - 4b/3`,
`R_2 -> z_b^2=4b^2/9`,                                      (4.6)

so

`kappa -> kappa_0 := (9 log 3-12b)/(4b^2)`,
`delta -> delta_0:=1-kappa_0`.                              (4.7)

We need only crude **rigorous** bounds on `delta_0`:

`boxed: 3/19 < delta_0 < 1/2.`                               (4.8)

#### Proof of the lower bound in (4.8)

`delta_0>3/19` is equivalent to `kappa_0<16/19`, i.e.

`19(9 log 3-12b)<64b^2`.                                    (4.9)

The elementary bounds

`log 2>0.693`, `log 3<1.1`                                  (4.10)

are rigorous: for the first, the positive `atanh` series gives

`log2=2 sum_{k>=0} (1/3)^(2k+1)/(2k+1)`
`    >2(1/3+1/81+1/1215)=842/1215>693/1000`;                (4.11)

for the second,

`e^(11/10) > sum_{j=0}^5 (11/10)^j/j! >3`,                  (4.12)

so `log3<11/10`. Thus the left side of (4.9) is strictly below

`171(1.1)-228(0.693)=30.096`,                               (4.13)

while the right side is strictly above

`64(0.693)^2=30.735936`.                                    (4.14)

This proves the lower bound.

#### Proof of the upper bound in (4.8)

`delta_0<1/2` is `kappa_0>1/2`, equivalently

`W_0>2b^2/9`.                                                (4.15)

Since `3>2^(3/2)` (because `9>8`),

`log3>(3/2)b`,                                               (4.16)

hence `W_0>b/6`. Also `b<3/4`, since the first four nonzero terms of the exponential series give `e^(3/4)>2`. Therefore

`b/6>2b^2/9`,                                                (4.17)

which proves (4.15).

---

## 5. Exact refutation of the rank-one candidate

For any small coordinate in (4.1),

`d_s/z_s^2=(1-r_s)/r_s ->2`.                                (5.1)

Therefore its contribution to the left side of the rank-one PSD criterion (4.4) tends to

`delta_0/(2+delta_0)`.                                       (5.2)

There are fourteen such coordinates, so the contribution of the small-coordinate orbit alone tends to

`14 delta_0/(2+delta_0)`
` >14 (3/19)/(2+3/19)=42/41>1`.                             (5.3)

By continuity, for every sufficiently small `epsilon>0`,

`delta sum_i z_i^2/(d_i+delta z_i^2)>1`.                    (5.4)

Hence `M^*` has a negative eigenvalue. An explicit negative direction is obtained by taking `v=A^{-1}z` in (4.2): if `C=z^T A^{-1}z`, then

`v^T M^* v=C(1-delta C)<0`.                                 (5.5)

Since the base is interior, moving a sufficiently small amount in this direction stays in the positive orthant. Thus the rank-one contact polynomial lies **below** `F` in one of the two-sided local directions and cannot be a global majorant.

### The failure is not caused by coefficient signs

The rank-one contact remains a legitimate **positive** local contact for all sufficiently small `epsilon`; its failure is genuinely second-order.

Pair masses are positive because `kappa_0>0` (`W_0>0` follows already from `3^3>2^4`). For a small coordinate,

`a_s^*/epsilon -> 2/3 - 4 kappa_0 b/9`
` >2/3-4(1)(3/4)/9=1/3>0`.                                 (5.6)

For a big coordinate,

`a_b^* -> b/3-W_0 = 5b/3-log3>0`,                           (5.7)

because `5 log2>3 log3` is exactly `32>27`. Thus all singleton and pair coefficients are positive for small enough `epsilon`.

### Theorem R15-F0111-RANK1-NOGO

For `n=16` there are fully interior heterogeneous bases at which the curvature-aligned rank-one point (2.8) of the positive quadratic contact cone has nonnegative coefficients and exact value/gradient `C_1` contact, but **fails the necessary Hessian condition** and therefore does not globally majorize `F_{16,2}`.

This rigorously kills the concrete candidate isolated in the preceding run. No numerical grid is used in the theorem.

---

## 6. The quadratic route itself survives: a curvature-sparing contact

The rank-one failure suggests why the candidate was too rigid: it spreads the available pair mass proportionally across every pair, including many tiny coordinates whose diagonal curvature is only order `epsilon^2`. The group structure suggests preserving the exact cross curvature on edges incident to the tiny orbit and placing the pair-mass deficit on the robust big-big edge.

At the same two-level base define

`e_ss=z_s^2` for every small-small pair,
`e_sb=z_s z_b` for every small-big pair,                     (6.1)

and choose the one big-big pair mass by the contact budget

`e_bb=W-C(m,2)z_s^2-2m z_s z_b`.                            (6.2)

Then `sum e_ij=W` exactly. Define singleton masses by (2.6).

### Positivity for small `epsilon`

As `epsilon->0`, `e_bb->W_0>0`. For a small coordinate,

`a_s/epsilon`
` -> 2/3 - 4b/9`
` >1/3>0`,                                                   (6.3)

using `b<3/4`. For a big coordinate,

`a_b -> b/3-W_0=5b/3-log3>0`.                               (6.4)

Hence all contact masses are nonnegative for sufficiently small positive `epsilon`.

### Exact Hessian structure

By construction,

`M_ss=e_ss-z_s^2=0`,
`M_sb=e_sb-z_s z_b=0`.                                      (6.5)

Thus the Hessian gate is block diagonal: fourteen positive scalar blocks `d_s`, and a `2 x 2` big block

`[ d_b, e_bb-z_b^2 ; e_bb-z_b^2, d_b ]`.                   (6.6)

In the singular limit,

`d_b -> 2b^2/9 = z_b^2/2`,
`e_bb-z_b^2 -> W_0-z_b^2 = -delta_0 z_b^2`.                 (6.7)

Because `delta_0<1/2`, the smaller limiting eigenvalue is

`z_b^2(1/2-delta_0)>0`.                                     (6.8)

By continuity, (6.6) is positive definite for all sufficiently small `epsilon>0`. Therefore this curvature-sparing positive quadratic contact passes **all zeroth-, first-, and second-order necessary conditions** at exactly the family where the rank-one object fails.

### What this proves and does not prove

This does **not** prove a global `C_1` majorant. It proves a sharper structural fact:

1. the preceding rank-one candidate is false even locally at second order;
2. the positive quadratic contact cone is not itself killed by second-order geometry;
3. pair-mass placement matters, and the right local optimization is a fractional-graph-plus-SDP problem rather than a rank-one ansatz.

The next exact finite-dimensional object is therefore

`{ e>=0 : sum e=W, degrees(e)<=m, M(e)>=0 }`.                (6.9)

This is a convex intersection of the carried fractional-graph contact polytope with an explicit spectrahedron. Any global quadratic `C_1` certificate must lie in this set; the two-level construction proves the set can remain nonempty after the rank-one point exits it.

---

## 7. Why this is genuine movement and what route remains

The previous run ended with a single explicit rank-one contact candidate and two unproved obligations: coefficient signs and global majorization. This run settles that fork decisively:

- coefficient signs can hold while the candidate still fails;
- the failure is witnessed by an exact negative Hessian direction on an analytic two-level family;
- the failure is not evidence that degree two is impossible, because another group-adapted contact passes the exact Hessian gate;
- any contact polynomial is automatically safe on every one-coordinate fiber, so a genuine counterexample to global majorization must use a multi-coordinate direction.

The next route should therefore **optimize the spectrahedral contact cone globally**, not return to the rank-one point and not return to the already-sharp serial Pascal compiler. Natural next attacks are:

- #19 MAKE IT AN ALGORITHM: solve the group-quotiented contact SDP symbolically for two-level bases and derive a canonical edge-allocation rule;
- #6 DEFORM TO A POINT YOU CAN SOLVE: start from the homogeneous global `C_1` certificate, follow an SDP-feasible contact continuously under heterogeneity, and identify the first genuine global obstruction;
- #28 REPLACE FOR ALL WITH TYPICAL: determine whether the global quadratic certificate holds on an open dense set of bases before confronting the exceptional strata.

Full Talagrand Problem 10.9 is still untouched for `k>=3` and remains **PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED** in this retained screen.

No exact-arithmetic checker was created because the new retained claims are parameter-uniform analytic theorems with complete proofs on the page. A floating-point eigenvalue grid would add no certification and is explicitly not being substituted for the arguments above.

---

## 8. Current source and prior-art log

Dated 2026-09-19 searches covered:

- Burdzy--Scheutzow exact title and exact `Problem 7.2`, plus later/citing material;
- Talagrand exact `Problem 10.9`, `C_gamma`, and cardinality-threshold language;
- current 2026 discrete-convexity / `k`-threshold papers;
- log-sum / log-sum-exp quadratic support inequalities;
- heterogeneous second-failure / 2-out-of-`n` exponential reliability and cumulative-hazard inequalities.

Primary Talagrand source was re-opened and Problem 10.9 rechecked. Current adjacent literature recovered includes Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), Chen Li, arXiv:2609.08967 (2026-09-08), and Jinyoung Park, arXiv:2609.14681 (2026-09-13). Their retrieved statements concern the discrete-convexity / `k`-threshold and fractional-threshold programs; the bounded search did not surface an accessible source stating the exact contact-SDP criterion plus the rank-one no-go family above, nor a source explicitly resolving Talagrand's exact Definition-10.1 / Problem-10.9 positive-multilinear-majorant formulation.

The semidefinite second-order condition and rank-one downdate test are standard optimization / linear-algebra machinery. I therefore treat those mechanisms as folklore and record **publication novelty as UNVERIFIED**. Search failure is not priority evidence.

---

## 9. Model / scheduler / authorization boundary

The configuration limitation is unchanged. The exposed task-management surface provides task identity/title, prompt, schedule or relative-start fields, timing mode and enabled state. It exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed hour-long execution field**. Thus `Model: GPT-6. Reasoning: maximum` remains prompt text here, not an enforceable scheduler setting.

The historical P26 response `You cannot modify this task` is an authorization-context boundary, not evidence that the task is intrinsically immutable. Repository continuity separately records a later successful P26 update from an authorized P/C context. The lawful workaround for a future refusal is the owning/otherwise-authorized account, workspace, or owner/admin product/API/support surface for the **same** task. Duplicating the task, bypassing permissions, or pretending a repository edit changes native model routing is not a workaround. No scheduler or permission change was attempted in this run.

---

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), arXiv:1302.6958, Problem 7.2; intake I0076"
  target: "Decide whether FBM + BBM + source-exact independence of the centered half-processes at an arbitrary finite random real seam implies 2BM"
  fixed_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  metric_before: "no surviving frozen candidate; historical eliminated candidates diagnostic 3/4; post-switch handoff gate metric frozen 2/4"
  metric_after: "no surviving frozen candidate; no source-metric movement; post-switch handoff gate metric frozen 2/4"
  source_metric_movement: "none"
  status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  unchanged_count: "6 (frozen at mandatory retirement; not incremented during successor screening)"
  free_ready_closable_before: 0
  free_ready_closable_after: 0
  tried_moves:
    - "#5 ADD A PARAMETER AND DIFFERENTIATE IN IT"
    - "#14 FIND THE GROUP ACTING"
    - "#30 DO ONE SCALE / ONE DIRECTION AT A TIME"
  retained_screen: "F0111 Talagrand Problem 10.9; PENDING / NOT READY / SELF_CHECK_ONLY / NOT CLAIMED"
  retained_screen_movement:
    - "proved the exact Hessian spectrahedron M(e)>=0 necessary for every quadratic global contact"
    - "proved every exact multilinear contact is automatically a majorant on each one-coordinate fiber through the base"
    - "proved an analytic n=16 two-level family where the positive rank-one contact fails the Hessian gate"
    - "constructed on the same family a different positive quadratic contact that passes the full Hessian gate"
  remaining_I0076_obligation: "handoff blocker H: prove or disprove equality with 2BM on the full common-rerooting invariant sigma-field / construct a genuine relative-phase counterexample; do not reopen without reassignment"
  remaining_F0111_obligation: "turn an SDP-feasible quadratic contact into a global positive majorant, then address k>=3; rank-one candidate is now eliminated"
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260919_0157Z_successor_screen_f0111_secondfailure_dual_y71v.md"
    - "operations/task_health/runs/2026-09-19T015000Z/status.md"
    - "this immutable report"
  audit_ids: []
  closure_claimed: false
```
