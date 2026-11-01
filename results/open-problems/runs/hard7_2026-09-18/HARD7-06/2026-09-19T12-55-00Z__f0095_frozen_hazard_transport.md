Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** **No movement:** `W_3: 0.656508 -> 0.656508`. Methods actually tried: **B18 / B13 / B21**.

# HARD7-06 run 17 — global frozen-pair hazard and exact safe-incidence transport

Status: **F0095 OPEN / HARD7-06 PARTIAL.** This run does not prove existence of the constant ordinary Erdős--Rényi 3-colourability threshold. It changes language from generic edge hazard to the global frozen-equivalence partition of all legal colourings, proves an exact transport identity showing what makes the hazard rise or fall from one layer to the next, and identifies the precise asymptotic statistic that would feed the exponential sprinkling condition isolated in the preceding run.

Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, exclusions, and source status

I resumed the canonical target `F0095`, owned by HARD7-06 in `operations/claims/F0095.md`. The claim is still `ASSIGNED / OPEN`; no competing F0095 owner, release, posted equivalent, or campaign closure appeared in the bounded repository-wide check. I did not restart the random-3-SAT/F0097 history. R03 already handed F0097 off after its allowed hard-task stuck cycles, and the latest neighboring R14 state has moved to P0157 rather than reopening the excluded negative-margin perceptron.

At run start I reread the controlling HARD7 policy, the latest new-methods policy and owner directive, root `POSTED.md`, root `RESULTS.md`, campaign `INDEX.md` and `RANKING.md`, `QUEUE.md`, the F0095 claim/intake material, the latest HARD7-06 report, the recent R14 handoff/reassignment state, and repository ownership search results. I preserved all prior checkpoints rather than restarting from the original candidate.

The primary source statement retained by the claim is Alan Frieze's ICM 2014 chromatic-number conjecture:

> **Conjecture.** There exists a sequence `d_k`, `k >= 2`, such that w.h.p. `chi(G_{n,d/n}) = k` for `d_{k-1} < d < d_k`.

HARD7-06 freezes the first small unresolved location case `k=3`: existence of a limiting constant average-degree threshold for ordinary sparse Erdős--Rényi 3-colourability, not merely a sharp `n`-dependent threshold sequence.

### Fresh bounded literature screen, 2026-09-19

The status search was rerun rather than inherited.

- Dimitris Achlioptas and Ehud Friedgut, *A Sharp Threshold for k-Colorability*, Random Structures & Algorithms 14 (1999), 63--70, DOI `10.1002/(SICI)1098-2418(1999010)14:1<63::AID-RSA3>3.0.CO;2-7`, still supplies the fixed-`k>=3` sharp `n`-dependent threshold theorem. Its abstract states existence of `d_k(n)`, not convergence to a constant.
- Joseph Culberson and Ian Gent, *Frozen development in graph coloring*, Theoretical Computer Science 265 (2001), 227--264, DOI `10.1016/S0304-3975(01)00164-5`, is directly relevant prior art for the language introduced below. They explicitly call two vertices frozen when they have the same colour in all legal colourings and study the collapsed graph empirically near the 3-colouring transition.
- Michael Molloy, *The freezing threshold for k-colourings of a random graph*, STOC 2012, pp. 921--930, DOI `10.1145/2213977.2214060`, rigorously determines a freezing threshold for a different, solution-cluster/local-reconfiguration notion: a colour is frozen if it cannot be changed through proper colourings obtained by `o(n)`-vertex alterations. That does not by itself give the global-all-colourings relation needed below.
- Clayton Mizgerd, Will Perkins and Yuzhou Wang, *On the Chromatic Number of Random Triangle-Free Graphs*, Random Structures & Algorithms 68 (2026), e70081, DOI `10.1002/rsa.70081`, published 6 June 2026, proves scaling-window results in the **triangle-free conditioned model** with a different density scale. It does not settle ordinary `G(n,d/n)` F0095.
- Bounded searches for 2025--2026 ordinary Erdős--Rényi `3-colorability threshold`, `3-colourability threshold`, and the fixed-`q=3` location problem recovered the conditioned triangle-free result and historical sharp-threshold/freezing work, but no source-matching ordinary-model resolution.

This is bounded negative evidence, not a worldwide openness or novelty certificate. The source remains **OPEN** in this run.

## 2. Frozen metric: second consecutive no-movement run

The fixed source-relevant metric remains

\[
W_3:=U_3-L_3,
\]

with the latest certified endpoints

\[
L_3=4.03,
\qquad
U_3=4.686508,
\qquad
W_3=0.656508.
\]

No endpoint is altered here:

\[
\boxed{W_3:0.656508\longrightarrow0.656508\quad\text{(no movement).}}
\]

This is the **second** consecutive unchanged run after the last moving checkpoint. Therefore Section I is not yet triggered. If the next invocation also leaves `W_3` unchanged, it must be a Section-I stuck/strategy run rather than another ordinary lemma run.

The reason to spend this run away from endpoint decimal optimization is source-level: the preceding run reduced threshold-location convergence to convergence of the normalized first-failure stopping-time mean and showed that even sharpness plus an exponential-rate limit plus IFR would not, abstractly, force location convergence. The missing information has to be stronger and model-specific.

## 3. B18 — say it in another language: the hazard is global frozen-pair density

Fix `n` and let

\[
N=\binom n2.
\]

Let `\mathcal C_m` denote all labelled 3-colourable graphs on `[n]` with exactly `m` edges, let

\[
a_m:=|\mathcal C_m|,
\qquad
p_m:=\frac{a_m}{\binom Nm},
\]

and let `Col(G)` be the set of proper 3-colourings of `G`.

For `G in \mathcal C_m`, define

\[
u\sim_G v
\quad\Longleftrightarrow\quad
\sigma(u)=\sigma(v)
\quad\text{for every }\sigma\in Col(G).
\tag{3.1}
\]

This is an equivalence relation. If its class sizes are `c_1,...,c_r`, set

\[
D(G):=\sum_{i=1}^r\binom{c_i}{2}.
\tag{3.2}
\]

Every frozen class is an independent set, because an edge `uv in E(G)` has opposite endpoint colours in every proper colouring. Therefore every pair counted by `D(G)` is a missing edge.

### Proposition 3.1 — exact frozen-pair hazard identity

For every colourable `G`,

\[
\boxed{
D(G)
=
\#\{e\notin E(G):G+e\text{ is not 3-colourable}\}.}
\tag{3.3}
\]

Consequently, if

\[
A_m:=N-m,
\qquad
\mu_m:=\mathbb E_m D(G),
\]

where `E_m` is uniform expectation on `\mathcal C_m`, then

\[
\boxed{
\frac{p_{m+1}}{p_m}=1-\frac{\mu_m}{A_m}.}
\tag{3.4}
\]

Thus the next-edge failure probability conditioned on layer-`m` 3-colourability is exactly

\[
\boxed{
r_m:=1-\frac{p_{m+1}}{p_m}=\frac{\mu_m}{A_m}.}
\tag{3.5}
\]

#### Proof

A missing pair `e={u,v}` makes `G+e` non-3-colourable iff **no** proper colouring of `G` separates `u` and `v`; this is exactly `u~_G v`, proving (3.3).

Hence the number of safe missing edges is

\[
S(G)=A_m-D(G).
\]

Double-count safe incidences `(G,e)` with `G in \mathcal C_m` and `G+e in \mathcal C_{m+1}`. Counting from below gives `sum_G S(G)`. Counting from above gives `(m+1)a_{m+1}` because every colourable `(m+1)`-edge graph has exactly `m+1` edge-deletion predecessors and all remain colourable. Therefore

\[
\sum_{G\in\mathcal C_m}(A_m-D(G))=(m+1)a_{m+1}.
\]

Divide by `a_m A_m` and use

\[
\frac{\binom N{m+1}}{\binom Nm}=\frac{A_m}{m+1}
\]

to obtain (3.4), hence (3.5). `square`

### Corollary 3.2 — exact sprinkling budget

For every `t>=1` with nonempty intermediate layers,

\[
\boxed{
-\log\frac{p_{m+t}}{p_m}
=
\sum_{j=m}^{m+t-1}-\log(1-r_j).}
\tag{3.6}
\]

In particular, because `-log(1-r)>=r`, a positive lower bound on the **average global frozen-pair hazard** `r_j` over `Theta(n)` consecutive layers yields an `e^{-Theta(n)}` conditional decay across that sprinkling window.

This is the first source-useful reframing of the run: the exponential-tail route is not asking generically for “many frozen variables.” It asks for a quantitative lower bound on

\[
\frac{\mathbb E[D(G_{n,m})\mid G_{n,m}\text{ 3-colourable}]}{\binom n2-m}
\]

in the correct near-threshold layer regime.

## 4. B13 — find what only increases: frozen coarsening versus survivor size bias

If `G subset H` and `H` is 3-colourable, then

\[
Col(H)\subseteq Col(G).
\]

Therefore every pair frozen in `G` remains frozen in `H`:

\[
\boxed{D(H)\ge D(G).}
\tag{4.1}
\]

So `D` is a genuine pathwise monovariant along safe edge additions. The tempting conjecture is then that the layer hazard `r_m` should also be monotone. The main point of this section is that this implication is **not automatic**: conditioning on survival size-biases toward lower-`D` graphs, and the exact competition can be written in one formula.

### Proposition 4.1 — exact safe-incidence transport identity

Let `\nu_m` be the uniform law on all safe incidences `(G,e)` from layer `m`, and write `H=G+e`. Define

\[
v_m:=\operatorname{Var}_m(D),
\qquad
J_m:=\mathbb E_{\nu_m}[D(H)-D(G)]\ge0.
\tag{4.2}
\]

Then

\[
\boxed{
\mu_{m+1}
=
\mu_m
-
\frac{v_m}{A_m-\mu_m}
+
J_m.}
\tag{4.3}
\]

#### Proof

Under the uniform safe-incidence law, the upper graph `H` is uniform on `\mathcal C_{m+1}` because each such `H` has exactly `m+1` deletion predecessors. The lower graph `G` is size-biased from the uniform law on `\mathcal C_m` by its number of safe extensions `S(G)=A_m-D(G)`. Therefore

\[
\mathbb E_{\nu_m}D(G)
=
\frac{\mathbb E_m[D(A_m-D)]}{A_m-\mu_m}
=
\mu_m-rac{v_m}{A_m-\mu_m}.
\]

Adding the mean coarsening jump `J_m` and using the uniform upper marginal gives (4.3). `square`

Equation (4.3) separates two effects exactly:

1. `J_m` is actual coarsening of the frozen partition and pushes the next-layer hazard upward;
2. `v_m/(A_m-\mu_m)` is survival size bias toward graphs with more safe extensions and pushes the next-layer mean downward.

This gives a concrete reason the pathwise monotonicity (4.1) does not itself settle the layerwise IFR conjecture tested in the previous run.

### Corollary 4.2 — exact IFR-defect formula

Using `r_m=\mu_m/A_m` and `A_{m+1}=A_m-1`,

\[
\boxed{
r_{m+1}-r_m
=
\frac{
J_m+\mu_m/A_m-v_m/(A_m-\mu_m)
}{A_m-1}.}
\tag{4.4}
\]

Hence layerwise discrete IFR / log-concavity at the transition is equivalent to

\[
\boxed{
J_m
\ge
\frac{v_m}{A_m-\mu_m}
-
\frac{\mu_m}{A_m}.}
\tag{4.5}
\]

A simple sufficient condition is

\[
\boxed{
v_m\le\frac{\mu_m(A_m-\mu_m)}{A_m},}
\tag{4.6}
\]

because `J_m>=0`.

This is a useful **counterexample-oriented diagnostic**. A failure of IFR, if it exists, must come from a layer where the survivor-size-bias variance term overwhelms both the deterministic denominator gain and the mean coarsening jump. Conversely, proving (4.5) or the stronger easy condition (4.6) in a source-relevant regime would certify IFR there. Neither is claimed asymptotically in this run.

## 5. B21 — who else has this shape? Frozen development is prior art; the transport formula is the new repository object

The terminology search changed the novelty assessment substantially.

Culberson--Gent (2001) already use essentially the global relation (3.1): two nodes are frozen when they have the same colour in **all** legal colourings, then merge frozen pairs into a collapsed graph. They report strong empirical evidence of sudden freezing in random 3-colouring and use frozen development to estimate tiny colourability probabilities. Therefore:

- the **global frozen-pair viewpoint is not new**;
- empirical sudden freezing is not a proof of the asymptotic hazard lower bound needed in (3.6);
- any publication claim must distinguish their mechanism from the exact layer-incidence identities here.

Molloy (2012) rigorously determines a freezing threshold, but his abstract defines a variable as frozen relative to a colouring/reconfiguration cluster: its colour cannot be changed through proper colourings using `o(n)`-vertex changes at a time. This is not the same quantifier as (3.1), which asks whether two vertices agree in **every legal colouring of the entire graph**. I found no justified implication from the cluster-freezing theorem to a positive global `r_m` of (3.5), so I do not use it as such.

A bounded search for the exact incidence-size-bias formula (4.3)--(4.5) did not recover it. That is not a novelty certificate. The correct label is:

**newly derived in this repository / novelty UNVERIFIED / source problem still OPEN.**

### What this route would need to close the missing exponential-tail step

The clean source-relevant next statement is now:

> For layer indices in a linear window just above an appropriate near-threshold anchor, prove that the uniform `m`-edge graph conditioned on 3-colourability has a positive average global frozen-pair hazard `r_m` (or directly positive average `-log(1-r_m)`).

By (3.6), that would generate the exponential sprinkling cost the preceding run identified as missing. It would still have to be connected carefully to the stopping-time mean/threshold-location convergence argument; I am **not** declaring that one hazard estimate alone closes F0095.

The most plausible mechanism suggested by (4.3) is to control the ratio between the coarsening gain `J_m` and the survivor-bias variance `v_m/(A_m-\mu_m)`, rather than to count frozen vertices inside one typical solution cluster.

## 6. Exact finite self-check — exhaustive only for n<=6

The idea was recorded first, before code, at:

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T12-50-00Z__f0095_frozen_hazard_derivation.md`

commit

`d36267bb510e61edfaf1036c96be8d1501f3876b`.

Only after that derivation was persisted did I add the exact finite checker:

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T12-50-00Z__f0095_frozen_incidence_exact.py`

commit

`ca44740da8f2ba0456a77ab85038713ef9f631f9`,

and archive its output at

`artifacts/hard7_2026-09-18/HARD7-06/2026-09-19T12-50-00Z__f0095_frozen_incidence_exact.out`

commit

`27f4977a1b1d34ba4a3a93e7c4ab9bdf9ce6484a`.

The checker uses only Python integers and `fractions.Fraction`. It enumerates **every labelled graph** for `n=4,5,6`, derives exact 3-colourability from all 3-colour partition masks, computes `D(G)`, and verifies:

- safe edges are exactly the missing non-frozen pairs;
- `D(H)>=D(G)` for every safe one-edge incidence;
- (3.4)/(3.5) exactly;
- the transport identity (4.3) exactly;
- the IFR-defect identity (4.4) exactly.

For `n=6`, the nontrivial rows include

\[
\begin{array}{c|c|c|c|c}
m&\mu_m&v_m&J_m&r_m\\\hline
5&30/1001&29130/1002001&135/998&3/1001\\
6&81/499&33858/249001&18/49&9/499\\
7&18/35&516/1225&96/131&9/140\\
8&156/131&12344/17161&1024/761&156/917\\
9&1836/761&697410/579121&90/91&306/761\\
10&279/91&4332/8281&5/11&279/455.
\end{array}
\]

The checker also finds nonnegative IFR defects on every checked internal layer for `n<=6`, consistent with the previous run's separate exact rank-log-concavity enumeration through `n<=7`. This is **finite evidence only**. It is not converted into an asymptotic theorem or a necessary condition.

The archived output ends twice, once per final audited block, with

`ALL_EXACT_CHECKS_PASS`.

I read back the derivation, checker, and output at their returned commits.

## 7. What the three methods did

### B18 — SAY IT IN ANOTHER LANGUAGE

**Succeeded structurally.** The generic safe-edge hazard became the exact global frozen-pair density `r_m=E[D]/(N-m)`. This gives a model-specific statistic rather than an abstract monotone-system hazard.

### B13 — FIND WHAT ONLY INCREASES

**Partly succeeded and refuted a naive inference.** The frozen partition coarsens pathwise, so `D` is monotone along safe extensions. But the exact transport identity exposes a negative survivor-size-bias variance term; pathwise monotonicity alone does not imply layerwise increasing hazard. The formula says exactly what a proof or counterexample must control.

### B21 — ASK WHO ELSE HAS THIS SHAPE

**Succeeded as prior-art correction and route refinement.** Culberson--Gent already own the global frozen-pair language empirically; Molloy's rigorous freezing is cluster-local rather than global-all-colourings. The next route must build an asymptotic global frozen-pair density theorem, not relabel cluster freezing or empirical frozen development as a proof.

## 8. Next obligation and stuck accounting

The fixed metric has now failed to move for two consecutive runs. If it fails to move once more, the next report must invoke Section I with the exact displayed blocker, full route-failure inventory, simplest unresolved special case, nearest solved analogue, and exactly one recovery choice.

Before that trigger, the mathematical obligation isolated by this run is:

\[
\boxed{
\text{control }\frac{1}{t}\sum_{j=m}^{m+t-1}
\frac{\mathbb E_jD}{N-j}
\text{ from below on a source-relevant }t=\Theta(n)\text{ window}.}
\tag{8.1}
\]

A direct attempt should not reuse B18/B13/B21. Tentative distinct next moves, subject to the mandatory Section-I trigger if the metric remains unchanged, are **B5 / B15 / B24**: interpolate density and differentiate the hazard, deliberately break symmetry to isolate large frozen classes, and search for the extremal conditioned colourable graphs that minimize global frozen-pair hazard.

## 9. Capability honesty

The requested configuration remains prompt text only. The exposed automation interface still has fields for title/prompt/schedule/timing mode/enabled state and **no model selector or reasoning-effort selector**. I therefore did not and cannot truthfully set GPT-6/maximum from this run. Actual runtime identity available to this report is **GPT-5.6 Sol**; reasoning level is **UNVERIFIED**.

The old policy file records historical native modification denials such as `You cannot modify this task` for P26/P01/P03. Root `RESULTS.md` now records that a later authorized context succeeded in updating P26 while some IDs in a separate context still rejected edits. The correct workaround for a genuine native permission denial is an authorized account/workspace context or platform support; creating a duplicate task or editing a repository file is not a scheduler repair. I made no automation changes in this run.

## 10. Structured ledger delta — report only, no shared-root write

```json
{
  "track": "HARD7-06",
  "target": "F0095",
  "status": "PARTIAL",
  "metric": "W_3",
  "before": "0.656508",
  "after": "0.656508",
  "movement": "no movement",
  "unchanged_streak": 2,
  "methods": ["B18", "B13", "B21"],
  "new_result": "Exact global frozen-pair hazard identity and safe-incidence transport/IFR-defect formula",
  "finite_check": "exhaustive labelled n=4,5,6 only; all exact checks pass",
  "next_obligation": "source-relevant positive average global frozen-pair hazard over a linear layer window; next unchanged run triggers Section I"
}
```

No email, Drive write, public posting, shared-ledger overwrite, other-track edit, or schedule modification was performed.
