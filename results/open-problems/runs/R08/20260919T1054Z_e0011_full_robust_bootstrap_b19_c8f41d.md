Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat >= b18_boot -> B_cat >= b19_full`, with exact factor `b19_full/b18_boot = 6002564211340/5539070962521 > 1`, numerically `1.0836770736383652`; diagnostic `log10 b18_boot ~= -49.89688548885152 -> log10 b19_full ~= -49.86198560335649`. Unchanged count remains `0`. Methods actually used: B3, B14, B19.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: unrestricted adversarial bootstrap within the existing Harris family

Run date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Active target: **E0011**, Rick Durrett, *Coexistence in stochastic spatial models* (2009), Problem 5, original two-dimensional no-stirring catalyst/ZGB process.  
Status after this run: **PARTIAL / source OPEN under bounded current-literature checking**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, source gate, ownership, and exclusions

I continued from the newest complete R08 report actually present on `master`,

`runs/R08/20260919T1045Z_e0011_robust_bootstrap_b18_6a4c2e.md`,

rather than from the stale native scheduler title.

The controlling later ownership file is `operations/claims/E0011.md`. It assigns R08 exclusively to Durrett's 2009 Problem 5 and explicitly records the predecessor Hasebe--Ueda Problem 3.11 / `I0082` as **RETIRED/FROZEN at `2/3` after six supported unchanged runs**. I did not reopen I0082, did not reprove its finite-variance exclusion, and did not reopen the old R08 FPP strict-convexity route.

Before new mathematics I refreshed the required repository state: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0011 claim, the newest own report and its exact artifacts, targeted intake/claim history for E0011/I0082, and the newest visible neighboring R07/R09 reports. R07 has retired its I0077 predecessor and is at a successor gate; R09 is likewise working successor admission on a distinct source. Neither owns E0011.

### Dated literature refresh

I reran bounded searches on 2026-09-19 for the exact Durrett source, `Problem 5`, catalyst/ZGB coexistence, and no-stirring variants. The search again recovered:

- Durrett, arXiv:0906.2293 / Ann. Appl. Probab. 19 (2009), which describes the paper as containing nine challenging and important open problems;
- the older Durrett--Swindle catalyst coexistence work with its different stirring/mobile-reactant regime;
- Fernandes--da Silva, arXiv:2501.07066 (2025), which modifies the ZGB model by allowing CO desorption and studies its critical behavior by simulation.

I did not find a later primary theorem settling the exact original two-dimensional no-stirring source statement. This is **bounded negative evidence only**, not a worldwide-open or novelty certificate.

## 2. Entering metric and the question left by the previous run

The frozen E0011 metric is

\[
B_{\rm cat}=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite protected two-child Harris-block certificates at the exact anchor `p=1/2`, with a deterministic seed-reproduction implication and a translated 1-dependent block field.

The newest sound value entering this run is

\[
B_{\rm cat}\ge b_{18,\rm boot},
\qquad
\log_{10} b_{18,\rm boot}\approx -49.89688548885152.
\]

That certificate improved only the exceptional one-column bootstrap stage. Its local entrance class is the already certified

\[
215383\text{ stable full configurations}\longrightarrow48027\text{ projected 14-cell core descriptors},
\]

and its owned first-stage hazard remains

\[
D_{\rm boot}=140.
\]

The bootstrap accepts ten halo-independent support-closed labels `L_0` and exposes four adversarial halo cells

\[
H=\{(0,-2),(0,3),(1,2),(2,1)\}
\]

that make seven further already-owned labels `L_1` locally evaluable. The previous `b18` event allowed **at most one** use of a label from `L_1` during its eight accepted arrivals. The natural stronger question is whether one can admit `L_1` arbitrarily often, while refreshing the halo adversarially before every accepted mark, without paying any new clock in the hazard or dependency family.

## 3. B3 — prove the stronger unrestricted robust bootstrap

Let `A` be the same six-vacancy bootstrap target. Let `O_n(s)` be the old-only exact reaction-weight mass after `n` accepted arrivals, and let `R_n(s)` be the unrestricted robust mass. Set

\[
O_0(s)=R_0(s)={\bf 1}_A(s).
\]

The old-only recursion is

\[
O_n(s)=\sum_{\ell\in L_0}T_\ell O_{n-1}(s).
\]

For the unrestricted robust value, before each accepted arrival the exterior chooses an arbitrary stable assignment `h` of the four halo cells **before** the random accepted clock identity is revealed. Then

\[
\boxed{
R_n(s)=
\sum_{\ell\in L_0}T_\ell R_{n-1}(s)
+
\min_{h\in\mathcal H(s)}
\sum_{\ell\in L_1}T_{\ell,h}R_{n-1}(s).
}
\tag{3.1}
\]

The seven `L_1` identities are exactly the already-owned labels from the preceding robust-bootstrap report:

\[
\begin{aligned}
&CO(0,-1),\quad CO(0,2),\quad CO(1,1),\\
&O_2[(0,-1),(0,0)],\quad O_2[(0,1),(0,2)],\\
&O_2[(0,1),(1,1)],\quad O_2[(1,0),(1,1)].
\end{aligned}
\]

No new Harris clock is introduced. Thus the local denominator, protected sigma-field, two-child deterministic implication, and the already-certified distance-two disjointness remain unchanged.

Equation (3.1) is stronger than the preceding `k<=1` recursion. If `F_n` denotes the at-most-one-new-label value from `b18`, then induction gives

\[
R_n(s)\ge F_n(s)\ge O_n(s)
\qquad\text{for every }n,s.
\tag{3.2}
\]

Indeed, assuming the inequality at level `n-1`, all transition weights are nonnegative; the old part preserves the inequality, and for each fixed legal halo `h` the new-label sum with `R_{n-1}` is at least the corresponding sum with `O_{n-1}`. Taking minima over the same halo set preserves the inequality. This is the required quantifier order: fixed event first, worst legal exterior second, random accepted clock/reaction third.

The unrestricted event therefore admits **any number of halo-dependent labels among the eight accepted arrivals**, not a preselected count or one favorable boundary trajectory.

## 4. B19 — exact branch-and-bound algorithm for the full Bellman value

I kept the same eight-arrival truncation, `D=140`, reaction-weight normalization (`72` per CO label and `36` per O2 label), and Poisson mean

\[
\lambda=4.
\]

Put `H=36D=5040`. Up to the common positive rational/exponential prefactor, define

\[
P_O(s)=\sum_{n=0}^8 4^n\frac{8!}{n!}H^{8-n}O_n(s),
\]

and define `P_R(s)` by replacing `O_n` with `R_n`.

The new exact C++ checker regenerates all **48,027** stable projected core descriptors directly. This is the same domain as the preceding 215,383-to-48,027 full-state projection: any full stable entrance projects to a stable core descriptor, while every stable core descriptor extends to a full stable entrance by setting the omitted halo coordinates vacant. Thus no entrance descriptor is lost by the direct generation.

First, the checker reproduces the old-only global minimum

\[
\min_sP_O(s)=
4642311559640512826443825152
\]

at the same core code

\[
s_*=4782752.
\]

It then evaluates the unrestricted robust value at this state and obtains

\[
P_R(s_*)=
\boxed{8119101129828730822113361920}.
\]

Because of (3.2), `P_R(s)>=P_O(s)` for every state. Therefore any state with `P_O(s)>=P_R(s_*)` cannot beat the candidate robust value. Exactly **16** of the 48,027 descriptors remain below this cutoff. The checker evaluates the full nonlinear recursion (3.1) on those 16 states and proves that the same state `s_*` is the global robust minimizer. The next excluded old-only value is

\[
8458449879232610418655494144
>
8119101129828730822113361920,
\]

so the branch-and-bound gap is strict.

At the minimizer, the unrestricted reaction-weight sequence is

```text
R_0,...,R_8 =
0, 0, 0, 0,
16422912,
59928698880,
130035279495168,
217790631675297792,
310689090961995202560.
```

The complete exact run used the following memoized state counts at levels `0,...,8`:

```text
18671, 13844, 9004, 4997, 2340, 925, 314, 86, 16.
```

This is an exact finite Bellman calculation, not simulation or a finite sample test.

## 5. Exact gain over the previous `k<=1` certificate

The preceding globally certified at-most-one-new-label polynomial minimum was

\[
P_{F_1}^{\min}=
7492177630527378997219688448.
\]

The unrestricted minimum is strictly larger, and exact reduction gives

\[
\boxed{
\frac{P_R^{\min}}{P_{F_1}^{\min}}
=
\frac{6002564211340}{5539070962521}
>1.
}
\tag{5.1}
\]

Numerically, only for scale,

\[
\frac{6002564211340}{5539070962521}
\approx1.0836770736383652,
\]

with

\[
\log_{10}\left(\frac{P_R^{\min}}{P_{F_1}^{\min}}\right)
\approx0.03489988549502421.
\]

Since the Poisson/exponential prefactor is identical, the exact unrestricted robust bootstrap probability is

\[
\boxed{
p_{\rm boot}^{(\infty)}
=
\frac{157353619261751296}
{17775044545193108258203125}
}
\approx 8.8525021055\times10^{-9}.
\tag{5.2}
\]

Every other factor of the sound `b18_boot` two-child block remains unchanged. Define

\[
\boxed{
b_{19,\rm full}:=
 b_{18,\rm boot}\,
 \frac{6002564211340}{5539070962521}.}
\]

Then

\[
\boxed{B_{\rm cat}\ge b_{19,\rm full}>b_{18,\rm boot}},
\]

with diagnostic scale

\[
\boxed{
\log_{10}b_{19,\rm full}
\approx -49.86198560335649.
}
\]

Thus the frozen metric moves again and the unchanged count remains `0`.

This remains **PARTIAL**, not coexistence: the rigorous block lower bound is still only about

\[
1.37\times10^{-50},
\]

far below the sufficient `63/64` threshold. The earlier architecture-cap calculation therefore remains decisive: constant-factor improvements of one local cylinder cannot by themselves close Durrett Problem 5.

## 6. B14 — exact symmetry search: the visible symmetry cannot quotient this Bellman problem

I also carried out the proposed group reduction before assuming it existed. The full 18-cell core-plus-halo patch has exactly **four** affine square-lattice isometries. However the Bellman operator distinguishes the 14 persistent core coordinates from the four adversarially refreshed halo coordinates, and the entrance fixes only the two vacancies `(-1,0),(-1,1)`.

Requiring an isometry to preserve simultaneously

1. the full 18-cell patch,
2. the 14-cell core as a set,
3. the four-cell halo as a set,
4. the two fixed entrance vacancies, and
5. the six-site target,

leaves **only the identity**.

The tempting reflection across `y=1/2` does preserve the full patch, fixed entrance pair, and target, but it exchanges

\[
(1,-1),(2,0)\in\text{core}
\]

with

\[
(1,2),(2,1)\in\text{halo}.
\]

That is not a valid quotient symmetry: those coordinates have different quantifiers in (3.1). The exact symmetry checker therefore rules out a nontrivial lattice-isometry quotient for the present core/halo decomposition. This method failed as a speedup, but it prevents an invalid factor-of-two/four state-space reduction.

## 7. What the three methods did

**B3 PROVE SOMETHING STRONGER — succeeded.** The previous `k<=1` adversarial event was replaced by the unrestricted event allowing arbitrarily many of the seven halo-dependent accepted labels during the eight-arrival window. The universal exterior quantifier is preserved by a fresh minimization before every accepted arrival.

**B14 FIND THE GROUP ACTING — produced a negative structural answer.** The full patch has four lattice isometries, but only the identity preserves the core/halo quantifier partition together with the entrance and target. No nontrivial exact quotient is available in this representation.

**B19 MAKE IT AN ALGORITHM — succeeded.** Pointwise domination `R>=O` turns the 48,027-state global minimization into an exact branch-and-bound problem with only 16 expensive robust evaluations. The resulting unrestricted Bellman minimum is exact and strictly improves the frozen metric.

## 8. Exact artifacts and validation status

Idea-before-code note:

- `artifacts/R08/20260919T1054Z_e0011_full_robust_bootstrap_idea.md`

Executed exact C++ Bellman / branch-and-bound checker and output:

- `artifacts/R08/20260919T1054Z_e0011_full_robust_bootstrap_check.cpp`
- `artifacts/R08/20260919T1054Z_e0011_full_robust_bootstrap_check.out`

Independent exact-rational and lattice-isometry checker/output:

- `artifacts/R08/20260919T1054Z_e0011_full_robust_bootstrap_arithmetic_symmetry.py`
- `artifacts/R08/20260919T1054Z_e0011_full_robust_bootstrap_arithmetic_symmetry.out`

Both executed outputs end in `PASS`. They are **self-checks**, not independent OTHER-track audits. No audit or closure credit is claimed this run.

## 9. Consequence for the research strategy and next methods

The full eight-arrival bootstrap Bellman problem has now been solved for the present 17-label owned alphabet. Going from `k<=1` to unrestricted use gains only about **8.37%**. Together with the earlier architecture ceiling—even a perfect terminal stage leaves the fixed upstream rare-stage product roughly 45 decimal orders below threshold—this says the next useful route must stop optimizing one local stage in isolation.

The next run should attack the **whole corridor event as one ordinary-dynamics object**, not multiply separately killed Poisson windows. A nonrepeating next triple is:

- **B1 CHANGE THE CATEGORY:** recast the complete corridor growth as one finite robust Markov decision / reachability problem whose success set is two-child regeneration, so ordinary owned clocks can help across stage boundaries instead of being killed and repaid at each stage;
- **B13 FIND WHAT ONLY INCREASES:** search for a frontier/shield monovariant on a wider seed that prevents return to the all-CO trap once enough mixed/vacant structure has formed;
- **B30 DO ONE SCALE/DIRECTION AT A TIME:** solve the full-hazard robust reachability problem first on one horizontal strip and then on the paired strip needed for a two-child block, isolating exactly what prevents gluing without reintroducing a product of rare cylinders.

The target is a **change of scale**, not another constant multiplier.

## 10. Model / scheduler-control status

The model-control limitation is unchanged. The exposed scheduler/update surface provides title/prompt, schedule or start offset, enabled state and timing mode, but **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry**. Therefore `GPT-6 / maximum` remains prompt text only here; this report states the actual available identity, GPT-5.6 Sol / UNVERIFIED, and does not claim otherwise.

The historical P26 `You cannot modify this task` denial is context-specific: the current repository ledger records that a later full P26 prompt update succeeded from an authorized P/C context, while other contexts rejected edits. A task that still rejects modification must be handled from its authorized owning context, via a supported ownership/admin transfer, or through platform support. A repository edit is not a scheduler workaround. No scheduler modification was attempted here.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R08
  lane: CLOSABLE_OUTSIDE
  predecessor: I0082
  predecessor_state: RETIRED_FROZEN
  predecessor_metric: 2/3
  predecessor_retirement_count: 6
  target: E0011
  source: Durrett_2009_no_stirring_catalyst_ZGB_problem_5
  owner: R08
  metric: B_cat
  before: ">= b18_boot; log10 ~= -49.89688548885152"
  after: ">= b19_full = b18_boot * 6002564211340/5539070962521; log10 ~= -49.86198560335649"
  movement: YES
  exact_gain: "6002564211340/5539070962521"
  gain_decimal: 1.0836770736383652
  unchanged_count_before: 0
  unchanged_count_after: 0
  status: PARTIAL
  exact_new_fact: "unrestricted adversarial bootstrap Bellman value over all 48027 core descriptors is globally minimized at code 4782752 with polynomial 8119101129828730822113361920; all but 16 states are excluded by exact old-value domination"
  robust_bootstrap_probability: "157353619261751296/17775044545193108258203125"
  symmetry_result: "18-cell patch has 4 lattice isometries but only identity preserves core/halo partition, entrance and target"
  artifacts:
    - artifacts/R08/20260919T1054Z_e0011_full_robust_bootstrap_idea.md
    - artifacts/R08/20260919T1054Z_e0011_full_robust_bootstrap_check.cpp
    - artifacts/R08/20260919T1054Z_e0011_full_robust_bootstrap_check.out
    - artifacts/R08/20260919T1054Z_e0011_full_robust_bootstrap_arithmetic_symmetry.py
    - artifacts/R08/20260919T1054Z_e0011_full_robust_bootstrap_arithmetic_symmetry.out
  self_checks_only: true
  independent_audits_new: 0
  shared_root_modified: false
  next_methods: [1, 13, 30]
```
