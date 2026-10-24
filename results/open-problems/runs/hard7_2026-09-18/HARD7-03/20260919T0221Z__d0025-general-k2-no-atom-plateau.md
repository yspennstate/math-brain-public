Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-03 metric moves `L <= Delta_2(Q): 1/16 -> 500000/6578563`; methods B5 / B21 / B29.**

# HARD7-03 — general iid `K=2` plateau without a minimum-rate atom, plus a sharper binary width

Date: 2026-09-19 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL.** The exact source Problem 4 remains open in its full arbitrary-`K` scope. This run proves, on the page and as a self-check pending independent audit/prior-art review, a substantially broader `K=2` theorem: the minimum-rate atom used in the preceding checkpoint is not needed. For every nondegenerate iid site-rate law covered by the source with positive essential infimum, the `K=2` flux has a nontrivial flat segment around density `1`. For the frozen binary law the stable tracked lower bound improves strictly from `1/16` to the exact rational `500000/6578563 = 0.07600444048...`.

Canonical target: `D0025`, Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), Problem 4, Section 4. Active claim: `operations/claims/D0025.md`, owner `HARD7-03`.

The source asks, for the disordered TASEP / `K`-exclusion model, whether there is a phase transition analogous to disordered zero-range and whether the flux `f_K(rho)` has a flat segment around `rho=K/2`. The already-known `K=1` plateau is excluded from new credit. The frozen metric remains

\[
\Delta_2(Q)=\sup\{\delta\ge0: f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\},
\qquad L\le\Delta_2(Q),
\]

for

\[
Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1.
\]

## 1. Continuity, repository state, and current-status refresh

I resumed the newest HARD7-03 checkpoint, not the admission state. Before doing the new mathematics I re-read or recovered:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/D0025.md`;
- the D-intake/source records keyed by `disordered_asep_open_1999::problem_4`;
- all preceding HARD7-03 checkpoints, especially `runs/hard7_2026-09-18/HARD7-03/20260919T0136Z__d0025-recovery2-sly-cusp-plateau.md`;
- the newest visible neighboring HARD7-02 and HARD7-04 checkpoints.

Repository search still shows D0025 as exclusively owned by HARD7-03. No release, posted equivalent, or conflicting current owner was found.

A bounded literature refresh dated 2026-09-19 checked the primary source and the main obvious aliases. Sources/search scope included:

- Seppäläinen 1999 source page/DOI: `https://doi.org/10.11606/resimeusp.v4i1.74889`, and arXiv `math/9906194`;
- Allan Sly, *Note on the flux for TASEP with general disorder*, `https://arxiv.org/abs/1609.06589`, which proves the iid-disorder plateau for ordinary `K=1` TASEP;
- Bahadoran--Bodineau, *Quantitative estimates for the flux of TASEP with dilute site disorder*, again `K=1`;
- Floreani--Redig--Sau, *Hydrodynamics for the partial exclusion process in random environment*, `arXiv:1911.12564`, whose random environment changes maximal occupancies rather than the source's asymmetric site jump rates;
- Gonçalves--Hayashi--Sasada, *Characterization of Gradient Condition for Asymmetric Partial Exclusion Processes and Their Scaling Limits*, `arXiv:2405.15142`, a different partial-exclusion setting without this quenched site-rate problem;
- Ayyer--Misra's 2024 exactly-solvable deformed-rate `K`-exclusion model, which is not Seppäläinen's process;
- queries `disordered K-exclusion plateau`, `site disorder K-exclusion flux`, `general K TASEP site disorder plateau`, and `asymmetric partial exclusion random environment flux`.

No theorem closing this exact `K>=2` source residual was found in that bounded search. This is **negative evidence only**, not a claim of exhaustive worldwide novelty. The theorem below is therefore labelled a self-checked candidate result, not publication-certified novelty.

## 2. Before/after metric

Previous certified self-check:

\[
L_{\rm before}=\frac1{16}=0.0625.
\]

This run proves the stronger exact rational lower bound

\[
\boxed{
L_{\rm after}=\frac{500000}{6578563}=0.0760044404834308\ldots
}
\]

and the exact checker verifies

\[
\frac{500000}{6578563}-\frac1{16}
=\frac{1421437}{105257008}>0.
\]

Thus this run has real movement on the fixed source-relevant metric. The stronger implicit bound obtained below is approximately `0.07600444246`, but the ledger metric is kept at the exact rational certificate above.

## 3. Setup inherited from the exact `K=2` growth representation

Under the `K=2` source change of coordinates

\[
t=i+j-1,\qquad y=j,
\]

the three admissible source increments become lazy nearest-neighbor increments

\[
\Delta y\in\{-1,0,1\}.
\]

Let the iid row rates be `(alpha_y)`, with law `Q` supported in `[r,1]`, where

\[
r=\operatorname*{ess\,inf}Q>0.
\]

Let `(xi_{t,y})` be iid unit exponentials independent of the row environment and set

\[
W_{t,y}=\frac{\xi_{t,y}}{\alpha_y}.
\]

For a lazy path from row `0` to row `m` in `n` time steps, write

\[
T_Q(n,m)=\max_\pi\sum_{t=1}^n W_{t,\pi_t},
\]

and let

\[
G_Q(v)=\lim_{n\to\infty}\frac1nT_Q(n,\lfloor vn\rfloor),\qquad |v|\le1,
\]

be the deterministic point-to-point shape. `G_r` denotes the homogeneous shape when every row rate equals `r`.

The previous checkpoint proved the plateau for one binary law by combining a central saturation identity, a coupling cusp, and the source convex duality. Its apparent limitation was that central saturation had been proved by finding all-`r` strips, which required an atom at `r`. B29 attacks exactly that boundary.

## 4. B29 — the minimum-rate atom is not needed

### Theorem 4.1 (central saturation for every iid law with positive essential infimum)

For every iid site-rate law `Q` on `[r,1]` with `r>0` its essential infimum,

\[
\boxed{G_Q(0)=G_r(0).}
\]

No assumption `Q({r})>0` is needed.

### Proof

The upper bound is pointwise. Since `alpha_y>=r`,

\[
W_{t,y}=\frac{\xi_{t,y}}{\alpha_y}\le\frac{\xi_{t,y}}r,
\]

so under the common-`xi` coupling

\[
T_Q(n,0)\le T_r(n,0),
\qquad G_Q(0)\le G_r(0).
\tag{4.1}
\]

For the reverse inequality, fix `epsilon>0`. Because `r` is the essential infimum,

\[
q_\epsilon:=Q([r,r+\epsilon])>0.
\tag{4.2}
\]

Fix a strip half-width `M`. Partition the row line into disjoint blocks of length `2M+1`. A block satisfies

\[
\alpha_y\le r+\epsilon\quad\text{for every row in the block}
\]

with probability `q_epsilon^(2M+1)>0`. These events are independent across the disjoint blocks, so almost surely infinitely many such blocks occur. Choose one and call its center `a_{M,epsilon}`. For fixed `M,epsilon`, this center is almost surely finite.

Inside this block, with the same exponentials,

\[
W_{t,y}=\frac{\xi_{t,y}}{\alpha_y}
\ge\frac{\xi_{t,y}}{r+\epsilon}.
\tag{4.3}
\]

Let `lambda_{M,r+epsilon}` be the homogeneous rate-`r+epsilon` zero-velocity shape constrained to a strip of half-width `M`. For `n>2|a_{M,epsilon}|`, use a path that travels from row zero to `a_{M,epsilon}`, spends the remaining `n-2|a_{M,epsilon}|` steps in that near-slow strip following an optimal constrained homogeneous comparison path, then returns. Passage weights are nonnegative, so the two travel pieces can be discarded from the lower bound. Time stationarity gives

\[
\liminf_{n\to\infty}\frac{T_Q(n,0)}n
\ge \lambda_{M,r+\epsilon}
\quad\text{a.s.}
\tag{4.4}
\]

As established in the preceding central-saturation checkpoint for homogeneous lazy LPP,

\[
\lambda_{M,r+\epsilon}\uparrow G_{r+\epsilon}(0)
\quad(M\to\infty).
\tag{4.5}
\]

Hence

\[
G_Q(0)\ge G_{r+\epsilon}(0).
\tag{4.6}
\]

Take a countable sequence `epsilon_j downarrow 0`, intersect the corresponding probability-one events, and use homogeneous exponential scaling:

\[
G_{r+\epsilon_j}(0)=\frac{G_1(0)}{r+\epsilon_j}
\longrightarrow \frac{G_1(0)}r=G_r(0).
\tag{4.7}
\]

Thus `G_Q(0)>=G_r(0)`. Together with (4.1), this proves the theorem. `□`

This removes the minimum-atom restriction from the mechanism. The earlier all-slow-strip proof was sufficient but not necessary; near-slow strips approximate the same central shape arbitrarily well.

## 5. B5 — vary the disorder law: a general `K=2` cusp

Define

\[
\mu_Q:=\mathbb E\left[\frac1r-\frac1\alpha\right].
\tag{5.1}
\]

If the disorder is nondegenerate, i.e. `Q(alpha>r)>0`, then `mu_Q>0`.

### Lemma 5.1 (minimum-rate coupling)

Conditional on a row rate `a>=r`, let

\[
W\sim\operatorname{Exp}(a),\qquad
U=B E,
\]

where

\[
B\sim\operatorname{Ber}(1-r/a),
\qquad E\sim\operatorname{Exp}(r),
\]

and `B,E,W` are independent. Then

\[
Z:=W+U\sim\operatorname{Exp}(r),
\qquad
\mathbb E[U\mid a]=\frac1r-\frac1a.
\tag{5.2}
\]

Indeed, for `s>=0`,

\[
\mathbb E e^{-sZ}
=\frac a{a+s}
\left(\frac ra+\left(1-\frac ra\right)\frac r{r+s}\right)
=\frac r{r+s}.
\]

Use this coupling independently at every space-time coordinate conditional on the row environment. Because the conditional joint law of the entire `Z` field is a product of `Exp(r)` laws and does not depend on the environment, the unconditional `Z` field is iid homogeneous rate `r`.

Let

\[
\mathcal F=\sigma((\alpha_y)_y,(W_{t,y})_{t,y}).
\]

Choose a maximizing disordered path `pi*` by a deterministic tie rule, so `pi*` is `F`-measurable. Suppose `m>0`, and let `tau_y` be its first hitting time of row `y`, `1<=y<=m`. The selected coordinates `(tau_y,y)` are distinct and `F`-measurable. Evaluating the homogeneous field on this same path gives

\[
T_r(n,m)
\ge T_Q(n,m)+\sum_{y=1}^m U_{\tau_y,y}.
\tag{5.3}
\]

The adaptive times cause no independence problem: conditional on `F`, the selected `U` variables are independent, and their laws depend only on the corresponding row rates.

### Lemma 5.2 (uniform lower-tail control for adaptively selected bonuses)

Put

\[
d_y=\frac1r-\frac1{\alpha_y}.
\]

For every `eta>0` and every collection of distinct `F`-measurable coordinates, one from each of `m` distinct rows,

\[
\mathbb P\left\{
\sum_{y=1}^m(U_y-d_y)\le-\eta m
\,\middle|\,\mathcal F
\right\}
\le \exp\left(-\frac{\eta^2r^2}{4}m\right).
\tag{5.4}
\]

### Proof

For a row with rate `a`, set `p=1-r/a`. For `theta>0`,

\[
\mathbb E[e^{-\theta U}\mid a]
=1-\frac{p\theta}{r+\theta}.
\]

Since `d=p/r`, writing `x=theta/r` and using `log(1-z)<=-z`,

\[
\begin{aligned}
\log\mathbb E[e^{-\theta(U-d)}\mid a]
&=px+\log\left(1-\frac{px}{1+x}\right)\\
&\le px-\frac{px}{1+x}
=\frac{px^2}{1+x}
\le x^2.
\end{aligned}
\tag{5.5}
\]

Conditional independence and Chernoff therefore give

\[
\mathbb P\left\{\sum(U_y-d_y)\le-\eta m\mid\mathcal F\right\}
\le \exp\left(-\theta\eta m+\frac{\theta^2}{r^2}m\right).
\]

Choosing `theta=eta r^2/2` proves (5.4). `□`

Now fix rational `v>0` and `m_n=floor(vn)`. By the spatial strong law,

\[
\frac1{m_n}\sum_{y=1}^{m_n}d_y\longrightarrow\mu_Q
\quad\text{a.s.}
\tag{5.6}
\]

The bound (5.4) is exponentially summable in `m_n`, so conditional Borel--Cantelli implies

\[
\liminf_{n\to\infty}\frac1n
\sum_{y=1}^{m_n}U_{\tau_y,y}
\ge v\mu_Q
\quad\text{a.s.}
\tag{5.7}
\]

Taking shape limits in (5.3), and repeating to the left for `v<0`, yields for rational `v`; continuity of the deterministic concave shapes extends it to all `|v|<=1`:

\[
\boxed{
G_r(v)\ge G_Q(v)+\mu_Q|v|.
}
\tag{5.8}
\]

The homogeneous shape is even and concave, hence `G_r(v)<=G_r(0)`. By Theorem 4.1,

\[
G_r(0)=G_Q(0).
\]

Therefore

\[
\boxed{
G_Q(0)-G_Q(v)\ge\mu_Q|v|.
}
\tag{5.9}
\]

This is a genuine linear cusp whenever the disorder is nondegenerate.

## 6. Convert the cusp to a source flux plateau

Let `gamma_Q(x,y)` be the source two-coordinate passage shape and `g_Q` the source level-one convex boundary. The exact `K=2` coordinate relation used and checked in the previous checkpoint is

\[
\gamma_Q(x,y)
=(x+y)G_Q\!\left(\frac{y}{x+y}\right).
\tag{6.1}
\]

Parameterize the level-one boundary by `v`:

\[
s(v)=\frac{v}{G_Q(v)},
\qquad
g_Q(s(v))=\frac{1-v}{G_Q(v)},
\qquad g_Q(0)=\frac1{G_Q(0)}.
\tag{6.2}
\]

Direct algebra gives the exact secant identity

\[
\frac{g_Q(s(v))-g_Q(0)}{s(v)}
=
\frac{G_Q(0)-G_Q(v)}{G_Q(0)v}-1.
\tag{6.3}
\]

Using (5.9) on the two sides of zero and convexity,

\[
\boxed{
\left[
-1-\frac{\mu_Q}{G_Q(0)},
-1+\frac{\mu_Q}{G_Q(0)}
\right]
\subseteq\partial g_Q(0).
}
\tag{6.4}
\]

The source hydrodynamic duality is

\[
f_{2,Q}(\rho)=\inf_x\{\rho x+g_Q(x)\}.
\tag{6.5}
\]

Whenever `-rho in partial g_Q(0)`, the minimizer in (6.5) includes `x=0`, and hence `f_{2,Q}(rho)=g_Q(0)`. Therefore:

### Theorem 6.1 (self-checked general iid `K=2` plateau candidate)

Let the source `K=2` site rates be iid with nondegenerate law `Q` supported in `[r,1]`, where `r>0` is the essential infimum. Then

\[
\boxed{
f_{2,Q}(\rho)=f_{2,Q}(1)
\quad\text{for every}\quad
|\rho-1|\le \delta_Q,
}
\tag{6.6}
\]

where

\[
\boxed{
\delta_Q:=\frac{\mu_Q}{G_Q(0)}
=\frac{1-r\,\mathbb E(1/\alpha)}{G_1(0)}>0.
}
\tag{6.7}
\]

The second equality follows from Theorem 4.1 and homogeneous scaling `G_Q(0)=G_r(0)=G_1(0)/r`.

This theorem answers the flat-segment clause of Seppäläinen Problem 4 for the full iid `K=2` site-disorder class under the source's positive lower-endpoint assumption, if all inherited source-coordinate/duality identifications survive independent audit. It **does not** answer the source for arbitrary `K>=3`, particle disorder, or any broader formulation. Therefore the correct fleet status remains PARTIAL.

## 7. B21 — compare the mechanism against adjacent literatures

The repaired route has two ingredients: rare near-minimum spatial strips fix the zero-tilt value, while an independent minimum-rate coupling gives an unavoidable mean bonus on every net row crossing. I explicitly compared this shape against the closest literature found in the bounded search:

1. Sly's 2016 result has the same conceptual homogeneous-minimum comparison, but its published target is ordinary `K=1` TASEP. It does not, in the material located in this run, state the `K=2` lazy-LPP theorem above.
2. Bahadoran--Bodineau's dilute-disorder theorem is again `K=1`.
3. Floreani--Redig--Sau randomize site capacities and study a different partial-exclusion random environment.
4. Gonçalves--Hayashi--Sasada characterize gradient/product-measure partial exclusion, not this quenched site-rate flux plateau.
5. Ayyer--Misra alter the `K`-exclusion jump rates to an integrable deformed model.

So the nearest solved problem remains the `K=1` disorder plateau, and the missing ingredient there is not obviously a published general-`K` statement. This remains only a bounded prior-art screen. A dedicated citation-graph audit is still required before any novelty claim or paper package.

## 8. Sharpen the frozen binary metric by optimizing the homogeneous union bound

For the frozen binary law,

\[
r=\frac12,
\qquad
\mathbb E\frac1\alpha=\frac32,
\qquad
\mu_Q=\frac12.
\tag{8.1}
\]

Consequently

\[
\Delta_2(Q)\ge\frac{1}{4G_1(0)}.
\tag{8.2}
\]

The previous run used the convenient but crude bound `G_1(0)<=4`. Optimize it.

There are at most `3^n` lazy paths of length `n`. Along a fixed path in the homogeneous rate-one field, the `n` weights are independent unit exponentials, so their sum is `Gamma(n,1)`. For every `a>1`, optimized Chernoff gives

\[
\mathbb P\{\Gamma(n,1)\ge an\}
\le\exp\{-n(a-1-\log a)\}.
\tag{8.3}
\]

Hence

\[
\mathbb P\{T_1(n,0)\ge an\}
\le
\exp\{-n[a-1-\log a-\log3]\}.
\tag{8.4}
\]

Let `a_*` be the unique root greater than one of

\[
a_*-1-\log(3a_*)=0.
\tag{8.5}
\]

The left side is strictly increasing for `a>1`. For every `a>a_*`, (8.4) is summable, so Borel--Cantelli and then `a downarrow a_*` give

\[
G_1(0)\le a_*.
\tag{8.6}
\]

Numerically only for orientation, `a_*=3.28928141456...`, yielding the implicit lower bound

\[
\Delta_2(Q)\ge\frac1{4a_*}=0.07600444245\ldots.
\]

For the **exact ledger certificate**, set

\[
a_{\rm hi}=\frac{6578563}{2000000}=3.2892815.
\]

To certify `a_hi>a_*` without floating point, it suffices to prove

\[
e^{a_{\rm hi}-1}>3a_{\rm hi}.
\]

Since `x=a_hi-1>0`, the degree-14 Taylor partial sum is a strict lower bound on `e^x`. The archived exact checker verifies, with rational arithmetic,

\[
\sum_{k=0}^{14}\frac{x^k}{k!}-3a_{\rm hi}
=
\frac{
47430167765937581947041349295831667457401616110078741744198815644306552687267546335367781899
}{
129848102092800000000000000000000000000000000000000000000000000000000000000000000000000000000000000
}>0.
\tag{8.7}
\]

Therefore `G_1(0)<a_hi`, and (8.2) gives

\[
\boxed{
\Delta_2(Q)\ge\frac1{4a_{\rm hi}}
=\frac{500000}{6578563}.
}
\tag{8.8}
\]

This is the tracked before/after movement.

## 9. Exact checker and output

Substantive exact artifacts for this run are:

- `artifacts/hard7_2026-09-18/HARD7-03/general_k2_plateau_width.py`;
- `artifacts/hard7_2026-09-18/HARD7-03/general_k2_plateau_width.out`.

They verify exactly:

1. the `Exp(a)+bonus = Exp(r)` Laplace-transform identity;
2. `E[bonus]=1/r-1/a`;
3. the source level-boundary secant algebra;
4. the binary values `E[1/alpha]=3/2`, `mu=1/2`, `r mu=1/4`;
5. the exact Taylor certificate (8.7), hence `a_hi>a_*`;
6. `L=500000/6578563`, `L>1/16`, and `L>19/250`.

The executed output ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker certifies the finite algebra only. The rare-strip, conditional concentration, shape-limit, and convex-duality steps are mathematical arguments written above and remain **self-checks**, not independent audits.

## 10. Counterexample-oriented stress tests and what failed

This run did not simply generalize the previous proof syntactically. It explicitly attacked the two places where the argument could fail.

- **No minimum atom.** The old proof seemed to break because exact all-minimum strips disappear. B29 shows this is not a counterexample: fixed near-minimum strips occur at every positive tolerance, and the order of limits `n -> infinity`, then strip width, then tolerance `epsilon -> 0` recovers exact central saturation.
- **Adaptive optimizer with a continuum of row rates.** The old binary proof could conceivably rely on identical fast-row bonus laws. Lemma 5.2 gives a uniform exponential lower-tail estimate after centering by the row-dependent means, so the path's offline time choices still cannot erase the average crossing bonus.
- **Adjacent partial-exclusion literature.** B21 found models with random capacities, gradient rates, and integrable deformations, but not an exact theorem that makes the source residual known. This lowers but does not eliminate prior-art risk.

The simplest remaining source-level obstruction is therefore no longer `K=2`; it is the extension of the lazy-path/coupling geometry to `K>=3`, where the source growth increment set and the forced-crossing decomposition need to be re-derived rather than guessed.

## 11. Next route and section-I state

Because the fixed metric moved again, the stagnation counter is zero. No Section-I rotation is triggered.

A subsequent run must use a different triple. The most promising choices are:

- **B1**: change category and express general `K` source growth as a finite-step directed control / queueing geometry;
- **B19**: make the `K>=3` crossing decomposition algorithmic and identify exactly how many independent row bonuses net displacement forces;
- **B27**: swap quantifiers by first proving a uniform theorem for each fixed `K` under iid site disorder, then ask whether the constant can be made explicit in `K`.

If that general-`K` route fails to move the fixed metric for three consecutive runs, the normal Section-I protocol applies.

## 12. Capability statement

The available scheduler/runtime surface still exposes no binding model selector, reasoning-effort selector, authenticated maximum-reasoning telemetry, or guaranteed execution duration. GPT-6/maximum is prompt-requested only. The actual model in this run is GPT-5.6 Sol; reasoning level is UNVERIFIED.

The repository policy also records historical native task-edit errors of the form `You cannot modify this task`. Where a task remains non-editable, the compliant workaround is the authorized owner/account/workspace interface or platform support/ownership correction. A repository edit is not a scheduler repair, and creating a duplicate task would violate the policy. No scheduler was created, modified, disabled, or re-enabled in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  canonical_target: D0025
  owner_claim: operations/claims/D0025.md
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  fixed_metric: "rigorous certified lower bound L <= Delta_2(Q) for Q=1/2 delta_{1/2}+1/2 delta_1"
  before: 1/16
  after: 500000/6578563
  movement: true
  methods: [5, 21, 29]
  theorem_candidate:
    scope: "K=2 iid site rates Q on [r,1], r=ess inf Q>0, nondegenerate"
    statement: "f_{2,Q} is flat around rho=1 with half-width at least mu_Q/G_Q(0)=(1-r E[1/alpha])/G_1(0)>0"
    central_saturation: "G_Q(0)=G_r(0), no atom at r required"
    cusp: "G_Q(0)-G_Q(v) >= mu_Q |v|"
    audit_status: "self-check only; prior-art novelty not certified"
  binary_exact_certificate:
    a_hi: 6578563/2000000
    L: 500000/6578563
  exact_artifacts:
    - artifacts/hard7_2026-09-18/HARD7-03/general_k2_plateau_width.py
    - artifacts/hard7_2026-09-18/HARD7-03/general_k2_plateau_width.out
  exact_output_status: "ALL_EXACT_CHECKS_PASS = True"
  section_I_state: "metric moved; stagnation reset"
  next_methods: [1, 19, 27]
  posted_changed: false
  results_changed: false
  queue_changed: false
  claim_changed: false
```

No root-ledger mutation, public posting, email, Drive write, independent audit, closure claim, or scheduler change is made in this run.
