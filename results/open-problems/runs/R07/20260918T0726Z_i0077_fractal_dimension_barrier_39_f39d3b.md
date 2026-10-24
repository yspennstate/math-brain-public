Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `38 -> 39` genuinely distinct nonparabolic shape families; Section-B moves actually used: #1 CHANGE THE CATEGORY, #2 ATTACK THE NEGATION FIRST, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** Problem 7.9, on forward Lévy processes, is separate.

# R07 CLOSABLE OUTSIDE — run 39: a Hausdorff-dimension barrier and fractal log-periodic skeletons

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and fixed metric

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260918T0624Z_i0077_proliferating_braided_forests_38_b38e7c.md`,

which moved `37 -> 38` and used moves `#3,#13,#24`. The present triple is different. All thirty Section-B numbers have already appeared somewhere in the long I0077 chain, so I do not falsely claim three globally unused numbers; the new route itself is different.

Before research I reread/recovered current `master` state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/claims/I0077.md`;
- the newest own R07 report and the searchable R07/I0077 chain;
- the newest neighboring R15 report. R15 preserves Burdzy–Scheutzow Problem 7.2 / I0076 as a retired handoff and is on unrelated successor-admission work, so there is no I0077 ownership collision;
- targeted intake/source searches for I0077, arXiv:1302.6958, Problem 7.8 and later resolutions.

`INDEX.md`/`RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 closure. `operations/claims/I0077.md` still says `PENDING_ADMISSION, not READY`; I preserve that shared operational label while following the owner's explicit assignment of I0077 to R07. The old R07 KPZ/FPP route remains preserved in immutable pre-I0077 reports and handoff. No shared root or peer file is edited here.

Entering metric: **38**.  
Entering unchanged count: **0**.

## 2. Primary source recovered again

Definition 2.1 of the source says that an FBM `X=(X_t)_{t in R}` has random witness times `S_j -> -infinity` a.s. such that for each fixed deterministic witness index `j`,

\[
B^{(j)}(s)=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\]

is standard Brownian motion.

Theorem 4.3 gives the parabolic-strip phase theorem. In particular:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the source's universal far-past obstruction;
2. if `lambda_0(c_1,c_2)<=1`, a decomposable FBM exists with the corresponding asymptotic normalized confinement;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM is pointwise confined to the exact parabolic strip for every negative time.

Remark 4.1 records continuity and strict endpoint monotonicity of `lambda_0`, and Remark 4.2 records the critical pair `lambda_0(-1,1)=1`. Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 from parabolas to other space-time shapes. The following forward-Lévy sentence is Problem 7.9 and is not part of I0077.

## 3. Fresh current-status / prior-art pass

A bounded fresh search on 2026-09-18 covered:

- exact `"Problem 7.8" "Forward Brownian Motion"` and `"other space-time shapes"` searches;
- Burdzy/Scheutzow later-author and citing-paper searches;
- forward Brownian motion together with fractal graphs / Hausdorff dimension;
- the classical Hausdorff dimension of a one-dimensional Brownian graph;
- exact Hausdorff dimension of classical Weierstrass graphs.

The exact-source search again surfaced the original paper but no later paper in this bounded search explicitly resolving exact Problem 7.8 or stating the source-specific theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

The mechanism itself has important classical prior art and is not claimed as novel. Taylor proved that the graph of one-dimensional Brownian motion over a nondegenerate interval has Hausdorff dimension `3/2` a.s.; a modern reference is Dysthe–Lai, *Hausdorff and Fourier dimension of graph of continuous additive processes*, SPA 155 (2023), arXiv:2107.10321. For the explicit deterministic fractal used below, Weixiao Shen proved that the graph of the classical Weierstrass function

\[
W_{\lambda,b}(r)=\sum_{n\ge0}\lambda^n\cos(2\pi b^n r)
\]

has Hausdorff dimension

\[
2+\frac{\log\lambda}{\log b}
\]

for every integer `b>=2` and `lambda in (1/b,1)`; see Math. Z. 289 (2018), 223–266, arXiv:1505.03986.

## 4. Move #1 — CHANGE THE CATEGORY: from moving-boundary probability to geometric measure theory

Runs 35–38 controlled confinement through Gaussian increment costs, lag geometry and template entropy. I instead discard metric width and transition probabilities completely and ask a geometric question:

> what deterministic space-time sets are too small, in Hausdorff dimension, to contain even one complete Brownian witness segment?

The FBM definition itself gives a standard Brownian graph on every fixed witness. A one-dimensional Brownian graph has deterministic a.s. Hausdorff dimension `3/2`. This turns a probabilistic confinement problem into a dimension-monotonicity obstruction.

**Outcome #1: success.** It yields the general theorem T43 below.

## 5. Move #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE: the `3/2` threshold

The number `3/2` appears in a different literature: fractal geometry of Brownian graphs. It is exactly the threshold needed here because Hausdorff dimension is monotone under inclusion and invariant under translations.

This is qualitatively different from the preceding R07 invariants. A deterministic skeleton can have zero width, infinite variation at every scale, no conserved branch address, and no usable finite-lag diameter bound; if its Hausdorff dimension is `<3/2`, it is still impossible for an FBM tail.

**Outcome #17: success.** The imported invariant closes the new family without a Gaussian template union bound.

## 6. I0077-R07-T43 — universal sub-Brownian-dimension space-time obstruction

Let `S subset R^2` be deterministic. Assume

\[
\boxed{\dim_H S<\frac32.}\tag{6.1}
\]

### Theorem T43

For every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ (t,X_t)\in S\quad\forall t\le -R
\right)=0.
}\tag{T43}
\]

No regularity, connectedness, fiber-width, periodicity, Markov property of the backward path, or decomposability assumption is imposed on `S` or `X` beyond determinism of `S` and the FBM definition.

### Proof

Suppose the event in T43 has positive probability. By a countable union over integer radii, there is a deterministic integer `R>=1` such that

\[
E_R=\{(t,X_t)\in S\text{ for every }t\le-R\}
\]

has probability `p>0`.

Let `(S_j)` be FBM witness times from Definition 2.1. Since `S_j -> -infinity` a.s.,

\[
\mathbb P(S_j+1\le-R)\longrightarrow1
\]

along the witness sequence. Choose one **deterministic** witness index `j` so far left that

\[
\mathbb P(A_j)>1-p/2,
\qquad A_j:=\{S_j+1\le-R\}.
\tag{6.2}
\]

Then

\[
\mathbb P(E_R\cap A_j)\ge p/2>0.
\tag{6.3}
\]

For this fixed `j`, Definition 2.1 says

\[
B^{(j)}(s)=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\]

is standard Brownian motion. Therefore the classical Brownian graph theorem gives

\[
\dim_H\{(s,B^{(j)}(s)):0\le s\le1\}=\frac32
\quad\text{a.s.}
\tag{6.4}
\]

On `E_R cap A_j`, every `S_j+s` with `0<=s<=1` is at most `-R`, hence

\[
G_j:=\{(S_j+s,X_{S_j+s}):0\le s\le1\}\subset S.
\tag{6.5}
\]

But `G_j` is the image of the graph in (6.4) under the random translation

\[
(s,y)\mapsto(S_j+s,X_{S_j}+y),
\]

which is an isometry for every realized translation vector. Thus

\[
\dim_H G_j=\frac32
\quad\text{a.s.}
\tag{6.6}
\]

On the positive-probability event in (6.3), (6.5), monotonicity of Hausdorff dimension, and (6.1) would give

\[
\frac32=\dim_HG_j\le\dim_HS<\frac32,
\]

a contradiction. Hence `P(E_R)=0` for every deterministic `R`, and T43 follows. `QED`

### Dependence check

The proof does **not** condition on the random witness time `S_j` and does not assert independence between `S_j` and `B^(j)`. It uses only two unconditional probability-one facts for one fixed deterministic witness index: `B^(j)` has the standard Brownian law, and its graph has Hausdorff dimension `3/2`.

## 7. Move #2 — ATTACK THE NEGATION FIRST: a subcritical parabolic hull need not make a closed skeleton feasible

A tempting extrapolation of Theorem 4.3 is:

> if a deterministic closed space-time skeleton lies inside a subcritical parabolic strip, perhaps one can choose the source's decomposable construction so that the FBM stays on that skeleton.

The next explicit shape disproves this extrapolation. This is **not** a refutation of the source's open-ended Problem 7.8.

Fix

\[
b=2,\qquad \lambda=2^{-3/4},
\]

and define the period-one classical Weierstrass function

\[
W(r)=\sum_{n=0}^{\infty}\lambda^n\cos(2\pi 2^n r).
\tag{7.1}
\]

Shen's theorem gives

\[
\dim_H\operatorname{graph}(W|_{[0,1]})
=2+\frac{\log(2^{-3/4})}{\log2}
=\boxed{\frac54}.
\tag{7.2}
\]

Now define the physical space-time skeleton

\[
\mathcal S_W
=
\left\{
(-u,\sqrt u\,W(\log u)):u>0
\right\}\cup\{(0,0)\}.
\tag{7.3}
\]

The function `W` is bounded, so the seam at `u=0` closes continuously and `S_W` is closed. On each logarithmic slab `r in [k,k+1]`, the map

\[
F(r,y)=(-e^r,e^{r/2}y)
\tag{7.4}
\]

is a `C^1` bi-Lipschitz diffeomorphism on the compact strip containing the graph of `W`. Hence every slab of `S_W` has Hausdorff dimension `5/4`. Since `S_W` is a countable union of these slabs plus one point,

\[
\boxed{\dim_H\mathcal S_W=\frac54<\frac32.}
\tag{7.5}
\]

T43 therefore yields

\[
\boxed{
\mathbb P\left(
\exists R:\ X_{-u}=\sqrt u\,W(\log u)\ \forall u\ge R
\right)=0
}
\tag{T44}
\]

for every FBM.

Yet this impossible skeleton has a **feasible parabolic hull**. Indeed

\[
A:=\|W\|_\infty=W(0)=\sum_{n\ge0}\lambda^n=\frac1{1-2^{-3/4}}>1,
\]

so

\[
\mathcal S_W\subset\{(-u,x):|x|\le A\sqrt u\}.
\]

The source has `lambda_0(-1,1)=1`, and strict endpoint monotonicity gives

\[
\lambda_0(-A,A)<1.
\]

Theorem 4.3(iii) therefore supplies a decomposable FBM confined to the **ambient hull** `|X_{-u}|<=A sqrt(u)` for all `u>=0`, while T44 says no FBM can eventually follow the fractal skeleton itself.

**Outcome #2: success.** A parabolically feasible hull does not imply feasibility of an arbitrary closed subset of that hull.

## 8. Why this earns metric point 39

The counted family is

> **deterministic sub-Brownian-dimensional space-time skeletons**, with a canonical parabolic-scale log-periodic Weierstrass skeleton of exact Hausdorff dimension `5/4`.

This is not a parameter variation of the earlier zero-width web results:

- run 32 used `C^1` moving affine Cantor laminations and conserved a Cantor address;
- run 33 used finitely many locally Lipschitz sheets, so every selector was locally Lipschitz;
- run 34 used countably many BV sheets under a summable total-variation budget, forcing every selector to have finite variation;
- the present canonical skeleton has Hausdorff graph dimension `5/4>1`, hence is not Lipschitz or bounded-variation/rectifiable, and its obstruction is purely fractal-dimensional.

It is also distinct from run 6's log-periodic **positive-width** pulsed tubes: `S_W` has singleton fibers and fractal roughness at every logarithmic scale. Brownian rescaling, reflection and constant translation are bi-Lipschitz maps of the plane and preserve Hausdorff dimension, so they cannot turn this `5/4`-dimensional skeleton into any of the dimension-one smooth/BV web families.

Therefore the frozen metric moves

\[
\boxed{38\longrightarrow39}.
\]

`unchanged_count = 0`.

## 9. Validation / closure bookkeeping

There is no finite arithmetic core in T43/T44, so no checker or Lean artifact is warranted. The finite-core requirement is **N/A**, not silently skipped. The theorem-sized claim is proved on the page above.

Independent OTHER-track audits of T43/T44: **0/2**. Therefore the overall source status is **PARTIAL**, not closed, and no `paper_*` package is created. Publication novelty remains **UNVERIFIED**; the Brownian `3/2` theorem and Shen's Weierstrass dimension theorem are explicitly prior art, and the source-specific FBM deduction should be treated as an elementary new application unless a broader search finds it already recorded.

The strongest next route is the **critical dimension `3/2` boundary**. Hausdorff dimension alone stops deciding at equality. A genuinely new criterion could use `3/2`-Hausdorff measure, capacity, conformal dimension, or quantitative covering entropy to separate critical skeletons that can or cannot contain an FBM witness graph.

## 10. Model / scheduler control status

The exposed scheduler control surface still has title/prompt, schedule/start-offset, enablement and timing mode, but no model-family selector, reasoning-effort selector or authenticated completed-run model telemetry. GPT-6 maximum is therefore prompt-only here; the actual report metadata remains GPT-5.6 Sol / UNVERIFIED.

The repository's current `RESULTS.md` records that P26's historical `You cannot modify this task` denial was authorization-context-specific and that its full update later succeeded from an authorized context. The legitimate workaround for any still-denied task is the owning/authorized account/workspace context or platform support, not a permission bypass or duplicate task. This run is expressly barred from scheduler changes and attempted none.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  allocation: CLOSABLE_OUTSIDE
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8 / I0077"
  source_status: PARTIAL
  fixed_metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem under frozen equivalence"
  metric_before: 38
  metric_after: 39
  movement: +1
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods: [1, 2, 17]
  new_claims:
    - I0077-R07-T43
    - I0077-R07-T44
  new_family: sub_brownian_dimension_fractal_space_time_skeletons
  canonical_example: "x = sqrt(u) W(log u), W classical Weierstrass with b=2, lambda=2^(-3/4), dim_H=5/4"
  finite_core: none
  finite_core_status: N/A_ANALYTIC_GEOMETRIC_THEOREM
  other_track_audits: "0/2"
  publication_novelty: UNVERIFIED
  next_frontier: "critical Hausdorff dimension 3/2: measure/capacity/entropy criterion"
```
