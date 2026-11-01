Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; the retirement unchanged count remains frozen at `6`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, the heterogeneous `k=2` hazard now has an exact radial-elasticity theorem `1 <= <q,grad F(q)>/F(q) <= 2`, which in turn gives a complete characterization and constructive nonemptiness of its positive degree-<=2 **local** contact/budget cone at every interior base. Methods #1 CHANGE THE CATEGORY, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT.**

# R15 retained screen — second-failure reliability geometry and the local quadratic contact cone

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All new mathematics below is **SELF_CHECK_ONLY**. Nothing here reopens I0076, promotes F0111 from `PENDING / NOT READY`, claims publication novelty, or satisfies the fleet's closure/audit requirements.

## 1. Continuity, source fidelity, and admission state

Before doing new mathematics I recovered the operative repository state from the campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the current task-health reconciliation `operations/task_health/runs/2026-09-19T005400Z/status.md`, the controlling I0076 six-run handoff

`runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`,

the immediately preceding R15 report

`runs/R15/20260919_0056Z_successor_screen_f0111_sorted_pascal_x70t.md`,

the newest visible neighboring Burdzy--Scheutzow track report

`runs/R07/20260919T0125Z_i0077_gaussian_marginal_dependent_pair_gates_57_gd57.md`,

and the current F0111 admission sentinel

`proofnet24/NM13-12/runs/2026-09-19/2026-09-19T00-59-30Z__post-e0086-admission-delta-screen-11-f0111-adaptive-k2.md`.

The latter explicitly preserves F0111 as `PENDING / PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED`; pending is not READY. The current task-health pass also does not expose a newly certified free CLOSABLE successor for R15. I therefore create no ownership claim and touch no shared root.

The large append-only intake ledgers are not small enough for an honest claim that every historical byte was re-rendered through the connector in this invocation. I exact-target-recovered I0076 and its prior-attempt chain, and the current source/ownership surfaces show no source-identity change. I do not treat a search miss or absent claim file as proof of free ownership.

The primary Burdzy--Scheutzow PDF was rechecked directly, including Definition 2.1 and Problem 7.2. The source says:

- FBM: there are random times `S_n -> -infinity` a.s. from which the complete centered future is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there is one random time `S` for which the centered future and centered past are **independent standard Brownian motions**;
- Problem 7.2 assumes FBM + BBM and existence of an arbitrary random time `T` such that the two complete centered half-paths at `T` are independent, and asks whether this forces 2BM.

There is no stopping-time assumption on `T`. Neither seam half is separately assumed Brownian. Problem 7.5 is distinct and remains excluded.

The six-run I0076 handoff remains controlling. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but no source-valid independent seam. The later Brownian-prefix/BES candidate had FBM, BBM and exact seam independence but was proved actually to be 2BM. Hence there is no live frozen counterexample candidate on which a third or fourth source obligation can honestly be counted. The historical `2/4` is a retirement value for the positive-route metric, not the score of a currently viable counterexample.

Fresh exact-title / exact-Problem-7.2 searches dated 2026-09-19 recovered the original paper and related citation pages but no accessible later primary paper explicitly announcing a resolution of exact Problem 7.2. That is bounded negative evidence only, not a worldwide openness certificate.

## 2. Retained screen: the heterogeneous cardinality-two hazard

The retained pending screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, Definition 10.1 / Problem 10.9. For independent coordinates with inclusion probabilities `1-exp(-t_i)`, write

`F_{n,k}(t)=-log P_t(|X|<k)`.

Talagrand's `C_gamma` condition asks, at every base `q>=0`, for a multilinear polynomial with nonnegative coefficients and zero constant term which globally majorizes `F_{n,k}` and obeys the scaled budget at `gamma q`. Problem 10.9 asks for one universal `gamma>0` across all `n,k` and all bases.

This run only studies `k=2`. Put

`T(t)=sum_i t_i`,
`S(t)=1+sum_i (exp(t_i)-1)=sum_i exp(t_i)-(n-1)`.

Then exactly

`F(t):=F_{n,2}(t)=T(t)-log S(t)`.                              (2.1)

At an interior base `q>0`, set

`S=S(q)`, `r_i=exp(q_i)/S`.

Then

`F_i(q)=1-r_i`,                                               (2.2)

and for distinct `i,j`,

`F_ij(q)=r_i r_j`,                                            (2.3)

while

`F_ii(q)=-r_i(1-r_i)`.                                       (2.4)

The preceding R15 work already proves SELF_CHECK_ONLY global `C_1` on homogeneous and flat-support bases, the exact endpoint `C_1` theorem, heterogeneous serial compilers, and the sharp `1/(n-1)` worst-case obstruction for the **entire serial compiler architecture**. This run leaves that architecture.

---

## 3. Method #1 — CHANGE THE CATEGORY: `F(tq)` is the cumulative hazard of a second failure

Fix an interior or nonnegative vector `q=(q_1,...,q_n)` and let independent component lifetimes satisfy

`tau_i ~ Exp(q_i)`.

Let `T_(2)` be the second component-failure time. The event `T_(2)>t` means that at time `t` either no component has failed or exactly one has failed, so

`P(T_(2)>t)`
` = exp(-Q t) [1+sum_i(exp(q_i t)-1)]`,                       (3.1)

where `Q=sum_i q_i`. Therefore its cumulative hazard is exactly

`H(t):=-log P(T_(2)>t)=F(tq)`.                               (3.2)

This makes the radial geometry of Talagrand's `k=2` hazard a reliability problem about a heterogeneous 2-out-of-`n` failure system.

### Theorem R15-F0111-ELASTIC2 — radial elasticity lies in `[1,2]`

For every `q>=0` with `F(q)>0`,

`boxed:  1 <= <q,grad F(q)>/F(q) <= 2.`                      (3.3)

Equivalently, for `H(t)=F(tq)` and every `t>0` with `H(t)>0`,

`H(t) <= t H'(t) <= 2 H(t)`.                                (3.4)

The lower inequality is the carried IFRA/radial-sublinearity fact from the preceding R15 prior-art transfer. The new part is the upper inequality.

### Proof of the new upper inequality

Write

`x_i(t)=exp(q_i t)-1`,
`A(t)=1+sum_i x_i(t)`,
`c_i=Q-q_i`.

Differentiating (3.2) gives the system hazard rate

`h(t):=H'(t)=N(t)/A(t)`,                                    (3.5)

where

`N(t)=sum_i c_i x_i(t)`.                                    (3.6)

Introduce weights

`w_0=1/A`, `w_i=x_i/A`,

and values

`c_0=0`, `d_0=0`,
`d_i=x_i'/x_i=q_i/(1-exp(-q_i t))`                           (3.7)

for positive `q_i` (zero-rate coordinates are obtained by continuity). Then `sum_a w_a=1`,

`h=sum_a w_a c_a`,

and direct differentiation of a weighted mean yields

`h'=Cov_w(c,d)`
`  =sum_{a<b} w_a w_b (c_a-c_b)(d_a-d_b)`.                  (3.8)

For `i,j>=1`, the map

`q -> q/(1-exp(-q t))`

is increasing in `q`, while `c_i=Q-q_i` is decreasing in `q_i`. Hence every positive-positive pair term in (3.8) is nonpositive. Only the `0-i` terms can be positive, so

`h'(t) <= w_0 sum_i w_i c_i d_i = N'(t)/A(t)^2`.             (3.9)

Now, term by term,

`t q_i exp(q_i t) <= A(t)(exp(q_i t)-1)`.                   (3.10)

Indeed `q_i t <= exp(q_i t)-1` and `A(t)>=exp(q_i t)`. Multiplying (3.10) by `c_i>=0` and summing gives

`t N'(t) <= A(t)N(t)`.                                      (3.11)

Combining (3.9)--(3.11),

`t h'(t) <= h(t)`.                                          (3.12)

Thus `h(t)/t` is nonincreasing. Consequently, for `0<s<=t`,

`h(s) >= (s/t)h(t)`.

Integrating from `0` to `t`,

`H(t)=int_0^t h(s) ds >= (t/2)h(t)`,                        (3.13)

which is the upper inequality in (3.4). QED.

### Remarks on status and literature

The reliability interpretation (3.1) is standard. The earlier lower inequality is classical IFRA machinery in this notation. A bounded 2026-09-19 search of heterogeneous second-failure / `k`-out-of-`n` reliability literature found many order-statistic and hazard-rate results, but I did not locate an accessible source stating exactly the upper generalized-hazard inequality `t h(t)<=2H(t)` for arbitrary independent exponential rates in the form above. **Novelty is therefore UNVERIFIED.** The proof, not the search miss, is the mathematical evidence being retained.

---

## 4. Two immediate exact consequences at a base point

Put

`m_i:=q_i F_i(q)=q_i(1-r_i)`,
`D:=sum_i m_i=<q,grad F(q)>`.                                (4.1)

Theorem R15-F0111-ELASTIC2 gives

`F(q) <= D <= 2F(q)`.                                       (4.2)

There is also a coordinatewise bound

`0<=m_i<=F(q)`.                                              (4.3)

To see this, hold all coordinates except `i` fixed. The hazard is increasing and concave in `q_i` (a carried elementary fact, also immediate from (2.2)--(2.4)). If `f(s)` is that one-coordinate section, concavity gives

`s f'(s) <= f(s)-f(0) <= f(s)`.

At `s=q_i` this is exactly (4.3).

Equations (4.2)--(4.3) are the entire input needed for the dual/local geometry below.

---

## 5. Method #11 — DUALIZE: exact local coefficient masses are a random singleton-or-pair law

Suppose a positive multilinear polynomial

`P(t)=sum_{empty != I} beta_I t_I`, `beta_I>=0`,              (5.1)

globally majorizes `F` and has an exact `C_1` contact at an interior base `q`, i.e.

`P(q)=F(q)`.                                                  (5.2)

Because `P-F>=0` globally and vanishes at an interior point, necessarily

`grad P(q)=grad F(q)`.                                       (5.3)

Define the **contact masses**

`c_I=beta_I q_I>=0`.                                        (5.4)

Then (5.2)--(5.3) become

`sum_I c_I=F(q)`,                                            (5.5)

`sum_{I contains i} c_I=m_i`.                               (5.6)

After normalizing by `F(q)`, the numbers

`pi_I=c_I/F(q)`                                              (5.7)

form a probability distribution on nonempty coordinate subsets. Its inclusion marginals are

`p_i=P_pi(i in I)=m_i/F(q) in [0,1]`,                        (5.8)

and its expected subset size is

`E_pi |I| = sum_i p_i = D/F(q) in [1,2]`.                   (5.9)

Thus every exact positive contact certificate has a very concrete local probabilistic shadow: a random nonempty hyperedge whose expected size is between one and two.

The converse local statement is stronger and constructive.

### Theorem R15-F0111-LOCAL2 — the positive degree-`<=2` contact cone is nonempty at every interior base

For every `n>=2` and every interior base `q>0`, there exist nonnegative numbers

`a_i>=0`, `e_ij>=0`

such that

`sum_i a_i + sum_{i<j} e_ij = F(q)`,                         (5.10)

`a_i+sum_{j!=i}e_ij = m_i` for every `i`.                   (5.11)

Consequently the quadratic positive multilinear polynomial

`P_loc,q(t)`
` = sum_i (a_i/q_i)t_i`
`   + sum_{i<j}(e_ij/(q_i q_j))t_i t_j`                     (5.12)

satisfies exactly

`P_loc,q(q)=F(q)`,                                           (5.13)

`grad P_loc,q(q)=grad F(q)`.                                (5.14)

This is a **local contact/budget theorem only**. It does not yet say `P_loc,q(t)>=F(t)` away from `q`.

### Proof

Normalize as in (5.8), and let

`s=sum_i p_i in [1,2]`,
`w=s-1 in [0,1]`.                                           (5.15)

A probability law supported on singleton and pair subsets with marginals `p_i` must put total mass `w` on pairs and mass `1-w=2-s` on singletons. In unnormalized units, the total desired pair contact mass is therefore

`W:=wF(q)=D-F(q)`.                                          (5.16)

It is enough to construct normalized pair-degrees `d_i` satisfying

`0<=d_i<=p_i`,
`sum_i d_i=2w`,
`max_i d_i<=w`.                                             (5.17)

Such degrees exist because

`sum_i min(p_i,w) >= 2w`.                                   (5.18)

Indeed, if all `p_i<=w`, the left side is `s=1+w>=2w`. If at least two `p_i>w`, it is at least `2w`. If exactly one, say `p_* > w`, then it is

`w+(s-p_*)=1+2w-p_* >=2w`

because `p_*<=1`. Thus we may choose `d_i<=min(p_i,w)` totaling `2w`.

It remains to realize the degree vector by a fractional loopless graph. Partition a circle of circumference `2w` into consecutive arcs of lengths `d_i`. Pair each point with its antipode at distance `w`. Since every arc has length at most `w`, an arc and its antipodal translate overlap only on a null boundary set, so no positive mass is paired to the same label. Restricting to one representative of each antipodal pair produces nonnegative edge masses `epsilon_ij` of total `w` and vertex degrees `d_i`.

Set normalized singleton masses

`alpha_i=p_i-d_i>=0`.                                       (5.19)

Then

`sum_i alpha_i = s-2w = 2-s = 1-w`,

and the singleton-plus-pair law has total mass one and inclusion marginals exactly `p_i`.

Finally put

`a_i=F(q) alpha_i`,
`e_ij=F(q) epsilon_ij`.

Equations (5.10)--(5.14) follow immediately. QED.

### Exact characterization of the quadratic local cone

The preceding proof also gives the whole cone. Let

`W=D-F(q)>=0`.                                               (5.20)

Every positive quadratic contact polynomial is equivalent to choosing edge masses `e_ij>=0` satisfying

`sum_{i<j} e_ij=W`,                                         (5.21)

`d_i:=sum_{j!=i}e_ij <=m_i`,                                (5.22)

and then setting

`a_i=m_i-d_i`.                                               (5.23)

Conversely every such fractional graph gives a positive quadratic polynomial with exact value and gradient contact through (5.12).

This is the cleanest dual conclusion of the run: **there is no zeroth- or first-order positivity obstruction to `C_1` for heterogeneous `k=2`, and degree two already suffices to satisfy every local contact/budget condition.** Any failure of `C_1` for `k=2` must therefore be genuinely global (or at least arise from second and higher order geometry away from the base), not from the positive coefficient cone at contact.

---

## 6. Method #24 — FIND THE EXTREMAL OBJECT: a canonical rank-one pair-mass ansatz

Theorem R15-F0111-LOCAL2 leaves a compact fractional-graph family of local quadratic contacts. The next question is to find one member which is a **global** majorant.

There is a natural base-adaptive candidate suggested by the cross-curvature (2.3). Define

`z_i=q_i r_i`,
`Z=sum_i z_i`,
`R_2=sum_{i<j} z_i z_j`,
`W=D-F(q)=log S-Z`.                                         (6.1)

When `R_2>0`, put

`kappa=W/R_2`                                               (6.2)

and propose pair contact masses

`e_ij^*=kappa z_i z_j`.                                    (6.3)

Their total is exactly `W`, as required by (5.21). The induced degrees and singleton contact masses are

`d_i^*=kappa z_i(Z-z_i)`,
`a_i^*=m_i-d_i^*`.                                          (6.4)

Whenever all `a_i^*>=0`, this gives the explicit positive quadratic

`P_q^*(t)`
` = sum_i [(1-r_i)-kappa r_i(Z-z_i)] t_i`
`   + kappa sum_{i<j} r_i r_j t_i t_j.                      (6.5)

Algebraically, regardless of the still-unproved coefficient signs, (6.5) has the exact contact identities

`P_q^*(q)=F(q)`,
`grad P_q^*(q)=grad F(q)`.                                  (6.6)

Global majorization is equivalent to the explicit inequality

`log S(t)`
` >= sum_i r_i t_i`
`    + kappa sum_{i<j} r_i r_j`
`       (q_j t_i + q_i t_j - t_i t_j)`                     (6.7)

for every `t>=0`.

At `t=q`, (6.7) is equality because `Z+kappa R_2=log S`. Its first derivatives also agree by construction.

I do **not** claim either of the two missing facts:

1. `a_i^*>=0` for every heterogeneous base;
2. the global inequality (6.7).

Those are now concrete analytic targets rather than an unspecified search over all positive coefficients. The rank-one ansatz is retained as a **candidate/extremal object**, not as a theorem or certificate.

A useful exact second-order diagnostic is available. In normalized coordinates `t_i=q_i x_i`, the Hessian of `P_q^*-F` at `x=1` has diagonal entries

`q_i^2 r_i(1-r_i)`                                          (6.8)

and off-diagonal entries

`-(1-kappa)z_i z_j`.                                       (6.9)

Thus even local minimality of this particular rank-one ansatz reduces to one explicit diagonal-minus-rank-one semidefinite inequality. A failure there would discard the ansatz immediately without affecting Theorem R15-F0111-LOCAL2; a proof there would still leave the global inequality (6.7).

This gives the next route a precise fork: either prove the rank-one object lies in the local cone and global-majorizes, or use the local fractional-graph polytope (5.21)--(5.23) to optimize away from rank one.

---

## 7. Why this is genuine movement but not source closure

The previous R15 report proved that every **serial** one-coordinate Pascal compiler for heterogeneous `k=2` has worst-case constant exactly `1/(n-1)`. This run changes category and shows that the underlying `k=2` function itself has much stronger local structure:

- its radial elasticity is universally between one and two;
- every interior base admits a positive degree-`<=2` polynomial with exact Talagrand `C_1` **budget and tangent contact**;
- the entire local quadratic contact cone is a fractional graph polytope with pair mass exactly `D-F`;
- a canonical curvature-aligned point of that polytope is now explicit, with a single global inequality left to test if its coefficient signs are established.

This explains why the serial method can lose a factor of `n` even though the true contact geometry has no such dimension loss. It also rules out a broad class of purely local obstructions to heterogeneous `k=2` `C_1`.

It does **not** prove `A_{n,2} in C_1`: local contact is not global majorization. It says nothing directly about `k>=3`. Hence Talagrand Problem 10.9 remains `PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED` in this retained screen.

No finite checker was created. The new retained claims are parameter-uniform analytic statements with proofs on the page; a numerical grid would not certify them. The rank-one object is explicitly labelled conjectural rather than being promoted from exploratory evidence.

---

## 8. Current literature / prior-art log

Dated 2026-09-19 searches covered:

- Burdzy--Scheutzow exact title, exact Problem 7.2 wording, later author/citing material;
- Talagrand exact Problem 10.9 / `C_gamma` / cardinality-threshold language;
- the 2026 discrete-convexity / `k`-threshold papers;
- heterogeneous second-failure / 2-out-of-`n` reliability, hazard-rate, generalized-failure-rate and exponential-order-statistic language.

Current adjacent Talagrand literature recovered includes:

- Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), *A reformulation of the discrete Convexity Conjecture via k-thresholds*;
- Jinyoung Park, arXiv:2609.14681 (2026-09-13), *A dimension-free comparison between expectation thresholds and fractional expectation thresholds*;
- the current admission sentinel also records Chen Li's September 2026 fractional result and the September 16 Fang--Wang note settling other explicitly numbered Talagrand conjectures, not Problem 10.9 in the retrieved source statements.

The bounded search did not produce an accessible source explicitly stating Theorem R15-F0111-ELASTIC2, the quadratic local-cone characterization above, or a resolution of Talagrand's exact Definition-10.1 / Problem-10.9 positive-multilinear-majorant formulation. The reliability interpretation and standard order-statistic machinery are folklore/classical; **publication novelty of the derived inequalities and their Talagrand use remains UNVERIFIED**.

Failure to find a paper is not treated as proof of worldwide openness or priority.

---

## 9. Model / scheduler / authorization boundary

The model-control situation is still the same as the operative repository manifest records. The exposed task-management surface provides task identity/title/prompt, scheduling or relative-start fields, timing mode and enabled state. It exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed hour-long execution field**. Accordingly `Model: GPT-6. Reasoning: maximum` remains prompt text here, not an enforceable scheduler setting.

The historical P26 event `You cannot modify this task` is preserved as an authorization-context boundary. Repository continuity separately records a later successful P26 update from an authorized P/C context. The lawful workaround for a future refusal is the owning/otherwise-authorized account, workspace or owner/admin product/API/support surface for the same task. Duplicating the task, bypassing permissions, or pretending a repository edit changes native model routing is not a workaround. No scheduler or permission change was attempted in this run.

---

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), arXiv:1302.6958, Problem 7.2; intake I0076"
  target: "Decide whether FBM + BBM + source-exact independence of the centered half-processes at an arbitrary finite random real seam implies 2BM"
  fixed_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  metric_before: "historical retired 2/4; no surviving frozen candidate"
  metric_after: "historical retired 2/4; no surviving frozen candidate"
  source_metric_movement: "none"
  status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  unchanged_count: "6 (frozen at mandatory retirement; not incremented during successor screening)"
  tried_moves:
    - "#1 CHANGE THE CATEGORY"
    - "#11 DUALIZE"
    - "#24 FIND THE EXTREMAL OBJECT"
  retained_screen: "F0111 Talagrand Problem 10.9; PENDING / NOT READY / SELF_CHECK_ONLY / NOT CLAIMED"
  retained_screen_movement:
    - "proved second-failure radial elasticity 1 <= <q,grad F>/F <= 2 for k=2"
    - "proved every interior k=2 base has a positive degree-<=2 exact local C1 contact/budget polynomial"
    - "characterized all such local quadratic contacts by a fractional graph with total pair mass D-F"
    - "isolated a curvature-aligned rank-one candidate and its exact remaining coefficient/global inequalities"
  remaining_I0076_obligation: "handoff blocker H: prove or disprove equality with 2BM on the full common-rerooting invariant sigma-field / construct a genuine relative-phase counterexample; do not reopen without reassignment"
  remaining_F0111_obligation: "turn a local quadratic contact into a global positive majorant with uniform source-valid scope; rank-one inequalities (6.4)/(6.7) are one concrete next target; full Problem 10.9 also requires k>=3"
  admission_state: "no new ownership-clear READY CLOSABLE successor claimed"
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260919_0056Z_successor_screen_f0111_sorted_pascal_x70t.md"
    - "proofnet24/NM13-12/runs/2026-09-19/2026-09-19T00-59-30Z__post-e0086-admission-delta-screen-11-f0111-adaptive-k2.md"
    - "this immutable report"
  audit_ids: []
  closure_claimed: false
```

Next genuinely different research methods if the retained screen is still the only lawful work are **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #14 FIND THE GROUP ACTING, #30 DO ONE SCALE/DIRECTION AT A TIME**, applied to the fractional-graph contact polytope and the explicit global inequality (6.7), not to another serial Pascal lemma.
