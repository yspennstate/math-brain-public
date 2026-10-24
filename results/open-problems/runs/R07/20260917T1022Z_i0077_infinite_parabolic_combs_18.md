Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: 17 -> 18 genuinely distinct nonparabolic shape families; Section-B moves tried: #7 TAKE THE LIMIT, #13 FIND WHAT ONLY INCREASES / conserved branch label, #21 ASK WHO ELSE HAS THIS SHAPE.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Overall status: PARTIAL; the open-ended source request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 18: infinite parabolic combs

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, ownership, and frozen metric

The fixed R07 quantity remains:

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260917T0923Z_i0077_power_sheared_parabolic_tubes_17.md`,

which moved the metric `16 -> 17` and used Section-B moves `#5,#20,#29`. This run does not repeat that triple.

All thirty Section-B moves had already been used at least once in the preceding I0077 sequence, so the literal “never tried before on this problem” pool is exhausted. As in the preceding second-cycle reports, I use a new triple relative to the immediately preceding run and a genuinely new route rather than falsely claiming unused move numbers.

The new counted family is an **infinite parabolic comb**: the normalized spatial cross-section is closed, unbounded, and has countably infinitely many bounded connected components. This is structurally different from the finite disconnected fans of run 13 and the compact/fat-Cantor cross-sections of run 14.

The metric moves

\[
\boxed{17\longrightarrow18}.
\]

`unchanged_count = 0`.

The old R07 KPZ/FPP work remains preserved and retired by its immutable handoff; no historical R07 file was modified or deleted.

## 2. Required repository / admission reread

Before new mathematics I reread or rechecked current `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the controlling owner-directive lineage;
- canonical reservation `operations/claims/I0077.md`;
- the full searchable R07/I0077 report chain through run 17;
- newest visible neighboring R15 state and its preserved handoff from distinct Burdzy–Scheutzow Problem 7.2 / I0076;
- C29’s earlier I0077 duplicate-exclusion history;
- targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

`INDEX.md`/`RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no 7.8 exclusion. `QUEUE.md` still lists I0077 separately. The canonical claim still reserves I0077 to R07 and still carries the shared text `PENDING_ADMISSION, not READY`; this worker does not rewrite shared operational files. The root `RESULTS.md` R07/FPP row is stale by its own warning and is not used as the mathematical baseline.

The large `probability_1000_intake_*/problems.jsonl` mirrors cannot be rendered literally row-by-row through the exposed connector without truncation. The intake reread is therefore honestly **PARTIAL / targeted**, with the exact source, ownership, duplicate-attempt and neighboring-scope checks recovered.

## 3. Primary source benchmark recovered

The primary source was rechecked directly, including Definition 2.1, Definition 2.2, Remark 4.1, Remark 4.2, Theorem 4.3, and the open-problem page.

An FBM is a continuous process `X=(X_t)_{t in R}` for which there are random times `S_n -> -infinity` such that for every fixed `n`,

\[
(X_{S_n+t}-X_{S_n})_{t\ge0}
\]

is standard Brownian motion. A decomposable FBM is obtained by concatenating independent Brownian pieces stopped at finite stopping times.

For `-infinity <= c_1<c_2<=infinity`, the source writes `lambda_0(c_1,c_2)` for the principal killed-Ornstein–Uhlenbeck exponent on `(c_1,c_2)`. Theorem 4.3 states:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2)<=1`, a decomposable FBM exists with the corresponding normalized asymptotic inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, a decomposable FBM can be confined pointwise to the exact parabolic strip for every `t<=0`.

Problem 7.8 is exactly the one-sentence question asking whether Theorem 4.3 can be generalized “from parabolas to other space-time shapes.” The forward-Lévy sentence after it is separately Problem 7.9.

## 4. Fresh current-status / prior-art pass — 2026-09-17

Fresh bounded searches included:

- exact title/arXiv ID with `Problem 7.8`, `Theorem 4.3`, and `other space-time shapes`;
- `forward Brownian motion` with `disconnected`, `comb`, `closed set`, and `space-time shape`;
- Brownian motion on disconnected state spaces;
- later/citing material around Burdzy–Scheutzow.

The closest distinct literature located is Bhamidi–Evans–Peled–Ralph, *Brownian motion on disconnected sets, basic hypergeometric functions, and some continued fractions of Ramanujan* (arXiv:math/0509270; IMS collection 2008). They construct a Brownian analogue **whose state space itself is a closed disconnected subset of R**, with a corresponding non-Euclidean “does not skip points” continuity notion. That is not the present object: here `X` is an ordinary Euclidean-continuous FBM on R and the disconnected set constrains only the normalized backward space-time position `X_{-u}/sqrt(u)`.

I found no later paper in this bounded dated search explicitly resolving exact Problem 7.8 or stating the infinite-comb theorem below. This is **negative search evidence only; publication novelty remains UNVERIFIED**.

## 5. Section-B move #7 — TAKE THE LIMIT: finite fans do not automatically give the infinite comb

Run 13 handled a finite union of normalized parabolic branches. A natural limit is

\[
D_*:=\bigcup_{k\in\mathbb Z}
\left[3k-\frac14,3k+\frac14\right].
\tag{5.1}
\]

The associated space-time shape is

\[
\boxed{
\mathcal C_*
=
\left\{(-u,x):u>0,\ \frac{x}{\sqrt u}\in D_*\right\}\cup\{(0,0)\}.
}
\tag{5.2}
\]

The finite truncations

\[
D_N=\bigcup_{|k|\le N}
[3k-1/4,3k+1/4]
\]

are covered by the finite-fan theorem, but the limit `N -> infinity` is **not** automatic: an eventually confined path could in principle choose a random branch index whose magnitude is larger than every fixed truncation chosen in advance. The new argument has to control that random branch without a uniform finite cutoff.

That exact failure is what moves the proof to the next method.

## 6. Section-B move #13 — FIND WHAT ONLY INCREASES / what is conserved: the branch label cannot change

For `u>0` define

\[
y(u):=\frac{X_{-u}}{\sqrt u}.
\tag{6.1}
\]

Because `X` is continuous, `y` is continuous on every tail `[R,infinity)`. The image of a connected interval under a continuous map is connected. Therefore if

\[
y(u)\in D\qquad\forall u\ge R
\tag{6.2}
\]

for a closed set `D`, then `y([R,infinity))` must be contained in **one connected component of `D`**. In an infinite comb this component index is a conserved tail label. The path cannot migrate to farther teeth at later scales without crossing a forbidden gap.

This observation removes the apparent “escape to branch infinity” obstruction in the finite-to-infinite limit.

## 7. I0077-R07-T19 — closed parabolic comb theorem

**Status of theorem: PROVED below. Overall source status remains PARTIAL.**

Let `D subset R` be closed and assume that **every connected component of `D` is bounded**. Define

\[
\mathcal F_D
=
\left\{(-u,x):u>0,\ \frac{x}{\sqrt u}\in D\right\}\cup\{(0,0)\}.
\tag{7.1}
\]

### (A) Universal obstruction

Assume that every nondegenerate component `C=[a,b]` of `D` satisfies

\[
\boxed{\lambda_0(a,b)>1.}
\tag{7.2}
\]

Then for every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
\frac{X_{-u}}{\sqrt u}\in D\quad\forall u\ge R
\right)=0.
}
\tag{T19-A}
\]

No compactness of `D`, finite-component assumption, finite Lebesgue measure, or bounded convex hull is required.

### (B) Existence from one subcritical tooth

If `D` has a nondegenerate component `C=[a,b]` with

\[
\boxed{\lambda_0(a,b)<1,}
\tag{7.3}
\]

then there exists a decomposable FBM `X` such that, almost surely,

\[
\frac{X_{-u}}{\sqrt u}\in D
\qquad\text{for all sufficiently large }u.
\tag{T19-B}
\]

### (C) Pointwise version when the subcritical component contains the seam direction

If in addition

\[
a\le0\le b,
\tag{7.4}
\]

then there exists a decomposable FBM satisfying

\[
\boxed{
\frac{X_{-u}}{\sqrt u}\in D\qquad\forall u>0
}
\tag{T19-C}
\]

almost surely.

Components with `lambda_0=1` are deliberately left unclassified. The source itself has a critical endpoint subtlety: Theorem 4.3(ii) gives limsup/liminf inclusion at equality, which does not automatically imply exact eventual membership in a closed component.

## 8. Proof of T19(A)

Fix an integer `N>=1` and let

\[
E_N=
\left\{
\frac{X_{-u}}{\sqrt u}\in D\ \forall u\ge N
\right\}.
\]

On `E_N`, continuity of `y(u)=X_{-u}/sqrt(u)` implies that the connected set `y([N,infinity))` lies in a single connected component of `D`.

### 8.1 Nondegenerate components

Every nondegenerate connected component of a subset of `R` contains a rational in its interior, so the family of nondegenerate components is countable.

Fix one such component `C=[a,b]`. By hypothesis,

\[
\lambda_0(a,b)>1.
\]

By continuity of `lambda_0` in the endpoints, choose `epsilon>0` such that

\[
\lambda_0(a-\epsilon,b+\epsilon)>1.
\tag{8.1}
\]

If `y(u) in [a,b]` for every sufficiently large `u`, then

\[
\liminf_{u\to\infty}y(u)\ge a>a-\epsilon,
\qquad
\limsup_{u\to\infty}y(u)\le b<b+\epsilon.
\tag{8.2}
\]

This contradicts source Theorem 4.3(i) applied to `(a-epsilon,b+epsilon)`. Hence eventual confinement to this fixed component has probability zero. Countability of the nondegenerate components shows that the probability of eventual confinement to **any** nondegenerate component is zero.

### 8.2 Singleton components: a uniform countable cover avoids an uncountable union

It remains to exclude the possibility that the connected image is a singleton `{c}`, where `c` itself may be random and the set of singleton components may be uncountable.

For every rational `q`, let

\[
J_q=[q-1/4,q+1/4].
\]

The interiors of these intervals form a countable cover of `R`. I claim

\[
\lambda_0(J_q)>1\qquad\forall q\in\mathbb Q.
\tag{8.3}
\]

For an interval `I=(a,b)` of length `d`, make the standard OU ground-state substitution

\[
g(x)=f(x)e^{-x^2/4}.
\]

Then the OU Rayleigh quotient becomes

\[
\frac{\frac12\int_I |f'|^2e^{-x^2/2}\,dx}
{\int_I f^2e^{-x^2/2}\,dx}
=
\frac{\frac12\int_I|g'|^2\,dx+
\int_I\left(\frac{x^2}{8}-\frac14\right)g^2\,dx}
{\int_Ig^2\,dx}.
\tag{8.4}
\]

Dirichlet Poincare therefore gives the uniform bound

\[
\lambda_0(a,b)
\ge
\frac{\pi^2}{2d^2}-\frac14.
\tag{8.5}
\]

For `d=1/2`,

\[
\lambda_0(J_q)
\ge2\pi^2-\frac14
>18-\frac14
=\frac{71}{4}>1.
\tag{8.6}
\]

Now suppose `y(u)=c` on a tail. Choose rational `q` with `c` strictly inside `J_q`. Then

\[
\liminf y=\limsup y=c
\]

lies strictly between the endpoints of a supercritical interval, contradicting Theorem 4.3(i). Since the `J_q` are countable, this excludes all random singleton components at once.

Thus `P(E_N)=0` for every integer `N`. Finally,

\[
\{\exists R:\ y(u)\in D\ \forall u\ge R\}
\subseteq
\bigcup_{N\ge1}E_N,
\]

so (T19-A) follows.

## 9. Proofs of T19(B) and T19(C)

Suppose `C=[a,b]` is a component with `lambda_0(a,b)<1`. By endpoint continuity choose `epsilon>0` such that

\[
a+\epsilon<b-\epsilon,
\qquad
\lambda_0(a+\epsilon,b-\epsilon)<1.
\tag{9.1}
\]

Source Theorem 4.3(ii) gives a decomposable FBM with

\[
\liminf_{u\to\infty}\frac{X_{-u}}{\sqrt u}\ge a+\epsilon,
\qquad
\limsup_{u\to\infty}\frac{X_{-u}}{\sqrt u}\le b-\epsilon.
\tag{9.2}
\]

Hence eventually

\[
a<\frac{X_{-u}}{\sqrt u}<b,
\]

so the path is eventually in the component `C subset D`. This proves (T19-B).

If `a<=0<=b`, source Theorem 4.3(iii) directly supplies a decomposable FBM satisfying

\[
a\sqrt u\le X_{-u}\le b\sqrt u\qquad\forall u\ge0,
\]

which proves (T19-C).

## 10. Canonical infinite comb: an unbounded shape whose convex hull is all of R but still forbids every FBM

For `D_*` in (5.1), every component has length

\[
d=\frac12.
\]

By (8.5), for every `k in Z`,

\[
\lambda_0\left(3k-\frac14,3k+\frac14\right)
\ge2\pi^2-\frac14
>\frac{71}{4}>1.
\tag{10.1}
\]

Therefore T19(A) gives

\[
\boxed{
\mathbb P\left(
\exists R:\
\frac{X_{-u}}{\sqrt u}\in
\bigcup_{k\in\mathbb Z}[3k-1/4,3k+1/4]
\ \forall u\ge R
\right)=0
}
\tag{10.2}
\]

for **every** FBM.

This example is intentionally extreme:

- the normalized cross-section is unbounded in both directions;
- it has countably infinitely many components;
- its convex hull is the whole real line, so convexification imposes **no constraint at all**;
- every physical-time slice has infinite total Lebesgue measure;
- nonetheless Euclidean continuity freezes the normalized path into one narrow tooth, and every tooth is supercritical.

Thus neither convex hull nor total slice measure is a useful general extension criterion for Problem 7.8.

## 11. Exact finite self-check

Only the finite arithmetic underlying the canonical comb was given a checker. The theorem itself is analytic and is proved on the page.

Artifacts:

- `artifacts/R07/20260917T1022Z_infinite_comb_check.py` — creation commit `b43d174d53082c720ec634777c727aa876b1cfa7`;
- `artifacts/R07/20260917T1022Z_infinite_comb_check.out` — creation commit `9c64e6402241b209f50d763a35435f7e6c5c13c4`.

The executed exact-arithmetic output is

```text
component_length=1/2
gap_length=5/2
lambda_lower_using_pi2_gt_9=71/4
PASS
```

This is a **self-check**, not an independent audit.

## 12. Section-B move #21 — ASK WHO ELSE HAS THIS SHAPE

The most relevant disconnected-state-space reference found is Bhamidi–Evans–Peled–Ralph. Their construction shows that disconnected closed subsets of `R` support their own natural quasidiffusions when continuity is redefined so paths do not skip state-space points. That comparison clarifies why the present obstruction is specifically an FBM/Euclidean-continuity phenomenon: our normalized path cannot teleport across the open gaps between comb teeth.

This literature connection also prevents an overclaim. “Brownian motion on a disconnected set” is existing terminology and machinery. The result here is instead a consequence for **ordinary forward Brownian motion constrained by a disconnected normalized space-time shape**.

## 13. Why this is a genuinely new metric family

Run 13: finitely many bounded normalized components.  
Run 14: arbitrary **compact** normalized cross-sections, including fat Cantor sets.  
Run 15: topology-changing time-dependent finite fans.  
Run 16: a connected unbounded half-line cross-section moving periodically.  
Run 17: one bounded connected interval with a power-law moving center.

The canonical comb here has **countably infinitely many bounded components and an unbounded normalized cross-section**. Brownian scaling preserves the static normalized set; reflection only reverses the tooth labels; no frozen trivial equivalence turns infinitely many unboundedly distributed branches into a finite or compact cross-section.

I therefore count exactly one new structural family, not one family per tooth spacing or width:

\[
\boxed{17\to18}.
\]

The stronger theorem T19 subsumes the earlier static finite/compact obstruction mechanisms when its hypotheses apply, but the metric increment is charged only to the genuinely new unbounded infinite-comb class, not retroactively to every closed set.

## 14. Closure status and remaining obligations

This run materially moves the fixed quantity, so the stuck protocol does not trigger.

T19 has a full proof on the page and its finite arithmetic self-check is archived, but it has **no P26 end-to-end audit and no second independent OTHER-track audit**. The bounded literature search is not a novelty certificate. Therefore:

- source status: **PARTIAL**;
- metric: **18**;
- unchanged count: **0**;
- paper package: **not created**;
- source closure: **not claimed**.

A future closure attempt should audit T19 end-to-end, especially (i) the countability split between nondegenerate and singleton components, (ii) the uniform ground-state/Poincare bound, and (iii) whether later literature already states an equivalent closed-cross-section FBM theorem.

## 15. Model / scheduler control and the P26 modification issue

The requested GPT-6/maximum configuration is still not enforceable from the exposed task-control schema. The interface available here exposes task title/prompt, schedule, enabled state and timing mode, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore this report states the actual model identity available to the run (`GPT-5.6 Sol`) and leaves reasoning as `UNVERIFIED` rather than claiming GPT-6 maximum.

The repository’s current `RESULTS.md` also records that the historical P26 `You cannot modify this task` failure was **authorization/context specific**: a later update succeeded from another authorized context, while R-series and other IDs were denied in a different context. The legitimate workaround is the task’s owning authorized context or platform support; there is no worker-level bypass and creating a duplicate task is prohibited. No scheduler modification was attempted here.

## 16. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  run_id: 20260917T1022Z_i0077_infinite_parabolic_combs_18
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8 / I0077"
  target: "generalize Theorem 4.3 from parabolic regions to genuinely distinct nonparabolic space-time shape families"
  fixed_metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem, modulo frozen trivial equivalences"
  value_before: 17
  value_after: 18
  movement: true
  status: PARTIAL
  unchanged_count: 0
  methods:
    - 7
    - 13
    - 21
  new_family: "unbounded infinite parabolic combs with countably many bounded normalized components"
  theorem_id: I0077-R07-T19
  theorem_summary: "For a closed normalized cross-section whose connected components are all bounded: if every nondegenerate component has OU exponent >1, no FBM is eventually confined; if one bounded interval component has exponent <1, a decomposable FBM is eventually confined; if that component contains 0, pointwise confinement follows."
  canonical_example: "D*=union_{k in Z}[3k-1/4,3k+1/4]"
  exact_self_check: "PASS; uniform rational lower bound 71/4 using pi^2>9"
  exact_evidence:
    - "artifacts/R07/20260917T1022Z_infinite_comb_check.py @ b43d174d53082c720ec634777c727aa876b1cfa7"
    - "artifacts/R07/20260917T1022Z_infinite_comb_check.out @ 9c64e6402241b209f50d763a35435f7e6c5c13c4"
  ownership: "R07 exclusive provisional reservation; shared claim remains PENDING_ADMISSION"
  prior_art: "bounded dated search; Bhamidi--Evans--Peled--Ralph disconnected-state Brownian motion is related but a different process notion; novelty UNVERIFIED"
  audits:
    p26: missing
    other_track: missing
  closure: false
  delivery: "private GitHub only"
```
