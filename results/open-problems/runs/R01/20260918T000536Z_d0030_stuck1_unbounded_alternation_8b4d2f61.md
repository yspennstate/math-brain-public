Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family or reasoning-effort selector, so I do not claim otherwise. **NO FIXED-METRIC MOVEMENT on active D0030: `E_phi_rho = 0 -> 0`; unchanged count `3 -> 4`; status `OPEN / PARTIAL / STUCK_RECOVERY_1 / THINKING_ONLY`; methods #20 FIND WHY THE ALGORITHM FAILS, #22 READ THE FAILURES, #27 SWAP THE QUANTIFIERS.**

# R01 — D0030 / Bradley Question 2: STUCK-RECOVERY-1 diagnosis of the unbounded-alternation barrier

Date: 2026-09-18 UTC.

Lane: **CLOSABLE OUTSIDE**.

This is the mandatory thinking-only run triggered by three consecutive complete D0030 runs without movement of the fixed source metric. I therefore do **not** add a new theorem, finite checker, numerical certificate, or refinement of the bounded-alternation lemma. The purpose of this report is to freeze the exact blocker, record why the attempted routes do not cross it, identify the simplest source-faithful special case R01 still cannot prove, identify the nearest solved literature mechanism, and select exactly one recovery action.

## 1. Continuity, repository state, ownership, exclusions

I did **not** reopen Aldous–Fill I0024. Its exact infimum-over-right-inverses characterization remains internally closed at distortion `C=1`:

\[
\tau_2=
\inf_{R:\,BR=I_{\mathcal H_0}}
\sup_{0\ne b\in\mathcal H_0}
\frac{(Rb)^TC^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with independent PASS audits

- `R20-AUDIT-R01-I0024-03`, and
- `P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10`.

Publication-level novelty of that generalized-inverse/right-inverse mechanism remains unclaimed. I also did not reopen I0113, G0012, D0057, or the old R01 FEI assignment; P03 owns FEI.

The active create-only claim remains `operations/claims/D0030.md`, owned by R01 and scoped to Richard C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys 2 (2005), Question 2, p. 114:

> If a given random sequence is phi-mixing, does it follow that it is rho-star-mixing?

The fixed source metric remains

\[
E_{\phi,\rho^*}\in\{0,1\},
\]

and it remains zero because neither a universal proof nor a source-valid stationary counterexample has been obtained.

Before this diagnosis I refreshed the required current state: campaign `INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the latest operations deployment/implementation material; the D0030 claim; the previous R01 D0030 report `runs/R01/20260917T2312Z_d0030_bounded_alternation_phi_to_rhostar_e0f79f6d.md`; the prior D0030 intake attempt; and the newest neighboring Bradley reports. The large intake JSONL corpus is connector-truncated when rendered wholesale, so I used exact-ID/source retrieval plus the canonical claim/attempt records rather than pretending to have a byte-for-byte visible reread of all approximately 780 rows.

Newest neighboring states recovered:

- R02 / D0031 has reached its six-run boundary and is `OPEN / PARTIAL / RETIRED-HANDOFF`; it is not a complete package eligible for a second-audit exchange.
- R7-01 / D0033 (the Markov-only Bradley Question 5) is `PROVED CANDIDATE / protocol closure open`, but its newest report still records P26 audit `0/1` and distinct OTHER audit `0/1`. It is therefore not yet a complete neighboring package under the owner's audit rule.

No audit budget is spent in this thinking-only run.

## 2. Exact source/current-literature check

Primary source rechecked on 2026-09-18 local / 2026-09-17 UTC:

- Bradley 2005 PDF: `https://www2.stat.duke.edu/~scs/Projects/Stable/Conditions/BradleyStrongMixingSurvey2005.pdf`.

The source explicitly says Question 2 remained unsolved there, records Bradley's expectation of YES and Walter Philipp's expectation of NO, and states the interlaced coefficient framework. It also records Theorem 2.1, under which interlaced alpha-mixing and interlaced rho-mixing are equivalent at the level of convergence to zero in the relevant stationary setting. Thus the source question can be attacked in event language without changing its answer.

Fresh bounded searches used the exact Question 2 wording and combinations of `phi-mixing`, `rho-star`, `interlaced maximal correlation`, `finite-state`, `finite-alphabet`, and Bradley's later work. They again recovered:

- Bradley 1997, *Every “lower psi-mixing” Markov chain is “interlaced rho-mixing”*, SPA 72, 221–239;
- Bradley 2001, a strictly stationary countable-state Markov chain which is rho-mixing with arbitrarily fast rate but not rho-star-mixing;
- later lower-psi / copula-Markov special-class papers.

No source-matching arbitrary stationary phi-to-rho-star resolution surfaced. A separate bounded search did not locate a theorem specifically closing even the finite-alphabet restriction. These are **negative search observations only**; they are not a worldwide openness or novelty certificate.

Bradley's 1997 abstract says that a Markov chain satisfying a condition slightly weaker than psi-mixing is rho-star-mixing, with exponential rate. Bradley's 2005 survey states the usable form: for a Markov chain, if the lower-psi coefficient `psi'(n)` is positive for some `n`, then the chain is rho-star-mixing and the decay is exponential. Later copula work likewise uses a positive lower density/minorization to get `psi'>0` and invokes Bradley's theorem.

## 3. The exact blocking statement

The previous run solved every **fixed** alternation complexity `K`, with a bound that deteriorates with `K`. The source problem asks for the supremum over all finite separated interlacings. Using Bradley's equivalence between alpha-star decay and rho-star decay, the exact source-faithful obstruction can be written as

\[
\boxed{
\text{For every strictly stationary }X,\qquad
\phi_X(n)\longrightarrow0
\quad\stackrel{?}{\Longrightarrow}\quad
\alpha_X^*(n)\longrightarrow0
\quad(\Longleftrightarrow\ \rho_X^*(n)\longrightarrow0).
}
\tag{3.1}
\]

What R01 can currently prove is only the fixed-complexity analogue. For witnesses whose merged chronological coloring has at most `K` monochromatic runs, the preceding report established

\[
\rho_K^*(n)
\le
\min\left\{1,\,2\sqrt{(2^{K-1}-1)\phi_X(n)}\right\}.
\tag{3.2}
\]

Thus (3.1) is blocked precisely at **uniformity in the number of alternating runs**. The exponential factor in (3.2) is useless when the optimizing interlacing is allowed to choose `K=K(n)\to\infty`.

This is the blocker. No additional lemma about fixed `K` changes the source metric.

## 4. Method #20 — FIND WHY THE ALGORITHM FAILS

### 4.1 Conditional peeling / operator route

The bounded-alternation proof conditions on one chronological block at a time. Each conditioning step can enlarge the remaining one-sided phi control by a factor at most two, and the Hilbert-space projection decomposition then recurses. The resulting recurrence is

\[
r_K(\varepsilon)^2
\le 4\varepsilon+r_{K-1}(2\varepsilon)^2,
\]

which produces the `2^{K-1}` loss in (3.2).

**Precise failure:** the algorithm consumes one factor of one-cut regularity every time the coloring switches. There is no regeneration/separator step in an arbitrary stationary sequence that resets the conditional law. Repeating the same peeling more carefully may improve constants, but without a new invariant or compression mechanism it still tracks the number of alternations and therefore cannot prove (3.1).

### 4.2 Why the Markov neighboring proof shape does not transfer automatically

The internal D0033 Markov candidate can use an intervening state as a separator: conditioned on that state, left and right path pieces factor, and side-separated additional conditioning preserves the factorization. An arbitrary stationary sequence has no such one-state separator. Replacing the separator by the entire gap simply moves the dependence into a larger conditioning field and does not give the product structure needed for alternation-independent tensorization.

**Precise failure:** the missing object is not another projection inequality; it is a substitute for Markov conditional factorization that survives arbitrary high-order interlacing.

## 5. Method #22 — READ THE FAILURES, NOT THE SUCCESSES

The attempted negative constructions fail for complementary reasons.

1. **Persistent global phase / shared rare marker.** If a nontrivial event is measurable from both separated sides, then conditioning on that event or its complement creates an order-one phi discrepancy. Making the shared event rare does not remove the worst-case conditioning in phi. Therefore a counterexample cannot simply hide a global phase in a rare set.

2. **Independent parallel weak channels.** Csaki–Fischer tensorization makes maximal correlation of independent joins equal to the supremum of the component correlations. Many independent weak correlations do not add up to a fixed HGR mode. Therefore a counterexample cannot be obtained by putting infinitely many independent `small phi / small rho` gadgets side by side.

3. **Finite-range scale-gadget compiler.** The first D0030 run proved that summably small finite-range phi gadgets with fixed interlaced rho would compile into a full counterexample. The compiler is sound as a route, but the required local gadget has not been found.

4. **Three-variable regrouping gadget.** Exact small-state searches suggested `R^2` on the same scale as phi. The next run then proved a three-block inequality and the full fixed-`K` estimate, so a direct local phi-analogue of Bradley's rho-only regrouping gadget cannot keep a fixed positive regrouped correlation while both chronological cut costs vanish.

5. **Growing alphabet / compactness escape.** Allowing state spaces and alternation complexity to grow is still logically available. But no construction has yet shown how to preserve a fixed interlaced mode without creating either a one-cut phi leak or a shared-tail event. Passing to a weak limit is also dangerous because the optimizing high-order events may move with the scale.

The failures all point to the same structural dichotomy: a NO example must use genuinely **collective, high-order, overlapping dependence across a number of alternating blocks tending to infinity**; a YES proof must show that phi-mixing forbids precisely that accumulation.

## 6. Method #27 — SWAP THE QUANTIFIERS

For every fixed `K`, R01 now has

\[
\phi_X(n)\to0
\quad\Longrightarrow\quad
\rho_K^*(n)\to0.
\]

The source asks whether

\[
\phi_X(n)\to0
\quad\Longrightarrow\quad
\sup_K\rho_K^*(n)\to0.
\]

The invalid inference is exactly

\[
\forall K\;\lim_{n\to\infty}\rho_K^*(n)=0
\quad\not\Rightarrow\quad
\lim_{n\to\infty}\sup_K\rho_K^*(n)=0.
\]

So the source question has become a **uniformity/interchange-of-supremum-and-limit problem** rather than a missing fixed-dimensional inequality. Any future argument that never addresses this quantifier swap cannot close D0030.

This diagnosis also explains why further exhaustive searches at a fixed alphabet and fixed number of blocks would be low-value unless they are designed to discover a dimension-free invariant.

## 7. What a complete proof must contain that no current route contains

A positive solution must supply at least one genuinely alternation-uniform mechanism, for example one of the following equivalent-in-spirit ingredients:

- a `K`-independent inequality converting all chronological one-cut phi bounds into an interlaced alpha/rho bound;
- a **compression theorem** saying that any event/correlation witness on many alternating blocks can be replaced, at controlled loss, by a witness using only boundedly many effective blocks;
- a regeneration/coupling structure derivable from phi alone which periodically resets accumulated high-order dependence;
- an event-level martingale/entropy invariant whose total cost across arbitrarily many alternations is summable rather than multiplicative.

A negative solution needs the opposite missing ingredient: an explicit strictly stationary multiscale process in which every past/future cut has uniformly vanishing conditional-probability error while a sequence of increasingly complicated alternating events retains nonzero alpha-star (equivalently rho-star) dependence. Such a construction must avoid both a common tail event and independent-product tensorization.

No route tried so far contains either ingredient.

## 8. Simplest special case still unproved by R01

The cleanest source-faithful restriction that R01 still cannot decide is:

\[
\boxed{
X\text{ strictly stationary and binary-valued (or finite-alphabet), }
\phi_X(n)\to0
\quad\stackrel{?}{\Longrightarrow}\quad
\rho_X^*(n)\to0.
}
\tag{8.1}
\]

This keeps arbitrary memory and arbitrary interlacing but removes all state-space pathologies. The bounded search this run did not locate a published theorem resolving (8.1), but that is not asserted as a literature-open certificate.

Why this is the right first special case: if even binary processes can support a negative construction, then growing alphabets are irrelevant; if finite alphabets force a positive result, the proof may expose the missing compactness or atom-counting mechanism before one attacks general state spaces.

## 9. Nearest solved problem in the literature, and what it has that D0030 lacks

The nearest clean positive theorem I found is Bradley (1997), *Every “lower psi-mixing” Markov chain is “interlaced rho-mixing”*. Its published abstract states that a Markov chain satisfying a condition slightly weaker than psi-mixing is interlaced-rho-mixing with exponential rate. Bradley's 2005 survey gives the operational statement: for a Markov chain, positivity of `psi'(n)` at some lag implies rho-star mixing, again with exponential decay.

That solved theorem has two resources the D0030 source hypothesis does not provide:

1. **Markov factorization:** a state can separate past and future, preventing dependence from accumulating indefinitely through a long alternating word.
2. **Lower-psi / relative minorization:** it controls joint probabilities from below relative to the product law. Ordinary phi controls absolute conditional-probability deviations across a one-sided cut; on very rare events this need not yield a uniform relative lower bound.

The second point is corroborated by later copula-Markov work: a density bounded away from zero gives `psi'>0`, after which Bradley's theorem supplies rho-star mixing. This is exactly the sort of regeneration/minorization mechanism absent from the arbitrary-sequence problem.

## 10. Exactly one Section-I recovery choice

I choose:

**PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The next ordinary research run will not restart the operator recursion. It will read Bradley's 1997 lower-psi Markov proof as far as accessible and extract the first exact step where either Markov factorization or positive lower-psi minorization is essential. Then it will ask whether, in the binary/finite-alphabet stationary phi-mixing case, one can replace that step by a blockwise **good-set minorization** whose exceptional mass is controlled by phi and whose constants do not depend on the number of future alternations.

A successful port would give a genuine new mechanism. A failed port must record the explicit finite-alphabet configuration that defeats the would-be minorization; that obstruction would then become the next counterexample design target.

The three Section-B moves assigned to the **next** D0030 research run are:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** target the binary/finite-alphabet restriction before the general state space;
- **#18 SAY IT IN ANOTHER LANGUAGE:** work in Bradley's equivalent interlaced-alpha/event formulation rather than HGR operator norm first;
- **#25 COUNT THE SAME THING TWICE:** count/charge alternating cylinder-event dependence against one-cut phi leakage to look for a dimension-free budget.

These differ from the present diagnostic triple and have not yet been used on D0030.

## 11. Audit gate

No second independent audit is supplied this run. R02/D0031 is a retired open handoff, not a complete package. R7-01/D0033 is mathematically `PROVED CANDIDATE` but still protocol-open with both required independent audits missing in its newest report. Under the explicit checking budget, neither is eligible for an R01 second-audit pass yet.

## 12. Model/scheduler control status and escalation boundary

The model-control limitation is still real in the exposed task surface. The available scheduler operations expose title, prompt, schedule/offset, timing mode, and enabled state. They expose **no model selector and no reasoning selector**, and there is no authenticated completed-run model/effort telemetry or guaranteed hour-long execution control. Therefore the requested GPT-6 / maximum setting remains prompt text only here.

The historical P26 `You cannot modify this task` error was authorization/context-specific. The current repository ledger records that another authorized P/C context later updated P26 successfully. The legitimate workaround is therefore an owning/authorized scheduler context or a product/platform migration that exposes the necessary controls; duplicating the task or bypassing permissions is not a valid workaround.

No scheduler change, Gmail/email, Drive action, public posting, purchase, permission change, shared-root edit, peer-file edit, or audit request was made.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R01
  lane: CLOSABLE_OUTSIDE
  frozen_original:
    id: I0024
    source: Aldous-Fill Open Problem 3.44
    metric: smallest uniform multiplicative distortion C
    before: 1
    after: 1
    status: PROVED_INTERNAL_CLOSED_FROZEN
    audit_ids:
      - R20-AUDIT-R01-I0024-03
      - P26-AUDIT-R01-I0024-AF344-SINGULAR-RIGHT-INVERSE-10
  active_target:
    id: D0030
    source: Bradley 2005 Question 2
    exact_scope: arbitrary strictly stationary phi-mixing random sequence -> rho-star-mixing?
    metric: E_phi_rho
    before: 0
    after: 0
    status: OPEN_PARTIAL_STUCK_RECOVERY_1_THINKING_ONLY
    unchanged_count_before: 3
    unchanged_count_after: 4
    tried_moves: [20, 22, 27]
    blocker: uniformity in unbounded alternation complexity; fixed-K rho-star bounds do not justify interchange of lim_n and sup_K
    simplest_unproved_by_R01: binary_or_finite_alphabet_stationary_phi_to_rhostar
    nearest_solved_literature: Bradley_1997_lower_psi_Markov_to_rhostar
    selected_recovery: PORT_TECHNIQUE_FROM_NEAREST_SOLVED_PROBLEM
    next_moves: [4, 18, 25]
    remaining_obligation: obtain an alternation-uniform mechanism, or an explicit stationary high-order counterexample; do not spend another run refining fixed-K constants
    evidence:
      - operations/claims/D0030.md
      - runs/R01/20260917T214202Z_d0030_scale_gadget_operator_6f2a91c4.md
      - runs/R01/20260917T2241Z_d0030_phi_regrouping_4e2b7c91.md
      - runs/R01/20260917T2312Z_d0030_bounded_alternation_phi_to_rhostar_e0f79f6d.md
      - Bradley 2005 Question 2 source recheck, dated 2026-09-18 local
      - Bradley 1997 lower-psi Markov theorem current literature check
    audit_ids: []
    neighbor_audit_gate:
      R02_D0031: OPEN_PARTIAL_RETIRED_HANDOFF_NOT_ELIGIBLE
      R7_01_D0033: PROVED_CANDIDATE_PROTOCOL_OPEN_0_OF_2_NOT_ELIGIBLE
```

END OF IMMUTABLE R01 REPORT
