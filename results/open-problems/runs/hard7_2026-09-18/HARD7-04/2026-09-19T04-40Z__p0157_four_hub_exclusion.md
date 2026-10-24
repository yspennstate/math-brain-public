Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-04 frozen metric has no movement, `Q_m=m^{-1}+O(m^{-2})->0` before and after; methods B4 / B10 / B16.**

# HARD7-04 bounded research iteration — P0157 four-hub exclusion and exact three-hub witness

Date: 2026-09-19 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN.** This run resumes the exclusive P0157 claim and the latest absorbing-hub-kernel checkpoint. It does not reopen I0049 or restart admission. The main new theorem is an actual-configuration-model four-hub exclusion on the explicit multi-hub stress family; the complementary three-hub route is reduced from a surrogate heuristic to an exact source-model witness count with expectation asymptotic to a positive constant times `m`.

## 1. Continuity, ownership, and repository state

I resumed:

`operations/claims/P0157.md`

owned exclusively by HARD7-04.

Before new mathematics I re-read/recovered:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/P0157.md`;
- the HARD7-04 checkpoint chain through
  `runs/hard7_2026-09-18/HARD7-04/2026-09-19T03-44Z__p0157_absorbing_hub_kernel.md`;
- the substantive predecessor artifacts, in particular
  `p0157_multihub_route_refutation.md`,
  `p0157_finite_population_hub_lln.md`, and
  `p0157_hub_connection_kernel.md`;
- newest neighboring HARD7-03 checkpoint, commit
  `ba729cc0fd0153aba2071d1412e37044b654ed62`;
- newest neighboring HARD7-05 checkpoint, commit
  `c96cff22b0bb20895ac9d1d92e5cbf4b4ad318cd`;
- repository-wide P0157/source-phrase/owner searches.

The current intake/queue collections are too large to render byte-for-byte through the connector in one response. I used the indexed queue/intake material plus canonical claim and alias searches, as in the preceding run, rather than falsely claiming a literal full-file dump. No release, collision, posted equivalent, or competing P0157 owner surfaced. Shared root ledgers were not edited; this report carries a structured `ledger_delta` for the designated maintainer.

## 2. Primary source and current-literature refresh

The current primary source was re-opened directly on 2026-09-19:

Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF page 255:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`

The page explicitly calls the finite-third-moment barely-subcritical configuration-model question an interesting open problem. It recalls Janson's strictly subcritical `d_max/(1-nu)` law, predicts persistence sufficiently far below criticality for sufficiently large `d_max`, contrasts it with the Erdős--Rényi scale

\[
\delta_n^{-2}\log(n\delta_n^3),
\]

and says that this “suggests that a phase transition occurs within the subcritical regime.” The track continues to use the positive convention

\[
\delta_n=1-\nu_n>0
\]

rather than the source's negative `epsilon_n=nu_n-1`.

A fresh bounded literature search dated 2026-09-19 used the source phrase and combinations of:

- `barely subcritical configuration model largest component finite third moment`;
- `largest component subcritical given degree sequence`;
- `largest subcritical component 2026 inhomogeneous random graph`;
- `configuration model high degree barely subcritical`.

It recovered, among others:

1. Matthew Coulson and Guillem Perarnau, *Largest component of subcritical random graphs with given degree sequence*, EJP 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`. It gives CM upper bounds, tight for certain degree sequences, but does not state the full finite-third-moment crossover requested by the 2026 monograph.

2. Peter Mörters and Nick Schleicher, *The largest subcritical component in inhomogeneous random graphs of preferential attachment type*, CPC 35 (2026), DOI `10.1017/S096354832610039X`, arXiv `2503.05469`. This concerns a different preferential-attachment-type inhomogeneous model and explicitly contrasts its behavior with rank-one/configuration-model behavior.

No located 2024--2026 result in this bounded search closes P0157's exact configuration-model crossover. This is a dated bounded negative search, not a worldwide novelty certificate.

## 3. Frozen metric — no movement

The frozen admission quantity remains the normalized branching-surrogate hub fluctuation

\[
Q_n
=
\frac{\operatorname{Var}(T_n)}
     {(d_{\max}/\delta_n)^2}
=
\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

On the explicit stress family introduced in the preceding runs,

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,\qquad \delta_m\sim m^{-1},
\]

and

\[
Q_m=m^{-1}+O(m^{-2})\to0.
\]

This run does not change that scalar:

\[
\boxed{
Q_m:m^{-1}+O(m^{-2})\to0
\quad\longrightarrow\quad
m^{-1}+O(m^{-2})\to0.
}
\]

This is the second consecutive no-movement run since the stress-family metric was first evaluated, so the Section-I three-unchanged-run trigger has **not** fired yet. I did not relabel a new auxiliary quantity as frozen progress.

## 4. B4 — prove something weaker, completely: four-hub exclusion

The previous checkpoint's most concrete open obligation was:

> prove a three-hub lower bound and four-hub exclusion for the explicit multi-hub family in the actual CM.

This run completely proves the second half:

\[
\boxed{
\mathbb P\{\exists\text{ a CM component containing at least four hubs}\}
=O(m^{-1})\to0.
}
\tag{4.1}
\]

The proof is graph-level and does not invoke independent surrogate hub edges.

### Structure of the proof

Let

\[
R=\left\lfloor\ell\delta/64\right\rfloor.
\]

A direct active-half-edge supermartingale argument gives, uniformly for every hub `h`,

\[
\mathbb P(\tau_h>R)
\le
\frac{256d}{\ell\delta^2},
\]

where `tau_h` is its component-exploration pairing time. Therefore

\[
\mathbb P(\exists h:\tau_h>R)
\le
\frac{256Md}{\ell\delta^2}
=O(m^{-3}).
\tag{4.2}
\]

On the complementary event, if a component contains at least four hubs, take a spanning tree, retain its minimal all-hub subtree, and repeatedly delete one leaf hub followed by any newly created non-hub leaves until exactly four hubs remain. This gives a connecting tree with at most `R` edges and no uncounted hub in its interior. Suppress all non-hub tree-degree-two vertices. The core consists of exactly four hubs and `t` bulk degree-three branch vertices. Degree counting forces `t<=2`.

For the exact numbers `C_t` of labeled cores,

\[
C_0=16,\qquad C_1=12,\qquad C_2=6.
\tag{4.3}
\]

For `q=6N_3/ell`, the exact identity

\[
1-q=\delta+\frac{d(d-1)M}{\ell}
\]

gives `q<=1-delta`. Summing every possible length assignment on the `3+t` core edges yields

\[
\mathbb E N_t
\le
C_t\,
\frac{M^4d^{6-t}}{\{\ell(1-\delta/32)\}^3}
\left(\frac2\delta\right)^{3+t}.
\tag{4.4}
\]

For the stress family this is

\[
O(m^{-1-t}).
\]

Summing `t=0,1,2`, and then adding (4.2), proves (4.1).

The full theorem and proof are in

`artifacts/hard7_2026-09-18/HARD7-04/p0157_four_hub_exclusion_and_three_hub_witness.md`.

**B4 outcome: successful.** One side of the latest explicit `k=3/k=4` boundary target is now a complete actual-CM theorem, not a surrogate calculation.

## 5. B10 — derandomize the surrogate: an explicit actual-CM three-hub witness count

The preceding report had only the independent rank-one heuristic

\[
M^3p_m^2\asymp m
\]

for three-hub trees. This run removes the independent-edge surrogate.

For distinct ordered hubs `(a,b,c)` and path lengths

\[
m\le r,s\le2m,
\]

let a **V-witness** be two internally vertex-disjoint paths, `a--b` of length `r` and `a--c` of length `s`, with all internal vertices chosen among the degree-three bulk vertices.

If `Z_m` counts actual half-edge embeddings of these witnesses, then exactly

\[
\boxed{
\mathbb EZ_m
=(M)_3d^3(d-1)
\sum_{r=m}^{2m}\sum_{s=m}^{2m}
\frac{(N_3)_{r+s-2}6^{r+s-2}}
{(\ell-1)(\ell-3)\cdots(\ell-(2(r+s)-1))}.
}
\tag{5.1}
\]

Writing `q=6N_3/ell`, uniform falling-factorial estimates for `r+s<=4m` and `m(1-q)->1` give

\[
\boxed{
\mathbb EZ_m
\sim
\frac{(e^{-1}-e^{-2})^2}{144}\,m
=0.0003755332\ldots\,m
\to\infty.
}
\tag{5.2}
\]

This is a rigorous actual-CM first moment. It is not a simulation and not a proof that `Z_m>0` with high probability.

The exact remaining lower-bound obligation is now

\[
\boxed{\mathbb P(Z_m>0)\to1.}
\tag{5.3}
\]

That requires an overlap/factorial-moment or switching argument. I do **not** infer (5.3) from the diverging expectation.

**B10 outcome: partial but substantive.** The heuristic marked-kernel three-hub object has been converted to a deterministic, exactly countable witness family in the source model. The unresolved issue is now dependence between overlapping witnesses, not the one-edge marginal.

## 6. B16 — compute every small core case exactly

The four-hub theorem has a genuinely finite combinatorial core, so this is where an exact checker is useful.

A Prüfer-word enumeration over every labeled tree with four hub labels and `t` labeled bulk branch labels gives:

\[
\boxed{
t=0:16,\quad
t=1:12,\quad
t=2:6,\quad
t=3:0.
}
\tag{6.1}
\]

The same values also follow analytically because a branch label must occur exactly twice in the Prüfer word.

Executed exact checker:

`artifacts/hard7_2026-09-18/HARD7-04/p0157_core_topologies_exact.py`

Archived output:

`artifacts/hard7_2026-09-18/HARD7-04/p0157_core_topologies_exact.out`

ending

`ALL_EXACT_CHECKS_PASS = True`.

This is not a receipt-only checker: the finite topology counts enter the proof of (4.1), and `t=3 -> 0` independently certifies the degree-budget cutoff.

**B16 outcome: successful.** The small-core sequence exposes the exact finite topology behind the `k=4` decay and confirms that no omitted branch type can contribute at the same order.

## 7. Mathematical checkpoint

The actual-CM picture for the explicit family is now:

\[
\mathbb EZ_m^{(3)}
\sim
\frac{(e^{-1}-e^{-2})^2}{144}\,m\to\infty,
\]

while

\[
\mathbb P(\text{some component contains }4\text{ hubs})
=O(m^{-1})\to0.
\]

This rigorously confirms the **upper** side of the previously heuristic three-hub boundary and supplies an exact source-model lower witness count. It does not yet prove that the maximal hub multiplicity is exactly three whp.

The highest-value next attack is therefore **not** another marginal or concentration lemma. It is a complete overlap taxonomy for pairs of V-witnesses:

1. vertex-disjoint witnesses;
2. exactly one shared hub;
3. shared path prefix;
4. same three hubs with different interiors;
5. cyclic union.

The goal is either

\[
\mathbb E[Z_m(Z_m-1)]
=(1+o(1))(\mathbb EZ_m)^2,
\]

or a switching/Janson-style inequality strong enough to imply (5.3).

Because this run used B4/B10/B16, the next run must use a different triple.

## 8. Capability honesty

The scheduler capability situation remains unchanged in the exposed native interface: title, prompt, schedule/timing mode and enabled state are exposed; there is no model selector, no reasoning-effort selector and no guaranteed execution duration. GPT-6/maximum remains prompt-requested only.

This invocation is actually GPT-5.6 Sol. Authenticated reasoning telemetry is not exposed, so the reasoning level is **UNVERIFIED**.

Making GPT-6/maximum a genuine scheduler guarantee would require the platform to expose and honor model/reasoning fields for scheduled jobs, or an authorized platform-side configuration change. A repository edit cannot do that.

The historical `You cannot modify this task` result for a P26 scheduler ID is a permission/context issue, not something to bypass. Repository records say P26 was subsequently editable from another authorized context. For any task currently returning that denial, the valid routes are the authorized account/workspace/context or platform support; do not create a duplicate or reactivate anything behind the restriction. No schedule was created, modified, disabled, or reactivated in this run.

## 9. Checkpoint / ledger delta

```yaml
ledger_delta:
  track: HARD7-04
  target: P0157
  source_status: OPEN
  worker_status: PARTIAL
  frozen_quantity: Q_n = sigma_n^2/(d_max*delta_n)
  before_on_stress_family: Q_m = m^-1 + O(m^-2) -> 0
  after_on_stress_family: Q_m = m^-1 + O(m^-2) -> 0
  movement: none
  unchanged_streak_since_last_metric_evaluation: 2
  methods: [B4, B10, B16]
  theorem: "P(any component contains >=4 designated hubs) = O(m^-1) -> 0 in the explicit multi-hub CM family"
  three_hub_exact_first_moment: "E Z_m ~ ((e^-1-e^-2)^2/144) m -> infinity"
  finite_core_counts: [16, 12, 6, 0]
  artifact: artifacts/hard7_2026-09-18/HARD7-04/p0157_four_hub_exclusion_and_three_hub_witness.md
  checker: artifacts/hard7_2026-09-18/HARD7-04/p0157_core_topologies_exact.py
  checker_output: artifacts/hard7_2026-09-18/HARD7-04/p0157_core_topologies_exact.out
  next_obligation: "prove P(Z_m>0)->1 by overlap factorial moments or matching switchings"
  next_methods: [B13, B20, B27]
```

No shared root ledger was edited. No email or Drive action was taken.
