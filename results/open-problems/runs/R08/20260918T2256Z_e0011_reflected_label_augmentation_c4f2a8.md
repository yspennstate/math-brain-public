Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat >= b9 -> B_cat >= b10`, exact `b10>b9`; diagnostic `log10(b10/b9)=2.8160986383777242`. Unchanged count remains `0`. Methods actually used: B11, B19, B27.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: support-free reflected-label augmentation

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active source target: Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5, original two-dimensional catalyst/ZGB process with `r=infinity`, `q/2=1-p`, without added stirring.

## 1. Continuity, source status, exclusions, and ownership

I did not reopen Hasebe--Ueda Problem 3.11 (`I0082`). The canonical I0082 file is an older admission record, but the later controlling `operations/claims/E0011.md` and the immutable R08 chain retire/freeze I0082 at its explicit-candidate metric `2/3` after six unchanged runs and assign R08 exclusively to E0011. The old R08 FPP strict-convexity route remains retired from this slot.

Before research I refreshed the required repository state rather than restarting from the scheduler title: campaign `INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; `operations/NEW_METHODS_2026-09-16.md`; `operations/claims/I0082.md` and `operations/claims/E0011.md`; the newest complete R08 report `runs/R08/20260918T2129Z_e0011_thin_corridor_shield_7a91c4.md`; the newest neighboring R07 and R09 reports/commits; and exact-ID/source searches in the intake/attempt material. The large intake mirrors were target-searched rather than falsely claimed as a byte-for-byte reread of every unrelated row.

The entering certificate was

\[
B_{\rm cat}\ge b_9,
\qquad
\log_{10}b_9\approx -60.39423679122342,
\]

with the thin-corridor two-child seed at spacing `L=9`, eleven local expander stages with

\[
D=(157,167,184,201,212,221,231,248,252,269,273),
\]

and the two-order planter factor `8192/469285569`.

A fresh current-literature screen dated 2026-09-18/19 again recovered Durrett's source statement verbatim and later ZGB simulation/modified-model work but no primary theorem settling the exact original no-stirring Problem 5. In particular, a 2025 ZGB paper concerns CO desorption and critical universality, and a 2026 ZGB paper concerns reactive sulfur; neither is the source process. This is bounded negative evidence only, not a worldwide novelty certificate.

## 2. Idea before code

The preceding block event treated every interference clock outside a one-sided seven-label local language as immediate failure. That is unnecessarily asymmetric.

Reflect the local expander across its horizontal midline `y=1/2`. Three labels appear that are not in the old seven-label alphabet:

\[
O_2[(-1,0),(0,0)],\qquad CO(1,1),\qquad CO(-1,0).
\]

The middle label `CO(1,1)` enlarges the causal read support by two cells and therefore risks destroying the carefully trimmed terminal geometry and the spacing-nine 1-dependence certificate. I did not count it.

The other two reflected labels are different:

\[
\boxed{O_2[(-1,0),(0,0)],\qquad CO(-1,0).}
\]

Their entire adsorption/reaction supports are already contained in the old seven-label read set. Therefore those clock identities were already inside every old local interference cone and already contributed to the same `D`; the old certificate merely declared their occurrence fatal. Reclassifying them from `failure` to `allowed transient move` can only enlarge the certified path family without changing any protected geometry.

This is the new route.

## 3. B11 — dualize the kill event into a Dirichlet/generator problem

The finite-window all-history recursion can be viewed as a killed Markov chain. The old seven-label language defines transient transitions, while all other clocks in the interference cone are sent to a cemetery state. The good event is hitting the vacancy target before the fixed window ends without first hitting the cemetery.

The corresponding infinite-horizon object is the Dirichlet problem

\[
h=Qh+q,
\]

or, in continuous time, the analogous killed-generator equation. Solving the full inverse `(I-Q)^{-1}` is not yet necessary. The useful dual observation is more elementary:

> before lengthening the horizon, move every support-free clock that is currently in the cemetery but whose exact transition can be tracked inside the existing state space back into `Q`.

The two labels above do exactly this. Because their support is already contained in the old read set, this dualization has zero geometric cost: the state descriptor, protected clock family, `D` values, block horizon, parent/child cylinders, and distance-two disjointness are unchanged.

The full absorption calculation remains a next-step route rather than a claimed theorem here. This run moves the metric using only the already frozen eight-arrival finite recursion.

## 4. B19 — make the support-preserving augmentation an exact algorithm

Let `A_7(n,s)` be the old integer-weighted sum over all length-`n` seven-label histories from local stable descriptor `s`, including exact reaction races. Define `A_9(n,s)` identically after adding the two safe reflected labels.

The exact algorithm is:

1. enumerate all `50,785` stable full boundary states and project them to the old `12,201` relevant descriptors;
2. enumerate the generated-shield class `7,255 -> 1,743` descriptors for later horizontal stages;
3. reuse the old local transition weights (`72` for a CO label before normalization, `36` for an O2 label before normalization);
4. run the same `n<=8` prefix dynamic program, but over nine labels rather than seven;
5. for the terminal trimmed stage delete `CO(1,0)` as before, giving an eight-label terminal language instead of the old six-label language;
6. scan the same integer Poisson means `1,...,8`; the exact optimum remains `lambda=2` in every stage;
7. multiply the eleven exact stage minima and the unchanged planter factor.

Two finite checks make the mechanism visible. On the full base descriptor class,

\[
\min_s A_7(4,s)=127,650,816,
\qquad
\boxed{\min_s A_9(4,s)=134,369,280}.
\]

At the terminal stage,

\[
\min_s A_6(5,s)=5,724,131,328,
\qquad
\boxed{\min_s A_8(5,s)=48,399,814,656}.
\]

The terminal gain is especially large because the reflected clocks repair configurations that were expensive for the one-sided trimmed language.

## 5. B27 — compile `for every boundary, choose an orientation` into one universal language

The tempting quantifier-swapped formulation is

\[
\forall\eta\ \exists\sigma\in\{\text{top-oriented},\text{bottom-oriented}\}
\quad\text{such that the local stage succeeds well from }\eta.
\]

That statement alone is awkward for a block construction because the choice of orientation could depend on an unknown exterior configuration.

The support-preserving augmentation compiles both orientations into one fixed stochastic language. We do not choose an orientation after seeing the boundary. Instead, the good event accepts histories from both sides simultaneously, and the exact recursion sums them. Thus the source-valid universal quantifier remains in the correct order:

\[
\exists\text{ one fixed nine-label event}\quad
\forall\eta\text{ stable},
\]

while still benefiting from the reflected route.

This is the useful outcome of B27. The full ten-label vertical symmetry closure was deliberately rejected because `CO(1,1)` enlarges the support and would require a new dependence-geometry proof.

## 6. Geometry and deterministic implication are unchanged

No new clock identity lies outside the old read support. Therefore every protected-set count and every spatial disjointness statement from `b9` remains valid.

The deterministic block implication is still

\[
\boxed{\text{one seed occurrence}\Longrightarrow
\text{two seed occurrences at offsets }0\text{ and }9.}
\]

The original parent survives as the left child; the thin vacancy cursor propagates right; the two rotated guard stages clear the final child buffer; and the two-order planter creates the right child. The full protected clock families of blocks separated by `2L=18` remain disjoint, hence the good-block field remains 1-dependent.

Because the target of every augmented local recursion is exactly the same full six-cell vacancy target as before, no generated-shield or planter hypothesis is weakened.

## 7. Exact metric movement

Write `p_j^{(7)}` for the old exact local stage probability and `p_j^{(9)}` for the support-augmented probability; for the terminal stage read `(6)` and `(8)` instead. Every single stage improves strictly.

The diagnostic log gains, in stage order, are

\[
0.3010997,\ 0.2565684,\ 0.2559583,\ 0.2554501,\ 0.2551643,
\]
\[
0.2549514,\ 0.2547340,\ 0.2544044,\ 0.1256621,
\ 0.3010533,\ 0.3010526.
\]

With the same planter factor, define

\[
\boxed{
b_{10}:=
\frac{8192}{469285569}
\prod_{j=1}^{11}p_j^{\rm aug}.
}
\]

The checker proves by exact rational arithmetic

\[
\boxed{b_{10}>b_9}.
\]

The exact multiplicative gain is the rational number archived in the checker output; diagnostically,

\[
\boxed{\log_{10}(b_{10}/b_9)=2.8160986383777242},
\]

so

\[
\frac{b_{10}}{b_9}\approx654.784874054.
\]

The block-bound scale moves from

\[
\log_{10}b_9\approx-60.39423679122342
\]

to

\[
\boxed{\log_{10}b_{10}\approx-57.57813815284567}.
\]

Thus the frozen metric genuinely moves:

\[
\boxed{B_{\rm cat}\ge b_{10}>b_9.}
\]

This is still astronomically below the sufficient closure threshold `63/64`; the source problem therefore remains **PARTIAL / OPEN_CURRENT_BOUNDED**, not proved.

## 8. What failed / what changed

**B11 DUALIZE.** A full absorbing-chain inverse was not needed to obtain movement. Its useful contribution was identifying that the old cemetery set contained clocks whose transitions are already representable in the old finite state space. Moving those clocks into the transient generator is the right direction. The remaining absorption calculation is still open.

**B19 MAKE IT AN ALGORITHM.** The safe augmentation is completely mechanical: close the local alphabet under reflected labels only when their support is already contained in the frozen read set, then rerun the exact prefix recursion. This produced a 654.8-fold block improvement without changing geometry.

**B27 SWAP THE QUANTIFIERS.** Choosing a top/bottom orientation separately for each exterior would have the wrong operational quantifier order. Summing both support-compatible orientations inside one fixed good event avoids that problem and preserves universal exterior validity.

The important negative diagnostic is that **full** reflection closure is not free. `CO(1,1)` introduces new read cells and would require a new terminal/dependence construction. I did not count any gain from it.

## 9. Next new-method triple

The next nonrepeating methods are **B14 / B24 / B30**:

- **B14 FIND THE GROUP ACTING:** compute the maximal subgroup/semigroup closure of local adsorption labels whose supports stay inside each frozen interference cone; the present two labels are only the first safe reflection closure.
- **B24 FIND THE EXTREMAL OBJECT:** among all support-preserving label alphabets, maximize the exact worst-boundary hitting probability rather than hand-selecting labels.
- **B30 ONE SCALE / ONE DIRECTION AT A TIME:** solve that extremal finite-state problem for one horizontal stage and the terminal stage separately before changing the global seed geometry.

The route worth pursuing is now clear: enlarge the **accepted local dynamics** without enlarging the **causal cone**. That changes the probability at every repeated stage while keeping the expensive 1-dependence proof intact.

## 10. Exact artifacts and self-check status

Self-check only, not an independent audit:

- `artifacts/R08/20260918T2256Z_e0011_reflected_label_augmentation_check.py`
- `artifacts/R08/20260918T2256Z_e0011_reflected_label_augmentation_check.out`

The archived execution begins

`PASS exact R08/E0011 reflected-label augmentation certificate`

and verifies the descriptor counts, support containment, unchanged terminal read set, local old/new minima, all eleven strict stage improvements, and exact `b10>b9`.

No closure audit is requested because the source problem remains open.

## 11. Model/scheduler control status

The exposed scheduler/update interface still has fields for prompt/title/schedule/timing/enabled state but no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. Therefore `GPT-6 / maximum` remains prompt text and cannot be certified or enforced from this run. The actual model available to this run is GPT-5.6 Sol; reasoning metadata is UNVERIFIED.

The repository's newer deployment evidence records that P26's full prompt update later succeeded from an authorized P/C context, so the older `You cannot modify this task` error was context-specific rather than proof of a universal scheduler defect. For a task that still rejects edits, the legitimate route is its authorized owning context, a supported ownership/admin transfer, or platform support. I made no scheduler changes.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  lane: CLOSABLE_OUTSIDE
  active_claim: E0011
  source: Durrett_2009_Problem_5_no_stirring_catalyst_ZGB
  metric: B_cat
  before: ">= b9"
  after: ">= b10"
  before_log10_diagnostic: -60.39423679122342
  after_log10_diagnostic: -57.57813815284567
  log10_gain_diagnostic: 2.8160986383777242
  exact_movement: true
  status: PARTIAL
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods: [11, 19, 27]
  next_methods: [14, 24, 30]
  artifacts:
    - artifacts/R08/20260918T2256Z_e0011_reflected_label_augmentation_check.py
    - artifacts/R08/20260918T2256Z_e0011_reflected_label_augmentation_check.out
  shared_root_edits: false
  scheduler_changes: false
  closure_audits_requested: false
```
