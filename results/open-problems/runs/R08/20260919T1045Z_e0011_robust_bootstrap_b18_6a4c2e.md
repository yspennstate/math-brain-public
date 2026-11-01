Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat >= b17_rob -> B_cat >= b18_boot`, with exact factor `b18_boot/b17_rob = 3035047884064870809017076077339859545315170762500000000000000000000 / 1906467115341816615178741523321245913280178771097328202961614705231 > 1`, numerically `1.591974946560097`; diagnostic `log10 b17_rob ~= -50.09882171767006 -> log10 b18_boot ~= -49.89688548885152`. Unchanged count `2 -> 0`. Methods actually used: B5, B15, B16.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: robustifying the expensive bootstrap without paying any new hazard

Date: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Status after this run: **PARTIAL / source OPEN under bounded current-literature checking**.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, source gate, ownership, and exclusions

I continued from the newest complete R08 report

`runs/R08/20260919T0926Z_e0011_co_poison_width8_7b4e21.md`

rather than restarting from the stale scheduler title.

The controlling later claim is `operations/claims/E0011.md`: Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), the original no-stirring catalyst/ZGB coexistence problem, with R08 as exclusive owner. The predecessor Hasebe--Ueda Problem 3.11 / I0082 remains **RETIRED/FROZEN at 2/3 after six unchanged runs**. I did not reopen it, did not reprove its finite-variance exclusion, and did not reopen the old R08 FPP strict-convexity route.

At run start I refreshed the campaign INDEX/RANKING, root POSTED/RESULTS, QUEUE, `operations/NEW_METHODS_2026-09-16.md`, the I0082/E0011 claims, the newest R08 report, and neighboring R07/R09 state. The root RESULTS view is intentionally stale for R-series mathematics and itself says to recover the newest complete per-track report before replacing a value; the immutable R08 reports therefore control this track's metric.

### Current-literature check

I reran bounded searches on 2026-09-19 for the exact Durrett source and later catalyst/ZGB work. Durrett's arXiv source `0906.2293` still describes the paper as containing nine challenging open problems. Durrett's publication record still distinguishes the 1994 mobile-reactant / stirring catalyst result from the no-stirring source target. The 2025 ZGB paper by Fernandes--da Silva, arXiv:2501.07066, studies a modified model with CO desorption. I did not find a later primary theorem settling the exact original no-stirring source problem. This is bounded negative evidence only, not a worldwide novelty certificate.

I also refreshed Hasebe--Ueda's ALEA source: its Problem 3.11 is indeed the non-delta freely strongly unimodal existence question, but the later E0011 handoff remains the controlling ownership instruction for this slot.

## 2. Frozen metric before the run

The frozen metric is

\[
B_{\rm cat}=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite protected two-child Harris-block certificates at `p=1/2`, with a 1-dependent translated block field, and `b(C)` is a rigorously certified lower bound on the block-good probability.

The last sound value is

\[
B_{\rm cat}\ge b_{17,\mathrm{rob}},
\qquad
\log_{10} b_{17,\mathrm{rob}}\approx -50.09882171767006.
\]

The preceding run proved that the current width-three seed has a positive-probability all-CO poisoning route and therefore cannot be made threshold-scale merely by waiting indefinitely. It also found that the same specific poisoning mechanism first falls below the whole `1/64` failure budget for a `2 x 8` vacancy rectangle. That suggested a wholesale seed-width redesign.

This run found a cheaper structural gain first: **the exceptional one-column bootstrap stage is still throwing away already-paid-for clock identities.**

## 3. B5 — add the right parameter: halo-dependent accepted-mark budget

The first bootstrap stage begins with only the local column

\[
(-1,0),(-1,1)
\]

known vacant. The existing exact enumeration has

\[
215383\text{ stable full entrance states}
\longrightarrow
48027\text{ projected core descriptors}.
\]

The old bootstrap accepts ten support-closed local adsorption labels. In the sound adversarial-boundary terminal calculation, exposing four halo cells

\[
H=\{(0,-2),(0,3),(1,2),(2,1)\}
\]

made seven more adsorption labels locally evaluable:

\[
\begin{aligned}
&CO(0,-1),\quad CO(0,2),\quad CO(1,1),\\
&O_2[(0,-1),(0,0)],\quad O_2[(0,1),(0,2)],\\
&O_2[(0,1),(1,1)],\quad O_2[(1,0),(1,1)].
\end{aligned}
\]

The new parameter is the number `k` of halo-dependent accepted labels allowed along one successful local history. The previous bootstrap is `k=0`. This run proves a strict gain already at **`k=1`**. I deliberately stopped there because it is enough to move the frozen metric and gives a much smaller exact game than the full unlimited-halo Bellman recursion.

## 4. B15 — break the stage symmetry on purpose

The expensive first stage is not in the same state class as later horizontal stages. Only it starts from one guaranteed vacant column; after one success the dynamics itself produces the old generated shield. Treating every stage with the same accepted alphabet therefore wastes probability exactly where the certificate is weakest.

I changed **only the bootstrap stage**. Every later corridor stage, guard, planter, terminal robust event, two-child deterministic implication, and dependency geometry remains the sound `b17_rob` construction.

More importantly, the seven newly accepted bootstrap identities cost no new hazard. The independent geometry checker reconstructs the first-stage owned Harris family and verifies

\[
D_{\rm raw}=157,\qquad D_{\rm blocked}=17,
\qquad \boxed{D_{\rm boot}=140}.
\]

All ten old labels and all seven halo-dependent labels are already identities in that same owned family. Hence accepting the extra seven labels changes neither the total owned rate nor the block's sigma-field/dependency footprint.

This is the main structural reason the gain is legitimate rather than a denominator trick.

## 5. Universal exterior: the one-new-label adversarial Bellman recursion

The four halo values are **not frozen**. As in the sound `b17_rob` correction, before each accepted arrival I allow the exterior to reset them adversarially to any assignment stable with the protected core. This is stronger than the real exterior dynamics and therefore preserves the universal boundary quantifier.

Let `A` be the six-vacancy bootstrap target. Let `O_n(s)` denote the exact integer reaction-weight mass of successful `n`-arrival histories using only the old ten labels. Let `F_n(s)` denote the corresponding mass when histories may use at most one of the seven halo-dependent labels. Then

\[
O_0(s)=F_0(s)={\bf 1}_A(s),
\]

and, writing `L_0` for the ten old labels, `L_1` for the seven new labels, and `\mathcal H(s)` for stable halo assignments,

\[
O_n(s)=\sum_{\ell\in L_0}T_\ell O_{n-1}(s),
\]

\[
\boxed{
F_n(s)=
\sum_{\ell\in L_0}T_\ell F_{n-1}(s)
+
\min_{h\in\mathcal H(s)}
\sum_{\ell\in L_1}T_{\ell,h}O_{n-1}(s).
}
\]

The first term keeps the one-new-label budget available for later. In the second term the budget has been spent, so every later accepted arrival uses only the halo-independent old alphabet. The same adversarial halo `h` is used across all seven possible new clock identities at that arrival, i.e. the adversary chooses a boundary state before the random accepted clock is revealed. This is the correct strong quantifier order for a lower certificate.

All transition weights are the exact reaction-race weights already used by the prior local automata: total weight `72` for a CO label and `36` for an O2 label. Since every new contribution is nonnegative,

\[
\boxed{F_n(s)\ge O_n(s)\quad\text{for every }n,s.}
\]

That pointwise monotonicity makes the exhaustive minimization inexpensive enough to certify sharply.

## 6. B16 — exact exhaustive ranking plus branch-and-bound

Use the same eight-arrival truncation, bootstrap hazard `D=140`, and `\lambda=4` window as the original one-column exact certificate. Put `H=36D=5040`. Up to the common positive exponential/rational prefactor, the old statewise polynomial is

\[
P_O(s)=\sum_{n=0}^8
4^n\frac{8!}{n!}H^{8-n}O_n(s),
\]

and replace `O_n` by `F_n` for `P_F`.

The checker enumerates all **215,383** stable full entrances and all **48,027** projected descriptors and obtains

\[
\min_s P_O(s)
=
4642311559640512826443825152
\]

at core code

\[
\boxed{s_*=4782752}.
\]

At that same state,

\[
P_F(s_*)
=
\boxed{7492177630527378997219688448}.
\]

Now use the monotonicity `P_F(s)>=P_O(s)`. Any state whose old polynomial is already at least this cutoff cannot possibly beat the candidate robust value. **Exactly 16** of the 48,027 descriptors have old polynomial below the cutoff. The checker evaluates `P_F` only on those 16 and finds the same global minimizer `s_*` and the same value above. The next old polynomial is

\[
8458449879232610418655494144,
\]

which is already strictly larger than the robust minimum. This is an exact branch-and-bound proof of the global minimum over the complete entrance class, not a sample or heuristic search.

The executed C++ output ends in `PASS`.

## 7. Exact probability gain and metric movement

The exact checker first reproduces the archived old `lambda=4` bootstrap factor

\[
p_{\rm old}
=
\frac{449855540637605888}
{88875222725965541291015625}.
\]

The one-new-label adversarial event gives

\[
\boxed{
p_{\rm boot}^{(1)}
=
\frac{80668567688839168}
{9875024747329504587890625}
}
\]

and therefore

\[
\frac{p_{\rm boot}^{(1)}}{p_{\rm old}}
=
\frac{88625135400336}{54914006425489}
\approx1.6138894458663933.
\]

The sound current `b17_rob` construction does not use `p_old`; it inherited the later `lambda=87/20` bootstrap optimization from `b13`. The exact archived gain of that bootstrap over `p_old` is

\[
\frac{34717319668318843590202198742697856944700233990464479}
{34245904058199771001461521651828906250000000000000000}.
\]

Cross multiplication in the checker and a separate rational-arithmetic checker give

\[
\boxed{
G_{18}:=
\frac{p_{\rm boot}^{(1)}}{p_{\rm boot,current}}
=
\frac{3035047884064870809017076077339859545315170762500000000000000000000}
{1906467115341816615178741523321245913280178771097328202961614705231}
>1.
}
\]

Numerically,

\[
G_{18}\approx1.591974946560097,
\qquad
\log_{10}G_{18}\approx0.20193622881853607.
\]

Every other factor in `b17_rob` is unchanged. Hence define

\[
\boxed{b_{18,\rm boot}:=b_{17,\rm rob}G_{18}}.
\]

Then

\[
\boxed{B_{\rm cat}\ge b_{18,\rm boot}>b_{17,\rm rob}},
\]

with diagnostic scale

\[
\boxed{\log_{10}b_{18,\rm boot}\approx-49.89688548885152}.
\]

This resets the unchanged count from `2` to `0`; the Section-I stuck protocol is **not** triggered.

## 8. What this does and does not prove

This run proves a real strict improvement of the frozen block-certificate metric with the universal exterior handled adversarially and with **no added hazard or dependency family**. It also identifies a reusable mechanism: an owned clock need not be killed merely because its full local effect is not determined by the core state; it can be admitted through an adversarial boundary game.

It does **not** prove coexistence. The new block lower bound is still only on the scale

\[
b_{18,\rm boot}\approx1.27\times10^{-50},
\]

far below the sufficient `63/64` block threshold. The architecture-cap result from the preceding work also remains important: local constant-factor improvements to the present rare-stage product cannot by themselves close the source problem.

Status remains

\[
\boxed{\text{PARTIAL / source OPEN under bounded current-literature checking}.}
\]

No paper folder is created and no closure/audit credit is claimed.

## 9. Artifacts and validation status

Idea note fixed before the final certificate implementation:

`artifacts/R08/20260919T1045Z_e0011_robust_bootstrap_idea.md`.

Executed exact Bellman / branch-and-bound checker and output:

- `artifacts/R08/20260919T1045Z_e0011_robust_bootstrap_check.cpp`
- `artifacts/R08/20260919T1045Z_e0011_robust_bootstrap_check.out`

Independent geometry and exact-rational reconciliation checker/output:

- `artifacts/R08/20260919T1045Z_e0011_robust_bootstrap_geometry_check.py`
- `artifacts/R08/20260919T1045Z_e0011_robust_bootstrap_geometry_check.out`

Both are **self-checks**, not independent OTHER-track audits.

## 10. What the three methods did

**B5 ADD A PARAMETER.** Introduced the halo-dependent accepted-label budget `k`; `k=0` is the old bootstrap and the rigorously solved `k=1` case already increases the complete block metric by about 59.2% over the current sound bootstrap.

**B15 BREAK THE SYMMETRY.** Applied the adversarial-halo enlargement only to the exceptional one-column bootstrap instead of forcing the same event definition on every stage. This preserves all later certified factors and attacks the stage where the state class is genuinely different.

**B16 COMPUTE EVERY SMALL CASE.** Exhausted all 48,027 entrance descriptors, ranked the exact old polynomial, and used `F>=O` to reduce the expensive robust verification to exactly 16 candidates. This turns what looked like a much larger Bellman calculation into a 4.87-second exact certificate in the archived run environment.

## 11. Next distinct methods

Do not repeat B5/B15/B16 next run. The next triple is:

- **B3 PROVE SOMETHING STRONGER.** Replace the `k=1` subevent by the full adversarial bootstrap value permitting arbitrarily many of the seven halo-dependent accepted labels within the eight-arrival window. The `k=1` certificate gives a rigorous lower baseline and a minimizer/cutoff to exploit.
- **B14 FIND THE GROUP ACTING.** Quotient the bootstrap core descriptors and halo actions by the exact reflections/label symmetries that preserve the entrance/target geometry; use canonical orbit representatives before attempting `k=2,3,...` or the full Bellman recursion.
- **B19 MAKE IT AN ALGORITHM.** Implement the hierarchy `F_k` with exact branch-and-bound: evaluate the old value on all states, derive a current robust cutoff, and recurse only on states that can still beat it. Stop when the metric gain saturates or the unrestricted robust value is reached.

The point is not another decimal tweak. The research question is whether adversarial admission of already-paid-for clocks can convert the bootstrap from a rare synchronized event into a qualitatively larger hitting event **without increasing the Harris dependency footprint**.

## 12. Model / scheduler escalation status

The model-control limitation is still real. The exposed scheduler/update schema provides title/prompt, schedule or start offset, enabled state and timing mode. It exposes **no binding model-family field, no reasoning-effort field, and no authenticated completed-run model telemetry**. Therefore `GPT-6 / maximum` remains prompt text only in this scheduler. This run actually reports GPT-5.6 Sol; reasoning level is UNVERIFIED.

A real fix requires platform/backend support that persists model family and reasoning effort in the scheduled-job definition, routes each invocation accordingly, and exposes authenticated run metadata. I cannot manufacture that through repository text.

The historical P26 `You cannot modify this task` denial was context-specific: the current root RESULTS record says a later full P26 update succeeded in an authorized P/C context, while other contexts still rejected edits. For any task that still rejects modification, the legitimate workaround is the authorized owning context, supported ownership/admin transfer, or platform support. No permission bypass and no scheduler modification was attempted here.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R08
  predecessor: I0082
  predecessor_state: RETIRED_FROZEN
  predecessor_metric: 2/3
  predecessor_retirement_count: 6
  target: E0011
  source: Durrett_2009_no_stirring_catalyst_ZGB_problem
  allocation: CLOSABLE_OUTSIDE
  owner: R08
  metric: B_cat
  before: ">= b17_rob; log10 ~= -50.09882171767006"
  after: ">= b18_boot = b17_rob * G18; log10 ~= -49.89688548885152"
  exact_gain: "3035047884064870809017076077339859545315170762500000000000000000000 / 1906467115341816615178741523321245913280178771097328202961614705231"
  gain_decimal: 1.591974946560097
  movement: positive
  unchanged_count_before: 2
  unchanged_count_after: 0
  source_status: OPEN_CURRENT_BOUNDED
  track_status: PARTIAL
  methods: [5, 15, 16]
  new_bootstrap_event: "at most one of seven adversarial-halo labels; all seventeen labels already owned; D=140 unchanged"
  entrance_full_states: 215383
  entrance_descriptors: 48027
  exact_candidates_after_branch_bound: 16
  new_bootstrap_probability: "80668567688839168 / 9875024747329504587890625"
  audit_status: self_checks_only
  next_methods: [3, 14, 19]
```
