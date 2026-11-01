Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy--Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the requested four-obligation candidate metric remains `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, the Hessian-null equations are converted into an exact nonnegative graph-flow system; that bare system is proved to have no obstruction whenever both active sign blocks have size at least two; a new two-coordinate global-face inequality couples local PSD to global majorization; and an exact `n=4` example proves that positive coefficients + exact contact + full PSD contact Hessian + cubic nullity + strict quartic positivity still do not imply a global certificate. Methods applied in new roles: #11 DUALIZE, #20 FIND WHY THE ALGORITHM FAILS, #4 PROVE SOMETHING WEAKER COMPLETELY.**

# R15 retained screen — graph-flow null equations versus global two-coordinate faces

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything newly proved below on Talagrand F0111 is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen I0076, make F0111 READY, establish publication novelty, solve Talagrand Problem 10.9, or satisfy the fleet two-independent-audit closure rule.

## 1. Continuity, source fidelity, ownership and exclusions

I continued from the immediately preceding immutable R15 report

`runs/R15/20260919_1634Z_successor_screen_f0111_unequal_nullcurve_z86t.md`

created at commit

`0b1ab9144715c51447e3019d28587f1f89ebd4a2`,

rather than restarting.

Before new mathematics I reread/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the controlling I0076 six-run handoff, the newest own R15 report, the neighboring F0111 handoff from R20, and the newest coordinator health report visible on `master` (`operations/task_health/runs/2026-09-19T165700Z/status.md`). The coordinator still records admission scarcity and `QUEUE.md` still records zero newly certified READY entries. I therefore did not steal an owned target, promote a PENDING row, or manufacture a successor claim.

### Exact I0076 source rechecked

Primary source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- FBM: there are random times `S_n -> -infinity` a.s. such that every complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there is one random time `S` at which the complete centered future and past are independent **standard Brownian motions**.

Problem 7.2 asks whether FBM + BBM plus existence of an arbitrary random time `T` for which

`(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

are independent as complete half-processes forces 2BM. The source does **not** assume `T` is a stopping time and does **not** separately assume either half at `T` is Brownian. Problem 7.5 is distinct and excluded.

The controlling I0076 six-run handoff remains unchanged. The source-Theorem-6.1 process has FBM, BBM and non-2BM but was eliminated as a source counterexample because it has no source-valid independent real seam. The later alternating Brownian-prefix/BES construction had exact seam independence but was proved to be 2BM. Thus no frozen counterexample candidate survives. The user's four-obligation candidate metric is therefore not honestly scoreable on a current candidate. The separate positive-route handoff metric froze at `2/4` after six unchanged runs and I0076 was operationally retired for reassignment, without claiming that the source problem was solved.

Fresh 2026-09-19 exact-title / author / arXiv / `Problem 7.2` searches recovered the original source and related Brownian splitting/pasting literature but no accessible later primary source explicitly claiming to resolve exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

### Retained F0111 current-literature check

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, Problem 10.9, and specifically the `k=2` threshold hazard. Fresh 2026-09-19 searches recover Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), which reformulates the discrete Convexity Conjecture via `k`-thresholds and proves substantial classes; Jinyoung Park, arXiv:2609.14681 (2026-09-13), which gives a dimension-free comparison explicitly described as progress toward the conjecture; and Fang--Wang, arXiv:2609.18458 (2026-09-16), which uses Chen Li's fractional result to answer another Talagrand problem. I found no accessible current source stating the graph-flow/face results below. Novelty remains `UNVERIFIED`.

### Section-B history

The preceding run used #18/#25/#7. Earlier R15/F0111 history already exhausted all 30 method numbers at least once, so I do not falsely claim globally unused numbers. This run uses a different nonconsecutive triple in new roles:

- **#11 DUALIZE** — rewrite Hessian-nullity as a nonnegative weighted-graph flow;
- **#20 FIND WHY THE ALGORITHM FAILS** — prove the bare flow equations are automatically solvable once both active sign blocks have size at least two;
- **#4 PROVE SOMETHING WEAKER COMPLETELY** — derive an exact pair-face compatibility inequality and use it to separate local feasibility from global majorization.

The analytic route was recorded before the formal exact checker in

`artifacts/R15/f0111_null_graphflow_face_idea_a87u.md`

at commit `e8b617ceda165098cbfcbb60fe1aee526dffdd68`.

---

## 2. Carried `k=2` setup

For

`F(t)=sum_i t_i-log S(t)`,

`S(t)=sum_i exp(t_i)-(n-1)`,                                  (2.1)

consider a nonnegative quadratic polynomial

`P(t)=sum_i A_i t_i + sum_{i<j} B_ij t_i t_j`,

`A_i,B_ij>=0`.                                                 (2.2)

At an interior exact contact `q`, put

`r_i = exp(q_i)/S(q)`.                                        (2.3)

Then

`partial_i F(q)=1-r_i`,                                      (2.4)

and

`H_F(q)=r r^T-diag(r)`.                                      (2.5)

If `P>=F` globally and `P(q)=F(q)`, the gap `G=P-F` has an interior minimum at `q`, so

`grad G(q)=0`, `H_G(q)>=0`.                                  (2.6)

The preceding R15 report classified the local derivative constraints for an unequal-amplitude mixed two-block null direction

`h=a 1_J-b 1_K`, `a,b>0`,                                    (2.7)

reducing cubic nullity plus strict quartic positivity to three scalar regimes after orientation. The question this run is whether the nonnegative coefficient equations themselves kill those regimes.

---

## 3. Method #11 — exact dual graph-flow form of Hessian nullity

Let

`p = sum_i r_i h_i`.                                         (3.1)

Because the Hessian of `P` has zero diagonal and off-diagonal entries `B_ij`, the equation

`H_G(q) h=0`                                                  (3.2)

is exactly

`boxed: sum_{j != i} B_ij h_j = r_i (p-h_i),  for every i.`  (3.3)

This is the correct local coefficient constraint. It is a weighted symmetric graph-flow problem, not merely a scalar moment condition.

For the two-block vector (2.7), let

`U=sum_{i<j, i,j in J} B_ij`,
`V=sum_{i<j, i,j in K} B_ij`,
`W=sum_{i in J, j in K} B_ij`,                               (3.4)

and

`x=sum_{i in J} r_i`, `y=sum_{i in K}r_i`.                   (3.5)

Summing (3.3) over the two active blocks gives

`2a U-bW = x(p-a)`,                                          (3.6)

`aW-2b V = y(p+b)`.                                          (3.7)

These identities are necessary for every Hessian-null global certificate.

### Both active blocks singleton is impossible on the cubic-null curve

Use the preceding report's normalized parameters

`a=m(1+delta)`, `b=m(1-delta)`, `p=m(delta+z)`,              (3.8)

with `0<delta<1`, and its exact cubic-null formulas for the aggregate weights `x,y`. If `|J|=|K|=1`, then `U=V=0`, so the two equations determine the same cross weight `W`. Their difference factors exactly as

`(delta+z)(delta+2z)(z-1)(z+1)`
`-------------------------------- = 0`.                      (3.9)
` (delta-1)(delta+1)(delta+3z)`

Positive `x,y` exclude `z=+-1` and `z=-delta`; the remaining root `z=-delta/2` lies in the gap between the two positive-weight intervals `(-(1+delta)/2,-delta)` and `(-delta/3,(1-delta)/2)`. Therefore there is **no positive-weight two-singleton Hessian-null candidate**.

If only `J` is singleton, then `U=0` and

`W = x(1-z)/(1-delta)`,                                      (3.10)

while (3.7) gives

`V = -(delta+z)(delta+2z)(z-1)(z+1)`
`    / [2(delta-1)^2(delta+3z)]`.                            (3.11)

Thus the positive-`C` surviving middle regime `z_*(delta)<z<-delta` has `V<0` and is impossible, and the `z>1` tail has `W<0` and is impossible. A `J`-singleton candidate can therefore survive the bare aggregate equations only in the `z<-1` tail. These are exact sign statements, not a numerical scan.

---

## 4. Method #20 — why the bare graph-flow attack fails when both blocks have size at least two

The hoped-for route was: combine (3.3) with `B_ij>=0` and eliminate all three scalar regimes. This route fails for a structural reason.

### R15-F0111-FLOW1 — automatic nonnegative solvability of the kernel rows

Let `h=a 1_J-b 1_K` with `a,b>0`, and assume

`|J|>=2`, `|K|>=2`.                                          (4.1)

For **arbitrary** positive numbers `r_i` and the corresponding `p=sum_i r_i h_i`, the row system (3.3) has a symmetric solution with

`B_ij>=0`, `B_ii=0`.                                         (4.2)

This statement concerns only the bare kernel rows. It does **not** assert gradient contact, coefficient-budget feasibility, positive semidefiniteness of the whole Hessian, or global majorization.

### Proof

Put

`g_i=r_i(p-a)` for `i in J`,
`g_j=r_j(p+b)` for `j in K`,                                 (4.3)

and write `m=|J|`, `ell=|K|`, `G_J=sum_J g_i`, `G_K=sum_K g_j`.

Choose a number `W>0` so large that all quantities below are positive. Define a common desired internal degree on `J` by

`s=(bW+G_J)/(am)`,                                            (4.4)

and cross row sums

`c_i=(as-g_i)/b`.                                             (4.5)

Then every `c_i>0` for sufficiently large `W` and

`sum_J c_i=W`.                                                (4.6)

Similarly define a common desired internal degree on `K` by

`t=(aW-G_K)/(b ell)`,                                         (4.7)

and cross column sums

`d_j=(g_j+bt)/a`.                                             (4.8)

Again all `d_j>0` for large `W` and

`sum_K d_j=W`.                                                (4.9)

Realize the internal `J` degrees by assigning every edge of the complete graph on `J` the weight `s/(m-1)`, and the internal `K` degrees by assigning every edge on `K` the weight `t/(ell-1)`. Realize the cross weights by the rank-one transport

`B_ij=c_i d_j/W`, `i in J`, `j in K`.                        (4.10)

Then each `J` row satisfies

`a s-b c_i=g_i`,                                              (4.11)

and each `K` row satisfies

`a d_j-b t=g_j`.                                              (4.12)

For a rest vertex `l` with `h_l=0`, equation (3.3) asks for

`a sum_{j in J}B_lj-b sum_{j in K}B_lj=r_l p`.               (4.13)

If `p>=0`, connect `l` to one fixed `J` vertex with weight `r_l p/a`; if `p<0`, connect it to one fixed `K` vertex with weight `-r_l p/b`. These rest edges do not change any active-row equation because `h_l=0` there. All remaining edges may be zero.

This constructs a symmetric nonnegative solution of (3.3). QED.

### Consequence

The three scalar null regimes from the preceding run **cannot** be eliminated, once both sign blocks contain at least two coordinates, by the nonnegative Hessian-kernel row equations alone. The missing information must come from one of:

1. the complete PSD constraint `H_G(q)>=0`, not merely `H_G(q)h=0`;
2. exact first-order/value contact and nonnegative singleton coefficients;
3. genuinely global majorization `P>=F`.

This is the precise failure mode of the graph-flow algorithm.

---

## 5. Method #4 — a global two-coordinate face inequality

The first global obstruction already appears on a two-coordinate face.

Fix distinct coordinates `i,j` and evaluate on

`t=s(e_i+e_j)`, `s>=0`.                                      (5.1)

For the `k=2` hazard,

`F(s(e_i+e_j))=f_2(s):=2s-log(2e^s-1)`.                     (5.2)

The quadratic polynomial restricts to

`P(s(e_i+e_j))=(A_i+A_j)s+B_ij s^2`.                        (5.3)

### R15-F0111-FACE1 — elementary lower envelope

For every `s>=0`,

`boxed: f_2(s)>=s^2/(1+s).`                                  (5.4)

Indeed

`f_2(s)=s-log(2-e^{-s})`.                                    (5.5)

Set

`g(s)=s/(1+s)-log(2-e^{-s})`.                                (5.6)

Then `g(0)=0` and

`g'(s)=1/(1+s)^2-1/(2e^s-1)>=0`,                             (5.7)

because `e^s>=1+s+s^2/2` gives

`2e^s-1 >= (1+s)^2`.                                         (5.8)

Thus `g>=0`, which is equivalent to (5.4).

### R15-F0111-FACE2 — local-PSD/global-face compatibility

Assume `P` is a global quadratic certificate exact at an interior base `q`. Then for every `i!=j`,

`boxed: B_ij <= [r_i+r_j-(r_i-r_j)^2]/2 <= 1`,               (5.9)

and

`boxed: A_i+A_j >= (1-sqrt(B_ij))^2.`                         (5.10)

Proof of (5.9): apply PSD of the contact Hessian to `e_i-e_j`:

`0 <= (e_i-e_j)^T H_G(q)(e_i-e_j)`
`   = r_i+r_j-(r_i-r_j)^2-2B_ij`.                            (5.11)

Since `0<r_i,r_j<=1`, the right endpoint in (5.9) is at most one.

Proof of (5.10): global majorization plus (5.4) gives, for every `s>0`,

`A_i+A_j >= s/(1+s)-B_ij s`.                                (5.12)

For `0<=B<=1`, the supremum of the right side over `s>=0` is exactly

`(1-sqrt B)^2`;                                               (5.13)

for `0<B<1` it occurs at `s=B^{-1/2}-1`, with the endpoint cases obtained by limits. This proves (5.10). QED.

This is a genuinely global constraint coupled to a local PSD capacity. It is invisible to the one-dimensional cubic/quartic null analysis and to the bare graph-flow rows.

---

## 6. Exact `n=4` stress test: all local conditions survive but the global face fails

The previous scalar classification left the outer regime `z>1`. I now give an exact point in that regime showing that **even the full local PSD condition does not eliminate it**.

Take

`delta=4/5`, `z=31/20`,                                      (6.1)

with two positive-block coordinates and two negative-block coordinates and no rest coordinates. The preceding cubic-null formulas give exactly

`x=39151/26160`,
`y=14993/8720`,
`k=-5797/2616`,                                               (6.2)

and because `C=-(n-1)=-3`,

`S(q)=7848/5797`.                                             (6.3)

The two block values are

`u=log(6909/6820)>0`,
`v=log(12267/10540)>0`,                                      (6.4)

so

`q=(u,u,v,v)`,
`h=(9/5,9/5,-1/5,-1/5)`.                                    (6.5)

The rational cubic/quartic factors are

`Q=-26367/43600`,
`R=3950752179/950480000>0`.                                  (6.6)

Consider the block-symmetric polynomial

`P(t)=alpha_J(t1+t2)+alpha_K(t3+t4)`
`    + beta_JJ t1 t2 + beta_KK t3 t4`
`    + T (t1+t2)(t3+t4)`.                                    (6.7)

Put `L=log(7848/5797)`. Exact value contact determines

`T = [1883520 L -430661 u^2 -2818872 u`
`     +20645361 v^2 -3238488 v]`
`    / [418560 (u+9v)^2].                                    (6.8)

Then Hessian-nullity gives

`beta_JJ = 430661/1883520 + (2/9)T`,                         (6.9)

`beta_KK = -764643/69760 + 18T`,                             (6.10)

while exact gradient contact gives

`alpha_J = 1-39151/52320-beta_JJ u-2Tv`,                     (6.11)

`alpha_K = 1-14993/17440-beta_KK v-2Tu`.                     (6.12)

These definitions make exact value and gradient contact algebraic identities. The null-row equations also hold identically in `T`.

The exact-rational interval checker described below certifies

`0.651<T<0.652`,
`0.373<beta_JJ<0.374`,
`0.757<beta_KK<0.758`,                                       (6.13)

`0.049<alpha_J<0.050`,
`0.008<alpha_K<0.009`.                                       (6.14)

Hence **every polynomial coefficient is strictly positive**.

The contact Hessian decomposes by block symmetry. Its two antisymmetric eigenvalues are

`lambda_J=r_J-beta_JJ`,
`lambda_K=r_K-beta_KK`,                                      (6.15)

where `r_J=39151/52320`, `r_K=14993/17440`. The remaining two-dimensional block-constant matrix has `h` as an exact null vector, so its other eigenvalue is its trace. The checker proves

`0.374<lambda_J<0.376`,
`0.102<lambda_K<0.103`,
`0.140<trace_block<0.142`.                                   (6.16)

Therefore

`boxed: H_G(q)>=0 and H_G(q)h=0.`                            (6.17)

So this point satisfies positive coefficients, exact value and gradient contact, full local PSD, Hessian nullity, cubic nullity and strict quartic positivity.

Yet it **cannot** be a global certificate. On the `J` pair, FACE2 requires

`2 alpha_J >= (1-sqrt(beta_JJ))^2`.                          (6.18)

With

`D_J=(1+beta_JJ-2alpha_J)^2-4 beta_JJ`,                     (6.19)

the checker proves

`boxed: 0.131 < D_J < 0.133.`                                (6.20)

Because `1+beta_JJ-2alpha_J>0` and `0<beta_JJ<1`, (6.20) is exactly the strict negation of (6.18). Thus the polynomial fails global majorization on the two-coordinate `J` face.

### What this example proves

This is not a counterexample to Talagrand and not a failed numerical candidate. It is an **exact structural counterexample to the local-only proof strategy**:

> Positive coefficients + exact contact + the full PSD contact Hessian with a nonzero null vector + cubic nullity + strict quartic positivity do not force a quadratic global majorant.

The remaining first-bifurcation problem is genuinely global. Any proof eliminating the scalar null regimes must import a global face/duality constraint such as FACE2 (or stronger), not merely more derivatives at the contact point.

---

## 7. Exact checker

After the analytic route was recorded, I executed an exact `fractions.Fraction` checker using rigorous rational intervals for logarithms obtained from

`log q = 2 atanh((q-1)/(q+1))`

and a rational positive-series tail bound.

Artifacts:

- checker: `artifacts/R15/f0111_null_graphflow_face_exact_a87u.py` @ commit `e6fc10d487301d77e41d07da4a593dde4929ad58`;
- archived output: `artifacts/R15/f0111_null_graphflow_face_exact_a87u.out` @ commit `ad3ac510c48ee20da1400a3c87b5d7c698941833`.

The executed output ends with the exact face contradiction and begins

`ALL_EXACT_CHECKS_PASS`.

The checker verifies exactly:

1. the rational scalar point and normalization;
2. the cubic-null and strict quartic factors;
3. rigorous rational intervals for `u,v,L`;
4. strict positivity of all five coefficient types;
5. the exact null-row identities;
6. strictly positive transverse/remaining Hessian eigenvalue margins, hence PSD with the desired null vector;
7. the strict polynomialized FACE2 violation `0.131<D_J<0.133`.

This is a self-check, not an independent audit.

---

## 8. What moved and the next obstruction

The native I0076 metric does **not** move. No Brownian candidate was revived or silently strengthened.

The retained-screen movement is exact:

1. the Hessian-null coefficient equations now have the graph-flow form (3.3);
2. the two-active-singleton case is eliminated exactly;
3. a `J`-singleton candidate is reduced to the negative-`C` `z<-1` tail;
4. if both active sign blocks have size at least two, the bare nonnegative graph-flow equations are always solvable, so that route is formally exhausted;
5. every global quadratic certificate satisfies the new pairwise local-PSD/global-face inequalities (5.9)--(5.10);
6. an exact `n=4` outer-tail example survives **all** local conditions including full PSD but violates the global pair-face inequality.

The highest-value next attack is therefore to combine, simultaneously,

- the null-flow rows (3.3),
- gradient/value contact,
- PSD pair capacities (5.9), and
- global face budgets (5.10)

into a finite-dimensional dual obstruction. Concretely, gradient contact writes

`A_i = 1-r_i-sum_{j != i} B_ij q_j`,                         (8.1)

so FACE2 becomes, for every pair,

`2-r_i-r_j`
` - sum_{k != i}B_ik q_k - sum_{k != j}B_jk q_k`
` >= (1-sqrt(B_ij))^2.                                       (8.2)

The next route should study (8.2) together with the null-flow equations as a capacitated nonlinear graph problem. If an extremal/compression argument reduces that system to two block levels, the scalar classification from the preceding runs becomes usable globally.

No closure label is changed.

---

## 9. Model / scheduler-control truth

This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so reasoning remains **UNVERIFIED**. I do not claim GPT-6 or verified maximum reasoning.

The task surface exposed to this worker still has prompt/title, schedule/timing, enabled state and ordinary update controls but **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution field**. GPT-6/maximum therefore remains prompt text in this interface. A real enforcement change requires a product/backend/API surface that exposes, persists and attests those routing settings.

The repository's implementation manifest records that P26 task ID `6aa7b43682948191b697d72fec69d539` once returned `You cannot modify this task` in one authorization context. The current `RESULTS.md` also records that a later authorized P/C context successfully updated P26. Thus the edit-denial workaround is the owning/authorized product or admin/API context, not task duplication or permission bypass. No scheduler or permission change was attempted in this run.

---

```yaml
ledger_delta:
  worker: R15
  source:
    id: I0076
    title: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, Problem 7.2"
    exact_scope: "FBM + BBM + independence of complete centered forward/backward half-processes at an arbitrary random T; decide whether 2BM follows"
    excluded: "Problem 7.5; deterministic-time substitutes; stopping-time strengthening; posted/settled work"
  native_metric:
    name: "number of four source-matching obligations proved for one frozen counterexample candidate"
    before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    movement: NO_MOVEMENT
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    historical_positive_route_metric: "2/4, frozen after six unchanged runs"
  successor_gate:
    before: 0
    after: 0
    unit: "newly certified free READY+CLOSABLE successors available to this bounded run"
    evidence: "QUEUE.md plus operations/task_health/runs/2026-09-19T165700Z/status.md"
  tried_moves:
    - "#11 DUALIZE — Hessian-nullity as a weighted nonnegative graph-flow system"
    - "#20 FIND WHY THE ALGORITHM FAILS — prove bare flow-row feasibility whenever both active blocks have size >=2"
    - "#4 PROVE SOMETHING WEAKER COMPLETELY — pair-face compatibility theorem and exact local-PSD/global-failure example"
    history_note: "all 30 method numbers were previously exhausted on the retained F0111 screen; this is a nonconsecutive triple used in new roles"
  retained_screen:
    id: F0111
    source: "Talagrand Problem 10.9, k=2 quadratic C_1 screen"
    disposition: "PENDING / NOT READY / SELF_CHECK_ONLY / NOT CLAIMED"
    movement:
      - "exact graph-flow kernel equation sum_j B_ij h_j = r_i(p-h_i)"
      - "automatic nonnegative row solvability if both sign blocks have size >=2"
      - "two-singleton null candidates eliminated; J-singleton reduced to z<-1"
      - "global pair-face theorem: B_ij <= [r_i+r_j-(r_i-r_j)^2]/2 and A_i+A_j >= (1-sqrt(B_ij))^2"
      - "exact n=4 local-PSD null candidate in z>1 branch fails pair-face globality"
  remaining_obligation: "combine null-flow rows, exact first-order/value contact, full PSD capacities and global pair-face budgets into a global dual/compression theorem; separately control the second-contact mechanism"
  evidence:
    idea_commit: e8b617ceda165098cbfcbb60fe1aee526dffdd68
    checker_commit: e6fc10d487301d77e41d07da4a593dde4929ad58
    checker_output_commit: ad3ac510c48ee20da1400a3c87b5d7c698941833
    checker_output: "ALL_EXACT_CHECKS_PASS"
  audit_ids: []
  closure: "NO — self-check only; no two independent audits"
```
