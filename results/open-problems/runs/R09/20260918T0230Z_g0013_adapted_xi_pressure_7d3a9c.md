Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — NO MOVEMENT on active R09 successor G0013: `U_* = 1289727882057511/11918000000000000 = 0.10821680500566462... -> same`; supported G0013 unchanged count `2 -> 3`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported retirement count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Methods used: B9 RANDOMIZE, B19 MAKE IT AN ALGORITHM, B28 REPLACE FOR ALL WITH FOR TYPICAL.** GPT-6 / maximum was requested in prompt text, but this runtime identifies as GPT-5.6 Sol and exposes no authenticated reasoning-effort telemetry, so I do not claim GPT-6 or maximum reasoning.

# R09 CLOSABLE OUTSIDE — G0013: adapted-transport / Chatterjee pressure and the two-sided near-functionality regime forced on every counterexample

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only.

## 1. Continuity, ownership, and what is not being reopened

I did **not** reopen Pengfei Tang, Question 4.11. The periodic-tree clause is already source-level REFUTED in the later R09 record, with exact verification, two outside audit passes, a paper package, and the owner's six-unchanged CLOSABLE retirement threshold reached. The transitive-graph clause remains open, but the Tang track is frozen for this slot at `UNBOUNDED_ABOVE`. The old critical-percolation one-arm route also remains retired. G0002 / Cerf 53.1 remains handed off at `Delta_8=UNMEASURED`.

The controlling exclusive R09 claim is still

`operations/claims/G0013.md`,

namely Catalano--Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034, Remark 3. Put
\[
\lambda=\operatorname{Unif}[0,1],\qquad \nu=\lambda\otimes\lambda,
\]
and
\[
M=\sup_{\pi\in\Pi(\lambda,\lambda)}W_2^2(\pi,\nu).
\]
The source conjecture is
\[
M=\frac1{10},
\]
with the diagonal and antidiagonal couplings as maximizers.

The frozen R09 quantity is

`U_* = smallest rigorous source-valid global upper bound on M established by R09`.

The newest complete own report before this run is

`runs/R09/20260918T0130Z_g0013_saddle_rankone_pressure_a91d3e.md`,

which leaves
\[
\boxed{
U_*=\frac{1289727882057511}{11918000000000000}
=0.10821680500566462\ldots .
}
\tag{1.1}
\]
This run does not lower (1.1). The supported unchanged count therefore becomes `3`, which means the **next** R09 run must follow the owner's Section-I thinking-only stuck protocol rather than append another nearby lemma.

Before new work I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the G0013 claim, the newest complete R09 report, the newest searchable neighboring R08/R10 state, and exact G0013 / Catalano--Lavenant / Schrott / intake searches. The connector does not render the roughly 780 JSONL intake rows as one complete bounded response, so I used exact target/source/ownership searches rather than pretending to have visually inspected every row. No conflicting G0013 owner surfaced.

## 2. Current-source and later-literature check — 18 September 2026

The primary PDF of Catalano--Lavenant still says in Remark 3 that, for two uniform marginals on `[0,1]` and quadratic Euclidean Wasserstein distance on the square, the supremum over copulas has not been solved; it conjectures the two diagonals and says a proof is lacking.

The later primary source remains Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467v1, submitted 9 September 2026. Its abstract/restatement still treats the Catalano--Lavenant uniform statement as a conjecture and proves the Gaussian analogue instead. Fresh bounded searches on 18 September 2026 for the exact title, authors, `uniform copula`, `farthest from independence`, `quadratic Wasserstein`, `1/10`, and citing/follow-up papers did not surface a later source claiming the exact uniform problem is resolved. This remains bounded dated status evidence, not a worldwide novelty guarantee.

For the method below I also checked Johannes Wiesel, *Measuring association with Wasserstein distances*, Bernoulli 28(4) (2022), arXiv:2102.00356. Wiesel defines directed conditional Wasserstein correlations, records `W <= AW`, extends the construction to `p>1`, and in Lemma 3.3 rewrites the Dette--Siburg--Stoimenov / Chatterjee coefficient through conditional CDFs. Catalano--Lavenant themselves review the same conditional-Wasserstein construction and adapted Wasserstein distance. Therefore the bridge used below is best viewed as a **direct specialization / recombination of existing machinery**, not a publication-novelty claim.

## 3. B19 — make it an algorithm: an exact conditional transport from a copula to independence

Let `(U,V)~pi`, with both marginals uniform on `[0,1]`. Let `pi_u` be a regular conditional law of `V` given `U=u`, and write `F_u` for its cdf.

The key one-dimensional identity is the following.

### Lemma 3.1 — uniform-reference CDF/quantile identity

For every probability law `mu` on `[0,1]`, with cdf `F` and generalized inverse `Q`,
\[
\boxed{
W_2^2(\mu,\lambda)
=\int_0^1(Q(s)-s)^2\,ds
=\int_0^1(F(t)-t)^2\,dt.
}
\tag{3.1}
\]

#### Proof

The first equality is the standard one-dimensional monotone-coupling formula. For the second, let `Z,Z'` be i.i.d. with law `mu`. Expanding the CDF integral gives
\[
\int_0^1(F(t)-t)^2dt
=\int F(t)^2dt-2\int tF(t)dt+\frac13.
\]
Now
\[
\int_0^1F(t)^2dt
=\mathbb E[1-\max(Z,Z')],
\]
while
\[
2\int_0^1tF(t)dt
=1-\mathbb E Z^2.
\]
Hence
\[
\int_0^1(F(t)-t)^2dt
=\mathbb EZ^2-\mathbb E\max(Z,Z')+\frac13.
\tag{3.2}
\]
If `A,A'` are i.i.d. uniform and `Z=Q(A)`, `Z'=Q(A')`, then
\[
\mathbb E\max(Z,Z')
=\int_0^1 2sQ(s)\,ds.
\]
Substituting into (3.2) yields
\[
\int_0^1(F(t)-t)^2dt
=\int_0^1(Q(s)-s)^2ds.
\]
This proves (3.1), including atomic laws.

### Proposition 3.2 — adapted/Chatterjee upper bound for the source functional

Let
\[
S(\pi)=W_2^2(\pi,\lambda^{\otimes2}).
\]
Then
\[
\boxed{
S(\pi)\le\frac{\xi(U,V)}6,
\qquad
S(\pi)\le\frac{\xi(V,U)}6,
}
\tag{3.3}
\]
and therefore
\[
\boxed{
S(\pi)\le \frac16\min\{\xi(U,V),\xi(V,U)\}.
}
\tag{3.4}
\]
Here `xi(U,V)` denotes the population Chatterjee/Dette--Siburg--Stoimenov directed coefficient, with `U` the conditioning variable and `V` the response.

#### Proof

For every `u`, take an optimal monotone coupling between `pi_u` and `lambda`. Integrate these conditional couplings against `du`, while coupling the first coordinate identically. The resulting global coupling has one marginal `pi` and the other marginal `lambda tensor lambda`, because conditionally on `U=u` the new second coordinate is uniform. Therefore
\[
S(\pi)
\le \int_0^1W_2^2(\pi_u,\lambda)\,du.
\tag{3.5}
\]
By Lemma 3.1,
\[
\int_0^1W_2^2(\pi_u,\lambda)du
=\int_0^1\int_0^1(F_u(t)-t)^2dt\,du.
\tag{3.6}
\]
Since the unconditional law of `V` is uniform,
\[
\int_0^1F_u(t)du=t.
\]
Thus the right side of (3.6) is
\[
\int_0^1\operatorname{Var}_u(F_u(t))dt.
\]
For a uniform response, the normalizing denominator in Chatterjee's population coefficient is
\[
\int_0^1 t(1-t)dt=\frac16,
\]
so (3.6) equals `xi(U,V)/6`. This proves the first inequality. Exchange the coordinates for the second.

Equivalently, (3.5) is the explicit algorithm behind the standard inequality `W_2 <= AW_2`: for the product target the first-coordinate coupling can be the identity, and the nested second-stage cost is exactly the average conditional `W_2^2`. In Wiesel's notation, for uniform response the square of the directed `p=2` Wasserstein correlation specializes to Chatterjee's `xi`. I **do not** claim this mechanism itself as new prior art.

## 4. B28 — replace `for all` by `for typical`: every counterexample is forced into a two-sided near-functionality regime

Proposition 3.2 gives a clean necessary condition that is independent of the Brenier/Jacobi route.

If
\[
S(\pi)>\frac1{10},
\]
then necessarily
\[
\boxed{
\xi(U,V)>\frac35,
\qquad
\xi(V,U)>\frac35.
}
\tag{4.1}
\]
More generally, `S(pi)>=s` forces both directed coefficients to be at least `6s`.

This can be turned into a concrete typical-set statement. Let `V,V^*` be conditionally i.i.d. given `U`, and define
\[
g_U(u)=\mathbb E\bigl[|V-V^*|\mid U=u\bigr].
\]
For uniform `V`, the standard conditional-CDF calculation gives the exact identity
\[
\boxed{
\mathbb E g_U(U)=\frac{1-\xi(U,V)}3.
}
\tag{4.2}
\]
Indeed, conditionally on `U=u`,
\[
\mathbb E[|V-V^*|\mid U=u]
=2\int_0^1F_u(t)(1-F_u(t))dt,
\]
and averaging and using the definition of `xi` gives (4.2).

Combining (3.3) and (4.2), every copula obeys the source-linked pressure
\[
\boxed{
\mathbb E g_U(U)\le \frac13-2S(\pi),
\qquad
\mathbb E g_V(V)\le \frac13-2S(\pi),
}
\tag{4.3}
\]
where `g_V` is defined symmetrically from conditionally i.i.d. copies of `U` given `V`.

Hence a source counterexample `S>1/10` would satisfy both
\[
\mathbb E g_U(U)<\frac{2}{15},
\qquad
\mathbb E g_V(V)<\frac{2}{15}.
\tag{4.4}
\]
For every threshold `tau>0`, Markov's inequality then yields
\[
\boxed{
\lambda\{u:g_U(u)>\tau\}
\le\frac{1-6S}{3\tau},
}
\tag{4.5}
\]
and the symmetric estimate in the other direction. Thus high source distance forces **most conditioning fibers**, quantitatively, to have small conditional Gini width.

There is also an `L^2` near-graph consequence. Put
\[
m(u)=\mathbb E[V\mid U=u].
\]
Since `|x-y|^2<=|x-y|` on `[0,1]`,
\[
\mathbb E\operatorname{Var}(V\mid U)
=\frac12\mathbb E(V-V^*)^2
\le\frac12\mathbb E|V-V^*|
=\frac{1-\xi(U,V)}6
\le\frac16-S.
\]
Therefore
\[
\boxed{
\mathbb E|V-m(U)|^2\le\frac16-S,
}
\tag{4.6}
\]
and symmetrically there exists `n(v)=E[U|V=v]` with
\[
\boxed{
\mathbb E|U-n(V)|^2\le\frac16-S.
}
\tag{4.7}
\]
A counterexample `S>1/10` is consequently simultaneously within squared `L^2` error `<1/15` of a graph in **both directions**.

This does not solve the conjecture: arbitrary measure-preserving graph copulas can have both directed `xi` equal to one. But it removes the possibility that a counterexample is a diffuse two-dimensional copula with weak conditional structure. Combined with the previous run's rank-one pressure theorem (`S>1/10` forces a weighted Hessian rank-one ratio `K>6/7`), a counterexample is now forced into two independent rigidity regimes at once:

1. the **target copula** is near functional in both directions in the quantitative sense (4.3)--(4.7);
2. the **source-to-target Brenier map** is near rank one in at least one weighted Hessian geometry.

The missing step is to make these two notions of near-one-dimensionality interact.

## 5. B9 — attack the negation with randomized near-rank-one sign cells: why the naive construction fails

I next tried to use the rank-one pressure theorem in the opposite direction: construct a putative counterexample by prescribing many regions on which
\[
\kappa=\frac{b^2}{ac}\approx1
\]
and randomizing the sign of `b=phi_xy` so that neither global diagonal orientation dominates.

Two obstructions appear before one gets a valid candidate.

### 5.1 Law-level randomization cannot beat the diagonal value

The functional
\[
\mu\mapsto W_2^2(\mu,\nu)
\]
is convex in its first argument. Therefore a literal mixture of the diagonal and antidiagonal copulas, or any convex mixture of already-certified `<=1/10` candidates, remains `<=1/10`. Randomizing the orientation **at the law level** cannot produce a counterexample.

### 5.2 Local Hessian signs are not independent degrees of freedom

Randomizing `b` locally is also not free. A smooth candidate Hessian
\[
D^2\phi=\begin{pmatrix}a&b\\b&c\end{pmatrix}\succeq0
\]
must satisfy the integrability/Codazzi identities
\[
\partial_y a=\partial_x b,
\qquad
\partial_y b=\partial_x c.
\tag{5.1}
\]
A formal patchwork of rank-one matrices with independently chosen signs of `b` will generally violate (5.1), even before enforcing the two output marginals. In the saddle coordinates of the previous report this is the statement that the two slope fields must come from one potential `Psi`, not merely satisfy the pointwise product bound.

This B9 route therefore produced **no valid counterexample** and no improvement of `U_*`. Its useful outcome is diagnostic: a serious negation attack must randomize an actual convex/saddle potential or a measure-preserving graph, not the Hessian entries independently.

I deliberately did not turn the exploratory failed sign-cell search into another checker artifact. There is no finite source-level claim here to certify.

## 6. What moved mathematically, and what did not

The source-valid global metric did not move:
\[
\boxed{
\frac1{10}\le M\le
\frac{1289727882057511}{11918000000000000}
=0.10821680500566462\ldots .
}
\tag{6.1}
\]
Status remains **PARTIAL / OPEN_CURRENT**.

What did move structurally is the description of every possible counterexample. The previous report forced near-rank-one Brenier geometry. This run independently forces high **bidirectional Chatterjee dependence** and hence two-sided near-functionality of the target copula. The next proof attempt should not optimize the scalar Jacobi envelope again; it should prove a rigidity theorem saying, roughly, that a copula which is simultaneously near a two-sided graph and generated from the square by an almost-rank-one Brenier/saddle map cannot exceed the diagonal cost.

Because this is the third supported unchanged G0013 run, the owner policy now triggers. **The next R09 invocation must be a Section-I stuck thinking run with no new theorem claims.** It must write the five requested items: exact blocking statement; all routes tried and why they fail; missing ingredient; simplest still-unproved special case; nearest solved literature analogue and the technique it has that G0013 lacks. It must then choose exactly one recovery action before resuming research.

## 7. Prior-art ownership of the B19 mechanism

The following part is deliberately conservative.

- Wiesel (2022) already defines directed Wasserstein correlation through conditional laws, proves/uses the adapted-Wasserstein hierarchy, extends the construction to `p>1`, and compares it to Chatterjee's coefficient.
- Catalano--Lavenant review both the joint product-distance `D_tensor` and conditional-distance `D_|bullet` constructions, as well as adapted Wasserstein distance.
- Wiesel's Lemma 3.3 gives the conditional-CDF formula for the Chatterjee/Dette--Siburg--Stoimenov coefficient.

Accordingly, I record (3.3) as a **source-specific bridge imported from known conditional/adapted transport machinery**, with a complete proof here for use by the fleet. I do not claim that the inequality or the identity between the uniform-response `p=2` conditional Wasserstein numerator and `xi/6` is new in the literature.

## 8. Model / scheduler-control check

This runtime still does **not** expose a model-family selector, reasoning-effort selector, or authenticated completed-run model telemetry through the scheduler action schema. The available task controls are title, prompt, schedule / relative start offset, timing mode, enabled state, and the task identifier for updates. Therefore GPT-6 / maximum remains request text only here and cannot honestly be asserted.

The root ledger records that the historical P26 `You cannot modify this task` response was authorization-context dependent: the full P26 prompt update later succeeded in a different authorized context, while another context rejected edits. The legitimate remedies for a denied task remain the owning authorized context, an ownership/admin transfer, or platform support. I did not attempt a scheduler modification, permission change, duplicate task, or bypass in this run.

## 9. Artifact decision

No new exact-arithmetic artifact was created. The substantive new result is analytic and proved on the page; the failed randomized sign-cell route produced no finite theorem-sized claim worth certifying. This is intentional under the owner's 90/10 rule and the instruction not to manufacture checker-only commits for an unchanged metric.

## 10. Structured `ledger_delta`

```yaml
ledger_delta:
  track: R09
  lane: CLOSABLE_OUTSIDE
  active_claim: G0013
  source: "Catalano--Lavenant, Measures of Dependence based on Wasserstein distances, arXiv:2510.06034, Remark 3"
  source_status_before: "PARTIAL / OPEN_CURRENT"
  source_status_after: "PARTIAL / OPEN_CURRENT"
  metric_name: "U_* = smallest rigorous source-valid global upper bound on M"
  metric_before: "1289727882057511/11918000000000000"
  metric_after: "1289727882057511/11918000000000000"
  movement: "NO MOVEMENT"
  supported_unchanged_count_before: 2
  supported_unchanged_count_after: 3
  stuck_trigger: true
  next_run_required_mode: "Section-I thinking-only stuck report; no new theorem claims"
  methods_used:
    - "B9 RANDOMIZE"
    - "B19 MAKE IT AN ALGORITHM"
    - "B28 REPLACE FOR ALL WITH FOR TYPICAL"
  substantive_new_results:
    - "Explicit conditional/adapted transport proof: S(pi) <= min{xi(U,V),xi(V,U)}/6."
    - "Any source counterexample S>1/10 must have both directed Chatterjee coefficients >3/5."
    - "Exact conditional-Gini pressure E|V-V*|=(1-xi(U,V))/3 and symmetric reverse bound."
    - "Two-sided L2 near-graph pressure E|V-E[V|U]|^2, E|U-E[U|V]|^2 <= 1/6-S."
    - "Naive random near-rank-one Hessian sign cells fail the integrability/Codazzi requirement before marginal constraints."
  novelty_status: "The conditional/adapted transport mechanism is prior-art-adjacent / likely folklore from Wiesel 2022 and related work; no novelty claim."
  tang_state: "RETIRED/FROZEN; periodic-tree clause source-level refuted; transitive clause open; metric UNBOUNDED_ABOVE; retirement count 6"
  g0002_state: "HANDED_OFF; Delta_8=UNMEASURED"
  checker_created: false
  scheduler_modified: false
  shared_roots_modified: false
  peer_files_modified: false
```
