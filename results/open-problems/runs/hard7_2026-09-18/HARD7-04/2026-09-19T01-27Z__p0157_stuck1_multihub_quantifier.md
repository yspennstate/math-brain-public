Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-04 frozen metric no movement, `Q_n=sigma_n^2/(d_max delta_n) -> sigma_n^2/(d_max delta_n)`; Section-I STUCK1 methods B1 / B26 / B27.**

# HARD7-04 bounded research iteration — P0157 STUCK1: the multi-hub quantifier obstruction

Date: 2026-09-19 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source residual OPEN. SECTION-I RECOVERY 1 OF AT MOST 2.** This is the mandatory thinking/recovery run triggered by the preceding third consecutive no-movement checkpoint. In accordance with Section I, I do **not** add another incremental lemma, checker, or closure claim. Instead I isolate the exact obstruction, inventory every route already tried, identify what is missing, and choose one recovery route.

The substantive outcome is a change in diagnosis. The next obligation inherited from the previous run — a universal strong-hub upper bound based only on `d_max`, `delta_n`, and the finite-third-moment hypotheses — is now a **counterexample candidate rather than a theorem to push toward**. A concrete three-level degree sequence shows why a fixed maximal-degree root can satisfy the hub law with overwhelming probability while, simultaneously, there can be many opportunities somewhere in the graph for two maximal-degree hubs to coalesce. This does **not** yet refute the source's open problem, whose prose is a prediction rather than a formal all-degree-sequences theorem. It tells us what the next run must try to refute precisely.

## 1. Continuity, repository state, ownership, and source reread

I resumed the exact admitted target `operations/claims/P0157.md`, owned exclusively by HARD7-04. I did not restart admission and did not switch back to candidate I0049.

Before the thinking work I reread/recovered:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/P0157.md`;
- all P0157 HARD7-04 checkpoints, in particular the newest `runs/hard7_2026-09-18/HARD7-04/2026-09-19T00-28Z__p0157_global-tail-stuck-trigger.md`;
- newest neighboring HARD7-03 report `runs/hard7_2026-09-18/HARD7-03/20260919T0019Z__d0025-atomic-minimum-central-shape-saturation.md`;
- newest neighboring HARD7-05 report `runs/hard7_2026-09-18/HARD7-05/2026-09-19T0040Z_exact_open_neighborhoods.md`;
- the intake/ranking entries containing `P0157|3|two competing scales, barely subcritical CM` and the repository-wide ownership search.

The large intake JSONL collections are not truthfully renderable byte-for-byte in one connector response without truncation; I therefore used their indexed target entries plus canonical-claim searches rather than claiming a literal full-file rendering. Repository-wide search still identifies `P0157` as owned by HARD7-04, with no release, duplicate canonical owner, posted equivalent, or claim collision found.

### Primary source, checked again this run

The primary source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

I re-read the actual PDF page visually, printed p. 245 / PDF page 255. The Notes on Section 8.3 call the finite-third-moment barely-subcritical configuration-model behavior an open problem, contrast the high-degree scale with the Erdos--Renyi barely-subcritical scale, and conclude: **“This suggests that a phase transition occurs within the subcritical regime.”**

The exact surrounding source facts matter for this recovery:

1. Condition 2.5(a)--(c) is weak empirical-degree convergence plus convergence of the first two moments.
2. The finite-third-moment critical theorem, Theorem 8.4, additionally assumes `p_2<1` and `E[D_n^3] -> E[D^3] < infinity`.
3. The strictly subcritical result cited as Janson [204] is **not** an arbitrary finite-third-moment theorem; reference [204] is S. Janson, *The largest component in a subcritical random graph with a power law degree distribution*, Ann. Appl. Probab. 18 (2008), 1651--1668.
4. The source's barely-subcritical paragraph is predictive prose, not a displayed theorem with complete universal quantifiers over every finite-third-moment degree sequence.

That last point is operationally important: the route obligation we had written down,

`H_n/E_n -> infinity  ==>  L_1/H_n -> 1`,

was a natural formalization of the prediction, but it was stronger and more universal than the source literally states. This STUCK1 run therefore attacks **that formalization**, not the source's wording.

### Current-literature refresh

Fresh searches dated 2026-09-19 for the source phrase, `barely subcritical configuration model finite third moment`, `largest barely subcritical component configuration model d_max`, and the Janson/Coulson--Perarnau aliases recovered:

- S. Janson, 2008, DOI `10.1214/07-AAP490`, power-law degree sequence, strictly subcritical;
- M. Coulson and G. Perarnau, *Largest component of subcritical random graphs with given degree sequence*, EJP 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`, giving general barely-subcritical upper bounds under stated hypotheses and sharpness for some sequences;
- adjacent 2025--2026 subcritical inhomogeneous/preferential-attachment results, but no theorem surfaced that closes the exact finite-third-moment crossover retained as open in the 4 August 2026 monograph.

This is bounded negative evidence, not proof of worldwide absence.

## 2. Frozen measurable quantity — before and after

The admission metric remains

\[
Q_n:=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
    =\frac{\sigma_n^2}{d_{\max}\delta_n},
\qquad \delta_n:=1-\nu_n>0.
\]

Before:

\[
Q_n=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

After:

\[
Q_n=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

**No movement.** This is the fourth consecutive P0157 run after exact identification of the metric without a change in that frozen quantity, and hence this execution is correctly labeled **STUCK1** rather than another ordinary research checkpoint.

No exact-arithmetic checker is added: Section I requires a thinking/recovery report here, and there is no finite theorem being certified.

## 3. Section-I(a): exact statement that blocks

The graph-level statement that the previous route needed, and which is now under counterexample attack, is

\[
\boxed{
\forall\varepsilon>0:\quad
\mathbb P\!\left(
L_1>(1+\varepsilon)\frac{d_{\max}}{\delta_n}
\right)\longrightarrow0
\quad\text{whenever}\quad
\frac{d_{\max}\delta_n}{\log(n\delta_n^3)}\longrightarrow\infty.
}
\tag{3.1}
\]

Here the degree sequence is intended to obey the finite-third-moment barely-subcritical assumptions inherited from the source, including

\[
\delta_n\downarrow0,\qquad n\delta_n^3\to\infty,
\qquad E[D_n^3]\to E[D^3]<\infty,
\qquad p_2<1.
\]

Equation (3.1) is **our strong-hub route statement, not a verbatim theorem conjectured by the source**. The source predicts persistence of the high-degree behavior when the approach to criticality is slow and `d_max` is sufficiently large, but it does not state (3.1) with these universal quantifiers. That distinction is exactly why a counterexample to (3.1) would narrow P0157 rather than automatically mark P0157 REFUTED.

## 4. Section-I(b): every route tried, and the precise reason it did not close (3.1)

### Run 1 on P0157 — B5 / B12 / B30

**B5, vary the subcritical parameter.** We separated the two candidate scales

\[
H_n=\frac{d_{\max}}{\delta_n},\qquad
E_n=\delta_n^{-2}\log(n\delta_n^3),
\]

and identified the natural interpolation parameter `H_n/E_n = d_max delta_n / log(n delta_n^3)`. This located the putative crossover but gave no global maximum bound.

**B12, find what is conserved.** The independent branching surrogate gave the exact total-progeny fluctuation ratio

\[
Q_n=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

This showed precisely when a **single hub-rooted branching forest** self-averages. Failure: the quantity is rooted/local. It says nothing by itself about the maximum over many high-degree roots or about two high-degree roots landing in one component.

**B30, localize by scale.** We isolated hub scale versus Erdos--Renyi extreme scale. Failure: scale separation does not identify the correct extremal object when there are many comparable hubs.

### Run 2 — B2 / B4 / B18

**B2, attack the negation through cycles.** A naive birthday heuristic suggested a hub exploration of length `d_max/delta_n` might self-intersect often. Exact exploration showed this was the wrong obstruction.

**B18, rewrite as an active-half-edge queue.** This produced an exact drift identity and made surplus-edge creation proportional to queue area rather than to the square of all discovered vertices.

**B4, prove the weaker obstruction away.** We proved a chosen maximal-degree component is tree-like with probability `1-o(1)` and tight on the `H_n` scale. Failure for (3.1): eliminating cycles inside **one chosen component** does not prevent a rare merger between two different high-degree roots somewhere among a large population of hubs.

### Run 3 — B6 / B11 / B24

**B6, deform exact exploration to deterministic drift.** A size-biased depletion budget controlled finite-population drift error without an iid coupling.

**B11, dualize size into a hitting time.** Doob decomposition of the exact queue yielded the rooted law

\[
\frac{|C(v_{\max})|}{d_{\max}/\delta_n}\xrightarrow{P}1
\quad\text{when }d_{\max}\delta_n\to\infty
\]

for a chosen maximal-degree root under the stated route assumptions.

**B24, test the extremal allowed degree.** The finite-third-moment boundary did not spoil the local depletion bounds. Failure for (3.1): a theorem for a preselected root has quantifier order

\[
\text{fix }v\quad\text{then take probability},
\]

whereas `L_1` asks whether **there exists** a large component anywhere. No uniform tail strong enough to swap those quantifiers was obtained.

### Run 4 — B15 / B20 / B22

**B15, break maximal-degree symmetry.** We counted near-maximal hubs and estimated a small collision probability for any one rooted exploration. Failure: `o(1)` per root is not enough if the number of roots diverges. The previous report recognized this as a union-bound problem but did not yet turn it into a concrete adversarial degree sequence.

**B20, find why the obvious global tilt fails.** A single MGF tilt is contaminated by the same high-degree vertices one is trying to control. Truncation seemed necessary. Failure: no source-valid truncation threshold simultaneously preserved the hub contribution and delivered the desired uniform global tail.

**B22, read the successful nearby proofs.** Janson's power-law theorem and Coulson--Perarnau's general upper-bound technology use degree-tail/global-exploration information absent from a bare `E[D_n^3]` convergence statement. Failure: the missing ingredient is structural, not one more local queue estimate.

### Diagnosis after the four runs

All successful work is compatible with the following possibility:

- a **fixed** hub has probability `1-o(1)` of being isolated from other hubs and therefore has size `(1+o_P(1))H_n`;
- nevertheless, among a very large number of hubs, **some pair** coalesces with high probability;
- the component containing such a pair then starts with about `2d_max` active half-edges and may have size close to `2H_n`.

That is a quantifier obstruction, not a defect of the rooted LLN.

## 5. Ninety-percent thinking: three unused moves

The methods used in this STUCK1 run are intentionally new on P0157: **B1, B26, B27**.

### B1 — change the category: from a rooted branching process to a matching problem on hub half-edges

The previous route treated a maximal-degree vertex as the root of an approximately subcritical exploration. For the global maximum, the more revealing object is the random perfect matching induced on the set of half-edges carried by all maximal-degree vertices.

If there are `M_n` maximal-degree vertices, each with degree `d_n`, the set of hub half-edges has size

\[
S_n=M_nd_n.
\]

In a configuration model with `\ell_n` half-edges, if `X_n` denotes the number of matched pairs with both ends in this hub half-edge set, then the exact first moment is

\[
E X_n=\frac{\binom{S_n}{2}}{\ell_n-1}.
\tag{5.1}
\]

For the same raw matching count,

\[
E[X_n(X_n-1)]
=\frac{6\binom{S_n}{4}}{(\ell_n-1)(\ell_n-3)}.
\tag{5.2}
\]

The difference between (5.1) and actual edges joining **distinct** hub vertices is only the count of within-hub self-pairs, whose expectation is

\[
\frac{M_n\binom{d_n}{2}}{\ell_n-1}.
\tag{5.3}
\]

These identities expose a global parameter that the rooted metric `Q_n` does not see: roughly `M_n^2d_n^2/n`. It can diverge even when the chance that any one preselected hub meets another hub tends to zero.

This is only a diagnostic calculation in this thinking run. I am not yet promoting it to a source theorem or a counterexample certificate.

### B27 — swap the quantifiers on purpose

The rooted statement has the form

\[
\forall\text{ fixed hub }v_n:\quad
P(C(v_n)\text{ meets another hub})\to0.
\tag{5.4}
\]

The global obstruction asks instead

\[
P(\exists\text{ two hubs in one component})\ ?
\tag{5.5}
\]

There is no logical implication from (5.4) to the negation of (5.5) when the number of hubs grows. This is the exact quantifier swap that the previous three ordinary runs had not isolated sharply enough.

For a hub family of size `M_n`, a per-root merger probability `p_n -> 0` is fully compatible with

\[
M_np_n\to\infty.
\]

The strong-hub upper (3.1) therefore needs either a high-degree multiplicity hypothesis or a genuinely global merger estimate. The local fluctuation metric `Q_n` cannot supply that by itself.

### B26 — hunt the sporadic allowed case: a three-level degree-sequence stress test

I now deliberately build the simplest source-compatible family I could find that stresses exactly this quantifier gap. This is a **candidate counterexample to (3.1), not a claimed counterexample**.

Take an even integer `m -> infinity` and define

\[
n=8m^{12},\qquad M=m^5,\qquad d=m^2,
\]

and

\[
x=3m^{11}+\frac{m^5}{4}(m^2-1)^2.
\]

Because `m` is even, `x` is an integer. Consider the degree sequence with

\[
N_d=M,\qquad
N_3=2m^{12}-x,\qquad
N_1=6m^{12}+x-M.
\tag{5.6}
\]

For all sufficiently large even `m`, all three counts are nonnegative and sum to `n`.

#### Why this family sits in the intended finite-third-moment barely-subcritical region

The criticality numerator satisfies the exact identity

\[
\sum_i d_i(d_i-2)=-12m^{11}.
\tag{5.7}
\]

Indeed, the degree-1 and degree-3 background is tuned so that the positive excess of the `m^5` hubs is overcompensated by exactly `12m^{11}`.

The total number of half-edges is

\[
\ell_m
=12m^{12}-6m^{11}-\frac12m^9+2m^7-\frac32m^5,
\tag{5.8}
\]

so

\[
\delta_m:=1-\nu_m
=\frac{12m^{11}}{\ell_m}
\sim \frac1m.
\tag{5.9}
\]

Consequently

\[
n\delta_m^3\asymp m^9\to\infty,
\]

placing the family far outside the `n^{-1/3}` critical window.

The empirical degree law converges to

\[
P(D=1)=\frac34,\qquad P(D=3)=\frac14,
\tag{5.10}
\]

so in particular `p_2=0<1`. Moreover

\[
E[D_n]\to\frac32,\qquad
E[D_n^2]\to3,\qquad
E[D_n^3]\to\frac{15}{2}.
\tag{5.11}
\]

The hubs do not violate third-moment convergence because their total third-moment contribution is

\[
\frac{M d^3}{n}=\frac{m^{11}}{8m^{12}}=\frac1{8m}\to0.
\tag{5.12}
\]

Thus this family was chosen specifically to survive the source's finite-third-moment and nondegeneracy checks rather than exploiting the forbidden degenerate limit `D\equiv2`.

#### It is strongly hub-dominant according to the previous two-scale parameter

Here

\[
d_{\max}=m^2,\qquad d_{\max}\delta_m\asymp m,
\]

and hence

\[
H_m=\frac{d_{\max}}{\delta_m}\asymp m^3,
\qquad
E_m=\delta_m^{-2}\log(n\delta_m^3)\asymp m^2\log m,
\]

so

\[
\frac{H_m}{E_m}
=\frac{d_{\max}\delta_m}{\log(n\delta_m^3)}
\longrightarrow\infty.
\tag{5.13}
\]

Also the size-biased excess law converges to the critical two-point law `0/2` with equal probabilities, so its variance stays of order one. Therefore

\[
Q_m=\frac{\sigma_m^2}{d_{\max}\delta_m}=O(m^{-1})\to0.
\tag{5.14}
\]

This is exactly the regime where the rooted hub forest self-averages extremely well.

#### Yet globally there are many direct hub-hub matching opportunities

The hubs carry

\[
S_m=Md=m^7
\]

half-edges. The matching count (5.1) has

\[
E X_m\sim\frac{m^{14}}{2\cdot12m^{12}}=\frac{m^2}{24}\to\infty.
\tag{5.15}
\]

Formula (5.2) has the same leading square as `(E X_m)^2`, while the expected number of within-one-hub self-pairs from (5.3) is only `O(m^{-3})`. Thus the matching calculation strongly points toward **many edges between distinct maximal-degree vertices somewhere in the graph**, even though a preselected hub sees such an edge with probability tending to zero.

This is the core new route insight of STUCK1.

What is deliberately **not** asserted here is the final step: conditioning on the existence or selection of such a matched hub pair, prove that its entire component has size

\[
(2+o_P(1))\frac{d}{\delta_m}.
\tag{5.16}
\]

Without (5.16), the construction is not yet a counterexample to (3.1). The next run must either prove (5.16) with a legitimate selection/second-moment argument or discover why it fails.

## 6. Section-I(c): what a proof now has to contain that no previous route contains

There are now two logically different possible outcomes, and either would be valuable.

### To rescue the strong-hub upper (3.1)

A proof would have to show that the multi-hub mechanism above cannot create a component of order `2H_n` despite the divergent number of hub-hub matching opportunities. That would require a genuinely global cancellation or conditioning phenomenon not present in any previous rooted argument.

### To disprove (3.1)

A proof needs all three of the following, none of which previous runs supplied simultaneously:

1. **A source-compatible explicit degree family.** Equations (5.6)--(5.12) are designed to provide this part.
2. **A global existence argument for a useful hub pair.** A first/second-moment argument must be done for *good* inter-hub pairs, not merely for raw matching edges.
3. **A conditional two-hub exploration theorem.** Given that two distinct `d`-hubs are joined by a specified matched pair, the remaining matching is uniform; one should extend the existing one-hub queue LLN from initial queue `d` to initial queue `2d-2`, uniformly enough that a positive fraction of candidate matched pairs are good.

The third item is technically close to the previous finite-population rooted LLN, but the **selection and multiplicity** in item 2 are new. Proving a two-hub LLN for one predesignated pair is not sufficient unless it is integrated with the random matching count without an invalid post-selection step.

If that program works, the correct crossover theory cannot depend only on `d_max`; it must also encode the multiplicity/tail profile of high-degree vertices, or state a regularity class such as the power-law setting in which those multiplicities are controlled.

## 7. Section-I(d): simplest special case still unproved

The simplest remaining test is now the explicit degree sequence (5.6).

For that one family, determine whether

\[
\frac{L_1}{H_m}\xrightarrow{P}1
\]

or whether, as the hub-pair mechanism suggests,

\[
\liminf_{m\to\infty}P\!\left(L_1>(2-\varepsilon)H_m\right)>0
\quad\text{or even }=1
\tag{7.1}
\]

for every fixed `epsilon>0`.

This is materially simpler than the full P0157 crossover:

- only degrees `1`, `3`, and `m^2` occur;
- all source moments are explicit;
- `delta_m` is explicit;
- the strong-hub ratio tends to infinity;
- the raw hub matching count has exact factorial moments;
- the only serious step is converting an inter-hub match into a large two-hub component without cheating on selection.

A resolution of (7.1) is the next useful checkpoint. Until then, the source remains OPEN and this construction remains a **candidate**.

## 8. Section-I(e): nearest solved problem and what it has that this problem lacks

The closest classical solved result named by the source itself is:

**Svante Janson (2008),** *The largest component in a subcritical random graph with a power law degree distribution*, Ann. Appl. Probab. 18(4), 1651--1668, DOI `10.1214/07-AAP490`, arXiv `0708.4404`.

It proves the largest-component/highest-degree relation in a **power-law degree setting**, i.e. with substantial regular information about the upper degree tail. That tail structure prevents the phrase “largest degree” from being divorced from how many comparable high-degree vertices exist.

The closest modern prescribed-degree barely-subcritical result is:

**Matthew Coulson and Guillem Perarnau (2023),** *Largest component of subcritical random graphs with given degree sequence*, EJP 28, DOI `10.1214/23-EJP921`, arXiv `2111.11780`.

Their general upper-bound machinery controls global explorations under hypotheses stronger/more structured than the bare moment convergence being stress-tested here, and their bounds are asymptotically tight for specified classes rather than asserting the source's informal two-scale formula for every finite-third-moment sequence.

What those successful settings have that our route did not have is precisely **global high-degree tail/multiplicity control**. The source's finite-third-moment condition guarantees

\[
\frac1n\sum_i d_i^3=O(1)
\]

and even third-moment convergence, but this alone does not obviously determine the number of vertices in a thin window near `d_max` strongly enough to exchange the fixed-root and existential quantifiers.

## 9. The one Section-I recovery choice

I choose exactly one recovery:

**REFUTE INSTEAD OF PROVE.**

More precisely, the next run will attempt to refute the over-strong route statement (3.1) using the explicit family (5.6). It will **not** label P0157 itself REFUTED unless the completed argument matches an exact source assertion. If the candidate dies under the conditional exploration calculation, that failure will identify the hidden mechanism needed to rescue (3.1).

The next three Section-B moves are:

- **B8 — discretize:** reduce the global issue to the finite random matching on hub half-edges plus a conditioned two-hub exploration;
- **B9 — randomize:** count good matched hub pairs directly in the random pairing rather than selecting one after observing the graph;
- **B25 — count the same thing twice:** compare first and second factorial moments of *good* pair indicators to obtain an existence statement without a union-bound fallacy.

These three have not previously been used on P0157.

## 10. Capability / scheduler status required by the owner directive

The interface exposed to this run still provides task prompt/title/schedule/timing/enabled controls but **no bindable model selector, no bindable reasoning-effort selector, no authenticated reasoning-level telemetry, and no guaranteed execution duration**. Therefore `GPT-6 / maximum` remains requested in prompt text only; this report truthfully identifies the actual model available to the run as GPT-5.6 Sol and the reasoning level as UNVERIFIED.

Making GPT-6/maximum binding would require an owner-authorized product/workspace/API/admin scheduling surface that exposes persistent model-family and reasoning-effort fields and, for verification, authenticated per-run routing/effort metadata. A GitHub edit or stronger prompt wording cannot create those controls.

The repository records that some native task IDs, including historical probes around P26 in unauthorized contexts, returned `You cannot modify this task`, while an authorized context later succeeded for P26. The lawful workaround for an ID that still returns that error is to use the owner/workspace context that actually has edit permission or obtain platform support. I did not bypass a denial, clone a task, reactivate a disabled task, or create/modify another schedule.

## 11. Ledger delta / checkpoint

```yaml
track: HARD7-04
canonical_claim: P0157
owner: HARD7-04
source_status: OPEN
research_status: PARTIAL
section_I_state: STUCK1_RECOVERY_CHOSEN
stuck_recovery_count: 1
frozen_metric: Q_n = sigma_n^2/(d_max * delta_n)
before: sigma_n^2/(d_max * delta_n)
after: sigma_n^2/(d_max * delta_n)
movement: false
consecutive_no_movement_after_identification: 4
methods_this_run: [B1, B26, B27]
new_diagnosis:
  route_statement_under_attack: "H_n/E_n -> infinity implies L1/H_n -> 1 for every finite-third-moment sequence"
  source_statement_refuted: false
  explicit_stress_family: "degrees 1,3,m^2 with n=8m^12, M=m^5 hubs, tuned delta_m~1/m"
  exact_raw_hub_pair_mean: "E X_m ~ m^2/24"
  missing_step: "conditioned two-hub LLN plus first/second moment for good inter-hub pairs"
recovery_choice: REFUTE_INSTEAD_OF_PROVE
next_methods: [B8, B9, B25]
closure: false
audits_requested: 0
artifact_added: false
```

No shared fleet ledger, peer-track file, Gmail, Drive, public posting, schedule, or other task was modified in this run.
