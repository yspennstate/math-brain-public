Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat: >= b1 -> >= b2 = b1*(432^432/432!)`, an exact multiplicative gain `432^432/432! > 1` (about `10^185.8983`); unchanged count remains `0`. Methods used: B4, B11, B18.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: Poissonized embedded-chain certificate

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, and source status

I continued from the newest complete R08 report

`runs/R08/20260918T1353Z_e0011_ensemble_amplification_4c2d9a.md`

rather than restarting the stale native title. The active exclusive claim remains `operations/claims/E0011.md`: Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5, for the original two-dimensional catalyst/ZGB process with `r=infinity`, `q/2=1-p`, and **no added stirring**.

Hasebe--Ueda Problem 3.11 / I0082 remains **RETIRED/FROZEN at `2/3` after six supported unchanged runs**. I did not reopen it. The old R08 FPP strict-convexity route likewise remains retired from this slot.

At run start I reread the required controlling repository state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0082.md`, `operations/claims/E0011.md`, the newest R08 report, current neighboring R07/R09 reports, and the E-intake/attempt records. The intake still records E0011 as Durrett Problem 5, historically attempted but unresolved; the canonical current ownership file remains exclusively R08. No ownership collision was found.

I also refreshed the literature screen on 2026-09-18. Queries included exact combinations of `Durrett Problem 5`, `Coexistence in stochastic spatial models`, `ZGB`, `catalyst`, `no stirring`, `coexistence`, and later rigorous results. The search recovered Durrett's 2009 source and the older modified-model/fast-stirring literature but no later primary theorem settling the original no-stirring Problem 5. This remains **bounded negative evidence only**, not a claim of worldwide bibliographic completeness or novelty.

## 2. Frozen metric before this run

The active metric remains

\[
B_{\rm cat}=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite protected Harris-block certificates at `p_0=1/2`, and `b(C)` is an exact certified lower bound on the good-block probability.

The preceding run proved

\[
B_{\rm cat}\ge b_1,
\]

with

\[
 b_1=
K\,\frac{35}{486}\left(\frac1{72}\right)^{20}
\left(\frac{32}{87}\right)^{432}
\left(\frac1{301}\right)^{328}
\left(\frac1{602}\right)^{104},
\]

where

\[
K=2^{24}\binom{20}{10}=3,099,691,319,296.
\]

This is algebraically the same lower bound written in the previous report as

\[
K\,\frac{35}{486}\left(\frac1{72}\right)^{20}
\left(\frac{32}{26187}\right)^{328}
\left(\frac{16}{26187}\right)^{104}.
\]

The central question this run was whether the remaining `e^{-432}` synchronization cost is intrinsic or merely an artifact of splitting the fixed horizon into 432 one-event slots.

## 3. B18 — say the protected Harris process in the right language

Inside the already certified protected block there are

- 144 protected CO site clocks, each of rate `1/2` at `p=1/2`;
- 314 protected O2 edge clocks, each of rate `1/4`.

Hence the total protected adsorption process is a homogeneous Poisson process of rate

\[
\Lambda=144\cdot\frac12+314\cdot\frac14=\frac{301}{2}.
\]

Conditional on a protected adsorption mark occurring, its label is independent of its arrival time. A specified CO-site label has conditional probability

\[
\frac{1/2}{301/2}=\frac1{301},
\]

and a specified O2-edge label has conditional probability

\[
\frac{1/4}{301/2}=\frac1{602}.
\]

Thus the block decomposes exactly into two independent pieces:

1. a scalar Poisson count/timing process `N(t)` of rate `301/2`;
2. an embedded discrete jump chain of adsorption labels, followed by the already-accounted instantaneous reaction races.

This is the useful language change. The deterministic 432-mark implication depends on the **ordered labels and reaction outcomes**, not on which equal subslot each mark happens to occupy.

## 4. B11 — dualize the certificate into count mass times embedded-chain weight

Let `H` be the family of the `K` pairwise disjoint successful 432-label histories from the preceding run. Every `h in H` contains exactly

\[
N_{CO}=328,\qquad N_{O_2}=104,
\]

and, conditional on its labels, has reaction-success probability at least

\[
q_{\rm react}=\frac{35}{486}\left(\frac1{72}\right)^{20}.
\]

For any deterministic horizon `T`, the probability that exactly 432 protected marks occur and that their ordered embedded-chain history lies in `H` is

\[
P(N(T)=432)\;K\;q_{\rm react}
\left(\frac1{301}\right)^{328}
\left(\frac1{602}\right)^{104}.
\]

This is already a finite source-valid Harris event. If exactly 432 protected marks occur in `[0,T]`, there is no later protected mark before the deterministic block endpoint to spoil the two child seeds. Uncontrolled marks outside the protected block cannot affect the active rectangle by the two-layer locality argument already checked in the positive-certificate report.

For a fixed required count `M`, the Poisson mass `e^{-Lambda T}(Lambda T)^M/M!` is maximized at `Lambda T=M`. Therefore choose exactly the same total horizon as the old slot construction,

\[
T=\frac{432}{301/2}=\frac{864}{301}.
\]

Then

\[
P(N(T)=432)=e^{-432}\frac{432^{432}}{432!}.
\]

The preceding run proved the exact elementary bound `e<87/32`, so

\[
e^{-432}>\left(\frac{32}{87}\right)^{432}.
\]

Consequently the same deterministic block implication gives the new rational certificate

\[
\boxed{
 b_2:=
K\,\frac{35}{486}\left(\frac1{72}\right)^{20}
\left(\frac{32}{87}\right)^{432}
\frac{432^{432}}{432!}
\left(\frac1{301}\right)^{328}
\left(\frac1{602}\right)^{104}.
}
\]

Since

\[
432!<432^{432},
\]

we have the exact strict improvement

\[
\boxed{b_2=b_1\frac{432^{432}}{432!}>b_1.}
\]

Thus the frozen metric moves:

\[
\boxed{B_{\rm cat}\ge b_2.}
\]

No approximation is needed for the claim. For scale only,

\[
\log_{10}\frac{432^{432}}{432!}\approx185.898300598692,
\]

so the certified lower-bound scale improves from approximately

\[
\log_{10}b_1\approx-1315.49327
\]

to

\[
\log_{10}b_2\approx-1129.59497.
\]

The gain is about **185.9 decimal orders of magnitude** without changing the deterministic 432-mark construction at all.

## 5. B4 — prove the weaker timing theorem completely before attacking the full Dirichlet problem

The conceptual lemma proved here is more general than this one block but much weaker than coexistence:

> **Poissonized-history lemma.** Suppose a protected Harris block has total protected rate `Lambda`, and a family `H` of successful ordered histories all have the same length `M`. Let `W(H)` be the total embedded-chain/reaction probability of those histories conditional on `M` protected arrivals. Then at the deterministic horizon `T=M/Lambda`, the event `N(T)=M` and `history in H` has probability
> \[
> e^{-M}\frac{M^M}{M!}\,W(H).
> \]
> Relative to an equal-slot certificate that demands exactly one protected arrival in each of `M` slots of length `1/Lambda`, this gains the exact factor
> \[
> \frac{M^M}{M!}.
> \]

The proof is one line after Poisson thinning: the count distribution is Poisson and the ordered labels conditional on the count are i.i.d. with the normalized clock rates. The factor is strict for `M>1` because `M!<M^M`.

This matters because it identifies another large piece of the old tiny probability as an artifact of the certification language rather than the source dynamics.

## 6. Exact finite self-check

The new arithmetic core is executed and archived at

`artifacts/R08/20260918T1425Z_e0011_poissonized_jumpchain_check.py`

with output

`artifacts/R08/20260918T1425Z_e0011_poissonized_jumpchain_check.out`.

It verifies exactly:

```text
M=432
Lambda=301/2
T=864/301
Lambda*T=432
K=3099691319296
p_CO_label=1/301
p_O2_label=1/602
b2=b1*(432^432/432!)
gain_exact_gt_1=True
b2_gt_b1=True
```

The floating-point logarithms printed by the script are diagnostics only. The metric movement is an exact rational inequality. This remains a **self-check**, not an independent audit.

## 7. What remains after removing the slot artifact

This run does **not** prove coexistence and does not approach the sufficient `63/64` block threshold numerically. Even after another `10^185.9` improvement,

\[
b_2\ll63/64.
\]

The useful structural conclusion is sharper than before:

- the earlier fixed reaction-priority penalty was mostly artificial and was removed in the preceding run;
- the equal-time-slot synchronization penalty was also artificial and is removed here;
- what now dominates is the **embedded-chain history weight itself**: forcing a highly specific sequence of 328 CO labels and 104 O2 labels.

So the next serious route is not another timing optimization. It is to solve or lower-bound an **absorbing Dirichlet/hitting-probability problem for a reduced local state space**, which automatically sums many different successful label orders.

Formally, for a finite protected local module with embedded transition matrix `P`, target set `G`, and failure set `F`, the all-histories success function satisfies

\[
h=Ph\quad\text{off }G\cup F,\qquad h|_G=1,\qquad h|_F=0.
\]

The current certificate lower-bounds `h` by summing a very sparse family of paths. Closing the gap requires a symmetry/state quotient small enough that this Dirichlet system can be solved or bounded exactly while retaining the worst-boundary guarantee.

## 8. Honest status

**Proved this run:** the exact Poisson/embedded-chain factorization for the existing protected block; optimal count horizon `T=864/301`; the source-valid exactly-432-arrivals event; the exact rational lower bound `b_2`; and the strict movement factor `432^432/432!`.

**Not proved:** any high-probability block event, supercritical oriented percolation, coexistence, or Durrett Problem 5 itself. No novelty claim is made for the elementary Poissonization lemma; the mechanism is standard. Its use here is a new repository route improvement, not a priority assertion.

Track status remains

\[
\boxed{\text{PARTIAL / source OPEN under bounded current-literature checking}.}
\]

Because the frozen metric moved, the unchanged count remains zero and the Section-I stuck protocol is not triggered.

## 9. Next new methods

Do not repeat B4/B11/B18 next run. Also do not return to earlier E0011 moves B7/B16/B26, B15/B19/B24, B3/B20/B25, or B9/B13/B28.

The next genuinely unused triple is:

- **B8 DISCRETIZE.** Build the smallest exact local embedded chain whose target is one-column vacancy propagation, with failure defined only by source-valid interfering marks; enumerate the reachable stable states rather than full `3^n` configurations.
- **B14 FIND THE GROUP ACTING.** Quotient that local chain by vertical reflection, translations, and species/geometry symmetries that preserve the source rates at `p=1/2`; the goal is a tractable exact Dirichlet system.
- **B27 SWAP THE QUANTIFIERS.** Instead of proving one fixed word works for every stable boundary, search for one boundary-oblivious policy whose *hitting probability* is uniformly bounded below over every stable boundary. This is stronger than choosing a different policy for each boundary and is the form that can iterate in a block construction.

The next metric target is an exact worst-boundary local hitting probability that strictly dominates the sparse-history lower bound enough to change the per-column exponential rate, not another global timing factor.

## 10. Model/runtime control status

The scheduler/runtime control situation is still unchanged in this exposed interface. The available automation update surface provides `title`, `prompt`, `schedule`, `timing_mode`, and `is_enabled`; it exposes **no binding model-family selector, reasoning-effort selector, or authenticated completed-run model telemetry**. Therefore `GPT-6 / maximum` remains prompt text only here, and this report correctly states the actually exposed runtime identity as GPT-5.6 Sol with reasoning level UNVERIFIED.

The historical P26 `You cannot modify this task` error is now known from `RESULTS.md` to have been context-specific: a later full P26 update succeeded from an authorized P/C context. For any task that still refuses modification, the legitimate remedy is the authorized owning context, supported owner/admin transfer, or platform support. Repository edits and duplicate jobs do not enforce a runtime model. No scheduler modification was attempted in this run, consistent with the current deployment restriction.

## 11. Structured ledger delta (own immutable report only)

```yaml
ledger_delta:
  worker: R08
  predecessor: I0082
  predecessor_state: RETIRED_FROZEN
  predecessor_metric: 2/3
  predecessor_retirement_count: 6
  target: E0011
  source: Durrett_2009_Problem_5
  allocation: CLOSABLE_OUTSIDE
  owner: R08
  metric: B_cat
  before: ">= b1 = K*(35/486)*(1/72)^20*(32/87)^432*(1/301)^328*(1/602)^104"
  after: ">= b2 = b1*(432^432/432!)"
  movement: positive
  exact_gain: "432^432/432! > 1"
  approximate_log10_gain: 185.898300598692
  unchanged_count_before: 0
  unchanged_count_after: 0
  source_status: OPEN_CURRENT_BOUNDED
  track_status: PARTIAL
  closure: false
  audits: 0/2
  self_check: artifacts/R08/20260918T1425Z_e0011_poissonized_jumpchain_check.py
  self_check_output: artifacts/R08/20260918T1425Z_e0011_poissonized_jumpchain_check.out
  methods: [4, 11, 18]
  next_methods: [8, 14, 27]
  predecessor_reopened: false
  old_fpp_reopened: false
  shared_root_writes: false
  email: false
  drive: false
  public_posting: false
  scheduler_changes: false
```
