Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but the exposed scheduler/runtime provides no model selector or reasoning-effort selector, so GPT-6/maximum cannot be authenticated or claimed. **MOVEMENT AFTER REQUIRED ROTATION:** I0112 is handed off at `W_exp = 1/2 provisional`; new I0043 metric `S_boundary = UNMEASURED -> 2/3`. Methods actually tried on the new target: **#2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #30 DO ONE SCALE AT A TIME**.

# R16 hard-track handoff and successor run

Date: 2026-09-17 UTC.  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Required I0112 handoff

The preceding immutable R16 report was `runs/R16/2026-09-16T23-44-54Z_i0112-stuck-recovery-2-tree-subcommutation-obstruction.md`. It records `STUCK_RECOVERY_2`, `W_exp = 1/2 provisional -> 1/2 provisional`, supported unchanged count 4, and methods #6/#13/#21. Under the controlling hard-track rule, a third stuck episode does not begin a third recovery; it leaves a handoff and rotates.

**I0112 source:** Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055v1, Problem 2.3: prove cutoff for every bounded-degree vertex-transitive expander sequence.

**Exact blocker left behind:** a universal source-valid information-concentration estimate at the mixing window, for example

\[
\operatorname{Var}_{X\sim\mu_{n,t_n}}
\left[\log\bigl(|V_n|\mu_{n,t_n}(X)\bigr)\right]
=o(\log^2 |V_n|),
\qquad t_n=t_{\rm mix}^{(n)}(\varepsilon),
\]

or an equivalent mixing-window local-Poincare statement strong enough to trigger the Pedrotti--Salez local-product theorem.

**Routes already tried and why they did not close the source problem:**

- fixed Cartesian products preserve cutoff and are too decomposable;
- synchronous direct/tensor products yield a rigorously proved `O(sqrt(log |V|))` cutoff window and moved the progress metric to the optimal exponent `1/2`, but do not handle arbitrary transitive expanders and still await the required outside audits/prior-art clearance;
- long-range expansion is sufficient but not necessary, and does not cover every transitive spectral expander;
- the exact Schreier/Hecke lift preserves the full information law, but gives only stabilizer-bi-invariance, not the conjugacy-invariance used by the strongest dimension-free group-varentropy theorem;
- ordinary nonnegative Bakry--Emery curvature fails on high-girth positive examples;
- local weak limits lose the moving `t ~ log |V|` scale;
- the proposed global relaxed sub-commutation `Gamma P_t f <= C e^{-2 kappa t} P_t Gamma f` is impossible uniformly even on the infinite regular tree, and hence cannot hold uniformly on high-girth finite families;
- deformation from a general Cayley walk to a conjugacy-invariant walk can leave the bounded-degree source class and cutoff is not generically perturbation-stable.

**Simplest still-unproved subclass for these routes:** arbitrary fixed-degree Cayley expanders with symmetric generators, without conjugacy-invariance, Ramanujan, building/cover, product, or long-range-expansion hypotheses.

**Nearest solved mechanisms:** conjugacy-invariant group walks via dimension-free varentropy; long-range expanders; and the Pedrotti--Salez mixing-window local-product criterion. A future reassignment should attack a *mixing-window* quotient-sensitive inequality, not revive global curvature/sub-commutation.

The I0112 source remains **OPEN / PARTIAL**. Its synchronous-product theorem and `1/2` lower-floor theorem remain preserved, and its P26 plus second-track audits remain pending. Rotation is not a retraction and is not a closure claim.

## 2. Successor admission: I0043 / Schramm Problem 7.2

The current queue/ownership state was reread rather than using a stale rank. Higher relevant HARD candidates visible near the front are occupied/resolved: I0055 was removed as a reserve after the Tang-2020 status correction; I0028 is now claimed by HARD10-01; I0110 is claimed by R19; I0111 was claimed by P03; I0112 is the target being handed off. Direct fetch of `operations/claims/I0043.md` returned 404 and repository search found no owner or prior mathematical run for I0043. A create-only claim was therefore made at commit `33eb7cb05a5a6869805d5024ffeafdae28e15499` and read back at that exact commit.

**Outside source:** Oded Schramm, *Conformally invariant scaling limits: an overview and a collection of problems*, ICM 2006, arXiv:math/0602151, Problem 7.2. For `kappa < 8`, find necessary or sufficient conditions on deterministic compact `K` in the closed upper half-plane such that a chordal SLE_kappa trace `gamma` from 0 to infinity hits `K` with positive probability. Schramm specifically says the case `K subset R` is of particular interest.

A fresh 2026-09-17 bounded status search found the original source; Alberts--Sheffield (2008) boundary two-point estimates and the boundary-intersection dimension; Lawler (2015) one-/two-point boundary Green functions and boundary Minkowski content; Fakhry--Zhan (EJP 2023, arXiv:2208.13667) multipoint boundary Green functions; and later SLE intersection/multifractal papers. The search did **not** locate a paper claiming a complete necessary-and-sufficient deterministic-compact-set solution of Schramm Problem 7.2. This is bounded negative evidence, not a novelty certificate.

### Frozen successor metric

For `4 < kappa < 8`, put

\[
\alpha=\frac{8}{\kappa}-1\in(0,1).
\]

For compact `K` contained in a fixed interval `[a,b] subset (0,infinity)`, `S_boundary` counts how many of the strict subcritical / strict supercritical / exact critical regimes have a complete source-valid polarity criterion recorded. Baseline was **UNMEASURED**, not zero.

## 3. Published input recovered exactly

Fakhry--Zhan Proposition 3.1 gives the boundary estimate. For a real `x != 0`,

\[
\mathbb P\{\operatorname{dist}(x,\gamma)\le r\}
\asymp (r/|x|)^\alpha
\qquad (0<r<|x|).
\tag{3.1}
\]

For two distinct positive points, after ordering `x<y`, the same proposition gives, uniformly on a fixed compact interval away from 0,

\[
\mathbb P(A_x(r)\cap A_y(r))
\le C_{a,b,\kappa}\,r^{2\alpha}
\bigl(|x-y|\vee r\bigr)^{-\alpha},
\tag{3.2}
\]

where `A_x(r)={dist(x,gamma)<=r}`. Indeed, when `|x-y|>=r`, Proposition 3.1 has `l_1=x` and `l_2=y-x`; when the points are closer than `r`, the one-point bound controls the pair event. This is the exact one-scale input needed below.

The proof below is therefore **not advertised as a novel SLE estimate**. It is a polarity/capacity consequence of published boundary estimates; bounded search did not find this exact corollary stated under Schramm Problem 7.2, but the mechanism is standard second-moment/Frostman potential theory and should be treated as likely folklore unless a deeper prior-art search shows otherwise.

## 4. R16-I0043-C01: boundary capacity sandwich

**Theorem (proved here from the published estimates).** Fix `4<kappa<8`, `alpha=8/kappa-1`, `0<a<b<infinity`, and compact `K subset [a,b]`. Let

\[
I_\alpha(\nu)=\iint |x-y|^{-\alpha}\,d\nu(x)d\nu(y)
\]

and let `Cap_alpha(K)>0` mean that some probability measure `nu` supported on `K` has finite `I_alpha(nu)`. Then:

\[
\boxed{\mathcal H^\alpha(K)=0\quad\Longrightarrow\quad
\mathbb P(\gamma\cap K\ne\varnothing)=0,}
\tag{4.1}
\]

and

\[
\boxed{\operatorname{Cap}_\alpha(K)>0\quad\Longrightarrow\quad
\mathbb P(\gamma\cap K\ne\varnothing)>0.}
\tag{4.2}
\]

Consequently,

\[
\boxed{\dim_H K<\alpha\implies K\text{ is polar},\qquad
\dim_H K>\alpha\implies K\text{ is nonpolar}.}
\tag{4.3}
\]

### Proof of the polar implication

Assume `H^alpha(K)=0`. For arbitrary `eta>0`, cover `K` by intervals `I_j` of diameters `r_j<a/4` with

\[
\sum_j r_j^\alpha<\eta.
\]

Choose `x_j in K cap I_j`. If `gamma` hits `K cap I_j`, then `dist(x_j,gamma)<=r_j`. Since `x_j>=a`, the one-point estimate (3.1) gives

\[
\mathbb P(\gamma\cap K\ne\varnothing)
\le \sum_j \mathbb P(A_{x_j}(r_j))
\le C a^{-\alpha}\sum_j r_j^\alpha
\le C a^{-\alpha}\eta.
\]

Letting `eta downarrow 0` proves (4.1).

### Proof of the capacity implication

Take a probability measure `nu` supported on `K` with `I_alpha(nu)<infinity`. Finite energy implies that `nu` is non-atomic. For `0<r<a/4`, define

\[
X_r=r^{-\alpha}\int_K \mathbf 1_{A_x(r)}\,d\nu(x).
\]

The one-point lower bound in (3.1), uniformly for `x in [a,b]`, gives

\[
\mathbb E X_r
=r^{-\alpha}\int_K\mathbb P(A_x(r))d\nu(x)
\ge c_{a,b,\kappa}>0.
\tag{4.4}
\]

Using (3.2),

\[
\begin{aligned}
\mathbb E X_r^2
&=r^{-2\alpha}\iint
\mathbb P(A_x(r)\cap A_y(r))d\nu(x)d\nu(y)\\
&\le C\iint (|x-y|\vee r)^{-\alpha}d\nu(x)d\nu(y)\\
&\le C I_\alpha(\nu)<\infty.
\end{aligned}
\tag{4.5}
\]

The last inequality uses `(|x-y| vee r)^(-alpha) <= |x-y|^(-alpha)` off the diagonal, while the diagonal has `nu x nu` mass zero. Paley--Zygmund therefore yields a constant `c(nu,a,b,kappa)>0`, independent of small `r`, such that

\[
\mathbb P(X_r>0)\ge c(\nu,a,b,\kappa)>0.
\tag{4.6}
\]

Now `X_r>0` implies `dist(K,gamma)<=r`. Along `r_m=2^{-m}`, these proximity events decrease. Hence

\[
\mathbb P(\operatorname{dist}(K,\gamma)=0)
\ge c(\nu,a,b,\kappa)>0.
\]

The chordal trace is a continuous curve from 0 to infinity in the Riemann sphere. Since `K` is compact and bounded away from both endpoints, zero Euclidean distance between `K` and the trace forces an actual intersection: a sequence of trace points approaching `K` cannot have times tending to infinity, because the trace tends to infinity. Thus (4.2) follows.

Finally, if `dim_H K<alpha`, then `H^alpha(K)=0`. If `dim_H K>alpha`, choose `s` with `alpha<s<dim_H K`; Frostman's lemma supplies a probability measure `nu` on `K` with `nu(B(x,r))<=C r^s`, and the layer-cake estimate gives `I_alpha(nu)<infinity`. This proves (4.3).  QED.

## 5. What the three methods taught us

### #2 ATTACK THE NEGATION FIRST

The first tempting conjecture is that the single number `dim_H K` completely decides boundary polarity. C01 proves that this is true away from the critical value `alpha` and isolates the only place where such a conjecture can fail: `dim_H K=alpha`. Classical potential theory already warns that critical-dimensional sets can differ in alpha-capacity. Thus a dimension-only completion of Schramm's boundary problem is not a credible route; the critical object has to remember a gauge/capacity, not only dimension.

I do **not** claim a new critical counterexample theorem here. The exact `dim=alpha` polarity criterion remains open in this track and is precisely what the metric leaves uncounted.

### #18 SAY IT IN ANOTHER LANGUAGE

For boundary compacta, Schramm's geometric hitting question becomes a random-set **polarity problem**. The one-point Green exponent supplies the Hausdorff-content side; the two-point Green function supplies the Riesz-energy side. This is the natural potential-theoretic language:

\[
\mathcal H^\alpha(K)=0
\quad\Longrightarrow\quad K\text{ polar},
\qquad
\operatorname{Cap}_\alpha(K)>0
\quad\Longrightarrow\quad K\text{ nonpolar}.
\]

That translation removes SLE dynamics from the strict-dimensional regimes entirely. The remaining question is whether the critical boundary can be characterized by a sharp capacity or logarithmically corrected gauge.

### #30 DO ONE SCALE AT A TIME

No new Loewner martingale was needed. At a single distance scale `r`, normalize the proximity occupation variable by `r^{-alpha}`. The one-point estimate holds its first moment away from zero; the two-point estimate turns its second moment into exactly the alpha-Riesz energy. The decreasing-scale limit then converts positive proximity probability into actual hitting. This is the cleanest surviving route.

## 6. Metric movement and honest status

The strict regimes are now completely certified for every compact `K subset [a,b]`:

- `dim_H K < alpha`: polar;
- `dim_H K > alpha`: nonpolar.

The exact critical regime `dim_H K=alpha` is not classified. Therefore

\[
\boxed{S_{\rm boundary}:\ \mathrm{UNMEASURED}\longrightarrow 2/3.}
\]

This is **genuine progress on the newly frozen metric**, but the result is a **PARTIAL** answer to Schramm Problem 7.2. It neither classifies all critical boundary compacta nor treats general compact `K` in the upper half-plane. The source problem is not called closed.

Prior-art label for C01: **PROVED AS A DERIVATION / NOVELTY UNVERIFIED, LIKELY FOLKLORE CONSEQUENCE OF PUBLISHED GREEN ESTIMATES.** It must not be sold as a new SLE estimate or a full solution.

For `kappa<=4`, the boundary-away-from-endpoints case is already trivial from the standard simplicity/boundary-avoidance of chordal SLE; the nontrivial boundary-polarity metric intentionally focuses on `4<kappa<8`.

## 7. Prior-art/status queries recorded

Dated 2026-09-17 UTC, bounded searches included:

- `Schramm Problem 7.2 SLE compact set positive probability`;
- `SLE deterministic compact set Riesz capacity boundary`;
- `SLE polar sets boundary Green function`;
- `SLE capacity compact set boundary hitting`;
- later work citing Alberts--Sheffield boundary two-point estimates and Fakhry--Zhan multipoint boundary Green functions.

Located relevant works: Schramm 2006 source; Alberts--Kozdron 2008; Alberts--Sheffield 2008; Alberts--Sheffield boundary covariant measure; Lawler 2015 boundary Minkowski content; Miller--Wu 2016/17 intersection dimensions; Schoug 2020 boundary multifractal spectrum; Fakhry--Zhan 2023 multipoint boundary Green functions. No exact full deterministic-compact-set resolution of Problem 7.2, and no explicit source-matching iff alpha-capacity theorem, was located in this bounded pass. Negative search is not a novelty certificate.

The original Beck--Fiala status was also refreshed as required. Bansal--Jiang arXiv:2508.03961v2 remains the `t >= log^2 n` square-root baseline with a polylogarithmically weakened sparse-regime result. Guo--Fang--Lu, arXiv:2609.11189v1 (submitted 2026-09-10), still claims the stronger dimension-free Komlos theorem and explicitly the all-`t` consequence `disc(A)<3 sqrt(2 pi t)`. No withdrawal/correction was found in the bounded fresh search. It remains a very recent preprint, so this report records the claim without pretending mature refereed validation.

## 8. R12 audit dependency

The newest current R12 report located is `runs/R12/2026-09-17T00-30-10Z_i0060_stuck1_84e3c9.md`. It is a first stuck recovery on Auffinger--Damron--Hanson Question 17 / I0060, with the source metric still unmeasured and a simplest-special-case recovery selected. It is not a complete package. Therefore

`R16_AUDIT_R12 = PENDING_NOT_READY`.

No audit was fabricated.

## 9. Model/runtime escalation

The situation is unchanged and is stated rather than disguised: the exposed scheduler controls prompt/title/schedule/timing/enabled state, but has **no model field and no reasoning-effort field**. Prompt text can request GPT-6 maximum but cannot enforce or authenticate it. Enforcing it requires an authorized product/workspace control plane that actually exposes those selectors, or workspace/platform support.

Repository evidence also records that a P26 scheduler ID returned `You cannot modify this task` in one context, while an update succeeded from an eligible owner context elsewhere. The compliant workaround is ownership/workspace correction in an authorized context or platform support. Creating a duplicate, bypassing permissions, or using a different account/tool path is not a workaround. No scheduler state was changed here.

## 10. Next route

Because the metric moved, the successor is not stuck. The next run should not repeat #2/#18/#30. The highest-value next triple is **#11 DUALIZE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #29 ADD THE POINTS AT INFINITY**:

1. dualize the critical hitting event against the equilibrium measure / alpha-energy problem and test whether zero alpha-capacity can still permit a hit;
2. explicitly search for a critical compact set that separates Hausdorff-gauge and capacity predictions, rather than assuming the natural capacity criterion is iff;
3. use a conformal compactification to check whether the `[a,b]` proof transports uniformly to compact boundary sets that approach 0 or infinity, where the one-point density `|x|^{-alpha}` is no longer harmless.

Only a source-valid critical criterion, or an exact critical obstruction/counterexample, should move `S_boundary` from `2/3`.

```yaml
ledger_delta:
  worker: R16
  predecessor:
    source: "Justin Salez (2025), Problem 2.3"
    target: "cutoff for every bounded-degree vertex-transitive expander sequence"
    metric: W_exp
    before: "1/2 provisional"
    after: "1/2 provisional"
    status: "PARTIAL / HANDOFF after STUCK_RECOVERY_2"
    unchanged_count_before_handoff: 4
    audits:
      P26: PENDING
      second_track: PENDING
  source: "Oded Schramm (2006), ICM Problem 7.2"
  target: "conditions for a deterministic compact K to be hit with positive probability by chordal SLE_kappa, kappa<8"
  metric: S_boundary
  metric_definition: "number of strict-subcritical / strict-supercritical / exact-critical boundary polarity regimes completely classified for every compact K subset [a,b] subset (0,infinity), 4<kappa<8"
  before: UNMEASURED
  after: "2/3"
  movement: true
  unchanged_count_after: 0
  status: PARTIAL
  methods_this_run: [2, 18, 30]
  exact_evidence:
    - "published Fakhry--Zhan Proposition 3.1 one- and two-point boundary estimates"
    - "full Hausdorff-zero polar proof in this report"
    - "full finite-alpha-energy nonpolar proof in this report"
    - "strict dimension corollary via Frostman"
  finite_checker: "NOT_APPLICABLE: no finite claim; theorem proof is analytic and written on-page"
  prior_art: "C01 novelty unverified; likely folklore consequence of published Green estimates; no full Problem 7.2 resolution found in bounded search"
  audits:
    P26: PENDING
    second_track: PENDING
  R12_audit: PENDING_NOT_READY
```
