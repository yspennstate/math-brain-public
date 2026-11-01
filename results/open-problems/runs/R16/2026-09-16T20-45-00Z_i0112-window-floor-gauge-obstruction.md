Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no model selector, no reasoning-effort selector, and no authenticated telemetry establishing GPT-6/maximum. **NO MOVEMENT:** `W_exp = 1/2 (provisional) -> 1/2 (provisional)`. This run proves that `1/2` is an absolute window-exponent floor for any cutoff source family and kills the simplest cross-generator perturbation as a disguised Cartesian product. Methods actually tried: **#5 ADD A PARAMETER AND DIFFERENTIATE, #12 FIND WHAT IS CONSERVED, #27 SWAP THE QUANTIFIERS.**

Problem/source: **R16 / I0112 — Justin Salez (2025), _Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon_, arXiv:2508.21055v1, Problem 2.3: prove that all bounded-degree vertex-transitive expander sequences exhibit total-variation cutoff.** Status: **PARTIAL**.

# R16 — the square-root window is an absolute floor, and one automorphic cross-matching is gauge-trivial

Run ID: `2026-09-16T20-45-00Z_i0112-window-floor-gauge-obstruction`.
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and mandatory state recovery

I did not restart R16 or Beck--Fiala. Before mathematics I read/searched the required current state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the current owner directive;
- canonical ownership `operations/claims/I0112.md`;
- the newest complete own report, `runs/R16/2026-09-16T19-48-00Z_i0112-synchronous-tensor-cutoff.md`;
- the immediately preceding I0112 product/varentropy report;
- the current Salez-neighbor report `runs/R01/20260916T2003Z_i0113_weak_dependency_01.md`;
- current R12 state. R12 has now exhausted and handed off its Paley I0102 target and created the HARD-OUTSIDE I0060/FPP Question-17 claim. There is no complete R12/I0060 proof package to audit yet, so `R16_AUDIT_R12=PENDING_NOT_READY`.

The intake JSONL corpus is too large for a literal one-response rendering. I recovered the exact I0112 intake/claim hits and relevant neighboring ownership; I do not claim a byte-for-byte semantic reread of all roughly 780 rows.

### Frozen metric and inherited state

The canonical R16 metric is

\[
W_{\exp}:=\inf\Bigl\{w\in[0,1]:
\text{R16 rigorously certifies a new source-admissible family with cutoff window }
O((\log|V|)^w)\Bigr\},
\]

with `UNMEASURED` if no family beyond already-published classes has been cleared.

The preceding run proved, on the page, that synchronous direct squares of suitable fixed-degree non-bipartite vertex-transitive Ramanujan families have continuous-time cutoff with window

\[
O(\sqrt{\log |V|}).
\]

It therefore recorded `W_exp = 1/2` **provisionally**, because the mathematical theorem was proved but full prior-art/class clearance and the two external audits remained pending. That is the exact before-value used here; I do not reset it to `UNMEASURED` or relabel the same exponent as new movement.

## 2. Dated source/literature refresh — 16 September 2026

### Originating Beck--Fiala source

The originating R16 Beck--Fiala problem remains literature-`KNOWN`, not reopened. The current arXiv record for Guo--Fang--Lu, `arXiv:2609.11189v1` (10 September 2026), still states the stronger Komlos theorem and explicitly the all-`t` Beck--Fiala consequence

\[
\operatorname{disc}(A)<3\sqrt{2\pi t}
\]

for every finite set system of maximum degree `t>=1`. Bansal--Jiang `arXiv:2508.03961` remains the earlier baseline: square-root order for `t>=log^2 n` and a polylogarithmically weakened bound below. A bounded current search found no v2/withdrawal/proof-specific correction to Guo--Fang--Lu. A negative bounded search is not mature referee validation.

### I0112 source

Salez's live notes still state Problem 2.3 literally: prove that all vertex-transitive expanders exhibit cutoff. The notes also state that expander mixing times are logarithmic in the number of vertices.

Fresh later-literature checks included:

- Dylan J. Altschuler, `arXiv:2609.14945`, submitted 14 September 2026: every fixed-degree long-range expander has Gaussian-profile cutoff; the abstract explicitly describes this as intermediate progress toward the transitive spectral-expander conjecture.
- Pedrotti--Salez, `arXiv:2607.05345`, _The local product condition implies cutoff_: window control through a non-equilibrium/local Poincare constant `gamma_*`.
- Salez, `arXiv:2307.10066`, _The varentropy criterion is sharp on expanders_: on sparse fast-mixing chains, cutoff is equivalent to the varentropy criterion.
- Hermon--Huang--Pedrotti--Salez, `arXiv:2409.16869`, _Concentration of information on discrete groups_: conjugacy-invariant group walks have uniformly bounded varentropy in the number of generators. This does not cover arbitrary vertex-transitive graphs.
- Guan-Yu Chen--Laurent Saloff-Coste, `arXiv:1304.4587`, _Comparison of cutoffs between lazy walks and Markovian semigroups_. Theorem 3.4 below is decisive for the frozen R16 metric.

A bounded search for `direct product graph cutoff`, `synchronous product Markov chain cutoff`, `tensor product Markov chain cutoff`, `finite cover cutoff`, and `semidirect product cutoff` did not locate a theorem that I can honestly identify as exactly the preceding R16 synchronous-square statement. This negative search is **not** a novelty certificate. More importantly, this run finds an internal reason not to spend another hour on the simplest proposed cross-matching perturbation.

## 3. R16-I0112-C06 — universal square-root lower bound on cutoff windows for source expanders

**STATUS: PROVED from a primary published theorem plus a self-contained expander mixing-time comparison. This is a metric obstruction, not a solution of Salez Problem 2.3.**

### Statement

Let `(G_n)` be any sequence of finite connected regular graphs with

- `N_n=|V(G_n)| -> infinity`,
- degrees uniformly bounded by a constant `D`,
- continuous-time spectral gaps bounded below by `gamma_0>0`.

Suppose continuous-time simple random walk on `(G_n)` has a total-variation `(t_n,b_n)` cutoff in the standard sense. Then

\[
\boxed{t_n=\Theta(\log N_n)}
\]

and necessarily

\[
\boxed{b_n=\Omega(\sqrt{\log N_n}).}
\tag{C06.1}
\]

Consequently no source-admissible vertex-transitive expander family can have a genuine total-variation cutoff window `O((log |V|)^w)` with `w<1/2`.

### Proof: `t_n=O(log N_n)`

For a regular graph the stationary law is uniform. Let `P_n` be the simple-random-walk kernel and let `lambda_n>=gamma_0` be the smallest positive eigenvalue of `I-P_n`. For the continuous-time semigroup,

\[
\chi^2(P_t(x,\cdot)\|\pi)
\le (N_n-1)e^{-2\gamma_0 t}.
\]

Therefore

\[
\|P_t(x,\cdot)-\pi\|_{\rm TV}
\le \frac12\sqrt{N_n-1}\,e^{-\gamma_0t}.
\]

Hence every fixed-accuracy mixing time is `O(log N_n)`.

### Proof: `t_n=Omega(log N_n)`

Let the maximum degree be at most `D`. A continuous-time walk has made `K_t~Pois(t)` jumps by time `t`. For `t=c log N_n`, with `c>0` chosen so small that

\[
2c\log(D-1)<1,
\]

Poisson concentration gives `P(K_t<=2t)->1`. On that event the walk remains in the graph ball of radius `2t` around its start. Such a ball has size at most

\[
C_D(D-1)^{2t}=N_n^{2c\log(D-1)+o(1)}=o(N_n).
\]

Thus the walk assigns probability tending to one to a set whose stationary mass tends to zero, and its total-variation distance tends to one. Therefore any fixed-accuracy mixing time is `Omega(log N_n)`.

Since a cutoff location is asymptotic to every fixed-accuracy mixing time, `t_n=Theta(log N_n)`.

### Proof: the window floor

Chen--Saloff-Coste, Theorem 3.4 of `arXiv:1304.4587`, states for an arbitrary family of irreducible positive recurrent chains that if the associated continuous semigroups exhibit a `(t_n,b_n)` total-variation cutoff with `t_n->infinity`, then

\[
\sqrt{t_n}=O(b_n).
\]

Combining this primary theorem with `t_n=Theta(log N_n)` gives (C06.1).

`QED`

### Consequence for the R16 metric

This changes the interpretation of the preceding run. The exponent `1/2` is not merely a good target: it is the **absolute theoretical floor** for this continuous-time total-variation window metric on bounded-degree expanders. Therefore a future R16 family cannot move the numerical metric below `1/2` at all.

I do **not** count that as numeric metric movement: before and after remain `1/2` provisionally. What improved is the certification: once the prior-family/class-clearance gate is discharged, `1/2` is automatically optimal for the frozen metric.

This was Section-B move **#27 (SWAP THE QUANTIFIERS)**: instead of asking for one family with a narrower window, quantify over every possible cutoff family and prove that no exponent below `1/2` can occur.

## 4. The proposed one-cross-generator perturbation is exactly gauge-trivial

The preceding report proposed trying to perturb the synchronous kernel `P tensor P` by a transitive cross-generator so that neither labeled coordinate projection remains Markov. This run tested the simplest such construction rather than assuming that breaking the visible projection creates genuinely new dynamics.

### R16-I0112-C07 — one automorphic matching between two layers is a disguised Cartesian product

**STATUS: PROVED. Elementary/structural; no novelty claim. It is a route obstruction.**

Let `H=(X,E)` be any finite graph and let `phi in Aut(H)`. Construct a two-layer graph `J_phi` on `X x {0,1}` as follows:

1. each layer induces a copy of `H`;
2. add the perfect matching
   \[
   (x,0)\sim(\phi(x),1),\qquad x\in X.
   \]

Then

\[
\boxed{J_\phi\cong H\square K_2.}
\tag{C07.1}
\]

### Proof

Define

\[
F(x,0)=(x,0),\qquad
F(x,1)=(\phi^{-1}x,1).
\]

A layer-0 edge is unchanged. A layer-1 edge `x~y` maps to `phi^{-1}x ~ phi^{-1}y` because `phi` is a graph automorphism. Finally, the matching edge

\[
(x,0)\sim(\phi x,1)
\]

maps to

\[
(x,0)\sim(x,1),
\]

which is precisely the `K_2` Cartesian edge. Thus `F` is a graph isomorphism. `QED`

### Application to the tempting swap perturbation

Take the preceding direct square

\[
H_N=G_N\times G_N
\]

and let `phi(x,y)=(y,x)`. The two-layer graph that has direct-square edges inside each layer and cross-edges

\[
(x,y,0)\sim(y,x,1)
\]

looks as if the extra generator destroys both coordinate projections. C07 shows that it is exactly

\[
H_N\square K_2
\]

in hidden coordinates. Therefore it is **not** a new non-product mechanism.

The Markov version makes the same point quantitatively. Put

\[
A=P\otimes P,\qquad M(x,y,b)=(y,x,1-b),
\]

and, for `0<eta<1`, consider

\[
Q_\eta=(1-\eta)A+\eta M.
\]

Under the coordinate change

\[
\Phi(x,y,0)=((x,y),0),\qquad
\Phi(x,y,1)=((y,x),1),
\]

`A` acts only on the first component and `M` flips only the second. Hence

\[
Q_\eta\cong (1-\eta)A\otimes I+\eta I\otimes F,
\]

an ordinary asynchronous product with a two-state chain. If the `A`-chain has cutoff at `tau_n` with window `w_n`, this perturbation merely rescales the slow center to

\[
T_\eta=\frac{\tau_n}{1-\eta}
\]

(up to the constant-time fiber relaxation), with

\[
\frac{dT_\eta}{d\eta}
=
\frac{\tau_n}{(1-\eta)^2}.
\]

No new mixing mechanism appears.

This is Section-B move **#5 (ADD A PARAMETER AND DIFFERENTIATE)**: the interpolation parameter `eta` exposes that the whole one-matching deformation only differentiates the time scale; it does not change the structural class.

## 5. Method #12 — the hidden conserved coordinate and what a genuine next perturbation must destroy

C07 can be rephrased as a conservation/gauge statement. In the swap-layer example the hidden coordinate

\[
Z=\begin{cases}
(x,y),&b=0,\\
(y,x),&b=1
\end{cases}
\]

is unchanged by the cross matching and evolves under the direct-square walk under within-layer steps. The apparent cross coupling is therefore removable by a layer-dependent relabeling.

More generally, **any single perfect matching between two identical layers that is induced by a graph automorphism is gauge-removable** by C07. So the next perturbation cannot just be “add one clever automorphic matching.” To escape this obstruction, a two-layer construction must contain at least two incompatible cross matchings (after gauging one to the identity, a nontrivial residual automorphism remains), or a cross relation that is not an automorphism matching at all. Maintaining vertex transitivity and a uniform spectral gap after that change is the real design problem.

This was Section-B move **#12 (FIND WHAT IS CONSERVED)**. Outcome: the suggested simplest cross-generator route is completely classified and rejected before another product lemma was written.

## 6. What the new window floor says about future R16 strategy

C06 exposes a weakness in the frozen progress metric itself: `W_exp=1/2` is a hard floor once any qualifying family reaches it. Therefore future genuine progress on Salez 2.3 cannot appear as a smaller exponent. Per the owner rule I do **not** silently replace the metric mid-track, and I do not relabel larger family coverage as numeric movement.

The source problem is still vastly stronger: prove cutoff for **every** bounded-degree vertex-transitive expander. The most promising current general criteria remain:

1. **Varentropy:** Salez proves that on sparse fast-mixing chains, cutoff is equivalent to the varentropy criterion. Thus a universal transitive-expander proof can be sought by showing information fluctuations are `o((log N)^2)` at the relevant times.
2. **Local Poincare:** Pedrotti--Salez prove a window bound `O(1/gamma_*)` using a non-equilibrium Poincare constant. The group result of Hermon--Huang--Pedrotti--Salez gives strong information concentration for conjugacy-invariant walks, but vertex transitivity alone does not provide conjugacy invariance.

The current general obstruction is therefore not the unavoidable square-root Poisson window; C06 shows that scale is expected. The hard missing statement is a **uniform non-equilibrium concentration principle from transitivity + spectral expansion alone**.

### Next genuinely new methods

Do not repeat this run's `#5,#12,#27`, nor the prior `#10,#11,#15`. A next run should try:

- **#3 PROVE SOMETHING STRONGER:** seek a time-local information/Poincare inequality for every transitive expander that directly implies the source conjecture;
- **#14 FIND THE GROUP ACTING:** express the heat-kernel law through the automorphism-group action/stabilizer pair and ask whether the missing concentration inequality is a Gelfand-pair/spherical-function statement rather than a Cayley-group statement;
- **#20 FIND WHY THE ALGORITHM FAILS:** construct the smallest transitive expander family for which the local Poincare constant `gamma(mu_t)` becomes much smaller than the equilibrium gap near mixing, or prove this cannot happen in a source-relevant subclass.

The first serious cross-generator construction should use at least two incompatible matchings or a genuine semidirect extension; C07 says one automorphic matching is just notation.

## 7. R12 directed audit status

The revised R12 assignment was read from the repository rather than assumed to be the old AT task. R12 has now handed off I0102/Paley after exhausting two stuck recoveries and created canonical claim `operations/claims/I0060.md` for Auffinger--Damron--Hanson, _50 years of first passage percolation_, Question 17:

\[
\underline\chi_2=\overline\chi_{2+\delta}
\quad\text{for some }\delta>0.
\]

The I0060 file is an ownership/admission claim, not a completed proof package. Therefore there is nothing source-level complete for R16 to independently audit this run. Status: `R16_AUDIT_R12=PENDING_NOT_READY`. No audit is invented.

## 8. Model/scheduler escalation status

Nothing changed in the exposed runtime capability. Task text can request GPT-6/maximum, but this runtime exposes no model selector and no reasoning-effort selector, and no authenticated telemetry verifies that request. Prompt text therefore cannot enforce the requested model.

The controlling repository policy records earlier native modification probes for P26/P01/P03 returning `You cannot modify this task`. The compliant workaround is correction through the authorized owner/workspace interface or platform support. Creating duplicate jobs, bypassing permissions, or treating a repository prompt edit as a scheduler repair is not acceptable. I made no scheduler change.

## 9. Checker / artifact decision

No new checker was created this run. C06 is an asymptotic theorem whose nontrivial window lower bound is a cited primary theorem, and C07 is a universal explicit graph isomorphism proved on the page. There is no new finite enumeration or numerical certificate whose correctness would be improved by manufacturing another artifact. This follows the 90-percent new-methods rule rather than producing a receipt for an unchanged metric.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R16
  active_source: "Justin Salez (2025), arXiv:2508.21055v1, Problem 2.3"
  source_target: "all bounded-degree vertex-transitive expander sequences exhibit total-variation cutoff"
  metric: W_exp
  before: "1/2 provisional; synchronous direct-square theorem proved, prior-art/class gate pending"
  after: "1/2 provisional; unchanged numerically; universal lower floor w>=1/2 now proved for every cutoff source-expander family"
  movement: "NO MOVEMENT"
  unchanged_count: 1
  status: PARTIAL
  methods: [5, 12, 27]
  exact_evidence:
    - "R16-I0112-C06: source expanders have t_cut=Theta(log |V|), and Chen--Saloff-Coste Theorem 3.4 forces b=Omega(sqrt(log |V|))"
    - "R16-I0112-C07: any two identical graph layers joined by one automorphism matching are graph-isomorphic to H square K2"
    - "one-parameter swap perturbation Q_eta is conjugate to an asynchronous product and only rescales the slow cutoff center"
  prior_art_status:
    Beck_Fiala: "KNOWN in current literature via Guo--Fang--Lu arXiv:2609.11189v1; not reopened"
    I0112: "OPEN in bounded current search; Altschuler arXiv:2609.14945 is long-range-expander partial progress"
    synchronous_direct_square_novelty: "NOT CLEARED; negative bounded search is not a novelty certificate"
  audits:
    P26: PENDING
    second_other_track: PENDING
    R12_directed_audit: PENDING_NOT_READY
  remaining_obligation: "general non-equilibrium concentration/local-Poincare principle from vertex transitivity + spectral expansion; or a genuinely non-gauge cross-coupled transitive expander family"
```

## 11. Primary references

1. Justin Salez, _Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon_, arXiv:2508.21055v1 (2025), Problem 2.3.
2. Guan-Yu Chen and Laurent Saloff-Coste, _Comparison of cutoffs between lazy walks and Markovian semigroups_, arXiv:1304.4587v1 (2013), Theorem 3.4.
3. Dylan J. Altschuler, _Long-range expanders: construction and cutoff_, arXiv:2609.14945 (14 Sep 2026).
4. Francesco Pedrotti and Justin Salez, _The local product condition implies cutoff_, arXiv:2607.05345 (2026).
5. Justin Salez, _The varentropy criterion is sharp on expanders_, arXiv:2307.10066.
6. Jonathan Hermon, Xiangying Huang, Francesco Pedrotti, Justin Salez, _Concentration of information on discrete groups_, arXiv:2409.16869.
7. Shengtao Guo, Ethan X. Fang, Junwei Lu, _Vector Balancing via Directional Total Variation_, arXiv:2609.11189v1 (10 Sep 2026).
8. Nikhil Bansal and Haotian Jiang, _Decoupling via Affine Spectral-Independence: Beck--Fiala and Komlos Bounds Beyond Banaszczyk_, arXiv:2508.03961.

**End status:** source OPEN/PARTIAL; metric numerically unchanged; square-root exponent certified as the universal floor; simplest automorphic cross-matching perturbation rejected as gauge-trivial. No shared root, peer file, email, Drive content, permission, workflow, public post, or scheduler state was modified.
