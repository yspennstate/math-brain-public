Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Movement on the frozen P0151 metric: **`gamma_E >= b4 -> gamma_E >= b5` with `b5>b4`**; methods actually used: **B6 / B11 / B28**.

# HARD7-04 bounded research iteration — full-attractiveness bridge amplification for fixed-outdegree PA criticality

Status: **PARTIAL / SOURCE OPEN**. This run gives a strict new lower bound for the expected largest-component power exponent in the exact fixed-outdegree sequential preferential-attachment model. It does **not** identify the critical-window width, prove a matching upper bound, prove `sqrt(n)/log n` scaling, tightness, or a scaling limit. The full analytic proof is also isolated at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_full_attractiveness_bridge_lemma.md`

created at commit `36dfb44dfa668c034416864522de6714cc5233fd` and read back successfully.

## 1. Continuity, ownership, and evidence consumed

I resumed the existing exclusive claim

`operations/claims/P0151.md`

owned by `HARD7-04`. I did not restart I0049, the retired BHS/configuration-model MST route, the independently-attached-edge growing-graph theorem, or any peer claim.

Before doing mathematics I reread the required control surfaces and current repository state:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the P0151 claim and intake/catalog aliases;
- the immediately preceding HARD7-04 reports, especially `2026-09-20T0130Z__p0151_all_gate_distinct_bridge.md`;
- the neighboring current R08 lifecycle report. R08 is on an unrelated retired/reassignment gate and creates no P0151 ownership collision.

The preceding HARD7-04 checkpoint explicitly said that another constant-base-ticket bridge lemma was no longer the right route and that the next attempt should use age/degree-dependent mass or a two-sided/spectral mechanism. This run follows that instruction: the new score is **full current attractiveness**, not another constant ticket.

The current posting registry contains no P0151-equivalent posted paper.

### Fresh current-literature check, 20 September 2026

A fresh bounded search rechecked the exact model and neighboring critical-window results.

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026), still gives the exact threshold for model (d), with sequential fixed outdegree `m`, but not a finite-size critical-window theorem:
   `https://arxiv.org/abs/2312.14085`.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, proves a `(log n)^(-2)` window and `sqrt(n)/log n` largest-component scale for models in which new vertices connect **independently** to earlier vertices. Their abstract explicitly keeps this independent-connection assumption:
   `https://arxiv.org/abs/2512.18937`.
3. Mörters--Schätze, arXiv:2606.27844, treats an inhomogeneous preferential-attachment-kernel graph in the infinite-variance regime with a moving threshold, not the fixed-`m`, `delta>0` sequential model:
   `https://arxiv.org/abs/2606.27844`.
4. Ray's thesis remains the current source restatement of the critical-regime program:
   `https://pure.tue.nl/ws/portalfiles/portal/345650538/20241204_Ray_hf.pdf`.

No source-matching fixed-outdegree sequential critical-window resolution surfaced. This is bounded negative evidence only, not a worldwide novelty certificate.

## 2. Frozen model and source-relevant metric

Fix integer `m>=2`, `delta>0`, and Ray/Hazra--van der Hofstad--Ray model (d): every arriving vertex has exactly `m` sequential edges to older vertices, target probability proportional to current degree plus `delta`, no self-loop for new vertices, followed by independent bond retention `pi`.

Put

`a:=m+delta`, `A:=2m+delta`.

At criticality,

`pi_c = delta / [2( m a + sqrt(m(m-1)a(a+1)) )]`.

The frozen metric remains

`gamma_E := liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The previous run proved

`gamma_E >= b4`,

with

`b2 := [m+a m pi_c]/A`,

`b4 := b2 + eta_0`,

`eta_0 := m(m-1)(a pi_c/A)^2`.

This run proves

`gamma_E >= b5 := b2 + eta_F`,                                    (2.1)

where

`eta_F := m(m-1) pi_c^2 a/A`.                                     (2.2)

Since

`eta_F/eta_0=A/a>1`,                                               (2.3)

we obtain strict source-metric movement

`b5>b4`.                                                            (2.4)

For orientation only, at `m=2`, `delta=1`:

`pi_c ~= 0.04587585476806849`,
`b4   ~= 0.4565663334381869`,
`b5   ~= 0.4575765385825233`.

No numerical value enters the proof.

---

## 3. Idea before validation: what changes category inside the same problem

The all-gate calculation from the previous run captured an old bridge root with only the constant base ticket `a`. That makes every birth increment bounded, but it throws away the root's accumulated degree.

The new idea is:

> **When an old bridge root is certified by a uniformizing base thinning, add the root with its full pre-birth attractiveness `d_u(t)+delta`, rather than with the base ticket `a`.**

The apparent fatal obstruction is that a bridge root can be a hub, so the shadow score no longer has bounded increments. The run therefore attacked the negation first: if the square-attractiveness of the entire graph grows faster than linearly, the proposed second-moment closure fails and this route should be discarded.

It does not fail for `delta>0`. The exact affine-PA recursion gives

`E sum_u (d_u(t)+delta)^2 = O(t)`.                                 (3.1)

This is precisely the finite-variance mechanism available in the positive-threshold regime. It lets the proof replace a **pointwise bounded-increment** argument by an **L^2 global-budget** argument.

A still more aggressive idea, using unthinned size-biased bridge roots, was also tested conceptually and rejected in this run: its first drift involves `sum w_u^2`, but its square-increment closure naturally exposes `sum w_u^3`. The full source range `delta>0` does not supply a uniform third-moment budget. The base thinning is therefore retained deliberately; it uniformizes bridge labels while still allowing the full first attractiveness moment to be harvested.

---

# 4. B6 — deform the old base-ticket route to full attractiveness

The old route corresponds to giving every captured old bridge root the score `a`. A natural deformation is

`h_lambda(w)=a+lambda(w-a)`, `0<=lambda<=1`.

At `lambda=0` this is the preceding base-ticket argument. At `lambda=1` it is full attractiveness. The only serious question is whether the moment closure survives at the endpoint `lambda=1`.

Rather than stop at an infinitesimal deformation, this run proves the endpoint completely. The connected shadow is defined as follows.

Start from a fixed non-initial vertex, say `Q_3={3}`. At the beginning of birth `t+1`, freeze `Q_t` and write

`w_u(t):=d_u(t)+delta`,

`W_t:=sum_{u in Q_t} w_u(t)`.

A **gate** is a retained new edge whose target is in `Q_t`. If any gate occurs, add the new vertex. For every non-initial old `u notin Q_t`, if a new edge targets `u`, independently accept it with probability

`a/w_u(current)`

and require retention. Call this a bridge certificate. Because non-initial vertices are born with degree `m`, `w_u>=a`, so the thinning is valid. Conditional on arbitrary earlier events in the same birth,

`P(B_j(u)=1 | birth history)=pi a/D_{t,j}`.                        (4.1)

Thus bridge certificates are uniform over non-initial vertex labels after thinning, despite the preferential-attachment target law.

If a gate occurs, capture every distinct bridge-certificate target. The set stays connected in the true percolated graph.

Let

- `H_t` = number of current edges targeting the frozen old `Q_t`;
- `I_t` = indicator of at least one gate;
- `J_t` = sum of the **final** attractivenesses at time `t+1` of all distinct captured old bridge roots.

Then exactly

`W_{t+1}-W_t = H_t + a I_t + J_t`.                                (4.2)

This is the endpoint `lambda=1` deformation. It is stronger than the previous ticket process and has unbounded increments, which is handled in Section 6 below.

Outcome of B6: **the old base-ticket route extends all the way to full attractiveness; the endpoint does not require a small perturbation argument.**

---

# 5. B11 — dualize the tracked component against its attractiveness complement

The source denominator satisfies, uniformly over the `m` edge labels,

`At-K <= D_{t,j} <= At+K`                                         (5.1)

for a fixed `K`. Total graph attractiveness is deterministic:

`T_t:=sum_{u<=t}w_u(t)=At+O(1)`.                                  (5.2)

The only vertices for which `a/w_u` need not be valid are the two finite initial vertices. Let

`Z_t:=w_1(t)+w_2(t)`.

Since bridge roots exclude those vertices and the shadow starts at vertex 3, `Q_t` never contains them. Therefore the total eligible outside attractiveness is exactly

`T_t-Z_t-W_t`.                                                     (5.3)

This exact inside/outside decomposition is the useful dual form.

For every ordered pair of distinct labels `j!=k` and eligible outside vertex `u`,

`P(G_j B_k(u)|F_t)
 >= [pi W_t/(At+K)] [pi a/(At+K)]`.                               (5.4)

Summing the frozen bridge weight `w_u(t)` over all outside `u` produces the bilinear cut term

`m(m-1) pi^2 a W_t(T_t-Z_t-W_t)/(At+K)^2`.                        (5.5)

Multiple gates and duplicate bridge hits must be corrected rather than ignored. If

`Y_t:=sum_{k,u} B_k(u)w_u(t)`

and `G_t` is the gate count, the distinct frozen captured mass `J_t^0` satisfies pointwise

`J_t^0
 >= G_tY_t - Y_t binom(G_t,2) - C_same`.                        (5.6)

The duplicate-target correction has conditional expectation `O(1/t)`. The weighted multiple-gate correction is a three-edge event; after summing over outside roots its conditional expectation is

`O((W_t^2+1)/t^2)`.                                                (5.7)

Therefore, since final captured attractiveness dominates frozen captured attractiveness,

`E[J_t|F_t]
 >= eta_F W_t/t
    - C W_t^2/t^2
    - C W_t Z_t/t^2
    - C W_t/t^2
    - C/t`,                                                        (5.8)

where

`eta_F=m(m-1)pi^2 a/A`.                                           (5.9)

This is the strict new coefficient. The preceding base-ticket coefficient was

`eta_0=m(m-1)a^2pi^2/A^2`,

so the gain factor is exactly `A/a`.

Outcome of B11: **the complement identity `T-W` turns the bridge contribution from a vertex-count effect into a full-attractiveness cut form `W(T-W)`, producing a strictly larger first-order coefficient.**

---

# 6. B28 — replace the pointwise bounded-jump demand by an `L^2` global budget

This is the main technical issue. A captured old vertex can have large degree, so the previous deterministic bound on `Delta_t` is gone.

Define the global square-attractiveness

`V_t:=sum_{u<=t}w_u(t)^2`.

During one attachment edge, if the selected vertex has current attractiveness `w`, the square sum rises by `2w+1`. Since target probabilities are proportional to `w`, the conditional expected square increment is `2V/D+1`. Iterating over the fixed `m` edges and then adding the new vertex's square `a^2` gives

`E[V_{t+1}|F_t]
 <= [1+2m/(At)+O(t^-2)]V_t+C`.                                    (6.1)

Because `delta>0`,

`2m/A<1`,

and therefore

`E V_t=O(t)`.                                                       (6.2)

The two finite initial vertices obey similarly

`E Z_t=O(t^h)`, `h:=m/A<1/2`.                                     (6.3)

For an upper drift bound, every captured old root has final attractiveness at most `w_u(t)+m`. Overcounting by all ordered gate--bridge pairs gives

`E[J_t|F_t]
 <= [eta_U/t+O(t^-2)]W_t+C/t`,                                   (6.4)

where

`eta_U:=m(m-1)pi^2 a(A+m)/A^2`.                                   (6.5)

Combining target hits, activation and bridges,

`E[W_{t+1}-W_t|F_t]
 <= [b_U/t+O(t^-2)]W_t+C/t`,                                     (6.6)

`b_U:=b2+eta_U`.                                                    (6.7)

At the exact threshold, `b_U<1/2`. To verify this algebraically, put

`r0:=sqrt(m(m-1)(a+1)/a)`,
`x:=a pi_c=delta/[2(m+r0)]`.

Then

`1/2-b_U
 = (x/A)[r0-m(m-1)x(A+m)/(aA)]`.                           (6.8)

Since `x<delta/(2m)`, `delta/a<1`, and `(A+m)/A<3/2`, the second term in the bracket is less than `3(m-1)/4`, while `r0>m-1`. Hence the bracket is positive.

The square of the bridge jump is also controlled. With at most `m` bridge labels,

`E[J_t^2|F_t]
 <= C (W_t+m)(V_t+t)/t^2`.                                       (6.9)

Since `W_t<=T_t=O(t)` and `E V_t=O(t)`,

`E(J_t^2)=O(1)`,                                                    (6.10)

and the other parts of the birth increment are bounded. Thus

`E(W_{t+1}-W_t)^2=O(1)`.                                           (6.11)

Writing `Y_t:=E W_t^2`, (6.6) gives

`Y_{t+1}
 <= [1+2b_U/t+O(t^-2)]Y_t+C`.                                    (6.12)

Because `2b_U<1`, induction yields

`E W_t^2=O(t)`.                                                     (6.13)

Outcome of B28: **the high-degree bridge roots are harmless in aggregate; the full-attractiveness score has the same linear second-moment budget needed for tangent bootstrapping even though its increments are not uniformly bounded.**

---

# 7. Lower drift and full proof of the new exponent

The ordinary target-hit term satisfies

`E[H_t|F_t] >= m W_t/(At+K)`.                                     (7.1)

Gate activation satisfies the exact lower Bonferroni bound

`P(I_t=1|F_t)
 >= m pi W_t/(At+K)-C W_t^2/t^2`.                                (7.2)

Combine (5.8), (7.1), and (7.2). At `pi=pi_c`, with

`b5:=b2+eta_F`,

`E[W_{t+1}-W_t|F_t]
 >= [b5/t-C/t^2]W_t
    - C W_t^2/t^2
    - C W_t Z_t/t^2
    - C/t`.                                                        (7.3)

Take expectations. From (6.13),

`E W_t^2/t^2=O(1/t)`.                                              (7.4)

Also `W_t<=Ct` deterministically and (6.3) gives

`E[W_tZ_t]/t^2 <= C E Z_t/t = O(t^{h-1})`.                        (7.5)

Therefore, for `mu_t:=E W_t`,

`mu_{t+1}
 >= [1+b5/t-C/t^2]mu_t-C t^{h-1}`.                               (7.6)

We need a positive seed strong enough to absorb this additive error. Without using any bridge contribution, the global chord

`1-(1-pi_c y)^m >= q y`,
`q:=1-(1-pi_c)^m`,                                                 (7.7)

gives directly

`mu_t>=c t^{b1}`,                                                   (7.8)

where

`b1:=[m+a q]/A>h=m/A`.                                             (7.9)

Let `R_t` solve

`R_{t+1}=R_t[1+b5/t-C/t^2]`.

Then `R_t=Theta(t^{b5})`. After division by `R_{t+1}`, the normalized error tail after time `T` is

`O(T^{h-b5})`,                                                     (7.10)

whereas the normalized seed is

`Omega(T^{b1-b5})`.                                                (7.11)

Their ratio is `Omega(T^{b1-h}) -> infinity`. Choose one fixed large `T`; iteration gives

`E W_n >= c n^{b5}`.                                               (7.12)

Finally, the chord (7.7) also gives

`E[I_t|F_t] >= q W_t/(At+K)`.                                     (7.13)

Each activation adds a new vertex to `Q`, so summing (7.13) with (7.12),

`E|Q_n| >= c n^{b5}`.                                              (7.14)

Since `Q_n` lies in one true percolation component,

`E|C_max(n,pi_c)| >= c n^{b5}`,

and hence

`gamma_E>=b5`.                                                     (7.15)

This proves the source-metric movement (2.1)--(2.4).

---

# 8. Exact remaining power gap

The new exponent is still strictly below `1/2`. With the `r0,x` notation above,

`1/2-b5
 = (x/A)[r0-m(m-1)x/a]`.                                          (8.1)

Since

`m(m-1)x/a < (m-1)delta/(2a) < (m-1)/2 < r0`,                    (8.2)

the right side is positive.

Thus this run does **not** prove the expected neighboring power `1/2`, and the source problem remains open.

The useful structural lesson is that the single-component shadow was not saturated at `b4`: replacing constant captured-root tickets by the **full first attractiveness moment** gives a strict additional gain while staying below the `L^2` barrier. The next genuinely different route should target the remaining gap through the Pólya-point-tree critical eigenfunction / age-dependent spectral score, rather than another finite collection of bridge events.

## 9. Before / after, auxiliary progress, and actual checks

### Source metric

Before:

`gamma_E >= b4 = b2 + m(m-1)(a pi_c/A)^2`.

After:

`gamma_E >= b5 = b2 + m(m-1)pi_c^2 a/A`.

Strict movement follows from `A/a>1`.

### Auxiliary mathematical progress

1. Global PA square-attractiveness budget `E V_t=O(t)` for the exact `delta>0` model, proved directly from the sequential attachment recursion.
2. Finite-seed attractiveness bound `E Z_t=O(t^{m/A})`.
3. Full-weight bridge drift identity based on the exact complement `T_t-Z_t-W_t`.
4. An explicit upper drift coefficient `b_U<1/2`, which is what makes the unbounded-jump second moment close.

These are auxiliary results; they do not by themselves answer the source critical-window problem.

### Actual tests / validation performed

- Fresh source/current-literature queries on 20 September 2026 were run against the exact fixed-outdegree wording and neighboring critical-window papers; no source-matching resolution surfaced.
- The algebra was checked at the representative point `m=2, delta=1`, giving `b4~=0.4565663334 < b5~=0.4575765386 < 1/2`.
- No finite simulation or sampled graph is used as evidence.
- No finite checker was manufactured because the substantive claim is analytic, not a finite exhaustive statement. The complete proof is on the page and in the matching artifact.

## 10. Remaining source-level obligations

Still OPEN:

- identify the actual finite-size critical-window width for the exact sequential fixed-outdegree model;
- obtain matching upper and lower component-size scales;
- determine whether `|C_max|` has the neighboring `sqrt(n)/log n` order at criticality;
- prove tightness / joint component scaling / limiting law;
- transfer the critical Pólya-point-tree spectral eigenfunction to a finite-graph exploration with quantitative truncation and dependency control.

A one-sided expected-size exponent, even a strictly improved one, is **PARTIAL**, not source closure.

## 11. Runtime / scheduler capability honesty

The prompt requests GPT-6 with maximum reasoning. The actual model exposed to this run is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The scheduler interface available here still exposes task identity/title, prompt, schedule/timing mode and enabled state, but **no bindable model selector, no bindable reasoning-effort selector, and no guaranteed-duration field**. Therefore GPT-6/maximum remains prompt-requested only. Making it binding would require a product/workspace/API scheduling surface that actually exposes model-family and effort fields and routes execution using them, ideally with runtime attestation.

The repository's current reconciliation also records that the historical P26/P01/P03 `You cannot modify this task` failures were authorization-context boundaries; P26 was later successfully updated from an authorized context. This run did not attempt any scheduler modification because the task contract expressly forbids it. For any task that still returns that denial, the compliant workaround is to use its owning/authorized account or workspace context, an exposed admin/ownership transfer mechanism, or platform support — **not** a duplicate schedule, repository metadata edit, or permission bypass.

No scheduler, shared ledger, peer claim, email, Drive object, permission, workflow, or public posting was changed.