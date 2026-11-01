Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated applied-model/reasoning selector or completed-run effort telemetry, so I do not claim otherwise. **NO MOVEMENT: H0006 `FSS_layers = 2/3 -> 2/3`; methods actually used: #4 PROVE SOMETHING WEAKER, COMPLETELY, #9 RANDOMIZE, #28 REPLACE “FOR ALL” WITH “FOR TYPICAL”.**

# R12 HARD OUTSIDE — H0006 fourth run: the sparse finite-graph window is `xi ~ N^{1/3}`, not the hard-cap `sqrt(N)` scale

Repository / branch: private `yspennstate/math-open-problems`, `master`.
Deployment: `NEW-METHODS-2026-09-16`.
Current exclusive claim: `operations/claims/H0006.md`.
Current source: Achyut Kumar (2026), arXiv:2608.15987, Section 12.3 open problem (4), **“Finite-size scaling on `G_n`.”**
Status after this run: **PARTIAL / OPEN**.

## 1. Continuity and controlling state

The native scheduler title still names Randomstrasse Conjecture 28 / I0102, but the newer immutable R12 history controls. I0102 was terminally handed off with best R12 uniform certificate `(a,C,p0)=(1/2,1,5)` and no further R12 recovery permitted. I0115 was later terminally handed off as well. R12 then passed successor admission and created the exclusive H0006 claim.

The immediately preceding R12 report is

`runs/R12/2026-09-18T10-32-19Z_h0006_geometry_rate_obstruction_03_f3a91c.md`.

It left the fixed metric at `2/3` and identified the remaining obligation: transfer the near-critical branching skeleton to the actual finite-graph cascade, with a quantitative graph-geometry error rather than bare Benjamini--Schramm convergence.

Before doing new mathematics I reread or exact-search recovered the required repository controls: campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the H0006 claim, the three preceding H0006 reports, the H intake row, and neighboring same-source H0003/H0005 state. H0003 and H0005 are distinct source questions and remain nonduplicate.

## 2. Source and current-literature check — 18 September 2026

The primary source remains Achyut Kumar, arXiv:2608.15987, submitted 17 August 2026. Its exact Section 12.3 item (4) asks for

> “Finite-size scaling on `G_n`. Quasi-stationary theory … for the cutoff `xi=(1-rho(M))^{-1}` against the finite size `n`; the window near criticality.”

A fresh bounded search on 18 September 2026 for the exact arXiv id/title, author, “finite-size scaling on G_n”, “near critical”, and later author papers again found no later paper closing this exact item. The Kumar--Duddala companion arXiv:2608.21125 (21 August 2026) treats front propagation/Bramson corrections and continuous-type limits, not this finite-graph scaling question. This is bounded negative evidence, not a worldwide novelty certificate.

The key older literature newly brought into the H0006 route is classical random-graph critical-window theory:

- A. Nachmias and Y. Peres, *Critical percolation on random regular graphs*, Random Structures & Algorithms 36 (2010), 111--148, DOI 10.1002/rsa.20277. For fixed `d>=3`, bond percolation on a uniform random `d`-regular graph has critical window width `N^{-1/3}` around `p_c=1/(d-1)`, with largest components of order `N^{2/3}` and Brownian-parabolic-excursion limits. Outside the window, the subcritical largest-component scale is `epsilon^{-2} log(epsilon^3 N)` up to the model's `d`-dependent constant.
- S. Dhara, R. van der Hofstad, J.S.H. van Leeuwaarden and S. Sen, *Critical window for the configuration model: finite third moment degrees*, EJP 22 (2017), article 16, DOI 10.1214/17-EJP29. They prove `N^{2/3}` component scaling and joint convergence of rescaled component sizes and surplus edges under finite third moments, including critical percolation on a supercritical configuration model.

These are prior art. I make no novelty claim for the `N^{-1/3}` random-graph critical window itself.

## 3. Frozen metric

The claim-file metric remains:

`FSS_layers` = number of nested source-valid layers with a rigorous explicit near-critical finite-size crossover:

1. exact one-type Bethe/Galton--Watson subclass;
2. general finite-type Galton--Watson skeleton;
3. actual finite-graph interacting-diffusion cascade on `G_N`, uniformly in the corresponding near-critical window.

Before this run: **2/3**.
After this run: **2/3**.

This is the **second consecutive unchanged H0006 run** after the movement to `2/3`. The three-run stuck protocol therefore does not yet fire.

The reason there is no metric movement is important: this run identifies the correct finite sparse-graph scaling and proves a structural obstruction to direct GW total-variation transfer, but it does not yet control the original interacting SDE uniformly in that window.

---

# 4. Method #4 — PROVE SOMETHING WEAKER, COMPLETELY: finite-graph completion of the Bethe skeleton

The previous reports correctly found the infinite-tree total-progeny cutoff

\[
\text{GW progeny cutoff}\asymp \xi^2,
\qquad
\xi=(1-\rho)^{-1}.
\tag{4.1}
\]

They then observed that forcing this cutoff all the way to the absolute graph-size cap `N` gives `xi ~ sqrt(N)`. That calculation is correct as a **hard-cap identity**, but it is not the onset of finite sparse-graph effects. Random-graph depletion and collisions become leading much earlier.

To isolate that effect completely, take the simplest finite-graph completion of the exact one-type Bethe skeleton:

- `G_N` is a uniform random `d`-regular graph, fixed `d>=3`;
- each edge is independently retained with probability `p_N`;
- explore the retained component of a uniform root.

Locally, before collisions, the non-root offspring law is exactly

\[
X_N\sim\operatorname{Bin}(d-1,p_N),
\qquad
\rho_N=(d-1)p_N,
\tag{4.2}
\]

which is the same one-type branching skeleton used in H0006 layer 1. This finite model is **not asserted to equal Kumar's interacting-diffusion cascade**; it is the canonical finite-graph Bernoulli completion of the same Bethe skeleton, and therefore a source-relevant weaker problem.

## Proposition 4.1 — the finite sparse-graph window

Let

\[
p_N=\frac{1+\lambda N^{-1/3}+o(N^{-1/3})}{d-1}
\tag{4.3}
\]

for fixed `lambda` in a bounded set. Then classical random-regular percolation theory yields

\[
|\mathcal C_{(j)}|\asymp N^{2/3}
\tag{4.4}
\]

for the largest critical components, with nondegenerate Brownian-parabolic-excursion scaling limits. Equivalently, for `lambda != 0`,

\[
1-\rho_N\asymp N^{-1/3},
\qquad
\boxed{\xi_N\asymp N^{1/3}.}
\tag{4.5}
\]

Combining (4.1) and (4.5),

\[
\boxed{\xi_N^2\asymp N^{2/3},}
\tag{4.6}
\]

which exactly matches the finite critical component-volume scale.

Thus the right matching is not

\[
\xi^2\sim N,
\]

but rather

\[
\boxed{
\text{tree progeny cutoff }\xi^2
\sim
\text{finite critical component scale }N^{2/3}.
}
\tag{4.7}
\]

The old `xi~sqrt(N)` scale lies **inside** the finite critical window: by the time `1-rho` has fallen to `N^{-1/2}`, depletion and collisions have already been leading-order for an entire `N^{-1/3}` window.

## 4.2 Three mutually consistent scales

The source's quasi-stationary language and the previous two R12 results now line up cleanly:

\[
\boxed{
\begin{array}{c|c|c}
\text{observable} & \text{infinite-GW scale} & \text{finite sparse-graph scale}\\
\hline
\text{generation / QSD lifetime} & \xi & N^{1/3}\\
\text{total progeny cutoff} & \xi^2 & N^{2/3}\\
\text{whole graph volume} & - & N
\end{array}}
\tag{4.8}
\]

At the true finite-size crossover, `xi~N^{1/3}`. The source's desired replacement of a cluster-volume error by a **front-width** error is also consistent with this: a critical cluster of volume `s~N^{2/3}` has tree-like height/front scale `sqrt(s)~N^{1/3}`.

## 4.3 Elementary exploration balance

The exponents can also be recovered without importing the final random-graph theorem. Explore a locally tree-like finite graph for `s` discovered vertices near criticality.

- martingale fluctuations of the active frontier are order `sqrt(s)`;
- finite-population depletion produces cumulative deterministic drift of order `s^2/N`;
- a spectral subcriticality `epsilon=1-rho` produces drift of order `epsilon s`.

The critical finite-size balance is

\[
\sqrt{s}\asymp \frac{s^2}{N},
\]

hence

\[
\boxed{s\asymp N^{2/3}.}
\tag{4.9}
\]

Balancing near-critical drift with noise at that size,

\[
\epsilon s\asymp\sqrt{s},
\]

gives

\[
\boxed{\epsilon\asymp N^{-1/3},\qquad \xi\asymp N^{1/3}.}
\tag{4.10}
\]

This is the mechanism the direct infinite-GW comparison deletes: the `s^2/N` depletion term is negligible on every fixed local neighborhood but leading at finite-size criticality.

**Outcome of #4:** success. A complete, literature-backed finite-graph theorem for the Bernoulli completion of the one-type skeleton identifies the correct mean-field finite-size exponents. It is still PARTIAL for H0006 because the original interacting SDE has not been transferred to this finite exploration law.

---

# 5. Method #9 — RANDOMIZE: a quantitative TV floor from surplus edges

The preceding run found that a direct total-variation route from the actual finite graph to the infinite GW law would need errors smaller than the rare-event probability being resolved. The random-graph critical window shows something stronger: at finite-size criticality there is an **unavoidable total-variation defect of exactly the relevant order**, even in the ideal finite Bernoulli skeleton.

## Proposition 5.1 — critical finite-graph cluster vs a tree-valued GW law

Consider a finite-third-moment configuration model in its standard `N^{-1/3}` critical window, and percolate in the corresponding critical window. Let `V_N` be a uniformly chosen vertex and let `C_N(V_N)` be its finite component as a rooted graph. Let `T_N` be any tree-valued law, in particular the matching Galton--Watson genealogy.

Then for some constant `c>0` along the critical sequence,

\[
\boxed{
\liminf_{N\to\infty}
N^{1/3}\,
 d_{\rm TV}\!\left(
 \mathcal L(C_N(V_N)),
 \mathcal L(T_N)
 \right)
>0.
}
\tag{5.1}
\]

### Proof

Let `A` be the event that the rooted connected component contains a cycle, equivalently has at least one surplus edge. Every tree-valued law satisfies

\[
\Pr(T_N\in A)=0.
\tag{5.2}
\]

Hence

\[
d_{\rm TV}(\mathcal L(C_N(V_N)),\mathcal L(T_N))
\ge
\Pr(C_N(V_N)\in A).
\tag{5.3}
\]

Condition on the finite percolated graph, whose connected components are `C_1,C_2,...`, and write `sp(C_i)` for surplus. Uniform rooting gives the exact identity

\[
\Pr(C_N(V_N)\in A\mid G_N)
=
\frac1N\sum_i |C_i|\,\mathbf 1_{\{sp(C_i)\ge1\}}.
\tag{5.4}
\]

Dhara--van der Hofstad--van Leeuwaarden--Sen prove joint critical-window convergence of

\[
\left(N^{-2/3}|C_i|,\,sp(C_i)\right)_{i\ge1}
\]

to Brownian-parabolic excursions with their surplus marks. The limiting marked process is nondegenerate: there exist finite `K`, `delta>0`, and `q>0` such that with limiting probability at least `q`, one of the first `K` components has scaled size at least `delta` and positive surplus. By convergence, for all sufficiently large `N` this event has probability at least `q/2`, and on it

\[
\sum_i |C_i|\mathbf 1_{\{sp(C_i)\ge1\}}
\ge \frac\delta2 N^{2/3}.
\]

Taking expectations in (5.4),

\[
\Pr(C_N(V_N)\in A)
\ge
\frac{q\delta}{4}N^{-1/3}
\]

for all sufficiently large `N`, proving (5.1). QED.

The point is not the particular cycle event. It is that finite-size geometry is a **leading-order perturbation**, not a remainder that can be squeezed below the branching survival scale while keeping an infinite-tree target.

## 5.2 Same order as the crossover probabilities

For a critical finite-variance GW process,

\[
\Pr(T=n)\asymp n^{-3/2},
\qquad
\Pr(T\ge n)\asymp n^{-1/2},
\qquad
\Pr(Z_k>0)\asymp k^{-1}.
\tag{5.5}
\]

Insert the finite-size scales `n~N^{2/3}` and `k~N^{1/3}`:

\[
\boxed{
\Pr(T\ge xN^{2/3})\asymp N^{-1/3},
\qquad
\Pr(Z_{tN^{1/3}}>0)\asymp N^{-1/3}.
}
\tag{5.6}
\]

Meanwhile a point probability at `n=floor(xN^{2/3})` is

\[
\boxed{\Pr(T=n)\asymp N^{-1}.}
\tag{5.7}
\]

Therefore the unavoidable `N^{-1/3}` TV floor in (5.1) is already the same order as the root-level finite-size tail and quasi-stationary probabilities. A direct comparison with an infinite GW tree can still converge in **absolute** total variation, because `N^{-1/3}->0`; it cannot by itself determine the relative finite-size crossover.

This sharpens the preceding report. Its sufficient condition

\[
N^{1/3}\eta_N\to0
\]

for direct tail/QSD transfer is not merely absent under bare Benjamini--Schramm convergence. In a canonical mean-field finite-graph model, an infinite-tree comparison has a geometric defect at order `N^{-1/3}` and therefore cannot satisfy that condition if `eta_N` faithfully includes the cycle/depletion error.

**Outcome of #9:** success. Randomizing the graph identifies a structural lower bound on the error of the wrong comparison target.

---

# 6. Method #28 — REPLACE “FOR ALL” WITH “FOR TYPICAL”: the correct two-stage target

The previous H0006 run proved that bare Benjamini--Schramm convergence can have arbitrarily slow short-cycle error. Consequently no universal `N`-only crossover can follow from that qualitative hypothesis.

The random-regular/configuration-model calculation suggests the right narrower theorem:

\[
\boxed{
\text{interacting SDE cascade}
\ \longrightarrow\ 
\text{finite depleted exploration skeleton}
\ \longrightarrow\ 
\text{Brownian-parabolic finite-size limit},
}
\tag{6.1}
\]

not

\[
\text{interacting SDE cascade}
\ \longrightarrow\ 
\text{infinite GW}
\ \longrightarrow\ 
\text{finite-size limit}.
\tag{6.2}
\]

The second arrow in (6.2) cannot recover the leading `s^2/N` depletion term because the infinite GW target has no collisions or surplus edges.

For a typical random regular or finite-third-moment configuration-model graph, finite exploration already has a canonical Markov description: remaining half-edges are sampled without replacement. After centering and `N^{1/3}`/`N^{2/3}` rescaling, the depletion term becomes the parabolic drift in the exploration process. That is the correct object to couple the diffusion cascade to.

This gives a precise new layer-3 intermediate target:

> **Finite-skeleton transfer target.** In the near-critical window `1-rho(M_N)=O(N^{-1/3})`, couple the actual interacting-diffusion failed-cluster exploration on a random regular/configuration-model `G_N` to a finite-population multitype exploration process that retains vertex depletion and cycle closures, with error `o(N^{-1/3})` on root-tail/QSD events.

If this is proved, existing critical random-graph machinery can plausibly supply the finite-size limit. The infinite-GW comparison remains valuable only below the scale on which depletion is leading.

## 6.1 What the source's current error bound says at the corrected window

The source's dissipative comparison has the schematic form

\[
D_N
\le
C\frac{\varepsilon_{\rm sat}(\delta_N)}
{(1-\kappa\rho(M_N))^2(1-\rho(M_N))}
+\eta_N.
\tag{6.3}
\]

For fixed `kappa<1` and the actual mean-field finite-size window

\[
1-\rho(M_N)\asymp N^{-1/3},
\]

this becomes

\[
D_N=O\!\left(
\varepsilon_{\rm sat}(\delta_N)N^{1/3}+\eta_N
\right).
\tag{6.4}
\]

If one nevertheless tried the direct infinite-GW transfer for a tail or QSD probability of order `N^{-1/3}`, sufficient relative precision would require

\[
D_N=o(N^{-1/3}),
\tag{6.5}
\]

hence formally

\[
\varepsilon_{\rm sat}(\delta_N)N^{2/3}\to0,
\qquad
N^{1/3}\eta_N\to0.
\tag{6.6}
\]

The first condition is exactly compatible with the source's hope that a cluster-volume error of order `s epsilon_sat` be controlled at `s~N^{2/3}`. The second condition is the wrong demand on the **graph** error: Proposition 5.1 shows that finite critical geometry itself naturally contributes at order `N^{-1/3}`. So the graph correction should not be driven to zero relative to the crossover; it should be retained in the limiting finite exploration process.

For a pointwise local law at size `n~N^{2/3}`, whose mass is order `N^{-1}`, a crude TV transfer to infinite GW would require the still stronger `D_N=o(N^{-1})`. This is even less appropriate.

## 6.2 What remains genuinely unproved

The missing H0006 layer is now much more sharply isolated:

1. choose a source-valid random-graph subclass, preferably random regular first;
2. derive the finite-population multitype exploration kernel induced by the threshold-diffusion front;
3. prove a uniform coupling of the actual cascade front to that finite kernel throughout `O(N^{2/3})` discoveries / `O(N^{1/3})` generations;
4. show the centered exploration has the correct Brownian covariance and the finite-population drift projects through the Perron directions to a nonzero parabolic term;
5. invoke or extend finite-type critical configuration-model scaling to obtain the limiting component sizes, lifetimes and QSD observables.

The difficult step is now (3), not the branching-process asymptotics. The front-decoupling estimate has to be strong enough on a growing exploration while preserving the leading collision/depletion term instead of absorbing it into `eta_N`.

**Outcome of #28:** success as a route change. It gives a realistic theorem class (“typical random regular/configuration-model `G_N`”) in which the finite-size question is quantitatively posed. It still does not prove the original finite-graph SDE layer, so no metric movement is claimed.

---

# 7. Correction to the interpretation of the earlier `sqrt(N)` statement

For continuity and to prevent a false fleet conclusion, the earlier H0006 reports must be read with the following distinction.

The formula

\[
\xi^2\asymp N
\iff
\xi\asymp\sqrt N
\tag{7.1}
\]

is an exact statement about when the **infinite-tree progeny cutoff** reaches an imposed hard maximum size `N`. It is not the finite-size critical window of a sparse random graph.

For a locally tree-like sparse graph, the finite exploration ceases to look like an unconstrained GW tree already at component volume `N^{2/3}`, yielding

\[
\boxed{
\xi^2\asymp N^{2/3}
\iff
\xi\asymp N^{1/3}.
}
\tag{7.2}
\]

No earlier immutable report is edited. This report records the corrected interpretation and supersedes any wording that called `sqrt(N)` the genuine finite-graph crossover.

---

# 8. Prior-art and novelty discipline

The following mechanisms are **KNOWN / prior art** and are not claimed as R12 discoveries:

- `N^{-1/3}` critical-window width and `N^{2/3}` component sizes for random regular percolation;
- Brownian motion with parabolic drift / multiplicative-coalescent finite-size limits;
- joint component-size and surplus-edge scaling in finite-third-moment configuration models;
- critical GW `n^{-3/2}` progeny and `k^{-1}` survival laws.

The R12 contribution in this run is only the **source-specific synthesis and obstruction**: once H0006's Perron gap `xi=(1-rho)^{-1}` and the already-proved `xi^2` GW cutoff are matched to actual finite sparse-graph exploration, the correct mean-field relation is `xi~N^{1/3}`; moreover, surplus-edge mass forces an `Omega(N^{-1/3})` TV defect between the finite critical rooted cluster and every tree-valued GW law, so an infinite-GW comparison is intrinsically too coarse to identify the relative finite-size crossover. A dedicated prior-art search for this exact H0006 formulation has not established novelty, so novelty remains **UNVERIFIED**.

# 9. Next run

The source metric remains `2/3`. This is unchanged run 2 after the last movement, so the next run is still a normal research run. It should attack the finite-skeleton coupling rather than add another GW asymptotic.

Reserved nonrepeating Section-B methods for the next run:

- **#6 DEFORM TO A POINT YOU CAN SOLVE:** start at zero back-reaction / exact independent front, then turn on `kappa` and track the finite exploration kernel;
- **#12 FIND WHAT IS CONSERVED:** identify a Perron-weighted exploration martingale that survives depletion and front coupling;
- **#24 FIND THE EXTREMAL OBJECT:** locate the worst front-history configuration for the one-step coupling error, instead of bounding all histories by cluster volume.

If that run also leaves `FSS_layers=2/3`, it will be the third consecutive unchanged H0006 run and the following invocation must be the full Section-I thinking-only stuck run.

# 10. Model / scheduler control status

The currently exposed scheduler/task-control schema still has no binding model-family selector and no reasoning-effort selector. It exposes task title/prompt, timing/schedule, enablement and timing mode, but GPT-6/maximum can only be requested in prompt text. A successful prompt update would not authenticate the model actually used. Product/runtime support would need to expose (i) a binding model field, (ii) a binding reasoning-effort field, and (iii) completed-run telemetry attesting the applied values.

The historical P26 `You cannot modify this task` response is an authorization/ownership boundary, not a research issue. The legitimate workaround is the owning account/workspace context, ownership transfer if the product supports it, or platform support. Do not duplicate the task or bypass permissions. No scheduler state was changed in this run.

# 11. Structured ledger delta

```yaml
ledger_delta:
  track: R12
  lane: HARD_OUTSIDE
  target: H0006
  source: "Kumar 2026 arXiv:2608.15987 Section 12.3 open problem (4)"
  metric: FSS_layers
  before: "2/3"
  after: "2/3"
  movement: "no movement"
  status: "PARTIAL / OPEN"
  supported_unchanged_streak_before: 1
  supported_unchanged_streak_after: 2
  methods_actual: [4, 9, 28]
  key_new_partial:
    - "Correct finite sparse-graph mean-field window: 1-rho = Theta(N^{-1/3}), xi = Theta(N^{1/3}), component volume Theta(N^{2/3})."
    - "The earlier xi~sqrt(N) relation is only where the infinite-GW progeny cutoff xi^2 hits the absolute hard cap N; it is not the sparse finite-graph critical window."
    - "Surplus-edge scaling yields a TV floor Omega(N^{-1/3}) between a critical finite rooted configuration-model cluster and every tree-valued GW law."
    - "Therefore layer 3 needs a finite depleted exploration target, not a higher-precision direct comparison to infinite GW."
  finite_core_checker: "none warranted; all new claims are analytic/literature-backed asymptotic statements, with no finite enumeration core"
  prior_art_status: "random-graph scaling mechanisms KNOWN; exact H0006 synthesis novelty UNVERIFIED"
  remaining_obligation: "Uniformly couple the actual threshold-diffusion cascade on a source-valid random-graph subclass to a finite-population multitype exploration through O(N^{2/3}) discoveries while preserving the leading parabolic depletion term."
  next_methods: [6, 12, 24]
  stale_targets_not_reopened: [I0102, I0115]
```
