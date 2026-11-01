Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: 12 -> 13 genuinely distinct nonparabolic shape families; Section-B moves tried: #2 ATTACK THE NEGATION FIRST, #3 PROVE SOMETHING STRONGER, #25 COUNT THE SAME THING TWICE.**
Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Status: PARTIAL; the source's open-ended request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 13: disconnected parabolic fans

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Fixed metric and continuity

The frozen metric remains

> the number of genuinely nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The previous authoritative report is

`runs/R07/20260917T0421Z_i0077_two_scale_aperture_12.md`,

which moved the metric `11 -> 12` for connected tubes with two positive normalized parabolic apertures, one at the seam and one in the remote past.

This run changes topology rather than merely another wall profile. The new family has, at every nonzero time slice, a **finite disconnected union of parabolic branches**. Every preceding counted I0077 family had a connected normalized cross-section (one interval, possibly moving, pulsed, corrugated, or nonmonotone). Brownian scaling and reflection preserve the number of connected components of the normalized slice. Hence a finite disconnected fan is not equivalent to any preceding family under the frozen convention.

Therefore the fixed metric moves

\[
\boxed{12\longrightarrow13.}
\]

`unchanged_count = 0`.

All 30 Section-B moves were already used once in I0077 runs 1–10. This run is in the second cycle. The preceding triple was `1,24,27`; the present triple `2,3,25` is different.

The old R07 KPZ/FPP route remains retired exactly as preserved by the immutable handoff; no historical report is deleted or rewritten.

## 2. Admission, repository continuity, and ownership

Before new mathematics I recovered current `master` evidence from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the complete searchable R07/I0077 report chain through run 12;
- the newest neighboring R15 report `runs/R15/20260917_0456Z_clb_centered_normalized_a25.md`;
- C29's earlier I0077 ownership-exclusion report, which recovered the source but correctly did not start a competing proof;
- targeted intake/attempt searches for I0077, arXiv:1302.6958, and Problem 7.8.

`INDEX.md` and `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 exclusion. `QUEUE.md` keeps I0077 as a distinct candidate, and `operations/claims/I0077.md` reserves it exclusively to R07 while still saying `PENDING_ADMISSION, not READY`. The owner continues to assign this exact target to R07; this worker does not edit the shared claim or ledgers.

The compact root `RESULTS.md` still contains a stale pre-rotation R07/FPP row and explicitly says newer complete current-target reports must be recovered before replacing R-series values. The immutable R07/I0077 chain is therefore the current mathematical state.

R15's current target is now a distinct Randomstrasse low-degree clique question; its former Burdzy–Scheutzow Problem 7.2 / I0076 assignment remains retired-handoff and is not reopened. No ownership collision was found.

The large `probability_1000_intake_*/problems.jsonl` resources are connector-truncated when rendered wholesale. I record the whole-intake reread honestly as **PARTIAL / targeted due connector limits**. Exact I0077 source, source statement, ownership, prior R07 work, exclusions, and neighboring ownership were recovered directly.

## 3. Source recovery and dated current-status pass

I reread the primary paper rather than relying on the intake snippet.

Definition 2.1: an FBM `X` has witness times `S_n -> -infinity` such that for each witness

\[
B^{(n)}_t=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

is standard Brownian motion.

Definition 2.2: a decomposable FBM is built by concatenating independent Brownian pieces stopped at finite stopping times.

For finite `c_1<c_2`, Theorem 4.3 states:

1. if `lambda_0(c_1,c_2)>=1`, every FBM almost surely violates at least one side of the parabolic asymptotic strip in the stated `limsup/liminf` sense;
2. if `lambda_0(c_1,c_2)<=1`, there is a decomposable FBM with normalized backward `liminf/limsup` lying between `c_1,c_2`;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there is a decomposable FBM lying pointwise in the exact parabolic strip for every `t<=0` almost surely.

The source identifies `lambda_0` as the principal killed-Ornstein–Uhlenbeck/Sturm–Liouville exponent, gives continuity and strict domain monotonicity, and records the symmetric critical identity

\[
\lambda_0(-1,1)=1.
\]

Problem 7.8 is exactly the single sentence asking whether Theorem 4.3 can be generalized from parabolas to other space-time shapes. The following forward-Lévy question is separately numbered Problem 7.9 and is not part of I0077.

### Dated literature search — 2026-09-17

Fresh bounded searches covered the exact title/problem wording, later Burdzy/Scheutzow papers, citing papers, disconnected/time-dependent OU killing domains, square-root Brownian boundaries, and Brownian cone/slow-point literature. They recovered the original paper and related ordinary-Brownian/OU moving-boundary literature, including recent time-varying OU boundary-crossing work, but I did **not** locate a later paper explicitly resolving exact Problem 7.8 or stating the finite disconnected-fan theorem below.

This is **bounded negative evidence only**. Publication novelty remains **UNVERIFIED**. Killed-OU spectral theory, direct sums on disconnected Dirichlet domains, Brownian scaling, and source Theorem 4.3 are standard/prior ingredients; the claim below is their source-matching FBM consequence for a new shape class.

## 4. Method #2 — attack the negation first: convexification gives the wrong answer

A natural attempted extension for a nonconvex shape is:

> replace each disconnected spatial slice by its convex hull and apply the parabolic theorem to that hull.

This fails decisively.

Take the normalized two-branch set

\[
D_*= [-6,-5]\cup[5,6].
\tag{4.1}
\]

The corresponding space-time fan is

\[
\mathcal F_{D_*}
=
\{(-u,x):u>0,\ x/\sqrt u\in D_*\}\cup\{(0,0)\}.
\tag{4.2}
\]

For the OU generator

\[
\mathcal A=\frac12\partial_{xx}-\frac12x\partial_x
\]

with invariant Gaussian weight `exp(-x^2/2)`, the Dirichlet Rayleigh quotient is

\[
\lambda_0(I)
=
\inf_{0\ne f\in H_0^1(I)}
\frac{\frac12\int_I |f'(x)|^2e^{-x^2/2}\,dx}
{\int_I f(x)^2e^{-x^2/2}\,dx}.
\tag{4.3}
\]

Put `g(x)=f(x)e^{-x^2/4}`. Integration by parts gives the exact ground-state transform

\[
\frac12\int_I |f'|^2e^{-x^2/2}dx
=
\int_I\left[
\frac12|g'|^2+
\left(\frac{x^2}{8}-\frac14\right)g^2
\right]dx.
\tag{4.4}
\]

Hence if `I subset [A,infinity)` then

\[
\lambda_0(I)\ge \frac{A^2}{8}-\frac14.
\tag{4.5}
\]

For `I=[5,6]`,

\[
\lambda_0(5,6)\ge\frac{25}{8}-\frac14=\frac{23}{8}>1,
\tag{4.6}
\]

and reflection gives the same bound for `[-6,-5]`.

But the convex hull of `D_*` is `[-6,6]`. It strictly contains `[-1,1]`, and source strict domain monotonicity together with `lambda_0(-1,1)=1` gives

\[
\lambda_0(-6,6)<1.
\tag{4.7}
\]

Therefore Theorem 4.3(iii) supplies a decomposable FBM lying **pointwise for all negative times** in the convex-hull parabola

\[
|X_t|\le6\sqrt{|t|}.
\tag{4.8}
\]

The theorem below, however, shows that **no FBM can even be eventually confined** in the disconnected fan (4.2). Convexification therefore reverses the confinement verdict. This falsifies a proposed extension mechanism, not the source's open-ended Problem 7.8.

The finite arithmetic in (4.6) and the strict hull containment were checked exactly in

- `artifacts/R07/20260917T0524Z_parabolic_fan_constants_check.py` @ `0adf00937c92f3006d739f8b93e04eddc784fffb`;
- archived output `artifacts/R07/20260917T0524Z_parabolic_fan_constants_check.out` @ `78edcdd52420542c4e3a98591b3e69f5c883aa3d`, which begins `PASS` and records `component_OU_lower_bound=23/8`.

The checker certifies only the finite arithmetic. Equations (4.3)–(4.5) and the source spectral facts are analytic claims proved/cited on this page, not delegated to code.

## 5. Method #3 — prove something stronger: arbitrary finite disconnected fans

Let

\[
D=\bigcup_{j=1}^{m}[a_j,b_j],
\qquad
m\ge2,
\qquad
a_j<b_j<a_{j+1},
\tag{5.1}
\]

be a finite union of pairwise disjoint compact intervals. Define the parabolic fan

\[
\mathcal F_D
=
\left\{(-u,x):u>0,\ \frac{x}{\sqrt u}\in D\right\}
\cup\{(0,0)\}.
\tag{5.2}
\]

For each component set

\[
\lambda_j=\lambda_0(a_j,b_j),
\qquad
\lambda_*(D)=\min_{1\le j\le m}\lambda_j.
\tag{5.3}
\]

# 6. I0077-R07-T14 — finite disconnected parabolic-fan theorem

**Status of theorem: PROVED on the page below. Overall source status remains PARTIAL.**

### T14(i): strict supercritical phase — universal impossibility

If

\[
\boxed{\lambda_*(D)>1,}
\tag{6.1}
\]

then for every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
\frac{X_{-u}}{\sqrt u}\in D
\quad\forall u\ge R
\right)=0.
}
\tag{T14.i}
\]

Thus no FBM can remain pointwise in `F_D` on the whole negative half-line either.

### T14(ii): strict subcritical phase — decomposable eventual existence

If

\[
\boxed{\lambda_*(D)<1,}
\tag{6.2}
\]

then there exists a decomposable FBM `X` such that

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
\frac{X_{-u}}{\sqrt u}\in D
\quad\forall u\ge R
\right)=1.
}
\tag{T14.ii}
\]

### T14(iii): pointwise source clause on a winning component

If for some component `j`,

\[
a_j\le0\le b_j,
\qquad
\lambda_j<1,
\tag{6.3}
\]

then there exists a decomposable FBM satisfying

\[
\boxed{
(-u,X_{-u})\in\mathcal F_D
\qquad\forall u\ge0
}
\tag{T14.iii}
\]

almost surely.

The critical boundary `lambda_*(D)=1` is deliberately not claimed. Source Theorem 4.3(ii) at equality controls only `liminf/limsup`; without an interior spectral margin it does not by itself imply eventual exact membership in a closed component of `D`.

## 7. Complete proof

### Proof of T14(i)

Assume `lambda_*(D)>1` and suppose, toward a contradiction, that for some FBM `X` the event

\[
E=\left\{\exists R:\ X_{-u}/\sqrt u\in D\ \forall u\ge R\right\}
\tag{7.1}
\]

has positive probability.

On every sample path in `E`, choose one admissible `R`. The map

\[
y(u)=\frac{X_{-u}}{\sqrt u},\qquad u\in[R,\infty),
\tag{7.2}
\]

is continuous. Its image is connected. Since `D` is a **finite disjoint union** of closed intervals separated by positive gaps, a connected subset of `D` lies in exactly one component. Thus on `E` there is some random index `J` such that

\[
y(u)\in[a_J,b_J]\qquad\forall u\ge R.
\tag{7.3}
\]

Because only finitely many `J` are possible and `P(E)>0`, there is one deterministic `j` for which the corresponding component event has positive probability.

Now `lambda_j>1`. Continuity of the principal eigenvalue under endpoint perturbation gives `delta>0` small enough that

\[
\lambda_0(a_j-\delta,b_j+\delta)>1.
\tag{7.4}
\]

Source Theorem 4.3(i), applied to this enlarged interval, gives for every FBM

\[
\mathbb P\left(
\limsup_{u\to\infty}y(u)\ge b_j+\delta
\ \text{or}\ 
\liminf_{u\to\infty}y(u)\le a_j-\delta
\right)=1.
\tag{7.5}
\]

But (7.3) implies simultaneously

\[
\limsup y\le b_j,
\qquad
\liminf y\ge a_j,
\tag{7.6}
\]

contradicting (7.5). Therefore `P(E)=0`, proving T14(i).

The endpoint enlargement in (7.4) is essential: applying the source theorem to `[a_j,b_j]` itself would allow equality at an endpoint and would not contradict exact membership in the closed component.

### Proof of T14(ii)

Assume `lambda_*(D)<1`. Choose `j` with

\[
\lambda_j<1.
\tag{7.7}
\]

By continuity of `lambda_0` and strict positivity of the interval length, choose `epsilon>0` so small that

\[
a_j+\varepsilon<b_j-\varepsilon
\quad\text{and}\quad
\lambda_0(a_j+\varepsilon,b_j-\varepsilon)<1.
\tag{7.8}
\]

Apply source Theorem 4.3(ii) to the **shrunken** component `[a_j+epsilon,b_j-epsilon]`. There exists a decomposable FBM `X` such that almost surely

\[
\liminf_{u\to\infty}y(u)\ge a_j+\varepsilon,
\qquad
\limsup_{u\to\infty}y(u)\le b_j-\varepsilon.
\tag{7.9}
\]

From the definitions of `liminf` and `limsup`, (7.9) implies that for all sufficiently large `u`,

\[
a_j<y(u)<b_j.
\tag{7.10}
\]

Hence eventually `y(u) in [a_j,b_j] subset D`, proving T14(ii).

The shrinking margin in (7.8) is essential for the same reason as the enlargement margin in T14(i): source asymptotic inequalities at a closed endpoint do not alone force eventual exact membership.

### Proof of T14(iii)

If (6.3) holds, source Theorem 4.3(iii) applied directly to the component `[a_j,b_j]` gives a decomposable FBM `X` satisfying

\[
a_j\sqrt u\le X_{-u}\le b_j\sqrt u
\qquad\forall u\ge0
\tag{7.11}
\]

almost surely. Since `[a_j,b_j] subset D`, this same process lies pointwise in `F_D`. QED.

## 8. Method #25 — count the same object twice: topology and spectrum give the same threshold

The Lamperti transform

\[
Y_s=e^{-s/2}B_{e^s}
\tag{8.1}
\]

turns ordinary Brownian motion into stationary OU motion and turns the parabolic fan `F_D` into killing outside the **fixed disconnected domain** `D`.

The Dirichlet form space decomposes orthogonally over connected components:

\[
H_0^1(D)
=
\bigoplus_{j=1}^m H_0^1((a_j,b_j)).
\tag{8.2}
\]

Consequently the killed-OU generator is a direct sum, and its spectral bottom is exactly

\[
\boxed{
\lambda_0(D)=\min_j\lambda_0(a_j,b_j)=\lambda_*(D).
}
\tag{8.3}
\]

That is the spectral count.

The pathwise count is the connected-image argument from T14(i): a continuous normalized FBM path that stays in a finite disconnected `D` on a whole tail cannot switch components, because switching would cross a gap. It therefore chooses exactly one branch, and the least costly branch is precisely the component with the smallest source exponent.

Thus the same threshold is obtained twice:

1. **topologically** — eventual confinement selects one connected component;
2. **spectrally** — the disconnected killed-OU operator is the direct sum of the component operators and selects their minimum principal exponent.

This identifies a natural nonparabolic replacement for the source exponent in this family rather than merely giving a one-off example.

## 9. Why this is a new metric point

The whole finite-fan class (all finite `m>=2` and all endpoint choices) counts as **one** structural family. Different component counts or endpoint parameters do not increment the metric separately.

It is nevertheless distinct from all twelve earlier families under the frozen equivalence convention:

- mixed/pure-power and logarithmic cusp gauges have one connected slice;
- outward corrugations have one connected slice;
- positive-seam gauges have one connected slice;
- periodic, aperiodic, nonsyndetic, and sparse-drifting pulse tubes move one interval in logarithmic time but keep each slice connected;
- the bounded-envelope log-sawtooth gauge is one symmetric interval;
- the pinched-seam and two-scale-aperture families are one connected interval at every nonzero time.

By contrast, `F_D` has `m>=2` components at every `u>0`. Brownian rescaling, reflection, and time translation preserve finite-slice component count, so no permitted trivial equivalence turns the fan into a previous family.

Hence the frozen metric legitimately moves

\[
\boxed{12\to13}.
\]

## 10. What the three methods accomplished

### #2 ATTACK THE NEGATION FIRST

The proposed “convexify first, then apply Theorem 4.3” extension fails. The canonical fan `[-6,-5] union [5,6]` is universally impossible even eventually, while its convex hull `[-6,6]` admits a source decomposable FBM pointwise for all negative times. This is a falsification of the proposed mechanism, **not** a refutation of Problem 7.8.

### #3 PROVE SOMETHING STRONGER

Rather than stop at the two-branch example, I proved the strict phase theorem for every finite union of disjoint parabolic branches, with the exact threshold `min_j lambda_j` and a source-matching pointwise clause whenever the winning branch straddles zero.

### #25 COUNT THE SAME THING TWICE

The threshold is simultaneously the direct-sum killed-OU principal exponent and the branch selected by continuity of the normalized path. This gives a structural explanation for why the minimum component exponent, not the convex hull, is the correct quantity.

## 11. Prior art and claim discipline

The analytic ingredients are classical/source-level:

- Burdzy–Scheutzow Theorem 4.3 and its principal OU exponent;
- continuity and strict domain monotonicity of the Dirichlet principal exponent;
- Lamperti's Brownian-to-OU transform;
- direct-sum spectral decomposition on disconnected Dirichlet domains;
- the elementary ground-state transform (4.4).

I found no explicit later source in the bounded dated search stating this finite disconnected-fan FBM theorem or closing Problem 7.8. That is **not** a novelty certificate. A specialist literature audit is still required before publication.

No source closure is claimed. T14 has no P26 end-to-end audit and no second independent OTHER-track audit. One earlier R06 scoped audit concerns the run-2 super-LIL gauge theorem, not T14, and cannot be repurposed as an audit of this run. Therefore no `paper_<name>/` folder is created.

## 12. Model / scheduler / permission status

The requested `GPT-6 / maximum` configuration remains unenforceable through the exposed scheduler surface. The available controls expose title/prompt, schedule/relative start, timing mode, and enabled state. They expose **no authenticated model-family selector, no reasoning-effort selector, and no completed-run model telemetry**. This run therefore reports the actual model family visible to it as GPT-5.6 Sol and the reasoning level as UNVERIFIED.

A verifiable GPT-6/maximum configuration would require the product/API to expose persistent model/reasoning fields and authenticated run metadata, or an authorized owner/admin product surface that can set them. Repository policy records the same limitation.

The historical P26 `You cannot modify this task` result was authorization/context scoped: another authorized context later succeeded with the P26 prompt update. The legitimate workaround is therefore the task's owning authorized context, an owner/admin permission repair, or platform support — not a duplicate schedule, permission bypass, or repository-only fiction. No scheduler modification was attempted in this run.

## 13. Exact artifacts and closure state

Exact finite checker:

- `artifacts/R07/20260917T0524Z_parabolic_fan_constants_check.py`
  - creation commit `0adf00937c92f3006d739f8b93e04eddc784fffb`;
- `artifacts/R07/20260917T0524Z_parabolic_fan_constants_check.out`
  - creation commit `78edcdd52420542c4e3a98591b3e69f5c883aa3d`;
  - readback output begins `PASS` and records `23/8` and gap `15/8` above the source critical exponent `1`.

The theorem-sized analytic claim is proved in full on this page. The finite checker is explicitly only a certificate for the canonical exact arithmetic.

Current source status: **PARTIAL**.  
Current fixed metric: **13**.  
Unchanged count: **0**.  
Independent T14 audits: **0/2**.  
Paper package: **not created**.

## 14. Next mathematical target

The highest-value next step is not to add another cosmetic branch count. The unresolved boundary is the **critical disconnected phase** `lambda_*(D)=1` and, more generally, disconnected shapes whose branches are connected by narrow time-dependent gates so that branch switching becomes possible.

A next second-cycle triple should differ again; a useful choice is `#4 PROVE SOMETHING WEAKER COMPLETELY`, `#11 DUALIZE`, and `#23 DO WHAT THE PROPOSER DID NOT EXPECT`. The concrete question is whether a narrow gate can be assigned an effective OU capacity/cost that interpolates between the direct-sum minimum rule above and the connected convex-domain exponent.

## 15. Structured ledger delta

```yaml
ledger_delta:
  worker: R07
  source:
    authors: [Krzysztof Burdzy, Michael Scheutzow]
    work: "Forward Brownian Motion"
    year: 2014
    arxiv: "1302.6958"
    locator: "Problem 7.8"
    intake: I0077
  target: >-
    Generalize Theorem 4.3 from parabolic regions to a genuinely distinct
    nonparabolic space-time shape family.
  metric: >-
    Number of genuinely distinct nonparabolic shape families with a complete
    source-appropriate theorem, modulo frozen trivial-equivalence convention.
  before: 12
  after: 13
  movement: true
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods_this_run: [2, 3, 25]
  theorem:
    id: I0077-R07-T14
    family: "finite disconnected parabolic fans"
    threshold: "lambda_*(D)=min_j lambda_0(a_j,b_j)"
    supercritical: "lambda_*>1 => every FBM eventually-confinement probability 0"
    subcritical: "lambda_*<1 => a decomposable FBM is eventually confined a.s."
    pointwise: "if one subcritical component contains 0, source pointwise confinement holds in that component"
    critical_case: "not claimed"
  canonical_counterexample_to_convexification:
    domain: "[-6,-5] union [5,6]"
    component_lower_bound: "23/8 > 1"
    convex_hull: "[-6,6]"
    hull_exponent: "< lambda_0(-1,1)=1 by strict domain monotonicity"
  exact_evidence:
    - "artifacts/R07/20260917T0524Z_parabolic_fan_constants_check.py @ 0adf00937c92f3006d739f8b93e04eddc784fffb"
    - "artifacts/R07/20260917T0524Z_parabolic_fan_constants_check.out @ 78edcdd52420542c4e3a98591b3e69f5c883aa3d"
  source_status: PARTIAL
  source_closure: false
  audits: []
  prior_art: >-
    Bounded dated 2026-09-17 search found no explicit later Problem-7.8 resolution
    or this finite-fan theorem; novelty remains UNVERIFIED; OU/direct-sum machinery
    is classical.
  ownership:
    canonical_claim: operations/claims/I0077.md
    owner: R07
    conflict_found: false
  delivery: "private GitHub only"
  next_methods: [4, 11, 23]
```
