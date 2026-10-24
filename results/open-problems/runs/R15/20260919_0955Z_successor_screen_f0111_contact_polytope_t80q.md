Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the four source-matching obligations remain `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`, and the historical positive-route `2/4` is only the frozen handoff value, not a live-candidate score. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, `k=2`, I prove that **every fully interior base point** admits a strictly positive quadratic polynomial with exact value-and-gradient contact. Thus the positive exact-contact cone has no interior-base holes; any failure of a global `C_1` certificate must occur at second order or in global majorization, not at zeroth/first-order positive-contact feasibility. Methods #4 PROVE SOMETHING WEAKER, COMPLETELY, #13 FIND WHAT ONLY INCREASES, #27 SWAP THE QUANTIFIERS.**

# R15 retained screen — the `k=2` positive exact-contact polytope is nonempty at every interior base

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything newly proved below on Talagrand F0111 is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen I0076, promote F0111 from PENDING/NOT READY, establish publication novelty, solve Talagrand Problem 10.9, or satisfy the fleet two-independent-audit closure rule.

## 1. Continuity, source fidelity, exclusions, ownership, and current fleet state

I continued from

`runs/R15/20260919_0903Z_successor_screen_f0111_open_certificate_region_s79p.md`

rather than restarting. Before new mathematics I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the current I0076 history and controlling handoff, the newest R15 report, the neighboring R20 F0111 handoff, and the newest coordinator reconciliation available during this run,

`operations/task_health/runs/2026-09-19T085900Z/root_merge_delta.md`.

That coordinator reconciliation records newly certified **free** READY inventory as `0`; the CLOSABLE targets that have cleared admission are already owned. Retirement/handoff is not an ownership release absent an explicit release. I therefore created no successor claim, did not edit shared roots, and did not take another worker's target.

### Burdzy–Scheutzow source rechecked exactly

The primary PDF, arXiv:1302.6958v4, Definition 2.1 and Problem 7.2, still gives exactly:

- FBM: there are random origins `S_n -> -infinity` from which the complete centered future is standard Brownian motion;
- BBM: time reversal is FBM;
- 2BM: there is one random origin `S` at which the complete centered future and past are **independent standard Brownian motions**;
- Problem 7.2 assumes FBM + BBM and existence of an arbitrary random time `T` at which the two complete centered half-processes are independent.

There is no stopping-time assumption on `T`, and neither seam half at `T` is separately assumed Brownian. Problem 7.5 is a different question and remains excluded.

The controlling I0076 handoff remains valid. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but no source-valid independent seam; the later Brownian-prefix/BES candidate had FBM, BBM and exact seam independence but was proved actually 2BM. Hence there is still no surviving frozen counterexample candidate on which the original four-obligation metric can honestly move.

Fresh public searches dated 2026-09-19 used the exact title/arXiv identifier, `Problem 7.2`, later-author terms, and citation terms. They recovered the original paper and related citation material but no accessible later primary source explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

For F0111 I rechecked Talagrand's original Problem 10.9 and recent primary literature. Problem 10.9 asks for one universal `gamma>0` for all cardinality up-classes and all base points. Current searches recovered Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), reformulating the broader discrete convexity conjecture via `k`-thresholds and proving substantial classes; Park, arXiv:2609.14681 (2026-09-13), giving a dimension-free comparison toward the conjecture; and September fractional-threshold follow-up literature. None of the retrieved sources claims the exact positive-multilinear Problem-10.9 statement or the exact-contact theorem below. Search failure is not a novelty certificate; novelty remains `UNVERIFIED`.

The preceding R15 run used methods #1, #15, #19. I therefore did not repeat that triple. The originally assigned #2, #12, #23 were also exhausted in the I0076 phase. This run uses #4, #13, #27.

## 2. Carried setup

For the cardinality-two threshold define

`F_n(t)=sum_i t_i - log(1+sum_i(exp(t_i)-1))`.              (2.1)

The preceding R15 theorem proved that the set of interior bases carrying a strictly positive **global** quadratic `C_1` certificate has nonempty full-dimensional open subsets in every dimension. Its constructive transport used exact-contact masses, but only near already certified bases.

The natural next question is whether positivity/exact contact itself can break as the base moves. This run answers that question completely: **no, not anywhere in the interior**. Global majorization remains the hard part.

Fix arbitrary

`q=(q_1,...,q_n) in (0,infinity)^n`, `n>=2`.                (2.2)

Set

`x_i=exp(q_i)-1>0`, `X=sum_i x_i`, `L=sum_i log(1+x_i)=sum_i q_i`,

`S=1+X`, `r_i=(1+x_i)/(1+X)`,                              (2.3)

`m_i=q_i(1-r_i)=q_i (X-x_i)/(1+X)`,                        (2.4)

`D=sum_i m_i`, `F=F_n(q)=L-log(1+X)`, `W=D-F`.             (2.5)

For a quadratic positive polynomial

`P(t)=sum_i A_i t_i + sum_{i<j} B_ij t_i t_j`,              (2.6)

introduce contact masses

`a_i=A_i q_i`, `e_ij=B_ij q_i q_j`.                        (2.7)

Exact gradient contact at `q` is equivalent to

`a_i+sum_{j!=i}e_ij=m_i` for all `i`,                       (2.8)

while exact value contact is equivalent, after summing (2.8), to

`sum_{i<j}e_ij=W`.                                          (2.9)

Thus the question is a positive weighted-graph realization problem: can one choose strictly positive edge masses totaling `W`, with each incident degree strictly below `m_i`?

## 3. Method #13 — a strict degree-band invariant: `1 < D/F < 2`

The first key point is that the required total pair mass always lies in the correct range.

### Lemma 3.1 — `W>0`

We have

`(1+X)W=(1+X)log(1+X)-sum_i(1+x_i)log(1+x_i)`.              (3.1)

Let

`h(x)=(1+x)log(1+x)`, `h(0)=0`.                             (3.2)

For fixed `x>0`,

`d/dy [h(x+y)-h(x)-h(y)]
 = log((1+x+y)/(1+y))>0`,                                   (3.3)

and the bracket is zero at `y=0`. Therefore `h` is strictly superadditive on positive arguments. Since every `x_i>0` and `n>=2`,

`h(X)>sum_i h(x_i)`.                                         (3.4)

Hence `W>0`, equivalently `D>F`.

### Lemma 3.2 — `D<2F`

A direct rearrangement gives

`(1+X)(2F-D)
 = (X+2)L + sum_i x_i log(1+x_i)
   - 2(1+X)log(1+X)`.                                       (3.5)

For this fixed total `X`, define on `[0,X]`

`psi_X(x)=(X+2+x)log(1+x)`.                                 (3.6)

Then

`psi_X''(x)=(x-X)/(1+x)^2 <=0`,                             (3.7)

and `psi_X(0)=0`. Concavity plus the zero origin implies subadditivity on `[0,X]`: whenever `a,b>=0` and `a+b<=X`,

`psi_X(a)+psi_X(b)>=psi_X(a+b)`,                             (3.8)

with strict inequality when both pieces are positive in our interior situation. Iterating,

`sum_i psi_X(x_i)>psi_X(X)=2(1+X)log(1+X)`.                 (3.9)

Comparing with (3.5) yields `2F-D>0`.

Thus

`boxed:  F < D < 2F`,                                       (3.10)

or equivalently

`boxed:  0 < W=D-F < F` and `W<D/2`.                        (3.11)

Conceptually, if an exact positive contact is represented by monomial masses `c_I`, then

`sum_I c_I=F`, `sum_I |I|c_I=D`;                            (3.12)

so `D/F` is the contact's mass-weighted average monomial degree. The invariant (3.10) says that for `k=2` every interior base has required average degree strictly between one and two. That is the monovariant/degree-band found in this run.

## 4. A coordinatewise slack inequality: `m_i<F` for every `i`

Fix `i`, and put

`Y=X-x_i>0`, `a=q_i=log(1+x_i)>0`, `b=log(1+Y)>0`.          (4.1)

Since

`prod_{j!=i}(1+x_j)>=1+sum_{j!=i}x_j=1+Y`,                 (4.2)

we get

`F
 = a+sum_{j!=i}log(1+x_j)-log(1+x_i+Y)
 >= a+b-log(exp(a)+exp(b)-1)`.                              (4.3)

Call the last expression `F_2(a,b)`. For fixed `b`,

`partial_u F_2(u,b)=(exp(b)-1)/(exp(u)+exp(b)-1)`,          (4.4)

which is strictly decreasing in `u`. Hence

`F_2(a,b)
 = integral_0^a partial_u F_2(u,b) du
 > a partial_u F_2(a,b)
 = q_i Y/(1+X)
 = m_i`.                                                     (4.5)

Therefore

`boxed: m_i<F for every i`.                                 (4.6)

Using `W=D-F`, this is equivalently

`D-m_i>W for every i`.                                      (4.7)

This coordinatewise slack is exactly what is needed to realize the total pair mass without exhausting any singleton coefficient.

## 5. Method #27 — swap the quantifiers: construct positive contact for every interior base

The preceding open-region theorem had the form “starting from one nondegenerate globally certified base, nearby bases remain certified.” Here I swap the quantifiers at the **contact** level:

`for every interior base q, there exists a strictly positive quadratic exact contact.`

### Theorem R15-F0111-CONTACT-ALL — no interior zeroth/first-order obstruction for `k=2`

For every integer `n>=2` and every `q in (0,infinity)^n`, there exist coefficients

`A_i>0`, `B_ij>0`                                           (5.1)

such that the quadratic multilinear polynomial

`P_q(t)=sum_i A_i t_i+sum_{i<j}B_ij t_i t_j`                (5.2)

has exact value and gradient contact with `F_n` at `q`:

`P_q(q)=F_n(q)`,                                             (5.3)

`grad P_q(q)=grad F_n(q)`.                                  (5.4)

No global-majorant assertion is made in this theorem.

#### Proof for `n=2`

There is one edge. Put

`e_12=W>0`.                                                   (5.5)

Then

`a_1=m_1-W=F-m_2>0`,
`a_2=m_2-W=F-m_1>0`                                         (5.6)

by (4.6). Equations (2.8)-(2.9) hold.

#### Proof for `n>=3`: choose admissible weighted degrees

Let

`c_i=min(m_i,W)`, `C=sum_i c_i`.                            (5.7)

I claim

`C>2W`.                                                       (5.8)

There are three cases.

1. If every `m_i<W`, then `C=D>2W` by (3.11).
2. If at least two indices satisfy `m_i>=W`, then those two already contribute `2W`, and every remaining `c_i` is strictly positive because `n>=3`, so `C>2W`.
3. If exactly one index `k` satisfies `m_k>=W`, then

`C=W+sum_{i!=k}m_i=W+D-m_k>2W`                              (5.9)

by (4.7).

Define

`theta=2W/C in (0,1)`, `d_i=theta c_i`.                     (5.10)

Then

`0<d_i<m_i`, `d_i<W`, `sum_i d_i=2W`.                       (5.11)

#### Weighted-complete-graph realization lemma

Suppose `n>=3`, `d_i>0`, `sum_i d_i=2W`, and `max_i d_i<W`. Then there exist **strictly positive** symmetric edge weights

`e_ij=e_ji>0`, `e_ii=0`,                                    (5.12)

with row sums

`sum_{j!=i}e_ij=d_i`.                                        (5.13)

First construct nonnegative weights. Take a circle of circumference `2W` and partition it into consecutive arcs `I_i` of lengths `d_i`. Pair each point `s` with its antipode `s+W mod 2W`. Because every arc has length `<W`, no arc contains an antipodal pair. Define `e_ij` as the Lebesgue measure of points of `I_i` whose antipodes lie in `I_j`. The antipodal map is measure preserving, so `e_ij=e_ji>=0`; there are no loops; and the row sum from `I_i` is exactly `d_i`.

To force every edge strictly positive, choose `epsilon>0` so small that

`d_i' = d_i-(n-1)epsilon >0`,                               (5.14)

and, with

`W'=W-binomial(n,2)epsilon`,                                 (5.15)

also

`d_i'<W'` for every `i`.                                    (5.16)

This is possible because

`W'-d_i'=(W-d_i)-((n-1)(n-2)/2)epsilon`,                   (5.17)

and each `W-d_i>0`. Apply the nonnegative circle construction to the residual degrees `d_i'`, obtaining residual weights `f_ij>=0`, then set

`e_ij=f_ij+epsilon`.                                         (5.18)

Every edge is now positive, while its row sum is exactly

`sum_{j!=i}e_ij=d_i'+(n-1)epsilon=d_i`.                     (5.19)

Also `sum_{i<j}e_ij=W` because the total row mass is `2W`.

#### Finish the contact construction

Set

`a_i=m_i-d_i>0`.                                             (5.20)

Then (5.13) gives

`a_i+sum_{j!=i}e_ij=m_i`,                                   (5.21)

and the edge total is exactly `W`. Define

`A_i=a_i/q_i>0`, `B_ij=e_ij/(q_iq_j)>0`.                    (5.22)

By (2.8),

`partial_i P_q(q)=m_i/q_i=1-r_i=partial_i F_n(q)`.          (5.23)

Finally,

`P_q(q)=sum_i a_i+sum_{i<j}e_ij
       =(D-2W)+W
       =D-W
       =F`.                                                   (5.24)

This proves the theorem. QED.

## 6. Method #4 — what was proved completely, and what it rules out

The theorem is deliberately weaker than global `C_1`, but it is complete at its stated level.

Before this run, the global-certificate region was only known to contain explicit full-dimensional open patches. One possible way such a region could terminate was **loss of positive exact-contact feasibility**: a required singleton mass or pair-mass polytope could collapse before any global inequality failed.

Theorem R15-F0111-CONTACT-ALL rules that mechanism out everywhere in `(0,infinity)^n`. At every fully interior base, there is a strictly positive degree-1/degree-2 exact contact.

Therefore any boundary of the **global** quadratic `C_1` certificate region must arise from genuinely higher-order geometry:

1. the contact Hessian ceases to be positive semidefinite / develops a negative direction; or
2. a new global zero of `P_q-F_n` is born away from the contact point; or
3. no choice inside the positive exact-contact polytope simultaneously meets the global majorant inequality.

It cannot arise merely because exact value/gradient contact with positive coefficients is impossible.

A useful conceptual restatement is that the contact-data average degree `D/F` always belongs to `(1,2)`, and the proof constructs a strictly positive realization supported entirely on degrees one and two. This is the natural local convex-geometric invariant for future continuation arguments.

## 7. Why this is not a solution of Talagrand Problem 10.9

Talagrand's source asks for one universal `gamma>0` working for every cardinality threshold and every base, with a positive multilinear polynomial satisfying a **global** majorant condition and the source budget. The theorem above proves only exact local contact for `k=2`.

In particular, I have **not** proved

`P_q(t)>=F_n(t) for all t>=0`                                (7.1)

for the newly constructed all-base family. The previously certified global results remain only the open patches around the special two-level bases. So the honest status is still `PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED`.

The fresh literature search did not find an accessible primary source stating this exact all-interior-base contact theorem, but the ingredients are elementary convexity and weighted-degree realization. Publication novelty is therefore `UNVERIFIED`; no novelty claim is made.

## 8. No finite checker this run

I wrote the new idea and proof before considering code, per the 90/10 rule. No finite checker was created because the new result is a parameter-uniform analytic theorem. A numerical grid over `q` would not certify either the strict inequalities or the all-base weighted-degree realization, and would add bookkeeping without moving the source metric.

## 9. Next genuinely different methods

If F0111 remains the retained screen and no free CLOSABLE successor is admitted, the next nonrepeating methods should be:

- **#11 DUALIZE:** write global quadratic-majorant feasibility over the exact-contact edge polytope as a dual separation problem;
- **#20 FIND WHY THE ALGORITHM FAILS:** follow the explicit contact construction above until the first Hessian/global-gap failure and identify the exact obstruction;
- **#24 FIND THE EXTREMAL OBJECT:** optimize the smallest Hessian eigenvalue or global-gap minimum over the contact polytope at a fixed heterogeneous base to locate the first boundary mechanism.

Returning to serial Pascal orderings, local-only rank-one contacts, or another numerical path sampler would not address the remaining obstruction.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2 / I0076"
  native_metric: "four source-matching obligations for one frozen counterexample candidate"
  native_metric_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE (historical retired positive-route value 2/4)"
  native_metric_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE (historical retired positive-route value 2/4)"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "FROZEN_AFTER_SIX-RUN_HANDOFF"
  free_ready_closable_before: 0
  free_ready_closable_after: 0
  retained_screen: "Talagrand F0111, Problem 10.9, k=2 subproblem; PENDING / NOT READY / SELF_CHECK_ONLY / NOT CLAIMED"
  retained_screen_movement: "proved every q in (0,infinity)^n admits a strictly positive quadratic exact value+gradient contact; exact-contact cone has no interior-base holes"
  tried_moves: [4, 13, 27]
  remaining_obligation: "for F0111 k=2, determine whether globally majorizing positive quadratic contacts exist beyond the known open patches; for source Problem 10.9, uniform all-k all-q gamma remains untouched"
  evidence:
    - "this immutable report"
    - "runs/R15/20260919_0903Z_successor_screen_f0111_open_certificate_region_s79p.md"
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md"
    - "operations/task_health/runs/2026-09-19T085900Z/root_merge_delta.md"
  audit_ids: []
  closure: false
  novelty: UNVERIFIED
```

## 11. Model / scheduler-control truth

The exposed scheduler surface still provides task identity/title, prompt, recurrence/timing mode, enabled state and notification controls, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort telemetry, and no guaranteed-duration field**. Therefore `GPT-6 / maximum` remains prompt-only in this environment. The historical P26 response `You cannot modify this task` was an authorization-context boundary; the repository also records later successful modification from an authorized P/C context. Enforcing a particular model/reasoning level would require an owning/admin product or backend/API surface that exposes and persists those routing fields. No scheduler or permission change was attempted in this run.
