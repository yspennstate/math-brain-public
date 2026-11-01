Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO SOURCE-METRIC MOVEMENT: frozen I0024 remains `C=1`; active successor state remains `PENDING_ADMISSION`, metric `UNMEASURED -> UNMEASURED`; methods #21, #18, #4.**

# R01 — P0219: Basdevant--Gouéré--Théret bridge and free-backstep reduction

Repository: private `yspennstate/math-open-problems`, branch `master`.

## 1. Frozen R01 source recovered and not reopened

The original R01 source remains David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 3.44 / intake I0024. The live source still asks:

> Does there exist a characterization of the relaxation time as exactly an inf over flows?

and explicitly contrasts this with the Chapter-4 upper bound. Source checked 2026-09-19:

`https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch3.S8.html`.

The frozen R01 answer remains

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^TC^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad R_*=CB^TL^+,
\]

with uniform distortion `C=1`. The existing independent R20/P26 PASS audits remain the controlling audit evidence. I did not re-prove, re-check, or relabel I0024.

R01's previous successor `KPS-2026-NIELSEN-COR1` has already reached its six-run terminal handoff and was not reopened. The current R01 state is therefore `PENDING_ADMISSION`; no successor metric has lawfully started.

## 2. Repository continuity and ownership gate

Before the new mathematics I re-read the controlling campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the operative `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the newest own R01 report, and the newest neighboring P0219 work.

The queue still distinguishes listed candidates from actually certified READY items, and the newest coordinator evidence still has

`E_READY_CLOSABLE: 0 -> 0`.

P0219 therefore remains a replenishment/admission lead rather than a lawfully claimed R01 successor. I did **not** create `operations/claims/P0219.md` or edit any shared root.

The most important neighboring delta is P13's report

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T03-22-00Z__successor-admission-p0219-routing-tax-dual.md`.

P13 proved the exact deterministic dual, for a closed-edge set `C` in the directed square grid,

\[
U_n(C)=\max_{A\subseteq V_n}
\left( |C\cap\delta^+(A)|-|\delta^-(A)|\right), \tag{2.1}
\]

whereas restricting the maximum to coordinate downsets gives the abstract poset width `W_n(C)`. Its exact integer checker found a genuine `n=4` routing-tax witness with

\[
W=2,\qquad U=3,
\]

and independently checked (2.1) against literal path-family enumeration for every closed-edge set at `n=2,3`. Thus the tempting exact identity `U=W` is false, but the source asymptotic can still hold if `U-W` is lower order.

## 3. New prior art — Method #21: ask who else has this shape

A fresh same-shape search, rather than an exact-title search for Aldous's conjecture, found a much closer theorem than the previously used Seppäläinen bridge:

Anne-Laure Basdevant, Jean-Baptiste Gouéré and Marie Théret,
*First-order behavior of the time constant in Bernoulli first-passage percolation*,
Ann. Appl. Probab. **32** (2022), 4535--4567,
DOI `10.1214/22-AAP1795`, arXiv `2106.12266`.

For Bernoulli **bond** FPP, an edge has passage time `0` with probability `epsilon` and time `1` otherwise. Their Theorem 1 proves

\[
\boldsymbol\mu_\epsilon(z)
=\|z\|_1-\mathbf C(d_1(z),d_2(z))\gamma(z)
\epsilon^{1/d_1(z)}+o(\epsilon^{1/d_1(z)}).
\]

Their Proposition 3 gives, in the two-dimensional diagonal bond case,

\[
\mathbf C(2,0)=2^{3/2}. \tag{3.1}
\]

Equally important for P0219, Section 3 first defines a discrete **oriented bond score** `S^D_epsilon`. Lemma 15 identifies its small-`epsilon` limit with the semi-continuous Hammersley score, and Section 3.3 / Lemma 18 proves that ordinary non-oriented Bernoulli FPP has the same first-order term as that oriented score. Their proof explicitly extracts a maximal monotone subsequence of zero-time edges and controls the extra non-monotone gain by a path-counting/Chernoff argument; “doubly open” sites occur with probability `O(epsilon^2)`.

Fresh queries on 2026-09-19 included the exact Aldous title, `"oriented percolation flows"`, the Basdevant--Gouéré--Théret title, the DOI, and combinations of `Aldous`, `Hammersley`, `Bernoulli FPP`, and `2^{3/2}`. I found no paper explicitly stating Aldous's `1-v(p)` conjecture as a corollary. That is negative search evidence only, not a novelty certificate.

This changes the research picture materially: the continuum/Hammersley constant and the relevant **two-orientation bond** discretization are already rigorously controlled in the literature. The missing step is now the effect of the routing freedom in Aldous's cut/path-cover functional.

## 4. Method #18: say it in another language — exact free-backstep passage formulation

Put

\[
q=1-p,
\]

so Aldous-closed edges have density `q`. Wire the left/bottom source boundary to a super-source and the top/right sink boundary to a super-sink. For a valid source-side cut `A`, write `O` for the open (`p`) primal edges and `C` for the closed (`q`) primal edges. Its open capacity is

\[
\operatorname{cap}(A)=|O\cap\delta^+(A)|.
\]

The deterministic directed divergence identity gives

\[
|\delta^+(A)|-|\delta^-(A)|=K_n,
\]

where `K_n=2n+O(1)`; the exact `O(1)` corner convention is the same harmless boundary convention already present in Aldous's `U` complement statement. Therefore

\[
K_n-\operatorname{cap}(A)
=|C\cap\delta^+(A)|-|\delta^-(A)|. \tag{4.1}
\]

Thus P13's dual score is not merely a path-cover curiosity: it is exactly the **bulk max-flow deficit** score.

In the planar dual, (4.1) has a useful passage-time interpretation. Traverse a separating dual contour from one corner to the opposite corner. A crossing of a primal edge in the positive/outgoing direction costs

- `1` if the primal edge is Aldous-open,
- `0` if it is Aldous-closed,

while a crossing in the negative/incoming direction costs `0` regardless of the primal state. Call the resulting minimum dual passage time `T_n^free(q)`. Up to the `O(1)` boundary convention,

\[
K_n-V(n,1-q)=K_n-T_n^{\rm free}(q). \tag{4.2}
\]

This is the clean category change: **P0219 is a small-defect first-passage problem with free backward steps.** Standard Bernoulli FPP charges a backward Aldous-open crossing one unit; the P0219 functional rebates exactly that unit. This is why Basdevant--Gouéré--Théret is extremely close but does not, without another argument, immediately settle the source.

The P13 routing-tax witness is precisely a finite witness that the free-backstep model can beat the purely monotone/Hammersley model.

## 5. Method #4: prove something weaker, completely — the conjectured constant is a rigorous lower bound

The Basdevant--Gouéré--Théret theorem nevertheless gives one side of Aldous's conjecture essentially for free.

### Proposition (one-sided P0219 asymptotic)

With Aldous's normalization,

\[
\boxed{
\liminf_{p\uparrow1}
\frac{1-v(p)}{\sqrt{1-p}}
\ge \sqrt2 .
}
\tag{5.1}
\]

### Proof

Set `q=1-p`. Restrict the dual separators in (4.2) to monotone corner-to-corner contours. A monotone contour has no negative/incoming steps, so its `free` passage cost is simply the number of Aldous-open primal edges that it crosses. After a square-lattice rotation/reflection, Aldous-closed primal edges become the zero-time edges in the diagonal Bernoulli bond model of Basdevant--Gouéré--Théret with parameter `epsilon=q`.

Their discrete oriented bond score `S_q^D(0,(n,n))` is built from strict monotone sequences of such zero-time edges. By the bond analogue of their Lemma 4, the selected sequence can be threaded by a monotone path whose passage time is at most

\[
2n-S_q^D(0,(n,n)).
\]

Using that monotone path as a valid separating dual contour gives, with only the endpoint/corner `O(1)` discrepancy,

\[
K_n-V(n,1-q)
\ge S_q^D(0,(n,n))-O(1). \tag{5.2}
\]

By definition of their mean directional score,

\[
\lim_{n\to\infty}\frac1n
\mathbb E S_q^D(0,(n,n))
=\sigma_q^D(1,1).
\]

Lemma 15 and Proposition 3 in their bond section yield

\[
\sigma_q^D(1,1)
=2^{3/2}\sqrt q+o(\sqrt q) \qquad(q\downarrow0). \tag{5.3}
\]

Aldous has `V(n,p)/(2n) -> v(p)` in `L^1`, and `K_n/(2n)->1`. Divide (5.2) by `2n`, take `n->infinity`, then `q->0`, and use (5.3):

\[
1-v(1-q)
\ge \frac12\left(2^{3/2}\sqrt q+o(\sqrt q)\right)
=\sqrt{2q}+o(\sqrt q).
\]

This is (5.1). ∎

This proposition is a **derived corollary of published 2022 prior art plus elementary planar duality**, not a novelty claim. I found no explicit statement of it in the bounded search, but absence from search results is not evidence of priority.

## 6. What remains: one sharply formulated lemma

The source conjecture is now reduced to the matching upper bound

\[
\limsup_{q\downarrow0}
\frac{1-v(1-q)}{\sqrt q}
\le \sqrt2. \tag{6.1}
\]

In the free-backstep language, it is enough to prove the first-order equivalence

\[
\boxed{
\mu_q^{\rm free}(1,1)
=2-2^{3/2}\sqrt q+o(\sqrt q),
}
\tag{6.2}
\]

where `mu_q^free` is the asymptotic passage constant of (4.2). Equivalently, in the P13 path-cover language it is enough to prove

\[
\boxed{
\lim_{q\downarrow0}
\frac1{\sqrt q}
\limsup_{n\to\infty}
\frac{\mathbb E[U_n(C_q)-W_n(C_q)]}{n}=0.
}
\tag{6.3}
\]

The exact `n=4` witness means (6.3) cannot be replaced by `U=W`.

The strongest new route is to port Basdevant--Gouéré--Théret's Section 3.3 proof of Lemma 18 to (6.2). Their argument already proves that ordinary backward detours do not improve the `sqrt(q)` coefficient. Our model changes only one local accounting rule: a backward crossing of an Aldous-open edge receives a one-unit rebate. The required adaptation is therefore not a new Hammersley limit theorem; it is a modified version of their Lemma 19 / union-bound estimate showing that paths collecting a `delta n sqrt(q)` advantage from these rebates have exponentially small probability. P13's exact witness says such rebates can matter finitely, but its minimal witness size four is consistent with a genuinely higher-order density effect.

This is substantially narrower than the previous `interchange the limits somehow` obligation.

## 7. Status and next methods

P0219 still remains `PENDING_NOT_READY`, not because the source is vague, but because the controlling queue has not admitted it and because the free-backstep upper bound (6.2) has not been checked against the full Bernoulli-FPP prior art. No claim was created.

The next nonrepeating Section-B moves for this lead are **#5 add a parameter and differentiate**, **#13 find what only increases**, and **#30 localize one scale/direction at a time**. Concretely: interpolate a backward-step cost `lambda in [0,1]` between the P0219 free model (`lambda=0`) and ordinary FPP (`lambda=1`), and try to show the derivative of the time constant contributes only `O(q)` uniformly near `q=0`. Since `q=o(sqrt(q))`, that would prove (6.2) in one stroke.

No audit is requested: P0219 is not admitted or closed. No new checker is created in this report; the only finite statement used is P13's already executed exact checker and its archived output.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  track: R01
  category: CLOSABLE_OUTSIDE
  frozen_source:
    id: I0024
    source: "Aldous--Fill, Open Problem 3.44"
    metric_name: "smallest uniform multiplicative distortion C"
    metric_before: 1
    metric_after: 1
    status: "PROVED_FROZEN_AUDITED"
    audits:
      - R20_PASS
      - P26_PASS
  active_successor:
    claim: null
    state_before: PENDING_ADMISSION
    state_after: PENDING_ADMISSION
    metric_name: UNMEASURED
    metric_before: UNMEASURED
    metric_after: UNMEASURED
    movement: false
    unchanged_runs: NOT_STARTED
  tried_moves: [21, 18, 4]
  replenishment_lead:
    id: P0219
    source: "David Aldous, A discrete Hammersley process as an extreme case of oriented percolation flows"
    source_endpoint: "1-v(p) ~ sqrt(2(1-p)) as p -> 1"
    lifecycle: PENDING_NOT_READY
    new_prior_art:
      citation: "Basdevant--Gouere--Theret, Ann. Appl. Probab. 32 (2022), DOI 10.1214/22-AAP1795"
      bond_diagonal_constant: "2^(3/2)"
      oriented_nonoriented_first_order_equivalence: true
    new_reduction:
      formulation: "Bernoulli bond FPP with zero-cost backward dual crossings"
      proved_one_sided_source_bound: "liminf_{p->1} (1-v(p))/sqrt(1-p) >= sqrt(2)"
      novelty_status: "DERIVED_FROM_PUBLISHED_PRIOR_ART; NOT_CLAIMED_NOVEL"
      remaining_lemma: "mu_free(q;1,1)=2-2^(3/2)*sqrt(q)+o(sqrt(q))"
      equivalent_routing_tax: "E[U-W]/n=o(sqrt(q)) after n->infinity then q->0"
    neighboring_exact_evidence:
      report: "proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T03-22-00Z__successor-admission-p0219-routing-tax-dual.md"
      finite_witness: "n=4, W=2, U=3"
      checker_status: "ALL_EXACT_P0219_ROUTING_TAX_CHECKS_PASS"
  repository_admission:
    E_READY_CLOSABLE: "0 -> 0"
    claim_created: false
  remaining_obligation: >-
    Do not admit P0219 until the coordinator ownership/current-status gate is satisfied.
    Mathematically, port the 2022 bond-FPP oriented-vs-nonoriented estimate to
    the free-backstep passage model and prove the matching upper bound.
  next_moves: [5, 13, 30]
  audits_requested: []
  checker_created_this_report: false
```

## 9. Model / scheduler control

The operative implementation record still says the exposed scheduler has title/prompt, schedule/timing, timing mode and enabled-state controls, but **no binding model-family selector, no reasoning-effort selector, no authenticated per-run applied-model/effort receipt, and no guaranteed hour-long execution field**. Therefore `GPT-6 / maximum` remains a prompt request only on this surface.

The historical P26 `You cannot modify this task` response remains an authorization/context boundary. A real fix requires the owning authorized workspace/account/admin/API or platform-support surface to expose persistent model/reasoning fields and runtime attestation. I did not bypass permissions, duplicate the task, or change any scheduler setting.
